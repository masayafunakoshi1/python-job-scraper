import requests
from bs4 import BeautifulSoup
from datetime import date
from sheets_append_values import append_values

#insert console inputted URL logic here
# URL = 'https://www.linkedin.com/jobs/view/3451031538/?alternateChannel=search&refId=Pn3zSJd09WKgEGmIwhjSrg%3D%3D&trackingId=dadK7Hxc%2FQ65gAzJMnnnyA%3D%3D'
# URL = 'https://www.linkedin.com/jobs/view/3457349697/?alternateChannel=search&refId=Pn3zSJd09WKgEGmIwhjSrg%3D%3D&trackingId=X4avWcEW%2F88OV1XMvw8Xkg%3D%3D&trk=d_flagship3_job_details'
print("Input job URL: ")
URL = str(input())

pageinfo = requests.get(URL)

soup = BeautifulSoup(pageinfo.text, 'html.parser')
html_title = soup.title.string

#stores info that will go into google docs
docs_info = {
    "date": date.today().strftime("%m/%d/%y"),
    "result": "Pending",
    "company_name": "",
    "position": "",
    "url": URL,
    "location": "",
}

def title_info_splitter(title):
    all_info_split = title.split('hiring')
    docs_info["company_name"] = all_info_split[0]

    role_and_location_info = all_info_split[1].split(' in ')
    role_info = role_and_location_info[0]
    docs_info["position"] = role_info

    location_info = role_and_location_info[1].split('|')
    location_info = location_info[0]
    docs_info["location"] = location_info
    print("Parsed Info: ", docs_info)

title_info_splitter(html_title)

#append onto google docs spreadsheet
append_values(docs_info)



