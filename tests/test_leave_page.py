from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.leave_page import LeavePage

def test_leave_page_operations(page: Page):
    login_page = LoginPage(page)
    leave_page = LeavePage(page)

    # Go to Dashboard page first
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    # If redirected to login, perform login
    if page.url.endswith("/auth/login"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

    # Navigate to Leave page
    leave_page.navigate_to_leave()

    # Test 1: Search with no employee (should show no records)
    leave_page.search_leave_records()
    leave_page.verify_no_records_found()
    print("No records found test passed")

    # Test 2: Search by employee name
    leave_page.search_by_employee_name("John")
    leave_page.click_search()
    print("Employee search test completed")

    # Test 3: Reset search
    leave_page.reset_search()
    print("Reset search test completed")

def test_leave_calendar_selection(page: Page):
    login_page = LoginPage(page)
    leave_page = LeavePage(page)

    # Go to Dashboard page first
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    # If redirected to login, perform login
    if page.url.endswith("/auth/login"):
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

    # Navigate to Leave page
    leave_page.navigate_to_leave()

    # Test calendar month selection
    leave_page.select_calendar_month("September")
    print("Calendar month selection test completed")

    # Test leave type selection
    leave_page.select_leave_type("CAN - Personal")
    print("Leave type selection test completed")
