'''
Created on Sep 18, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324241
TestCase Name = Run Mode_Run Content : Run_Portal_Verify_changes_and_Close
'''

import unittest, time
from common.lib import utillity
from common.pages import vfour_portal_run, vfour_portal_canvas, vfour_portal_ribbon,wf_legacymainpage
from common.lib.basetestcase import BaseTestCase


class C2324241_TestClass(BaseTestCase):

    def test_C2324241(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        v4p_ribbon=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        vfour_canvasobj = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        proj_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        parent_folder_name='BIP_V4_Portal'
        BIP_Portal_Path = str(proj_id)+'->'+str(suite_id)+'->'+parent_folder_name
        
        """
        Step 01: Sign in as WF Developer
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        time.sleep(5)        

        """
        Step 02: Right click on portal 'BIP_xxx_Portal123_V4' and run the portal; 
        """
        wf_mainobj.select_repository_menu(BIP_Portal_Path+'->BIP_xxx_Portal123_V4', 'Run')
        time.sleep(4)
        element_css="#BIPortalPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 190)
        
        """
        Step 02.1: Verify the recent changes made in the portal edit mode is available in run mode;
        """
        vfour_canvasobj.verify_page_in_navigation_bar('Test_Page', "Step 2: Verify Test_Page in Navigation Bar.")
        vfour_runobj.verify_number_of_portal_panel(4, "Step2.a:")
        vfour_runobj.verify_portal_panel_label(['Panel 1','Panel 2','Panel 3','Panel 4'], "Step2.b:")
        user_id = utillobj.parseinitfile('mrid03')
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Enable Accessibility', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
        else:
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
        
        v4p_ribbon.verify_menu_bar_style(menu_item_font_name='Arial', menu_item_font_size=9, menu_item_bold=True, menu_item_italic=True, 
                                                     menu_item_underline=True, border_width=4, menu_item_text_color='blue',
                                                     border_color='red', border_style='solid', menubar_background='yellow')
        
        
        """verify Panel 1"""
        utillobj.verify_object_visible("div[id^='BidTreeBlock'][class*='bi-component']", True, 'Step 2.d: Panel1 Visible')
        utillobj.verify_object_visible("#treeView tbody>tr>td>img[src*='discovery_domain']", True, 'Step 2.e: Panel Domain tree Visible')
        """verify Panel 2"""
        utillobj.verify_object_visible("div[id^='BipContentArea'][class*='bi-component bip-panel-pane'] div[id^='BipPortalTree']", True, 'Step 2.f: Panel2 portal list Visible')
        """verify Panel 3"""
        utillobj.verify_object_visible("textarea[class*='bi-text-field text-field bip-panel-pane']", True, 'Step 2.g: Panel3 textarea Visible')
        """verify Panel 4"""
        utillobj.verify_object_visible("div[id^='BipContentArea'][class*='bi-component bip-panel-pane'] img[src*='babydeer']", True, 'Step 2.h: Panel4 babydeer Visible')
        
        """
        Step 03: Open the 'BIP_xxx_Portal123_V4' portal's resource folder.
        Step 04: Drag a page onto the page canvas
        """
        v4p_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(9)
        target_elem = driver.find_element_by_css_selector("#BIPortalPanel")
        msg='Step 04: Verify that you get the no drop icon'
        vfour_canvasobj.verify_no_drag_drop_icon_on_canvas(BIP_Portal_Path+'->BIP_xxx_Portal123_V4 Resources->Test_Page', target_elem, 'C2324241', msg, ty_offset=150, mouse_move_duration=1)
         
        """
        Step 05: Close the portal run mode.
        """
        vfour_runobj.select_or_verify_portal_menu_bar_item(select='Close')
        time.sleep(2)
        
        """
        Step 6:In the banner link, click on the top right username > Click Sign Out.
        """
                                
if __name__ == '__main__':
    unittest.main()