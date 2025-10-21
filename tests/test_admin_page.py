def test_admin_page_navigation(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewAdminModule")
    page.wait_for_selector("h5:has-text('System Users')")
    assert page.is_visible("h5:has-text('System Users')")
    print("Admin page opened successfully")
