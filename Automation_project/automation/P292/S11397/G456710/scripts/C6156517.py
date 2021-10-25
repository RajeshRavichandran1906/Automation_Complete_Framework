'''
Created on July 02, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6156517
TestCase Name = Target a drill down to a panel
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design,Preview
from common.wftools import chart
from common.wftools import report
from common.pages.ia_run import IA_Run

class C6156517_TestClass(BaseTestCase):

    def test_C6156517(self):
        
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
        report_obj=report.Report(self.driver)
        ia_run_obj=IA_Run(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S11397' domain;
        Click on 'G456710' folder and click on 'page' action tile from under Designer category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """ 
        Step 4: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 5: Drag 'drill_to' onto the page
        """
        page_designer_obj.drag_content_item_to_blank_canvas("drill_to", 1, None)
        
        """ 
        Step 6:Click open properties panel;
        Type "TestDrill" in the classes text box under Content properties
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab_settings_option("Content", "text_box", 'Classes', "TestDrill")
        
        """ 
        Step 7: Drag and drop 'drill_from' fex onto the page canvas
        """
        page_designer_obj.drag_content_item_to_blank_canvas("drill_from", 4)
        
        """ 
        Step 8: Click on Previewbutton
        Drill down on ENGLAND
        """
        page_designer_obj.click_preview()
        page_designer_obj.switch_to_container_frame("drill_from")
        
        """ 
        Step 9: Click on ENGLAND drill down in 'drill_from' panel
        """
        ia_run_obj.select_and_verify_drilldown_report_field("table[summary]", 2, 1)
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 9.01: Verify 'drill_to' fex changes as below
        """
        page_designer_obj.switch_to_container_frame("drill_to")
        chart_obj.verify_x_axis_title_in_run_window(['CAR'],msg="Step 08.01")
        chart_obj.verify_y_axis_title_in_run_window(['DEALER_COST'],msg="Step 08.02")
        chart_obj.verify_x_axis_label_in_run_window(['JAGUAR', 'JENSEN', 'TRIUMPH'],msg="Step 08.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '4K', '8K', '12K', '16K', '20K'],msg="Step 08.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] rect", 1, 3, msg="Step 08.05")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 10: Click on back button to get back to designer page
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """ 
        Step 11: Click on Save button;
        Enter title as 'C6156517' and click save;
        Close designer
        """
        page_designer_obj.save_page_from_toolbar("C6156517")
        core_util_obj.switch_to_previous_window(True)
        
        """ 
        Step 12: Right click on 'C6156517' and select Run
        """
        main_page_obj.right_click_folder_item_and_select_menu("C6156517", "Run")
        core_util_obj.switch_to_frame("iframe.ibx-iframe-frame")
        
        """ 
        Step 13: Click on ENGLAND drill down in 'drill_from' panel
        """
        page_designer_obj.switch_to_container_frame("drill_from")
        ia_run_obj.select_and_verify_drilldown_report_field("table[summary]", 2, 1)
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 13.01: Verify 'drill_to' fex changes as below
        """
        core_util_obj.switch_to_frame("iframe.ibx-iframe-frame")
        page_designer_obj.switch_to_container_frame("drill_to")
        chart_obj.verify_x_axis_title_in_run_window(['CAR'],msg="Step 13.01")
        chart_obj.verify_y_axis_title_in_run_window(['DEALER_COST'],msg="Step 13.02")
        chart_obj.verify_x_axis_label_in_run_window(['JAGUAR', 'JENSEN', 'TRIUMPH'],msg="Step 13.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '4K', '8K', '12K', '16K', '20K'],msg="Step 13.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] rect", 1, 3, msg="Step 13.05")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 14: Close page
        """
        main_page_run.close()
        
        """ 
        Step 15: Signout WF
        """
if __name__ == '__main__':
    unittest.main()
        
        