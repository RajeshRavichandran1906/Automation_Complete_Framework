'''
Created on November 13, 2018

@author: Nasir
Testcase Name : Verify selected users/groups are grayed out in new search
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261700
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity,core_utility, javascript
from common.lib.webfocus import poptop_dialog
from common.pages.wf_mainpage import Wf_Mainpage as home_pages
import time

class C8261700_TestClass(BaseTestCase):
    
    def test_C8261700(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj=designer_portal.Canvas(self.driver)
        share_dlg=poptop_dialog.Share_With_Others(self.driver)
        j_script=javascript.JavaScript(self.driver)
        homepage_obj=home_pages(self.driver)
        
        """    1. Sign in to WebFOCUS as Developer user    """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """    2. Expand the domain from the tree and click on 'P292_S19901_G520454'    """
        """    3. Right click on 'V5 Portal Share' from the content area > Run    """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share', context_menu_item_path='Run', folder_path='Domains->P292_S19901_G520454')
        util_obj.wait_for_page_loads(10)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(".pd-container-title", 'Panel 1', main_page_obj.home_page_medium_timesleep)
        
        """    4. Click on Share button from the personal page toolbar    """
        portal_obj.click_on_page_header_button('Stop sharing')
        time.sleep(4)
        """    5. Click on drop-down in the search box > Choose Users in the drop-down list.    """
        search_menu_dropdown_element = share_dlg.get_searchbox_menu_button()
        core_util_obj.left_click(search_menu_dropdown_element)
        homepage_obj.select_context_menu_item('Users')
        
        # to close context menu
        pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']"
        popup_menu_rows=pop_up_css+" div[data-ibx-type*='MenuItem'] div[class='ibx-label-text']"
        popup_items = self.driver.find_elements_by_css_selector(popup_menu_rows)
        return_obj=j_script.find_elements_by_text(popup_items, 'Users')
        core_util_obj.python_left_click(return_obj[0], xoffset=-100)
        
        
        """    6. Enter 'auto' in the 'Enter user' search box
        Verify the list of users containing with a word 'auto' are displayed as follows:
        autoadvuser04
        autobaseuser08 (previously added 'autobaseuser08' user is greyed out) and autodevuser82)    """
        enter_user_in_inputbox=share_dlg.get_searchbox_input_element()
        util_obj.set_text_to_textbox_using_keybord(text_string='auto', text_box_elem=enter_user_in_inputbox, type_speed=2)
        time.sleep(4)
        users_list=[userobj for userobj in share_dlg.get_dropdown_searched_items() if userobj.is_displayed()]
        for item in users_list:
            if 'auto' in item.text:
                token=True
            else:
                token=False
                break    
        util_obj.asequal(token, True, "Step 06.01: Verify the list of users containing with a word 'auto' are displayed")
        token=False
        for item in users_list:
            if 'autobasuser08\nautobasuser08(auto@devmail.com)' in item.text and item.value_of_css_property('opacity')=='0.4':
                token=True
        util_obj.asequal(token, True, "Step 06.02: Verify 'autobaseuser08' user is greyed out")
            
        """    7. Click on 'autobaseuser08' user
        Verify that unable to select 'autobaseuser08' user    """
        item_visibility_status=False
        for item in users_list:
            if item.text=='autobasuser08\nautobasuser08(auto@devmail.com)':
                self.driver.execute_script("arguments[0].scrollIntoView();", item)
                time.sleep(5)
                core_util_obj.python_left_click(item)
                item_visibility_status=item.is_displayed()
        util_obj.asequal(item_visibility_status, True, "Step 07.01: Verify that unable to select 'autobaseuser08' user")        
        
        """    8. Click Cancel to close the Share with dialog box.    """
        cancel_css = ".ibx-dialog-cancel-button .ibx-label-text"
        cancel_button_obj = util_obj.validate_and_get_webdriver_object(cancel_css, 'Cancel_button')
        core_util_obj.left_click(cancel_button_obj)
        util_obj.wait_for_page_loads(10)
        
        """    9. Close the portal run window    """
        core_util_obj.switch_to_previous_window()
        
        """    10. In the banner link, click on the top right username > Click Sign Out.    """
        main_page_obj.signout_from_username_dropdown_menu()
               
if __name__ == '__main__':
    unittest.main()