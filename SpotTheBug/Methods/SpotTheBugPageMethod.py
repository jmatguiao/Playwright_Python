from playwright.sync_api import expect
from base.BasePage import BasePages
from Locators.SpotTheBugpageLocators import SpotTheBugpageLocators

class SpotTheBugPageMethod(BasePages):
    def Verify_Header(self):
        header = self.get_element(SpotTheBugpageLocators.STB_Header)
        expect(header).to_be_visible()
        
    def Verify_FirstName_TextField(self):
        FirstNameTextField = self.get_element(SpotTheBugpageLocators.STB_FirstName)
        FirstNameTextField.click()
        FirstNameTextField.fill("jona")
        expect(FirstNameTextField).to_have_value("jona")
        
        
    def Verify_LastName_TextField(self):
        LastNameTextField = self.get_element(SpotTheBugpageLocators.STB_LastName)
        LastNameTextField.click()
        LastNameTextField.fill("guiao")
        expect(LastNameTextField).to_have_value("guiao")
        self.page.screenshot(path="screenshots/STB_final.png")
        
        
        
