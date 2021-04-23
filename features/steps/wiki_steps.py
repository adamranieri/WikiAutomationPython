from behave import given, when, then, fixture
from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.poms.wiki_home import WikiHomePage

driver: WebDriver = webdriver.Chrome('C:\\Users\\AdamRanieri\\Desktop\\drivers\\chromedriver.exe')
wiki_home_page = WikiHomePage(driver)

@given('The Guest is on the Wikipedia Home Page')
def get_to_wiki_home(context: Context):
    driver.get('https://www.wikipedia.org/')

@when('The Guest clicks on English')
def nav_to_english(context: Context):
    wiki_home_page.english().click()

@when('The Guest clicks on Spanish')
def nav_to_english(context: Context):
    wiki_home_page.espanol().click()

@when('The Guest clicks on Italian')
def nav_to_english(context: Context):
    wiki_home_page.italian().click()

@then('The Guest should be on the Spanish Home Page')
def verify_on_english(context: Context):
    assert driver.title == 'Wikipedia, la enciclopedia libre'

@then('The Guest should be on the Italian Home Page')
def verify_on_english(context: Context):
    assert driver.title == "Wikipedia, l'enciclopedia libera"

@then('The Guest should be on the English Home Page')
def verify_on_english(context: Context):
    assert driver.title == 'Wikipedia, the free encyclopedia'

@when('The Guest types {word} in the search bar')
def type_into_search_bar(context: Context, word: str):
    wiki_home_page.search_bar().send_keys(word)

@when("The Guest clicks the search button")
def press_search_button(context: Context):
    wiki_home_page.search_button().click()

@then("The title should be {title}")
def verify_title_page(context: Context, title: str):
    assert driver.title == title

