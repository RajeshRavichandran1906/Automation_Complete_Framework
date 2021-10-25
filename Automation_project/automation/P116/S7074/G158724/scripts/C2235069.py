'''
Created on Jul 27, 2017
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235069
TestCase Name = Verify Pie With Depth via Advance chart tool bar
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea, active_miscelaneous, ia_ribbon, active_chart_rollup
from common.lib import utillity

class C2235069_TestClass(BaseTestCase):

    def test_C2235069(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        rollup_obj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        Test_Case_ID="C2235069"
        
        
        """    1. Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES. Set the output type as Active Report    """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='ActiveReport', with_regular_exprestion=True)
        time.sleep(1)
        
        """    2. Add fields Category, Product ID under the Horizontal axis. Add Unit Sales, Dollar Sales under the Vertical axis.    """
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product ID', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category:ProductID', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend g text[class='legend-labels!s1!']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        
        result_obj.verify_xaxis_title("TableChart_1", "Category : Product ID", "Step 02a: Verify X-Axis Title")
        expected_xval_list=['Coffee : C141', 'Coffee : C144']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02b: Verify XY labels")
        result_obj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 02c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02d: Verify First bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 02e: Verify Second bar color")
        
        expected_xval_list=['Coffee : C141', 'Coffee : C142', 'Coffee : C144', 'Food : F101', 'Food : F102', 'Food : F103', 'Gifts : G100', 'Gifts : G104', 'Gifts : G110', 'Gifts : G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        legend=["Unit Sales", "Dollar Sales"]
        column_values=['Coffee', 'Food', 'Gifts']
        oActiveChart_toolbar=['More Options','Advanced Chart','Original Chart']
        oAggr=['Aggregation']
        expected_tooltip_list=['Category:Gifts', 'Product ID:G100', 'Dollar Sales:4522521', 'Filter Chart', 'Exclude from Chart']
        """    3. Click the Run button.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", "Category : Product ID", "Step 03a: Verify X-Axis Title")
        time.sleep(2)
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03b: Verify XY labels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 03c: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!", "bar_blue", "Step 03d: Verify First Series bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 03e: Verify Second Series bar color")
        result_obj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03f: Verify Y-Axis Title")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product ID', 'Step 03g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', oActiveChart_toolbar,"Step 03h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', oAggr,"Step 03i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!", expected_tooltip_list, "Step 03k: Verify bar value")
        
        """    4. Select the Advanced Chart icon from the tool bar. Scroll down to the PIE selections. Select PIE with Depth    """
        """    5. Click the OK button for the PIE with Depth selection.    """
        rollup_obj.click_pivot_menu_bar_items('MAINTABLE_wmenu0', 1)
        rollup_obj.select_advance_chart('wall1', 'piewithdepth')
        time.sleep(5)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, 'Step 05a: Expect to see the six PIE Chart Visible.', custom_css=".chartPanel path[class$='mwedge!r0!c0!']")
        expected_label_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05b: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!r0!c0!', 'dark_green', 'Step 05c(1): Verify any one pie color from first pie chart.')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g1!mwedge!r0!c0!', 'pale_green', 'Step 05c(2): Verify any one pie color from second pie chart.')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s4!g0!mwedge!r0!c1!', 'brick_red', 'Step 05c(3): Verify any one pie color from third pie chart.')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s3!g1!mwedge!r0!c1!', 'pale_yellow', 'Step 05c(4): Verify any one pie color from fourth pie chart.')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s8!g0!mwedge!r0!c2!', 'moss_green', 'Step 05c(5): Verify any one pie color from fifth pie chart.')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s6!g1!mwedge!r0!c2!', 'periwinkle_gray', 'Step 05c(6): Verify any one pie color from sixth pie chart.')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product ID', 'Step 05d: Verify pie Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05e: Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05f: Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05g: Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales', 'Dollar Sales', 'Unit Sales', 'Dollar Sales', 'Unit Sales', 'Dollar Sales'],"'Step 05h: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', column_values, "Step 05i: Verify row header and value")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=5)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)        
        
if __name__ == '__main__':
    unittest.main()