'''
Created on Jan 9, 2019

@author: AA14564

Testsuite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/20311&group_by=cases:section_id&group_id=517231&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/8149222
TestCase Name = AHTML:HFREEZE plus Column Freeze: Bad report output (ACT-1652)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.global_variables import Global_variables
import pyautogui

class C8149222_TestClass(BaseTestCase):

    def test_C8149222(self):
        
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
        page_load_css = '#IWindowBodyFTB_0_0 tr:nth-child(1) td:nth-child(1)'
        case_id = 'C8149222'
        freeze_table_css = "IWindowBodyFTS_0_0"
        freeze_table_css_1 = "IWindowBodyFTS_0_0_r"
        
        '''
        local function
        '''
        def re_size_window():
            '''
            Desc: This will resize the window and update the x and y coordinates
            '''
            self.driver.set_window_size(1450, 990)
            time.sleep(2)
            update_coordinates()
        
        def update_coordinates():
            '''
            Desc: This will  get window current location on screen after resized the window and update the x and y coordinates
            '''
            x=self.driver.execute_script("return window.screenX;")
            y=self.driver.execute_script("return window.screenY;")
            Global_variables.current_working_area_browser_x = int(x) + 7 + Global_variables.current_working_area_browser_x 
            Global_variables.current_working_area_browser_y = int(y) + 7 + Global_variables.current_working_area_browser_y
        
        def select_menu_items(table_id, column_no, column_name):
            '''
            Desc:- This will select menu items.
            '''
            index=list(table_id)[-1]
            main_menu_id=""+str(index)+"_" + str(column_no) + "_0"
            menu_btn_css="#" + table_id + " #popid" + str(index) + "_" + str(column_no) + " img"
            parent="#dt" + main_menu_id
            menu_btn_click=utilobj.validate_and_get_webdriver_object("#" + table_id + " #TCOL_" + str(index) + "_C_" + str(column_no)+'_f', 'Column')
            core_utilobj.left_click(menu_btn_click)
            menu_btn=utilobj.validate_and_get_webdriver_object(menu_btn_css, 'cell drop down image')
            core_utilobj.left_click(menu_btn)
            time.sleep(3)
            menu_hov = utilobj.validate_and_get_webdriver_object(parent + " table tr", 'Popup table first row')
            core_utilobj.move_to_element(menu_hov)
            time.sleep(1)
            x = utilobj.validate_and_get_webdriver_objects("#dt"+ main_menu_id + ">table>tbody>tr", 'Popup table')
            for i in range(len(x)):
                item_css="set" + main_menu_id + "_" + str(i)
                lineObjbj = utilobj.validate_and_get_webdriver_object("#"+ item_css + "i_t", 'popup table row').text
                if lineObjbj == column_name:
                    item=utilobj.validate_and_get_webdriver_object("#"+ item_css + "i_t", 'popup table actual row')
                    core_utilobj.left_click(item)
                    break
        
        def verify_page_summary(expected_title, msg):
            page_summary_css=".statusBarPagingTemplate"
            summary_object = utilobj.validate_and_get_webdriver_object(page_summary_css, 'Page summary text')
            actual_title = utilobj.get_element_attribute(summary_object, 'title').strip().replace(' ','')
            utilobj.asequal(expected_title, actual_title, msg)
        
        def move(x):
            core_utilobj.python_move_to_element(veritical_scroll_bar, yoffset=-10)
            time.sleep(2)
            pyautogui.mouseDown()
            pyautogui.moveTo(x, duration= 2)
            pyautogui.mouseUp()
        
        """
        Step 1: Log in to WebFOCUS
                http://machine:port/{alias}
        """
        """
        Step 2: Execute ACT-1652.fex from below API
                http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S20311/G517177&BIP_item=ACT-1652.fex
        """
        active_rpt_obj.run_active_report_using_api('ACT-1652.fex', column_css=page_load_css, synchronize_visible_element_text='Midwest', repository_path=folder_path)
        verify_page_summary('117of117records,Page1of3', 'Step 1: Verify page summary.')
        expected_heading = ['Region', 'State', 'City', 'Product', 'Category', 'UnitSales', 'DollarSales', 'BudgetUnits', 'BudgetDollars', 'UnitSales', 'DollarSales', 'BudgetUnits', 'BudgetDollars', 'UnitSales', 'DollarSales', 'BudgetUnits', 'BudgetDollars']
        active_rpt_obj.verify_column_heading('IWindowBodyFTS_0_0', expected_heading, 'Step 1.1: Verify heading.')
        active_rpt_obj.verify_active_report_dataset(case_id+'.xlsx', 'Step 1.2: Verify data set', table_css="#IWindowBodyFTB_0_0")
         
        """
        Step 3: Resize the window to see Horizontal Scroll bar
        """
        re_size_window()
        time.sleep(3)
        utilobj.verify_object_visible("#IWindowBodyFBO_0_0 .vertical-virtual-scrollbar-wrapper", True, 'Step 3: Verify Horizontal Scroll bar.')
        utilobj.verify_object_visible("#IWindowBodyFBO_0_0 .vertical-scroll-indicator-wrapper", True, 'Step 3.1: Verify Horizontal Scroll bar.')
         
        """
        Step 4: From State Column click drop down and select Freeze Column
                Verify State Column Freezed and other columns are displaying properly.
        """
        select_menu_items('IWindowBodyFTS_0_0', 1, 'Freeze Column')
        time.sleep(5)
        active_rpt_obj.verify_freeze_column('Step 4: verify freeze column scroll bar',  scroll_window_id=freeze_table_css)
        active_rpt_obj.verify_freeze_column('Step 4.1: verify freeze column scroll bar',  scroll_window_id=freeze_table_css_1)
        column_list=['Region', 'State']
        active_rpt_obj.verify_column_heading(freeze_table_css, column_list, 'Step 4.2: Verify State Column Freezed.')
        column_list1=['City', 'Product', 'Category', 'UnitSales', 'DollarSales', 'BudgetUnits', 'BudgetDollars', 'UnitSales', 'DollarSales', 'BudgetUnits', 'BudgetDollars', 'UnitSales', 'DollarSales', 'BudgetUnits', 'BudgetDollars']
        active_rpt_obj.verify_column_heading(freeze_table_css_1, column_list1, 'Step 4.3: Verify State Column Freezed and other columns are displaying properly.')
        first_freeze_table_object = utilobj.validate_and_get_webdriver_object('#hfreezeGridPage_0 .slideA', "First freeze table")
        if Global_variables.browser_name == 'firefox':
            actual_border_width = first_freeze_table_object.value_of_css_property('border-right-width')
            utilobj.asequal('1px', actual_border_width, 'Step 4.4: Indicating the freeze line')
        else:
            actual_border_width = int(utilobj.get_element_css_propery(first_freeze_table_object, 'border-right')[:1])
            utilobj.asequal(1, actual_border_width, 'Step 4.4: Indicating the freeze line')
        utilobj.verify_object_visible("#IWindowBodyFBO_0_0_r .horizontal-scroll-indicator-wrapper", True, 'Step 4.5: Verify Horizontal Scroll bar.')
        utilobj.verify_object_visible("#IWindowBodyFBO_0_0_r .horizontal-virtual-scrollbar-wrapper", True, 'Step 4.6: Verify Horizontal Scroll bar.')
         
        """
        Step 5: Now move the non Freeze Columns
                Verify State Column still Freezed and non Freeze Columns are moving properly
        """
         
        before_scroll_state_cell_object = utilobj.validate_and_get_webdriver_object("#TCOL_0_C_1_f", 'State Cell')
        berfore_scroll_state_cell_object_location_x = int(core_utilobj.get_web_element_coordinate(before_scroll_state_cell_object, element_location='middle_left')['x'])
        before_scroll_category_cell_object = utilobj.validate_and_get_webdriver_object("#TCOLTD_0_C_4_f", 'Category Cell')
        berfore_scroll_category_cell_object_location_x = int(core_utilobj.get_web_element_coordinate(before_scroll_category_cell_object, element_location='middle_left')['x'])
        veritical_scroll_bar = utilobj.validate_and_get_webdriver_object("#IWindowBodyFBO_0_0_r .horizontal-scroll-indicator-wrapper", 'Vertical scroll bar after freeze')
        if Global_variables.browser_name == 'firefox':
            move(1000)
        else:
            scroll_able_object = core_utilobj.get_web_element_coordinate(veritical_scroll_bar)
            utilobj.drag_drop_on_screen(sx_offset=int(scroll_able_object['x']), sy_offset=int(scroll_able_object['y']-20), tx_offset=int(scroll_able_object['x']+90), ty_offset=int(scroll_able_object['y']-20))
        time.sleep(2)
        after_scroll_state_cell_object = utilobj.validate_and_get_webdriver_object("#TCOL_0_C_1_f", 'State Cell')
        after_scroll_state_cell_object_location_x = int(core_utilobj.get_web_element_coordinate(after_scroll_state_cell_object, element_location='middle_left')['x'])
        after_scroll_category_cell_object = utilobj.validate_and_get_webdriver_object("#TCOLTD_0_C_4_f", 'Category Cell')
        after_scroll_category_cell_object_location_x = int(core_utilobj.get_web_element_coordinate(after_scroll_category_cell_object, element_location='middle_left')['x'])
        if after_scroll_category_cell_object_location_x < berfore_scroll_category_cell_object_location_x and after_scroll_state_cell_object_location_x == berfore_scroll_state_cell_object_location_x:
            status = True
        else:
            status = False
        utilobj.asequal(True, status, 'Step 05.01: Verify State Column still Freezed and non Freeze Columns are moving properly.')
         
        """
        Step 6: Again From State Column click drop down and select Un Freeze All
                Verify State Column is Un Freezed and report is displaying without any error
        """
        select_menu_items('IWindowBodyFTS_0_0', 1, 'Unfreeze All')
        time.sleep(5)
        utilobj.verify_object_visible("#IWindowBodyFBO_0_0_r .horizontal-scroll-indicator-wrapper", False, 'Step 06.01: Verify Horizontal Scroll bar.')
        utilobj.verify_object_visible("#IWindowBodyFBO_0_0_r .horizontal-virtual-scrollbar-wrapper", False, 'Step 06.02: Verify Horizontal Scroll bar.')
        active_rpt_obj.verify_active_report_dataset(case_id+'.xlsx', 'Step 06.03: Verify data set', table_css="#IWindowBodyFTB_0_0")
         
        """
        Step 7: Dismiss the window and logout.
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()