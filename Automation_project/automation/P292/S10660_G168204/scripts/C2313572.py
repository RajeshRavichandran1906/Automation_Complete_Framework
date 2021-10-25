'''
Created on Oct 31, 2017

@author: BM13368
Testcase_ID: http://172.19.2.180/testrail/index.php?/cases/view/2313572
Testcase_Name : Edit format of measure for tooltip 

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2313572_TestClass(BaseTestCase):

    def test_C2313572(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2313572'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        
        """
            Step 01 : Invoke IA Chart tool with wf_retail_lite
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_2', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 02 : Double click Product,Category, Discount & Quantity,Sold
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        metaobj.datatree_field_click("Discount", 2, 1)
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        """
            Step 03 : Right click Discount > Edit Format
        """
        metaobj.querytree_field_click('Discount', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Edit Format')
        time.sleep(2)
        parent_css="div[id^='QbDialog'] div[class*='bi-window active window']"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 04 : Change Currency Symbol to None
        """
        metaobj.set_bin_format(currency_symbol='None')
        """
            Step 05 : Check Suppress Comma > OK 
        """
        metaobj.set_bin_format(check_box_list=['Suppress Comma (c)'], ok_btn=True)
        time.sleep(1)
        
        """
            Step 06 : Right click Quantity,Sold > Edit Format
        """
        metaobj.querytree_field_click('Quantity,Sold', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Edit Format')
        time.sleep(2)
        parent_css="div[id^='QbDialog'] div[class*='bi-window active window']"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 07 : Change Field Type to Decimal
        """
        metaobj.set_bin_format(field_type='Decimal')
        
        """
            Step 08 : Change Currency Symbol to Floating Currency (M) > OK
        """
        metaobj.set_bin_format(currency_symbol='Floating Currency', ok_btn=True)
        """
            Step 09 : Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 09:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 09:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "pale_green", "Step 09:03: Verify second bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['Discount', 'Quantity Sold'], 'Step 09.04 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 14, 'Step 09.05: Verify Number of bar chart')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 09:06: Verify X-Axis Title")
        time.sleep(1)
        
        """
            Step 10 : Hover over Discount riser
            Discount displays without commas and without dollar sign
        """
        expected_tooltip_list=['Product Category:Media Player', 'Discount:11519142.41']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g3!mbar!", expected_tooltip_list, "Step 10:01 Hover over Discount riser and verify Discount displays without commas and without dollar sign")
        time.sleep(1)
        """
            Step 11 : Hover over Quantity,Sold riser
        """
        expected_tooltip_list=['Product Category:Media Player', 'Quantity Sold:$771,934.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g3!mbar!", expected_tooltip_list, "Step 10:02 Hover over Quantity,Sold riser and verify Quantity,Sold displays with dollar sign and 2 decimal points")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        """
            Step 12: Save with name C2313572 and close
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        """
            Step 13: Use API to run from tree
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2313572.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        parent_css=("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 13:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 13:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "pale_green", "Step 13:03: Verify second bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['Discount', 'Quantity Sold'], 'Step 13.04 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 14, 'Step 13.05: Verify Number of bar chart')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 13:06: Verify X-Axis Title")
        
        """
            Step 14 : Hover over risers
            Format matches expected results in steps 10 and 11
        """
        expected_tooltip_list=['Product Category:Media Player', 'Discount:11519142.41']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g3!mbar!", expected_tooltip_list, "Step 14:00 Hover over Discount riser and verify Discount displays without commas and without dollar sign")
        """
            Step 14:01 : Hover over Quantity,Sold riser
        """
        expected_tooltip_list=['Product Category:Media Player', 'Quantity Sold:$771,934.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g3!mbar!", expected_tooltip_list, "Step 14:01 Hover over Quantity,Sold riser and verify Quantity,Sold displays with dollar sign and 2 decimal points")
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        
    if __name__ == "__main__":
        unittest.main()
        
        
        
        
        
        
        