'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324256
TestCase Name = Cut_Paste_portal_object_testing
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324256_TestClass(BaseTestCase):

    def test_C2324256(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver
        portal_name = 'Easy_Selector'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+'->'+suite_id
        BIP_Portal_Path = folder_path+'->BIP_V4_Portal'
        
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        
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
        wf_mainpageobj.expand_tree(project_id)
        wf_mainpageobj.select_menu(folder_path+'->BIP_V4_Portal','Paste')
        driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        wf_mainpageobj.verify_repositery_item(folder_path+'->BIP_V4_Portal->'+portal_name, portal_name ,item_exit=True, msg="04.00")
        
        """ Step 5: Sign Out from WebFOCUS
        """
        time.sleep(1)
                

if __name__ == '__main__':
    unittest.main()