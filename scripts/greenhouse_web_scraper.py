import requests
from bs4 import BeautifulSoup
from datetime import date
from sheets_append_values import append_values

#insert console inputted URL logic here
# URL = 'https://www.linkedin.com/jobs/view/3451031538/?alternateChannel=search&refId=Pn3zSJd09WKgEGmIwhjSrg%3D%3D&trackingId=dadK7Hxc%2FQ65gAzJMnnnyA%3D%3D'
# URL = 'https://www.linkedin.com/jobs/view/3457349697/?alternateChannel=search&refId=Pn3zSJd09WKgEGmIwhjSrg%3D%3D&trackingId=X4avWcEW%2F88OV1XMvw8Xkg%3D%3D&trk=d_flagship3_job_details'

#stores info that will go into google docs
docs_info = {
    "date": date.today().strftime("%m/%d/%y"),
    "result": "Pending",
    "company_name": "",
    "position": "",
    "url": "",
    "location": "",
}

def title_info_splitter(title, url):
    docs_info["url"] = url
    #adjust accordingly to greenhouse websites
    print("Parsed Info: ", docs_info)

#main function
def scraping_handler(url):
    print("GREEN HOUSE")
    # pageinfo = requests.get(url)

    # soup = BeautifulSoup(pageinfo.text, 'html.parser')
    # html_title = soup.title.string

    # title_info_splitter(html_title, url)
    
    # #append onto google docs spreadsheet
    # append_values(docs_info)



