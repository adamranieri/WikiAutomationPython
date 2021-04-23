from selenium.webdriver.chrome.webdriver import WebDriver


class WikiHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def english(self):
        element = self.driver.find_element_by_id('js-link-box-en')
        return element

    def espanol(self):
        element = self.driver.find_element_by_css_selector("div[lang='es']")
        return element

    def italian(self):
        element = self.driver.find_element_by_xpath('//*[@id="js-link-box-it"]')
        return element

    def search_bar(self):
        element = self.driver.find_element_by_name('search')
        return  element

    def search_button(self):
        element = self.driver.find_element_by_class_name('pure-button-primary-progressive')
        return element
