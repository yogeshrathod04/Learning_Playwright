from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto("https://demo.automationtesting.in/")

    # css Selectors - id=#, class=.(dot), attribute= tagname[attribute = "value"]

    #using ID
    '''emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type("test5@gmail.com")
    page.wait_for_timeout(3000)

    button = page.wait_for_selector("#enterimg")
    button.click()
    page.wait_for_timeout(3000)'''

    #class selector: attribute = tagname['value']
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page.wait_for_selector("input[name='username']").fill("Admin")
    page.wait_for_timeout(3000)

    password = page.wait_for_selector("input[name='password']").fill("admin123")
    page.wait_for_timeout(3000)

    login_button = page.wait_for_selector('button[type="submit"]')
    login_button.click()
    page.wait_for_timeout(3000)

    page.get_by_text("Admin").click()
    page.wait_for_timeout(3000)

    page.get_by_text("PIM").click()
    page.wait_for_timeout(3000)

    page.get_by_text("Leave").click()
    page.wait_for_timeout(3000)

    page.get_by_text("Time").click()
    page.wait_for_timeout(3000)


