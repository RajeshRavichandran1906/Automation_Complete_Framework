'''
Created on 11-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324326
TestCase Name = Global Resources Testing : Create_GlobalResources_Portal
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324326_TestClass(BaseTestCase):

    def test_C2324326(self):
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
        
        """ Step 2: Right click on Global Resources Node
                    Verify that only Refresh shows.
        """
        wf_mainpageobj.select_menu('Global Resources', expected_menu_list=['Refresh'], item_exit=True, msg='Step 2:')
        wf_mainpageobj.select_menu('P292', 'Refresh')
        
        """ Step 3: Open the Global Resources Node
        """
        """ Step 4: Open the Page templates folder
        """
        """ Step 5: Right click on custom
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', expected_menu_list=['New', 'PasteCtrl+V', 'Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 3')
        wf_mainpageobj.select_menu('P292', 'Refresh')
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', 'New', expected_menu_list=['PortalPage', 'Folder'], item_exit=True, msg='Step 3.1')
        
        """ Step 6: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()