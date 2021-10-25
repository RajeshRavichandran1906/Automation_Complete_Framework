'''
Created on January 7, 2019

@author: KK14897

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5831044
TestCase Name = AHTML: Cache ON, filtering on QYY/Mtr/Wtr dates causes looping (ACT-1292)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.wftools import active_report
from common.lib import core_utility

class C5831044_TestClass(BaseTestCase):
    
    def test_C5831044(self):
        
        ac_obj=active_chart.Active_Chart(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        '''
        Step 1 : Sign in to WebFOCUS
        http://machine:port/{alias}
        Step 2 : Execute fex using below API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/S18035&BIP_item=ACT-1292.fex
        '''
        ar_obj.run_active_report_using_api("ACT-1292.fex", repository_path=folder_path, column_css="#ITableData0 tr:nth-child(3) td:nth-child(2)", synchronize_visible_element_text="1996/12/01")
        
        '''
        Step 3 : Click drop down from Mtr Order Date
        Step 4 : Select Filter->Equals and select a single value JUNE
        '''
        ar_obj.select_menu_items('ITableData0', 13, 'Filter','Equals')
        ar_obj.create_filter(1, 'Equals', value1='June')
        
        '''
        Step 5 : Click filter and Verify the Mtr Order Date values are filtered properly without any errors
        Expect to see the filter values displays 101 of 1000 records
        '''
        ar_obj.filter_button_click('Filter')
        ar_obj.verify_page_summary(0, '101of1000records,Page1of2', "Step 05.01 : Verify Page Summary")
        
        '''
        Step 6 : Close the filter selection window
        '''
        ar_obj.close_filter_dialog()
        '''
        Step 7 : Now Select drop down from Wtr Order Date
        Step 8 : Select Filter->Equals and select a single value Friday
        '''
        ar_obj.select_menu_items('ITableData0', 14, 'Filter','Equals')
        ar_obj.create_filter(1, 'Equals', value1='Friday')
        
        '''
        Step 9 : Click filter and Verify the Wtr Order Date values are filtered properly without any errors
        Expect to see the filter values displays 181 of 1000 records
        '''
        ar_obj.filter_button_click('Filter')
        ar_obj.verify_page_summary(0, '181of1000records,Page1of4', "Step 09.01 : Verify Page Summary")

        '''
        Step 10 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        ac_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()