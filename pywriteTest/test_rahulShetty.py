import time

from playwright.sync_api import sync_playwright, expect


def test_webAuto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("learning")
        page.get_by_role("combobox").select_option("teach")
        page.get_by_role("link", name="terms and conditions").click()
        checkbox = "#terms"
        page.locator(checkbox).check()
        page.get_by_role("button", name="Sign In").click()
        time.sleep(5)


# check error message
def test_webAuto1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("leartrey")
        page.get_by_role("combobox").select_option("teach")
        page.get_by_role("link", name="terms and conditions").click()
        checkbox = "#terms"
        page.locator(checkbox).check()
        page.get_by_role("button", name="Sign In").click()
        expect(page.get_by_text("username/password.")).to_be_visible()


def test_fire():
    with sync_playwright() as p:
        firefox = p.firefox.launch(headless=False)
        fpage = firefox.new_page()
        fpage.goto("https://rahulshettyacademy.com/loginpagePractise/")
        fpage.get_by_label("Username:").fill("rahulshettyacademy")
        fpage.get_by_label("Password:").fill("learning")
        fpage.get_by_role("combobox").select_option("teach")
        fpage.get_by_role("link", name="terms and conditions").click()
        checkbox = "#terms"
        fpage.locator(checkbox).check()
        fpage.get_by_role("button", name="Sign In").click()
