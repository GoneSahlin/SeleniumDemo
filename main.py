from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
import shutil
import time



def open_driver():
    # install geckodriver
    # path to geckodriver
    

    # path to firefox executable
    

    # create options
    

    # set binary location
    

    # create a service object and set executable_path to driver_path
    

    # create a driver


    # return driver

    pass


def get_download(driver, ticker):
    # url
    url = "https://finance.yahoo.com/quote/" + ticker + "/history"

    # open page


    # wait for page to load


    # close pop-up if it occurs
    

    # click on dropdown
    

    # click on max
    

    # click on apply
    

    # click on download
    

    # move download
    
    pass


def main():
    driver = open_driver()

    get_download(driver, "F")
    get_download(driver, "AAPL")

    # close the driver
    


if __name__ == "__main__":
    main()
