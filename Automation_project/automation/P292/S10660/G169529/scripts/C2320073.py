'''
Created on Oct 17, 2017

@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon, metadata

class C2320073_TestClass(BaseTestCase):


    def test_C2320073(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID='C2320073'
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        metaobj1=metadata.MetaData(self.driver)
        
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=baseapp/wf_retail
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02 : Right click Revenue > Create Bins
        """
        metaobj.datatree_field_click("Revenue", 1, 0, "Create Bins...")
        time.sleep(4)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        """
            Step 03 : Change bin width to 100, change format to integer 9 with comma (I9C) > OK
        """
        metaobj.create_bin("REVENUE_US_BIN_1", btn_click='OK', bin_format_edit='I9C', bin_width='100')
        time.sleep(4)
        metaobj1.collapse_data_field_section("Measure Groups")
        time.sleep(3)
        metaobj.verify_data_pane_field("Dimensions", "REVENUE_US_BIN_1", 7, 'Step 03 :01: ')
        """
            Step 04 : Format > Chart Type > Other > Bar > Vertical Histogram > OK
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_histogram', 6, ok_btn_click=True)
        time.sleep(4)
        
        """
            Step 05 : Double click Revenue
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(5)
        
        metaobj.verify_query_pane_field('Measure', 'CNT.Revenue', 1, "Step 05::01: ")
        metaobj.verify_query_pane_field('Measure', 'REVENUE_US_BIN_2', 2, "Step 05::02: ")
        metaobj1.collapse_data_field_section("Measure Groups")
        time.sleep(3)
        metaobj.verify_data_pane_field('Dimensions', 'REVENUE_US_BIN_2', 8, "Step 05:03:")
        
        """
            Step 06: Drag REVENUE_US_BIN_1 from data pane over the REVENUE_US_BIN_2 in the query
        """
        
        metaobj.drag_drop_data_tree_items_to_query_tree("Dimensions->REVENUE_US_BIN_1", 1,'CNT.Revenue', 0)
        parent_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, "REVENUE_US_BIN_1", 30)
        metaobj.verify_query_pane_field('CNT.Revenue', 'REVENUE_US_BIN_1', 1, "Step 06::01: ")
        metaobj.verify_query_pane_field_available('Marker', 'REVENUE_US_BIN_2', 'Tooltip', "Step 06:02 ", availability=False)
        
        """
            Verification : Verify the preview chart
        """
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        expected_xval_list=['0', '100', '200', '300', '400', '500', '600','700','800']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 06:04: X and Y axis labels',x_axis_label_length=1)
        
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 06:05: Verify first bar color")
        resultobj.verify_number_of_riser("TableChart_1", 1, 85, 'Step 06:06 Verify the total number of risers displayed on live preview Chart')
        resultobj.verify_xaxis_title("TableChart_1", 'REVENUE_US_BIN_1', "Step 06:07 : Verify live preview x-axis title")
        resultobj.verify_yaxis_title("TableChart_1",'CNT Revenue', "Step 06:08 : Verify live preview y-axis title")
        
        obj1=driver.find_element_by_css_selector("#TableChart_1")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step06', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        
        """"
            Step 07 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        

if __name__ == "__main__":
    unittest.main()