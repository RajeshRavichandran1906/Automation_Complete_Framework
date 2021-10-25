"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 21 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927751_TestClass(BaseTestCase):
    
    def test_C9927751(self):
        
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
            Step 02.00 : Click the 'Workspaces' tab
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples
        """
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verify user sees 'Breadcrumb Trail and Search' folder.
        """
        expected_items = ['Breadcrumb Trail and Search']
        HomePage.Workspaces.ResourcesTree.verify_items(expected_items, "03.01", assert_type = "asin")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Click on Visualizations in tree
        """
        HomePage.Workspaces.ResourcesTree.select("Visualizations")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify breadcrumb trail is "Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > Visualizations".
            Also,Verify Visualizations is selected in tree and the following items are appear in content area
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Visualizations"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "04.01")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Revert back the Home Page by its default state (Click on 'Workspaces' from the navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            Step 06.00 : Expand Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            Step 07.00 : Click on Visualizations in tree
        """ 
        HomePage.Workspaces.ResourcesTree.select("Visualizations")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify breadcrumb trail is "Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > Visualizations".
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Visualizations"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "07.01")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : Click on > before Visualizations in breadcrumb trail
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow("Retail Samples")
        utils.capture_screenshot("08.00", STEP_08)
        
        STEP_8_01 = """
            Step 08.01 : Verify drop down list appears with My Content, Reports, Charts, Documents, Visualizations, Portal, InfoApps, Mobile
        """
        expected_menus = ['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile']
        HomePage.ContextMenu.verify(expected_menus, "08.01")
        utils.capture_screenshot("08.01", STEP_8_01, expected_image_verify = True)
        
        STEP_09 = """
            Step 09.00 : Revert back the Home Page by its default state (Click on 'Workspaces' from the navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("09.00", STEP_09)
        
        STEP_10 = """
            Step 10.00 : Expand Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > click on Visualizations
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples->Visualizations")
        utils.capture_screenshot("10.00", STEP_10)
        
        STEP_10_01 = """
            Step 10.01 : Verify breadcrumb trail is "Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > Visualizations"
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Visualizations"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "10.01")
        utils.capture_screenshot("10.01", STEP_10_01, expected_image_verify = True)
        
        STEP_11 = """
            Step 11.00 : Click on > before Visualizations in the breadcrumb
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow("Retail Samples")
        utils.capture_screenshot("11.00", STEP_11)
        
        STEP_11_01 = """
            Step 11.01 : Verify the drop-down list appears with My Content, Reports, Charts, Documents, Visualizations (appears in bold), Portal, InfoApps, Mobile
        """
        expected_menus = ['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile']
        HomePage.ContextMenu.verify(expected_menus, "11.01")
        expected_menus = ['Visualizations']
        HomePage.ContextMenu.verify_bold_text_options(expected_menus, "11.02")
        utils.capture_screenshot("11.01", STEP_11_01, expected_image_verify = True)
        
        STEP_12 = """
            Step 12.00 : Select Reports from the drop-down list
        """
        HomePage.ContextMenu.select("Reports")
        utils.capture_screenshot("12.00", STEP_12)
        
        STEP_12_01 = """
            Step 12.01 : Verify breadcrumb trail is "Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > Reports". 
            Verify Reports the in tree and items in Reports folder appear in the canvas area
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Reports"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "12.01")
        expected_files = ['Margin by Product Category', 'Quantity Sold By Stores', 'Sales Metrics YTD', 'Yearly Product Metrics']
        HomePage.Workspaces.ContentArea.verify_files(expected_files, "12.02", assert_type = "asin")
        expected_folders = ['Auto Link Targets']
        HomePage.Workspaces.ContentArea.verify_folders(expected_folders, "12.02", assert_type = "asin")
        utils.capture_screenshot("12.01", STEP_12_01, expected_image_verify = True)
        
        STEP_13 = """
            Step 13.00 : Revert back the Home Page by its default state (Click on 'Workspaces' from the navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("13.00", STEP_13)
        
        STEP_14 = """
            Step 14.00 : Expand Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples")
        utils.capture_screenshot("14.00", STEP_14)
        
        STEP_15 = """
            Step 15.00 :  Click on Charts in the tree
        """
        HomePage.Workspaces.ResourcesTree.select("Charts")
        utils.capture_screenshot("15.00", STEP_15)
        
        STEP_15_01 = """
            Step 15.01 : Verify breadcrumb trail is "Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > Charts"
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Charts"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "15.01")
        utils.capture_screenshot("15.01", STEP_15_01, expected_image_verify = True)
        
        STEP_16 = """
            Step 16.00 : Click on > before Charts in the breadcrumb trail
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow("Retail Samples")
        utils.capture_screenshot("16.00", STEP_16)
        
        STEP_17 = """
            Step 17.00 : Select Visualization
        """
        HomePage.ContextMenu.select("Visualizations")
        utils.capture_screenshot("17.00", STEP_17)
        
        STEP_17_01 = """
            Step 17.01 : Verify breadcrumb trail is "Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples >Visualizations"
            Verify Visualizations folder is selected in tree and items are listed in the content area
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Visualizations"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "17.01")
        utils.capture_screenshot("17.01", STEP_17_01, expected_image_verify = True)
        
        STEP_18 = """
            Step 18.00 : Revert back the Home Page by its default state (Click on 'Workspaces' from the navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("18.00", STEP_18)
        
        STEP_19 = """
            Step 19.00 : Expand Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875163->Breadcrumb Trail and Search")
        utils.capture_screenshot("19.00", STEP_19)
        
        STEP_20 = """
            Step 20.00 : Click on Retail Samples in the tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot("20.00", STEP_20)
        
        STEP_21 = """
            Step 21.00 : Click the ">" to the left of the Retail Samples in breadcrumbs
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow("Breadcrumb Trail and Search")
        utils.capture_screenshot("21.00", STEP_21)
        
        STEP_21_01 = """
            Step 21.01 : Verify no error occurs and drop-down lists with the sub folder Retail Samples (appears in bold)
        """ 
        expected_menus = ['Retail Samples']
        HomePage.ContextMenu.verify(expected_menus, "21.01")
#         expected_menus = ['Retail Samples']
        HomePage.ContextMenu.verify_bold_text_options(expected_menus, "11.02")
        utils.capture_screenshot("21.01", STEP_21_01, expected_image_verify = True)
        
        STEP_22 = """
            Step 22.00 : Expand Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples
        """
#         HomePage.Workspaces.NavigationBar.select_workspaces()
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples")
        utils.capture_screenshot("22.00", STEP_22)
        
        STEP_23 = """
            Step 23.00 : Click on Reports in the tree
        """
        HomePage.Workspaces.ResourcesTree.select("Reports")
        utils.capture_screenshot("23.00", STEP_23)
        
        STEP_24 = """
            Step 24.00 : Click on arrow before P406_S31920
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow("Workspaces")
        utils.capture_screenshot("24.00", STEP_24)
        
        STEP_24_01 = """
            Step 24.01 : Verify that scroll bar is displayed in the P406_S31920
            Note: If we have more No.of folders then only scroll bar displayed. Otherwise, we didn't see the scrollbar.
        """
        expected_menus = ['P406_S31920', 'Public', 'Retail Samples']
        HomePage.ContextMenu.verify(expected_menus, "24.01", assert_type = "asin")
        utils.capture_screenshot("24.01", STEP_24_01, expected_image_verify = True)
        
        STEP_25 = """
            Step 25.00 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("25.00", STEP_25)
        
if __name__ == "__main__":
    unittest.main() 