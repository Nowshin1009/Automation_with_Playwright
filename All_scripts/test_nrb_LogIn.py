import re
from playwright.sync_api import expect

def test_nrb_login(page):
    try:
        page.goto("https://qa.nrbfamilysupport.com/") 
        page.locator("text='Log In'").click()
        page.wait_for_url("**/auth/login")

        page.locator("input[name='email']").fill("iffataranowshin55@gmail.com")
        page.locator("input[name='password']").fill("1ek2dui@")
        page.get_by_role("button", name=re.compile("Login", re.IGNORECASE)).click()

        page.wait_for_timeout(4000)
        expect(page).to_have_url(re.compile("dashboard", re.IGNORECASE))
        print("Login successful")

    except Exception as e:
        print(f"Test failed: {e}")
        page.screenshot(path="bug_ss1.png")
        print("Screenshot saved as bug_ss1.png")
        raise

