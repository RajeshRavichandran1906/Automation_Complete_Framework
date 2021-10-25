'''
Created on October 19, 2018

@author: Varun
Testcase Name : Verify Scheduling and Library Content Properties sections displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261750
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.pages import wf_mainpage as mainpage
from common.lib import utillity, core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools.paris_home_page import ParisHomePage

class C8261750_TestClass(BaseTestCase):
    
    def test_C8261750(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        wfmainpageobj = mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        coreutil_obj = core_utility.CoreUtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        tab_css = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        util_obj.wait_for_page_loads(time_out=20, pause_time=2)
        
        """
        Step 2: Expand Domain > Retail Samples > click on Charts
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples->Charts')
        util_obj.wait_for_page_loads(10, pause_time=2)
        util_obj.synchronize_with_visble_text("div.files-box", 'Bar - Highest Margin Products', 150)
    
        """
        Step 3: Right click on 'Bar - Highest Margin Products' > Properties > Advanced tab
        """
        main_page_obj.right_click_folder_item_and_select_menu('Bar - Highest Margin Products', 'Properties')
        util_obj.synchronize_with_number_of_element(tab_css, 4, Global_variables.mediumwait)
        main_page_obj.select_property_tab_value('Advanced')
        scroll_elem=wfmainpageobj.get_property_dialog_rows_object('Advanced', 'Tags', step_number='Step 3:')
        coreutil_obj.move_to_element(scroll_elem)
#         util_obj.mouse_scroll(scroll_type='down', number_of_times=5, pause=3)
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Restrict schedule to Library only', '03.01',checkbox='enable')
        
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