'''
Created on June 13, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234938
TestCase Name =Verify Horizontal Clustered, Stacked & Percent Bars in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_ribbon
from common.lib import utillity


class C2234938_TestClass(BaseTestCase):

    def test_C2234938(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2234938"
        
        
        """ Step 1: Right click on folder created in IA.
                    Select New > Chart.
                    Select Reporting server as GGSALES.
                    From Home tab Select Active Report as Output file format.
                    Select Format > Other
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='ActiveReport', with_regular_exprestion=True)
        time.sleep(1)
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
               
        
        """ Step 2: From Select a chart pop up choose 'Horizontal Clustered Bar' and click OK
                    Click OK to select.
        """
        ia_ribbonobj.select_other_chart_type('bar', 'horizontal_clustered_bars', 14, ok_btn_click=True)
        time.sleep(1)
        
        
        """ Step 3: Add fields as follows:
                    Category and Product ID under Vertical Axis.
                    Unit Sales and Dollar Sales under Horizontal Axis.
        """
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
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        result_obj.verify_xaxis_title("TableChart_1", 'Category : Product ID', "Step 3.1: Verify X-Axis Title")
        expected_xval_list=['Coffee : C141', 'Coffee : C144']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.3: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 3.4 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 3.6: Verify Color')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 3.5: Verify Number of riser')
        
        
        """ Step 4: Click Run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category : Product ID', "Step 4.1: Verify X-Axis Title")
        expected_xval_list=['Coffee : C141', 'Coffee : C142', 'Coffee : C144', 'Food : F101', 'Food : F102', 'Food : F103', 'Gifts : G100', 'Gifts : G104', 'Gifts : G110', 'Gifts : G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4.2: Verify XY Label')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 4.3: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'bar_blue', 'Step 4.4: Verify Color')
        expected_tooltip_list=['Category:Coffee', 'Product ID:C141', 'Dollar Sales:3906243', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', expected_tooltip_list, 'Step 4.5: verify the default tooltip values', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product ID', 'Step 4.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 4.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 4.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 4.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        
        
        """ Step 5: Back in the Others/Bar Chart menu, select Horizontal Stacked Bar Chart.
                    Click OK. 
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('bar', 'horizontal_stacked_bars', 15, ok_btn_click=True)
        time.sleep(1)
        
        """ Step 6: Click Run.
                    Expect to see the Vertical Stacked Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category : Product ID', "Step 6.1: Verify X-Axis Title")
        expected_xval_list=['Coffee : C141', 'Coffee : C142', 'Coffee : C144', 'Food : F101', 'Food : F102', 'Food : F103', 'Gifts : G100', 'Gifts : G104', 'Gifts : G110', 'Gifts : G121']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 6.2: Verify XY Label')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 2, 10, 'Step 6.3: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'bar_blue', 'Step 6.4: Verify Color')
        expected_tooltip_list=['Category:Coffee', 'Product ID:C141', 'Dollar Sales:3906243', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', expected_tooltip_list, 'Step 6.5: verify the default tooltip values', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product ID', 'Step 6.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 6.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 6.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 6.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        
        
        """ Step 7: Back in the Others/Bar Chart menu, select Horizontal Percentage Bar Chart.
                    Click OK.
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('bar', 'horizontal_percent_bars', 20, ok_btn_click=True)
        time.sleep(1)       
        
        
        """ Step 8: Click Run.
                    Expect to see the Vertical Percent Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category : Product ID', "Step 8.1: Verify X-Axis Title")
        expected_xval_list=['Coffee : C141', 'Coffee : C142', 'Coffee : C144', 'Food : F101', 'Food : F102', 'Food : F103', 'Gifts : G100', 'Gifts : G104', 'Gifts : G110', 'Gifts : G121']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 8.2: Verify XY Label')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 2, 10, 'Step 8.3: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'bar_blue', 'Step 8.4: Verify Color')
        expected_tooltip_list=['Category:Coffee', 'Product ID:C141', 'Dollar Sales:3906243', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', expected_tooltip_list, 'Step 8.5: verify the default tooltip values', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product ID', 'Step 8.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 8.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 8.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 8.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()