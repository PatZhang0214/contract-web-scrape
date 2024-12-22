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
# Example: Extract some data
title = driver.title
print(title)

def getTitle():
    titles = []
    items = driver.find_elements(By.CSS_SELECTOR, "div[class='tender-wrap']")
    for i in items:
        t = i.find_element(By.CSS_SELECTOR, "span[itemprop='name']")
        titles.append(t.text)
    print(titles)
    print("\nThere are " + str(len(titles)) + " opens")
    return titles

def getLink():
    links = []
    items = driver.find_elements(By.CSS_SELECTOR, "div[class='tender-wrap']")
    for i in items:
        t = i.find_element(By.CSS_SELECTOR, "a[title='View Detail']")
        links.append(t.get_attribute('href'))
    print(links)
    return links

def fetchContractsOnPage(keywords: list[str], parsedDict: dict):
    links = getLink()
    titles = getTitle()
    try:
        for i in range(len(titles)):
            for keyword in keywords:
                if titles[i].upper() in keyword.upper():
                    itemTuple = (titles[i], links[i])
                    parsedDict[keyword].append(itemTuple)
    except Exception as e:
        print(e)

def fetchContracts(keywords: list[str]):
    driver.get("https://www.globaltenders.com/government-tenders-canada#tenderPagination")
    parsedDict = {}
    fetchContractsOnPage(keywords, parsedDict)
    title = 20
    while len(driver.find_elements(By.CSS_SELECTOR, "div[class='tender-wrap']")) > 0:
        try:
            time.sleep(1)
            link = driver.find_element(By.CSS_SELECTOR, "a[title='"+str(title)+"']")
            driver.execute_script("arguments[0].click();", link)
            time.sleep(4)
            fetchContractsOnPage(keywords, parsedDict)
            print("Clicked on the link successfully.")
            title += 20
        except Exception as e:
            print(f'Error: {e}')
            break
    driver.close()
    return parsedDict

if __name__ == "__main__":
    keywords = ["Drones", "UAV", "UAVs", "RPA", "RPAS", "Remotely Piloted Aircraft Systems",
                "EVTOL", "VTOL", "Electric Fixed-wing Aircraft", "Heavy-lift Drones", "DJI",
                  "Dajiang Industries", "Mavic 3", "Matrice 350", "M3E", "M3M", "M30", "M30T",
                    "M350", "Multispectral", "Thermal", "Night Vision"]
    fetchContracts(keywords)
