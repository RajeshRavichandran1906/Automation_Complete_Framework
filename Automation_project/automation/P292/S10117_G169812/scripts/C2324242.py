'''
Created on Oct 11, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2324242
TestCase Name = Portal Designer_Layout : Change_Layout_options_from_Layout_tab
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run, wf_legacymainpage
from common.lib import utillity


class C2324242_TestClass(BaseTestCase):

    def test_C2324242(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        
        """ Step 1: Signin as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#topBannerMenuBox [id^='BiWelcomeBannerMenuButton']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="autodevuser43", with_regular_exprestion=True)
        
        """ Step 2: Right click and Edit the portal 'BIP_xxx_Portal123_V4'
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        utillobj.switch_to_window(1)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 3: Click on Banner button and get rid of Left option
                    Verify that the page has shifted to the left
        """
        portal_ribbon.select_layout_banner(banner_area='Left', close=True)
        time.sleep(2)
        panel_obj = portal_canvas.get_panel_obj('Panel 1').location['x']
        print(panel_obj)
        if panel_obj < 20:
            utillobj.asequal(True, True, "Step 3: Verify that the page has shifted to the left")
        else:
            utillobj.asequal(True, False, "Step 3: Verify that the page has shifted to the left")
        
        """ Step 4: Click on 'Test_page' page
                    Click on style tab under image choose default
        """
        portal_canvas.select_page_in_navigation_bar('Test_Page')
        time.sleep(3)
        portal_ribbon.select_ribbon_item("Style", "Style_Image")
        time.sleep(1)
        parent_css="[id^='dlgIbfsOpenFile'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        utillobj.click_dialog_button("[id^='dlgIbfsOpenFile'] [class*='active'] [id*='BiHBox']", 'Use Default Image')
        time.sleep(3)
        
        """ Step 5: Right click on the 'Test_Page' and choose Page Layout
                    Change the layout to Fluid canvas by clicking on the Layout button and choosing Fluid canvas
                    Verify that the page layout has changed
        """
        portal_ribbon.select_tab('Layout')
        time.sleep(3)
        portal_canvas.manage_page_menu('Test_Page', 'Page Layout', page_layout='Fluid Canvas')
        portal_canvas.verify_canvas_type('fluid_canvas', "Step 5: Verify that the page layout has changed to Fluid canvas")
        
        """ Step 6: Press F8 to bring up the Resource Tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        
        """ Step 7: Drag the Retail Samples under all the panels
                    Choose the lower option. As you drag it over the Cross you will see the areas being highlighted in red
                    Verify that a Cross with options appear on the upper right area of the panel1.
                    Verify that now 4 panels are on top of panel 5
        """
        item_path="Retail Samples"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3", drop_point='bottom_middle', ty_offset=-3)
        time.sleep(5)
        portal_canvas.verify_panel_caption('Panel 5', 'Step 7: Verify that now 4 panels are on top of panel 5')
        panel_name = ['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4']
        status_ = False
        for pan in panel_name:
            panel_loc_y = portal_canvas.get_panel_obj(pan).location['y']
            panel_size = portal_canvas.get_panel_obj(pan).size['height']
            panel5 = portal_canvas.get_panel_obj('Panel 5').location['y']
            temp_obj = panel5 - (panel_loc_y + panel_size)
            if temp_obj < 15:
                status_ = True
            else:
                status_ = False
                break
        utillobj.asequal(status_, True, "Step 7.1: Verify that now 4 panels are on top of panel 5")
        
        """ Step 8: Save and exit the portal
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        time.sleep(2)
        portal_ribbon.select_tool_menu_item('menu_Exit')
        time.sleep(3)
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        utillobj.switch_to_window(0)
        parent_css = "#topBannerMenuBox [id^='BiWelcomeBannerMenuButton']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="autodevuser43", with_regular_exprestion=True)
        
        """ Step 9: Run the portal and verify the changes
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        parent_css="div[class*='menu'][class*='bar'][class*='item'] [class*='menu'][class*='button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="autodevuser43", with_regular_exprestion=True)
        time.sleep(8)
        panel_name = ['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4']
        i=0
        for pan in panel_name:
            portal_canvas.verify_panel_caption(pan, 'Step 9.'+str(i)+': Verify that now 4 panels are on top of panel 5')
            i+=1
        status_ = False
        for pan in panel_name:
            panel_loc_y = portal_canvas.get_panel_obj(pan).location['y']
            panel_size = portal_canvas.get_panel_obj(pan).size['height']
            panel5 = portal_canvas.get_panel_obj('Panel 5').location['y']
            temp_obj = panel5 - (panel_loc_y + panel_size)
            if temp_obj < 15:
                status_ = True
            else:
                status_ = False
                break
        utillobj.asequal(status_, True, "Step 9"+str(i)+": Verify that now 4 panels are on top of panel 5")
        
        """ Step 10: Close portal and Sign Out from WebFOCUS
        """
        time.sleep(3)
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()