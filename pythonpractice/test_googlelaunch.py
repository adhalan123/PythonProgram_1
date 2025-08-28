def test_launch_browser(page):
    # Open website
    page.goto("https://example.com")
    # Verify title
    assert "Example Domain" in page.title()
