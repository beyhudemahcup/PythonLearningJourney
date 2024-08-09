from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
url = "https://github.com/beyhudemahcup"
# set english as a browser's language
options.set_preference('intl.accept_languages', 'en-US, en')
driver = webdriver.Firefox(options=options)

driver.get(url)
driver.maximize_window()

print(driver.title)






