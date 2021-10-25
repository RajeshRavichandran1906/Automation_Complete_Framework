'''
Created on Oct 27, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313573
TestCase Name = Edit format of measure for tooltip
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2313573_TestClass(BaseTestCase):

    def test_C2313573(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2313573'

        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click Product,Category, Discount and Quantity,Sold.
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        
        time.sleep(4)
        metaobj.datatree_field_click("Discount", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels!']"
        resultobj.wait_for_property(parent_css, 6)
        
        time.sleep(4)
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14)
        
        """
        Step 03: Right click Discount > Edit Format
        """
        time.sleep(4)
        metaobj.querytree_field_click("Discount", 1, 1, 'Edit Format')
        time.sleep(6) 
        
        """
        Step 04: Change Currency Symbol to None
        Step 05: Check Suppress Comma > OK
        """
        metaobj.set_bin_format(currency_symbol='None')
        metaobj.set_bin_format(check_box_list=['Suppress Comma (c)'], ok_btn=True)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14)
        bar=['Product Category:Accessories', 'Discount:6014845.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step05: Verify first bar value for Discount")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Quantity Sold:771,934', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g3!mbar!", bar,"Step05: Verify last bar value for Quantity,Sold")
        
        """
        Step 06: Right click Quantity,Sold > Edit Format
        """
        metaobj.querytree_field_click("Quantity,Sold", 1, 1, 'Edit Format')
        time.sleep(4)
        
        """
        Step 07: Change Field Type to Decimal
        Step 08: Change Currency Symbol to Floating Currency (M) > OK
        """
        metaobj.set_bin_format(field_type='Decimal')
        metaobj.set_bin_format(currency_symbol='Floating Currency', ok_btn=True)
        time.sleep(8)
        
        """
        Step 09: Hover over Discount in preview
        """
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels!']"
        resultobj.wait_for_property(parent_css, 5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step09:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','4M','8M','12M','16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step09.c: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g3!mbar!", "pale_green", "Step09.c: Verify second bar color")
        legend=['Discount', 'Quantity Sold']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step09.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Discount:6014845.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step09: Verify bar value for Discount")
        time.sleep(5)
        
        """
        Step 10: Hover over Quantity,Sold in preview
        """
        time.sleep(5)
        bar=['Product Category:Media Player', 'Quantity Sold:$771,934.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g3!mbar!", bar,"Step10: Verify bar value for Quantity,Sold")
        time.sleep(5)
        
        """
        Step 11: Save with name C2313573 and close
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 12: Use API to run from tree:
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2313573.fex
        """
        utillobj.active_run_fex_api_login('C2313573.fex','S10660_visual_2','mrid','mrpass')
        time.sleep(10)
        
        """
        Step 13: Hover over Discount and Quantity,Sold and review tooltip
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14) 
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step13:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','4M','8M','12M','16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g3!mbar!", "pale_green", "Step13.c: Verify second bar color")
        legend=['Discount', 'Quantity Sold']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13.d: Verify Legends Title")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Discount:6014845.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step13: Verify first bar value for Discount")
        time.sleep(8)
        bar=['Product Category:Media Player', 'Quantity Sold:$771,934.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g3!mbar!", bar,"Step13b: Verify last bar value for Quantity,Sold")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2313573_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()        