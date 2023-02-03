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

#main function
def scraping_handler(url):
    print("GREEN HOUSE URL")
    docs_info["url"] = url
    
    pageinfo = requests.get(url)

    soup = BeautifulSoup(pageinfo.text, "html.parser")
    html_string_position = soup.find(class_="app-title").string.strip()
    html_string_location = soup.find(class_="location").string.strip()

    html_string_company = soup.find(class_="company-name").string.split(" at ")
    html_string_company = html_string_company[1].split("\n")
    html_string_company = html_string_company[0]

    docs_info["company_name"] = html_string_company
    docs_info["position"] = html_string_position
    docs_info["location"] = html_string_location
    
    #append onto google docs spreadsheet
    append_values(docs_info)



