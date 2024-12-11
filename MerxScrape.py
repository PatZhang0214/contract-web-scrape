from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Optional, for automatic driver management

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# or specify the path directly
# driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Navigate to the website
driver.get('https://www.merx.com/public/solicitations/open?keywords=RPAs&publishDate=&solSearchStatus=openSolicitationsTab&sortBy=&sortDirection=')
# Example: Extract some data
title = driver.title
h1 = driver.find_elements("class name", 'rowTitle')
links = driver.find_elements("class name", "mets-command-link")
print(f'Title of the page: {title}')

for i in h1:
    print(i.text)

for i in links:
    if(i.get_attribute('href').__contains__("https://www.merx.com/public/supplier/interception/")):
        print(i.get_attribute('href'))
# Close the driver
driver.quit()
