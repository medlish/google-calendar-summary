# Import the necessary libraries
import os
import datetime
import google.auth
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Set the calendar ID and time range
calendar_id = '6l0e6i50kc7loautpstekk4ec0@group.calendar.google.com'
start_date = datetime.datetime.utcnow()
end_date = start_date + datetime.timedelta(weeks=4)

# Authenticate and build the service
creds = None
scopes = ['https://www.googleapis.com/auth/calendar.readonly']

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', scopes)
else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('calendar', 'v3', credentials=creds)

# Call the Calendar API and get the events for the specified time range
events_result = service.events().list(calendarId=calendar_id, timeMin=start_date.isoformat()+'Z', timeMax=end_date.isoformat()+'Z', singleEvents=True, orderBy='startTime').execute()
events = events_result.get('items', [])

# Print the events line by line
if not events:
    print('No events found for the next 4 weeks.')
else:
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_time = datetime.datetime.fromisoformat(start).strftime('%a, %d.%m. %H:%M')
        print(f'{start_time} {event["summary"]}')