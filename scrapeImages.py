# Resources:
# https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

print("run imports...")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3
import argparse
import urllib.request

print("define program variables and open google images...")
searchterm = 'calvin_klein_dresses' # will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome()
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
counter = 0
succounter = 0

print("start scrolling to generate more images on the page...")
# 500 time we scroll down by 10000 in order to generate more images on the website
for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

print("start scraping ...")
for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:", x.get_attribute('src'))

    img = x.get_attribute('src')
    new_filename = "image"+str(counter)+".jpg"

    try:
        path = r'C:\Users\Asrita\Downloads\shein_dresses\calvin_klein_dresses'
        path += new_filename
        urllib.request.urlretrieve(img, path)
        succounter += 1
    except Exception as e:
        print(e)

print(succounter, "pictures succesfully downloaded")
browser.close()
