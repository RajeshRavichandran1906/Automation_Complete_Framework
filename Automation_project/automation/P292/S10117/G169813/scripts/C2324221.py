'''
Created on Sep 8, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324221
TestCase Name = Portal Designer_Design Properties : Rename_Default_page
'''

import unittest, time
from common.lib import utillity
from common.lib import core_utility
from common.pages import vfour_portal_ribbon, wf_legacymainpage, vfour_portal_canvas, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324221_TestClass(BaseTestCase):

    def test_C2324221(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+'->'+suite_id
        
        
        """
        Step 01: Sign in as WF Developer
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)

        """
        Step 02: Edit 'BIP_xxx_Portal123_V4' from P292 domain->S10117 folder
        """
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, 190)
        
        """ 
        Step 3: Click on Page 1
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(3)
        
        """ 
        Step 4: Enter 'Page_New' in the Title section of properties
        """
        portal_properties.edit_input_control('page', 'Title', 'textbox', textbox_input='Page_New')
        time.sleep(2)
        """Verify that the title got changed on the page tab and also in the properties section"""
        portal_canvas.verify_page_in_navigation_bar('Page_New', 'Step 4: Verify that the title got changed on the page tab and also in the properties section')
        
        
        """ 
        Step 5: Save and exit portal
        """
        time.sleep(2)
        vfour_ribbonobj.select_tool_menu_item('menu_Save')
        time.sleep(3)
        vfour_ribbonobj.select_tool_menu_item('menu_Exit')
        time.sleep(2)
        core_utillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        
        """ 
        Step 6: Sign Out from WebFOCUS
        """
        
if __name__ == '__main__':
    unittest.main()