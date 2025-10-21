from playwright.sync_api import sync_playwright

def save_login_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Dashboard")

        # Save login session
        context.storage_state(path="state.json")
        print("Login state saved successfully in 'state.json'")

        browser.close()


if __name__ == "__main__":
    save_login_state()
