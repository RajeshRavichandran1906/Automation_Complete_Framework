'''
Created on Sep 7, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053800
'''

import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.pages import active_miscelaneous,active_chart_rollup,visualization_resultarea

class C2053800_TestClass(BaseTestCase):

    def test_C2053800(self):
        
        """
            Step 01: Execute the 121426.fex
        """
        act_obj = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        utillobj.active_run_fex_api_login("121426.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        miscelanousobj.verify_page_summary(0, '26of26records,Page1of1', "Step 01.01: Execute the 121426.fex")
        column_list=['Country', 'Region', 'State', 'Product Type', 'Line Total', 'Quantity', 'Cost of Goods Sold', 'Profit', 'Returns', 'Return Ratio']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.02: Verify all columns listed on the report 121426.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', '121426.xlsx','Step 01.03: Verify data set')
        
        """
        Step 02: From the Quantity column drop down menu, select chart -> scatter -> Profit
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Chart','Scatter','Profit')
        miscelanousobj.verify_popup_appears('wall1', 'Quantity by Profit', 'Step 02.01: Verify Quantitty by Profit opens')

        miscelanousobj.verify_active_popup_chart_tooltip('wall1', 'scatter', 'x', 'x=637y=13', 'Lochmara', 'Step 02.02: Verify tooltip')
         
        """
        Step 03: click on FIRST drop down icon and select Arrange By -> Product Type
        """
#         rollupobj.create_new_item(0, 'Arrange By->Product Type')
        act_obj.create_new_item('wall1', 'Arrange By->Product Type')
        miscelanousobj.verify_active_popup_chart_tooltip('wall1', 'line', 'Audio', 'Audiox=74104y=316', 'Lochmara', 'Step 03.01: Verify tooltip')
        
if __name__ == '__main__':
    unittest.main()        