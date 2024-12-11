from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Optional, for automatic driver management
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# or specify the path directly
# driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Navigate to the website
driver.get('https://www.merx.com/public/solicitations/open?keywords=thermal&publishDate=&solSearchStatus=openSolicitationsTab&sortBy=&sortDirection=')
# Example: Extract some data
title = driver.title
# h1 = driver.find_elements("class name", 'rowTitle')
# links = driver.find_elements("class name", "mets-command-link")
# print(f'Title of the page: {title}')

# for i in h1:
#     print(i.text)

# for i in links:
#     if(i.get_attribute('href').__contains__("https://www.merx.com/public/supplier/interception/")):
#         print(i.get_attribute('href'))

# try:
#     link = driver.find_element(By.CLASS_NAME, "next")
#     driver.execute_script("arguments[0].scrollIntoView();", link)
#     link.click()
#     print("Clicked on the link successfully.")
# except Exception as e:
#     print(f'Error: {e}')

# Close the driver
# time.sleep(10)

def constructParsedInformation(d: dict):
    openTitles = getOpens()
    links = getLinks()
    try:
        for i in range(len(openTitles)):
            d[openTitles[i]] = links[i]
    except Exception as e:
        print("\nError")

def getOpens():
    titles = []
    h1 = driver.find_elements("class name", 'rowTitle')
    for i in h1:
        titles.append(i.text)
    print("\nThere are " + str(len(titles)) + " opens")
    return titles

def getLinks():
    links = []
    l = driver.find_elements("class name", "mets-table-row")
    for tr in l:
        aTag = tr.find_elements("tag name", "a")
        links.append(aTag[0].get_attribute('href'))
        print(aTag[0].get_attribute('href'))
    print("\nThere are " + str(len(links)) + " links")
    return links

if __name__ == "__main__":
    parsedDict = {}
    constructParsedInformation(parsedDict)
    print(parsedDict)
    while len(driver.find_elements(By.CLASS_NAME, "next")) > 0:
        try:
            time.sleep(3)
            link = driver.find_element(By.CLASS_NAME, "next")
            driver.execute_script("arguments[0].scrollIntoView();", link)
            link.click()
            constructParsedInformation(parsedDict)
            print("Clicked on the link successfully.")
        except Exception as e:
            print(f'Error: {e}')
            break
    time.sleep(2)
    driver.quit()
    print(parsedDict)


