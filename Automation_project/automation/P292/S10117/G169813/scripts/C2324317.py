'''
Created on 03-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324317
TestCase Name = Run Mode_Run Content : Replacing content at run-time
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import visualization_resultarea, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run, vfour_portal_properties, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324317_TestClass(BaseTestCase):

    def test_C2324317(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = project_id+'->'+suite_id+'->BIP_V4_Portal'
        
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        
        """ Step 2: Open P292 -> S10117 from domains tree,
                    Edit 'BIP_xxx_portal123_V4' portal
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_xxx_Portal123_V4', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        coreutillobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(5)
        
        """ Step 3: Unlock Page 1
                    Verify that is a 2 column layout page. If not please change the layout
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 3: ')
        
        """ Step 4: Save the portal
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        coreutillobj.switch_to_previous_window(window_close=False)
        time.sleep(5)
        
        """ Step 5: Run portal
                    Drag Category Sales from Retail Samples-->Portal-->Small Widgets folder to Unlocked page
                    Verify that the report shows
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 2)
        time.sleep(5)
        portal_canvas.verify_panel_caption('Category Sales', "Step 5: Verify Category Sales Panel able to drag into canvas.")
        
        """ Step 6: Close portal and Run Portal again
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """Step 7:Navigate URL to http://environment_name:port/alias/legacyhome and and Run Portal again"""
        
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        
        """ Step 8: Replace Category Sales with Regional Sales Trend by dragging the report from F8 into the existing container and choose Replace Content
                    Verify that the report shows
        """
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 2)
        utillobj.select_or_verify_bipop_menu('Replace Content', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden'])")
        time.sleep(5)
        portal_canvas.verify_panel_caption('Regional Sales Trend', "Step 7: Verify Regional Sales Trend Panel able to drag into canvas.")
        
        """ Step 9: Close portal and Run
                    Verify that you get no errors like "Error: Application error: name _contentArea already exists in name scope"
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """Step 10:Navigate URL to http://environment_name:port/alias/legacyhome and and Run Portal again"""
        
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_canvas.verify_panel_caption('Regional Sales Trend', "Step 8: Verify Regional Sales Trend Panel able to drag into canvas.")
        
        """ Step 11: Close the portal
            Step 12: If you got an error in step 8 Remove customization of the portal and it will become usable again.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 13: In the banner link, click on the top right username > Click Sign Out.
        """
        time.sleep(2)
                

if __name__ == '__main__':
    unittest.main()