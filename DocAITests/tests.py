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