from selenium import webdriver
from bs4 import BeautifulSoup
import json
import csv
from random import randint


def getData(link, driver):

    driver.get(link)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(randint(0,9))
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    json_alldata = soup.find_all("code")
    for x in json_alldata:
        try:
            json_data = json.loads(x.text)
        except ValueError:
            print "123"
        if "data" in json_data:
            if "$type" in json_data["data"]:
                if json_data["data"]["$type"] == "com.linkedin.voyager.identity.profile.ProfileView":
                    break

    name = headline = industry = location = summary = vanity_url = website = email = phone = "None"
    for x in json_data["included"]:
        if x["$type"] == "com.linkedin.voyager.identity.profile.Profile":
            try :
                name = x["firstName"] + " " + x["lastName"]
            except:
                print "No Name"

            try :
                headline = x["headline"]
            except:
                print "No Headline"

            try :
                industry = x["industryName"]
            except:
                print "No Industry"

            try :
                location = x["locationName"]
            except:
                print "No Location"

            try :
                summary = x["summary"]
            except:
                print "No Summary"
    driver.find_element_by_class_name("contact-see-more-less").click()
    new_html = driver.page_source
    soup = BeautifulSoup(new_html, "html.parser")

    try:
        vanity_url = soup.find_all("section", {"class": "ci-vanity-url"})
        vanity_url = vanity_url[0].find_all("div", {"class": "pv-contact-info__contact-item"})
        vanity_url = vanity_url[0].text
    except:
        print "No vanity_url"

    try:
        website = soup.find_all("section", {"class": "ci-websites"})
        website = website[0].find_all("div", {"class": "pv-contact-info__action"})
        website = website[0].text
    except:
        print "No website link"

    try:
        email = soup.find_all("section", {"class": "ci-email"})
        email = email[0].find_all("span", {"class": "pv-contact-info__contact-item"})
        email = email[0].text
    except:
        print "No email"

    try:
        phone = soup.find_all("section", {"class": "ci-phone"})
        phone = phone[0].find_all("div", {"class": "pv-contact-info__contact-item"})
        phone = phone[0].text
    except:
        print "No Mobile Number"

    with open('data.csv', 'ab') as f:
        writer = csv.writer(f)
        writer.writerow([name.encode("ascii", "ignore"), headline.encode("ascii", "ignore"), industry.encode("ascii", "ignore"), location.encode("ascii", "ignore"), summary.encode("ascii", "ignore"), vanity_url, website, email, phone])



def main():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=210.38.1.139:8080')
    username = raw_input("Linkedin Username :")
    password = raw_input("Linkedin Password :")
    driver = webdriver.Chrome('/home/mahesh/PycharmProjects/Scrapers/linkedin/chromedriver', chrome_options=chrome_options)
    driver.get('https://www.linkedin.com/')
    driver.set_page_load_timeout(30)
    driver.find_element_by_name("session_key").send_keys(username)
    driver.find_element_by_name("session_password").send_keys(password)
    driver.find_element_by_id("login-submit").click()
    c = 'y'
    while (c=='y'):
        anchor = raw_input("Copy/Paste the profile links :")
        getData(anchor, driver)
        c = raw_input("Press 'y' to continue: ")


if __name__ == '__main__':
    main()

