'''
Created on December 18, 2018

@author: varun
Testcase Name : Add My pages folder with set property under main portal
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262156
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8262156_TestClass(BaseTestCase):
    
    def test_C8262156(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        properties_css = ".properties-page-label .ibx-label-text"
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"] .ibx-label-text"
        folder_item_css = ".folder-item"
        
        """
        Test case variables
        """
        action_bar_text = 'Action Bar'
        folders_text = 'Folders'
        portal_name = 'V5 Personal Portal_Nav-3'
        pages_label = 'My Pages'
        pages_to_check = 'Allow personal pages'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G517783 folder. 
        """
        main_page_obj.expand_repository_folder('P292_S19901->G517783')
        
        """
        Step 3: Double click on 'V5 Personal Portal_Nav-3' > Click on folder action bar.
        """
        util_obj.synchronize_with_visble_text(locator_obj.folders_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.double_click_folder_item_and_select_menu(portal_name)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tabs_option('Folder')
        
        """
        Step 4: Enter Title as 'My Pages' and click OK. 
        Verify My Pages folder is created.
        """
        main_page_obj.create_new_folder(pages_label)
        util_obj.synchronize_with_number_of_element(folder_item_css, 1, base_obj.home_page_medium_timesleep )
        main_page_obj.verify_folders_in_grid_view([pages_label], 'asin', 'Step 4.1: Verify pages folder in the content area')
        
        """
        Step 5: Right click on 'My Pages' folder > Properties > Advanced tab.
        Verify that you see Allow personal pages checkbox
        """
        main_page_obj.right_click_folder_item_and_select_menu(pages_label, 'Properties')
        util_obj.synchronize_with_visble_text(properties_css, pages_label, base_obj.home_page_medium_timesleep)
        main_page_obj.select_property_tab_value('Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', pages_to_check, 'Step 5.1',checkbox='enable')
        
        """
        Step 6: Check personal pages box and click save.
        """
        main_page_obj.edit_property_dialog_value(pages_to_check, 'checkbox', 'check', tab_name='Advanced')
        main_page_obj.select_property_dialog_save_cancel_button('Save')
        
        """
        Step 7: Click on G517783 folder in the tree and right click on 'V5 Personal Portal_Nav-3' > Publish
        """
        main_page_obj.expand_repository_folder('G517783')
        util_obj.synchronize_with_visble_text(locator_obj.folders_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Publish')
        util_obj.synchronize_with_visble_text(locator_obj.folders_css, folders_text, base_obj.home_page_short_timesleep)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(portal_name, 'publish','Step 7.1: Verify folder is published')
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
    
if __name__ == '__main__':
    unittest.main()