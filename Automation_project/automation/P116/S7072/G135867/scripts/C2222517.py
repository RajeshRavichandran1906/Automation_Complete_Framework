'''
Created on Feb 5, 2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222517
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,wf_mainpage
from common.lib import utillity
import unittest,time
from selenium.webdriver.common.by import By



class C2222517_TestClass(BaseTestCase):

    def test_C2222517(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Run the attached 122806.fex from text editor.
        """
        utillobj.active_run_fex_api_login("ACT-265lime-red.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.a: Verify the Report Heading')
        column_list=['CAR', 'SEATS', 'SEATS', 'SEATS', 'SEATS', 'SEATS']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT-265lime-red.xlsx','Step 01.c: Verify data set')
        time.sleep(5)
        miscellaneousobj.verify_cell_property('ITableData0',0,3,'8','Step 01.1:Verify row highlighted',bg_color='red')
        miscellaneousobj.verify_cell_property('ITableData0',3,4,'4','Step 01.2:Verify row highlighted',bg_color='red')
        miscellaneousobj.verify_cell_property('ITableData0',5,0,'JENSEN','Step 01.3:Verify row highlighted')
        miscellaneousobj.verify_cell_property('ITableData0',5,1,'4','Step 01.4:Verify row highlighted',bg_color='lime')
        miscellaneousobj.verify_cell_property('ITableData0',5,2,'.','Step 01.5:Verify row highlighted',bg_color='lime')
        miscellaneousobj.verify_cell_property('ITableData0',6,3,'2','Step 01.6:Verify row highlighted',bg_color='transparent')
        
        """
        Step 02: Execute the attached repro - ACT-265red-lime.fex
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        utillobj.active_run_fex_api_login("ACT-265red-lime.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 02.a: Verify the Report Heading')
        column_list=['CAR', 'SEATS', 'SEATS', 'SEATS', 'SEATS', 'SEATS']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 02.b: Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT-265lime-red.xlsx','Step 02.c: Verify data set')
        time.sleep(5)
        miscellaneousobj.verify_cell_property('ITableData0',0,3,'8','Step 02.1:Verify row highlighted',bg_color='red')
        miscellaneousobj.verify_cell_property('ITableData0',3,4,'4','Step 02.2:Verify row highlighted',bg_color='red')
        miscellaneousobj.verify_cell_property('ITableData0',5,0,'JENSEN','Step 02.3:Verify row highlighted')
        miscellaneousobj.verify_cell_property('ITableData0',5,1,'4','Step 02.4:Verify row highlighted',bg_color='red')
        miscellaneousobj.verify_cell_property('ITableData0',5,2,'.','Step 02.5:Verify row highlighted',bg_color='lime')
        miscellaneousobj.verify_cell_property('ITableData0',6,3,'2','Step 02.6:Verify row highlighted',bg_color='transparent')
        
         
if __name__ == '__main__':
    unittest.main()  
                       
        