from playwright.sync_api import Page, expect

class LeavePage:
    
    def __init__(self, page: Page):
        self.page = page
        # Navigation elements
        self.leave_tab = page.get_by_role("link", name="Leave")
        
        # Search form elements
        self.calendar_icon = page.locator(".oxd-icon.bi-calendar").first
        # More resilient month selection by text later
        self.leave_type_dropdown = page.locator(
            ".oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon"
        ).first
        self.employee_search_box = page.get_by_role("textbox", name="Type for hints...")
        
        # Action buttons
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        
        # Result elements
        self.no_records_found = page.get_by_text("No Records Found")
        self.table_rows = page.locator("div.oxd-table-body > div.oxd-table-card")
    
    def navigate_to_leave(self):
        """Navigate to Leave page"""
        self.leave_tab.click()
        self.page.wait_for_url("**/leave/**", timeout=20000)
    
    def select_calendar_month(self, month: str = "September"):
        """Select calendar month by visible text (best-effort)."""
        self.calendar_icon.click()
        # Try to click desired month if visible in any calendar widget
        month_option = self.page.get_by_text(month, exact=True)
        try:
            month_option.click(timeout=2000)
        except Exception:
            # If not available, ignore and proceed with current month
            pass
    
    def select_leave_type(self, leave_type: str = "CAN - Personal"):
        """Select leave type from dropdown"""
        self.leave_type_dropdown.click()
        self.page.get_by_role("option", name=leave_type).click()
    
    def search_by_employee_name(self, employee_name: str):
        """Search for employee by name"""
        self.employee_search_box.click()
        self.employee_search_box.fill(employee_name)
        # Pick first matching suggestion containing the name
        self.page.get_by_role("option").filter(has_text=employee_name).first.click()
    
    def click_search(self):
        """Click search button"""
        self.search_button.click()
    
    def click_reset(self):
        """Click reset button"""
        self.reset_button.click()
    
    def verify_no_records_found(self):
        """Verify that no records are found"""
        expect(self.no_records_found).to_be_visible(timeout=10000)
    
    def wait_for_results(self):
        """Wait until either results appear or 'No Records Found' is shown."""
        self.page.wait_for_timeout(500)  # brief debounce
        try:
            self.table_rows.first.wait_for(state="visible", timeout=5000)
            return
        except Exception:
            pass
        expect(self.no_records_found).to_be_visible(timeout=5000)
    
    def search_leave_records(self, employee_name: str = None, leave_type: str = "CAN - Personal", month: str = "September"):
        """Complete leave search workflow"""
        # Select calendar month
        self.select_calendar_month(month)
        
        # Select leave type
        self.select_leave_type(leave_type)
        
        # Search
        self.click_search()
        self.wait_for_results()
        
        # If employee name provided, search by employee
        if employee_name:
            self.search_by_employee_name(employee_name)
            self.click_search()
            self.wait_for_results()
    
    def reset_search(self):
        """Reset the search form"""
        self.click_reset()
