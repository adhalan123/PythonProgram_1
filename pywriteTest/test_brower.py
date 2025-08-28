# def test_browser(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://practice.qabrains.com/")
#     page.get_by_placeholder("eg. user@user.com").fill("qa_testers@qabrains.com")
#     page.get_by_placeholder("*******").fill("Password123")
#     page.get_by_role("button", name="Login").click()


def test_web(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.qabrains.com/")
    userAuthentication = ".rc-menu-submenu-title"
    UserAuth = page.locator(userAuthentication)
    UserAuth.wait_for(state="visible")
    UserAuth.click()
    resitartion = "#registration"
    resitartion = page.locator(resitartion)
    resitartion.wait_for(state="visible")
    resitartion.click()
    page.get_by_role("textbox", name="name").fill("aarati")
    country = "#country"
    page.locator(country).select_option("Andorra")
    accountType = "#account"
    page.locator(accountType).select_option(label="Engineer")
