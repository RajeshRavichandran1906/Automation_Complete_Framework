'''
Created on Oct 9, 2017

@author: Bhagavathi

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227648
TestCase Name = Date Filter with decomposed date format YYMD
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2316513_TestClass(BaseTestCase):

    def test_C2316513(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2316513'
        
        """
            Step 01 : Use API call to open chart in Edit mode (edit the URL with domain,port,alias, do not use as is).
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660XX_Chart_Bucket_Test_Suite%2FC2316513.fex
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_1', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        """
            Verification : The default chart bar chart
        """
        parent_css="#pfjTableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("pfjTableChart_1", expected_xval_list, expected_yval_list, 'Step 01:01: X and Y axis labels')
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mbar!", "lochmara", "Step 01:02: Verify first bar color")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 01:03: Verify second bar color")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s2!g0!mbar!", "dark_green", "Step 01:04: Verify third bar color")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s3!g0!mbar!", "pale_yellow_2", "Step 01:05: Verify four bar color")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 01:06: Verify five bar color")
        expected_label_list=['Series0','Series1','Series2','Series3','Series4']
        resultobj.verify_riser_legends('pfjTableChart_1', expected_label_list, 'Step 01:07: Verify pie chart Legends')
        resultobj.verify_number_of_riser("pfjTableChart_1", 1, 25, 'Step 01:08 Verify the total number of risers displayed on live preview Chart')
        """
            Step 02: Expand Product > Model > Attributes
            Step 03 : Right click Price,Dollars > Create Bin
        """
        time.sleep(5)
        metaobj.datatree_field_click("Price,Dollars", 1, 0, "Create Bins...")
        time.sleep(4)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 04: Click Format
            Step 05 : Select Integer, select Use Comma, select Currency Symbol = Floating Currency > OK
            Step 06 : Change bin width to 100 > OK
        """
        metaobj.create_bin("PRICE_DOLLARS_BIN_1", btn_click='OK', bin_format_btn='dummy', field_type='Integer', check_box_list=['Use Comma (C)'], currency_symbol='Floating Currency', ok_btn=True, bin_width='100')
         
        """
            Verification : Step 06:01 : Bin is created in data pane under Dimensions
        """
        metaobj.verify_data_pane_field("Dimensions", "PRICE_DOLLARS_BIN_1", 7, 'Step 06 :01: Bin is created in data pane under dimensions')
        """
            Step 07: Double click the bin to add to Horizontal axis (can't be done yet because of IA-7034, for the time being drag the bin to the horizontal bucket).
        """
        metaobj.datatree_field_click("PRICE_DOLLARS_BIN_1", 2, 1)
        metaobj.verify_query_pane_field('Horizontal Axis', 'PRICE_DOLLARS_BIN_1', 1, "Step 07::01: Verify PRICE_DOLLARS_BIN_1 is visible underneath Horizontal Axis")
          
        """
            Step 08 : Double click Quantity,Sold
        """
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        metaobj.verify_query_pane_field('Vertical Axis', 'Quantity,Sold', 1, "Step 08::01: Verify Quantity,Sold is visible underneath Vertical Axis")
           
        """
            Verification : Step 08:01 : Verify the created chart in preview.  
        """
        time.sleep(5)
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step 8:a(i) Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE_DOLLARS_BIN_1', "Step 8:a(ii) Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 18, 'Step 08a: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        expected_xval_list=['$0', '$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 08b: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c(i) Verify first bar color")
        obj1=driver.find_element_by_css_selector("#TableChart_1")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
                         
        """
            Step 09: Save with name "C2316513" and close IA.
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
          
        """
            Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
            Step 10: Use API to run from tree
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2316513.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_1", 'mrid', 'mrpass')
        time.sleep(6)
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'Quantity Sold', "Step 10:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'PRICE_DOLLARS_BIN_1', "Step 10:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 18, 'Step 10:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        expected_xval_list=['$0', '$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 10:04: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 10:05: Verify first bar color")
        expected_tooltip_list=['PRICE_DOLLARS_BIN_1:$0', 'Quantity Sold:284,474']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", expected_tooltip_list, "Step 10:06: Verify Salary bar value")
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
