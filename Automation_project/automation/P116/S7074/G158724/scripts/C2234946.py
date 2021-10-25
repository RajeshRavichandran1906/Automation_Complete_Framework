'''
Created on JUN 15, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234946
TestCase Name = Verify Scatter in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous, ia_resultarea,ia_ribbon
from common.lib import utillity


class C2234946_TestClass(BaseTestCase):

    def test_C2234946(self):
        Test_Case_ID="C2234946"
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
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES
        """  
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(4)  
        """
            Step 02: From Home tab Select Active Report as Output file format.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        """
            Step 02: From Home tab Select Active Report as Output file format.
        """
        ribbonobj.select_ribbon_item('Home', 'Records', opt = 'All', custom_css="div[id^='BiList']>div")
        time.sleep(5)
        
        """
            Step 03:Select X Y Plots > XY Scatter chart type and click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('x_y_plots', 'x_y_plots_buttons', 1, ok_btn_click=True)
        time.sleep(2)
        """
            Step 04:Add fields as follows: Category under Horizontal Axis, Unit Sales under Vertical Axis,Product under Color.
        """
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales',2, 0)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product', 1, 0, 'Add To Query', 'Color')
        parent_css="#TableChart_1 g.legend g text[class='legend-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        time.sleep(2)
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 04.1: Verify -yAxis Title")
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 04.2: Verify -xAxis Title")
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 04.3: Verify lablesList')
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 04.4: Verify XY labels")
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mmarker!', 'bar_blue1', 'Step 04.5:  Verify Color',attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 10, 'Step 04.6: Expect to see the Series Selection set to Scatter.', custom_css="g [class*= 'marker'] circle")
        
        """
            Step 05:Click run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.1: Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 05.2: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05.3: Verify XY labels")
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05.4: Verify lablesList')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mmarker!', 'bar_blue', 'Step 05.5: Verify Color',attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 05.6 Verify number of Scatter")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Product, Category', 'Step 05.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:189217', 'Product:Capuccino', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mmarker", expected_tooltip_list, "Step 05: Verify bar value")
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
