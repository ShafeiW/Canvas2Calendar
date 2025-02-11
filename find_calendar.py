from googleapiclient.discovery import build
from google.oauth2 import service_account
from config import GOOGLE_CREDENTIALS_FILE

# Authenticate
SCOPES = ["https://www.googleapis.com/auth/calendar"]
creds = service_account.Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
service = build("calendar", "v3", credentials=creds)

# Fetch and print all available calendars
calendar_list = service.calendarList().list().execute()
for calendar in calendar_list["items"]:
    print(f"Calendar Name: {calendar['summary']}, ID: {calendar['id']}")
