'''
Created on October 19, 2018

@author: Varun
Testcase Name : Verify Interactive Reporting Properties sections displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779145
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.pages import wf_mainpage as mainpage
from common.lib import utillity, core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6779145_TestClass(BaseTestCase):
    
    def test_C6779145(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        wfmainpageobj = mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        coreutil_obj = core_utility.CoreUtillityMethods(self.driver)
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
        scroll_elem=wfmainpageobj.get_property_dialog_rows_object('Advanced', 'Tags', step_number='Step 3:')
        coreutil_obj.move_to_element(scroll_elem)
        util_obj.mouse_scroll(scroll_type='down', number_of_times=5)
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Prompt for parameters', '3.i)',checkbox='enable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Enable AutoLinking', '3.ii)',checkbox='enable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'AutoLink target', '3.iii)',checkbox='enable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Enable AutoDrill', '3.iv)',checkbox='enable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Run with OLAP', '3.v)',checkbox='disable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Use title for deferred report description', '3.vi)',checkbox='enable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Schedule only', '3.vii)',checkbox='enable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Only run as deferred report', '3.viii)',checkbox='enable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Only allow user to run', '3.ix)',checkbox='disable')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Allow user to run', '3.x)',checkbox='disable')
        
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