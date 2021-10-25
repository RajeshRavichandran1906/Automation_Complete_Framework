'''
Created on Nov 3, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053852
Verify Using Cache request when Export to Filtered only HTML displays with column title.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, ia_run, visualization_resultarea
from common.lib import utillity
import unittest,time

class C2053855_TestClass(BaseTestCase):

    def test_C2053855(self):
        
        driver = self.driver #Driver reference object created'
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        table_run = ia_run.IA_Run(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        """
        Step 01: Execute the attached Fex with Cache ON.
        """
        utillobj.active_run_fex_api_login("119866.fex", "S7077", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
        
        column_list=['Country Name', 'Car','Model', 'Bodytype', 'Number of Seats', 'Dealer Cost', 'Retail Cost']
        
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '119866.xlsx','Step 01.3: Verify data set')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '119866.xlsx')
        
        
        """
        Step 02: Add a filter: Country Name Equals ENGLAND and click Filter.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        time.sleep(15)
        
        miscelanousobj.move_active_popup(1, 350, 450)
        time.sleep(4)
        
        filterselectionobj.create_filter(1, 'Equals', value1='ENGLAND')
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        
        time.sleep(8)
        
        """Step 03: Click on Country and select Export > Filtered Only"""
        
        #Step 04: Verify Report is displayed with column title.
        
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','HTML','Filtered only')
        
        time.sleep(12)
        utillobj.switch_to_window(1)
        driver.maximize_window()
        time.sleep(9)
         
#         table_run.create_table_data_set('html>body>table', 'C2053855_Ds01.xlsx')
        
        ''' In IE we can't Identify 'html>body>table', so go with 'tag' name script verification check point '''
        if browser == 'IE':
            actual_data=driver.find_element_by_tag_name("html").text.split("\n")
            expected_data=['PAGE 1',  'CountryName Car Model Bodytype Numberof Seats DealerCost RetailCost',  'ENGLAND JAGUAR V12XKE AUTO CONVERTIBLE 2 7,427 8,878',  'ENGLAND JAGUAR XJ12L AUTO SEDAN 5 11,194 13,491',  'ENGLAND JENSEN INTERCEPTOR III SEDAN 4 14,940 17,850',  'ENGLAND TRIUMPH TR7 HARDTOP 2 4,292 5,100']
            utillobj.as_List_equal(expected_data, actual_data, 'Step 04: Verify data set')
        else:
            table_run.verify_table_data_set('html>body>table','C2053855_Ds01.xlsx','Step 04: Verify data set')
         
        driver.close()
         
        time.sleep(4)
        utillobj.switch_to_main_window()
        time.sleep(3)
        filterselectionobj.close_filter_dialog(popup_id='wall1')
        time.sleep(2)
        
        
        
        

if __name__ == "__main__":
    unittest.main()