'''
Created on 12th April 2018

@author: AA14564
Testcase Name : Create Work Book under portal
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261628
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools.designer_chart import Designer_Chart

class C8261628_TestClass(BaseTestCase):
    
    def test_C8261628(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        designer_chart_obj = Designer_Chart(self.driver)
        
        """
        Test case CSS
        """
        workpage_css = "div[class*='metadata-container'][class*='{0}-tree-box']"
        workpage_bucket_css = ".dm_listener [data-ibx-type='bucketGroup']"
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Workspaces')
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        main_page_obj.select_option_from_crumb_box('Workspaces')
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'v5portal1' under 'V5 Domain Testing' in content tree and choose Workbook tile from action bar
        """
        main_page_obj.expand_repository_folder('V5 Domain Testing->v5portal1')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Workbook',base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Workbook')
        
        """
        Step 4: Double click on application folder (eg: ibisamp) > choose car.mas > click select.
        """
        main_page_obj.select_file_or_folder_from_resource_dialog('ibisamp', selection_type='double')
        main_page_obj.select_file_or_folder_from_resource_dialog('car.mas')
        util_obj.synchronize_with_number_of_element(".pop-top .ibx-dialog-ok-button:not([class*='ibx-widget-disabled'])",1, main_page_obj.home_page_long_timesleep)
        main_page_obj.click_button_on_popup_dialog('Select')
        
        """
        Step 5: Double click on Country under dimension and Sales under Measures.
        """
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(workpage_css.format('dimension'), 'COUNTRY', main_page_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_dimension_field('COUNTRY')
        util_obj.synchronize_with_visble_text(workpage_bucket_css, 'COUNTRY', main_page_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('SALES')
        util_obj.synchronize_with_visble_text(workpage_bucket_css, 'SALES', main_page_obj.home_page_long_timesleep)
        
        
        """
        Step 6: Click save;
                Enter 'Workbook_New' and click save button
        """
        designer_chart_obj.save_designer_chart_from_toolbar('Workbook_New')
        
        """
        Step 7: Close designer
        """
        designer_chart_obj.close_designer_chart_from_application_menu()
        core_utill_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Workbook_New',base_obj.home_page_medium_timesleep)
        
        """
        Step 8: Right click on 'Workbook_New' and click Publish
                Verify 'Workbook_new' has been published
        """
        main_page_obj.right_click_folder_item_and_select_menu('Workbook_New', context_menu_item_path='Publish')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Workbook_New',base_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish('Workbook_New', 'publish', "Step 08.00: Verify 'Workbook_new' has been published")
        
        """
        Step 9: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()