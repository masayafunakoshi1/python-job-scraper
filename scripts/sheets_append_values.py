#accessgooglesheetsapi@job-applications-script.iam.gserviceaccount.com

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def append_values(data):
    try:
        SERVICE_ACCOUNT_FILE = 'credentials.json'
        credentials = service_account.Credentials.from_service_account_file(
            filename=SERVICE_ACCOUNT_FILE
        )

        service_sheets = build('sheets', 'v4', credentials=credentials)

        GOOGLE_SHEETS_ID = '14QzRhFTzHDxWTgHpXhUL20qWGh8aq4jKewrIASmvxMs'

        worksheet_name='2nd-run Applications(8-2022)!'
        cell_range = 'A1:G1'
        values = [
            [
                data['date'], data['result'], data['company_name'], data['position'], data['url'], data['location']
            ]
        ]

        body = {
            'values': values
        }

        request = service_sheets.spreadsheets().values().append(
            spreadsheetId=GOOGLE_SHEETS_ID, 
            range=worksheet_name + cell_range,
            valueInputOption='USER_ENTERED',
            insertDataOption='INSERT_ROWS', 
            body=body
            )
        response = request.execute()
        print("SUCCESSFULLY INPUTTED DATA: ")
        print(response)
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

