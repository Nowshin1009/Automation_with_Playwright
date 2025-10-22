from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_admin_page_navigation(page: Page):
    login_page = LoginPage(page)
    
    # Go to admin page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewAdminModule")
    
    # If redirected to login, perform login
    if "/auth/login" in page.url:
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
    
    # Wait for admin page to load and verify
    expect(page.get_by_role("heading", name="System Users")).to_be_visible(timeout=20000)
    print("Admin page opened successfully")
