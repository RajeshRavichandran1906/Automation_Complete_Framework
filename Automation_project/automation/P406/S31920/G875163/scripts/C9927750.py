"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 21 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9927750_TestClass(BaseTestCase):
    
    def test_C9927750(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
    
        STEP_01 = """
        Step 01.Sign in to WebFOCUS as Developer User..
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00',STEP_02)
    
        STEP_03 = """
        Expand Workspaces > P406_S31920> G875163 >Click "Breadcrumb Trail and Search" in tree
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G875163->Breadcrumb Trail and Search')
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_03_01 = """
        Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs('Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search','03.01')
        utils.capture_screenshot('03.01',STEP_03_01,expected_image_verify=True)
        
        STEP_04 = """
        Expand Breadcrumb Trail and Search > Click on Retail Samples in tree
        """
        HomePage.Workspaces.ResourcesTree.select('Breadcrumb Trail and Search->Retail Samples')
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_04_01 = """
        Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search > Retail Samples
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs('Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples','04.01')
        utils.capture_screenshot('04.01',STEP_04_01,expected_image_verify=True)
        
        STEP_05 = """ Expand Retail Samples in tree > Click on Charts in the content area
        """
        HomePage.Workspaces.ContentArea.select_folder("Charts")
        
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """Verify still breadcrumb trail is "Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search > Retail Samples"
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs('Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples','05.01')
        utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """Double click on Charts in the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder('Charts')
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search > Retail Samples > Charts"
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs('Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Charts','06.01')
        utils.capture_screenshot('06.01',STEP_06_01,expected_image_verify=True)
        
        STEP_07 = """Click on > before Charts in breadcrumb trail
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow('Retail Samples')
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """Verify drop down list appears with My Content, Reports, Charts, Documents, Visualizations, Portal, InfoApps, Mobile and Hidden Content
        """
        HomePage.ContextMenu.verify(['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile', 'Hidden Content'],'07.01')
        utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """Select Documents from drop down list
        """
        HomePage.ContextMenu.select('Documents')
        utils.capture_screenshot('08.00',STEP_08)
        
        STEP_08_01 ="""Verify breadcrumb trail is "Workspaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > Documents".
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Documents",'05.01')
        utils.capture_screenshot('08.01',STEP_08_01)
        
        STEP_08_02 = """Verify Documents is selected in tree and items ('Regional Analysis and Sales by Region Dashboard') in Documents folder appear in canvas area
        """
        HomePage.Workspaces.ContentArea.verify_files(['Regional Analysis', 'Sales by Region Dashboard'],'08.02')
        utils.capture_screenshot('08.02',STEP_08_02)
        
        STEP_09 = """Revert back the Home Page by its default state (Click on 'Workspaces' from the navigation bar)
        """
        utils.capture_screenshot('09.00',STEP_09)
        
        STEP_10 = """In the banner link, click on the top right username > Sign out."""
        utils.capture_screenshot('10.00',STEP_10)
        
        
if __name__ == "__main__":
    unittest.main() 