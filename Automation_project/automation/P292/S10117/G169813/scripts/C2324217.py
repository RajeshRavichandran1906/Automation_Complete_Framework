'''
Created on 28-Aug-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324217
TestCase Name = Portal Designer_Design Tree : Create_and_Delete_folder_from_F8_Resource_Tree
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import vfour_miscelaneous, wf_legacymainpage, vfour_portal_ribbon
from common.lib.basetestcase import BaseTestCase

class C2324217_TestClass(BaseTestCase):

    def test_C2324217(self):

        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        vfour_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        portal_path = project_id+'->'+suite_id+'->'
        
        """ Step 1: Sign in as WF Developer
            Step 2: Open 'P292_S10032' domain and edit 'BIP_xxx_Portal123_V4' portal
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        wf_mainpageobj.select_repository_menu(portal_path+'BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        core_utilobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """ Step 3: Press F8 to invoke resource tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(5)
        
        """ Step 4: Right click on the 'P292_S10032' domain and choose New > Folder. 
                    Enter 'aaa_BIP' and click the OK button
        """
        vfour_misobj.create_resource_folder(portal_path+'BIP_V4_Portal', 'aaa_BIP')
        time.sleep(2)
        
        """ Step 5: Verify aaa_BIP folder appears under the domain
        """
        vfour_misobj.verify_resource_item(portal_path+'BIP_V4_Portal->aaa_BIP', 'aaa_BIP', '5')
        time.sleep(2)
        
        """ Step 6: Right click on 'aaa_BIP' and delete
                    Click Yes
                    Verify the confirmation deletion window
                    Verify 'aaa_BIP' folder is deleted from Resource tree
        """
        vfour_misobj.delete_resource_item(portal_path+'BIP_V4_Portal->aaa_BIP')
        
        """ Step 6: Right mouse click to refresh the Repository and make sure the folder is gone.
                    Verify 'aaa_BIP' folder is deleted from Resource tree
        """
        time.sleep(2)
        vfour_misobj.verify_resource_item(portal_path+'BIP_V4_Portal->BIP_xxx_Portal123_V4', 'aaa_BIP', '6', item_exit=False)
        
        """ Step 7: Exit portal
                    Sign Out from WebFOCUS
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        time.sleep(5)
        

if __name__ == '__main__':
    unittest.main()
    