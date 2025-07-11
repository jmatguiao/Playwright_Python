from playwright.sync_api import Page

class BasePages:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url, wait_until="load")

    def get_element(self, selector: str):
        return self.page.locator(selector)

    def wait_for_element(self, selector: str):
        element = self.page.locator(selector)
        element.wait_for(state="visible")
        return element

    def get_title(self):
        return self.page.title()
