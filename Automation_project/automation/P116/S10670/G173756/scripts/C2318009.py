'''
Created on May 25, 2018

@author: BM13368
TestCase_Name  : Verify Horizontal Histogram in others tab under Format menu.
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2318009
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon
from common.lib import utillity

class C2318009_TestClass(BaseTestCase):

    def test_C2318009(self):
        
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
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01:Right click on folder created in IA. 
            Sselect New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P292/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        ribbonobj.switch_ia_tab("Home")
        ia_ribbobj.select_or_verify_output_type(launch_point='Home', item_select_path='Active Report')
        
        """
            Step 02:Add fields Product, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title']", "Product", 15)
        
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", "Unit Sales", 15)
        
        metadataobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='legend-labels!s1!']", "Dollar Sales", 15)
        time.sleep(3)
        
        """
        Verify preview chart 
        """
        resobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 02:01: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02:02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 02:03: Verify bar color")
        xaxis_value="Product"
        resobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:04: Verify X-Axis Title")
        resobj.verify_legends(['Unit Sales','Dollar Sales'], "#TableChart_1", msg="Step 02:05:Verify bar chart legends")
        
        """
            Step 03:Click the Run button.
            Expect to see the following Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 3:02: Verify -xAxis Title")
        
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03:03 Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 03:04: Verify the total number of risers displayed on preview')
        
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 03:05: Verify  bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Product', 'Step 03:06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03:07: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03:08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03:09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=2)
        
        """
            Step 04:Select Format > Other.
            From Select a chart pop up choose 
            'Horizontal Histogram'.
            Click OK.
            Expect to see the Clustered bar chart converted into the Preview pane for Horizontal Histogram.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'horizontal_histogram', 21, ok_btn_click=True)
        
        """
        Verify preview chart
        """
        resobj.verify_number_of_riser("TableChart_1", 1, 162, 'Step 04:01: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['100', '110', '120', '130', '140', '150', '160', '170', '180']
        expected_yval_list=['0', '4', '8', '12', '16']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04:02: X annd Y axis Scales Values has changed or NOT',x_axis_label_length=3)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 04:03: Verify bar color")
        yaxis_value="CNT Unit Sales"
        xaxis_value="UNITS_BIN_1"
        resobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 04:04: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 04:04: Verify X-Axis Title")
         
        """ 
            Step 05:Click the Run button.
            Expect to see the following Horizontal Histogram Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)

        expected_yval_list=['0', '10', '20', '30', '40', '50']
        expected_xval_list=['60','70','80','90','100', '110', '120', '130', '140', '150', '160', '170', '180']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05:01 Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 179, 'Step 05:02: Verify the total number of risers displayed on preview')
        yaxis_value="CNT Unit Sales"
        xaxis_value="UNITS_BIN_1"
        resobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 05:03: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 05:04: Verify X-Axis Title")
        
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 05:05: Verify  bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'CNT Unit Sales BY UNITS_BIN_1', 'Step 05:06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05:07: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05:08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Count'],"Step 05:09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
if __name__ == "__main__":
    unittest.main()