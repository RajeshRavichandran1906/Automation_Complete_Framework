'''
Created on Sep 28, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203727
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,ia_resultarea, visualization_ribbon,visualization_metadata
from common.lib import utillity

class C2203727_TestClass(BaseTestCase):

    def test_C2203727(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2203727'
        """
        Step 01: Right click on folder created in IA and select New > Report and select Reporting server as GGSALES
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_resobj=ia_resultarea.IA_Resultarea(self.driver)
        
        utillobj.infoassist_api_login('Report', 'ibisamp/ggsales', 'P116/S7072', 'mrid', 'mrpass')
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
         
        """
        Step 02: On the Format tab, in the Output Types group, click Active Report
        """
        ribbonobj.change_output_format_type('active_report')
        
        """
        Step 03: Select data from the left pane (Dimensions and Measures) Category, Product ID, Product, 
        State, Unit Sales, Dollar Sales
        Verify columns for a report is displayed on canvas with selected data.
        """
        time.sleep(5)
        metaobj.datatree_field_click("Unit Sales",1,1,'Sum')
        time.sleep(5)
        metaobj.datatree_field_click("Dollar Sales",1,1,'Sum')
        time.sleep(5)
        metaobj.datatree_field_click('Category',2,1)
        time.sleep(5)
        metaobj.datatree_field_click('Product ID',2,1)
        time.sleep(5)
        metaobj.datatree_field_click('Product',2,1)
        time.sleep(5)
        metaobj.datatree_field_click('State',2,1)
        time.sleep(5)
        ia_resobj.verify_report_data_set('TableChart_1', 19,6, Test_Case_ID+'_Ds01.xlsx',"Step 03: Verify columns for a report is displayed on canvas")
        
        """
        Step 04: Now go to Format tab and select Accordion option
        """
        ribbonobj.select_ribbon_item('Format','Accordion')
        
        """
        Step 05: Click Run command
        Verify Active Report is displayed with collapse sign(+) under Category column.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        self.driver.switch_to.frame(driver.find_element_by_css_selector("[id^='ReportIframe']"))
        time.sleep(4)
        utillobj.asequal('+',driver.find_element_by_css_selector('#I0r0\.0C0 div span').text,"Step 05: Verify + sign displayed under Category")
        
        """
        Step 06: Click + sign for each field and all the report menu options will get expanded.
        """        
        '''Gifts'''
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 63, 0) 
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 63, 1) 
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 63, 2)
        '''Food'''
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 30, 0)
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 30, 1)
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 30, 2)
        '''Coffee'''
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 0, 0)
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 0, 1)
        miscelanousobj.expand_or_colapse_accordian_field('ITableData0', 0, 2)
        
        """
        Step 07: When all the options are expanded a complete report will be displayed.
        """
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx',"Step 07: Verify the report is displayed")
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
       
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
