"""-------------------------------------------------------------------------------------------
Author Name : Prasanth
Automated On : 29 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9928128_TestClass(BaseTestCase):
    
    def test_C9928128(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        utils.wait_for_page_loads(10)
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on 'Workspaces' tab > Click on 'Global Resources' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select('Global Resources')
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('02.00', Step_02)
        
        Step_02_01 = """
            Step 02.01 : Verify that Page Templates, Page Templates (Legacy) and Themes folders are displayed
        """
        HomePage.Workspaces.ContentArea.verify_folders(['Page Templates (Legacy)', 'Page Templates', 'Themes'], "02.01")
        utils.capture_screenshot('02.01', Step_02_01)
        
        Step_02_02 = """
            Step 02.02 : Also, Verify NO action bar is displayed
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("02.02")
        utils.capture_screenshot('02.02', Step_02_02)
        
        Step_03 = """
            Step 03 : Double click on 'Page Templates' folder in content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder('Page Templates')
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('03.00', Step_03)
        
        Step_03_01 = """
            Step 03.01 : Verify that Page Templates, Page Templates (Legacy) and Themes folders are displayed
        """
        HomePage.Workspaces.ContentArea.verify_folders(['Standard', 'Custom'], "03.01")
        utils.capture_screenshot('03.01', Step_03_01)
        
        Step_03_02 = """
            Step 03.02 : Also, Verify NO action bar is displayed
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("03.02")
        utils.capture_screenshot('03.02', Step_03_02)
        
        Step_04 = """
            Step 04 : Double click on 'Standard' folder in content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder('Standard')
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """
            Step 04.01 : Verify NO action bar is displayed
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("04.01")
        utils.capture_screenshot('04.01', Step_04_01)
        
        Step_05 = """
            Step 05 : Click on 'Custom' folder under Page Templates from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Page Templates->Custom")
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
        Verify that the 'Folder' action bar is displayed and Verify 'Assemble Visualizations' is displayed in Plus menu.
        """
        HomePage.Workspaces.ActionBar.verify_displayed("05.01")
        HomePage.Workspaces.ActionBar.verify_tab_options(['Folder'], "05.02")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        actual_status = utils.validate_and_get_webdriver_object('.pop-top .tlm-assemble', "Assemble Visualizations").is_displayed()
        msg = "Step 05.03 : Verify 'Assemble Visualizations' is displayed in Plus menu"
        utils.asequal(True, actual_status, msg)
        utils.capture_screenshot('05.01', Step_05_01)
        close_obj=utils.validate_and_get_webdriver_object('.pop-top .tool-list-menu-close-icon', "close button")
        close_obj.click()
        HomePage.Workspaces.switch_to_frame()
        
        Step_06 = """
            Step 06 : Click on 'Page Templates (Legacy)' from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Global Resources->Page Templates (Legacy)")
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('06.00', Step_06)
        
        Step_06_01 = """
            Step 06.01 : Verify that Page Templates, Page Templates (Legacy) and Themes folders are displayed
        """
        HomePage.Workspaces.ContentArea.verify_folders(['Standard', 'Custom'], "06.01")
        utils.capture_screenshot('06.01', Step_06_01)
        
        Step_06_02 = """
            Step 06.02 : Also, Verify NO action bar is displayed
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("06.02")
        utils.capture_screenshot('06.02', Step_06_02)
        
        Step_07 = """
            Step 07 : Double click on 'Standard' folder in content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder('Standard')
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('07.00', Step_07)
        
        Step_07_01 = """
            Step 07.01 : Verify NO action bar is displayed
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("07.01")
        utils.capture_screenshot('07.01', Step_07_01)
        
        Step_08 = """
            Step 08 : Click on 'Custom' folder under Page Templates from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Page Templates (Legacy)->Custom")
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('08.00', Step_08)
        
        Step_08_01 = """
            Step 08.01 : Verify that the 'Folder' and 'Portal Page' action bars are displayed
        """
        HomePage.Workspaces.ActionBar.verify_displayed("08.01")
        HomePage.Workspaces.ActionBar.verify_tab_options(['Folder', 'Portal Page'], "08.02")
        utils.capture_screenshot('08.01', Step_08_01)
        
        Step_09 = """
            Step 09 : Click on 'Themes' from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select('Global Resources->Themes')
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('09.00', Step_09)
        
        Step_09_01 = """
            Step 09.01 : Verify that 'Standard' and 'Custom' folders are displayed
        """
        HomePage.Workspaces.ContentArea.verify_folders(['Standard', 'Custom'], "09.01")
        utils.capture_screenshot('09.01', Step_09_01)
        
        Step_09_02 = """
            Step 09.02 : Also, Verify NO action bar is displayed
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("09.02")
        utils.capture_screenshot('09.02', Step_09_02)
        
        Step_10 = """
            Step 10 : Double click on 'Standard' folder in content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder('Standard')
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('10.00', Step_10)
        
        Step_10_01 = """
            Step 04.01 : Verify NO action bar is displayed
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("10.01")
        utils.capture_screenshot('10.01', Step_10_01)
        
        Step_11 = """
            Step 11 : Click on 'Custom' folder under Themes from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Themes->Custom")
        utils.wait_for_page_loads(5)
        utils.capture_screenshot('11.00', Step_11)
        
        Step_11_01 = """
            Step 11.01 : Click on 'Custom' folder under Themes from the resource tree
        """
        HomePage.Workspaces.ActionBar.verify_displayed("11.01")
        HomePage.Workspaces.ActionBar.verify_tab_options(['Folder', 'Text Editor'], "11.02")
        utils.capture_screenshot('11.01', Step_11_01)
        
        Step_12 = """
            Step 12 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('12.00', Step_12)
        
    if __name__ == "__main__":
        unittest.main()