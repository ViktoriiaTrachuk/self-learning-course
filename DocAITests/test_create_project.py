from playwright.sync_api import Playwright, sync_playwright, expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto_login_page(self):
        self.page.goto(
            "https://auth.demo.h2o.ai/auth/realms/q8s-qa/protocol/openid-connect/auth?client_id=document-ai-qa&redirect_uri=https%3A%2F%2Fdocument-ai.cloud-qa.h2o.ai%2F&response_type=code&scope=openid&state=618f8d1022364509bfd48f9ae8d84ccf&code_challenge=5UzmpTqXWWtCR_ovxlViXa8x3qIaO21Qu-gt2dibgHo&code_challenge_method=S256&response_mode=query")

    def enter_username(self, username):
        self.page.locator("input[name=\"username\"]").click()
        self.page.locator("input[name=\"username\"]").fill(username)
        self.page.locator("input[name=\"username\"]").press("Tab")

    def enter_password(self, password):
        self.page.locator("input[name=\"password\"]").fill(password)

    def submit_login(self):
        with self.page.expect_navigation():
            self.page.locator("input[name=\"password\"]").press("Enter")


class ProjectsPage:
    def __init__(self, page):
        self.page = page

    def goto_projects_page(self):
        self.page.goto("https://document-ai.cloud-qa.h2o.ai/")

    def create_new_project(self):
        self.page.locator("a:has-text(\"Create a New Project\")").click()

    def enter_project_name(self, name):
        self.page.locator("input[name=\"name\"]").click()
        self.page.locator("input[name=\"name\"]").fill(name)

    def enter_project_description(self, description):
        self.page.locator("textarea[name=\"description\"]").click()
        self.page.locator("textarea[name=\"description\"]").fill(description)

    def upload_document_sets(self, filename):
        self.page.locator("[aria-label=\"Upload document sets\"]").click()
        self.page.locator("[aria-label=\"Upload document sets\"]").set_input_files(filename)

    def create_project(self):
        with self.page.expect_navigation():
            self.page.locator("text=Create project").click()


class JobsPage:
    def __init__(self, page):
        self.page = page

    def goto_jobs_page(self):
        self.page.locator("a:has-text(\"Jobs (0)\")").click()


class AnnotationSetsPage:
    def __init__(self, page):
        self.page = page

    def goto_annotation_sets_page(self):
        self.page.locator("text=Annotation sets (0)").click()


class DocumentSetsPage:
    def __init__(self, page):
        self.page = page

    def goto_document_sets_page(self):
        self.page.locator("text=Document sets (0)").click()


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.goto_login_page()
    login_page.enter_username("h2oai-tester")
    login_page.enter_password("tester")
    login_page.submit_login()

    projects_page = ProjectsPage(page)
    projects_page.goto_projects_page()
    projects_page.create_new_project()
    projects_page.enter_project_name("0001NewProject")