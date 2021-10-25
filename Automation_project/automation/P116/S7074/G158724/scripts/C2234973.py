'''
Created on June 9, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234973
TestCase Name = AHTML: JSCHART: Pie showing empty circle for null data (166076)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea
from common.lib import utillity


class C2234973_TestClass(BaseTestCase):

    def test_C2234973(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """ Step 1: Launch WF, New > Visualization 
                    using the wf-retail-lite file.
                    Expect to see the following Bar chart Visualization Preview pane.
        """
        utillobj.infoassist_api_login('idis', 'baseapp/wf_retail_lite', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 text[class='title']"
        utillobj.synchronize_with_visble_text(parent_css, "DropMeasuresorSortsintotheQueryPane", 125)
       
        ribbonobj.change_chart_type("bar")
        parent_css="#TableChart_1 .chartPanel rect[class*='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 15)
        
        """ step 2: From Home tab Click Change dropdown button and select Bar and Double click "Cost of Goods".
        """
        metadataobj.datatree_field_click('Cost of Goods', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, "Cost of Goods", 15)
        
        """
            Expect to see the following Visualization
        """
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'lochmara', 'Step 2.2: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 2.3: Verify Number of circle')
        result_obj.verify_yaxis_title("TableChart_1", 'Cost of Goods', "Step 2.4: Verify X-Axis Title")
        expected_xval_list=['']
        expected_yval_list=['0', '200M', '400M', '600M', '800M', '1,000M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2.5: Verify XY Label')
         
        """ Step 3: Right mouse click on Cost of Goods in the Query pane.
                    Select Sort/Sort/Ascending
                    Expect to see the following Visualization with the Sort Ascending icon with Cost of Goods in the Horizontal Axis bucket.
        """
        metadataobj.querytree_field_click("Cost of Goods", 1, 1, "Sort", "Sort","Ascending")
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(7)", "Cost of Goods", 15)
        time.sleep(2)
        metadataobj.verify_query_pane_field('Horizontal Axis',"Cost of Goods",1, "Step 03:01:Verify querypane field added in the querybucket and showing gray color", color='Trolley_Grey',font_style='italic')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(7)", "Cost of Goods", 15)
        
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'lochmara', 'Step 3.2: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 3.3: Verify Number of circle')
        result_obj.verify_yaxis_title("TableChart_1", 'Cost of Goods', "Step 3.4: Verify X-Axis Title")
        expected_xval_list=['']
        expected_yval_list=['0', '200M', '400M', '600M', '800M', '1,000M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.5: Verify XY Label')
        
        time.sleep(5)
        
        """ Step 4: Right mouse click on Cost of Goods in the Query pane.
                    Select Sort/Sort/Descending
                    Expect to see the following Visualization with the Sort Descenfing icon with Cost of Goods in the Horizontal Axis bucket.
        """
        metadataobj.querytree_field_click("Cost of Goods", 1, 1, "Sort", "Sort","Descending")
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(9)", "Cost of Goods", 15)
        metadataobj.verify_query_pane_field('Horizontal Axis',"Cost of Goods",1, "Step 04:02:Verify querypane field added in the querybucket and showing gray color", color='Trolley_Grey',font_style='italic')
        
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'lochmara', 'Step 4.3: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 4.4: Verify Number of circle')
        result_obj.verify_yaxis_title("TableChart_1", 'Cost of Goods', "Step 4.5: Verify X-Axis Title")
        expected_xval_list=['']
        expected_yval_list=['0', '200M', '400M', '600M', '800M', '1,000M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4.6: Verify XY Label')
        
        time.sleep(5)
        utillobj.switch_to_default_content(pause=5)
        
        
if __name__ == '__main__':
    unittest.main()