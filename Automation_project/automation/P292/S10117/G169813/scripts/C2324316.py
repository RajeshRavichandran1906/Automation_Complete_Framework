'''
Created on 13-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324316
TestCase Name = Portal Designer_Design Properties : Default Page
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run, wf_legacymainpage, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324316_TestClass(BaseTestCase):

    def test_C2324316(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = project_id+'->'+suite_id+'->BIP_V4_Portal'
        workspace = "Workspaces"
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text("#PortalResourcevBOX table tr td", workspace, resultobj.chart_long_timesleep)
                
        """ Step 2: Open P292 -> S10117 from domains tree.
        """
        """ Step 3: Right click on 'BIP_Responsive' portal and choose Edit
                    Make sure you have a few pages there. If not add some. It does not matter for this test if they have content or not
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_Responsive', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utilobj.switch_to_new_window()
        time.sleep(1)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_canvas.add_page('1 Column', Page_title='Default Responsive')
        time.sleep(2)
        portal_canvas.select_column(1)
        time.sleep(1)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(1)
        portal_canvas.verify_panel_caption('Panel 1', "Step 3: Verify Panel 1 added in Default Responsive page.")
        
        """ Step 4: In the properties section, choose a page to be the default. Don't choose the first page or the page that is highlighted now.
        """
        portal_properties.select_breadcrumb_panel('BIP_Responsive')
        time.sleep(1)
        
        """ Step 5: Click on any other page.
                    By design the last page chosen would be the one that shows unless the default is set.
        """
        portal_properties.edit_input_control('pageview', 'Default Page', 'combobox', combobox_input='Default Responsive')
        
        """ Step 6: Exit and save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        time.sleep(2)
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text("#PortalResourcevBOX table tr td", workspace, resultobj.chart_long_timesleep)
        
        """ Step 7: Run the portal.
                    Verify that the page chosen in that setting is the one that is highlighted now.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_Responsive', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_canvas.verify_panel_caption('Panel 1', "Step 7: Verify that the page chosen in that setting is the one that is highlighted now.")
        
        """ Step 8: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 9: In the banner link, click on the top right username > Click Sign Out.
        """

if __name__ == '__main__':
    unittest.main()