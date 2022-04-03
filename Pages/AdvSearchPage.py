from selenium.webdriver.common.by import By

from Pages.commonPage import commonPage

writtenInLanguageDropdownID = "search_language"
withThisManyStarsTextBoxID = "search_stars"
inTheStateDropdownID = "search_state"
withThisLicenseDropdownID = "search_license"
withThisManyFollowersTextBoxID = "search_followers"
submitButtonCSS = "div.container-lg.p-responsive.advanced-search-form  button[type='submit']"

class AdvSearchPage():

    def perform_advanced_search(self,language, stars, license, followers,state):
        commonPage.select_by_visible_text(self,By.ID, writtenInLanguageDropdownID, language)
        commonPage.select_by_visible_text(self,By.ID, inTheStateDropdownID, state)
        commonPage.select_by_visible_text(self,By.ID, withThisLicenseDropdownID, license)
        self.driver.find_element(By.ID, withThisManyStarsTextBoxID).send_keys(stars)
        self.driver.find_element(By.ID, withThisManyFollowersTextBoxID).send_keys(followers)
        self.driver.find_element(By.CSS_SELECTOR, submitButtonCSS).click()
        print("Advanced search completed with criteria with Language=" +language +" state= " +state + " stars=" +stars +" License=" +license +" Followers=" +followers)