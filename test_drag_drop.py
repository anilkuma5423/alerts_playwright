from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/droppable")
    source=(page.locator("//div[@id='draggable']"))
    target=(page.locator("#droppable")).first

    source.drag_to(target)
    print(target.inner_text())

    page.wait_for_timeout(5000)
    #page.pause()


    page.title()
    browser.close()