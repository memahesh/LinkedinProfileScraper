# LinkedinProfileScraper

## Requirements :
    1. Python2.7
    2. ChromeDriver
    3. The following modules :
        - Selenium : Portable software-testing framework for web applications
        - bs4      : Helps in easy code parsing of webpage
        - json     : Linkedin webpages requires json handling
        - csv      : To append your data to a csv
        - random   : Handling random numbers

## Brief Desription :
    This scraper gives you the basic information and contact info of the profile(if present) on providing the profile url.

## Files :
    linkedin_profile.py    : Python code to scrape the linkedin data.
    data.csv               : Data is stored into this file.
    chromedriver.exe       : ChromeDriver is a separate executable that WebDriver uses to control Chrome.
                             (There are drivers available for other browsers too. However, I am using ChromeDriver.)
Visit [here](http://docs.seleniumhq.org/download/) to download drivers for other browsers and know more about Selenium.

## How to use :

- **Step 1:**

Run the python code in your terminal or command prompt (preferably).

```
cd <file path to the location>
python <filename>
```

- **Step 2:**

You will be asked to give your Linkedin Credentials. It is entirely safe to give your credentials. No one is storing         them.

```
Linkedin Username : username
Linkedin Password : password
```

After logging in, there will be a prompt for profile link

```
Paste the profile link : linkedinprofilelink
```

- **Step 3:**

    i. Copy and Paste (Ctrl+Shift+V for cmd or terminal) the profile link.
    
    ii. The basic description of profile and contact info (if present) will be stored in data.csv

## Other Details :
    1. Continue the loop to scrape as many profiles as you wish in a single login.
    2. A new row is added for every new profil scraped. So, no need to worry for the loss of data.
    3. Since, it's a Selenium webDriver system, you can see whatever is happening with the browser.
