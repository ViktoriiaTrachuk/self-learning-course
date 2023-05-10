from playwright.sync_api import Playwright, sync_playwright, expect
from typing import List

class LoginPage:
    def sign_in(self, page, url, username, password):
        self.page = page
        self.page.goto(url)
        self.page.locator("input[name=\"username\"]").fill(username)
        self.page.locator("input[name=\"password\"]").fill(password)
        with self.page.expect_navigation():
            self.page.locator("input[name=\"password\"]").press("Enter")

'''
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def set_username(self, username):
        #self.page.locator("input[name=\"username\"]").click()
        self.page.locator("input[name=\"username\"]").fill(username)
        #self.page.locator("input[name=\"username\"]").press("Tab")

    def set_password(self, password):
        self.page.locator("input[name=\"password\"]").fill(password)
        with self.page.expect_navigation():
            self.page.locator("input[name=\"password\"]").press("Enter")
'''

class ProjectPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def create_new_project(self, name, description): #files: List[str], self,
        self.page.locator("a:has-text(\"Create a New Project\")").click()
        #self.page.locator("input[name=\"name\"]").click()
        self.page.locator("input[name=\"name\"]").fill(pr_name)
        #self.page.locator("textarea[name=\"description\"]").click()
        self.page.locator("textarea[name=\"description\"]").fill(pr_description)
        self.page.locator("[aria-label=\"Upload document sets\"]").click()
        self.page.get_by_role("switch", name="Upload pdfs, images").click()
        #self.page.locator("[aria-label=\"Upload document sets\"]").set_input_files(*files)
        with self.page.expect_navigation():
            self.page.locator("text=Create project").click()


class NavigationMenu:
    def __init__(self, page):
        self.page = page

    def go_to_jobs(self):
        self.page.locator("a:has-text(\"Jobs (0)\")").click()

    def go_to_annotation_sets(self):
        self.page.locator("text=Annotation sets (0)").click()

    def go_to_document_sets(self):
        self.page.locator("text=Document sets (0)").click()


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage
    url = "https://document-ai.cloud-qa.h2o.ai/"
    username = "h2oai-tester"
    password = "tester"
    create_project = ProjectPage
    #create_project.navigate()
    name = "A Brand New Project"
    description = "test"
    create_project.create_new_project(name, description)
    page.screenshot(path="example.png")

'''    
    login_page.navigate(
        "https://auth.demo.h2o.ai/auth/realms/q8s-qa/protocol/openid-connect/auth?client_id=document-ai-qa&redirect_uri=https%3A%2F%2Fdocument-ai.cloud-qa.h2o.ai%2F&response_type=code&scope=openid&state=618f8d1022364509bfd48f9ae8d84ccf&code_challenge=5UzmpTqXWWtCR_ovxlViXa8x3qIaO21Qu-gt2dibgHo&code_challenge_method=S256&response_mode=query")
    login_page.set_username("h2oai-tester")
    login_page.set_password("tester")
    page.screenshot(path="example.png")

    #create_project = ProjectPage(page)
    #create_project.navigate(self,"/document-sets" )



def test_run (playwright: Playwright)-> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.navigate(
        "https://auth.demo.h2o.ai/auth/realms/q8s-qa/protocol/openid-connect/auth?client_id=document-ai-qa&redirect_uri=https%3A%2F%2Fdocument-ai.cloud-qa.h2o.ai%2F&response_type=code&scope=openid&state=618f8d1022364509bfd48f9ae8d84ccf&code_challenge=5UzmpTqXWWtCR_ovxlViXa8x3qIaO21Qu-gt2dibgHo&code_challenge_method=S256&response_mode=query")
    login_page.set_username("h2oai-tester")
    login_page.set_password("tester")
'''