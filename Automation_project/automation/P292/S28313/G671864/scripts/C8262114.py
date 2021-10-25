'''
Created on November 26, 2018

@author: varun
Testcase Name : Add My pages folder with set property under main portal
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262114
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity

class C8262114_TestClass(BaseTestCase):
    
    def test_C8262114(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        folder_css = ".folder-item"
        portal_wait_css = ".folder-item-published .image-text .ibx-label-text"
        properties_css = ".properties-page-label .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        util_obj.wait_for_page_loads(20, pause_time=3)
        
        """
        Step 3: Double click on 'V5 Personal Portal' > Click on folder action bar.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal', click_option='double_click')
        main_page_obj.select_action_bar_tabs_option('Folder')
        
        """
        Step 4: Enter Title as 'My Pages' and click OK.
        Verify My Pages folder is created.
        """
        main_page_obj.create_new_folder('My Pages')
        util_obj.synchronize_with_number_of_element(folder_css,1,45)
        main_page_obj.verify_folders_in_grid_view(['My Pages'], comparision_type='asin', msg="Step 4.1: My pages is available in the grid")
        
        """
        Step 5: Right click on 'My Pages' folder > Properties > Advanced tab.
        Verify that you see Allow personal pages checkbox
        """
        main_page_obj.right_click_folder_item_and_select_menu('My Pages', 'Properties')
        util_obj.synchronize_with_visble_text(properties_css,'My Pages', 45)
        main_page_obj.select_property_tab_value('Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Automatically open', '5.1',checkbox='enable')
        
        """
        Step 6: Check personal pages box and click save.
        """
        main_page_obj.edit_property_dialog_value('Allow personal pages', 'checkbox', 'check', tab_name='Advanced')
        main_page_obj.select_property_dialog_save_cancel_button('Save')
        main_page_obj.close_property_dialog()
        
        """
        Step 7: Click on G513510 folder in the tree and right click on 'V5 Personal Portal' > Publish.
        Verify 'V5 Personal Portal' is published.
        """
        main_page_obj.expand_repository_folder('G513510')
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal','Publish')
        util_obj.synchronize_with_visble_text(portal_wait_css, 'V5 Personal Portal',45)
        main_page_obj.verify_content_area_folder_publish_or_unpublish('V5 Personal Portal','publish',msg='Step 7.1: Verify V5 portal is published')
        util_obj.wait_for_page_loads(15, pause_time=3)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()