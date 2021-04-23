from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.poms.wiki_home import WikiHomePage

# all setup and teardown functions must go in this file
#function must be named using behave conventions

#context is a shared object in behave. Any variable attached to context in before_all will be available
# in the later step implementations
def before_all(context):
    driver: WebDriver = webdriver.Chrome('C:\\Users\\AdamRanieri\\Desktop\\drivers\\chromedriver.exe')
    wiki_home_page = WikiHomePage(driver)
    context.driver = driver
    context.wiki_home_page = wiki_home_page
    print("started")

def after_all(context):
    context.driver.quit()
    print("ended")