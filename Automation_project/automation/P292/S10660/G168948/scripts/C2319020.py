'''
Created on Oct 5, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319020
TestCase Name = Home Tab - Define field
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.lib import utillity, core_utility

class C2319020_TestClass(BaseTestCase):
    
    def test_C2319020(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2319020'
        expected_field_value='"Revenue" * - 1'
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['-400M', '-300M', '-200M', '-100M','0', '100M', '200M', '300M', '400M']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)
        
        """    2. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        utillobj.synchronize_until_element_is_visible("#fname", metaobj.chart_long_timesleep)
        
        """    3. Set Field = "NEG_REVENUE".    """
        """    4. Change Format to "D20.2".    """
        """    5. Double click field "REVENUE".    """
        calculate_obj.enter_define_compute_parameter("NEG_REVENUE", "D20.2", "Revenue", 1)
        time.sleep(5)
        
        """    6. Verify it got inserted into the textbox.    """
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value")
        utillobj.asequal(expected_field_value[:-5], actual_field_value, "Step 06a: Verify the define field value")
        
        """    7. Add "* -1" in the textbox.    """
        calculate_obj.select_calculation_btns("mult->minus->one")
        
        """    8. Verify the entry is same as shown.    """
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value")
        utillobj.asequal(expected_field_value, actual_field_value, "Step 08a: Verify the define field value")
        
        """    9. Click "OK".    """
        calculate_obj.close_define_compute_dialog("ok")
        utillobj.synchronize_until_element_disappear("#fname", metaobj.chart_long_timesleep)
        
        """    10. Verify the define (NEG_REVENUE) has been added to the Data pane (Measures fields list).    """
        metaobj.expand_field_tree('Measure Groups->Sales')
        time.sleep(2)
        metaobj.verify_data_pane_field("Measure Groups", "NEG_REVENUE", 17, "Step 10a: Verify the define (NEG_REVENUE) has been added to the Data pane (Measures fields list)")
        
        """    11. Click Calculation > "Detail (Define)".    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        utillobj.synchronize_until_element_is_visible("#fname", metaobj.chart_long_timesleep)
        
        """    12. Create a new define as shown:
         Field = DEFN_PROD
         Format = A40
         Field used = Product,Category    """
        calculate_obj.enter_define_compute_parameter("DEFN_PROD", "A40", "Product,Category", 1)
        time.sleep(5)
        
        """    13. Click "OK".    """
        calculate_obj.close_define_compute_dialog("ok")
        utillobj.synchronize_until_element_disappear("#fname", metaobj.chart_long_timesleep)
        
        """    14. Verify "DEFN_PROD" has been added to the Data pane (Dimensions fields list).    """
        metaobj.expand_field_tree('Dimensions->Product->Product')
        time.sleep(2)
        metaobj.verify_data_pane_field("Dimensions", "DEFN_PROD", 9, "Step 14a: Verify 'DEFN_PROD' has been added to the Data pane (Dimensions fields list)")
        
        """    15. Double click "NEG_REVENUE", "Revenue", "DEFN_PROD".    """
        metaobj.datatree_field_click("Measure Groups->Sales->NEG_REVENUE", 2, 1)
        riser_css = "#MAINTABLE_wbody1_f rect[class*='riser']"
        utillobj.synchronize_with_number_of_element(riser_css, 1, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("Revenue", 2, 1)
        utillobj.synchronize_with_number_of_element(riser_css, 2, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("Dimensions->Product->Product->DEFN_PROD", 2, 1)
        utillobj.synchronize_with_number_of_element(riser_css, 14, metaobj.chart_long_timesleep)
        
        """    16. Verify following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'DEFN_PROD', "Step16:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEG_REVENUE','Revenue'], "Step 16:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 16.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 16.c(ii): Verify first bar color")
        
        """    17. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
        
        """    18. Verify output at Runtime is correct.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'DEFN_PROD', "Step18:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEG_REVENUE','Revenue'], "Step 18:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 18.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 18.c(ii): Verify first bar color")
        
        """    19. Close the output window.    """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", metaobj.chart_long_timesleep)
        
        """    20. Click "IA" > "Save" > Save As "C2160105".    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.chart_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    21. Close IA from X in the tool's upper right corner.    """
        """    22. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    23. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160105.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_1',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar']", metaobj.chart_long_timesleep)
        
        """    24. Verify Define fields (NEG_REVENUE, DEFN_PROD) are displayed in the fields List.    """
        metaobj.expand_field_tree('Dimensions->Product->Product')
        time.sleep(2)
        metaobj.verify_data_pane_field("Dimensions", "DEFN_PROD", 6, "Step 24a: Verify 'DEFN_PROD' has been added to the Data pane (Dimensions fields list)")
        metaobj.expand_field_tree('Measure Groups->Sales')
        time.sleep(2)
        metaobj.verify_data_pane_field("Measure Groups", "NEG_REVENUE", 3, "Step 24b: Verify the define (NEG_REVENUE) has been added to the Data pane (Measures fields list)")
        
        """    25. Verify chart displayed on canvas is correct.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'DEFN_PROD', "Step 25:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['NEG_REVENUE','Revenue'], "Step 25:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 25:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 25.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!", "lochmara", "Step 25.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "pale_green", "Step 25.c(ii): Verify first bar color")
        
        """    26. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()