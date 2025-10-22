from playwright.sync_api import Page, expect

class MyInfoPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.my_info_tab = page.get_by_role("link", name="My Info")
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.gender_female = page.locator("label").filter(has_text="Female").locator("span")
        self.save_personal_button = page.locator("form").filter(has_text="Employee Full Name").get_by_role("button")
        self.blood_dropdown_icon = page.locator("form").filter(has_text="Blood Type").locator("i")
        self.blood_type_option = lambda type: page.get_by_role("option", name=type, exact=True)
        self.blood_save_button = page.locator("form").filter(has_text="Blood Type").get_by_role("button")
        self.success_message = page.locator(".oxd-toast").last.locator(".oxd-toast-content-text")

    def navigate_to_my_info(self):
        self.my_info_tab.click()

    def update_personal_details(self, first, middle, last):
        self.first_name.fill(first)
        self.middle_name.fill(middle)
        self.last_name.fill(last)
        self.gender_female.click()
        self.save_personal_button.click()

    def update_blood_type(self, blood_type):
        self.blood_dropdown_icon.click()
        self.blood_type_option(blood_type).click()
        self.blood_save_button.click()

    def verify_success_message(self):
        # Wait a moment for the toast to appear
        self.page.wait_for_timeout(1000)
        # Check if any success message is visible
        success_toast = self.page.locator(".oxd-toast").last
        expect(success_toast).to_be_visible(timeout=5000)
        print("Successfully updated information on My Info page.")
