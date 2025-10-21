from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_pim_page_operations(page: Page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)

    # Go to dashboard with extended timeout
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",
        wait_until="domcontentloaded",
        timeout=60000,
    )

    # If redirected to login
    if "/auth/login" in page.url:
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

    # Confirm dashboard loaded
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=20000)

    # Navigate to PIM
    pim_page.navigate_to_pim()

    # Search for employee (handles both found/not found)
    pim_page.search_employee("Valid")

    # Add new employee
    pim_page.add_employee("Iffat", "Ara", "Nowshin")
