'''
Created on May 15, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227617
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227617_TestClass(BaseTestCase):
    def test_C2227617(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227617'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
             
        """
        Step02: Click "Change" in the Home Tab > Select "Bubble" chart type
        """
        ribbonobj.change_chart_type('bubble_chart')
        time.sleep(5)
               
        """
        Step03: Double-click "Gross Profit"
        Step04: Double-click "Product,Category"
        Step05: Drag and drop "Sale,Quarter" (from Sales_Related > Trasaction Date, Simple) to the Rows bucket
        """
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Rows', 0)
        time.sleep(8)
         
        """
        Step06: Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.verify_query_pane_field('Rows', 'Sale,Quarter', 1, "Step06: Verify Rows")
            
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step06:a(i) Verify Y-Axis Title")
        expected_label=['1','2','3','4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Quarter', expected_label, "Step06a(ii): Verify row header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M','24M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 28, 29, 'Step 06b: Verify number of Circle displayed')
            
        time.sleep(5)
        bar=['Sale Quarter:1', 'Gross Profit:$20,953,693.47', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0", bar, "Step08: Verify bar value")
                    
        """
        Step07:Hover over any point from Quarter 1 > Verify menu with "Drill up to Sale Year" and "Drill down to" sub menu "Sale Month" and "Product Subcategory"
        Step08: Select "Drill up to Sale Year"
        """
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mmarker!r0!c0']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0",'Drill up to Sale Year',default_move=True)
             
        """
        Step09:Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_query_pane_field('Rows', 'Sale,Year', 1, "Step09: Verify Rows")
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step09:a(i) Verify Y-Axis Title")
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Year', expected_label, "Step09a(ii): Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step09:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 42, 43, 'Step 09b: Verify number of Circle displayed')
           
        time.sleep(5)
        bar=['Sale Year:2011', 'Gross Profit:$3,962,974.73', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0", bar, "Step09: Verify bar value")
        
        """
        Step10: Click Run
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(5) 
              
        """
        Step11: Hover over "Stereo Systems" for Year 2014 > select "Drill down to" > "Sale Quarter"
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 6)

        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step11:a(i) Verify Y-Axis Title")
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Year', expected_label, "Step11a(ii): Verify row header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '5M', '10M','15M', '20M','25M','30M','35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 42, 43, 'Step11b: Verify number of Circle displayed')
         
        time.sleep(5)
        bar=['Sale Year:2011', 'Gross Profit:$3,962,974.73', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0", bar, "Step11: Verify bar value")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mmarker!r0!c0']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0",'Drill down to->Sale Quarter',default_move=True,verify_menu1=['Sale Quarter', 'Product Subcategory'],msg="Step11: Verify Drill down to menu")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mmarker!r0!c0']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0",'Drill down to->Sale Quarter',default_move=True)
         
        """
        Step12: Verify output
        """         
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 4)
          
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step12:a(i) Verify Y-Axis Title")
        expected_label=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Quarter', expected_label, "Step12a(ii): Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 4, 5, 'Step12b: Verify number of Circle displayed')
         
        time.sleep(5)
        bar=['Sale Quarter:1', 'Gross Profit:$1,072,105.66', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", bar, "Step12: Verify bar value")
        
        time.sleep(5)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227617_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step13: Click Save in the toolbar
        Step14: Save as "C2158150" > Click Save
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
          
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
          
        """
        Step15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
          
        """
        Step16: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
           
        """
        Step17: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_query_pane_field('Rows', 'Sale,Year', 1, "Step17: Verify Rows")
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step17:a(i) Verify Y-Axis Title")
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Year', expected_label, "Step17a(ii): Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 42, 43, 'Step17b: Verify number of Circle displayed')
           
        time.sleep(5)
        bar=['Sale Year:2011', 'Gross Profit:$3,962,974.73', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0", bar, "Step17: Verify bar value")
              
if __name__ == '__main__':
    unittest.main()