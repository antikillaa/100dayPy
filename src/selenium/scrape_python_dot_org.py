from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/staspeshkur/PycharmProjects/learn/src/selenium/chromedriver'

driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://www.python.org/')
dates = driver.find_elements(By.XPATH, "//div[@class='medium-widget event-widget last']/div/ul/li/time")
titles = driver.find_elements(By.XPATH, "//div[@class='medium-widget event-widget last']/div/ul/li/a")
events = {}

for i in range(len(dates)):
    events[i] = {
        "time": dates[i].text,
        "name": titles[i].text,
    }

print(events)