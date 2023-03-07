from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
import shutil
import time



def open_driver():
    # wherever you installed geckodriver
    driver_path = R"/usr/local/bin/geckodriver"

    # which firefox
    firefox_path = R"/bin/firefox"

    options = Options()
    options.add_argument('-headless')

    # create a driver
    options.binary_location = firefox_path
    service = Service(executable_path=driver_path)
    driver = webdriver.Firefox(options=options, service=service)

    return driver


def get_download(driver, ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/history"
    driver.get(url)

    time.sleep(2)

    close = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
    close.click()

    dropdown = driver.find_element(By.XPATH, "//div[@role='button'][@aria-label='']")
    dropdown.click()

    max = driver.find_element(By.XPATH, "//button[@data-value='MAX']")
    max.click()

    apply = driver.find_element(By.XPATH, "//span[text()='Apply']")
    apply.click()

    download = driver.find_element(By.XPATH, "//a[@download='" + ticker + ".csv']")
    download.click()


def move_download(ticker):

    time.sleep(4)
    src_path = r"/home/zach/Downloads/" + ticker + ".csv"
    dst_path = r"downloads"
    shutil.move(src_path, dst_path)


def main():
    driver = open_driver()

    ticker = "F"
    get_download(driver, ticker)
    move_download(ticker)

    driver.close()


if __name__ == "__main__":
    main()