'''
Created on July 13, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2317999
TestCase Name = Verify Vertical Waterfall Chart in others tab under Format menu.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_resultarea, ia_ribbon
from common.lib import utillity


class C2317999_TestClass(BaseTestCase):

    def test_C2317999(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2317999"
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """ Step 1: Right click on folder created in IA. 
                    select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        ribbonobj.change_output_format_type('active_report')
        time.sleep(9)
         
        """ Step 2: Add fields Category, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Category', 15)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Unit Sales', 15)
        
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        utillobj.synchronize_with_visble_text(parent_css, 'Dollar Sales', 15)
        
        '''verification check point'''
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 2.1: Verify X-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2.2: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 2.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 2.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar', 'bar_green', 'Step 2.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 2.6: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
         
         
        """ Step 3: Click the Run button.
                    Expect to see the following Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category', "Step 3.1: Verify X-Axis Title")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 6, 'Step 3.3: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!mbar', 'pale_green', 'Step 3.4: Verify Color')
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 3.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 3.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 3.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 3.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
         
         
        """ Step 4: Select Format > Other.
                    From Select a chart pop up choose 
                    'Vertical Waterfall Chart'.
                    Click OK.
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_waterfall_chart', 4, ok_btn_click=True)
        time.sleep(1)
         
        """ Step 5: Expect to see the Clustered bar chart converted into the Preview pane for Vertical Waterfall Chart.
        """
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 5.1: Verify X-Axis Title")
        expected_xval_list=['Coffee', 'Total']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 5.2: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 5.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'dark_cyan', 'Step 5.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g1!mbar', 'desaturated_blue', 'Step 5.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 5.6: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
        css="#TableChart_1 .chartPanel [class*='waterfallProperties-connectorLine!s0!g0']"
        utillobj.verify_object_visible(css, True, 'Step 5.7: Verify  Vertical Waterfall Chart')
        
        
        """ Step 6: Click the Run button.
                    Expect to see the following Vertical Waterfall Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", "Category", 15)
        
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category', "Step 6.1: Verify X-Axis Title")
        expected_xval_list=['Coffee', 'Food', 'Gifts', 'Total']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 6.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 6.3: Verify Number of riser')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 6.4: Verify  Vertical Waterfall Chart', custom_css=".chartPanel [class*='waterfallProperties-connectorLine!']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'dark_cyan', 'Step 6.5: Verify Color')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g3!mbar', 'desaturated_blue', 'Step 6.6: Verify Color')
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category', 'Step 6.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 6.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 6.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 6.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(7)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step6', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()