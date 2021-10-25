'''
Created on May'05, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227607
'''
import unittest
from selenium.webdriver import ActionChains
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227607_TestClass(BaseTestCase):
    def test_C2227607(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227607'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Click "Change" in the Home Tab > Select "Bubble" chart type
        """
        ribbonobj.change_chart_type('bubble_chart')
        time.sleep(5)
         
        """
        Step03: Double-click "Cost of Goods"
        Step04: Drag "Product,Category" to Horizontal Axis.
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Add To Query","Horizontal Axis")
        time.sleep(8)
        
        parent_css="#MAINTABLE_wbody1 svg g circle[class^='riser']"
        resultobj.wait_for_property(parent_css,7)
        
        """
        Step05: Lasso "Camcorder" and "Computers" risers > Select "Filter Chart"
        """
        riser=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 [class*='riser!s0!g1!mmarker']")
        utillobj._validate_page(riser)
         
        #Filter Chart
        resultobj.create_lasso("MAINTABLE_wbody1","circle",'riser!s0!g1!mmarker', target_tag='circle', target_riser='riser!s0!g2!mmarker')
        time.sleep(2)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
         
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker']"
        resultobj.wait_for_property(parent_css2,2)
         
        """
        Step06: Verify Preview
        """
        time.sleep(10)
        d=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker",d,"Step06: Verify output value")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step06: Verify riser color")
         
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 2, 3, 'Step06: Verify number of Circle displayed')
        x_val_list=['Camcorder','Computers']
        y_val_list=['0', '20M', '40M', '60M', '80M', '100M','120M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step06: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step06:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step06:d(ii) Verify Y-Axis Title")
        
        """
        Step07: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
            
        """
        Step08: Verify output
        """
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(5)
        riser=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker']")
        utillobj._validate_page(riser)
        
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 2, 3, 'Step08: Verify number of Circle displayed')
        x_val_list=['Camcorder','Computers']
        y_val_list=['0', '20M', '40M', '60M', '80M', '100M','120M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step08: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step08:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step08:d(ii) Verify Y-Axis Title")        
        
        d=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker",d,"Step08: Verify output value")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step08: Verify riser color")
         
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227607_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 09: Click Save in the toolbar
        Step10: Save as "C2158150" > Click Save
        """
        time.sleep(5)
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
        time.sleep(5)
        
        """
        Step11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
        
        """
        Step12: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_2',mrid='mrid',mrpass='mrpass')
        
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker']"
        resultobj.wait_for_property(parent_css2,1)
         
        """
        Step13: Verify canvas
        """
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 2, 3, 'Step13: Verify number of Circle displayed')
        x_val_list=['Camcorder','Computers']
        y_val_list=['0', '20M', '40M', '60M', '80M', '100M','120M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step13: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step13:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step13:d(ii) Verify Y-Axis Title")        
        
        time.sleep(10)
        d=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker",d,"Step13: Verify output value")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step13: Verify riser color")         
        
if __name__ == '__main__':
    unittest.main()

