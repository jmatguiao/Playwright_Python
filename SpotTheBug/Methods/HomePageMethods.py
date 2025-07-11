from playwright.sync_api import expect
from base.BasePage import BasePages
from Locators.HomePageLocators import HomePageLocators

class HomePageMethod(BasePages):
    def Verify_Welcome_Header(self):
        header = self.get_element(HomePageLocators.WelcomeHeader)
        expect(header).to_be_visible()
        
    def click_sidebar_toggle(self):
        sideBar = self.get_element(HomePageLocators.SideBar)
        sideBar.click()
        
    def Verify_Sidebar(self):
        header = self.get_element(HomePageLocators.SideBarHeader)
        expect(header).to_be_visible()
        self.page.screenshot(path="screenshots/homePage_final.png")
        
        
        
        
