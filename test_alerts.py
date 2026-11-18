from playwright.sync_api import sync_playwright
'''def handler(dialog):
    message=dialog.message
    print(message)
    dialog.accept()'''
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    '''alert_ok_or_cancel_button= page.wait_for_selector("//a[@href='#CancelTab']")
    alert_ok_or_cancel_button.click()
    print("Alert ok")

    #page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", handler)
    #page.wait_for_timeout(3000)

    confirm_box= page.wait_for_selector("//div[@id='CancelTab']/button")
    confirm_box.click()
    print("Confirm box")

    page.wait_for_timeout(5000)'''

    alert_textbox_button= page.wait_for_selector("//a[@href='#Textbox']")
    alert_textbox_button.click()

    page.on("dialog", lambda dialog: dialog.accept("Anil Kumar"))

    prompt_box= page.wait_for_selector("//div[@id='Textbox']/button")
    prompt_box.click()

    #page.on("dialog", lambda dialog: dialog.accept("Anil Kumar"))
    page.wait_for_timeout(5000)


    page.title()

    browser.close()
