1. ID Locator
Definition
Used to locate an element using its unique HTML id attribute.
Symbol: #

HTML
<input id="username">

Syntax
page.locator("#username")

Example
page.locator("#username").fill("admin")

Interview Answer
ID locator is used to identify an element using its unique id attribute. In CSS selector, # represents id.
-------------------------------------------------------

2. Class Locator
Definition
Used to locate elements using the HTML class attribute.
Symbol: .(dot)

HTML
<button class="login-btn">

Syntax
page.locator(".login-btn")

Example
page.locator(".login-btn").click()

Interview Answer
Class locator identifies elements using class names. In CSS selector, dot (.) represents a class.
----------------------------------------------------------

3. Tag Locator
Definition
Used to locate elements by HTML tag name.
HTML

<button>Login</button>

Syntax

page.locator("button")

Example

page.locator("button").click()

Interview Answer
Tag locator identifies elements using HTML tags such as button, input, div, span etc.

4. Attribute Locator
Definition
Used to locate elements based on any HTML attribute.
HTML

<input type="text">

Syntax

page.locator("[type='text']")

Example

page.locator("[type='text']").fill("Admin")

Interview Answer
Attribute locator identifies elements using custom or standard HTML attributes.

5. CSS Selector
Definition
CSS selector is a powerful way to locate elements using id, class, attributes and hierarchy.
Syntax

page.locator("div.login input")

Example

page.locator("form #username")

Interview Answer
CSS selectors are faster and more readable than XPath in most cases.

6. XPath
Definition
XPath is used to navigate and locate elements using XML/HTML structure.
Syntax

page.locator("//input[@id='username']")

Example

page.locator("//button[text()='Login']")

Interview Answer
XPath is useful when CSS selectors cannot uniquely identify an element.

PLAYWRIGHT SPECIAL LOCATORS

7. get_by_text()
Definition
Locates element using visible text.
Syntax

page.get_by_text("Login")

Example

page.get_by_text("Submit").click()

Interview Answer
Used when an element can be uniquely identified by visible text.

8. get_by_role()
Definition
Locates elements based on accessibility roles.
Syntax

page.get_by_role("button", name="Login")

Example

page.get_by_role("link", name="Home")

Interview Answer
Playwright recommends role locators because they are reliable and accessibility-friendly.

9. get_by_label()
Definition
Locates form controls associated with labels.
HTML

<label>Username</label>
<input>

Syntax

page.get_by_label("Username")

Example

page.get_by_label("Username").fill("admin")

Interview Answer
Used for form fields that have label associations.

10. get_by_placeholder()
Definition
Locates input fields using placeholder text.
HTML

<input placeholder="Enter username">

Syntax

page.get_by_placeholder("Enter username")

Example

page.get_by_placeholder("Enter username").fill("admin")


11. get_by_test_id()
Definition
Locates elements using test-specific IDs.
HTML

<button data-testid="login-btn">

Syntax

page.get_by_test_id("login-btn")

Example

page.get_by_test_id("login-btn").click()

Interview Answer
Test IDs are stable locators created specifically for automation testing.

ACTIONS
click()
Definition
Used to click an element.
Syntax

locator.click()

Example

page.locator("#login").click()


fill()
Definition
Used to clear existing text and enter new text.
Syntax

locator.fill("value")

Example

page.locator("#username").fill("admin")

Difference from type()
fill():
* Clears existing text first
type():
* Types character by character

hover()
Definition
Moves mouse pointer over an element.
Syntax

locator.hover()

Example

page.locator("#menu").hover()

Used for dropdown menus.

check()
Definition
Used to select a checkbox.
Syntax

locator.check()

Example

page.locator("#remember").check()


uncheck()
Definition
Used to deselect a checkbox.
Syntax

locator.uncheck()


select_option()
Definition
Used to select values from dropdown lists.
Syntax

locator.select_option("India")

Example

page.locator("#country").select_option("India")


ASSERTIONS
to_have_text()
Definition
Verifies the expected text is displayed.
Syntax

expect(locator).to_have_text("Success")

Example

expect(page.locator("#msg")).to_have_text("Success")


to_be_visible()
Definition
Verifies element is visible.
Syntax

expect(locator).to_be_visible()

Example

expect(page.locator("#login")).to_be_visible()


to_have_url()
Definition
Verifies current URL.
Syntax

expect(page).to_have_url("https://example.com")


WAITS
Auto Wait
Definition
Playwright automatically waits before performing actions.
What it waits for
* Visible
* Enabled
* Stable
* Attached to DOM
Example

page.locator("#submit").click()

No explicit wait needed.
Interview Question
Why is Playwright more stable than Selenium?
Answer:
Because Playwright provides built-in auto-waiting, reducing flaky tests.

DIALOGS
Alert
Definition
A popup showing information with OK button.
Syntax

page.on("dialog",
        lambda dialog: dialog.accept())


Confirm
Definition
Popup with OK and Cancel buttons.
Accept

dialog.accept()

Cancel

dialog.dismiss()


Prompt
Definition
Popup asking user input.
Syntax

dialog.accept("John")

Example

page.on(
    "dialog",
    lambda d: d.accept("John")
)


INTERVIEW GOLDEN QUESTION
Locator vs ElementHandle
Locator

locator = page.locator("#login")

Definition:
Locator is a smart object that finds elements whenever an action is performed.
Advantages:
* Auto waiting
* Retry mechanism
* Dynamic

ElementHandle

element = page.query_selector("#login")

Definition:
ElementHandle stores a direct reference to a DOM element.
Disadvantages:
* Can become stale
* No auto retry
Interview Answer
Locator is recommended because it is dynamic and supports auto-waiting, while ElementHandle is a static reference.

