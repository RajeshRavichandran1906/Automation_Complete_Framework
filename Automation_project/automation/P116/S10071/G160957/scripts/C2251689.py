'''
Created on Jan 19, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251689
TestCase Name = Multi-field Document Filter - Check Box.
'''
import unittest, time
import re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251689_TestClass(BaseTestCase):

    def test_C2251689(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251689'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        """    1. Execute the attached repro - ACT-287a.fex    """
            
        utillobj.active_run_fex_api_login('act-287a.fex', 'S10071_3', 'mrid', 'mrpass')
             
        resultobj.wait_for_property("#ITableData0",1,30)
         
        time.sleep(3)
         
        """    "1.1. Expand the window to maximum.    """
        """    "1.2. Expect to see the following Document with a Check Box and an 18 row Active Report.    """
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading')
        utillobj.create_data_set('ITableData0', 'I0r', 'C2251689_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251689_Ds01.xlsx', 'Step 1.2c: Verify data.')
        exp_list=['[All]', 'ENGLAND,JAGUAR', 'ENGLAND,JENSEN', 'ENGLAND,TRIUMPH', 'FRANCE,PEUGEOT', 'ITALY,ALFA ROMEO', 'ITALY,MASERATI', 'JAPAN,DATSUN', 'JAPAN,TOYOTA', 'W GERMANY,AUDI', 'W GERMANY,BMW']
        p1=self.driver.find_elements_by_css_selector("#checkbox_dOBJECT3 table tbody tr td:nth-child(2)")
        chkbox_lst=[]
        for i in p1:
            chkbox_lst.append(i.text)
        utillobj.as_List_equal(exp_list,chkbox_lst,'Step 1.2d Verify Checkbox contents')
        
        """    2. Check the first Italy selection for ITALY,ALFA ROMEO    """
        """    2.1. Expect to see 3 rows, all for Italy, Alfa Romeo.    """
        
                
        #iarun.select_active_dashboard_prompts("#checkbox_dOBJECT3", ['ITALY,ALFA ROMEO'])
        iarun.select_active_dashboard_prompts('checkbox', "#checkbox_dOBJECT3", ['ITALY,ALFA ROMEO'])
        
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '3of18records,Page1of1', 'Step 2.1a: Verify the Report Heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251689_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251689_Ds02.xlsx', 'Step 2.2a: Verify data after filter.')
        
        """    "3. Check the last JAPAN selection for JAPAN,TOYOTA    """
        """    "3.1. Expect to see 4 rows, with the single row for Japan, Toyota added to the rows for Italy,Alfa Romeo.    """
        
        iarun.select_active_dashboard_prompts('checkbox',"#checkbox_dOBJECT3", ['JAPAN,TOYOTA'])
        
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '4of18records,Page1of1', 'Step 3.1a: Verify the Report Heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251689_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251689_Ds03.xlsx', 'Step 3.2a: Verify data after 2nd filter.')
        time.sleep(5)
        
        """    4. Click the [All] option.    """
        """    4.1. Expect to see all 18 rows re-appear.    """
        
        iarun.select_active_dashboard_prompts('checkbox',"#checkbox_dOBJECT3", ['[All]'])
        
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 4.1a: Verify the Report Heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251689_Ds01.xlsx', 'Step 4.2a: Verify data on clicking ALL.')
        time.sleep(3)

        
if __name__=='__main__' :
    unittest.main()
        