'''
Created on Mar 31, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227666
Test case Name =  Sort Descending and Ascending
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity, core_utility

class C2227666_TestClass(BaseTestCase):

    def test_C2227666(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227666'
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", resultobj.chart_long_timesleep)

        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, resultobj.chart_long_timesleep)
        
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, resultobj.chart_long_timesleep)
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        Step 05: Click OK
        """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        metaobj.create_visualization_filters("alpha")        
        
        """
        Step 06: Click Prompt menu in the upper right corner
        Step 07: Select "Descending"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, resultobj.chart_long_timesleep)
        propertyobj.change_prompt_options("1","Descending")
        time.sleep(5)        
        
        menu_list_items=['[All]', 'Video Production', 'Televisions', 'Stereo Systems', 'Media Player', 'Computers', 'Camcorder', 'Accessories']
        propertyobj.select_or_verify_show_prompt_item('1', 'Video Production', menu_list=menu_list_items,msg="Step 07.00: Verify prompt menu list")
                
        """
        Step 08: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, resultobj.chart_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08.01 Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 08.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.04: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 08.05: Verify bar value")
        utillobj.synchronize_until_element_disappear("span[id*='tdgchart-tooltip']:not([style*='hidden'])", resultobj.home_page_short_timesleep)
        
        """
        Step 09: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
          
        """
        Step 10: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        utillobj.synchronize_until_element_is_visible(chart_type_css, resultobj.chart_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 10.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.04: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 10.05: Verify bar value")
        
        menu_list_items=['[All]', 'Video Production', 'Televisions', 'Stereo Systems', 'Media Player', 'Computers', 'Camcorder', 'Accessories']
        propertyobj.select_or_verify_show_prompt_item('1', '[All]', menu_list=menu_list_items,msg="Step 10.06: Verify prompt menu list")
                
        """
        Step 11: Close the output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", resultobj.chart_long_timesleep)          
                
        """
        Step12: Click Save in the toolbar > Save as "C2227666" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", resultobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step13: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
          
        """
        Step14: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227666.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
          
        """
        Step15: Verify Canvas
        """
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1", 'Product Category', resultobj.chart_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 15.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 15.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 15.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.04: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 15.05: Verify bar value")
        
        menu_list_items=['[All]', 'Video Production', 'Televisions', 'Stereo Systems', 'Media Player', 'Computers', 'Camcorder', 'Accessories']
        propertyobj.select_or_verify_show_prompt_item('1', '[All]', menu_list=menu_list_items,msg="Step 15.06: Verify prompt menu list")
        
        """
        Step 16: Click Prompt menu in the upper right corner
        Step 17: Select "Ascending"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.chart_long_timesleep)
        propertyobj.change_prompt_options("1","Ascending")
                
        """
        Step 18: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, resultobj.chart_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 18.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 18.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 18.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 18.04: Verify first bar color")
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 18.05: Verify bar value")
        
        menu_list_items=['[All]', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        propertyobj.select_or_verify_show_prompt_item('1', '[All]', menu_list=menu_list_items,msg="Step 18.06: Verify prompt menu list")
                         
        """
        Step 19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()
        