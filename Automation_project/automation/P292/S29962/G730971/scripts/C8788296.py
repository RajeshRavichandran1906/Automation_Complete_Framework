'''
Created on July 24, 2019

@author: Vpriya

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/8788296
TestCase Name : Add Personal Pages as Dev User
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.locators import wf_mainpage_locators
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.designer_portal import Two_Level_Side
from common.wftools.designer_portal import Canvas

class C8788296_TestClass(BaseTestCase):

    def test_C8788296(self):
        """
            CLASS OBJECTS 
        """
        login    = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils  = UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utils =CoreUtillityMethods(self.driver)
        portal =Two_Level_Side(self.driver)
        portal_canvas = Canvas(self.driver)
        
        """
            TESTCASE CSS 
        """
        
        PORTAL_NAME = 'v5portal1dev'
        project_id= core_utils.parseinitfile('project_id')
        Suite_id = core_utils.parseinitfile('suite_id')
        group_id = core_utils.parseinitfile('group_id')
        
        repository_folder = project_id+'_'+Suite_id+'->'+group_id
        expected_error_message = "Title cannot be empty"
        workspace = 'Workspaces'
        
        """
        Step 1:Login WF as developer.
        """
        login.invoke_home_page('mrid','mrpass')

        """
        Step 2:Click on Content view from side bar
        """
        utils.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, homepage.home_page_medium_timesleep)
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, homepage.home_page_medium_timesleep)
        
        """
        Step 3:Expand 'P292_S19901' domain-> Click on 'G671753' folder;
        Right click on 'v5portal1dev' and click on Run
        """
        homepage.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, PORTAL_NAME, homepage.home_page_medium_timesleep)
        homepage.right_click_folder_item_and_select_menu(PORTAL_NAME,'Run')
        
 
        """
        Step 4:Click on 'My Pages' menu;
        Click (+) below and choose Grid 4-2-1 template.
        
        Verify 'Page1' has been created whereas all panels have the easy selector + sign at the center
        """
        
        core_utils.switch_to_new_window()
        portal.click_on_plus_icon_under_the_folder_in_left_sidebar('My Pages')
        portal.select_new_page_template("Grid 4-2-1")
        utils.synchronize_until_element_is_visible(".pd-header-buttons-wrapper",homepage.chart_long_timesleep)
        
        """
        Step 5:Click the delete icon for 'Page 1' >> Click OK on the confirmation window.
        
        Verify 'Page 1' is deleted and you are still in the My Pages folder and it is highlighted.
        """
        portal.delete_page()
        homepage.click_button_on_popup_dialog("OK")
        utils.synchronize_until_element_disappear(".pd-header-buttons-wrapper",homepage.chart_long_timesleep)
        portal.verify_folders_in_left_sidebar(['My Pages'], msg="Step05: 'Page 1' is deleted and you are still in the My Pages folder and it is highlighted")
        
        """
        Step 6:Create 3 pages using any Grid template under 'My Pages'.

        Verify 'Page 1', 'Page 2' & 'Page 3' are listed under 'My Pages'.
        """
        portal.click_on_plus_icon_under_the_folder_in_left_sidebar('My Pages')
        portal.select_new_page_template("Grid 4-2-1")
        utils.synchronize_until_element_is_visible(".pd-header-buttons-wrapper",homepage.chart_long_timesleep)
        portal.click_on_plus_icon_under_the_folder_in_left_sidebar('My Pages')
        portal.select_new_page_template("Grid 4-2-1")
        utils.synchronize_with_number_of_element(".pd-header-buttons-wrapper",2,homepage.chart_long_timesleep)
        portal.click_on_plus_icon_under_the_folder_in_left_sidebar('My Pages')
        portal.select_new_page_template("Grid 2-1")
        
        """
        Step 7:Delete 'Page 2'.
        
        Verify that you are now on 'Page 3'.
        """
        portal.select_page_from_folder_in_left_sidebar("My Pages", 'Page 2')
        portal.delete_page()
        homepage.click_button_on_popup_dialog("OK")
        utils.synchronize_until_element_disappear(".pd-header-buttons-wrapper",homepage.chart_long_timesleep)
        portal.verify_pages_under_the_folder_in_left_sidebar('My Pages',['Page 1', 'Page 3', '+'],msg="Step07: 'Page 2' is deleted and you are still in the My Pages folder and it is highlighted")
        
        """
        step 8:Delete both 'Page 1' & 'Page 3'.
        
        Verify both the pages are deleted and you are still in the My Pages folder and it is highlighted.
        """
        portal.select_page_from_folder_in_left_sidebar("My Pages", 'Page 1')
        portal.delete_page()
        homepage.click_button_on_popup_dialog("OK")
        utils.synchronize_until_element_is_visible(".pd-header-buttons-wrapper",homepage.chart_long_timesleep)
        portal.verify_pages_under_the_folder_in_left_sidebar('My Pages',['Page 3', '+'],msg="Step08: 'Page 1 is deleted and you are still in the Page 3 it is highlighted")
        portal.select_page_from_folder_in_left_sidebar("My Pages", 'Page 3')
        portal.delete_page()
        homepage.click_button_on_popup_dialog("OK")
        utils.synchronize_until_element_disappear(".pd-header-buttons-wrapper",homepage.chart_long_timesleep)
        portal.verify_folders_in_left_sidebar(['My Pages'], msg="Step08: 'Page 1' is deleted")
        portal.verify_pages_under_the_folder_in_left_sidebar('My Pages',['+'],msg="Step08: 'All page folders are deleted")
        
        """
        Step 9:Click (+) below and choose Grid 4-2-1 template
        
        Verify 'Page 1' has been created whereas all panels have the easy selector + sign at the center
        """
        
        portal.click_on_plus_icon_under_the_folder_in_left_sidebar('My Pages')
        portal.select_new_page_template("Grid 4-2-1")
        utils.synchronize_until_element_is_visible(".pd-header-buttons-wrapper",homepage.chart_long_timesleep) 

        """
        Step 10:Double click 'Page1'
        
        Verify page title has been selected to 'Change title' in edit mode
        """
        portal.rename_page_under_the_folder_in_left_sidebar('My Pages','Page 1','')
        time.sleep(2)
        utils.verify_object_visible('[data-ibx-name="titleBox"]', True, "Step 10:Change title")
        
        """
        Step 11:Remove text 'Page 1' and hit enter
        Verify error message appears in dialog as below,
        """
        Error_message = utils.validate_and_get_webdriver_object('[data-ibx-name="contentBox"]',"error_box").text
        utils.asequal(Error_message,expected_error_message,"Step 11")

        """
        step 12:Click OK.
        
        Verify 'Page 1' title is retained.
        """
        homepage.click_button_on_popup_dialog("OK")
        portal.verify_pages_under_the_folder_in_left_sidebar('My Pages', expected_pages_list=['Page 1', '+'], msg='Step 12: Verify Page 1 title is retained..')
        
        
        """
        Step 13:Double Click on Page1 and enter 'Personal page' as the new title and hit enter.
        Verify title has been changed in side bar from 'Page 1' to 'Personal page'.
        """
        portal.rename_page_under_the_folder_in_left_sidebar('My Pages','Page 1','Personal page')
        time.sleep(2)
        portal.verify_pages_under_the_folder_in_left_sidebar('My Pages', expected_pages_list=['Personal page', '+'], msg='Step 12: Verify Page 1 title is retained..')
        
        """
        Step 14:Hover over the (+) sign inside Panel1.
        
        Verify 'Add content' tool tip appears.
        """
        portal_canvas.verify_panel_add_content_tooltip_in_container('Panel 1', "Add", msg="Step 14:Verify 'Add content' tool tip appears.")
        
        """
        Step 15:Click on (+) inside Panel1;
        
        Expand Retail Samples -> Documents;
        Select 'Regional analysis' and click on Add button.
        """
        portal_canvas.click_on_panel_add_content_button_in_container('Panel 1')
        time.sleep(2)
        portal_canvas.select_repository_file_using_add_content_in_panel_container('Retail Samples->Documents->Regional Analysis',select_button='Add')
        
        
        """
        Step 16: click on (+) inside Panel2;
        Select 'Sales by Region Dashboard' and click on Add button.
        """
        portal_canvas.click_on_panel_add_content_button_in_container('Panel 2')
        time.sleep(2)
        portal_canvas.select_repository_file_using_add_content_in_panel_container('Sales by Region Dashboard',select_button='Add')
        

        """

        Step 17:Click on (+) inside Panel3;
        Expand Retail Samples -> Mobile;
        Select 'Show Me Inventory' and click on Add button.
        """
        portal_canvas.click_on_panel_add_content_button_in_container('Panel 3')
        time.sleep(2)
        portal_canvas.select_repository_file_using_add_content_using_crumb_in_panel_container(workspace,'Retail Samples->Mobile->Show Me Inventory',select_button='Add')

 
        """
        Step 18:Click on (+) inside Panel4;
        Expand Retail Samples -> Portal -> Large Widgets;
        Select 'Store Sales by Region' and click on Add button.
        """
        
        portal_canvas.click_on_panel_add_content_button_in_container('Panel 4')
        time.sleep(2)
        portal_canvas.select_repository_file_using_add_content_using_crumb_in_panel_container(workspace,'Retail Samples->Portal->Large Widgets->Store Sales by Region',select_button='Add')
        time.sleep(24)
 
        """
        Step 19:Click on (+) inside Panel5;
        
        Expand Retail Samples -> Portal -> Small Widgets;
        Select 'Category Sales' and click on Add button.
        """
        portal_canvas.click_on_panel_add_content_button_in_container('Panel 5')
        time.sleep(2)
        portal_canvas.select_repository_file_using_add_content_using_crumb_in_panel_container(workspace,'Retail Samples->Portal->Small Widgets->Category Sales',select_button='Add')
        
 
        """
        Step 20:click on (+) inside Panel6;
        Select 'Regional Sales Trend' and click on Add button.
        """
        portal_canvas.click_on_panel_add_content_button_in_container('Panel 6')
        time.sleep(2)
        portal_canvas.select_repository_file_using_add_content_in_panel_container('Regional Sales Trend',select_button='Add')
        

 
        """
        Step 21:Click on (+) inside Panel7;
        Select 'Discount by Region' and click on Add button.
        Verify page appears as below,
        """
        portal_canvas.click_on_panel_add_content_button_in_container('Panel 7')
        time.sleep(2)
        portal_canvas.select_repository_file_using_add_content_in_panel_container('Discount by Region',select_button='Add')
        time.sleep(2)
        portal_canvas.verify_all_containers_title(['Regional Analysis', 'Sales by Region Dashboard', 'Show Me Inventory', 'Store Sales by Region', 'Category Sales', 'Regional Sales Trend', 'Discount by Region'],"Step 18:Verify page appears as below")
    
        """
        Step 22:Close portal.
        """
        
        core_utils.switch_to_previous_window()

 
        """
        Step 23:In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()