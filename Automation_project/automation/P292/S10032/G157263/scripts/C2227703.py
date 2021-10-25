'''
Created on Jun 08, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227703
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By



class C2227703_TestClass(BaseTestCase):

    def test_C2227703(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227703'
        
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
        Step02: Click "Change" button in the Home Tab ribbon > Select Bubble Chart
        """
        ribbonobj.change_chart_type('bubble_chart')
        time.sleep(5)
        
        """
        Step03: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(2)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
                    
        """
        Step04: Double-click "Product,Subcategory", located under Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(4)
          
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step04: Verify vertical axis")
        metaobj.verify_query_pane_field('Detail',"Product,Subcategory",1,"Step04: Verify Detail")
             
        """
        Step05: Right-click "Color" bucket in the Query pane > verify menu
        Step06: Select "Color BY"
        """
        time.sleep(2)
        metaobj.querytree_field_click("Color", 1, 1)
        time.sleep(2)
        a=['Color BY']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,msg='Step05: Verify menu in querypane')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Color BY')
        time.sleep(2)
        
        """
        Step07: Drag and drop "Product,Category" to "Color BY" bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("Product,Category", 1, 'Color BY', 0)
        time.sleep(2) 
        parent_css="#MAINTABLE_wbody1 .legend-title"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        
        """
        Step08: Verify changes in the Query pane and Preview
        """          
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step08: Verify vertical axis")
        metaobj.verify_query_pane_field('Detail',"Product,Subcategory",1,"Step08: Verify Detail")
        metaobj.verify_query_pane_field('Color BY',"Product,Category",1,"Step08: Verify Color BY")
        
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step08:a(i) Verify Y-Axis Title")
        expected_xval_list=[]
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        label=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", label,"Step08: Verify bubble chart Legend")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 21, 22, 'Step08b: Verify number of Circle displayed')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g0!mmarker", "pale_yellow", "Step08.c(i) Verify first bar color")
        
#         time.sleep(5)
#         bar=['Cost of Goods:$181,112,921.00', 'Product Category:Media Player', 'Product Subcategory:Blu Ray', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s3!g0!mmarker", bar, "Step08: Verify bar value")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2227705_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
    
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                    
        """
        Step09: Click Save in the toolbar
        Step10: Save as "C2158261" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
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
                     
        parent_css="#MAINTABLE_wbody1 .legend-title"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
                
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step13: Verify vertical axis")
        metaobj.verify_query_pane_field('Detail',"Product,Subcategory",1,"Step13: Verify Detail")
        metaobj.verify_query_pane_field('Color BY',"Product,Category",1,"Step13: Verify Color BY")
        
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step13:a(i) Verify Y-Axis Title")
        expected_xval_list=[]
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        label=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", label,"Step13: Verify bubble chart Legend")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 21, 22, 'Step13b: Verify number of Circle displayed')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g0!mmarker", "pale_yellow", "Step13.c(i) Verify first bar color")
        
#         time.sleep(5)
#         bar=['Cost of Goods:$181,112,921.00', 'Product Category:Media Player', 'Product Subcategory:Blu Ray', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s3!g0!mmarker", bar, "Step13: Verify bar value")
        

if __name__ == '__main__':
    unittest.main()



    
     
        