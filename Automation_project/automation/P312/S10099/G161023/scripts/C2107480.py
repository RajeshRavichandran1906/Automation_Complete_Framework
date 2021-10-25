'''
Created on May'03, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107480
'''
import unittest
from selenium.webdriver import ActionChains
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2107480_TestClass(BaseTestCase):
    def test_C2107480(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107480'

        """
            Step 01: Launch the IA API with wf_retail_lite
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
            
        #utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8357', 'mrid01', 'mrpass01')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
       
        """
            Step 02: Change to bubble Chart.
        """
        ribbonobj.change_chart_type('bubble_chart')
        time.sleep(5)
        """
            Step 03: Double click Model and Revenue.
        """
        metaobj.datatree_field_click("Model", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(8)
        
        """
            Step 04: Verify fields added to query pane.
        """
        metaobj.verify_query_pane_field('Vertical Axis', 'Revenue', 1, "Step 04a: field model added to query pane")
        metaobj.verify_query_pane_field("Detail","Model",1,"Step 04b: field Revenue added to query pane")
        time.sleep(5)
        """
            Step 05: Verify any 2 model and revenue values from top and bottom
        """
        
        parent_css="#MAINTABLE_wbody1 svg g circle[class^='riser']"
        resultobj.wait_for_property(parent_css,157)
        
        a=['Revenue:$14,850,534.60', 'Model:Sony KDL46HX800', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']     
        b=["Revenue:$460,735.48","Model:Toshiba R420A","Filter Chart", "Exclude from Chart", 'Drill up to Product Subcategory']
       
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g134!mmarker", a, "Step 05a: Verify model and revenue value from Top")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g134!mmarker", "bar_blue", "Step 05a: Verify riser color")
        time.sleep(5)
        
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g150!mmarker", b, "Step 05b: Verify model and revenue value from bottom")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g150!mmarker", "bar_blue", "Step 05b: Verify riser color")
        

        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 157, 158, 'Step 05: Verify number of Circle displayed')
        x_val_list=[]
        y_val_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 05: X and Y axis Scales Values has changed or NOT')
        yaxis_value="Revenue"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 05:d(ii) Verify Y-Axis Title")
        
        """
            Step 06: Add Quantity Sold(format - I11C) to Horizontal axis.
        """
        time.sleep(5)
        metaobj.datatree_field_click("Quantity,Sold", 1, 1,"Add To Query","Horizontal Axis")
        time.sleep(8)
        browser =utillobj.parseinitfile('browser')
        move_ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(move_ele,move=True)
        else :
            action = ActionChains(driver)
            action.move_to_element_with_offset(move_ele,1,1).perform()
        
        time.sleep(5)
        """
            Step 07: Hover over on any bubble and click Filter Chart.
        """
        riser=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 [class*='riser!s0!g22!mmarker']")
        utillobj._validate_page(riser)
        
        c=['Quantity Sold:25,666', 'Revenue:$6,858,809.70', 'Model:GLXYT10716', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g22!mmarker",c,"Step 07: Hover any bubble and click filter chart")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g22!mmarker", "bar_blue", "Step 07: Verify riser color")
        time.sleep(5)
        x_val_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        y_val_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 07: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Quantity Sold"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 07:d(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 157, 158, 'Step 07: Verify number of Circle displayed')
        
        #Filter Chart
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g22!mmarker", 'Filter Chart')
        
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker']"
        resultobj.wait_for_property(parent_css2,1)
        
        """
            Step 08: Verify output (exact bubble value)
        """
        time.sleep(10)
        d=['Quantity Sold:25,666', 'Revenue:$6,858,809.70', 'Model:GLXYT10716', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker",d,"Step 08: Verify output value")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step 08: Verify riser color")
        
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 1, 1, 'Step 08: Verify number of Circle displayed')
        x_val_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        y_val_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 08: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Quantity Sold"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 08:d(ii) Verify Y-Axis Title")

        """
        Step 09: Click "Save" in the toolbar > Type C2107480 > Click "Save" in the Save As dialog
        """
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2107480_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
if __name__ == '__main__':
    unittest.main()

