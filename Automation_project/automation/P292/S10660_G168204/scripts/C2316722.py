'''
Created on Oct 10, 2017

@author: BM13368
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2316722_TestClass(BaseTestCase):


    def test_C2316722(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID1 = 'C2316513'
        Test_Case_ID = 'C2316722'
        """
            Step 01 :Launch the IA API with wf_retail_lite, Visualization mode:
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_edit(Test_Case_ID1, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        """
            Verification : Verify live-preview chart
        """
        time.sleep(5)
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 1:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE_DOLLARS_BIN_1', "Step 1:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 18, 'Step 1:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        expected_xval_list=['$0', '$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 1:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 1:05: Verify first bar color")
        """
            Step 02: Right click Bin in data pane > Edit Bins...
        """
        metaobj.datatree_field_click("PRICE_DOLLARS_BIN_1", 1, 0, "Edit Bins...")
        time.sleep(4)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1)
         
        """
            Step 03 : Change Field name to Price > OK
        """
        metaobj.create_bin('PRICE_DOLLARS_BIN_1', 'OK', bin_name='PRICE')
        metaobj.verify_data_pane_field("Dimensions", "PRICE", 7, 'Step 03 :01: Verify PRICE Bin is created in data pane under dimensions')
         
        """
            Verification : Verify the changes after changed the FIELD ANAME
        """
        time.sleep(5)
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 3:01 Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE', "Step 3:02 : Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 18, 'Step 3:03 : Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        expected_xval_list=['$0', '$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 3:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 03:05: Verify first bar color")
        first_barobj=self.driver.find_element_by_css_selector("#TableChart_1 rect[class*='riser!s0!g0!mbar']")
        bar_width_before=first_barobj.get_attribute('width')
        """
            Step 04 : Right click the bin in the query pane > Edit Bins...
        """
        metaobj.querytree_field_click("PRICE", 1, 1, "Edit Bins...")
        time.sleep(4)
        """
            Step 05 : Change bin width to 150 > OK
        """
        metaobj.create_bin('PRICE', 'OK', bin_width='150')
        time.sleep(5)
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 5:01 Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE', "Step 5:02 : Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 15, 'Step 5:03 : Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        expected_xval_list=['$0', '$150', '$300', '$450', '$600', '$750', '$900', '$1,050', '$1,200', '$1,350', '$1,950', '$2,100', '$3,300', '$3,450', '$3,900']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 5:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 5:05: Verify first bar color")
        first_barobj=self.driver.find_element_by_css_selector("#TableChart_1 rect[class*='riser!s0!g0!mbar']")
        bar_width_after=first_barobj.get_attribute("width")
        verify_bin_width=float(bar_width_after)-float(bar_width_before)
        if verify_bin_width >= 5:
            utillobj.asequal(True, True, 'Step 05:06 : Bar width is expanded to 150')
        else:
            utillobj.asequal(False, True, 'Step 05:06 : Bar width is not expanded to 100')
        obj1=driver.find_element_by_css_selector("#TableChart_1")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
           
        """
            Step 06 : Save and exit.
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == "__main__":
    unittest.main()