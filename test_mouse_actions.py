from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")

    #page.mouse.move(0,0)
    #page.mouse.move(0,100)
    #page.mouse.move(100,0)
    #page.mouse.move(100,100)
    #page.mouse.up()
    #page.mouse.down()
    page.mouse.click(500,300, button="right")
    #page.pause()
    #page.mouse.dblclick(100,100)
    

    page.wait_for_timeout(10000)

    page.title()
    browser.close()
