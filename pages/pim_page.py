from playwright.sync_api import Page, expect

class PimPage:
    def __init__(self, page: Page):
        self.page = page
        self.pim_tab = page.get_by_role("link", name="PIM")
        self.search_box = page.get_by_role("textbox", name="Type for hints...").first
        self.search_button = page.get_by_role("button", name="Search")
        self.add_employee_link = page.get_by_role("link", name="Add Employee")
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.save_button = page.get_by_role("button", name="Save")
        self.success_message = page.get_by_text("Success", exact=True)

    def navigate_to_pim(self):
        self.pim_tab.click()
        # wait until URL or heading confirms PIM page
        self.page.wait_for_url("**/pim/**", timeout=20000)
def search_employee(self, name: str):
    self.search_box.fill(name)
    self.search_button.click()

    # Wait for either result row or "No Records Found"
    result_locator = self.page.locator("div.oxd-table-card")
    no_record_locator = self.page.get_by_text("No Records Found")

    if result_locator.first.is_visible(timeout=8000):
        print(f"Search executed for '{name}' — results visible.")
    elif no_record_locator.is_visible(timeout=3000):
        print(f"No records found for '{name}'.")
    else:
        raise AssertionError(f"❌ Unexpected search state for '{name}'.")

    def add_employee(self, first: str, middle: str, last: str):
        self.add_employee_link.click()
        self.first_name.fill(first)
        self.middle_name.fill(middle)
        self.last_name.fill(last)
        self.save_button.click()
        expect(self.success_message).to_be_visible(timeout=10000)
        print(f"Added employee: {first} {middle} {last}")
