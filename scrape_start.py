import sys
import re

sys.path.insert(0, "/mnt/d/coding/programming_projects/Extra-projects/python-job-scraper/scripts")
import linkedin_web_scraper
import greenhouse_web_scraper

print("Input job URL: ")
URL = str(input())

# search for LinkedIn, Greenhouse, or Workday in URL, determine which script to run
if re.search("linkedin", URL):
    linkedin_web_scraper.scraping_handler(URL)
elif re.search("greenhouse", URL):
    greenhouse_web_scraper.scraping_handler(URL)
