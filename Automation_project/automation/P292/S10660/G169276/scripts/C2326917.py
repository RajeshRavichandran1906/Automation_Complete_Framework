'''
Created on Sep 5, 2019

@author: Niranjan
Test rail link : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2326917
Testcase title : CCW:Content Interaction:Adding a PGX to a Collaborative Portal
'''
import unittest
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login
from common.pages.vfour_portal_ribbon import Vfour_Portal_Ribbon
from common.pages.vfour_miscelaneous import Vfour_Miscelaneous
from common.lib.javascript import JavaScript
from common.pages.page_designer_design import PageDesignerDesign
import pyautogui
import time

class C2326917_TestClass(BaseTestCase):
   
    def test_C2326917(self):
       
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        portal = Vfour_Portal_Ribbon(self.driver)
        portal_misc = Vfour_Miscelaneous(self.driver)
        page = PageDesignerDesign(self.driver)
        js = JavaScript(self.driver)
        
        def verify_alert_message(expected_text):
            time.sleep(2)
            als = self.driver.switch_to.alert
            actual_alert_msg=als.text
            if actual_alert_msg == expected_text:
                status = True
            else:
                status = False
            als.accept()    
            utils.asequal(True, status, 'Step 12.00: Verify alert message')
            
        '''
        Step 1 : Invoke WF Home Page as Developer user.
        '''
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.main-panel .toolbar', 'Workspaces', homepage.home_page_long_timesleep)
         
        '''
        Step 2 : Under Domain tree >> Navigate to "P292_S10660" domain >> Select folder G169276.
        '''
        homepage.expand_repository_folder('Domains->P292_S10660->G169276')
        utils.synchronize_with_visble_text('.sd-content-title-label-files', 'Items', homepage.home_page_long_timesleep)       
         
        '''
        Step 3 : Create a new Collaborative Portal with Title/Name as Test_V4.
        
        Verify Page template dialog is displayed.
        '''
        homepage.select_action_bar_tab('Other')
        utils.synchronize_with_visble_text('div[class*="action-bar-tab other-group-tab"]', 'Collaborative Portal', homepage.home_page_long_timesleep)
        homepage.select_action_bar_tabs_option('Collaborative Portal')
        utils.synchronize_with_visble_text('.ibx-dialog-button-box', 'Cancel', homepage.home_page_long_timesleep)
        homepage.enter_new_folder_title_in_popup_dialog('Test_V4')
        homepage.click_button_on_popup_dialog('Create')
        
        coreutils.switch_to_new_window()
        utils.synchronize_with_number_of_element('#dlgTitleExplorer', 1, homepage.home_page_long_timesleep)
        page_template = utils.validate_and_get_webdriver_object('#dlgTitleExplorer', 'page template')
        if page_template.is_displayed() == True:
            status = True
        else:
            status = False
        utils.asequal(status, True, 'Step 03.00 : Verify Page template dialog is displayed')
         
        '''
        Step 4 : Cancel the page template dialog.
        '''
        portal_misc.select_page_template(btn_name="Cancel")
        
        '''
        Step 5 : Navigate to Insert Tab >> Click on WebFOCUS Resources.
        
        Verify a new banner is opened in the right with resource tree contents.
        '''
        portal.invoke_and_verify_wf_resource_tree()
        
        '''
        Step 6 : From the WebFOCUS Resources panel on the right >> Navigate to "P292_S10660/G169276" >> Drag the "PGX_portal_page" onto the page tab area.
        
        Verify the "PGX_portal_page" is inserted onto the canvas.
        '''
        portal_misc.expand_resource_tree('P292_S10660->G169276->PGX_portal_page')
        
        source_obj = utils.validate_and_get_webdriver_object('#treeView tr[class="selected lead"] img[src*="pagev4"]', 'drag')
        target_obj = utils.validate_and_get_webdriver_object("div[id*='BiVBox']>div[id*='BipNavigatorTop']", "drop")

        source_elem = coreutils.get_web_element_coordinate(source_obj)
        target_elem = coreutils.get_web_element_coordinate(target_obj)
        pyautogui.mouseDown(source_elem['x'], source_elem['y'], duration=2)
        pyautogui.moveTo(target_elem['x'], target_elem['y'],duration=2)
        pyautogui.mouseUp(target_elem['x'], target_elem['y'])
        time.sleep(10)
        coreutils.switch_to_frame(frame_css = 'iframe[class="bi-iframe iframe "]')
        js.wait_for_page_loads(10)
        page.verify_page_heading_title(['Page Heading'], 'Step 06.00 : Verify the "PGX_portal_page" is inserted onto the canvas')
        coreutils.switch_to_default_content()
    
        '''
        Step 7 : Save the portal & Close portal window.
        '''
        portal.select_tool_menu_item('menu_Save')
        coreutils.switch_to_previous_window()
         
        '''
        Step 8 : Run Test_V4 portal.
        
        Verify output,
        '''
        homepage.right_click_folder_item_and_select_menu('Test_V4', 'Run')
        coreutils.switch_to_new_window()
        utils.synchronize_with_number_of_element('iframe[class="bi-iframe iframe "]', 1, homepage.home_page_long_timesleep)
        coreutils.switch_to_frame(frame_css = 'iframe[class="bi-iframe iframe "]')
        js.wait_for_page_loads(10)
        page.verify_number_of_panels(4, 'Step 08.00 : Verify 4 panels are displaying in page canvas')
        page.verify_containers_title(["Blue", "Gray", "Green", "Red"], 'Step 08.01 : Verify container titles') 
        coreutils.switch_to_default_content()
        
        '''
        Step 9 : Close portal run time window.
        '''
        coreutils.switch_to_previous_window()
        
        '''
        Step 10 : Edit Test_V4 portal.
        
        Verify designer window,
        '''
        homepage.right_click_folder_item_and_select_menu('Test_V4', 'Edit')
        coreutils.switch_to_new_window()
        utils.synchronize_with_number_of_element('iframe[class="bi-iframe iframe "]', 1, homepage.home_page_long_timesleep)
        coreutils.switch_to_frame(frame_css = 'iframe[class="bi-iframe iframe "]')
        js.wait_for_page_loads(10)
        page.verify_number_of_panels(4, 'Step 10.00 : Verify 4 panels are displaying in page canvas')
        page.verify_containers_title(["Blue", "Gray", "Green", "Red"], 'Step 10.01 : Verify container titles') 
        coreutils.switch_to_default_content()
        
        '''
        Step 11 : Navigate to Insert Tab >> Click on WebFOCUS Resources.
        '''
        portal.invoke_and_verify_wf_resource_tree()
         
        '''
        Step 12 : From the WebFOCUS Resources panel on the right >> Navigate to "P292_S10660/G169276" >> Drag the "PGX_portal_page" onto the page tab area.
        
        Verify it displays error message "Page already in portal".
        Step 13 : Click Ok in the dialog box.
        '''
        portal_misc.expand_resource_tree('P292_S10660->G169276->PGX_portal_page')
        
        source_obj = utils.validate_and_get_webdriver_object('#treeView tr[class="selected lead"] img[src*="pagev4"]', 'drag')
        target_obj = utils.validate_and_get_webdriver_object("div[id*='BiVBox']>div[id*='BipNavigatorTop']", "drop")

        source_elem = coreutils.get_web_element_coordinate(source_obj)
        target_elem = coreutils.get_web_element_coordinate(target_obj)
        pyautogui.mouseDown(source_elem['x'], source_elem['y'], duration=2)
        pyautogui.moveTo(target_elem['x'], target_elem['y'],duration=2)
        pyautogui.mouseUp(target_elem['x'], target_elem['y'])  
        time.sleep(5)
        verify_alert_message("Page already in portal.")  
        
        '''
        Step 14 : Close portal designer window.
        '''
        coreutils.switch_to_previous_window()
        
        '''
        Step 15 : Run Test_V4 portal.
        
        Verify output is unchanged,
        '''
        homepage.right_click_folder_item_and_select_menu('Test_V4', 'Run')
        coreutils.switch_to_new_window()
        utils.synchronize_with_number_of_element('iframe[class="bi-iframe iframe "]', 1, homepage.home_page_long_timesleep)
        coreutils.switch_to_frame(frame_css = 'iframe[class="bi-iframe iframe "]')
        js.wait_for_page_loads(10)
        page.verify_number_of_panels(4, 'Step 15.00 : Verify 4 panels are displaying in page canvas')
        page.verify_containers_title(["Blue", "Gray", "Green", "Red"], 'Step 15.01 : Verify container titles') 
        coreutils.switch_to_default_content()
        
        '''
        Step 16 : Close portal run time window.
        '''
        coreutils.switch_to_previous_window()
         
        '''
        Step 17 : In the banner link, click on the top right username > Sign Out.
        '''
        homepage.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 