'''
Created on July 03, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204917
TestCase Name =Verify that Changed titles on axis labels are reflected in output
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity

class C2204917_TestClass(BaseTestCase):

    def test_C2204917(self):
       
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID="C2204917"
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01 : Open IA and create a new chart using the GGSALES file.
            Select Active Report as the output type.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series 0', expire_time=20)
        ribbonobj.change_output_format_type('active_report')
        utillobj.synchronize_with_visble_text("#HomeFormatType", 'ActiveReport', expire_time=5)
        
        """
            Add Unit Sales to the Vertical axis.
            Add Product ID to the Horizontal axis.
        """
        metadataobj.datatree_field_click('Product ID', 1, 1, 'Add To Query', 'Horizontal Axis')
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'ProductID', expire_time=5)
        
        metadataobj.datatree_field_click('Unit Sales', 1, 1,'Add To Query','Vertical Axis')
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=5)
        
        """
            Expect to see the following Active Bar Preview pane.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Product ID', "Step 01.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 01.2 : Verify Y-Axis Title")
        expected_xval_list=['C141','C144']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.3 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 01.4 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.5 : Verify bar color")
        
        """
            Step 02 : Click the Run button.
            Expect to see the following default Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=10)
       
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product ID", "Step 02.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 02.2 : Verify Y-Axis Title")
        expected_xval_list=['C141','C142','C144','F101','F102','F103','G100','G104','G110','G121']
        expected_yval_list=['0', '200K', '400K', '600K', '800K','1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 02.4 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'bar_blue', 'Step 02.5 : Verify bar Color')
        expected_tooltip_list=['Product ID:C142', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 02.6 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product ID', 'Step 02.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        utillobj.switch_to_default_content(pause=1)
        
        
        """
            Step 03 : Right click on any bar and select Data labels, then Show.
        """
        result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=5)
        obj_locator=self.driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        utillobj.select_or_verify_bipop_menu('Data Labels')
        utillobj.select_or_verify_bipop_menu('Show')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='dataLabels!s0!g0!mdataLabels!']", '294K', expire_time=5)
        
        """
            Expect to see the following Preview pane with Data labels above each bar.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Product ID', "Step 03.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 03.2 : Verify Y-Axis Title")
        expected_xval_list=['C141','C144']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.3 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 03.4 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.5 : Verify bar color")
        result_obj.verify_data_labels("TableChart_1",['294K','189K'],'Step 03.6 : Verify expect to see the following Preview pane with Data labels above each bar',custom_css=".chartPanel .groupPanel text[class^='dataLabels']")
        
        """
            Step 04 : Click the Run button.
            Expect to see the following Bar Chart, now displaying the summed value of Unit Sales for each Product ID, above the bars.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=10)

        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product ID", "Step 04.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 04.2 : Verify Y-Axis Title")
        expected_xval_list=['C141','C142','C144','F101','F102','F103','G100','G104','G110','G121']
        expected_yval_list=['0', '200K', '400K', '600K', '800K','1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 04.4 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'bar_blue', 'Step 04.5 : Verify bar Color')
        expected_tooltip_list=['Product ID:C142', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 04.6 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product ID', 'Step 04.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True) 
        result_obj.verify_data_labels("MAINTABLE_wbody0",['309K','878K','189K','333K','421K','630K','361K','190K','187K','191K'],'Step 03.6 : Verify Expect to see the following Bar Chart, now displaying the summed value of Unit Sales for each Product ID, above the bars',custom_css=".chartPanel .groupPanel text[class^='dataLabels']")       
        utillobj.switch_to_default_content(pause=1)
      
        """
            Step 05 : Right click on any bar and select Data labels, then Hide.
        """
        result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=5)
        obj_locator=self.driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        utillobj.select_or_verify_bipop_menu('Data Labels')
        utillobj.select_or_verify_bipop_menu('Hide')
        utillobj.synchronize_until_element_disappear("#TableChart_1 text[class^='dataLabels']", 15)
        
        """
            Expect to see the following Preview pane, now with data labels removed.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Product ID', "Step 05.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 05.2 : Verify Y-Axis Title")
        expected_xval_list=['C141','C144']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05.3 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 05.4 : Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 05.5 : Verify bar color")
        data_labels=len(self.driver.find_elements_by_css_selector("#TableChart_1 .chartPanel .groupPanel text[class^='dataLabels']"))
        utillobj.asequal(0,data_labels,'Step 05.6 : Verify expect to see the following Preview pane, now with data labels removed') 
        
        """
            Step 06 : Click the Run Button.
            Expect to see the data labels removed and the default bars re-displayed.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=10)
    
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product ID", "Step 06.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 06.2 : Verify Y-Axis Title")
        expected_xval_list=['C141','C142','C144','F101','F102','F103','G100','G104','G110','G121']
        expected_yval_list=['0', '200K', '400K', '600K', '800K','1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 06.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 06.4 : Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", 'bar_blue', 'Step 06.5 : Verify bar Color')
        expected_tooltip_list=['Product ID:C142', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 06.6 : verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product ID', 'Step 06.7 : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True) 
        data_labels=len(self.driver.find_elements_by_css_selector("#MAINTABLE_wbody0 .chartPanel .groupPanel text[class^='dataLabels']"))
        utillobj.asequal(0,data_labels,'Step 06.11 : Verify expect to see the data labels removed and the default bars re-displayed.')        
        utillobj.switch_to_default_content(pause=1)
       
        """
            Save Report      
        """
        ele=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204917_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
      
if __name__ == '__main__':
    unittest.main()  