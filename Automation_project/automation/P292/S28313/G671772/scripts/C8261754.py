'''
Created on April 13, 2019

@author: Varun
Testcase Name : Properties: Remove Intent phrases from Folders
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261754
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261754_TestClass(BaseTestCase):
    
    def test_C8261754(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
     
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Step 3: Right click on 'P292_S28313' domain and select Properties
        """
        main_page_obj.select_repository_folder_context_menu('P292_S28313', 'Properties')
        util_obj.synchronize_with_visble_text(".properties-page-label", 'P292_S28313', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on advanced tab
        Verify Intent phrases property doesn't appear
        """
        main_page_obj.select_property_tab_value('Advanced')
        advanced_tab_properties = util_obj.validate_and_get_webdriver_object(".properties-advanced-pane-tab ", 'advanced-tab').text.strip()
        util_obj.as_notin('Intent phrases', advanced_tab_properties, "Step 4.1: Verify Intent phrases not in the advanced tab")
        
        """
        Step 5: Click cancel
        """
        main_page_obj.select_property_dialog_save_cancel_button('Cancel')
        
        """
        Step 6: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()