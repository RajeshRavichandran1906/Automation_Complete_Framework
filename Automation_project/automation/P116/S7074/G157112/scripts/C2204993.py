'''
Created on Jul 11, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204993
TestCase Name = HTML:AFLEX Compound report with 1 report doesnt work(Project 99382)

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2204993_TestClass(BaseTestCase):

    def test_C2204993(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204993'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
       
        """
        Step 01: Launch IA and create a new document using the ggsales master file.
        Change the output format to Active Report..
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#canvasFrame img"
        result_obj.wait_for_property(parent_css,2)
        time.sleep(2)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(4)
        
        """
        Add the fields unit sales, dollar sales, category, product, state
        """
        metadataobj.datatree_field_click("Unit Sales",2,1)
        parent_css="#canvasFrame #TableChart_1 div[class^='x']"
        result_obj.wait_for_property(parent_css, 2)
        
        metadataobj.datatree_field_click("Dollar Sales",2,1)
        parent_css="#canvasFrame #TableChart_1 div[class^='x']"
        result_obj.wait_for_property(parent_css, 4)
        
        metadataobj.datatree_field_click("Category",2,1)
        parent_css="#canvasFrame #TableChart_1 div[class^='x']"
        result_obj.wait_for_property(parent_css, 6)
        
        metadataobj.datatree_field_click("Product",2,1)
        parent_css="#canvasFrame #TableChart_1 div[class^='x']"
        result_obj.wait_for_property(parent_css, 11)
        
        metadataobj.datatree_field_click("State",2,1)
        time.sleep(6)
        
        """
        Step 02 : Run the report.
        Verify that the report generates properly, containing all the specified columns. 
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        parent_css="#ITableData0 .arGridColumnHeading [id^='TCOL']"
        result_obj.wait_for_property(parent_css, 5)
        time.sleep(4)
        miscelaneousobj.verify_page_summary(0,'107of107records,Page1of2','Step 02.1 : Verify page summary')
        miscelaneousobj.verify_column_heading('ITableData0',['Category', 'Product', 'State', 'Unit Sales', 'Dollar Sales'],'Step 02.2 : Verify containing all the specified columns')
        utillobj.verify_data_set('ITableData0', 'I0r','C2204993_Data_Set_01.xlsx','Step 02.3 : Verify that the report generates properly')
        
        """
        Step 03 : Check the report by selecting the state column and sorting in Descending order.
        Expect to see the following report in State sequence.
        """
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Sort Descending')
        time.sleep(4)
        miscelaneousobj.verify_page_summary(0,'107of107records,Page1of2','Step 03.1 : Verify page summary')
        miscelaneousobj.verify_column_heading('ITableData0',['Category', 'Product', 'State', 'Unit Sales', 'Dollar Sales'],'Step 03.2 : Verify table column headings')
        utillobj.verify_data_set('ITableData0', 'I0r','C2204993_Data_Set_02.xlsx','Step 03.3 : Verify Expect to see the following report in State sequence')
        
        """
        Save Document
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
       
        
if __name__=='__main__' :
    unittest.main()