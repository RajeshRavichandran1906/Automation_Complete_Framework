'''
Created on Jun 20, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227713
TestCase Name = Preview pop up menu
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227713_TestClass(BaseTestCase):

    def test_C2227713(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227713'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double-click "Cost of Goods" from Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
                 
        """
        Step03: Double-click "Product,Category" from Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step04: Expand Dimension "Sales_Related" > "Trasaction Date, Simple" > Right-click "Sale,Quarter" > Select "Add to Query" > "Columns"
        """
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Quarter", 1, 1,"Add To Query", 'Columns')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28)
        
        """
        Step05: Expand Dimension "Sales_Related" > "Trasaction Date, Simple" > Right-click "Sale,Year" > Select "Add to Query" > "Rows"
        """
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Add To Query", 'Rows')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 168)
        
        """
        Step06: Right-click "Gross Profit" > Select "Add to Query" > "Color"
        """
        time.sleep(5)
        metaobj.datatree_field_click("Gross Profit", 1, 1,"Add To Query", 'Color')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 168)
        
        """
        Step07: Right-click "Quantity,Sold" > Select "Add to Query" > "Size"
        """
        time.sleep(5)
        metaobj.datatree_field_click("Quantity,Sold", 1, 1,"Add To Query", 'Size')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 168)
        
        """
        Step08: Right-click "Sale Unit(s)" > Select "Add to Query" > "Tooltip"
        """
        time.sleep(5)
        metaobj.datatree_field_click("Sale Unit(s)", 1, 1,"Add To Query", 'Tooltip')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 168)
        
        """
        Step09: Verify Query and Preview
        """
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        metaobj.verify_query_pane_field('Rows',"Sale,Year",1,"Step 09.a")
        metaobj.verify_query_pane_field('Columns',"Sale,Quarter",1,"Step 09.b")
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step 09.c")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step 09.d")
        metaobj.verify_query_pane_field('Color',"Gross Profit",1,"Step 09.e")
        metaobj.verify_query_pane_field('Size',"Quantity,Sold",1,"Step 09.f")
        metaobj.verify_query_pane_field('Tooltip',"Sale Unit(s)",1,"Step 09.g")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 168)
        time.sleep(2)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step09:h(i) Verify X-Axis Title")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step09:h(ii) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '5.6M', '11.2M', '16.8M', '22.4M', '28M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step09:h(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 168, 'Step09.i: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", "dollar_bill", "Step09.j: Verify first bar color")
        time.sleep(5)
        expected=['2011','2012','2013','2014','2015','2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step09.k(i): Verify Row header")
        expected=['1','2','3','4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columnn','Sale Quarter', expected,"Step09.k(ii): Verify Column header")
        legend=['Gross Profit', '0.1M', '2.7M', '5.3M', '7.9M', '10.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step09.l: Verify legend Title")
        time.sleep(3)
        
        """
        Step10: Hover over the green "Stereo Systems" riser for Year 2016, Quarter 1> Verify pop up menu
        """
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mbar!r5!c0!']")
        utillobj.click_on_screen(parent_elem, 'top_middle',y_offset=7)
        bar=['Sale Year:2016', 'Sale Quarter:1', 'Product Category:Stereo Systems', 'Cost of Goods:$20,327,832.00', 'Quantity Sold:109,642', 'Gross Profit:$8,495,513.74', 'Sale Unit(s):77,803', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", bar, "Step10: Verify bar value",default_move=True)
         
#          
#         bar=['Sale Year:2016', 'Sale Quarter:1', 'Product Category:Stereo Systems', 'Cost of Goods:$20,327,832.00', 'Quantity Sold:109,642', 'Gross Profit:$8,495,513.74', 'Sale Unit(s):77,803', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", bar, "Step10: Verify bar value")
        time.sleep(5) 
        
        """
        Step11: Click Run > Verify output
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(15)  
          
        chart_type_css="rect[class*='riser!s0!g4!mbar!r5!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 48)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 168)
        time.sleep(2)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step11:(i) Verify X-Axis Title")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step11(ii) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M', '24M', '28M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step11(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 168, 'Step11: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", "dollar_bill", "Step11: Verify first bar color")
        time.sleep(5)
        expected=['2011','2012','2013','2014','2015','2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step11: Verify Row header")
        expected=['1','2','3','4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columnn','Sale Quarter', expected,"Step11: Verify Column header")
        legend=['Gross Profit', '0.1M', '2.7M', '5.3M', '7.9M', '10.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11: Verify legend Title")
        time.sleep(3)
        
        """
        Step12: Hover over the green "Accessories" riser for Year 2016, Quarter 2> Verify pop up menu
        """
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mbar!r5!c0!']")
        utillobj.click_on_screen(parent_elem, 'middle')
        bar=['Sale Year:2016', 'Sale Quarter:1', 'Product Category:Stereo Systems', 'Cost of Goods:$20,327,832.00', 'Quantity Sold:109,642', 'Gross Profit:$8,495,513.74', 'Sale Unit(s):77,803', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", bar, "Step12: Verify bar value",default_move=True)
         
#         bar=['Sale Year:2016', 'Sale Quarter:1', 'Product Category:Stereo Systems', 'Cost of Goods:$20,327,832.00', 'Quantity Sold:109,642', 'Gross Profit:$8,495,513.74', 'Sale Unit(s):77,803', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", bar, "Step12: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227713_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
      
        """
        Step14: Click "Save" > Save as "C2164833" > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                  
        """
        Step15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step16: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158180.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
                 
        """
        Step17: Verify Preview and Query pane
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g4!mbar!r5!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        metaobj.verify_query_pane_field('Rows',"Sale,Year",1,"Step 17.a")
        metaobj.verify_query_pane_field('Columns',"Sale,Quarter",1,"Step 17.b")
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step 17.c")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step 17.d")
        metaobj.verify_query_pane_field('Color',"Gross Profit",1,"Step 17.e")
        metaobj.verify_query_pane_field('Size',"Quantity,Sold",1,"Step 17.f")
        metaobj.verify_query_pane_field('Tooltip',"Sale Unit(s)",1,"Step 17.g")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 168)
        time.sleep(2)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step17:h(i) Verify X-Axis Title")
        yaxis_value="Cost of Goods"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step17:h(ii) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '5.6M', '11.2M', '16.8M', '22.4M', '28M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:h(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 168, 'Step17.i: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", "dollar_bill", "Step17.j: Verify first bar color")
        time.sleep(5)
        expected=['2011','2012','2013','2014','2015','2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step17.k(i): Verify Row header")
        expected=['1','2','3','4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columnn','Sale Quarter', expected,"Step17.k(ii): Verify Column header")
        legend=['Gross Profit', '0.1M', '2.7M', '5.3M', '7.9M', '10.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17.l: Verify legend Title")
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mbar!r5!c0!']")
        utillobj.click_on_screen(parent_elem, 'top_middle',y_offset=7)
        bar=['Sale Year:2016', 'Sale Quarter:1', 'Product Category:Stereo Systems', 'Cost of Goods:$20,327,832.00', 'Quantity Sold:109,642', 'Gross Profit:$8,495,513.74', 'Sale Unit(s):77,803', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r5!c0!", bar, msg="Step17: Verify bar value",default_move=True)
        time.sleep(5) 
        
        """
        Step18: Logout
        """
        
if __name__ == '__main__':
    unittest.main()