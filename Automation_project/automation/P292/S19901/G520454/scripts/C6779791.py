'''
Created on November 13, 2018

@author: Vpriya
Testcase Name : Verify drop down list options in search box
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779791
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.pages import portal_canvas
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C6779791_TestClass(BaseTestCase):
    
    def test_C6779791(self):
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
        Cancel_css="div[class*='ibx-dialog-cancel-button']"
        user_popup_css = ".Share-with-others-menu"
        menu_item_text_css = "div[data-ibx-type='ibxCheckMenuItem']"
        actual_users_list=['Users','Groups','Users/Groups']
        
        
        def verify_users_dropdown(verify_value=None,dropdownlist=None,msg=None):
            dropdown_elem=util_obj.validate_and_get_webdriver_object(drop_down_css,'dropdowncss')
            core_util_obj.python_left_click(dropdown_elem)
            util_obj.synchronize_with_number_of_element(user_popup_css, '1', Global_variables.longwait)
            verify_checked = util_obj.validate_and_get_webdriver_objects(menu_item_text_css, "menu_item")
            verify_dict = {}
            present_list=[]
            for element in verify_checked:
                present_list.append(element.text.strip())
                verify_dict[element.text.strip()] = element.get_attribute('aria-checked')
            util_obj.asequal(dropdownlist,present_list,msg)
            util_obj.asequal(verify_dict[verify_value],'true',msg)
         
        def Select_users_dropdown(select_value=None):
            share_dialog_elem=util_obj.validate_and_get_webdriver_object(pop_top_css,"Share_dialog_css")
            util_obj.click_on_screen(share_dialog_elem,'middle',click_type=0)
            dropdown_elem=util_obj.validate_and_get_webdriver_object(drop_down_css,'dropdowncss')
            core_util_obj.python_left_click(dropdown_elem)
            verify_checked = util_obj.validate_and_get_webdriver_objects(menu_item_text_css, "menu_item")
            for element in verify_checked:
                if select_value!=None:
                    if element.text.strip()==select_value:
                        core_util_obj.python_left_click(element)
                else:
                    dispaly_msg="The value is not available in the dropdown"
                    raise LookupError(dispaly_msg)
        
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
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        
        """
        Step 3: Right click on 'V5 Portal Share from the content area > Run
        """
        
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share','Run')
        core_util_obj.switch_to_new_window()
        util_obj.validate_and_get_webdriver_object(share_css,'share_button_css')
        
        """
        Step 4:Click on Share button from the personal page toolbar.
        """
        share_button_elem=util_obj.validate_and_get_webdriver_object(share_css,'share_button_css')
        share_button_elem.click()
        
        """
        Step 5: Click on drop-down in the search box.
        Verify Users, Groups and Users/groups (By default checked) are appears
        """
        verify_users_dropdown(verify_value="Users/Groups",dropdownlist=actual_users_list,msg="Step5:verify users dropdown menu")
         
        """
        Step 6: Click on Users in the drop-down list.   
        Verify Users is checked, 'Enter users' appears in the search box and the drop-down lists still appear    
        """
        
        util_obj.synchronize_with_number_of_element(menu_item_text_css, '3', Global_variables.longwait)
        Select_users_dropdown('Users')
        util_obj.synchronize_with_number_of_element(menu_item_text_css, '3', Global_variables.longwait)
        verify_users_dropdown(verify_value="Users",dropdownlist=actual_users_list,msg="Step6:verify users dropdown menu")
        
        
        """
        Step 7: Click on Users in the drop-down list.   
        Verify Groups is checked, 'Enter groups' appears in the search box and the drop-down lists still appear    
        """
        util_obj.synchronize_with_number_of_element(menu_item_text_css, '3', Global_variables.longwait)
        Select_users_dropdown('Groups')
        util_obj.synchronize_with_number_of_element(menu_item_text_css, '3', Global_variables.longwait)
        verify_users_dropdown(verify_value="Groups",dropdownlist=actual_users_list,msg="Step7:verify users dropdown menu")
        
        """
        Step 8: Click on Users/Groups in the drop-down list.
        Verify Users/Groups is checked, 'Enter groups' appears in the search box and the drop-down lists still appear
        """
        util_obj.synchronize_with_number_of_element(menu_item_text_css, '3', Global_variables.longwait)
        Select_users_dropdown('Users/Groups')
        util_obj.synchronize_with_number_of_element(menu_item_text_css, '3', Global_variables.longwait)
        verify_users_dropdown(verify_value="Users/Groups",dropdownlist=actual_users_list,msg="Step8:verify users dropdown menu")
        
        """
        Step 9: Click Cancel button to close the Share with Others window.
        """
        cancel_button_obj = util_obj.validate_and_get_webdriver_object(Cancel_css, 'Cancel_button')
        core_util_obj.left_click(cancel_button_obj)
        
        """
        Step 10: Close the portal run window..
        """
        core_util_obj.switch_to_previous_window()
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        