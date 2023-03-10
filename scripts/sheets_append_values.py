#accessgooglesheetsapi@job-applications-script.iam.gserviceaccount.com
import os
from dotenv import load_dotenv

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

def type_checker(data):
    if isinstance(data['location'], str):
        return data['location']  
    else:
        return " ".join(data['location'])

def append_values(data):
    try:
        SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
        credentials = service_account.Credentials.from_service_account_file(
            filename=SERVICE_ACCOUNT_FILE
        )

        service_sheets = build('sheets', 'v4', credentials=credentials)

        GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")

        worksheet_name='2nd-run Applications(8-2022)!'
        cell_range = 'A1:G1'
        values = [
            [
                data['date'], data['result'], data['company_name'], data['position'], data['url'], type_checker(data)
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
        print("\n")
        print("SUCCESSFULLY INPUTTED DATA: ")
        print(response)
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

