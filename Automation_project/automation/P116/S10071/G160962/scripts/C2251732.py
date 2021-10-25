'''
Created on Jan 19, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251732
Test_Case Name : Document with scatter chart (usually with large answer sets) works correctly with cache
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_run, active_miscelaneous, visualization_resultarea
from common.lib import utillity

class C2251732_TestClass(BaseTestCase):

    def test_C2251732(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251732'
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        visual_result=visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01 : Execute the attached repro - Document-with-Scatter.
        """
        utillobj.active_run_fex_api_login('Document-with-Scatter.fex', 'S10071_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'Product', 60)
        
        """
            Step 01.1 : Expect to see an AHTML Document with a multi-line report and a multi-point Scatter diagram.
        """
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx', 'Step 01.1 : Verify Report data')
        active.verify_page_summary(0, '240of240records,Page1of5', 'Step 01.2 : Verify page summary')
        
        """
            Step 02 : Verify scatter chart
        """
        visual_result.verify_xaxis_title('MAINTABLE_wbody1_f', 'Product', 'Step 02.1 : Verify X-Axis title')
        visual_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Unit Sales', 'Step 02.1 : Verify Y-Axis title')
        expected_xaxis_label=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yaxis_label=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K']
        visual_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', expected_xaxis_label, expected_yaxis_label, 'Step 02.3 :', 15)
        visual_result.verify_riser_legends('MAINTABLE_wbody1_f', ['Category', 'Coffee', 'Food', 'Gifts'], 'Step 02.4 : Verify chart legend values')
        visual_result.verify_number_of_circles('MAINTABLE_wbody1_f', 0, 241, 'Step 02.4 : Verify number of circle in chart')
        active.verify_chart_title('MAINTABLE_wbody1_ft', 'Unit Sales by Category, Product, Date', 'Step 02.6 : Verify chart title')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation'], 'Step 02.7 : Verify chart tool menus', custom_css='[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['Sum'], 'Step 02.8 : Verify Aggregation menu text', text=True, custom_css="[id^='SUM'] td[class^='tabPagingTex']")
#         visual_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g50!mmarker!', ['Product:Latte', 'Unit Sales:42717', 'Category:Coffee', 'Date:1996/03/01', 'Filter Chart', 'Exclude from Chart'], 'Step 02.9 : Verify circle tooltip value')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step01')
        
if __name__ == '__main__':
    unittest.main()