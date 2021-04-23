from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from behave.runner import Context
from features.poms.wiki_home import WikiHomePage

@given('The Guest is on the Wikipedia Home Page')
def get_to_wiki_home(context: Context):
    driver: WebDriver = context.driver # type annotation for intellisense
    driver.get('https://www.wikipedia.org/')

@when('The Guest clicks on English')
def nav_to_english(context: Context):
    wiki_home_page: WikiHomePage = context.wiki_home_page
    wiki_home_page.english().click()

@when('The Guest clicks on Spanish')
def nav_to_english(context: Context):
    wiki_home_page: WikiHomePage = context.wiki_home_page
    wiki_home_page.espanol().click()

@when('The Guest clicks on Italian')
def nav_to_english(context: Context):
    wiki_home_page: WikiHomePage = context.wiki_home_page
    wiki_home_page.italian().click()

@then('The Guest should be on the Spanish Home Page')
def verify_on_english(context: Context):
    driver: WebDriver = context.driver
    assert driver.title == 'Wikipedia, la enciclopedia libre'

@then('The Guest should be on the Italian Home Page')
def verify_on_english(context: Context):
    driver: WebDriver = context.driver
    assert driver.title == "Wikipedia, l'enciclopedia libera"

@then('The Guest should be on the English Home Page')
def verify_on_english(context: Context):
    driver: WebDriver = context.driver
    assert driver.title == 'Wikipedia, the free encyclopedia'

@when('The Guest types {word} in the search bar')
def type_into_search_bar(context: Context, word: str):
    wiki_home_page: WikiHomePage = context.wiki_home_page
    wiki_home_page.search_bar().send_keys(word)

@when("The Guest clicks the search button")
def press_search_button(context: Context):
    wiki_home_page: WikiHomePage = context.wiki_home_page
    wiki_home_page.search_button().click()

@then("The title should be {title}")
def verify_title_page(context: Context, title: str):
    driver: WebDriver = context.driver
    assert driver.title == title

