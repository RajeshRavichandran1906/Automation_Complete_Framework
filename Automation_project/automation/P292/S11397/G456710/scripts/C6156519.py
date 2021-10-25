'''
Created on July 03, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6156519
TestCase Name = Tabbed container with no Drill Target
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design,Preview
from common.wftools import chart
from common.pages.ia_run import IA_Run

class C6156519_TestClass(BaseTestCase):

    def test_C6156519(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        main_page_run=wf_mainpage.Run(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj=Preview(self.driver)
        chart_obj = chart.Chart(self.driver)
        ia_run_obj=IA_Run(self.driver)
        
        """
        TESTCASE CSS
        """
        
        """
        TESTCASE VARIABLES
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Expand 'P292_S11397' domain -> 'G456710' folder
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_long_timesleep)
        
        """ 
        Step 4: Right click on 'C6156517' and select Edit
        """
        main_page_obj.right_click_folder_item_and_select_menu("C6156517", "Edit")
         
        """ 
        Step 5: Drag and drop 'drill_to' fex over the alraedy available 'drill_to' fex panel;
        Click on 'Add content as new tab' to create a tabbed container.
        """
        core_util_obj.switch_to_new_window()
        page_designer_obj.drag_content_item_to_blank_canvas("drill_to", 1, None)
        util_obj.synchronize_with_visble_text(".pop-top div[data-ibx-type='ibxHSplitMenuButton']", "Add content as new tab", main_page_obj.home_page_long_timesleep)
        button=util_obj.validate_and_get_webdriver_object(".pop-top div[data-ibx-type='ibxHSplitMenuButton']", "Add content as new tab")
        core_util_obj.left_click(button)
        """ 
        Step 6: Click on Preview button
        """
        page_designer_obj.click_preview()
         
        """ 
        Step 7: Click on first tab in 'drill_to' panel
        """
        page_designer_obj.tab_container("drill_to").select_tab("drill_to")
         
        """ 
        Step 8: Click on JAPAN in 'drill_from' panel
        """
        page_designer_obj.switch_to_container_frame("drill_from")
        ia_run_obj.select_and_verify_drilldown_report_field("table[summary]", 5, 1)
        page_designer_obj.switch_to_default_page()
         
        """ 
        Step 8.01: Verify 'drill_to' fex changes as below
        """
        page_designer_obj.switch_to_container_frame("drill_to")
        chart_obj.verify_x_axis_title_in_run_window(['CAR'],msg="Step 08.01")
        chart_obj.verify_y_axis_title_in_run_window(['DEALER_COST'],msg="Step 08.02", x_or_y_axis_title_length=3)
        chart_obj.verify_x_axis_label_in_run_window(['DATSUN', 'TOYOTA'],msg="Step 08.03", xyz_axis_label_length=3)
        chart_obj.verify_y_axis_label_in_run_window(['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500'],msg="Step 08.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] rect", 1, 2, msg="Step 08.05")
        page_designer_obj.switch_to_default_page()
         
        """ 
        Step 9: Click on second tab
        """
        page_designer_obj.tab_container("drill_to").select_tab("drill_to",2)
         
        """ 
        Step 9.01: Verify no changes happens and chart appears as below
        """
        page_designer_obj.switch_to_container_frame("drill_to")
        chart_obj.verify_x_axis_title_in_run_window(['CAR'],msg="Step 09.01")
        chart_obj.verify_y_axis_title_in_run_window(['DEALER_CO...'],msg="Step 09.02", x_or_y_axis_title_length=3)
        chart_obj.verify_x_axis_label_in_run_window(['ALFA...', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASE...', 'PEUG...', 'TOYOTA', 'TRIUM...'] ,msg="Step 09.03", xyz_axis_label_length=3)
        chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K'] ,msg="Step 09.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] rect", 1, 10, msg="Step 09.05")
        page_designer_obj.switch_to_default_page()
        page_preview_obj.go_back_to_design_from_preview()
         
        """ 
        Step 10: Click save and close designer
        """
        page_designer_obj.click_toolbar_save()
        core_util_obj.switch_to_previous_window(True)
        
        """ 
        Step 11: Right click on 'C6156517' and select Run
        """
        main_page_obj.right_click_folder_item_and_select_menu("C6156517", "Run")
        util_obj.synchronize_until_element_is_visible("iframe.ibx-iframe-frame", main_page_obj.home_page_long_timesleep)
        core_util_obj.switch_to_frame("iframe.ibx-iframe-frame")
        
        """ 
        Step 12: Click on first tab in 'drill_to' panel
        """
        page_designer_obj.tab_container("drill_to").select_tab("drill_to")
        
        """ 
        Step 13: Click on ITALY in 'drill_from' panel
        """
        page_designer_obj.switch_to_container_frame("drill_from")
        ia_run_obj.select_and_verify_drilldown_report_field("table[summary]", 4, 1)
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 13.01: Verify 'drill_to' fex changes as below
        """
        core_util_obj.switch_to_frame("iframe.ibx-iframe-frame")
        page_designer_obj.switch_to_container_frame("drill_to")
        chart_obj.verify_x_axis_title_in_run_window(['CAR'],msg="Step 13.01")
        chart_obj.verify_y_axis_title_in_run_window(['DEALER_COST'],msg="Step 13.02", x_or_y_axis_title_length=3)
        chart_obj.verify_x_axis_label_in_run_window(['ALFA ROMEO', 'MASERATI'],msg="Step 13.03", xyz_axis_label_length=3)
        chart_obj.verify_y_axis_label_in_run_window(['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K'], msg="Step 13.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] rect", 1, 2, msg="Step 13.05")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 14: Click on second tab
        """
        core_util_obj.switch_to_frame("iframe.ibx-iframe-frame")
        page_designer_obj.tab_container("drill_to").select_tab("drill_to",2)
        
        """ 
        Step 14.01: Verify no changes happens and chart appears as below
        """
        page_designer_obj.switch_to_container_frame("drill_to")
        chart_obj.verify_x_axis_title_in_run_window(['CAR'],msg="Step 14.01")
        chart_obj.verify_y_axis_title_in_run_window(['DEALER_CO...'],msg="Step 14.02", x_or_y_axis_title_length=3)
        chart_obj.verify_x_axis_label_in_run_window(['ALFA...', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASE...', 'PEUG...', 'TOYOTA', 'TRIUM...'] ,msg="Step 14.03", xyz_axis_label_length=3)
        chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K'] ,msg="Step 14.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] rect", 1, 10, msg="Step 14.05")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 15: Close page
        """
        main_page_run.close()
        
        """ 
        Step 16: Signout WF
        """
if __name__ == '__main__':
    unittest.main()
