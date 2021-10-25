'''
Created on Sep 11, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324237
TestCase Name = Run Mode : Run_the_Portal
'''

import unittest, time
from common.lib import utillity
from common.pages import vfour_portal_run, wf_legacymainpage, vfour_portal_ribbon 
from common.lib.basetestcase import BaseTestCase

class C2324237_TestClass(BaseTestCase):

    def test_C2324237(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        user_id = utillobj.parseinitfile('mrid03')
        browser=utillobj.parseinitfile('browser')
        
        """
        Step 01: Sign into WebFOCUS home page as Developer User
                 Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)

        """
        Step 02: Double click the portal 'BIP_xxx_Portal123_V4' under P292 domain ->S10117 folder to run it
        """
        wf_mainobj.select_repository_menu(project_id+'->'+suite_id+'->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        time.sleep(4)
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        time.sleep(3)
        
        
        """
        Step 02.1: Verify the changes that we made in the portal design mode are available in run mode;
        """
         
        if browser == 'IE':
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
        else:
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
         
         
        """
        Step 02.2: Verify the URL is correct. the machine name might be different for your testing. make sure its softcontext/portal/parent folder/portal name
        """
        current_url = driver.current_url
        portal_url = "/portal/"+project_id+"/"+suite_id+"/BIP_V4_Portal/BIP_xxx_Portal123_V4"
        utillobj.asin(portal_url, current_url, "Step 02.2: Verify the portal URL is correct")
         
        """
        Step 03: Bring up the F8 tree and scroll to the right
        Verify that white spaces appear
        """
        tree_css=driver.find_element_by_css_selector("#BIPortalPanel")
        utillobj.click_on_screen(tree_css, 'middle')
        time.sleep(3)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        utillobj.synchronize_until_element_is_visible("#treeContainer", 39)
        utillobj.verify_object_visible("#treeContainer", True, 'Step 03: Resource tree Visible')
        tree_css=driver.find_element_by_css_selector("#treeContainer")
        utillobj.click_on_screen(tree_css, 'bottom_left', x_offset=36, y_offset=-9)
        scroll_resource = utillobj.get_object_screen_coordinate(tree_css, coordinate_type='bottom_left', x_offset=36, y_offset=-9)
        time.sleep(2)
        utillobj.drag_drop_on_screen(sx_offset=scroll_resource['x']+9,sy_offset=scroll_resource['y'],tx_offset=scroll_resource['x']+119,ty_offset=scroll_resource['y']+0)
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#treeContainer")
        utillobj.take_screenshot(ele,'C2324237_Actual_step03')
         
        """
        Step 04: Close the F8 resource tree
        """
        time.sleep(3)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=False)
        utillobj.synchronize_until_element_disappear("#treeContainer", 39)
        utillobj.verify_object_visible("#treeContainer", False, 'Step 04: Resource tree closed')
         
        """
        Step 05: Press F8 to bring the tree back
        Verify that it shows the original state.
        """
        time.sleep(3)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        utillobj.synchronize_until_element_is_visible("#treeContainer", 39)
        utillobj.verify_object_visible("#treeContainer", True, 'Step 05: Verify Resource tree shows the original state')
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#treeContainer")
        utillobj.take_screenshot(ele,'C2324237_Actual_step05')
         
        """
        Step 06: Close the resource tree.
        Close portal
        """
        time.sleep(3)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=False)
        utillobj.synchronize_until_element_disappear("#treeContainer", 39)
        utillobj.verify_object_visible("#treeContainer", False, 'Step 06: Close the resource tree')
        vfour_runobj.select_or_verify_portal_menu_bar_item(select='Close', msg='Step 06: Close the portal run mode by clicking on the Close Menubar link.')

        """
        Step 07: In the banner link, click on the top right username > Click Sign Out.
        """
        
if __name__ == '__main__':
    unittest.main()        