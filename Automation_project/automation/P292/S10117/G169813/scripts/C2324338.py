'''
Created on 04-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324338
TestCase Name = Help : Help_Designer
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import wf_legacymainpage, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2324338_TestClass(BaseTestCase):

    def test_C2324338(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        core_util_object = core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = str(project_id)+'->'+str(suite_id)+'->BIP_V4_Portal'
        portal_name = 'BIP_xxx_Portal123_V4'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        help_img_css="img#showHelpButton"
        test_case_id="C2324338"
        
        """ Step 1: Sign into WebFOCUS home page as Developer User Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 2: Right click on 'BIP_xxx_Portal123_V4' and choose Edit
        """
        """ Step 3: Maximize the window
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Edit')
        core_util_object.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 190)
        
        """ Step 4: Click on the Help icon in the upper right corner
        """
        help_img_elem=self.driver.find_element_by_css_selector(help_img_css)
        utillobj.default_click(help_img_elem)
        core_util_object.switch_to_new_window()
        time.sleep(1)
        
        """ Step 5: Verify that you are in the Portal Designer Overview section
        """
        '''verify help window left panel'''
        portal_misobj.verify_help_window_left_panel('Portal Designer Overview', 'Step 9: Verify that you are in the Portal Designer Overview section.')
        
        '''verify help window right panel'''
        msg='Step 9.1: Verify that you are in the Portal Designer Overview section.'
        portal_misobj.verify_help_window_right_panel(['Business Intelligence Portal>Understanding the Structure of Business Intelligence Portals'], msg, right_panel_css="div.help_breadcrumbs")
        msg='Step 9.2: Verify that you are in the Portal Designer Overview section.'
        portal_misobj.verify_help_window_right_panel(['Portal Designer Overview'], msg)
        msg='Step 9.3: Verify that you are in the Portal Designer Overview section.'
        expected_item_list=['In this section:Creating a PortalPortal Designer InterfacePage TemplatesApplication MenuQuick Access ToolbarRibbonCanvasProperties PanelBreadcrumb Trail']
        portal_misobj.verify_help_window_right_panel(expected_item_list, msg, right_panel_css="table.nested_mini_toc")
        time.sleep(3)
        utillobj.take_browser_snapshot(test_case_id+'_Actual_Step_5')
        time.sleep(3)
        
        """ Step 6: Close the Help window
        """
        core_util_object.switch_to_previous_window()
        
        """ Step 7: Exit out of designer
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        core_util_object.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        time.sleep(1)
        
        """ Step 8: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()