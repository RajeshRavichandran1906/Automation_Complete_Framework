'''
Created on Jun 26, 2019

Testcase Name : Create,Edit and View URL
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6459323
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import page_designer
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6459323_TestClass(BaseTestCase):
    
    def test_C6459323(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        page_designer_obj=page_designer.Design(self.driver)
        wfmain_obj_run=wf_mainpage.Run(self.driver)
        
        """
        Test case CSS
        """
        url_popup_css = ".ibx-root .create-new-url"
        action_bar_tab_options_css = "div:not([class*='tpg-hidden'])>div>div.create-new-item[role='button']"
        
        """
        Test case variables
        """
        test_case_id = 'C6459323'
        title_name = 'Google'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on the Content Sidebar.
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S11397' domain -> 'G490183' folder;
        Double click on 'Explorer Widget page'
        """
        main_page_obj.expand_repository_folder("P292_S11397->G490183")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        
        """
        Step 4: Click on 'URL' action tile from under other 
        """
        main_page_obj.select_action_bar_tab('Other')
        util_obj.synchronize_with_number_of_element(action_bar_tab_options_css, 8, base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('URL')
        util_obj.synchronize_with_number_of_element(url_popup_css , 1 , base_obj.home_page_medium_timesleep)
        
        """
        Step 4.1: Verify New URL dialog opens as below
        """
        main_page_obj.verify_popup_dialog_caption('New URL', "Step 4.1: Verify New URL dialog opens as below")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog('OK', 'Step 4.2: Verify New URL dialog opens as below', enable=False)
    
        """
        Step 5: Enter Title as 'Google' and URL as 'http://www.google.com' > Click OK. 
        """
        main_page_obj.enter_url_title_in_popup_dialog(title_name)
        main_page_obj.enter_url_in_popup_dialog('http://www.google.com')
        main_page_obj.click_button_on_popup_dialog('OK')
        
        """
        Step 5.1: Verify 'Google' is created and listed under G490183 folder
        """
        main_page_obj.verify_items_in_grid_view(['Google'],'asin', "Step 5.1: Verify 'Google' is created and listed under G490183 folder")
        
        """
        Step 6: Double click on 'Google' URL and click open in new window icon. 
        """
        page_designer_obj.run_page_designer_by_double_click(title_name)
        time.sleep(8)
        wfmain_obj_run.switch_to_frame()
        
        """
        Step 7: Close Google page
        """
        wfmain_obj_run.switch_to_default_content()
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        wfmain_obj_run.close()
        
        """
        Step 8: Right Click on 'Google' > Edit       
        """
        main_page_obj.right_click_folder_item_and_select_menu(title_name, 'Edit')
        util_obj.synchronize_with_number_of_element(url_popup_css , 1 , base_obj.home_page_medium_timesleep)
        
        """
        Step 8.1: Verify that Edit URL dialog opens as below
        """
        main_page_obj.verify_popup_dialog_caption('Edit URL', "Step 8.1: Verify that Edit URL dialog opens as below")
        
        """
        Step 9: Click Cancel to close the 'Edit URL' dialog.
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, title_name, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.switch_to_default_page()
        
        """
        Step 10: Close the 'Explorer widget' page run window.
        """
        wfmain_obj_run.close()
        self.driver.refresh()
        
        """
        Step 10.1: Verify Home page is displayed and URL 'Google' is listed under G490183 folder
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Other', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([title_name],'asin', "Step 10.1: Verify Home page is displayed and URL 'Google' is listed under G490183 folder")
        
        """
        Step 11: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()