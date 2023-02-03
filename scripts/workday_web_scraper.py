import requests
from bs4 import BeautifulSoup
from datetime import date
import os.path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from sheets_append_values import append_values


#insert console inputted URL logic here
# URL = "https://www.linkedin.com/jobs/view/3451031538/?alternateChannel=search&refId=Pn3zSJd09WKgEGmIwhjSrg%3D%3D&trackingId=dadK7Hxc%2FQ65gAzJMnnnyA%3D%3D"
# URL = "https://www.linkedin.com/jobs/view/3457349697/?alternateChannel=search&refId=Pn3zSJd09WKgEGmIwhjSrg%3D%3D&trackingId=X4avWcEW%2F88OV1XMvw8Xkg%3D%3D&trk=d_flagship3_job_details"

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

    ## Setup chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')

    options.binary_location = "/usr/bin/google-chrome-stable"
    # Choose Chrome Browser
    browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)

    sleep(5)

    # Get the page
    browser.get("https://google.com")

    if browser.title == "Google":
        print("Google page is loaded successfully")
    else:
        print("Failed to load Google page")

    # Get page
    # browser.get("https://google.com")




    # options = Options()
    # # options.binary_location = "/mnt/c/'Program Files'/BraveSoftware/Brave-Browser/application/brave"
    # # options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    # options.binary_location = "/mnt/c/'Program Files'/Google/Chrome/Application/chrome"

    # s = Service("/~/chromedriver")


    # driver = webdriver.Chrome(service = s, options = options)
    # driver.get('https://google.com')


    # pageinfo = requests.get(url)
    # time.sleep(5)

    # soup = BeautifulSoup(pageinfo.text, "html.parser")

    # html_data_info = soup.find(class_="css-7papts")
    # print(html_data_info)


    # title_info_splitter(html_title, url)
    
    # #append onto google docs spreadsheet
    # append_values(docs_info)



