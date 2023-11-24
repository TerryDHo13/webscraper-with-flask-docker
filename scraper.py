from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def scraper():
    #the url of the website
    URL = "https://www.scrapethissite.com/pages/simple/"

    #additional settings for chrome options.
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    #setting a service for the driver.
    service = ChromeService(executable_path=ChromeDriverManager().install())

    #creating an instance of a driver.
    driver = webdriver.Chrome(options=options, service=service)

    #get the url of the website to be scraped.
    driver.get(URL)

    #get result from the website
    result = driver.find_elements(By.CLASS_NAME, "country-name")
    print(f"I scraped: {URL}")
    print(f"Number of items in the list: {len(result)}" )
    number = len(result)

    #quits the webdriver
    driver.quit()

    #returns the number of items in the list
    return number

if __name__ == '__main__':
    scraper()
