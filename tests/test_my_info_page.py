from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage

def test_update_my_info(page: Page):
    login_page = LoginPage(page)
    my_info_page = MyInfoPage(page)

    # Go to Dashboard page first
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    # If redirected to login, perform login
    if page.url.endswith("/auth/login"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

    # Navigate to My Info tab
    my_info_page.navigate_to_my_info()

    # Update details
    my_info_page.update_personal_details("Iffat", "Ara", "Nowshin")

    # Update blood type
    my_info_page.update_blood_type("B+")

    # Verify success toast
    my_info_page.verify_success_message()
