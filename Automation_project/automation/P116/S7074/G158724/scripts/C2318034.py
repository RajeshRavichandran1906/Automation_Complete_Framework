'''
Created on JUL 28, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2318034
TestCase Name = Verify Gauge Chart in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,ia_ribbon
from common.lib import utillity


class C2318034_TestClass(BaseTestCase):

    def test_C2318034(self):
        
        Test_Case_ID="C2318034"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        """
            Step 01:Right click on folder created in IA and create a new Chart using the GGSALES file.From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 290)
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 290)
        
        """
            Step 02:Add fields Category to the Horizontal axis. Add Unit Sales to the Vertical axis.
        """
        metadataobj.datatree_field_click('Category', 2, 0)
        parent_css="#TableChart_1 g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Category', 290)
        metadataobj.datatree_field_click('Unit Sales',2, 0)
        parent_css="#TableChart_1 g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'UnitSales', 290)
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 02.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 02.2: Verify -yAxis Title")
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", ["Coffee"], expected_yval_list, "Step 02.3: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 1, 'Step 02.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 04.5: Verify  bar color")
        """
            Step 03:Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 03.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 03.2: Verify -yAxis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 3, 'Step 03.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 03.5: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category', 'Step 03.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 03.10: Verify bar value")
        
        """
            Step 04:Select Format > Other. Select the Special tab series. From Select a chart pop up choose 
                    Gauge Chart. Click OK.
        """
        time.sleep(5)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('special', 'gauge', 1, ok_btn_click=True)
        time.sleep(2)
        resobj.verify_data_labels('TableChart_1',['482761'],'Step 04.1: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        resobj.verify_data_labels('TableChart_1',['Coffee'],'Step 04.2: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
        labels=['0','100K','200K','300K','400K','500K','600K','627.6K']
        resobj.verify_data_labels('TableChart_1',labels,'Step 04.3: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 5, "Step 04.4: verify the Gauge", custom_css=".chartPanel path[class*='gaugeRange']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, "Step 04.4: verify the needle", custom_css=".chartPanel path[class*='needle']")
        utillobj.verify_chart_color('TableChart_1',None, 'green', 'Step 04.5: Verify Gauge color',custom_css=".chartPanel path[class='gaugeRange'][fill*='rgb(0,'][fill*='128,'][fill*='0)']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mneedle", "bar_blue1", "Step 04.6: Verify needle color")
        """
            Step 05:Click the Run button.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mneedle", "bar_blue", "Step 05.1: Verify  bar color")
        utillobj.verify_chart_color('MAINTABLE_wbody0',None, 'green', 'Step 05.2: Verify Gauge color',custom_css=".chartPanel path[class='gaugeRange'][fill*='rgb(0,'][fill*='128,'][fill*='0)']")
        totalLabel=['1376266', '1384845','927880']
        resobj.verify_data_labels('MAINTABLE_wbody0',totalLabel,'Step 05.3: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        groupLabel=['Coffee', 'Food','Gifts']
        resobj.verify_data_labels('MAINTABLE_wbody0',groupLabel,'Step 05.4: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
        gaugelabels=['0','0.4M','0.8M','1.2M','1.6M','1.8M','0','0.4M','0.8M','1.2M','1.6M','1.8M','0','0.4M','0.8M','1.2M','1.6M','1.8M']
        resobj.verify_data_labels('MAINTABLE_wbody0',gaugelabels,'Step 04.1: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 15, "Step 04.2: verify the Gaugerange", custom_css=".chartPanel path[class*='gaugeRange']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, "Step 04.2: verify the needle", custom_css=".chartPanel path[class*='needle']")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category', 'Step 05.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()