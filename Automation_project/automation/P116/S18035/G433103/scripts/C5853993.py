'''
Created on January 7, 2019

@author: KK14897

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5853993
TestCase Name = Filter using DATE/DATETIME fields with Cache ON causes Fex errors. (proj 153599)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_report
from common.lib import core_utility

class C5853993_TestClass(BaseTestCase):
    
    def test_C5853993(self):
        
        ar_obj=active_report.Active_Report(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        '''
        Step 1 :Execute the attached 153599.fex using the below API Url
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9043&BIP_item=Active_Technologies/Report/153599.fex
        '''
        ar_obj.run_active_report_using_api("153599.fex", repository_path=folder_path, column_css="#ITableData0 tr:nth-child(3) td:nth-child(1)", synchronize_visible_element_text="Order Number INTEGER")
        
        '''
        Step 2 : Select the Date YYMD field, then Filter and Not Equal.
        From the value box, select the first value - 1996/01/01 and click Filter.
        Expect to see the report starting with 1996/02/01 and containing 820 lines.
        '''
        ar_obj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        ar_obj.create_filter(1, 'Not equal', value1='1996/01/01')
        ar_obj.filter_button_click('Filter')
        ar_obj.verify_page_summary(0, '820of1000records,Page1of15', "Step 02 : Verify Page Summary")
        
        '''
        Step 3 : Exit the Filter menu
        Expect to see the original 1000 line report.
        '''
        ar_obj.close_filter_dialog()
        ar_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03 : Verify Page Summary")
        
        '''
        Step 4 : Select the DATETIME HYYMDSA field, then Filter and Equal.
        From the value box, select the first value - 2002/12/31 11:59:59PM, then click Filter.
        Expect to see the report with 5 rows
        '''
        ar_obj.select_menu_items('ITableData0', 7, 'Filter','Equals')
        ar_obj.create_filter(1, 'Equals', value1='2002/12/31 11:59:59PM')
        ar_obj.filter_button_click('Filter')
        ar_obj.verify_page_summary(0, '5of1000records,Page1of1', "Step 04 : Verify Page Summary")
        
if __name__ == '__main__':
    unittest.main()