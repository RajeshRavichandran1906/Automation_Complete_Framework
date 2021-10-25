'''
Created on Jan 19, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251690
TestCase Name = Multi-field Document Filter - Radio Button.
'''
import unittest, time
import re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251690_TestClass(BaseTestCase):

    def test_C2251690(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251690'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        """    1. Execute the attached repro - ACT-287c_new.fex, Mximize the window.    """
            
        utillobj.active_run_fex_api_login('act-287c_new.fex', 'S10071_3', 'mrid', 'mrpass')
             
        resultobj.wait_for_property("#ITableData0",1,30)
         
        time.sleep(3)
         
        """    1.1 Expect to see the following Document with a Radio Button control and a 13 row Active Report.    """
        """    1.2. Verify that the values in the Check Box consist of Country,Bodytype values.    """
        
        miscelanousobj.verify_page_summary(0, '13of13records,Page1of1', 'Step 1.2a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "BODYTYPE", "DEALER_COST", "RETAIL_COST"]
        
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251690_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251690_Ds01.xlsx', 'Step 1.2c: Verify data.')
        exp_list=['[All]', 'ENGLAND,CONVERTIBLE', 'ENGLAND,HARDTOP', 'ENGLAND,SEDAN', 'FRANCE,SEDAN', 'ITALY,COUPE', 'ITALY,ROADSTER', 'ITALY,SEDAN', 'JAPAN,SEDAN', 'W GERMANY,SEDAN']
        p1=self.driver.find_elements_by_css_selector("#radiobutton_dPROMPT_1 table tbody tr td:nth-child(2)")
        box_lst=[]
        for i in p1:
            box_lst.append(i.text)
        utillobj.as_List_equal(exp_list,box_lst,'Step 1.2d Verify Radiobutton contents')
        
        """    2. Check the first England button for ENGLAND,HARDTOP    """
        """    2.1. Expect to see 1 row, for England,Hardtop    """
        
                
        iarun.select_active_dashboard_prompts('radiobutton', "#radiobutton_dPROMPT_1", ['ENGLAND,HARDTOP'])
        
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '1of13records,Page1of1', 'Step 2.1a: Verify the Report Heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251690_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251690_Ds02.xlsx', 'Step 2.2a: Verify data after filter.')
        
        """    3. Check the first Italy button for ITALY,COUPE    """
        """    3.1. Expect to see 2 rows, both for Italy, Coupe.    """
        
        iarun.select_active_dashboard_prompts('radiobutton',"#radiobutton_dPROMPT_1", ['ITALY,COUPE'])
        
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '2of13records,Page1of1', 'Step 3.1a: Verify the Report Heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251690_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251690_Ds03.xlsx', 'Step 3.2a: Verify data after 2nd filter.')
        time.sleep(5)
        
        """    4. Click the [All] option.    """
        """    4.1. Expect to see all 13 rows re-appear.    """
        
        iarun.select_active_dashboard_prompts('radiobutton',"#radiobutton_dPROMPT_1", ['[All]'])
        
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '13of13records,Page1of1', 'Step 4.1a: Verify the Report Heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251690_Ds01.xlsx', 'Step 4.2a: Verify data on clicking ALL.')
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()
        