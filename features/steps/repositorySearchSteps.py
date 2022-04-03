from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages import AdvSearchPage, GitRepoSearchPage as gitSearch, AdvancedSearchResultPage, SearchResultPage, \
    MvoloskovRepoPage


@given(u'user is on git search Page')
def goToGitSearchPage(context):
    p = ChromeDriverManager()
    context.driver = webdriver.Chrome(p.install())
    context.driver.maximize_window()
    gitSearch.gitRepoSearch.goToGitHub(context)


@when(u'user enters "{searchString}" in search box and hits enter')
def searchForReact(context, searchString):
    gitSearch.gitRepoSearch.perform_gitSearch(context,searchString)

@when(u'user is on results page and clicks on advanced search link')
def step_impl(context):

    SearchResultPage.searchResultsPage.click_advancedSearch(context)


@when(u'user searches for repo in advanced search page')
def step_impl(context):

    for row in context.table:
        AdvSearchPage.AdvSearchPage.perform_advanced_search(context, language=row['Language'], stars=row['Stars'],
                                                            license=row['License'], followers=row['Followers'],
                                                            state=row['State'])
    print("Step -user searches for repo in advanced search page to be implemented ")


@then(u'User should see only 1 repo result that reads \'mvoloskov/decider\'')
def step_impl(context):
     assert AdvancedSearchResultPage.AdvancedSearchResultsPage.is_repo_name_mvoloskov(context)
     AdvancedSearchResultPage.AdvancedSearchResultsPage.select_repo(context)


@then(u'user should be able to print first 300 characters of the readme.md file of the repository')
def step_impl(context):
    MvoloskovRepoPage.mvoloskov.click_readMeFile(context)
    assert MvoloskovRepoPage.mvoloskov.print_first300Characters_of_file(context)


