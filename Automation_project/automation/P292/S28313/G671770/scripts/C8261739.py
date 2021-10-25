'''
Created on May 7, 2019

@author: varun
Testcase Name : Create Workbook
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261739
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility
from common.wftools import designer_chart

class C8261739_TestClass(BaseTestCase):
    
    def test_C8261739(self):
        """
        Test case objects
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        workspace = "Workspaces"
        
        """
        Test case CSS
        """
        domains_css = ".toolbar"
        
        """
        Step 1: Sign into WebFOCUS as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Click on "P292_S28313'domain -> 'G671770' folder > Click on "Workbook" action tile under common category button.
        """
        util_obj.synchronize_with_visble_text(domains_css, workspace, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tab('Common')
        main_page_obj.select_action_bar_tabs_option('Workbook')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'Open', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Double click on ibisamp > Choose car.mas > Click on select button
        """
        main_page_obj.select_file_or_folder_from_resource_dialog('ibisamp', selection_type='double')
        main_page_obj.select_file_or_folder_from_resource_dialog('car.mas', selection_type='double')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("div[id^='chartpreview']", 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Drag and drop "Country" under Dimensions> Origin to vertical field
        """
        designer_chart_obj.drag_dimension_field_to_query_bucket('COUNTRY', 'Vertical')
        
        """
        Step 6: Click on Save button from the toolbar > Enter "Workbook_test" as title > Click Save
        """
        designer_chart_obj.save_designer_chart_from_toolbar('Workbook_test')
        
        """
        Step 7: Click on the application icon > Close
        Verify that the "Workbook_test" displayed in the content area.
        """
        designer_chart_obj.close_designer_chart_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Items \"]", 'Items', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Workbook_test'], 'asin', 'Step 7.1: Verify the item in content area')
        
        """
        Step 8: Right click on "Workbook_test" > Click on Delete > Click on Yes.
        """
        main_page_obj.right_click_folder_item_and_select_menu('Workbook_test', 'Delete')
        main_page_obj.click_button_on_popup_dialog('OK')
        main_page_obj.verify_items_in_grid_view(['Workbook_test'], 'asnotin', 'Step 8.1: Verify the item is not in content area')
        
        """
        Step 9: In the banner link. click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()