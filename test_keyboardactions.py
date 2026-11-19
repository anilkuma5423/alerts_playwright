from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")
    '''page.locator('//input[@name="username"]').fill("Admin")
    page.locator("//input[@name='password']").fill("admin123")
    #Enter Key
    #page.keyboard.press("Enter")

    page.locator('//input[@name="username"]').click()

    #select All and delete
    page.keyboard.press("Control+A")
    page.wait_for_timeout(5000)
    page.keyboard.press("Backspace")'''

    #Tab key
    page.locator('//input[@name="username"]').fill("Admin")
    page.wait_for_timeout(5000)
    page.keyboard.press("Tab")
    page.locator("//input[@name='password']").fill("admin123")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)

    page.wait_for_timeout(7000)

    page.title()
    browser.close()
