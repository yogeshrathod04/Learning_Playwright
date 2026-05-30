from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

# There are two types of drop-downs
# 1. Select Drop-downs
# 2. Boostrap Drop-downs

    #i. find the select location
    select_skill = page.query_selector('//select[@id="Skills"]')
    # ii. select option
    select_skill.select_option("Adobe Photoshop")

    # page.query_selector('//select[@id="country"]').select_option("India")

    page.select_option('//select[@id="country"]', "India")
    page.wait_for_timeout(5000)

