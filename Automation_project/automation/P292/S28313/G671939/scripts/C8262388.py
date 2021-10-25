'''
Created on Aug 16, 2019

@author: osdamtx

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262388
TestCase Name = HIDENULLACRS ON respected after filtering at run time
'''
import unittest
from common.wftools.report import Report
from common.wftools.active_report import Active_Report
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
import pyautogui

class C8262388_TestClass(BaseTestCase):

    def test_C8262388(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj= Report(self.driver)
        core_utils_obj = CoreUtillityMethods(self.driver)
        active_obj = Active_Report(self.driver)
        util_obj = UtillityMethods(self.driver)
                
        """
            TESTCASE Variables
        """
        project_id = core_utils_obj.parseinitfile('project_id')
        suite_id = core_utils_obj.parseinitfile('suite_id')
        group_id = core_utils_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        case_id = 'C8262388'
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        
        '''
        step 1 : Run the below fex using API link
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S28313/G671939/ahtml_hidenullacrs_on.fex
        '''
        report_obj.run_fex_using_api_url(folder_name=folder_path, fex_name='ahtml_hidenullacrs_on',mrid='mrid', mrpass='mrpass',run_table_css='table[class="arGrid"] > tbody > tr')
        report_obj.wait_for_visible_text('#ITableData0', 'Product')
        
        '''
        step 01.01 : An active report appears, with two Region rows (Midwest and Northeast and two Product columns (Capuccino and Latte).
        The report entries for Midwest and Capuccino are missing; none of the others are.
        
        '''
        active_obj.verify_page_summary('0', '6of6records,Page1of1', 'Step 01.01: Verify page summary')
#         active_obj.create_active_report_dataset(DATA_SET_NAME1)
        active_obj.verify_active_report_dataset(DATA_SET_NAME1, msg='Step 01.02 : Verify report data', table_css='#ITableData0')
        
        """
        step 2: Click on the arrow to the right of Region, select Filter, and select Equals.
        """
        active_obj.select_menu_items('ITableData0', 0, 'Filter', 'Equals')
        
        """
        step 2.01: A Filter Selection window opens.
        """
        active_obj.verify_filter_selection_dialog(True, "Step 02.01: A Filter Selection window open",['Region', 'Equals'])
        
        """
        step 3: After the second, empty input box, click on the arrow and select Midwest.
        Click Filter.
        Move the Filter Selection box out of the way of the report.
        """
        active_obj.create_filter(1, 'Equals', value1="Midwest")
        active_obj.filter_button_click('Filter')
        
        source_element = util_obj.validate_and_get_webdriver_object('#wall1 .arWindowBarTitle', 'filter-panel-css')
        sourcevalue = core_utils_obj.get_web_element_coordinate(source_element)
        pyautogui.mouseDown(sourcevalue['x'], sourcevalue['y'], duration=1)
        pyautogui.moveTo(x=1000, y=33, duration=1)
        pyautogui.mouseUp(duration=1)
        
        
        """
        Step 3.01: Region is now limited to Midwest, and the only value for Product is Latte.
        The HIDENULLACRS=ON setting suppresses the column for Capuccino.
        """
#         active_obj.create_active_report_dataset(DATA_SET_NAME2)
        active_obj.verify_active_report_dataset(DATA_SET_NAME2, msg='Step 03.01 : Verify report data', table_css='#ITableData0')
        
        '''
        Step 4: Close the report.
        step 5 : Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        report_obj.api_logout()
        
    if __name__ == '__main__':
        unittest.main()
        

        
        