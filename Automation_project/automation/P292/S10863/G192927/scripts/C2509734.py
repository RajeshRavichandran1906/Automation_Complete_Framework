'''
Created on Sep 18, 2019

@author: Aftab
Testcase Name : Verify User Can share with using the new UI
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2509734
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators import wf_mainpage_locators
import time

class C2509734_TestClass(BaseTestCase):
    
    def test_C2509734(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        locatorsobj = wf_mainpage_locators.WfMainPageLocators()
                
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        folder_name_path="Domains->Retail Samples"
        
        
        actual_users_list=['Users','Groups','Users/Groups']
        drop_down_css = ".Share-with-menu-btn"
        user_popup_css = ".Share-with-others-menu"
        menu_item_text_css = ".Share-with-others-menu div[data-ibx-type='ibxCheckMenuItem']"
        
        def verify_users_dropdown(verify_value=None,dropdownlist=None):
            dropdown_elem=util_obj.validate_and_get_webdriver_object(drop_down_css,'dropdowncss')
            core_util_obj.python_left_click(dropdown_elem)
            util_obj.synchronize_with_number_of_element(user_popup_css, 1, Global_variables.longwait)
            verify_checked = util_obj.validate_and_get_webdriver_objects(menu_item_text_css, "menu_item")
            verify_dict = {}
            present_list=[]
            for element in verify_checked:
                present_list.append(element.text.strip())
                verify_dict[element.text.strip()] = element.get_attribute('aria-checked')
            util_obj.asequal(dropdownlist,present_list,"Step 04.00 :Verify User, Groups, Users/Groups")
            util_obj.asequal(verify_dict[verify_value],'true',"Step 04.01 :Verify Users/Groups are selected by default")
        
        
        Step1 = """
        Step 1: Invoke WF_setup as WF_Administrator.
        """
        login_obj.invoke_home_page('mridadm', 'mrpassadm')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.longwait)
        util_obj.capture_screenshot("01.00", Step1)
        
        Step2 = """
        Step 2: Under Domain Tree >> Select 'Retail Samples'/'My Content' folder
        Step 02.00:Verify 'TE_Report' is present under MyContent folder.
        """
        main_page_obj.select_option_from_crumb_box("Domains")
        util_obj.wait_for_page_loads(10)
        main_page_obj.click_repository_folder("Domains->Retail Samples->My Content")
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(locatorsobj.content_area_css, 'TE_Report', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_items_in_grid_view(['TE_Report'], 'asin', msg= 'Step 02.00: Verify TE_Report is present under MyContent folder')
        util_obj.capture_screenshot("02.00", Step2)
        
        Step3 = """
        Step 3: Right-click on TE_Report >> Under Context menu select 'Share with'
        """
        main_page_obj.right_click_folder_item_and_select_menu('TE_Report','Share with...')
        share_with_css = ".Share-with-menu-btn div[class*='caret-down']"
        util_obj.synchronize_with_number_of_element(share_with_css, 1, Global_variables.longwait)
        util_obj.capture_screenshot("03.00", Step3)
        
        Step4 = """
        Step 4: Click on the drop-down arrow in search box.
        Step 04.00: Verify the Users/Groups are selected by default.
        """
        verify_users_dropdown(verify_value="Users/Groups",dropdownlist=actual_users_list)
        util_obj.capture_screenshot("04.00", Step4)
              
        Step5 = """
        Step 5: Type in Retail_Samples under search box;
        From the search list >> Select 'Retail_Samples/AdvancedUsers' group >> Click Ok.
        Report will be shared with retail Sample/Advanced Users
        Step 05.00: UI will be closed and the shared icon will shown on the item to let user know that this item is shared
        """
        search_box_css = "div[class^='share-with-others-dialog'] div[class^='share-with-txt-search'] input"
        search_box_elem=util_obj.validate_and_get_webdriver_object(search_box_css,'search input box')
        util_obj.set_text_to_textbox_using_keybord('Retail', text_box_elem=search_box_elem, type_speed=0)
        #util_obj.set_text_field_using_actionchains(search_box_elem,'Retail')
        time.sleep(Global_variables.longwait)
        user_css = "div[class*='pop-top'] div[title*='Retail Samples Advanced Users']"
        util_obj.synchronize_with_number_of_element(user_css, 2, main_page_obj.home_page_medium_timesleep)
        user_css_elem=util_obj.validate_and_get_webdriver_object(user_css,'user group selection')
        core_util_obj.left_click(user_css_elem)
        ok_elem = util_obj.validate_and_get_webdriver_object('.ibx-dialog-ok-button','ok button')
        core_util_obj.left_click(ok_elem)
        util_obj.synchronize_until_element_disappear('.ibx-dialog-ok-button', Global_variables.longwait)
        main_page_obj.verify_item_icon_in_content_area('TE_Report','share', '05.00')
        util_obj.capture_screenshot("05.00", Step5)
        
        Step6 = """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        util_obj.capture_screenshot("06.00", Step6)
        
        Step7 = """
        Step 7: Login as Retail_Samples Domain Advanced User.
        Step 07.00 : Verify the shared report is visible under Shared Contents of Administrator.
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.longwait)
        folder_name_path = 'Workspaces->Retail Samples->Shared Content->autoadmuser08'
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.wait_for_page_loads(20)
        util_obj.synchronize_with_visble_text(locatorsobj.content_area_css, 'TE_Report', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['TE_Report'], 'asin', msg= 'Step 07.00: Verify TE_Report is present')
        expected_crumb_box_text = 'Workspaces->Retail Samples->Shared Content->autoadmuser08'
        main_page_obj.verify_crumb_box(expected_crumb_box_text, msg='Step 07.02: Verify the crumb box')
        util_obj.capture_screenshot("07.00", Step7)
        
        Step8 = """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        util_obj.capture_screenshot("08.00", Step8)
        
if __name__ == '__main__':
    unittest.main()