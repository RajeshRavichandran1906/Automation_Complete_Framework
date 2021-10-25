'''
Created on Jun 16, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227720
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, metadata
from common.lib import utillity


class C2227720_TestClass(BaseTestCase):

    def test_C2227720(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227720'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem = "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(elem, 1, metaobj.chart_long_timesleep)
         
        """
        Step 02: Double click "Gross Profit", "Product,Category".
        """
        for item in ["Gross Profit", "Product,Category"]:
            metaobj.datatree_field_click(item,2,1)
            utillobj.synchronize_with_visble_text("#queryTreeColumn", item, metaobj.chart_medium_timesleep)
                 
        """
        Step03: Drag "Store Type" to Matrix - Columns.
        Step04: Verify the following chart is displayed.
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        new_metaobj.collapse_data_field_section('Filters and Variables')
        metaobj.drag_drop_data_tree_items_to_query_tree("Store Type", 1, 'Columns', 0)
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
#         xaxis_value="Product Category"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step04:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step 04.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 04.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step 04.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 04.04: Verify first bar color")
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type : Product Category', expected,"Step 04.05: Verify Column header")
                 
        """
        Step05: Drag "Store Type" to the Filter pane.
        Step06: Click "OK" on "Filter for Store Type".
        Step07: Verify "Store Type" filter has been placed into the Filter pane.
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 14)
        metaobj.drag_drop_data_tree_items_to_filter("Store Type", 1)        
        metaobj.create_visualization_filters('alpha')
        metaobj.verify_filter_pane_field('Store Type',1,"Step 07.01: Verify 'Store Type' appears in filter pane")        
         
        """
        Step08: Verify Filter Prompts appears on the canvas (rightmost area) with [All] checkbox checked.
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step 08.01: Verify All checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=False,msg="Step 08.02: Verify Store Front unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=False,msg="Step 08.03: Verify Web unchecked in prompt")
         
        """
        Step09: Enable "Store Front" checkbox.
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=False,msg="Step 09.01: Verify All unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=True,msg="Step 09.02: Verify Store Front checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=False,msg="Step 09.03: Verify Web unchecked in prompt")
         
        """
        Step10: Verify the following chart is displayed.
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
#         xaxis_value="Product Category"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step10:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step 10.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 10.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 10.04: Verify first bar color")
        expected=['Store Front']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type : Product Category', expected,"Step 10.05: Verify Column header")
         
        """
        Step11: Disable "Store Front" checkbox.
        Step12: Verify that [All] checkbox has been selected.
        Step13: Enable "Web" checkbox.
        Step14: Verify the following chart is displayed.
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step 12.01: Verify All checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=False,msg="Step 12.02: Verify Store Front unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=True,msg="Step 12.03: Verify Web checked in prompt")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
#         xaxis_value="Product Category"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step14:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step 14.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0','5M','10M','15M','20M','25M','30M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 14.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 14.04: Verify first bar color")
        expected=['Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type : Product Category', expected,"Step 14.05: Verify Column header")
         
        """
        Step15: Enable "Store Front" checkbox.
        Step16: Verify the following chart is displayed.
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=True,msg="Step 16.01: Verify Store Front checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=True,msg="Step 16.02: Verify Web checked in prompt")
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
#         xaxis_value="Product Category"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step16:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step 16.03: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.04:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step 16.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 16.06: Verify first bar color")
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type : Product Category', expected,"Step 16.07: Verify Column header")
         
        """
        Step17: Drag "Product,Category" to the Filter pane.
        Step18: Click "OK" on "Filter for Product,Category".
        Step19: Verify "Product,Category" filter has been placed into the Filter pane.
        Step20: Verify Filter Prompts appears on the canvas (rightmost area) with [All] checkbox checked.
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 14)
        new_metaobj.collapse_data_field_section('Store')
        new_metaobj.collapse_data_field_section('Measure Groups')
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)        
        parent_css="#avFilterOkBtn"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        metaobj.create_visualization_filters('alpha')
        metaobj.verify_filter_pane_field('Store Type',1,"Step 19.01: Verify 'Store Type' appears in filter pane")        
        metaobj.verify_filter_pane_field('Product,Category',2,"Step 19.02: Verify 'Product,Category' appears in filter pane")        
        parent_css="#resultArea div[id^='BoxLayoutFilterWindow']"
        resultobj.wait_for_property(parent_css, 2)
        propertyobj.select_or_verify_show_prompt_item('2', '[All]',verify=True, verify_type=True,msg="Step 20.01: Verify All checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=True,msg="Step 20.02: Verify Store Front checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=True,msg="Step 20.03: Verify Web checked in prompt")
        
        """
        Step21: Enable "Computers" checkbox.
        Step22: Verify only "Computers" product is displayed.
        """
        propertyobj.select_or_verify_show_prompt_item('2', 'Computers',verify=False,scroll_down=True)
        propertyobj.select_or_verify_show_prompt_item('2', 'Computers',verify=True, verify_type=True,msg="Step 22.01: Verify Computers checked in prompt")
        expected_xval_list=['Computers']
        expected_yval_list=['0','4M','8M','12M','16M','20M','24M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 22.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 22.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 22.04: Verify first bar color")
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type : Product Category', expected,"Step 22.05: Verify Column header")
        
        """
        Step23: Enable "Video Production" checkbox.
        Step24: Verify the following chart is displayed.
        """
        propertyobj.select_or_verify_show_prompt_item('2', 'Video Production',verify=False,scroll_down=True)
        propertyobj.select_or_verify_show_prompt_item('2', 'Video Production',verify=True, verify_type=True,msg="Step 24.01: Verify Video Production checked in prompt")
        expected_xval_list=['Computers','Video Production']
        expected_yval_list=['0','4M','8M','12M','16M','20M','24M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 24.01: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1,4, 'Step 24.02: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 24.03: Verify first bar color")
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type : Product Category', expected,"Step 24.04: Verify Column header")
        
        """
        Step25: Enable "Camcorder" check box.
        Step26: Verify the following chart is displayed.
        """
        propertyobj.select_or_verify_show_prompt_item('2', 'Camcorder',verify=False,scroll_down=True)
        propertyobj.select_or_verify_show_prompt_item('2', 'Camcorder',verify=True, verify_type=True,msg="Step 26.01: Verify Camcorder checked in prompt")
        expected_xval_list=['Camcorder','Computers','Video Production']
        expected_yval_list=['0','5M','10M','15M','20M','25M','30M','35M','40M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 26.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1,6, 'Step 26.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 26.04: Verify first bar color")
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type : Product Category', expected,"Step 26.05: Verify Column header")
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, metaobj.chart_medium_timesleep)
       
        """
        Step27: Click Save as "C2158200" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
                   
        """
        Step28: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()