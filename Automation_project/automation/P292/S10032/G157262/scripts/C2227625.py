'''
Created on May 22, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227625
TestCase Name = Drill down with Heatmap chart type
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227625_TestClass(BaseTestCase):

    def test_C2227625(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227625'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """
        Step 02: Click "Change" in the Home Tab > Select "Heatmap" chart
        """
        ribbonobj.change_chart_type("heatmap")
        
        """
        Step 03: Double-click "Gross Profit"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g rect[class*='riser!s0!g0!mbar']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 04: Double-click "Product,Category"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='zaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 05: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 7, 'Step 05a: Verify number of Circle displayed')
        expected_xval_list=[]
        expected_yval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 05.b: X and Y axis Scales Values has changed or NOT', y_custom_css="text[class^='zaxisOrdinal-labels']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g0!mbar!", "elf_green", "Step 05.c(i) Verify first bar color")
        legend=['Gross Profit', '16.8M', '34.2M', '51.5M', '68.8M', '86.2M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step05:d(ii) Verify Y-Axis Title")
        time.sleep(2)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 05:d(i) Verify X-Axis Title")
        expected_tooltip=['Gross Profit:$49,598,845.24', 'Product Category:Camcorder', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s1!g0!mbar",expected_tooltip, "Step 05.e: verify the default tooltip values")       
        
        """
        Step 06:  Hover over area for "Camcorder" value > Verify tooltip menu > Select "Drill down to Product Subcategory"
        """
        time.sleep(5)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s1!g0!mbar!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(3)        
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s1!g0!mbar!", "Drill down to Product Subcategory")
        time.sleep(5)
        
        """
        Step 07: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='zaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step07.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 07a: Verify number of Circle displayed')
        expected_xval_list=[]
        expected_yval_list=['Handheld', 'Professional', 'Standard']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07.b: X and Y axis Scales Values has changed or NOT', y_custom_css="text[class^='zaxisOrdinal-labels']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "elf_green", "Step 07.c(i) Verify first bar color")
        legend=['Gross Profit', '8.8M', '12M', '15.1M', '18.3M', '21.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step07:d(i) Verify Y-Axis Title")
        time.sleep(2)
        xaxis_value="Product Subcategory"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 07:d(ii) Verify X-Axis Title")
        expected_tooltip=['Gross Profit:$21,393,654.97', 'Product Subcategory:Handheld', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 07.e: verify the default tooltip values")       
        
        """
        Step 08: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 09:  Hover over value for "Professional" > Select "Drill down to Model"
        """
        chart_type_css="rect[class*='riser!s1!g0!mbar!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='zaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s1!g0!mbar!", "Drill down to Model")
        time.sleep(5)
        
        """
        Step 10: Verify output
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='zaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        xaxis_value="Model"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10:d(i) Verify X-Axis Title")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 4, 'Step 10a: Verify number of Circle displayed')
        expected_xval_list=[]
        expected_yval_list=['Canon XHA1S', 'JVC GYHD200U', 'Sony HDRAX2000', 'Sony HXRNX5U']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.b: X and Y axis Scales Values has changed or NOT', y_custom_css="text[class^='zaxisOrdinal-labels']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar", "elf_green", "Step 10.c(i) Verify first bar color")
        legend=['Gross Profit', '1.5M', '1.8M', '2.1M', '2.4M', '2.7M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(ii) Verify Y-Axis Title")
        time.sleep(2)
        expected_tooltip=['Gross Profit:$1,892,638.80', 'Model:Canon XHA1S', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 10.e: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227625_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 11: Click "Save" > Save as "C2167768" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """
        Step 12: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
        Step 13: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
            
        """
        Step 14: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='zaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step14.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 14a: Verify number of Circle displayed')
        expected_xval_list=[]
        expected_yval_list=['Handheld', 'Professional', 'Standard']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 14.b: X and Y axis Scales Values has changed or NOT', y_custom_css="text[class^='zaxisOrdinal-labels']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "elf_green", "Step 14.c(i) Verify first bar color")
        legend=['Gross Profit', '8.8M', '12M', '15.1M', '18.3M', '21.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step14:d(i) Verify Y-Axis Title")
        time.sleep(2)
        xaxis_value="Product Subcategory"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 14:d(ii) Verify X-Axis Title")
        expected_tooltip=['Gross Profit:$21,393,654.97', 'Product Subcategory:Handheld', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 14.e: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()