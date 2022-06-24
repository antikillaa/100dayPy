from selenium import webdriver

chrome_driver_path = '/Users/staspeshkur/PycharmProjects/learn/src/selenium/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://amazon.com")
driver.quit()
print("hello")
