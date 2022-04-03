from selenium.webdriver.common.by import By

resultRepoListCSS = "ul.repo-list"
resultRepoItemCSS = "li.repo-list-item a"


class AdvancedSearchResultsPage():
    def select_repo(self):
        self.driver.find_element(By.CSS_SELECTOR, resultRepoItemCSS).click()

    def is_Only_one_repo_displayed(self):

        itemsInList = list(self.driver.find_elements(By.CSS_SELECTOR, resultRepoItemCSS))
        print("Total repos listed:: ",itemsInList.__len__())

        if itemsInList.__len__() > 1:
            return False
        else:
            return True

    def is_repo_name_mvoloskov(self):
       required_repoName = "mvoloskov/decider"

       repoName = self.driver.find_element(By.CSS_SELECTOR, resultRepoItemCSS)
       actual_repoName = repoName.text
       print("RepoName seen ===", actual_repoName)
       if(required_repoName == actual_repoName):
         return True
       else:
         return False