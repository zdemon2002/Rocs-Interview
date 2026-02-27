import re
from playwright.sync_api import expect, Page
from pages.homepage import HomePage
def test_web(page: Page) -> None:
    home = HomePage(page)
    page.goto("https://rocscience.com")
    home.accept_notice_if_present()
    home.toogleAccount().click()
    expect(home.login_link()).to_be_visible()
    home.login_link().click()
    
    expect(page).to_have_url(re.compile(r"https://auth\.rocscience\.com/u/login"))
    #check if login form is visible
    expect(home.email_field()).to_be_visible()
    expect(home.password_field()).to_be_visible()
    expect(home.login_button()).to_be_visible()
    #check if login form is enabled
    expect(home.login_button()).to_be_enabled()
    
    
    
    