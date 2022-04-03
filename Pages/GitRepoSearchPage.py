
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

searchTextBoxCSS = "input[name='q'][data-test-selector='nav-search-input']"
githubUrl = "https://github.com/%5D(https://github.com/)"

class gitRepoSearch():
   def perform_gitSearch(self,searchString):
       self.driver.find_element(By.CSS_SELECTOR,value=searchTextBoxCSS).send_keys(searchString)
       self.driver.find_element(By.CSS_SELECTOR,value=searchTextBoxCSS).send_keys(Keys.ENTER)

       print("Entered react")
       print("Hit Enter")

   def goToGitHub(self):
       self.driver.get(githubUrl)
       print("In Url " +githubUrl)



















