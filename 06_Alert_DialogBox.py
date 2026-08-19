from playwright.sync_api import sync_playwright

text_alert = []
def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')


    # in playwright we don't need to click ok button its automatically handle/press the ok button
    # playwright automatically click ok

    # alert box
    # page.wait_for_selector("//div[@id='OKTab']/button") # after locating a alertbox then "slash" /button means direct locate to its child button & click
    # page.wait_for_timeout(6000)


    # alert with ok & cancel
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(2000)

    # control alert (playwright automatically click the cancel button, that reason we've to control it using lambda function to tell dialog to accept/dismiss)
    # page.on("dialog", lambda dialog: dialog.accept())  # dialog.dismiss() for reject

    # print alert message whatever coming in alert dialog
    # page.on("dialog", lambda dialog: print(dialog.message))

    page.on("dialog", handle_dialog)  # it tells the browser whenever dialog appear handle it
    page.wait_for_selector('//div[@id="CancelTab"]').click()
    page.wait_for_timeout(2000)
    print(text_alert)



