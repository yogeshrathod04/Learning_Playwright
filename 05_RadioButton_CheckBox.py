
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.automationtesting.in/Register.html")
    # page.select_option("//select[@id='country']", "India")
    # page.select_option("//select[@id='yearbox']", "2004")
    # page.wait_for_selector("input[type='password']").fill("12345678")
    # page.wait_for_selector("//select[@placeholder='Month']").select_option('January')

    # Radio Button
    radio_button = page.query_selector('//input[@value="FeMale"]')
    radio_button.click()
    # page.query_selector('//input[@Value="FeMale"]').check()
    # page.query_selector('input[value="FeMale"]').set_checked(True)

    # Check Box
    page.query_selector('input[value="Cricket"]').set_checked(True)

    check_box = page.query_selector("//input[@value='Movies']")
    check_box.click()

    page.query_selector("input[value='Hockey']").click()

    page.wait_for_timeout(5000)

