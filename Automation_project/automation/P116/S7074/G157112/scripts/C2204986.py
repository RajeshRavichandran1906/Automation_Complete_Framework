'''
Created on JUL 7, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204986
TestCase Name = AHTML:Chart:Months sorted incorrectly with NOPRINT at run time-140819
'''
import unittest, time
from common.lib import utillity
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous

class C2204986_TestClass(BaseTestCase):

    def test_C2204986(self):
            
        """
            CLASS & OBJECTS
        """
        chart_obj = Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)        
        
        """
            Step 01:Launch IA and create a simple chart using WF_RETAIL master file.
            Change the output format to Active Report.
            Add the fields " Sales Month and sales Month Name" found under the Sales Related/Transaction/Sale Month tab to the X-axis and "Revenue" under the Sales Measure to the Y-axis.
        """    
        utillobj.infoassist_api_login('Chart', 'baseapp/wf_retail', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)  
        time.sleep(3)  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        
        """
            Step 02: Select Sales and Car fields    
        """  
        metadataobj.datatree_field_click('Sale,Month', 2, 0)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='SaleMonth', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Sale,Month Name', 2, 0)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='SaleMonth:SaleMonthName', with_regular_exprestion=True)
        time.sleep(1)
        metadataobj.datatree_field_click('Revenue', 2, 0)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Revenue', with_regular_exprestion=True)
        time.sleep(3)
        resobj.verify_yaxis_title("TableChart_1", "Revenue", "Step 02.01: Verify -yAxis Title")
        time.sleep(1)
        resobj.verify_xaxis_title("TableChart_1", "Sale Month : Sale Month Name", "Step 02.02: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['1 : JAN', '2 : FEB', '3 : MAR', '4 : APR', '5 : MAY', '6 : JUN', '7 : JUL', '8 : AUG', '9 : SEP', '10 : OCT', '11 : NOV', '12 : DEC']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.03: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 12, 'Step 02.04: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 02.05 Verify  bar color")
        
        """
            Step 03:Run the report    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        chart_obj.switch_to_frame()
        time.sleep(3)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Revenue", "Step 03.01: Verify -yAxis Title")
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Sale Month : Sale Month Name", "Step 03.02: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['1 : JAN', '2 : FEB', '3 : MAR', '4 : APR', '5 : MAY', '6 : JUN', '7 : JUL', '8 : AUG', '9 : SEP', '10 : OCT', '11 : NOV', '12 : DEC']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.03: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 12, 'Step 03.04: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 03.05 Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue by Sale Month, Sale Month Name', 'Step 03.06: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 04:Right-click on the Field "Sale,Month" and choose Visibility->Hide.
        """
        chart_obj.switch_to_default_content()
        time.sleep(2)
        metadataobj.querytree_field_click("Sale,Month",1,1, 'Visibility','Hide')
        time.sleep(3)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        chart_obj.switch_to_frame()
        time.sleep(3)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Revenue", "Step 04.01: Verify -yAxis Title")
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Sale Month Name", "Step 04.02: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.03: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 12, 'Step 04.04: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 04.05 Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Revenue by Sale Month Name', 'Step 04.06: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        chart_obj.switch_to_default_content()
       
if __name__ == '__main__':
    unittest.main()