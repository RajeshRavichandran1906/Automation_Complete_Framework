'''
Created on Aug 10, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7073&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055524
TestCase Name = AHTML:negative color is not applied in visualized column(127568)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException

class C2055524_TestClass(BaseTestCase):

    def test_C2055524(self):
        
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj= visualization_resultarea.Visualization_Resultarea(self.driver)
        """
        Step 1. Execute the attached repro - 127568.fex
        """
        utillobj.active_run_fex_api_login("127568.fex", "S7073", 'mrid', 'mrpass')
        parent_css="table#IWindowBody0.arGrid"
        result_obj.wait_for_property(parent_css, 1)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.a: Verify the Report Heading')
        column_list=['CAR', 'TEST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        #utillobj.create_data_set('ITableData0','I0r','C2055524_Ds_01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2055524_Ds_01.xlsx',"Step 01.c: Verify entire Data set in Page 1") 
         
         
        """
        Step 02a:Click on test column and locate the Visualize option.
        Step 03a: Click Visualize.. 
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Visualize')  
        time.sleep(2)
        driver.implicitly_wait(1)
        #Expected_list = ['rgba(191, 64, 108, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(191, 64, 108, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(23, 5, 122, 1)', 'rgba(191, 64, 108, 1)', 'rgba(191, 64, 108, 1)', 'rgba(191, 64, 108, 1)']
        Expected_list = [True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, True, True]
        actual_list = []
        total_rows=driver.find_elements_by_css_selector("[id='ITableData0'] tr[id ^= 'I0r']")
        for i in range(0, len(total_rows)):
            try:
                actual_color_code=driver.find_element_by_css_selector("[id='ITableData0']" + " tr[id ^= 'I0r" + str(i) +"'] > td:nth-child(3) > table table td").value_of_css_property('background-color')
                color = True if actual_color_code in ['rgba(191, 64, 108, 1)', 'rgb(191, 64, 108)'] else False
                actual_list.append(color)
            except NoSuchElementException:
                actual_list.append('Null')
        utillity.UtillityMethods.asequal(self,actual_list, Expected_list,'Step 04.c: Verify visualization added for Mixed pos/neg')
        #miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'gray', 'Step 03b: Verify visualization added for Total')         
        time.sleep(5)       
        
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
