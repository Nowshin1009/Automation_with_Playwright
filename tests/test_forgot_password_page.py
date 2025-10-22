from playwright.sync_api import Page, expect
from pages.forgot_password_page import ForgotPasswordPage

def test_forgot_password_workflow(page: Page):
    """Test complete forgot password workflow"""
    forgot_password_page = ForgotPasswordPage(page)
    
    # Navigate to login page
    forgot_password_page.navigate_to_login()
    
    # Click forgot password link
    forgot_password_page.click_forgot_password()
    
    # Verify reset password page loaded
    forgot_password_page.verify_reset_password_page()
    
    print("Forgot password workflow completed successfully")

def test_forgot_password_page_elements(page: Page):
    """Test individual forgot password page elements"""
    forgot_password_page = ForgotPasswordPage(page)
    
    # Navigate to login page
    forgot_password_page.navigate_to_login()
    
    # Click forgot password link
    forgot_password_page.click_forgot_password()
    
    # Verify reset password page elements
    forgot_password_page.verify_reset_password_page()
    
    print("Forgot password page elements verified successfully")

def test_reset_password_form_submission(page: Page):
    """Test reset password form submission"""
    forgot_password_page = ForgotPasswordPage(page)
    
    # Navigate to login page
    forgot_password_page.navigate_to_login()
    
    # Click forgot password link
    forgot_password_page.click_forgot_password()
    
    # Verify page loaded
    forgot_password_page.verify_reset_password_page()
    
    # Fill and submit form
    forgot_password_page.enter_username_for_reset("Admin")
    forgot_password_page.click_reset_password_button()
    
    # Verify success message
    forgot_password_page.verify_reset_success()
    
    print("Reset password form submission completed successfully")
