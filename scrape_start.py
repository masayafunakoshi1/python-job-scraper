import sys
import re
import subprocess
import os

CURR_DIR = os.getcwd()
sys.path.insert(0, f"{CURR_DIR}/scripts")
import linkedin_web_scraper
import greenhouse_web_scraper
import workday_web_scraper

print("Input job URL: ")
URL = str(input())

#quit out of program
if(URL == "quit" or URL == "q"):
    print("Great job! You got this!")
    sys.exit()
    
# search for LinkedIn, Greenhouse, or Workday in URL, determine which script to run
if re.search("linkedin", URL):
    linkedin_web_scraper.scraping_handler(URL)
elif re.search("greenhouse", URL):
    greenhouse_web_scraper.scraping_handler(URL)
elif re.search("workday", URL):
    workday_web_scraper.scraping_handler(URL)
else:
    print("Invalid URL, please try again.")

print("\n")

subprocess.run(["python3 scrape_start.py"], shell=True)