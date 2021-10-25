'''
Created on Apr 20, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227653
Test case Name =  List of Values with Attributes field
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227653_TestClass(BaseTestCase):

    def test_C2227653(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227653'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step 02: Double-click "Cost of Goods", "Gross Profit" and "Revenue"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Gross Profit",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Revenue",2,1)
                  
        """
        Step03: Expand Product Dimension > Double click "Product,Category"
        Step04: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > "Sale,Month" > "Attributes" > Drag and drop "Sale,Month Name" into the Rows bucket under Matrix in the Query pane.
        """
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Month Name", 1, 1,"Add To Query", 'Rows')
                  
        """
        Step05: Drag and drop "Sale,Month Name" into the Filter pane
        """
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Month Name", 1, 1,"Filter")        
        time.sleep(6)
                  
        """
        Step06: Verify Filter dialog
        Step07: Click OK
        """            
        item_list=['[All]', 'APR','AUG','DEC','FEB','JAN','JUL','JUN','MAR','MAY','NOV','OCT','SEP']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True, msg = "Step06: Verify Filter Pane Checkbox values") 
        time.sleep(3)
                     
        """
        Step08: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Month Name',1,"Step08: Verify 'Sale,Month Name' appears in filter pane")
             
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step08:Verify prompt [All] is checked")
        time.sleep(5)
                      
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step08:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','14M','28M','42M','56M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 84, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step08.c: Verify first bar color")
        time.sleep(5)
        expected=['APR', 'AUG', 'DEC', 'FEB', 'JAN', 'JUL', 'JUN']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month Name', expected,"Step08: Verify Row header")
               
        bar=['Sale Month Name:APR', 'Product Category:Media Player', 'Revenue:$18,517,796.02', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", bar, "Step08: Verify bar value")

        """
        Step09: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)    
                  
        """
        Step10: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(10)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step10:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(ii) Verify Y-Axis Title")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 72)
        time.sleep(2)
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','14M','28M','42M','56M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 84, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step10.c: Verify first bar color")
        time.sleep(5)
        expected=['APR', 'AUG', 'DEC', 'FEB', 'JAN', 'JUL', 'JUN', 'MAR', 'MAY']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month Name', expected,"Step10: Verify Row header")
        bar=['Sale Month Name:APR', 'Product Category:Media Player', 'Revenue:$18,517,796.02', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", bar, "Step10: Verify bar value")
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step10:Verify prompt [All] is checked")
        time.sleep(8)
                             
        """
        Step11: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
       
        """
        Step12: Click Save
        Step13: Click Save as "C2158200" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                   
        """
        Step14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
               
        """
        Step15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
                  
        """
        Step16: Verify Canvas
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Month Name',1,"Step16: Verify 'Sale,Month Name' appears in filter pane")
        time.sleep(5)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step16:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','14M','28M','42M','56M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 84, 'Step16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step16.c: Verify first bar color")
        time.sleep(5)
        expected=['APR', 'AUG', 'DEC', 'FEB', 'JAN', 'JUL', 'JUN']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month Name', expected,"Step16: Verify Row header")
        bar=['Sale Month Name:APR', 'Product Category:Media Player', 'Revenue:$18,517,796.02', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", bar, "Step16: Verify bar value")
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step16:Verify prompt [All] is checked")
        time.sleep(5)
        
        """
        Step17: Check off values JAN, FEB, MAR in the Filter Prompt
        Step18: Verify Canvas
        """
        propertyobj.select_or_verify_show_prompt_item('1', 'JAN')
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', 'FEB')
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', 'MAR')
        time.sleep(2)
        
        propertyobj.select_or_verify_show_prompt_item('1', 'FEB',verify=True, verify_type=True,msg="Step17:Verify prompt FEB is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'JAN',verify=True, verify_type=True,msg="Step17:Verify prompt JAN is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'MAR',verify=True, verify_type=True,msg="Step17:Verify prompt MAR is checked")
        time.sleep(5)
                    
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step17:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 21, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step17.c: Verify first bar color")
        time.sleep(5)
        expected=['FEB', 'JAN', 'MAR']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month Name', expected,"Step17: Verify Row header")
        bar=['Sale Month Name:FEB', 'Product Category:Media Player', 'Revenue:$18,642,764.35', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", bar, "Step17: Verify bar value")
        
        
        """
        Step19: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)    
                  
        """
        Step20: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        driver.maximize_window()
        time.sleep(5)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit','Revenue']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step20:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step20:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 3, 21, 'Step20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", "dark_green", "Step20.c: Verify first bar color")
        time.sleep(5)
        expected=['FEB', 'JAN','MAR']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month Name', expected,"Step20: Verify Row header")
        bar=['Sale Month Name:FEB', 'Product Category:Media Player', 'Revenue:$18,642,764.35', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s2!g3!mbar!r0!c0", bar, "Step20: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227653_Actual_Step20', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(10)
        propertyobj.select_or_verify_show_prompt_item('1', 'FEB',verify=True, verify_type=True,msg="Step20:Verify prompt FEB is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'JAN',verify=True, verify_type=True,msg="Step20:Verify prompt JAN is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'MAR',verify=True, verify_type=True,msg="Step20:Verify prompt MAR is checked")
        time.sleep(5)
                 
        """
        Step21: Close the output
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
        time.sleep(5)
        
        """
        Step22: Logout
        """
        
if __name__ == '__main__':
    unittest.main()
        