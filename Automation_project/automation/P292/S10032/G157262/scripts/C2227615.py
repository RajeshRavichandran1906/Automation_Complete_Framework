'''
Created on May 11, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227615
'''
import unittest, time
from selenium.webdriver.common.by import By
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2227615_TestClass(BaseTestCase):
    
    def test_C2227615(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227615'
        query_css = '#queryTreeColumn'
        
        """
            TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """
        Step02: Click "Change" in the Home Tab > Select "Side-by-side" chart
        """
        ribbonobj.change_chart_type('bar')
        time.sleep(5)
           
        """
        Step03: Double-click "Cost of Goods" and "Gross Profit"
        Step04: Double-click "Product,Category"
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        utillobj.synchronize_with_visble_text(query_css, "Cost of Goods", 30)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        utillobj.synchronize_with_visble_text(query_css, "Gross Profit", 30)
        metaobj.datatree_field_click("Product,Category", 2,1)
        utillobj.synchronize_with_visble_text(query_css, "Product,Category", 30)
         
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
         
        """
        Step05: Hover over blue riser for value "Computers" > Verify menu with "Drill down to Product Subcategory"
        """
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 05.01: Verify tool tip with 'Drill down to Product Subcategory'")
         
        """
        Step06: Select "Drill down to Product Subcategory"
        """
        time.sleep(2)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g2!mbar",'Drill down to Product Subcategory')
         
        """
        Step07: Verify Preview with "Product Subcategory" in the Horizontal Axis and "Product Category" filter in the Filter pane
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Subcategory', 1, "Step 07.01: Verify Product Subcategory in Horizontal Axis")
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step 07.02: Verify Product Category in Filter Pane")
         
        """
        Step08: Hover over green riser for value "Smartphone" > Verify menu with "Drill up to Product Category" and "Drill down to Model"
        """
        time.sleep(5)
        bar=['Product Subcategory:Smartphone', 'Gross Profit:$15,834,702.15', 'Filter Chart', 'Exclude from Chart', 'Go up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g0!mbar", bar, "Step 08.01: Verify bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step 08.02: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step 08.03: Verify Y-Axis Title")
        expected_xval_list=['Smartphone','Tablet']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.04:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 08.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar", "pale_green", "Step 08.06: Verify first bar color")
        time.sleep(5)
        
        """
        Step09: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
             
        """
        Step10: Hover over blue riser for "Tablet" > Verify menu with "Drill up to Product Category" and "Drill down to Model"
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step 10.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step 10.02: Verify Y-Axis Title")
        expected_xval_list=['Smartphone','Tablet']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 10.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 10.05: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Tablet', 'Cost of Goods:$25,771,890.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 10.06: Verify bar value")
        time.sleep(5)
        
        """
        Step11: Select "Drill down to Model" > Verify output
        """
        time.sleep(2)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g1!mbar",'Drill down to Model')
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 10)
        
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Model', "Step 11.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step 11.02: Verify Y-Axis Title")
        expected_xval_list=['GLXYT10716','GLXYT10732','GLXYT3B','GLXYT3W','GLXYT70','SGP311U1/B','SGP312U1/B','SGPT121US/S','SGPT122US/S','SGPT123US/S']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M','3.5M','4M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 20, 'Step 11.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g2!mbar", "pale_green", "Step 11.05: Verify first bar color")
        time.sleep(5)
        
        """
        Step12: Hover over green riser for value "GLXYT3B" > Verify menu with "Drill up to Product Subcategory"
        """
        bar=['Model:GLXYT3B', 'Gross Profit:$1,233,116.25', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Go up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g2!mbar", bar, "Step 12.01: Verify bar value")
        
        """
        Step13: Close the output window
        Step14: Click Save in the toolbar > Save as "C2227615" > Click Save
        """
        time.sleep(5)
        core_utils.switch_to_previous_window()
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
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Subcategory', 1, "Step 17.01: Verify Product Subcategory in Horizontal Axis")
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step 17.02: Verify Product Category in Filter Pane")
        
        time.sleep(5)
        bar=['Product Subcategory:Smartphone', 'Gross Profit:$15,834,702.15', 'Filter Chart', 'Exclude from Chart', 'Go up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g0!mbar", bar, "Step 17.03: Verify bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step 17.04: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step 17.05: Verify Y-Axis Title")
        expected_xval_list=['Smartphone','Tablet']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 17.06: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 17.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar", "pale_green", "Step 17.08: Verify first bar color")
        time.sleep(5)      
        
if __name__ == '__main__':
    unittest.main()