'''
Created on May 10 2019

@author: Vpriya

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261581
TestCase Name = Broken MFD links on Home Page canvas
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.pages import wf_mainpage as main_pages
from common.pages import portal_canvas

class C8261581_TestClass(BaseTestCase):

    def test_C8261581(self):
        """
        TESTCASE VARIABLES
        """
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        mainpage_obj = main_pages.Wf_Mainpage(self.driver)
        main_page_obj=wf_mainpage.Wf_Mainpage(self.driver)
        portal_canvas_obj=portal_canvas.Portal_canvas(self.driver)
        
        domain_folder='Domains->Public'
        action_bar = 'Data'
        warning_message="Metadata does not exist: IBFS:/EDA/EDASERVE/ibisamp/uploadtree_xls_uploadtree.mas"
        
        
        excel_css=".wcx-grid-body>div :nth-child(3)"
        Load_css=".wcx-highlighted.wcx-ribbon-vbox div[title='Load and go to the next step to Report']"
        load_options_css=".ibx-popup .wcx-popup-window-container"
        Date_rec_css='div[data-ibx-type="ibxPopup"] [data-ibx-type="ibxSelectItemList"] div[qa="DATREC - fast binary"]'
        ibisamp_css='.wcx-fp-tree div[wcnode="ibisamp"]'
        search_icon_css='#WcMultiframesContentView-2 [title="Find"]'
        search_box_css=".wcx-grid-searchbox"
        
        
        def select_load_options_value(self, select_options, text_string_to_enter=None, change_opt=None):
            grid_elem=self.driver.find_elements_by_css_selector(".pop-top [class*='wcx-form-item']")
            k=[(i,obj_ ) for i,obj_ in enumerate(grid_elem,0) if obj_.is_displayed() and obj_.text!='' and obj_.text.strip() == select_options][0]
            if change_opt != None:
                options_to_click=grid_elem[k[0]+1].find_element_by_css_selector('.fa-ellipsis-h')
                core_util_obj.python_left_click(options_to_click)
            else:
                options_to_click=grid_elem[k[0]+1].find_element_by_css_selector('input')
                core_util_obj.python_left_click(options_to_click)
            if text_string_to_enter != None:
                util_obj.set_text_to_textbox_using_keybord(text_string=text_string_to_enter,text_box_elem=options_to_click)

             
        """ 
        Step 1: Sign in to WebFOCUS as Administrator
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content tree from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Public folder under Domains tree
        Click on Data tag from action bar
        Click on Upload data tile
        """
        main_page_obj.expand_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Data')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Metadata', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Upload Data')
          
        """
        Step 4:Right click on Excel-> Select Upload Data
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(excel_css,'Excel',main_page_obj.home_page_medium_timesleep)
        excel_elem=util_obj.validate_and_get_webdriver_object(excel_css, 'excel_elem')
          
          
        """Step 5:Upload 'UploadTree.xls' attached
        """
        core_util_obj.python_right_click(excel_elem)
        mainpage_obj.select_context_menu_item('Upload Data')
        main_page_obj.upload_file_using_action_bar(['UploadTree'])
          
        """
        Step 6:Click on > button (Load and go to the next step to Report)
        """
        util_obj.synchronize_with_visble_text(Load_css,'goto_next_right',main_page_obj.home_page_long_timesleep)
        Load_button_elem=util_obj.validate_and_get_webdriver_object(Load_css,'Load_button_Css')
        core_util_obj.python_left_click(Load_button_elem)
  
        """
        Step 7:Click on Adapter drop down and select 'DATREC- fast binary';
        Point app folder 'ibisamp';
        Add the suffix in synonym as 'Uploadtree_xls_uploadtree'
        Click 'Proceed to Load'
        """
        util_obj.synchronize_until_element_is_visible(load_options_css,main_page_obj.home_page_long_timesleep)
        select_load_options_value(self,'Adapter')
        util_obj.synchronize_with_visble_text(Date_rec_css,'DATREC - fast binary',main_page_obj.home_page_long_timesleep)
        Date_rec_elem=util_obj.validate_and_get_webdriver_object(Date_rec_css,'apdater_options_pop_up_css')
        core_util_obj.python_left_click(Date_rec_elem)
        time.sleep(9)
        select_load_options_value(self,'Synonym Application',change_opt='True')
        util_obj.synchronize_with_visble_text(ibisamp_css, 'ibisamp', main_page_obj.home_page_long_timesleep)
        ibisamp_elem=util_obj.validate_and_get_webdriver_object(ibisamp_css,'ibisamp_file_css')
        core_util_obj.python_left_click(ibisamp_elem)
        time.sleep(9)
        main_page_obj.click_button_on_popup_dialog("OK")
        time.sleep(9)
        select_load_options_value(self,'Synonym',text_string_to_enter='Uploadtree_xls_uploadtree')
        main_page_obj.click_button_on_popup_dialog("Proceed to Load")
          
        """
        Verify a link to Metadata 'Uploadtree_xls_uploadtree.mas' is created in content area.
        """
        core_util_obj.switch_to_previous_window(window_close=False)
          
          
        """
        Step 8:Click on Public folder;
        Click on Metadata tile from under Data tag in action bar
        """
        main_page_obj.expand_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Data')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Metadata', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Metadata')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible("div[class='wcx-grid-body-row-cell c0']",main_page_obj.home_page_medium_timesleep)
        file_selection_tree_elem=util_obj.validate_and_get_webdriver_objects(".wcx-grid-body div[class='wcx-grid-body-row-cell c0']","file selection_path")
        for x in file_selection_tree_elem:
            if 'ibisamp' in  x.text.strip():
                core_util_obj.python_left_click(x)
        util_obj.synchronize_until_element_is_visible(search_icon_css,main_page_obj.home_page_medium_timesleep)
        search_elem=util_obj.validate_and_get_webdriver_object(search_icon_css,'Search_icon_css')
        core_util_obj.python_left_click(search_elem)
          
          
        """
        Step 9:Click on ibisamp from applications;
        Delete Uploadtree_xls_uploadtree.mas
        """
          
        util_obj.synchronize_until_element_is_visible(search_box_css,main_page_obj.home_page_medium_timesleep)
        search_box_elem=util_obj.validate_and_get_webdriver_object(search_box_css,'Search_box_css')
        core_util_obj.python_left_click(search_box_elem)
        util_obj.set_text_to_textbox_using_keybord(text_string='Uploadtree_xls_uploadtree',text_box_elem=search_box_elem)
        upload_mas_css="#WcGrid-2 .wcx-grid-body-row-cell.c0 [style*='ibi_master']"
        upload_mas_elem=util_obj.validate_and_get_webdriver_object(upload_mas_css,'Uploadtree_xls_uploadtree_mas_elem')
        core_util_obj.python_right_click(upload_mas_elem)
        mainpage_obj.select_context_menu_item('Delete')
        main_page_obj.click_button_on_popup_dialog("OK")
         
        """
        Step 10:Double click on 'Uploadtree_xls_uploadtree.mas' from under Public folder
        Verify warning message appears as below.
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'uploadtree_xls_uploadtree',main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('uploadtree_xls_uploadtree',click_option='double_click')
        portal_canvas_obj.verify_dialog_msg(warning_message,'Step 10:01')
         
         
        """
        Step 11:Click Ok in warning dialog.
        """
         
        main_page_obj.click_button_on_popup_dialog("OK")
         
          
        """
        Step 12:Right click on 'Uploadtree_xls_uploadtree.mas' from under Public folder and choose New-> InfoAssist-> Report
         
        Verify warning message appears as below.
         
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'uploadtree_xls_uploadtree',main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('uploadtree_xls_uploadtree',context_menu_item_path='New->InfoAssist->Report')
        portal_canvas_obj.verify_dialog_msg(warning_message,'Step 10:01')
        
        
        """
        Step 13:Click Ok in warning dialog.
        """
        
        main_page_obj.click_button_on_popup_dialog("OK")
        time.sleep(2)
        
         
        """
        Step 14:In the banner link, click on the top right username > Click Sign Out.
        """       
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()