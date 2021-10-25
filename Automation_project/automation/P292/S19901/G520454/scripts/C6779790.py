'''
Created on November 13, 2018

@author: vpriya
Testcase Name : Verify Share with Others UI opens
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779790
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.pages import portal_canvas
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C6779790_TestClass(BaseTestCase):
    
    def test_C6779790(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_canvas_obj=portal_canvas.Portal_canvas(self.driver)
        content_css='div[class="ibx-label-glyph ibx-label-icon fa fa-bar-chart"]'
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        folder_name_path="Domains->P292_S19901_G520454"
        share_css="div[title*=Share]"
        pop_top_css="div[class*='share-with-others-dialog ibx-widget']"
        drop_down_css = ".Share-with-menu-btn"
        ok_css='div[class*="ibx-dialog-ok-button"]'
        Cancel_css="div[class*='ibx-dialog-cancel-button']"
        Share_checkbox_css="div[class*='share_with_everyone ibx-can-toggle']"
        
        
        """
        Step 1: Sign in to WebFOCUS as Developer user.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(content_css, '1', Global_variables.longwait)
        
        """
        Step 2: Click on Content View from the sidebar and Click on Domain from the resource tree
        """
        
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        
        """
        Step 3: Expand the domain from the tree and click on 'P292_S19901_G520454'
        """
        
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        
        """
        Step 4: Right click on 'V5 Portal Share from the content area > Run
        """
        
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share','Run')
        core_util_obj.switch_to_new_window()
        util_obj.validate_and_get_webdriver_object(share_css,'share_button_css')
        
        """
        Step 5:Click on Share button from the personal page toolbar
        Verify 'Share with Others' window appears with the following options:
        1. 'Enter users and groups' search box is empty with the dropdown control, 
        2. OK button is disabled and Cancel button is enabled by default,
        3. Share with everyone checkbox.
        """
        share_button_elem=util_obj.validate_and_get_webdriver_object(share_css,'share_button_css')
        share_button_elem.click()
        util_obj.synchronize_with_number_of_element(pop_top_css, '1', Global_variables.longwait)
        util_obj.verify_object_visible(pop_top_css,True,"step5.1 Verify Share with Others window appears")
        portal_canvas_obj.search_input_in_share_with_others_dialog(verify_value='',verify_placeholder='Enter users and groups', verify_drop_down_button='display', msg=" Step 5.2:Enter users and groups search box is empty with the dropdown control" )
        ok_elem=util_obj.validate_and_get_webdriver_object(ok_css,"ok_button_css")
        ok_attribute=util_obj.get_element_attribute(ok_elem,"aria-disabled")
        util_obj.asequal(ok_attribute,"true","Step:5.3 Verify ok button is disabled")
        cancel_elem=util_obj.validate_and_get_webdriver_object(Cancel_css,"cancel_button_css")
        cancel_attribute=util_obj.get_element_attribute(cancel_elem,"aria-disabled")
        util_obj.asequal(cancel_attribute,"false","Step:5.3 Verify ok button is disabled")
        util_obj.verify_object_visible(Share_checkbox_css,True,"step5.2 Share with everyone checkbox appear")
        
        """
        Step 6: Click Cancel button to close the Share with Others window.
        """
        
        cancel_button_obj = util_obj.validate_and_get_webdriver_object(Cancel_css, 'Cancel_button')
        core_util_obj.left_click(cancel_button_obj)
        
        """
        Step 7: Close the portal run window.
        """
    
        core_util_obj.switch_to_previous_window()
        
        """
        Step 4: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        