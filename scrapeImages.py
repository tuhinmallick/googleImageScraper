from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3
import argparse
import urllib.request

folderfs=r'C:\Users\name\Downloads\folder\calvin_klein_dresses' 
searchterm = 'calvin_klein_dresses' # this goes in the search query
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome() #keep the chrome webdriver in the same folder as this code
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
counter = 0
succounter = 0

#Click 'show more results' in the opened browser to get more images. Scrolls automatically only till then
for _ in range(200):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:", x.get_attribute('src'))

    img = x.get_attribute('src')
    new_filename = "image"+str(counter)+".jpg"

    try:
        
        path =  folderfs
        path += new_filename
        urllib.request.urlretrieve(img, path)
        succounter += 1
    except Exception as e:
        print(e)

print(succounter, "pictures succesfully downloaded")
browser.close()
