from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



class commonPage():

    def initialize_driver(context):
        context.driver = webdriver.Chrome(ChromeDriverManager().install())

    def select_by_visible_text(self,by, locator, value):
            select = Select(self.driver.find_element(by,locator))
            select.select_by_visible_text(value)




