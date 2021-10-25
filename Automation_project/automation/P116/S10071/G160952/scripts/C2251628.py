'''
Created on Jan 17, 2018

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10071&group_by=cases:section_id&group_id=160952&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2251628
TestCase Name = Verify compound report,global filter window closes for second time (131548)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous ,active_filter_selection
from common.lib import utillity

class C2251628_TestClass(BaseTestCase):

    def test_C2251628(self):
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        """
            Step 01 :Run the attached repro - global_filter.fex.Expect to see the following AHTML Document with a Global Filter and two reports.
        """
        utillobj.active_run_fex_api_login('global_filter.fex','S10071_2', 'mrid', 'mrpass')
        result_obj.wait_for_property("#MAINTABLE_wbody0 [class='arGrid']",1,65)
        
        miscelanousobj.verify_page_summary('0','10of10records,Page1of1', 'Step 01.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2251628_Ds01.xlsx', 'Step 01.2:Verify the report is generated.')
        time.sleep(4)
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1', 'Step 01.3: Verify the page summary')
        utillobj.verify_data_set('ITableData1','I1r','C2251628_Ds01a.xlsx', 'Step 01.4:Verify the report is generated.')
        time.sleep(4)
           
        """
            Step 02:In the first report, click the drop down for the Country field and select the Global Filter menu option.
            Expect to see the following Global Filter menu panel appear.        
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 0, 'Filter', option, 'Step 02.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(2)
        miscelanousobj.select_menu_items("ITableData0", "0", "Global Filter")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 2.2: Verify Filter that the selection menu appears:")
        time.sleep(2)
         
        """
            Step 03:Close the global filter window.
            Expect to see the original Document, with the Global Filter menu removed.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelanousobj.verify_page_summary('0','10of10records,Page1of1', 'Step 03.1: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2251628_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2251628_Ds02.xlsx', 'Step 03.2:Verify the report is generated.')
        time.sleep(2)
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1', 'Step 03.3: Verify the page summary')
#         utillobj.create_data_set('ITableData1','I1r','C2251628_Ds02a.xlsx')
        utillobj.verify_data_set('ITableData1','I1r','C2251628_Ds02a.xlsx', 'Step 03.4:Verify the report is generated.')
        time.sleep(3)
            
        """
            Step 04:Once again select Global filter option in the compound report.
            Expect to see the following Global Filter menu panel appear. 
        """
        dashboard = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar']")
        utillobj.click_on_screen(dashboard, 'middle')
        utillobj.click_on_screen(dashboard, 'middle', click_type=0)
        time.sleep(2)
        production_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar'] td[id='iLayM4$']")
        production_css.click()
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 04.1: Verify Global Filter that the selection menu appears:")
           
        """
            Step 05:Close the global filter window for the second time.
            Expect to see the original Document, with the Global Filter menu removed.
        """
           
        miscelanousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelanousobj.verify_page_summary('0','10of10records,Page1of1', 'Step 05.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2251628_Ds03.xlsx', 'Step 05.2:Verify the report is generated.')
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1', 'Step 05.3: Verify the page summary')
        utillobj.verify_data_set('ITableData1','I1r','C2251628_Ds03a.xlsx', 'Step 05.4:Verify the report is generated.')
        time.sleep(2)
         
        """
            Step 06:Once again select Global filter option in the compound report.
            Expect to see the following Global Filter menu panel appear.        
        """
        dashboard = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar']")
        utillobj.click_on_screen(dashboard, 'middle')
        utillobj.click_on_screen(dashboard, 'middle', click_type=0)
        time.sleep(2)
        production_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar'] td[id='iLayM4$']")
        production_css.click()
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 06.1: Verify Global Filter that the selection menu appears:")
        
        """
            Step 07:In the Global Filter panel, click Add Condition.Select Country.
            Use the drop down for the operator and select Not Equal.From the value box, select ENGLAND.       
        """
        filterselectionobj.add_global_condition_field('COUNTRY', parent_menu_css="0_globalop_0")
        time.sleep(4)
        filterselectionobj.create_filter(1,'Not equal', value1='ENGLAND')
        time.sleep(4)
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 07.1: Verify Filter that the selection menu appears:',['COUNTRY', 'Not equal','ENGLAND'])
        
        """
            Step 08:Click the Filter button.Expect to see the Document display with both reports not containing data for ENGLAND.      
        """
        
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary('0','7of10records,Page1of1', 'Step 08.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2251628_Ds04.xlsx', 'Step 08.2:Verify the report is generated.')
        miscelanousobj.verify_page_summary('1','7of10records,Page1of1', 'Step 08.3: Verify the page summary')
        utillobj.verify_data_set('ITableData1','I1r','C2251628_Ds04a.xlsx', 'Step 08.4:Verify the report is generated.')
        time.sleep(3)
        
        """
            Step 09:Click the Clear All button to remove the Filter operation.Expect to see the original Document with ENGLAND once again present.
            Also expect to see the Global Filter panel reset.      
        """
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(3)
        miscelanousobj.verify_page_summary('0','10of10records,Page1of1', 'Step 09.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2251628_Ds05.xlsx', 'Step 09.2:Verify the report is generated.')
        time.sleep(3)
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1', 'Step 09.3: Verify the page summary')
        utillobj.verify_data_set('ITableData1','I1r','C2251628_Ds05a.xlsx', 'Step 09.4:Verify the report is generated.')
        time.sleep(3)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 06.1: Verify Global Filter that the selection menu appears:")
        
        """
            Step 10:Close the global filter window.Expect to see the original Document with no Global Filter menu present.   
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','10of10records,Page1of1', 'Step 10.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2251628_Ds06.xlsx', 'Step 10.2:Verify the report is generated.')
        time.sleep(3)
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1', 'Step 10.3: Verify the page summary')
        utillobj.verify_data_set('ITableData1','I1r','C2251628_Ds06a.xlsx', 'Step 10.4:Verify the report is generated.')
        time.sleep(3)
                
if __name__ == '__main__':
    unittest.main()
    