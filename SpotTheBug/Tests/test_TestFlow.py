import sys
import os

from Methods.HomePageMethods import HomePageMethod
from Methods.SpotTheBugPageMethod import SpotTheBugPageMethod
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_full_flow(page):
    home = HomePageMethod(page)
    spot_bug = SpotTheBugPageMethod(page)

    home.open_url("https://qa-practice.netlify.app/")
    home.Verify_Welcome_Header()
    home.click_sidebar_toggle()
    home.Verify_Sidebar()
    
    spot_bug.open_url("https://qa-practice.netlify.app/bugs-form")
    spot_bug.Verify_Header()
    spot_bug.Verify_FirstName_TextField()
    spot_bug.Verify_LastName_TextField()

