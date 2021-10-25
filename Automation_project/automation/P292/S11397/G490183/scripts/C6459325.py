"""-------------------------------------------------------------------------------------------
Created on July 01, 2019
@author: vpriya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6459325
Test Case Title =  Upload contents
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
import time


class C6459325_TestClass(BaseTestCase):

    def test_C6459325(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_run = Run(self.driver)
        
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
            TESTCASE CSS
        """
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        explorer_css = "div[class^='file-item file-item-published']"
        
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
        
        """
            STEP 3 : Expand 'P292_S11397' domain -> 'G490183' folder;
            Double click on 'Explorer Widget page'
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        pd_design.run_page_designer_by_double_click("Explorer Widget page")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        
        """
        Step 4:Click on 'Upload File' action tile from under Other category
        """
        main_page.select_action_bar_tab('Other')
        utils.synchronize_with_visble_text(locator_obj.content_area_css, 'Upload File', main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Upload File')
         
        """
        Step 5:Multi select 'babydeer.jpg', 'test_info.txt', 'test upload document-doc.doc', 'Target Accounts - US.xlsx' from the below shared location
        \ibirisc2\bipgqashare\Images_and_Things
        Verify Upload Completed popup displays as below
        Verify 'babydeer.jpg', 'test_info.txt', 'test upload document-doc.doc', 'Target Accounts - US.xlsx' are listed under 'G490183' folder
        """
        main_page.upload_file_using_action_bar(['babydeer.jpg'])
        utils.synchronize_with_visble_text(".dlg-upload .ibx-dialog-main-box","babydeer.jpg", main_page.home_page_medium_timesleep)                                      
        main_page.select_action_bar_tabs_option('Upload File')
        main_page.upload_file_using_action_bar(['test_info.txt'])
        utils.synchronize_with_visble_text(".dlg-upload .ibx-dialog-main-box","test_info.txt", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Upload File')
        main_page.upload_file_using_action_bar(['test upload document - doc.doc'])
        utils.synchronize_with_visble_text(".dlg-upload .ibx-dialog-main-box","test_upload_document_-_doc.doc", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Upload File')
        main_page.upload_file_using_action_bar(['Target Accounts - US.xlsx'])
        utils.synchronize_with_visble_text(".dlg-upload .ibx-dialog-main-box",'Target_Accounts_-_US.xlsx', main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Upload File')
        main_page.verify_items_in_grid_view(['babydeer','Target_Accounts_-_US','test_info','test_upload_document_-_doc'],"asin","Step 5.1 Verify files is available under 'G490183' folder in content area as below")
         
        """
        Step 6:Close upload completed message box
        """
        main_page.click_button_on_popup_dialog('close')
        time.sleep(2)
        
        """
        Step 7:Double click on babydeer.jpg
        Verify image displays as below
        """
        pd_design.run_page_designer_by_double_click("babydeer")
        time.sleep(5)
        utils.verify_picture_using_sikuli("C6459325_step7.PNG","Step:7.1")
        time.sleep(5)

        """
        Step 8:Close image run window
        """
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page_run.close()
         
        """
        Step 9:Close the 'Explorer widget' page run window
        """
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)

        """
        Step 10Refresh the browser.
        Verify Home page is displayed whereas 'babydeer.jpg', 'test_info.txt', 'test upload document-doc.doc', 'Target Accounts - US.xlsx' are listed under 'G490183' folder
        """
        self.driver.refresh()
        utils.synchronize_with_visble_text(explorer_css, "Explorer",main_page.home_page_medium_timesleep)
        main_page.verify_items_in_grid_view(['babydeer','Target_Accounts_-_US','test_info','test_upload_document_-_doc'],"asin","Step 5.1 Verify files is available under 'G490183' folder in content area as below")

        
        """
        Step 11:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
 

 

 
if __name__ == '__main__':
    unittest.main() 