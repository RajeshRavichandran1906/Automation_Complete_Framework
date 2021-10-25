"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 31 December 2019
---------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9928473_TestClass(BaseTestCase):
    
    def test_C9928473(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign in to WebFOCUS as Basic User.
        """ 
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand Workspaces > P406_S31920> G875163 >Breadcrumb Trail and Search >Retail Samples in tree 
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """ Click on Visualizations in tree
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples->Visualizations')
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
        Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 >Breadcrumb Trail and Search >Retail Samples > Visualizations".
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Visualizations",'04.01')
        HomePage.Workspaces.ContentArea.verify_files(['Analytical Dashboard', 'Executive Dashboard', 'Sales by Country and Product', 'Store and Product Profits Over Time'],'04.02')
        utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)
        
        STEP_05 = """
        Click on > before Visualizations in breadcrumb trail
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow('Retail Samples')
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
        Verify drop down list appears with My Content, Reports, Charts, Documents, Visualizations, Portal, InfoApps, Mobile
        """
        HomePage.ContextMenu.verify(['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile'],'05.01')
        utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Select Reports from the drop-down list
        """
        HomePage.ContextMenu.select('Reports')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, 'Margin', 60)
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
        Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 >Breadcrumb Trail and Search >Retail Samples > Reports". 
        Verify Reports the in tree and items in Reports folder appear in the canvas area
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Reports",'06.01')
        HomePage.Workspaces.ContentArea.verify_files(['Margin by Product Category', 'Quantity Sold By Stores', 'Sales Metrics YTD', 'Yearly Product Metrics'],'06.02')
        utils.capture_screenshot("06.01", STEP_06_01,expected_image_verify=True)

        STEP_07 = """
        Click on the arrow before P406_S31920
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow('Workspaces')
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """Verify that scroll bar is displayed in the P406_S31920
        Note: If we have more No.of folders then only scroll bar displayed. Otherwise, we didn't see the scrollbar.
        """
        HomePage.ContextMenu.verify(['P406_S31920', 'Public', 'Retail Samples'],'07.01')
        '''As per testcase comemnts scroll_bar is not displayed for P406_S31920'''
        utils.capture_screenshot("07.01", STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)
        
if __name__ == "__main__":
    unittest.main()