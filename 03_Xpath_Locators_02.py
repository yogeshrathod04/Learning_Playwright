from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")

    # XPath: it's easy to travel web elements from forward to backward,
    # it's used to traverse between web element

    # Relative x_path
    # using attribute: //tagname[@attribute_name='value']
    page.wait_for_selector('//input[@name="username"]').fill('Admin')
    page.wait_for_timeout(3000)

    page.wait_for_selector('//input[@placeholder="Password"]').fill('admin123')
    page.wait_for_timeout(3000)

    '''page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(6000)'''


    # text: //tagname[text()="text"]
    # text match exactly page/UI texts
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    page.wait_for_timeout(6000)

    #  Contains:
    # Attributes: //tagname[contains(attribute, "value")]  example: text: //tagname[contains(text(),"Forgot your")]
    # //input[contains(@placeholder,"User")]
    # Text: tagname[contains(text(), "Username")] ex. label[contains(text(), "Username")]

    # dynamic: yogesh123, yogesh4332, yogesh9282
    # starts-with: tagname[starts-with(@id, 'yogesh')]
    # ends-with: tagname[ends-with(@id,'32user')]

    # family
    # parent: tagname[id@="xy"]/parent::input[]
    # child: tagname[id@="xy"]/child::input[]



