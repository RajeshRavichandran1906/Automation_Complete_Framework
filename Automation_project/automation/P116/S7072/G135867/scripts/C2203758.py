'''
Created on Oct 7, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203756
'''
import unittest,time
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,active_miscelaneous,ia_styling

class C2203758_TestClass(BaseTestCase):

    def test_C2203758(self):
        
        """
            TESTCASE OBJECTS
        """
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
                
        """
        Step 01: Create an report using GGSALES master file
        """
        utillobj.infoassist_api_login('report', 'ibisamp/ggsales', 'P116/S7072', 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(100)
        time.sleep(4)
        
        """
        Step 02: Select format as Active Report.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 03: Select fields Category, Product ID, Product, State, Unit Sales , Dollar Sales.
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        metadataobj.datatree_field_click('Product ID', 2, 1)
        metadataobj.datatree_field_click('Product', 2, 1)
        metadataobj.datatree_field_click('State', 2, 1)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        time.sleep(5)
        
        """
        Step 04: From Format tab select features and click on Accordion option
        """
        ribbonobj.select_ribbon_item('Format', 'Accordion')
        time.sleep(5)
       
        """
        Step 05: Select Unit Sales and right click for selecting Traffic light condition.
        """
        metadataobj.querytree_field_click('Unit Sales', 1,1,'More','Traffic Light Conditions...')
        time.sleep(2)
        
        """
        Step 06: Select the value dropdown from the unit sales and click "1008" value for the condition.
        """
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', value_box_input=1008)
        time.sleep(4)
        
        """
        Step 07: Click on the Text color icon and select the color for condition and click OK.
        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, text_color='coral')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(5)
        
        """
        Step 08: Execute the report and from column drop down select Accordion->Expand all.
        """
        ribbonobj.select_visualization_top_toolbar_item('run')
        time.sleep(3)
        core_utils.switch_to_frame()
        time.sleep(8)
        miscellaneousobj.select_menu_items('ITableData0', 0, 'Accordion','Expand All')
        time.sleep(5)
        
        """
        Step 09: Verify conditional styling is applied to accordion report.
        """
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203758_Ds01.xlsx','Step 09.01: Verify data set',color='coral')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()