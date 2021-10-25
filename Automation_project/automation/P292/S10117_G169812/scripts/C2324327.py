'''
Created on 12-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324327
TestCase Name = Global Resources Testing : Global Resources Menus for folders
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324327_TestClass(BaseTestCase):

    def test_C2324327(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02', 'wfinst03', 'wfinst04','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """ Step 1: Sign in as WF Administrator
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 2: Right Click on Global Resources Folder
                    Verify that ONLY Refresh shows
        """
        wf_mainpageobj.select_menu('Global Resources', expected_menu_list=['Refresh'], item_exit=True, msg='Step 2:')
        wf_mainpageobj.select_menu('P292', 'Refresh')
          
        """ Step 3: Right Click on Global Resources --> Page Templates
                    Verify that ONLY Refresh shows
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates', expected_menu_list=['Refresh'], item_exit=True, msg='Step 3')
        wf_mainpageobj.select_menu('P292', 'Refresh')
          
        """ Step 4: Right Click on Global Resources --> Page Templates --> Standard
                    Verify that ONLY Refresh, Security and Properties show
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Standard', expected_menu_list=['Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 4')
        wf_mainpageobj.select_menu('P292', 'Refresh')
          
        """ Step 5: Right Click on Global Resources --> Page Templates --> Standard --> Resources
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Standard->Resources', expected_menu_list=['Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 5')
        wf_mainpageobj.select_menu('P292', 'Refresh')
        
        """ Step 6: Right Click on Global Resources --> Page Templates --> Standard --> any page templates
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Standard->1 Column', expected_menu_list=['CopyCtrl+C', 'Security', 'Properties'], item_exit=True, msg='Step 6')
        wf_mainpageobj.select_menu('P292', 'Refresh')
        
        """ Step 7: Right Click on Global Resources --> Page Templates --> Custom
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', expected_menu_list=['New', 'PasteCtrl+V', 'Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 7')
        wf_mainpageobj.select_menu('P292', 'Refresh')
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', 'New', expected_menu_list=['PortalPage', 'Folder'], item_exit=True, msg='Step 7.1')
        
        """ Step 8: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()