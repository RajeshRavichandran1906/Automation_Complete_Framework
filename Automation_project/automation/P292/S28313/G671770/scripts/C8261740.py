'''
Created on May 7, 2019

@author: Niranjan

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261739
TestCase Name = Create Insight Chart
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib import core_utility
from common.wftools import wf_mainpage
from common.wftools import login
from common.locators import wf_mainpage_locators
from common.lib import base
from common.wftools.designer_chart import Designer_Chart

class C8261740_TestClass(BaseTestCase):

    def test_C8261740(self):
        
        """
        TESTCASE OBJECTS
        """
        util_obj = utillity.UtillityMethods(self.driver)
        main_page_obj =wf_mainpage.Wf_Mainpage(self.driver)
        login_obj = login.Login(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        designer_chart_obj = Designer_Chart(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        TESTCASE CSS
        """
        
        workpage_css = "div[class*='metadata-container'][class*='{0}-tree-box']"
        
        """
        TESTCASE VARIABLES
        """
        
        """
        Step 1:Sign into WebFOCUS as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
 
        """
        Step 2:Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)

        """
        Step 3:Click on "P292_S28313'domain -> 'G671770' folder >  Click on "Common" category button > Click on "Chart" action tile.
        """
        main_page_obj.expand_repository_folder('P292_S28313->G671770')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Chart',base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Chart')

        """
        Step 4:Double click on ibisamp > Choose car.mas > Click on select button
        """
        util_obj.synchronize_with_visble_text('div .files-box-files-title', 'Name', main_page_obj.home_page_long_timesleep)
        main_page_obj.select_file_or_folder_from_resource_dialog('ibisamp', selection_type='double')
        main_page_obj.select_file_or_folder_from_resource_dialog('car.mas')
        util_obj.synchronize_with_number_of_element(".pop-top .ibx-dialog-ok-button:not([class*='ibx-widget-disabled'])",1, main_page_obj.home_page_long_timesleep)
        main_page_obj.click_button_on_popup_dialog('Select')
 
        """
        Step 5:Drag and drop "Country" under Dimensions> Origin to vertical field
        """
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(workpage_css.format('dimension'), 'COUNTRY', main_page_obj.home_page_long_timesleep)
        designer_chart_obj.drag_dimension_field_to_query_bucket('COUNTRY', 'Vertical')
 
        """
        Step 6:Click on Save button from the toolbar > Enter "designerchart_test" as title > Click Save
        """
        designer_chart_obj.save_designer_chart_from_toolbar('designerchart_test') 
        
 
        """
        Step 7:Click on the application icon > Close

        Verify that the "designerchart_test" displayed in the content area.
        
        """
        designer_chart_obj.close_designer_chart_from_application_menu()
        core_utill_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'designerchart_test',base_obj.home_page_medium_timesleep)
        
        """
        Step 8:Right click on "designerchart_test" > Click on Delete > Click on Yes.

        Verify that "designerchart_test" is deleted from the content area.
        """
        main_page_obj.right_click_folder_item_and_select_menu('designerchart_test', context_menu_item_path='Delete')
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'designerchart_test', base_obj.home_page_medium_timesleep, condition_type='asnotin')
        main_page_obj.verify_items_in_grid_view(['designerchart_test'], 'asnotin','Step 08.00:')
    
        """
        Step 9:In the banner link. click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
 

 
if __name__ == '__main__':
    unittest.main()