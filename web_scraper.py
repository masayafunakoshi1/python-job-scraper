import requests
from bs4 import BeautifulSoup
from datetime import date

#insert console inputted URL logic here
URL = 'https://www.linkedin.com/jobs/view/3451031538/?alternateChannel=search&refId=Pn3zSJd09WKgEGmIwhjSrg%3D%3D&trackingId=dadK7Hxc%2FQ65gAzJMnnnyA%3D%3D'
pageinfo = requests.get(URL)

soup = BeautifulSoup(pageinfo.text, 'html.parser')
print(soup.title)

html_title = soup.title.string

#stores info that will go into google docs
docs_info = {
    "date_of_application": date.today().strftime("%m/%d/%y"),
    "result": "Pending",
    "name_of_company": "",
    "position": "",
    "url": "",
    "location": "",
}

# def title_info_splitter(title):
#     edited = title.split('hiring')
#     edited.split('in')
#     print(edited)

# title_info_splitter(html_title)


