import requests
from bs4 import BeautifulSoup
from datetime import date
import os.path

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

def html_info_splitter(driver, url):
    #URL
    docs_info["url"] = url

    #Company Name
    twitter_html_element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "css-1bc6tqb"))
    )
    twitter_handle = twitter_html_element.get_attribute("href").split("/")
    docs_info["company_name"] = twitter_handle[3]

    # #Position
    title_html_element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "css-7papts"))
    )
    docs_info["position"] = title_html_element.text

    #Location
    location_html_element = driver.find_element(By.CLASS_NAME, "css-k008qs")
    child_elements = location_html_element.find_elements(By.CLASS_NAME, "css-129m7dg")

    #change into readable locations in a list
    for i, el in enumerate(child_elements):
        child_elements[i] = el.text
    
    docs_info["location"] = child_elements


# main function
def scraping_handler(url):
    # Use selenium for headless browser
    ## Setup chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')

    options.binary_location = "/usr/bin/google-chrome-stable"
    # Choose Chrome Browser
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)

    # Get the page
    driver.get(url)

    if driver.current_url == url:
        print("Page is loaded successfully")
    else:
        print("Failed to load page")

    html_info_splitter(driver, url)

    driver.quit()

    append_values(docs_info)



