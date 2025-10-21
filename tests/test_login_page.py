import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_example(page: Page) -> None:
    login_page = LoginPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    if page.url.endswith("/auth/login"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=10000)
    print("Test passed — Dashboard is visible after login.")
