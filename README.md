# google-calendar-summary

read_calendar: 
Reads all events for the next 4 weeks from a specified google calendar and prints Weekday, Date Time Summary on console for each event.
Requires a credentials.json file which can be acquired from the google api dashboard (https://console.cloud.google.com/apis/dashboard). Create a project and under APIs and services -> Credentials create "OAuth 2.0 Client IDs". From there you can download the credentials.json.

On the first call of the program you may need to login. With a valid login, a token file is generated which is from there on read automatically so no further login is necessary.

Within the script you will find a variable calendar_id which defines which calendar is read. If you wish to use any other calendar than the primary one, you need to find out the calendar id, whcih you can do with the list_calendars script.

list_calendars:
List all calendars accessible through account in the format "id name".
