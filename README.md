# Python Job Scraper 
A Python-based web scraper that collects job information from various job sites and stores it in a Google Sheet.

## 🚀 Features 
- Scrapes job information from popular job sites including LinkedIn, Greenhouse, and Workday
- Utilizes <strong>
  <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">
  Beautiful Soup
  </a>
 </strong> and <strong>
  <a href="https://www.selenium.dev/">
  Selenium
  </a>
 </strong> for web scraping
- Stores the data in a Google Sheet using the Google Sheets API from Google Cloud
- The data is organized in a row divided by sections: Date of application, Result, Name of company, Position, Job posting, Location, and Resources.

## 🛠 Usage
The code is separated into several Python scripts, each focusing on a specific job site.
<br/>
<br/> 
To use, simply run the `scrape_start.py` script, insert a valid URL, and watch the magic happen!

### 👀 Keep in Mind: 
- Make sure to run `pip install -r requirments.txt`
- Use your own Google Sheets API account, create a service worker, and your own Google Sheet.<br/>
  Create a `.env` file like `example.env, insert the service worker JSON download file and Google Sheets ID.

#### Use this video as reference: https://www.youtube.com/watch?v=sVURhxyc6jE

## 🛰 Future Development
More job sites will be added in the future to increase the scope of the project.

## 🌠 Contributions
Contributions are always welcome! If you would like to contribute, please fork the repository and make the necessary changes. Submit a pull request for review and if approved, it will be merged.
