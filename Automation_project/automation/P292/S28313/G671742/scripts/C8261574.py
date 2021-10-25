'''
Created on August 9 2019

@author: Vpriya

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261577
TestCase Name = Intent Phrases property should not be exposed in 82xx/8205
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators


class C8261577_TestClass(BaseTestCase):

    def test_C8261577(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Domains->Retail Samples'
        advanced_tab_css = '[data-ibx-type="homePropertyPage"] [role="tab"]:nth-child(2)'
        
        """
        Step 1: Sign in to WebFOCUS as Developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from the side bar
        """  
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on "Retail samples" domain
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Charts', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Right click on Charts folder and Select Properties.
        """
        main_page_obj.right_click_folder_item_and_select_menu("Charts",'Properties')
          
        """
        Step 5: Click Advanced tab.
        Verify the "Intent Phrases" property is not available under Properties section.
        """
        main_page_obj.select_property_tab_value('Advanced')
        util_obj.synchronize_with_visble_text(advanced_tab_css, 'Advanced', main_page_obj.home_page_medium_timesleep)
        try:
            main_page_obj.verify_property_dialog_value("Intent Pharses", 'text_value','', msg="Step:5.1", tab_name='Advanced')
        except: 
            print("Step 5:Verify the 'Intent Phrases' property is not available under Properties section.-passed")
        
        """
        Step 6: Click Cancel to close the property dialog.
        """
        main_page_obj.select_property_dialog_save_cancel_button("Cancel")
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()