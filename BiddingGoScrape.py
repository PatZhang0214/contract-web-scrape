from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Optional, for automatic driver management
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# or specify the path directly
# driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Navigate to the website
# Example: Extract some data
title = driver.title

def changePage(keyword: str):
    link = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search by Keyword']")
    link.clear()
    link.send_keys(keyword)
    link.send_keys(Keys.RETURN)
    time.sleep(2)

def forwardPage():
    nextPage = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next page']")
    attr = nextPage.get_attribute("disabled")
    print(nextPage)
    if attr is None:
        driver.execute_script("arguments[0].scrollIntoView();", nextPage)
        print("Scrolling")
        time.sleep(1)
        nextPage.click()
        return True
    else:
        return False

def scrapePage():
    time.sleep(1)
    links = []
    rawLinks = driver.find_elements(By.CSS_SELECTOR, "a[href='javascript:void(0);']")
    for rl in rawLinks:
        if "OXOXOXOX" in rl.text:
            links.append(rl.text)
    print(links)
    forwarded = forwardPage()
    time.sleep(2)
    print(forwarded)
    return links

def scrapeTerm(keyword: str, parsedDict: dict):
    parsedDict[keyword] = []
    changePage(keyword)
    parsedDict[keyword].extend(scrapePage())
    while forwardPage():
        parsedDict[keyword].extend(scrapePage())
    print(parsedDict)

def scrapeAllTerms(keywords: list[str]):
    driver.get("https://www.biddingo.com/search?k=")
    parsedDict = {}
    for keyword in keywords:
        scrapeTerm(keyword, parsedDict)
    print(parsedDict)
    driver.close()
    return parsedDict

if __name__ == "__main__":
    keywords = ["Drones", "UAV", "UAVs", "RPA", "RPAS", "Remotely Piloted Aircraft Systems",
                "EVTOL", "VTOL", "Electric Fixed-wing Aircraft", "Heavy-lift Drones", "DJI",
                  "Dajiang Industries", "Mavic 3", "Matrice 350", "M3E", "M3M", "M30", "M30T",
                    "M350", "Multispectral", "Thermal", "Night Vision"]
    # keywords = ["Drones", "UAV", "UAVs", "RPA", "RPAS", "Remotely Piloted Aircraft Systems",
    #             "EVTOL", "VTOL", "Electric Fixed-wing Aircraft"]
    # keywords = ["truck"]
    parsed = scrapeAllTerms(keywords)

