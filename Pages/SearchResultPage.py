from selenium.webdriver.common.by import By


advancedSearchLinkCSS = "Advanced search"
class searchResultsPage():

    def click_advancedSearch(self):
        self.driver.find_element(By.LINK_TEXT,value=advancedSearchLinkCSS).click()
        print("Clicked on AdvancedSearchLink")

