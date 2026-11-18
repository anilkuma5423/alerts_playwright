from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practice-automation.com/form-fields/")

    page.locator('//input[@id="name-input"]').fill("Admin")
    page.locator('//input[@type="password"]').fill("Admin123")

    checkbox1=(page.locator('//input[@type="checkbox"]')).nth(1)
    checkbox1.check()
    print(checkbox1.is_checked())

    checkbox1.uncheck()
    print(checkbox1.uncheck())
    page.wait_for_timeout(3000)

    radio = (page.locator('//input[@type="radio"]')).nth(2)
    radio.check()
    print(radio.is_checked())
    select = (page.locator('//select[@id="automation"]'))
    select.select_option(label="Yes")

    page.locator("//input[@id='email']").fill("admin12@gmail.com")
    page.wait_for_timeout(3000)
    page.locator("//textarea[@id='message']").fill("Thank You")
    page.wait_for_timeout(3000)

    page.locator('//button[@id="submit-btn"]').click()

    page.wait_for_timeout(10000)

    page.title()
    browser.close()