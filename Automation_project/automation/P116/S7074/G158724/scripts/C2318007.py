'''
Created on July 17, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2318007
TestCase Name = Verify Horizontal Stacked Bars in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_resultarea, ia_ribbon
from common.lib import utillity


class C2318007_TestClass(BaseTestCase):

    def test_C2318007(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2318007"
        
         
        """ Step 1: Right click on folder created in IA. 
                    select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(9)
         
        """ Step 2: Add fields Product, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click('Product', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class$='title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        '''verification check point'''
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 2.1: Verify X-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2.2: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 2.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 2.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar', 'bar_green', 'Step 2.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 2.6: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
         
         
        """ Step 3: Click the Run button.
                    Expect to see the following Horizontal Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 3: Verify X-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, 'Step 3.3: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'lochmara', 'Step 3.4: Verify Color')
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar', expected_tooltip_list, 'Step 3.5: verify the default tooltip values')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 3.6: Verify Legends ')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Product', 'Step 3.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 3.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 3.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 3.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
         
         
        """ Step 4: Select Format > Other.
                    From Select a chart pop up choose 
                    'Horizontal Stacked Bars'.
                    Click OK.
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('bar', 'horizontal_stacked_bars', 15, ok_btn_click=True)
        time.sleep(1)
        parent_css="#TableChart_1 g.chartPanel text[class$='title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        
         
        """ Step 5: EExpect to see the Clustered bar chart converted into the Preview pane for Horizontal Stacked Bars.
        """
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 5.1: Verify X-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 5.2: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 5.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 5.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar', 'bar_green', 'Step 5.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 5.6: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
        
        
        """ Step 6: Click the Run button.
                    Expect to see the following Horizontal Stacked Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 6.1: Verify X-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 6.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, 'Step 6.3: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'lochmara', 'Step 6.4: Verify Color')
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar', expected_tooltip_list, 'Step 6.5: verify the default tooltip values')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 6.6: Verify Legends ')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Product', 'Step 6.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 6.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 6.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 6.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(7)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step6', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()