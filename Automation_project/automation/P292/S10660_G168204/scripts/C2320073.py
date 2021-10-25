'''
Created on Oct 17, 2017

@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon, ia_resultarea
from selenium.webdriver.common.by import By


class C2320073_TestClass(BaseTestCase):


    def test_C2320073(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID='C2320073'
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01 : Invoke IA Chart tool with wf_retail
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_2', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
            Step 02 : Right click Revenue > Create Bins
        """
        time.sleep(5)
        metaobj.datatree_field_click("Revenue", 1, 0, "Create Bins...")
        time.sleep(4)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1)
        
        
        """
            Step 03 : Change bin width to 100, change format to integer 9 with comma (I9C) > OK
        """
        metaobj.create_bin("REVENUE_US_BIN_1", btn_click='OK', bin_format_edit='I9C', bin_width='100')
        metaobj.verify_data_pane_field("Dimensions", "REVENUE_US_BIN_1", 7, 'Step 03 :01: ')
        """
            Step 04 : Format > Chart Type > Other > Bar > Vertical Histogram > OK
        """
        time.sleep(4)
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_histogram', 6, ok_btn_click=True)
        
        """
            Step 05 : Double click Revenue
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        metaobj.verify_query_pane_field('Measure', 'CNT.Revenue', 1, "Step 05::01: ")
        metaobj.verify_query_pane_field('Measure', 'REVENUE_US_BIN_2', 2, "Step 05::02: ")
        metaobj.verify_data_pane_field('Dimensions', 'REVENUE_US_BIN_2', 8, "Step 05:03:")
        
        """
            Step 06: Drag REVENUE_US_BIN_1 from data pane over the REVENUE_US_BIN_2 in the query
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("REVENUE_US_BIN_1", 0,'CNT.Revenue', 0)
        time.sleep(15)
        metaobj.verify_query_pane_field('CNT.Revenue', 'REVENUE_US_BIN_1', 1, "Step 06::01: ")
        metaobj.verify_query_pane_field_available('Marker', 'REVENUE_US_BIN_2', 'Tooltip', "Step 06:02 ", availability=False)
        
        """
            Verification : Verify the preview chart
        """
        parent_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        resultobj.wait_for_property(parent_css, 1)
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        expected_xval_list=['0', '100', '200', '300', '400', '500', '600', '700', '800', '900', '1,000', '1,100', '1,200', '1,300', '1,400', '1,500', '1,600', '1,700', '1,800', '1,900', '2,000', '2,100', '2,200', '2,300', '2,400', '2,500', '2,600', '2,700', '2,800', '2,900', '3,000', '3,100', '3,200', '3,300', '3,400', '3,500', '3,700', '3,800', '3,900', '4,000', '4,100', '4,200', '4,400', '4,600', '4,700', '4,800', '5,000', '5,100', '5,200', '5,300', '5,400', '5,500', '5,700', '5,900', '6,000', '6,100', '6,200', '6,300', '6,700', '6,900', '7,100', '7,300', '7,600', '7,800', '7,900', '8,000', '8,100', '8,300', '8,600', '8,900', '9,100', '9,400', '9,500', '9,700', '10,100', '10,400', '10,700', '11,100', '11,500', '11,900', '12,200', '13,500', '13,900', '14,300', '15,900']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 06:04: X and Y axis labels', x_axis_label_length=1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 06:05: Verify first bar color")
        resultobj.verify_number_of_riser("TableChart_1", 1, 85, 'Step 06:06 Verify the total number of risers displayed on live preview Chart')
        resultobj.verify_xaxis_title("TableChart_1", 'REVENUE_US_BIN_1', "Step 06:07 : Verify live preview x-axis title")
        resultobj.verify_yaxis_title("TableChart_1",'CNT Revenue', "Step 06:08 : Verify live preview y-axis title")
        obj1=driver.find_element_by_css_selector("#TableChart_1")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step06', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        
        """"
            Step 07 : Close IA without saving.
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(3)
        ia_resultarea_obj.ia_exit_save("No")
        time.sleep(1)
        utillobj.infoassist_api_logout()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()