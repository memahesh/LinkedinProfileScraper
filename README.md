# LinkedinProfileScraper

Requirements :
1. Python2.7
2. The following modeules (selenium, bs4, json, csv, random)

Brief Desription :
This scraper gives you the basic information and contact info of the profile(if present) on providing the profile url.

Files :
linkedin_profile.py    : Python code to scrape the linkedin data.
data.csv               : Data is stored into this file

How to use :
Step 1: 
Run the python code in your terminal or command prompt (preferably).
Step 2: 
You will be asked to give your Linkedin Credentials. It is entirely safe to give your credentials. No one is storing them.
Step 3:
Copy and Paste (Ctrl+Shift+V for cmd or terminal) the profile link.
The basic description of profile and contact info (if present) will be stored in data.csv

Other Details :
1. Continue the loop to scrape as many profiles as you wish in a single login.
2. A new row is added for every new profil scraped. So, no need to worry for the loss of data.
3. Since, it's a Selenium webDriver system, you can see whatever is happening with the browser.
