# Import the necessary libraries
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import os

# Authenticate and build the service
creds = None
scopes = ['https://www.googleapis.com/auth/calendar.readonly']

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = google.oauth2.credentials.Credentials.from_authorized_user_file('token.json', scopes)
else:
    flow = google.oauth2.flow.InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('calendar', 'v3', credentials=creds)

# Call the Calendar API and get a list of calendars
calendar_list = service.calendarList().list().execute()

# Print the calendar IDs and names
for calendar in calendar_list['items']:
    print(calendar['id'], calendar['summary'])
