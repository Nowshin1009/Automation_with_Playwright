import re
from playwright.sync_api import Page, expect

class ForgotPasswordPage:
    
    def __init__(self, page: Page):
        self.page = page
        # Login page elements
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        # More flexible locator for forgot password link
        self.forgot_password_link = page.locator("a[href*='forgotPassword']")
        
        # Forgot password page elements
        self.reset_password_heading = page.get_by_role("heading", name="Reset Password")
        self.instruction_text = page.get_by_text("Please enter your username to", exact=False)
        self.forgot_username_input = page.get_by_role("textbox", name="Username")
        self.reset_password_button = page.get_by_role("button", name="Reset Password")
        self.success_heading = page.get_by_role("heading", name="Reset Password link sent")
    
    def navigate_to_login(self):
        """Navigate to login page"""
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Clear any existing session by going to logout first
        try:
            self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/logout")
            self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        except:
            pass
    
    def click_forgot_password(self):
        """Click on 'Forgot your password?' link"""
        try:
            self.forgot_password_link.click(timeout=10000)
        except:
            # Fallback: try different locator strategies
            try:
                # Try by text content
                text_link = self.page.get_by_text("Forgot your password?", exact=False)
                text_link.click(timeout=5000)
            except:
                # Try by partial text
                partial_link = self.page.locator("a").filter(has_text="Forgot")
                partial_link.click(timeout=5000)
    
    def verify_reset_password_page(self):
        """Verify that reset password page is loaded"""
        # Wait for page to load and check for reset password heading
        try:
            self.page.wait_for_url("**/auth/requestPasswordResetCode**", timeout=10000)
        except:
            # If URL doesn't match, just wait for the heading
            pass
        expect(self.reset_password_heading).to_be_visible(timeout=10000)
    
    def enter_username_for_reset(self, username: str):
        """Enter username for password reset"""
        self.forgot_username_input.click()
        self.forgot_username_input.fill(username)
    
    def click_reset_password_button(self):
        """Click reset password button"""
        self.reset_password_button.click()
    
    def verify_reset_success(self):
        """Verify that reset password link was sent successfully"""
        # Wait for success page to load
        try:
            self.page.wait_for_url("**/auth/sendPasswordReset**", timeout=10000)
        except:
            # If URL doesn't match, just wait for the heading
            pass
        expect(self.success_heading).to_be_visible(timeout=10000)
    
    def reset_password_workflow(self, username: str):
        """Complete forgot password workflow"""
        # Navigate to login page
        self.navigate_to_login()
        
        # Click forgot password link
        self.click_forgot_password()
        
        # Verify reset password page loaded
        self.verify_reset_password_page()
        
        # Enter username and reset
        self.enter_username_for_reset(username)
        self.click_reset_password_button()
        
        # Verify success
        self.verify_reset_success()
