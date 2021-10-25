'''
Created on 11-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324326
TestCase Name = Global Resources Testing : Create_GlobalResources_Portal
'''
import unittest, time
from common.lib import utillity
from common.pages import wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324326_TestClass(BaseTestCase):

    def test_C2324326(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        workspace = "Workspaces"
        
        """ Step 1: Sign into WebFOCUS home page as Administrator.
                    Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        time.sleep(1)
        
        """ Step 2: Right click on Global Resources Node
                    Verify that only Refresh shows.
        """
        wf_mainpageobj.select_menu('Global Resources', expected_menu_list=['Refresh'], item_exit=True, msg='Step 2:')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
        
        """ Step 3: Open the Global Resources Node
        """
        """ Step 4: Open the Page templates folder
        """
        """ Step 5: Right click on custom
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', expected_menu_list=['New', 'PasteCtrl+V', 'Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 3')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', 'New', expected_menu_list=['PortalPage', 'Folder'], item_exit=True, msg='Step 3.1')
        
        """ Step 6: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()