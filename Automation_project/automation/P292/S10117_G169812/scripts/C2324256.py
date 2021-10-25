'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324256
TestCase Name = Cut_Paste_portal_object_testing
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324256_TestClass(BaseTestCase):

    def test_C2324256(self):
        """
        TESTCASE VARIABLES
        """
        driver = self.driver
        portal_name = 'Easy_Selector'
        BIP_Portal_Path = 'P292->S10117->BIP_V4_Portal'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+'->'+suite_id
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 2: Expand P292->S10117 from domains tree,
                    Right click on 'Easy_Selector' portal and choose Cut
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+"->"+portal_name, 'Cut')
        
        """ Step 3: Expand P292 , right click on S10117 folder
                    In HomePage, verify that Paste option is NOT enabled and is greyed out
                    In Legacyhome page, verify Paste option is enabled
        """
        wf_mainpageobj.verify_repository_menu_enabled(folder_path+'->BIP_V4_Portal','Paste Ctrl+V', enabled=True)
        
        """ Step 4: Right click on 'BIP_V4_Portal' folder
                    Choose Paste
                    Verify duplicate version of portal is created under the 'BIP_V4_Portal' folder.
        """
        time.sleep(2)
        wf_mainpageobj.select_menu(folder_path+'->BIP_V4_Portal_upload','Paste')
        driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        wf_mainpageobj.verify_repositery_item(folder_path+'->BIP_V4_Portal_upload', portal_name ,item_exit=True, msg="4")
        
        """ Step 5: Sign Out from WebFOCUS
        """
        time.sleep(5)
                

if __name__ == '__main__':
    unittest.main()