'''
Created on December 17, 2018

@author: varun
Testcase Name : Choose other filters using the icon
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6694045
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.wftools import page_designer
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods

class C6694045_TestClass(BaseTestCase):
    
    def test_C6694045(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        page_preview_obj = page_designer.Preview(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        pd_filter_window = ".pd-filter-window .ibx-dialog-main-box"
        legend_label = "text[class*='legend-labels']"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        
        """
        Test case variables
        """
        portal_name = 'V5 Personal Portal_Nav-2'
        frame_name = 'Category Sales'
        frame_legend = 'Camcorder'
        folders_text = 'Folders'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        main_page_obj.expand_repository_folder('P292_S19901->G514402')
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_filter_window, 1, base_obj.home_page_long_timesleep)
        
        """
        Step 4: Click on filter icon > Click on Select North America > Choose North America
        """
        page_preview_obj.select_filter_dropdown_option('Select North America', 'North America')
        
        """
        Step 5: Click Category > dropdown > choose Camcorder.
        """
        page_preview_obj.select_filter_dropdown_option('Category:', 'Camcorder')
        
        """
        Step 6: Click the Submit button.
        Verify the reports change accordingly. Only the controls which relate to a particular report should take affect.
        """
        main_page_obj.click_button_on_popup_dialog('Submit')
        page_preview_obj.switch_to_container_frame(frame_name)
        util_obj.synchronize_with_number_of_element(legend_label, 1, base_obj.home_page_long_timesleep)
        observed_legend_text = util_obj.validate_and_get_webdriver_object(legend_label,"label-name").text
        util_obj.asequal(frame_legend, observed_legend_text, 'Step 6.1: Verify only one legend is present in the frame Category Sales')
        
        """
        Step 7: Close the 'V5 Personal Portal_Nav-2' run window.
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()