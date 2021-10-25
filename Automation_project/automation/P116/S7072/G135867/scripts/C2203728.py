'''
Created on Sep 29, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203728
'''
import unittest,time
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,ia_resultarea, visualization_ribbon,visualization_metadata

class C2203728_TestClass(BaseTestCase):

    def test_C2203728(self):
        
        """
            TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resobj=ia_resultarea.IA_Resultarea(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Right click on folder created in IA and select New > Report and select Reporting server as GGSALES
        """
        utillobj.infoassist_api_login('Report', 'ibisamp/ggsales', 'P116/S7072', 'mrid', 'mrpass')
       
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
        ia_resobj.verify_report_data_set('TableChart_1', 19,6, 'C2203727_Ds01.xlsx',"Step 03: Verify columns for a report is displayed on canvas")
        
        """
        Step 04: Now go to Format tab and select Accordion option
        """
        ribbonobj.select_ribbon_item('Format','Accordion')
        
        """
        Step 05: Click Run command
        Click dropdown menu from any column and select Accordion > Expand All
        Verify all the fields of the report are expanded and all the columns are visible
        
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        core_utils.switch_to_frame()
        time.sleep(8)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Accordion','Expand All')        
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','I0r','C2203728_Ds01.xlsx',"Step 05: Verify the report after Expand All")
        
        """
        Step 06: Click dropdown menu from any column and select Accordion > Collapse All
        Verify all the fields of the report are collapsed and only Category column is visible
        """
        time.sleep(4)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Accordion','Collapse All')        
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','I0r','C2203728_Ds02.xlsx',"Step 06: Verify the report after Collapse All")
        
        """
        Step 07: Click dropdown menu from any column and select Accordion > Switch to Flat
        Verify all the fields of the report are expanded and all the columns are visible
        """
        time.sleep(4)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Accordion','Switch to Flat')        
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','I0r','C2203728_Ds03.xlsx',"Step 07: Verify the report after Switch to Flat")
  
if __name__ == '__main__':
    unittest.main()