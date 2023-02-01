import importlib.util
import sys

sys.path.insert(0, "/mnt/d/coding/programming_projects/Extra-projects/python-job-scraper/scripts")
from linkedin_web_scraper import scraping_handler

print("Input job URL: ")
URL = str(input())

scraping_handler(URL)
