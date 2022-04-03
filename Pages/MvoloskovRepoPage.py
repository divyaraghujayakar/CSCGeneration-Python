from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

readMeFileLink = "a[title='README.md']"
readMeFileFrameID = "readme"

class mvoloskov():
    def click_readMeFile(self):
     while True:
        self.driver.implicitly_wait(4)
        try:
            self.driver.find_element(By.CSS_SELECTOR,readMeFileLink).click()
        except StaleElementReferenceException:
            self.driver.find_element(By.CSS_SELECTOR,readMeFileLink).click()
        except NoSuchElementException:
            break
     print("Clicked on readMeFileLink")

    def print_first300Characters_of_file(self):
        readmeData = self.driver.find_element(By.ID, readMeFileFrameID).text
        first300 = readmeData[0:300]
        print(first300)
        return str(first300).__len__()==300
