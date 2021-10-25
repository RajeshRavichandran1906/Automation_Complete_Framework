'''
Created on October 19, 2018

@author: Varun
Testcase Name : Search Properties sections displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779144
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6779144_TestClass(BaseTestCase):
    
    def test_C6779144(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        tab_css = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Step 2: Expand Domain > Retail Samples > click on Charts
        """
        main_page_obj.select_option_from_crumb_box('Domains')
        main_page_obj.expand_repository_folder('Retail Samples->Charts')
        util_obj.synchronize_with_visble_text("div.files-box", 'Bar - Highest Margin Products', 15)
    
        """
        Step 3: Right click on 'Bar - Highest Margin Products' > Properties > Advanced tab
        """
        main_page_obj.right_click_folder_item_and_select_menu('Bar - Highest Margin Products', 'Properties')
        util_obj.synchronize_with_number_of_element(tab_css, 4, Global_variables.mediumwait)
        main_page_obj.select_property_tab_value('Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Tags', '3')
        
        """
        Step 4: Click Cancel to close the Properties window.
        """
        main_page_obj.close_property_dialog()
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
    