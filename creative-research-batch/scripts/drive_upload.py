"""Upload a file into a Google Drive folder, converting to a Google type on the way in.

One-time setup (about ten minutes of clicking):
  1. https://console.cloud.google.com  ->  New project (any name).
  2. APIs & Services -> Library -> enable "Google Drive API".
  3. APIs & Services -> OAuth consent screen -> External -> add your own
     Gmail address under Test users. Nothing else needs filling in.
  4. APIs & Services -> Credentials -> Create credentials -> OAuth client ID
     -> Application type "Desktop app" -> Create -> Download JSON.
  5. Save that JSON as  scripts/client_secret.json  (next to this file).

First run opens a browser tab asking you to approve Drive access. After you
click through, a token.json is written next to this file and every later run
is silent. Both JSON files are gitignored.

Usage:
  python scripts/drive_upload.py --parent FOLDER_ID --file path/to/Batch.xlsx
  python scripts/drive_upload.py --parent FOLDER_ID --file brief.html --title "My Brief"

.xlsx and .csv become Google Sheets, .html/.docx/.md become Google Docs, unless
--no-convert is passed. Prints the new file's link.
"""
import argparse
import mimetypes
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

HERE = Path(__file__).resolve().parent
CLIENT_SECRET = HERE / "client_secret.json"
TOKEN = HERE / "token.json"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

GOOGLE_TYPES = {
    ".xlsx": "application/vnd.google-apps.spreadsheet",
    ".csv": "application/vnd.google-apps.spreadsheet",
    ".html": "application/vnd.google-apps.document",
    ".htm": "application/vnd.google-apps.document",
    ".docx": "application/vnd.google-apps.document",
    ".md": "application/vnd.google-apps.document",
    ".txt": "application/vnd.google-apps.document",
}


def credentials() -> Credentials:
    creds = None
    if TOKEN.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if not CLIENT_SECRET.exists():
            sys.exit(
                f"Missing {CLIENT_SECRET}. Follow the setup steps at the top of this file."
            )
        flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
        creds = flow.run_local_server(port=0)
    TOKEN.write_text(creds.to_json())
    return creds


def upload(path: Path, parent: str, title: str | None, convert: bool) -> dict:
    service = build("drive", "v3", credentials=credentials())
    source_mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    if path.suffix.lower() == ".xlsx":
        source_mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    meta = {"name": title or path.stem, "parents": [parent]}
    target = GOOGLE_TYPES.get(path.suffix.lower()) if convert else None
    if target:
        meta["mimeType"] = target

    media = MediaFileUpload(str(path), mimetype=source_mime, resumable=False)
    return (
        service.files()
        .create(body=meta, media_body=media, fields="id,name,mimeType,webViewLink")
        .execute()
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--parent", required=True, help="Drive folder id to upload into")
    ap.add_argument("--file", required=True, type=Path, help="Local file to upload")
    ap.add_argument("--title", help="Name in Drive (default: filename without extension)")
    ap.add_argument("--no-convert", action="store_true", help="Keep the original format instead of converting to a Google type")
    args = ap.parse_args()

    if not args.file.exists():
        sys.exit(f"No such file: {args.file}")
    result = upload(args.file, args.parent, args.title, convert=not args.no_convert)
    print(f"{result['name']}  ({result['mimeType']})")
    print(result["webViewLink"])


if __name__ == "__main__":
    main()
