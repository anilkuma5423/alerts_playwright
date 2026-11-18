from playwright.sync_api import sync_playwright,expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(3000)

    page.locator("//input[@id='user-name']").wait_for(state="visible")
    print("Username Visible")
    page.wait_for_timeout(3000)

    page.locator("//input[@id='password']").wait_for(state="visible")
    print("Password Visible")
    page.wait_for_timeout(3000)

    expect(page.locator("//input[@name='login-button']")).to_be_enabled()
    page.wait_for_timeout(10000)
    print("Login Button enabled")

    print(page.title())
    browser.close()