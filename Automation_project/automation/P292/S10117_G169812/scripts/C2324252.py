'''
Created on 30-Oct-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324252
TestCase Name = Portal Designer_Design Properties : Check Layout Change
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, wf_legacymainpage, vfour_portal_ribbon, vfour_portal_properties, vfour_portal_canvas, vfour_portal_run
from common.lib.basetestcase import BaseTestCase

class C2324252_TestClass(BaseTestCase):

    def test_C2324252(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        
        """ Step 1: Signin as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 2: Right click on 'BIP_xxx_Portal123_V4' and choose Edit
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
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
        time.sleep(5)
        
        """ Step 3: Add a new page and change the title to 'page_layout_check' and choose Single Area template
                    Verify the should be locked and the Prevent Layout Change should be checked and greyed out.
        """
        portal_canvas.add_page("Single Area", Page_title="page_layout_check")
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('page_layout_check', "Step 3: Verify page_layout_check is added in portal.", verify=True)
        time.sleep(1)
        portal_properties.verify_input_control('page', 'Lock Page', 'checkbox', 'Step 3.1: Verify Lock Page check Box option is checked.', checkbox_input='check')
        portal_properties.verify_input_control_enable_or_disable('page', 'Prevent Layout Change', 'checkbox', 'Step 3.2: Verify Prevent Layout Change check Box option is checked and disabled.',
                                                                  enable_status='disabled', enable_value=True, color_name='silver')
        
        """ Step 4: Click on Insert tab then click the resource tree
                    Verify that the panel has the tree embedded in it.
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(2)
        
        """ Step 5: Click the BIP icon and exit and save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        utillobj.switch_to_window(0)
        time.sleep(2)
        
        """ Step 6: Right click on 'BIP_xxx_Portal123_V4' and choose Run
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        parent_css = "#BIPortalPanel [class*='bip-canvas'] [class*='bip-page']:not([style*='hidden'])"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        
        """ Step 7: Click on 'page_layout_check' page
                    Right click on the page canvas
                    Verify that nothing shows up
        """
        portal_canvas.select_page_in_navigation_bar('page_layout_check')
        
        """ Step 8: Right click on the page tab
                    Press F8 and try to drag a folder onto the page
                    Verify that only refresh show.
                    Page Layout should NOT be on the list
                    Verify that you can't drag anything onto the page
        """
        page_value = driver.find_element_by_css_selector("#BIPortalPanel [class*='bip-canvas'] [class*='bip-page']:not([style*='hidden'])").text
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        item_path="Retail Samples->Reports"
        target_elem=driver.find_element_by_css_selector("#BIPortalPanel [class*='bip-canvas'] [class*='bip-page']:not([style*='hidden'])")
        portal_run.drag_portal_resource_tree_item(item_path, target_elem)
        time.sleep(2)
        page_value1 = driver.find_element_by_css_selector("#BIPortalPanel [class*='bip-canvas'] [class*='bip-page']:not([style*='hidden'])").text
        utillobj.asequal(page_value, page_value1, "Step 8: Verify that you can't drag anything onto the page.")
        portal_canvas.verify_page_menu('page_layout_check', ['Refresh'], 'Step 8.1: Verify Only Refresh option is visible in page menu option and Page Layout should NOT be on the list.')
        
        """ Step 9: Click Close
                    Right click on 'BIP_xxx_Portal123_V4' and choose Edit
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
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
        time.sleep(5)
        
        """ Step 10: Click on the page tab
        """
        portal_canvas.select_page_in_navigation_bar('page_layout_check')
        
        """ Step 11: Uncheck the Lock page checkbox
                    Verify that Prevent Layout Change is no longer grayed out and unchecked
        """
        portal_properties.verify_input_control('page', 'Lock Page', 'checkbox', 'Step 11: Verify Lock Page check Box option is checked.', checkbox_input='check')
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 11.1: ')
        time.sleep(2)
        portal_properties.verify_input_control('page', 'Lock Page', 'checkbox', 'Step 11.2: Verify Lock Page check Box option is Unchecked.', checkbox_input='Uncheck')
        portal_properties.verify_input_control('page', 'Prevent Layout Change', 'checkbox', 'Step 11.3: Verify Prevent Layout Change check Box option is Unchecked.', checkbox_input='Uncheck')
        portal_properties.verify_input_control_enable_or_disable('page', 'Prevent Layout Change', 'checkbox', 'Step 11.4: Verify Prevent Layout Change check Box option is enabled.',
                                                                  enable_status='enabled', enable_value=True, color_name='white')
        
        """ Step 12: Click the BIP icon and exit and save
                    Right click on 'BIP_xxx_Portal123_V4' and choose Run
        """
        portal_ribbon.bip_save_and_exit('Yes')
        utillobj.switch_to_window(0)
        time.sleep(2)
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        parent_css = "#BIPortalPanel [class*='bip-canvas'] [class*='bip-page']:not([style*='hidden'])"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        
        """ Step 13: Right click on the page canvas
                    Verify that page layout shows
        """
        page_elem = driver.find_element_by_css_selector(parent_css)
        utillobj.click_on_screen(page_elem, 'middle', click_type=1)
        expected_list = ['Page Layout']
        utillobj.select_or_verify_bipop_menu(verify=True, expected_popup_list=expected_list, msg="Step 13")
        
        """ Step 14: Right click on the page tab
                    Verify that page layout, refresh and remove my customizations shows on the list.
        """
        expected_list = ['Page Layout', 'Refresh', 'Remove My Customizations']
        portal_canvas.verify_page_menu('page_layout_check', expected_list, "Step 14: Verify that page layout, refresh and remove my customizations shows on the list. ")
        
        """ Step 15: Press F8 and Try to drag a folder (Public) onto the page
                    Verify that you now can add something onto the page
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
        item_path="P292->S10117->BIP_V4_Portal->babydeer"
        target_elem=driver.find_element_by_css_selector(parent_css)
        portal_run.drag_portal_resource_tree_item(item_path, target_elem)
        portal_canvas.verify_panel_caption('babydeer', "Step 15: Verify BabyDeer drag and drop into canvas sucessfully.")
        
        """ Step 16: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 17: Re run the portal to make sure the public panel is still there.
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        parent_css = "#BIPortalPanel [class*='bip-canvas'] [class*='bip-page']:not([style*='hidden'])"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        time.sleep(5)
        portal_canvas.verify_panel_caption('babydeer', "Step 17: Verify BabyDeer panel Displayed.")
        
        """ Step 18: Right click on the page tab
                    Choose page layout and then 2 columns
                    Verify that page layout has been changed.
        """
        portal_canvas.manage_page_menu('page_layout_check', 'Page Layout', page_layout='Two Column')
        colums=self.driver.find_elements_by_css_selector("[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bip-column']")
        utillobj.asequal(2, len(colums), "Step 18: Verify that page layout has been changed.")
        
        """ Step 19: Press F8 and Try to drag a folder onto the page
                    Verify that you now can add something onto the page
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(3)
        item_path="P292->S10117->BIP_V4_Portal->Bluehills"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 2)
        
        """ Step 20: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 21: Sign Out from WebFOCUS
        """
        time.sleep(5)
                

if __name__ == '__main__':
    unittest.main()