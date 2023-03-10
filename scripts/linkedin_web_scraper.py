import requests
from bs4 import BeautifulSoup
from datetime import date
from sheets_append_values import append_values

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
    print("LINKED IN URL")
    docs_info["url"] = url

    all_info_split = title.split('hiring')
    docs_info["company_name"] = all_info_split[0]

    role_and_location_info = all_info_split[1].split(' in ')
    role_info = role_and_location_info[0]
    docs_info["position"] = role_info

    location_info = role_and_location_info[1].split('|')
    location_info = location_info[0]
    docs_info["location"] = location_info
    print("Parsed Info: ", docs_info)

#main function
def scraping_handler(url):
    pageinfo = requests.get(url)

    soup = BeautifulSoup(pageinfo.text, "html.parser")
    html_title = soup.title.string
    # html_with_info = soup.find("body").find("").find(class_="jobs-unified-top-card ")
    # print(html_with_info)

    title_info_splitter(html_title, url)
    
    #append onto google docs spreadsheet
    append_values(docs_info)



