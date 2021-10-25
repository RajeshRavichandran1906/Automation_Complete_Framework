'''
Created on Aug 25, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7075&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053811
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_tools
from common.lib import utillity
import time

class C2053811_TestClass(BaseTestCase):

    def test_C2053811(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolobj=active_tools.Active_Tools(driver)
        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-AHTML-001.fex and Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the AR-AHTML-001.fex and Verify the column heading')
        """
        2. Click State > Grid Tool
        Verify that Grid Tool is displayed.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        miscelanousobj.verify_popup_appears('wall1', 'Grid Tool', 'Step 02.1: that Grid Tool is displayed.')
        """
        3. Drag 'Product' column and 'Unit Sales' column from Column Order to Sort Order area
        Verify both the columns appear under Sort Order area Verify that sort order by default is A to Z.
        """
        toolobj.grid_tool_drag_drop_items('gridtoolt1', 'Product', 1, 0)
        time.sleep(1)
        toolobj.grid_tool_drag_drop_items('gridtoolt1', 'Unit Sales', 1, 1)
        time.sleep(1)
        """
        4. Change sort order of Product column from A - Z to Z - A by clicking sort arrow.
        Verify that sort order is from Z - A.  
        """
        toolobj.grid_tool_sort_item(1)
        time.sleep(1)
        sort_css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) div[title='Select Sort Order']" 
        sort_btns=self.driver.find_elements_by_css_selector(sort_css)
        utillobj.take_screenshot(sort_btns[0], 'GT_Sort_Descending',image_type='actual')
        """
        5. Click Ok.
        Verify that other column data are displayed per Product column.
        """
        toolobj.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(1)
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05.1: Verify column list in report heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2053811_Ds01.xlsx', 'Step 05.2: Verify that other column data are displayed per Product column.')
        """
        6. Now click State > Grid Tool again and change sort order for Unit Sales from Z - A.
        Verify that sort order is from Z - A. 
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        miscelanousobj.verify_popup_appears('wall1', 'Grid Tool', 'Step 06.1: that Grid Tool is displayed.')
        toolobj.grid_tool_sort_item(2)
        time.sleep(1)
        sort_css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) div[title='Select Sort Order']" 
        sort_btns=self.driver.find_elements_by_css_selector(sort_css)
        utillobj.take_screenshot(sort_btns[1], 'GT_Sort_Descending', image_type='actual')
        """
        7. Click Ok.
        Verify that report Product column in Z to A order and on second level it sorts Unit Sales. 
        Ie. For Product = Thermos, it shows Unit Sales from higher order to lower order, 29743/17678/17568/16734/16344.
        """
        toolobj.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(1)
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07.1: Verify column list in report heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2053811_Ds02.xlsx', 'Step 07.2: Verify the entire table to make sure all sorted data correct')
        
if __name__ == '__main__':
    unittest.main()    