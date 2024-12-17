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

driver.get("https://www.globaltenders.com/government-tenders-canada#tenderPagination")
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

# def fetchContractsOnPage(keywords: list[str]):


# def fetchContracts(keywords: list[str]):

# def constructParsedInformation(d: dict):
#     openTitles = getOpens()
#     links = getLinks()
#     try:
#         for i in range(len(openTitles)):
#             d[openTitles[i]] = links[i]
#     except Exception as e:
#         print("\nError")

# def getOpens():
#     titles = []
#     h1 = driver.find_elements("class name", 'rowTitle')
#     for i in h1:
#         titles.append(i.text)
#     print("\nThere are " + str(len(titles)) + " opens")
#     return titles

# def getLinks():
#     links = []
#     l = driver.find_elements("class name", "mets-table-row")
#     for tr in l:
#         aTag = tr.find_elements("tag name", "a")
#         links.append(aTag[0].get_attribute('href'))
#         print(aTag[0].get_attribute('href'))
#     print("\nThere are " + str(len(links)) + " links")
#     return links

# def getAllLinks():
#     parsedDict = {}
#     constructParsedInformation(parsedDict)
#     print(parsedDict)
#     while len(driver.find_elements(By.CLASS_NAME, "next")) > 0:
#         try:
#             time.sleep(1)
#             link = driver.find_element(By.CLASS_NAME, "next")
#             driver.execute_script("arguments[0].scrollIntoView();", link)
#             link.click()
#             constructParsedInformation(parsedDict)
#             print("Clicked on the link successfully.")
#         except Exception as e:
#             print(f'Error: {e}')
#             break
#     time.sleep(1)
#     print(parsedDict)
#     return parsedDict

# def getAllParsedInfo(keywords: list[str]):
#     parsedDicts = {}
#     for keyword in keywords:
#         driver.get("https://www.merx.com/public/solicitations/open?keywords="+keyword+"&publishDate=&solSearchStatus=openSolicitationsTab&sortBy=&sortDirection=")
#         parsedDicts[keyword] = getAllLinks()

#     print(parsedDicts)
#     driver.quit()
#     return parsedDicts

if __name__ == "__main__":
    getTitle()
    getLink()
