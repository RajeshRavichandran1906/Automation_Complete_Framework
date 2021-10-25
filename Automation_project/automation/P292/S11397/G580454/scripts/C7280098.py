'''
Created on 26-June 2018

@author: Varun/Prasanth

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/7280098
TestCase Name = Global Resources Testing : Create_GlobalResources_Portal
'''
import unittest
from common.lib import utillity
from common.pages import wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C7280098_TestClass(BaseTestCase):

    def test_C7280098(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        
        """ 
        STEP 1: Sign into WebFOCUS home page as Administrator.
                Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, 'Workspaces', 190)
        
        """ 
        STEP 2: Right click on Global Resources Node
                Verify that only Refresh shows.
        """
        wf_mainpageobj.select_menu('Global Resources', expected_menu_list=['Refresh'], item_exit=True, msg='Step 02')
        
        """ 
        STEP 3: Open the Global Resources Node
        STEP 4: Open the Page templates folder
        STEP 5: Right click on custom
        STEP 5.01 : Verify that the following options are displayed:
                1.New
                2.Paste Ctrl+V
                3.Refresh
                4.Security
                5.Properties
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', expected_menu_list=['New', 'PasteCtrl+V', 'Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 05')
        
        """ 
        STEP 6: Hover the mouse to New
        STEP 6.01 Expected: Verify that Page and Folder options are displayed
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', 'New', expected_menu_list=['Page', 'Folder'], item_exit=True, msg='Step 06')
        
        """ 
        STEP 7: Open the Page templates (Legacy) folder
        STEP 8: Right click on custom
        STEP 8.01 : Verify that the following options are displayed:
                1.New
                2.Paste Ctrl+V
                3.Refresh
                4.Security
                5.Properties
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates (Legacy)->Custom', expected_menu_list=['New', 'PasteCtrl+V', 'Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 08')
        
        """ 
        STEP 9: Hover the mouse to New
        STEP 9.01 Expected: Verify that Page and Folder options are displayed
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates (Legacy)->Custom', 'New', expected_menu_list=['Portal Page', 'Folder'], item_exit=True, msg='Step 06')
        
        
        """ Step 6: Sign Out from WebFOCUS
        """
        
if __name__ == '__main__':
    unittest.main()