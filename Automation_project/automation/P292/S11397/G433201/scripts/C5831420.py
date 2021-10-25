"""-------------------------------------------------------------------------------------------
Created on August 09, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22062565&group_by=cases:section_id&group_order=asc&group_id=433201
Test Case Title =  Search all items in Domains
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C5831420_TestClass(BaseTestCase):

    def test_C5831420(self):
        
        """
            Test case objects    
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
        
        """
            Test case css
        """
        parent_css = ".sd-category-buttons"
        shared_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(1)"
        personel_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(2)"
        home1091_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(3)"
        home1091a_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(4)"
        public_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(5)"
        a_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(7)"
        b_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(8)"
        c_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(9)"
        d_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(10)"
        e_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(11)"
        f_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(12)"
        g_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(13)"
        purple_value = "rgba(147, 112, 219, 0.3)"
        green_value = "rgba(51, 204, 51, 0.3)"
        blue_value = "rgba(35, 183, 229, 0.3)"
        
        """
            STEP 1 : Sign into WebFOCUS Home Page as Developer User.
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 2 : Click Domains in tree.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        main_page.select_option_from_crumb_box("Domains")
        time.sleep(10)
        
        """    
            STEP 3 : Type * in Search box.
        """
        main_page.search_input_box_options(option_type ='write', input_text_msg= "*")
        utils.synchronize_until_element_is_visible(".sd-category-buttons", main_page.home_page_long_timesleep)
        
        """
            STEP 3.1 : Verify Shared and Personal tags appear in 'Purple'.
        """
        shared_obj = utils.validate_and_get_webdriver_object(shared_css, "Shared css")
        actual_result = shared_obj.value_of_css_property('background-color')
        msg = "Step 3.1.1 : Verify Shared and Personal tags appear in 'Purple'"
        utils.asequal(purple_value, actual_result, msg)
        
        personel_obj = utils.validate_and_get_webdriver_object(personel_css, "Personel css")
        actual_result = personel_obj.value_of_css_property('background-color')
        msg = "Step 3.1.2 : Verify Shared and Personal tags appear in 'Purple'"
        utils.asequal(purple_value, actual_result, msg)
        
        """
            STEP 3.2 : Verify Domain tags appear for HOME-1091, HOME-1091A and Public in 'Green'.
        """
        home1091_obj = utils.validate_and_get_webdriver_object(home1091_css, "Home1091 css")
        actual_result = home1091_obj.value_of_css_property('background-color')
        msg = "Step 3.2.1 : Verify Domain tags appear for HOME-1091, HOME-1091A and Public in 'Green'."
        utils.asequal(green_value, actual_result, msg)
        
        home1091a_obj = utils.validate_and_get_webdriver_object(home1091a_css, "Home1091a css")
        actual_result = home1091a_obj.value_of_css_property('background-color')
        msg = "Step 3.2.2 : Verify Domain tags appear for HOME-1091, HOME-1091A and Public in 'Green'."
        utils.asequal(green_value, actual_result, msg)
        
        public_obj = utils.validate_and_get_webdriver_object(public_css, "Public css")
        actual_result = public_obj.value_of_css_property('background-color')
        msg = "Step 3.2.3 : Verify Domain tags appear for HOME-1091, HOME-1091A and Public in 'Green'."
        utils.asequal(green_value, actual_result, msg)
        
        """
            STEP 3.3 : Verify A,B,C,D,E,F and G tags appear in 'Blue'.
        """
        a_obj = utils.validate_and_get_webdriver_object(a_css, "A css")
        actual_result = a_obj.value_of_css_property('background-color')
        msg = "Step 3.3.1 : Verify A,B,C,D,E,F and G tags appear in 'Blue'."
        utils.asequal(blue_value, actual_result, msg)
        
        b_obj = utils.validate_and_get_webdriver_object(b_css, "B css")
        actual_result = b_obj.value_of_css_property('background-color')
        msg = "Step 3.3.2 : Verify A,B,C,D,E,F and G tags appear in 'Blue'."
        utils.asequal(blue_value, actual_result, msg)
        
        c_obj = utils.validate_and_get_webdriver_object(c_css, "C css")
        actual_result = c_obj.value_of_css_property('background-color')
        msg = "Step 3.3.3 : Verify A,B,C,D,E,F and G tags appear in 'Blue'."
        utils.asequal(blue_value, actual_result, msg)
        
        d_obj = utils.validate_and_get_webdriver_object(d_css, "D css")
        actual_result = d_obj.value_of_css_property('background-color')
        msg = "Step 3.3.4 : Verify A,B,C,D,E,F and G tags appear in 'Blue'."
        utils.asequal(blue_value, actual_result, msg)
        
        e_obj = utils.validate_and_get_webdriver_object(e_css, "E css")
        actual_result = e_obj.value_of_css_property('background-color')
        msg = "Step 3.3.5 : Verify A,B,C,D,E,F and G tags appear in 'Blue'."
        utils.asequal(blue_value, actual_result, msg)
        
        f_obj = utils.validate_and_get_webdriver_object(f_css, "F css")
        actual_result = f_obj.value_of_css_property('background-color')
        msg = "Step 3.3.6 : Verify A,B,C,D,E,F and G tags appear in 'Blue'."
        utils.asequal(blue_value, actual_result, msg)
        
        g_obj = utils.validate_and_get_webdriver_object(g_css, "G css")
        actual_result = g_obj.value_of_css_property('background-color')
        msg = "Step 3.3.7 : Verify A,B,C,D,E,F and G tags appear in 'Blue'."
        utils.asequal(blue_value, actual_result, msg)
        
        """
            STEP 4 : Remove search string by clicking on (X) button.
        """
        main_page.search_input_box_options(option_type ='clear')
        utils.synchronize_until_element_disappear(parent_css, main_page.home_page_long_timesleep)
        
        """
            STEP 4.1 : Verify the page reloads & displays default home page view.
        """
        main_page.verify_folders_in_grid_view(['HOME-1091', 'HOME-1091A', 'Public'], 'asin', "Step 4.1 : Verify the page reloads & displays default home page view.")
        
        """
            STEP 5 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
         
if __name__ == '__main__':
    unittest.main()