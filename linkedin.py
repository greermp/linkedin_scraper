""" filename: script.py """


# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time 

# defining new variable passing two parameters
writer = csv.writer(open('afile.csv', 'w'))

# writerow() method to the write to the file object
#writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])
writer.writerow(["test"])
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('chromedriver.exe')
print("Good")

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_id("session_key")

# send_keys() to simulate key strokes
username.send_keys("greermp@gmail.com")

# sleep for 0.5 seconds
time.sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_id('session_password')

# send_keys() to simulate key strokes
password.send_keys('qazwsx321')
time.sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()
# time.sleep(6)
# print ("searching")
# driver.maximize_window
# print(driver.find_elements_by_id("ember14"))
# search = driver.find_element_by_class_name('global-nav__search-typeahead search-global-typeahead ember-view')
# print(search.find_elements())
driver.get('https:www.google.com')
time.sleep(3)


names = ["Max Greer", "Adam Greer"]
for name in names :
    query = "site:linkedin.com/in/ AND  '" + name + "' AND 'Virginia'"
    print (query)
    search_query = driver.find_element_by_name('q')
    search_query.send_keys(query)
    time.sleep(0.5)
    
    search_query.send_keys(Keys.RETURN)
    time.sleep(3)
