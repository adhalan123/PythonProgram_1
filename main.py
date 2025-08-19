from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Chromium executable:", p.chromium.executable_path)
    print("Firefox executable:", p.firefox.executable_path)
    print("WebKit executable:", p.webkit.executable_path)
