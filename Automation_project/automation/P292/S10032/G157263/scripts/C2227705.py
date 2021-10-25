'''
Created on Jun 07, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227705
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By



class C2227705_TestClass(BaseTestCase):

    def test_C2227705(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227705'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
                    
        """
        Step03: Double-click "Product,Category", from Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)  
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step03: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step03: Verify horizontal axis")
             
        """
        Step04: Right-click "Cost of Goods" in the Query pane > verify menu
        Step05: Select "More > Aggregation Functions > Average"
        """
        time.sleep(2)
        metaobj.querytree_field_click("Cost of Goods", 1, 1)
        time.sleep(2)
        a=['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Edit Format', 'Drill Down', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,msg='Step04: Verify menu in querypane')
        time.sleep(2)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
#         utillobj.click_on_screen(parent_elem, 'middle')
#         time.sleep(1)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(2) 
        utillobj.select_or_verify_bipop_menu('Average')
        time.sleep(2) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
         
        """
        Step06: Verify changes in the Query pane and Preview
        """  
        metaobj.verify_query_pane_field('Vertical Axis',"AVE.Cost of Goods",1,"Step06: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step06: Verify horizontal axis")
          
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step06:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'AVE Cost of Goods', "Step06:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '200','400','600','800','1,000']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step06.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step06.c: Verify first bar color")
#         time.sleep(5)
#         bar=['Product Category:Accessories', 'AVE Cost of Goods:$247.26', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step06: Verify bar value")
        time.sleep(5)
          
#         time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2227705_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
   
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                   
        """
        Step07: Click Save in the toolbar
        Step08: Save as "C2158261" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                   
        """
        Step09: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)  
           
        """
        Step10: Reopen
        Step11: Verify canvas
        """ 
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(2)
                    
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
          
        metaobj.verify_query_pane_field('Vertical Axis',"AVE.Cost of Goods",1,"Step11: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step11: Verify horizontal axis")
        time.sleep(3)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'AVE Cost of Goods', "Step11:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '200','400','600','800','1,000']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step11.c: Verify first bar color")
        time.sleep(5)
#         bar=['Product Category:Accessories', 'AVE Cost of Goods:$247.26', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step11: Verify bar value")
#         time.sleep(5) 
 

if __name__ == '__main__':
    unittest.main()