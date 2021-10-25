'''
Created on 12-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324318
TestCase Name = Run Mode_Run Content : Adding Content at run time
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon
from common.pages import vfour_miscelaneous, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324318_TestClass(BaseTestCase):

    def test_C2324318(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        Test_Case_ID="C2324318"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = project_id+'->'+suite_id+'->BIP_V4_Portal'
        portal_name = 'test_run_content'
        
        """ 
            Step 1: Sign into WebFOCUS home page as Developer User
            Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        wf_mainpageobj.select_menu(workspace, 'View->Display By Title')
        
        """ Step 2: Expand P292 domain , right click on S10117 folder,
                    Create a new portal named 'test_run_content'
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        coreutillobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
        portal_misobj.verify_page_template("Step 02.00: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
        
        """ Step 3: Choose the Single Area layout and name it as 'page1_self_service'
        """
        portal_misobj.select_page_template(page_template="Single Area", Page_title='page1_self_service', btn_name='Create')
                
        """ Step 4: Unlock the page
                    Save and exit the portal
        """
        portal_canvas.select_page_in_navigation_bar('page1_self_service')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 04.00: ')
        time.sleep(2)
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        
        """ Step 5: Run the portal
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
        
        """ Step 6: Drag the 'page1_self_service' page in the page tab area
                    Verify that you get a message stating the page already is in the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Resources')
        item_path=BIP_Portal_Path+"->test_run_content Resources->page1_self_service"
        target_elem=driver.find_element_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipAddButton']")
        portal_run.drag_portal_resource_tree_item(item_path, target_elem)
        time.sleep(1)
        als = driver.switch_to.alert
        actual_alert_msg=als.text
        utillobj.asin(actual_alert_msg,'Page already in portal.', "step 06.00: Verify that you get a message stating the page already is in the portal")
        time.sleep(5)
        driver.switch_to_default_content()
        """ Step 7: Under Workspaces > P292_S10117_G169813 > S10117 > C2324318 Resources folder 
        > drag and drop 'Page_Unlock' onto the page tab area and change the title as 'Page_title_changed'
        """
        item_path="P292_S10117_G169813->S10117->C2324318 Resources->Page_Unlock"
        target_elem=driver.find_element_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipAddButton']")
        portal_run.drag_portal_resource_tree_item(item_path, target_elem)
        time.sleep(1)
        portal_canvas.manage_page_menu('Page_Unlock', 'Change Title', change_title='Page_title_changed')
        time.sleep(3)
        
        """ Step 8: Close and Navigate URL to http://environment_name:port/alias/legacyhome
        """ 
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        
        """ Step 9: Rerun the portal"""
        
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
        portal_canvas.verify_page_in_navigation_bar('Page_title_changed', 'Step 09.01: Verify that the title change is still there.')
        
        """ Step 10: Right click on the second page and choose Remove
        """
        portal_canvas.manage_page_menu('Page_title_changed', 'Remove')
        
        """ Step 11: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 12:In the banner link, click on the top right username > Click Sign Out.
        """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()