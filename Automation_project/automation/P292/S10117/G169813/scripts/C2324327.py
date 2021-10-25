'''
Created on 12-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324327
TestCase Name = Global Resources Testing : Global Resources Menus for folders
'''
import unittest, time
from common.lib import utillity
from common.pages import wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324327_TestClass(BaseTestCase):

    def test_C2324327(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        
        """ Step 1: Sign into WebFOCUS home page as Administrator
                    Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        time.sleep(1)
        
        """ Step 2: Right Click on Global Resources Folder
                    Verify that ONLY Refresh shows
        """
        wf_mainpageobj.select_menu('Global Resources', expected_menu_list=['Refresh'], item_exit=True, msg='Step 2:')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
          
        """ Step 3: Right Click on Global Resources --> Page Templates
                    Verify that ONLY Refresh shows
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates', expected_menu_list=['Refresh'], item_exit=True, msg='Step 3')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
          
        """ Step 4: Right Click on Global Resources --> Page Templates --> Standard
                    Verify that ONLY Refresh, Security and Properties show
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Standard', expected_menu_list=['Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 4')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
          
        """ Step 5: Right Click on Global Resources --> Page Templates --> Standard --> Resources
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Standard->Resources', expected_menu_list=['Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 5')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
        
        """ Step 6: Right Click on Global Resources --> Page Templates --> Standard --> any page templates
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Standard->1 Column', expected_menu_list=['CopyCtrl+C', 'Security', 'Properties'], item_exit=True, msg='Step 6')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
        
        """ Step 7: Right Click on Global Resources --> Page Templates --> Custom
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', expected_menu_list=['New', 'PasteCtrl+V', 'Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 7')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', 'New', expected_menu_list=['PortalPage', 'Folder'], item_exit=True, msg='Step 7.1')
        
        """ Step 8: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()