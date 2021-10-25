'''
Created on Jun 07, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227704
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227704_TestClass(BaseTestCase):

    def test_C2227704(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227704'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
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
        Step04: Right-click "Product,Category" in the Query pane > verify menu
        Step05: Select "Create Group..."
        """
        time.sleep(2)
        metaobj.querytree_field_click("Product,Category", 1, 1)
        time.sleep(2)
        a=['Filter Values...', 'Sort', 'Visibility', 'Create Group...', 'Change Title...', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,msg='Step04: Verify menu in querypane')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Create Group...')
        time.sleep(2)
        
        """
        Step06: Multi-select values "Accessories", "Camcorder" and "Computers" and click Group
        Step07: Click OK
        """
        metaobj.create_ia_group('Group', ['Accessories','Camcorder','Computers'], close_button='ok')
        time.sleep(2)
        
        """
        Step08: Verify changes in the Query pane and Preview
        """   
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
         
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step08: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"PRODUCT_CATEGORY_1",1,"Step08: Verify horizontal axis")
          
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 5)
        xaxis_value="PRODUCT_CATEGORY_1"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step08:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Ca','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '50M','100M','150M','200M','250M','300M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step08: Verify bar value")
        time.sleep(5)
          
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2227704_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
   
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                   
        """
        Step09: Click Save in the toolbar
        Step10: Save as "C2158261" > Click Save
        """
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
        Step12: Reopen
        Step13: Verify canvas
        """ 
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(2)
                    
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 5)
          
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step13: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"PRODUCT_CATEGORY_1",1,"Step13: Verify horizontal axis")
        time.sleep(3)
        xaxis_value="PRODUCT_CATEGORY_1"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step13:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Ca','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '50M','100M','150M','200M','250M','300M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step13: Verify bar value")
        time.sleep(5) 
 

if __name__ == '__main__':
    unittest.main()



    
     
        