'''
Created on Jun 09, 2017
@author: Kiruthika
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227701
'''

import unittest, time
from common.lib import utillity
from common.lib import core_utility
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.locators import visualization_resultarea_locators
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon

class C2227701_TestClass(BaseTestCase):

    def test_C2227701(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227701'
        
        """
        CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
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
        Step02: Double-click "Cost of Goods" and "Gross Profit", from Sales Measures
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeWindow", "Cost of Goods", 30)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeWindow", "Gross Profit", 30)
                
        """
        Step03: Double-click "Product,Category", from Product Dimension
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)  
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step 03.01: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step 03.02: Verify horizontal axis")
             
        """
        Step04: Right-click "Vertical Axis" in the Query pane > verify menu
        Step05: Select "Multi-Y split"
        Step06: Verify Preview
        """
        time.sleep(2)
        metaobj.querytree_field_click("Vertical Axis", 1, 1)
        time.sleep(2)
        a=['Multi-Y split']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,msg='Step 04.01: Verify menu in querypane')
        time.sleep(2)
                
        utillobj.select_bipopup_list_item('Multi-Y split')
#         utillobj.select_or_verify_bipop_menu('Multi-Y split')
        time.sleep(2) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step 06.01: Verify vertical axis")
        metaobj.verify_query_pane_field('Vertical Axis',"Gross Profit",2,"Step 06.02: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step 06.03: Verify horizontal axis")
            
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        yaxis_value = "Cost of Goods"
        y2axis_value = "Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 06.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 06.05: Verify y-Axis Title", custom_css="text[class='yaxis-title']")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", y2axis_value, "Step 06.06: Verify y2-Axis Title", custom_css="text[class='y2axis-title']")

        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '60M','120M','180M','240M']
        expected_y2val_list=['0','25M','50M','75M','100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 06.07:Verify XY labels")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_y2val_list,"Step 06.08", y_custom_css="text[class^='y2axis-labels']")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step 06.09: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!ay1!mbar", "bar_blue", "Step 06.10: Verify first bar color")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!ay2!mbar", "bar_blue", "Step 06.11: Verify first bar color")
        
        """
        Step07: Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utils.switch_to_new_window()
      
        """
        Step08: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, ribbonobj.home_page_long_timesleep)
        xaxis_value="Product Category"
        
        yaxis_value = "Cost of Goods"
        y2axis_value = "Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08.02: Verify y-Axis Title", custom_css="text[class='yaxis-title']")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", y2axis_value, "Step 08.03: Verify y2-Axis Title", custom_css="text[class='y2axis-title']")   
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '60M','120M','180M','240M']
        expected_y2val_list=['0','25M','50M','75M','100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.04:Verify XY labels")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_y2val_list,"Step 08.05:", y_custom_css="text[class^='y2axis-labels']")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step 08.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!ay1!mbar", "bar_blue", "Step 08.07: Verify first bar color")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!ay2!mbar", "bar_blue", "Step 08.08: Verify first bar color")
        time.sleep(5)
        
        """
        Step09: Close output window
        """
        core_utils.switch_to_previous_window()

        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step10: Click "Save" > Save as "C2167744" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step12: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step13: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, ribbonobj.home_page_long_timesleep)
                     
        """
        Step14: Verify Preview
        """ 
        metaobj.verify_query_pane_field('Vertical Axis',"Cost of Goods",1,"Step 14.01: Verify vertical axis")
        metaobj.verify_query_pane_field('Vertical Axis',"Gross Profit",2,"Step 14.02: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Product,Category",1,"Step 14.03: Verify horizontal axis")
            
        xaxis_value="Product Category"
        yaxis_value = "Cost of Goods"
        y2axis_value = "Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 14.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 14.05: Verify y-Axis Title", custom_css="text[class='yaxis-title']")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", y2axis_value, "Step 14.06: Verify y2-Axis Title", custom_css="text[class='y2axis-title']")

        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '60M','120M','180M','240M']
        expected_y2val_list=['0','25M','50M','75M','100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14.07:Verify XY labels")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_y2val_list,"Step 14.08", y_custom_css="text[class^='y2axis-labels']")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step 14.09: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!ay1!mbar", "bar_blue", "Step 14.10: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!ay2!mbar", "bar_blue", "Step 14.11: Verify first bar color")

if __name__ == '__main__':
    unittest.main()        