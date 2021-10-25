'''
Created on Aug 09, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7073&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055523
TestCase Name = AHTML_Cache:visualize ROW-TOTAL column-get Error,hangs (110336)
'''
import unittest
import time
import re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2055523_TestClass(BaseTestCase):

    def test_C2055523(self):
        
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached repro - 139120.fex
        """
        utillobj.active_run_fex_api_login("110336.fex", "S7073", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '288of288records,Page1of6', 'Step 01.a: Verify the Report Heading')
        column_list=['City', 'Date', 'Budget Dollars', 'Budget Units', 'TOTAL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        utillobj.create_data_set('ITableData0','I0r','C2055523_Ds_01.xlsx')
        #utillobj.verify_data_set('ITableData0','I0r','C2055523_Ds_01.xlsx',"Step 01.c: Verify entire Data set in Page 1") 
        
        
        """
        Step 02a: From the drop down for the TOTAL column, locate the Visualize option. 
        """
        obrowser = utillobj.parseinitfile('browser')
        if obrowser == 'IE':
            Expected_list = ['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        else:
            Expected_list = ['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Save Changes','Export', 'Print', 'Window', 'Restore Original']
        print(obrowser)
        #Expected_list = ['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_btn_css="#ITableData0 #popid0_4 img"
        driver.find_element_by_css_selector(menu_btn_css).click()
        time.sleep(2)
        x = driver.find_elements_by_css_selector("#dt0_4_0>table>tbody>tr span[id^='set']")
        Actual_list=[]
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            if lineObjbj.group(1) != None:
                Actual_list.append(lineObjbj.group(1))
        print(Actual_list)
        utillity.UtillityMethods.asequal(self,Actual_list, Expected_list,'Step 02.a: Expect to see the following Active drop down menu for TOTAL')
       
        if obrowser=='Firefox' :
            temp_click=driver.find_element_by_css_selector("#TCOL_0_C_4")
            temp_click.click()
            time.sleep(2)
        """
        Step 03a: Click Visualize..
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Visualize')  
        time.sleep(3)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'light_gray', 'Step 03b: Verify visualization added for Total')         
        time.sleep(3)       
        
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
