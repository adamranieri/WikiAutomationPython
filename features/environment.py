from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.poms.wiki_home import WikiHomePage

# all setup and teardown functions must go in this file
#function must be named using behave conventions
def before_all(context):
    print("started")

def after_all(context):
    print("ended")