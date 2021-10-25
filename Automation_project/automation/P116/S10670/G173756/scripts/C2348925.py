'''
Created on Nov 23, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2348925
TestCase Name = Verify Vertical Histogram in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon
from common.lib import utillity

class C2348925_TestClass(BaseTestCase):

    def test_C2348925(self):
        
        Test_Case_ID="C2348925"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        time_out=30

        """
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S10670', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.1: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 01.2: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 01.3: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 01.4: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar", "med_green", "Step 01.5: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar", "pale_yellow_2", "Step 01.6: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar", "brick_red", "Step 01.7: Verify  bar color")
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.8: Verify Y-Axis legend")  

        """
            Step 02:Add fields Category and Unit Sales
        """
        metadataobj.datatree_field_click('Category', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Category', expire_time=time_out)
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='UnitSales', expire_time=time_out)
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 02.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 02.2: Verify -xAxis Title")
        expected_xval_list=['Coffee']
        expected_yval1_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.3: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 1, 'Step 02.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 02.4: Verify  bar color")

        """
            Step 03:Select Format > Other
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Selectachart', expire_time=time_out)
        
        """
            Step 04:From Select a chart pop up choose 'Vertical Histogram Bar'
                    Click ok
        """
        ia_ribbobj.select_other_chart_type('bar', 'vertical_histogram', 6, ok_btn_click=True)
        time.sleep(8)
        
        """
            Step 05: Expected to see the chart 
        """
        resobj.verify_xaxis_title("TableChart_1", "UNITS_BIN_1", "Step 05.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("TableChart_1", "CNT Unit Sales", "Step 05.2: Verify -xAxis Title")
        expected_datalabel1=['0', '4', '8', '12', '16']
        resobj.verify_data_labels("TableChart_1", expected_datalabel1, "Step 05.4: verify x label", custom_css="svg > g text[class^='yaxis-labels']" )
        resobj.verify_number_of_riser("TableChart_1", 1, 162, 'Step 05.5: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 05.6: Verify  bar color")

        """
            Step 06:Verify output.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "UNITS_BIN_1", "Step 06.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "CNT Unit Sales", "Step 06.2: Verify -xAxis Title")
        expected_datalabel1=['0', '10', '20', '30', '40', '50']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel1, "Step 06.3: verify x label", custom_css="svg > g text[class^='yaxis-labels']" )
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 179, 'Step 06.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 06.5: Verify  bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'CNT Unit Sales by UNITS_BIN_1', 'Step 06.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Count'],"Step 06.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['UNITS_BIN_1:100', 'CNT Unit Sales:38', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 06.10: Verify tooltip ")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_6', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        utillobj.infoassist_api_logout()  
        time.sleep(5) 
         
if __name__ == '__main__':
    unittest.main()