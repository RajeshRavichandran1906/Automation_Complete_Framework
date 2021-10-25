'''
Created on May 12, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227616
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227616_TestClass(BaseTestCase):
    def test_C2227616(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227616'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
             
        """
        Step02: Click "Change" in the Home Tab > Select "Scatter" chart type
        """
        ribbonobj.change_chart_type('scatter')
        time.sleep(5)
               
        """
        Step03: Double-click "Cost of Goods" and "Product,Category"
        Step04: Drag and drop "Customer,Business,Region" into the Columns bucket
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Customer,Business,Region",1,1,'Add To Query','Columns')
        time.sleep(8)
             
        """
        Step05: Hover over point for "Media Player" in 'North America' region > Verify pop up menu with "Drill down to" sub menu.
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        bar=['Customer Business Region:North America', 'Cost of Goods:$79,074,473.00', 'Product Category:Media Player', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mmarker!r0!c1", bar, "Step 05: Verify bar value")
            
        """
        Step06: Select "Drill down to" > Verify options > "Customer Business Sub Region" and "Product Subcategory"
        Step07: Select "Customer Business Sub Region"
        """        
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mmarker!r0!c1']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g3!mmarker!r0!c1",'Drill down to->Customer Business Sub Region',default_move=True,preview=True,verify_menu1=['Customer Business Sub Region', 'Product Subcategory'],msg="Step06: Verify Drill down to menu")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mmarker!r0!c1']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g3!mmarker!r0!c1",'Drill down to->Customer Business Sub Region',default_move=True,preview=True)
        
        """
        Step08: Verify Preview and field "Customer Business Sub Region" in the Columns bucket (Query pane)
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.verify_query_pane_field('Columns', 'Customer,Business,Sub Region', 1, "Step08: Verify Customer,Business,Sub Region in Columns")
        metaobj.verify_filter_pane_field('BUSINESS_REGION and PRODUCT_CATEGORY', 1, "Step08: Verify Filter Pane")
           
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step08:a(i) Verify Y-Axis Title")
        expected_label=['Canada', 'East', 'Mexico', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Customer Business Sub Region', expected_label, "Step08a(ii): Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 8, 9, 'Step 08b: Verify number of Circle displayed')
           
        time.sleep(5)
        bar=['Customer Business Sub Region:Canada', 'Cost of Goods:$16,190,913.00', 'Product Category:Media Player', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", bar, "Step08: Verify bar value")
             
        """
        Step09: Right click filter in the Filter pane > Verify only "Delete" option is available
        """
        metaobj.filter_tree_field_click('BUSINESS_REGION and PRODUCT_CATEGORY', 1, 1)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Delete'],msg='Step09: Verify popup menu')        
        
        """
        Step10: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
              
        """
        Step11: Hover over point for "East" Sub Region > Verify menu with "Drill up to Customer Business Region" and "Drill down to" sub menu
        Step12: Select "Drill down to" sub menu > Verify options for "Customer Country" and "Product Subcategory"
        Step13: Select Drill down to > Customer Country"
        """
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(5)
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 8)

        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step13:a(i) Verify Y-Axis Title")
        expected_label=['Canada', 'East', 'Mexico', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Customer Business Sub Region', expected_label, "Step13a(ii): Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 8, 9, 'Step13b: Verify number of Circle displayed')
         
        time.sleep(5)
        bar=['Customer Business Sub Region:East', 'Cost of Goods:$11,455,431.00', 'Product Category:Media Player', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c1", bar, "Step13: Verify bar value")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker!r0!c1']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c1",'Drill down to->Customer Country',default_move=True,verify_menu1=['Customer Country', 'Product Subcategory'],msg="Step13: Verify Drill down to menu")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker!r0!c1']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c1",'Drill down to->Customer Country',default_move=True)
         
        """
        Step14: Verify output
        Step15: Hover over point > Verify pop up menu and sub menu options
        """         
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 1)
          
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step14:a(i) Verify Y-Axis Title")
        expected_label=['United States']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Customer Country', expected_label, "Step14a(ii): Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step14:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 1, 2, 'Step14b: Verify number of Circle displayed')
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227616_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1) 
        time.sleep(5)
        bar=['Customer Country:United States', 'Cost of Goods:$11,455,431.00', 'Product Category:Media Player', 'Remove Filter', 'Drill up to Customer Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", bar, "Step14: Verify bar value")
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker!r0!c0']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        if browser != 'Firefox':
            time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill down to->Product Subcategory',default_move=True,verify_menu1=['Customer State Province', 'Product Subcategory'],msg="Step15: Verify Drill down to menu")
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mmarker!r0!c0']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0",'Drill down to->Product Subcategory',default_move=True) 
          
        """
        Step16: Click Save in the toolbar
        Step17: Save as "C2158150" > Click Save
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
          
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
          
        """
        Step18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
          
        """
        Step19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
           
        """
        Step20: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='colLabel']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.verify_query_pane_field('Columns', 'Customer,Business,Sub Region', 1, "Step20: Verify Customer,Business,Sub Region in Columns")
        metaobj.verify_filter_pane_field('BUSINESS_REGION and PRODUCT_CATEGORY', 1, "Step20: Verify Filter Pane")
         
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step20:a(i) Verify Y-Axis Title")
        expected_label=['Canada', 'East', 'Mexico', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns', 'Customer Business Sub Region', expected_label, "Step20a(ii): Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 8, 9, 'Step20b: Verify number of Circle displayed')
         
        time.sleep(5)
        bar=['Customer Business Sub Region:Canada', 'Cost of Goods:$16,190,913.00', 'Product Category:Media Player', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", bar, "Step20: Verify bar value")
        
if __name__ == '__main__':
    unittest.main()