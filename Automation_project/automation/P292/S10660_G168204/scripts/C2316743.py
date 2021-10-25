'''
Created on Nov 1, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2316743
TestCase Name = Add bin to horizontal axis
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2316743_TestClass(BaseTestCase):

    def test_C2316743(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2316743'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Invoke IA Visualization tool with wf_retail
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=wf_retail
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Expand Product > Model > Attributes
        """
        time.sleep(3)
        metaobj.expand_field_tree('Product')
        time.sleep(2)
        metaobj.expand_field_tree('Product')
        time.sleep(2)
        metaobj.expand_field_tree('Model')
        time.sleep(2)
        metaobj.expand_field_tree('Attributes')
        time.sleep(6)
       
        """
        Step03: Right click Price,Dollars > Create Bins...
        """ 
        metaobj.expand_field_tree('Price,Dollars', click_opt=1, x_offset=35)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Create Bins...')
        time.sleep(6)
        
        """
        Step04: Change bin width to 100 > OK
        """ 
        bin_dialog="div[id^='QbDialog'] div[class*='bi-window active window']"
        resultobj.wait_for_property(bin_dialog, 1)
        metaobj.create_bin('PRICE_DOLLARS_BIN_1',bin_width='100')
        
        """
        Step05: Double click the bin to add to horizontal axis (can't be done right now because of IA-7034, for the time being drag the bin to horizontal axis instead)
        """ 
        time.sleep(4)
        metaobj.verify_data_pane_field("Customer", "PRICE_DOLLARS_BIN_1", 1, "Step 05: Verify the PRICE_DOLLARS_BIN_1 has been added to the Data pane")
        metaobj.datatree_field_click('PRICE_DOLLARS_BIN_1', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 18)
        
        """
        Step 06: Double click Quantity,Sold
        """
        time.sleep(5)
        metaobj.datatree_field_click('Quantity,Sold', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRICE_DOLLARS_BIN_1', "Step06:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step06:a(ii) Verify Y-Axis Title")
        expected_xval_list=['.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 18, 'Step06.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step06.c: Verify first bar color")
        time.sleep(5)
        expected_tooltip=['PRICE_DOLLARS_BIN_1:100.00', 'Quantity Sold:1,137,404']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", expected_tooltip,"Step06.d: Verify bar value")
        time.sleep(5)
        
        """
        Step07: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
         
        """
        Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 18)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRICE_DOLLARS_BIN_1', "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 18, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step07.c: Verify first bar color")
        time.sleep(5)
        expected_tooltip=['PRICE_DOLLARS_BIN_1:100.00', 'Quantity Sold:1,137,404']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", expected_tooltip,"Step07.d: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2316743_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 08: Close output, save visualization with name C2316743 and close IA.
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()