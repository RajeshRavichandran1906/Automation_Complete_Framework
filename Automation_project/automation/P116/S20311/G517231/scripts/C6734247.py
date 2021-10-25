'''
Created on Jan 9, 2019

@author: AA14564

Testsuite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/20311&group_by=cases:section_id&group_id=517231&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/6734247
TestCase Name = AHTML:Popup menu not aligned when using Freeze Column (143947)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C6734247_TestClass(BaseTestCase):

    def test_C6734247(self):
        
        """
            TESTCASE VARIABLES
        """
        active_rpt_obj = Active_Report(self.driver)
        core_utilobj = CoreUtillityMethods(self.driver)
        utilobj = UtillityMethods(self.driver)
        project_id = core_utilobj.parseinitfile('project_id')
        suite_id = core_utilobj.parseinitfile('suite_id')
        group_id = core_utilobj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        page_load_css = '#ITableData0 tr:nth-child(2) td:nth-child(1)'
        case_id = 'C6734247'
        column_css = "#MAINTABLE_wbody0 table tbody #TCOL_0_C_{0}"
        freeze_table_css = "[id='IScrollWindowBodyTab0']"
        freeze_table_css_1 = "#IFixWindowBody0"
        
        '''
        local function
        '''
        def verify_window_has_scroll(cell_number, msg):
            '''
            Desc: This will verify window has vertical scroll.
            '''
            before_scroll_cell_object = utilobj.validate_and_get_webdriver_object(column_css.format(str(cell_number)), 'table cell')
            before_scroll_cell_object_middle_left_x = int(core_utilobj.get_web_element_coordinate(before_scroll_cell_object, element_location='middle_left')['x'])
            after_scroll_cell_object_middle_left_x = self.driver.execute_script("return document.body.clientWidth")
            if after_scroll_cell_object_middle_left_x < before_scroll_cell_object_middle_left_x:
                status = True
            else:
                status = False
            utilobj.asequal(True, status, msg)
            
        
        """
        Step 1: Run the attached 143947.fex from Run adhoc page.
                Expect to see the following Active Report.
                Notice the scroll bar, as the report extends off-page to the right.
        """
        active_rpt_obj.run_active_report_using_api('143947.fex', column_css=page_load_css, synchronize_visible_element_text='ENGLAND', repository_path=folder_path)
        active_rpt_obj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1: Verify the Page Summary 18 of 18 records')
        active_rpt_obj.verify_active_report_dataset(case_id+'.xlsx', 'Step 1.2: Verify data set', table_css="#ITableData0")
        verify_window_has_scroll(30, 'Step 1.3: Notice the scroll bar, as the report extends off-page to the right.')
        
        """
        Step 2: Select the column CAR and click on Freeze Column
                Expect to see the darker vertical line between CAR and MODEL, indicating the freeze line.
                Also, notice that the scroll bar begins under the MODEL column, the first column that can be scrolled.
        """
        active_rpt_obj.select_menu_items('ITableData0', 1, 'Freeze Column')
        time.sleep(5)
        active_rpt_obj.verify_freeze_column('Step 2: verify freeze column scroll bar')
        column_list1=['MODEL', 'BODYTYPE', 'SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL']
        active_rpt_obj.verify_column_heading('IScrollWindowBody0 ', column_list1, 'Step 2.1: Notice that the scroll bar begins under the MODEL column')
        first_freeze_table_object = utilobj.validate_and_get_webdriver_object(freeze_table_css_1, "First freeze table")
        actual_border_width = int(utilobj.get_element_css_propery(first_freeze_table_object, 'border-right-width').replace('px',''))
        utilobj.asequal(1, actual_border_width, 'Step 2.2: Indicating the freeze line')
        
        """
        Step 3: Scroll the report all the way to the right.
                Expect to see COUNTRY and CAR not move.
                Expect to see the MODEL field and all others move to the left.
        """
        accel_first_column_css = '[id="I0r0.0C30"]'
        active_rpt_obj.verify_freeze_column('Step 3: Expect to see COUNTRY and CAR not move', scroll_window_id='IFixWindowBody0')
        accel_first_column_obj_location = utilobj.validate_and_get_webdriver_object(accel_first_column_css, 'Accel first column').location['x']
        utilobj.as_not_equal('2195',accel_first_column_obj_location,'Step 3.1: Expect to see the MODEL field and all others move to the left')
        
        """
        Step 4: Click on the 'SEATS' column, the pop up menu is displaying under the seats column
                Expect to see the pop up menu appear below SEATS with its upper left corner directly below the drop down arrow.
        """
        seat_column_drop_down_css = "[id='popid0_4']"
        seat_column_pop_up_menu_css = "[id='dt0_4_0']:not([style*='none'])"
        seat_column_drop_down_object = utilobj.validate_and_get_webdriver_object(seat_column_drop_down_css, "'SEATS' column drop_down")
        core_utilobj.left_click(seat_column_drop_down_object)
        seat_column_pop_up_menu_object = utilobj.validate_and_get_webdriver_object(seat_column_pop_up_menu_css, "'SEATS' column pop_up_menu")
        seat_column_pop_up_menu_object_top_left_x = int(core_utilobj.get_web_element_coordinate(seat_column_pop_up_menu_object, element_location='top_left')['x'])
        seat_column_pop_up_menu_object_top_left_y = int(core_utilobj.get_web_element_coordinate(seat_column_pop_up_menu_object, element_location='top_left')['y'])
        seat_column_pop_up_menu_object_top_right_x = int(core_utilobj.get_web_element_coordinate(seat_column_pop_up_menu_object, element_location='top_right')['x'])
        seat_column_pop_up_menu_object_bottom_middle_y = int(core_utilobj.get_web_element_coordinate(seat_column_pop_up_menu_object, element_location='bottom_middle')['y'])
        seat_column_object = utilobj.validate_and_get_webdriver_object(column_css.format('4'), "'SEATS' column")
        seat_column_object_left_x = int(core_utilobj.get_web_element_coordinate(seat_column_object, element_location='middle_left')['x'])
        retail_cost_column_object = utilobj.validate_and_get_webdriver_object(column_css.format('6'), "'Retail' column")
        retail_cost_column_object_right_x = int(core_utilobj.get_web_element_coordinate(retail_cost_column_object, element_location='middle_right')['x'])
        freeze_table_object = utilobj.validate_and_get_webdriver_object(freeze_table_css, "freeze_table")
        freeze_table_object_top_left_y = int(core_utilobj.get_web_element_coordinate(freeze_table_object, element_location='top_left')['y'])
        freeze_table_object_bottom_left_y = int(core_utilobj.get_web_element_coordinate(freeze_table_object, element_location='bottom_left')['y'])
        if seat_column_object_left_x < seat_column_pop_up_menu_object_top_left_x and seat_column_pop_up_menu_object_top_right_x < retail_cost_column_object_right_x and freeze_table_object_top_left_y < seat_column_pop_up_menu_object_top_left_y and  seat_column_pop_up_menu_object_bottom_middle_y < freeze_table_object_bottom_left_y:
            status = True
        else:
            status = False
        utilobj.asequal(True, status, 'Step 4: Expect to see the pop up menu appear below SEATS with its upper left corner directly below the drop down arrow.')
        

if __name__ == '__main__':
    unittest.main()