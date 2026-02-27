from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    # -------- Locators --------

    def notice_heading(self):
        return self.page.get_by_role("heading", name="Notice")

    def accept_all_button(self):
        return self.page.get_by_role("button", name="Accept all")
    def toogleAccount(self):
        return self.page.get_by_role("button", name="Toggle Account Menu")
    
    def login_link(self):
        return self.page.get_by_role("link", name="Log In Log in to RocPortal")

    def email_field(self):
        return self.page.get_by_role("textbox", name="Email Address")

    def password_field(self):
        return self.page.get_by_role("textbox", name="Password")

    def login_button(self):
        return self.page.get_by_role("button", name="Continue", exact=True)
    # -------- Actions --------
    def accept_notice_if_present(self):
        try:
         self.accept_all_button().click()
        except :
         pass

    