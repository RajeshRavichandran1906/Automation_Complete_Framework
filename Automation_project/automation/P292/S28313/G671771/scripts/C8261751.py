'''
Created on October 19, 2018

@author: Varun
Testcase Name : Verify that not a designated product name also capitalized it refers to a special type of value
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261751
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,page_designer
from common.lib import core_utility,utillity
from common.pages import page_designer_miscelaneous
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261751_TestClass(BaseTestCase):
    
    def test_C8261751(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        page_misc_obj = page_designer_miscelaneous.PageDesignerMiscelaneous(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
     
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        util_obj.wait_for_page_loads(40, pause_time=5)
        
        """
        Step 2: Expand Domain > Click 'Retail Samples' domain
        """
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.wait_for_page_loads(40, pause_time=5)
        main_page_obj.expand_repository_folder("Retail Samples")
        
        """
        Step 3: Select Designer category > Create a PGX by clicking Page action bar using blank template
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        core_util_obj.update_current_working_area_browser_specification() # For edge browser, updating wrong browser Y value. So script level updating browser Y value
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.wait_for_page_loads(40, pause_time=5)
        
        """
        Step 4: Click on Portal > Small Widget > drag and drop 'Category Sales' in to the page canvas.
        """
        page_title_css = ".pd-page-title"
        util_obj.synchronize_with_number_of_element(page_title_css, 1, Global_variables.mediumwait)
        page_designer_obj.drag_content_item_to_blank_canvas('Category Sales', 1, 'Portal->Small Widgets')
        
        """
        Step 5: Click on quick filter icon in the designer toolbar.
        """
        page_designer_obj.click_quick_filter()
        
        """
        Step 6: Click on Category control > click on properties panel in the designer toolbar.
        """
        filter_css = "div[title=\"Show filters\"]"
        util_obj.synchronize_with_number_of_element(filter_css, 1, Global_variables.mediumwait)
        page_designer_obj.click_property()
        tab_css = ".pd-right-pane div[data-ibx-type=\"ibxTabPane\"] .ibx-tab-button"
        util_obj.synchronize_with_number_of_element(tab_css, 2, Global_variables.mediumwait)
        page_designer_obj.verify_setting_tab_properties('Data Settings', ['Show All option=on', 'Display text=All', 'Default value=_FOC_NULL'], 'Step 06 : Verify Data Settings properties')

        """
        Step 7: Close the Page Designer from the application menu
        """
        page_designer_obj.close_page_designer_from_application_menu()
        page_misc_obj.dialog_box(button_name_to_click='No') 
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()