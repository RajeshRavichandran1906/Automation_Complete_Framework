'''
Created on Oct 20, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328046
TestCase Name = PCT.CNT as aggregation option for dimension (char) fields in IA+
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2328046_TestClass(BaseTestCase):

    def test_C2328046(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2328046'

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double click "Product, Category" to Horizontal axis
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 03: Drag and drop "Model" to Vertical Axis
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_query_tree("Model", 1, 'Vertical Axis', 0)
        time.sleep(2) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 11)  
        
        """ 
        Step 04: Verify in query pane Vertical axis CNT prefix added to "Model" field and displayed same in preview    
        """
        metaobj.verify_query_pane_field('Vertical Axis', 'CNT.Model', 1, "Step04a: Verify in query pane Vertical axis CNT prefix added to 'Model' field")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'CNT Model', "Step04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '5','10','15','20','25','30','35','40','45','50']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step04:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step04.c: Verify first bar color")
        time.sleep(6)
        bar=['Product Category:Accessories', 'CNT Model:14', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step04: Verify bar value")
        time.sleep(5)
        
        """ 
        Step 05: Right click on "CNT.Model" > More >Aggregations functions (pull right) 
        Step 06: Verify the list of options:
        Count (grey dot)
        Count Distinct
        Percent of Count
        """
        time.sleep(2)
        metaobj.querytree_field_click("CNT.Model", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(0.5)
        a=['Count','Count Distinct','Percent of Count']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Count'],msg='Step06: Verify the list of options')
#         utillobj.verify_object_visible("[class='icon-column checkbox']",False,'"Step04:checkbox checked')
        
        """
        Step 07: Click "Percent of Count" option
        """
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Percent of Count')
        
        """ 
        Step 08: Verify query pane and preview updated with "PCT.CNT.Model" aggregation function 
        """
        metaobj.verify_query_pane_field('Vertical Axis', 'PCT.CNT.Model', 1, "Step08: Verify in query pane Vertical axis CNT prefix added to 'Model' field")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'PCT.CNT Model', "Step08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '5','10','15','20','25','30']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'PCT.CNT Model:8.81', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step08: Verify bar value")
        time.sleep(5)
        
        """ 
        Step 09: Right Click "PCT.CNT.Model" > More >Aggregations functions (pull right)
        Step 10: Verify "Percent of Count" option is selected (grey dot)
        Step 11: Click OK
        """
        time.sleep(2)
        metaobj.querytree_field_click("PCT.CNT.Model", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(0.5)
        a=['Count','Count Distinct','Percent of Count']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Percent of Count'],msg='Step10: Verify "Percent of Count" option is selected')
        
        """ 
        Step 12: Hover on "Media player" riser
        Step 13: Verify the tool tip value
        """
        time.sleep(8)
        bar=['Product Category:Media Player', 'PCT.CNT Model:27.04', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar,"Step13: Verify the tool tip value")
        
        """
        Step 14: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
                  
        """
        Step 15: Hover on "computer" riser 
        Step 16: Verify the tool tip value
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'PCT.CNT Model', "Step16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '5','10','15','20','25','30']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step16.c: Verify first bar color")
        time.sleep(6)
        bar=['Product Category:Computers', 'PCT.CNT Model:12.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar!", bar,"Step16: Verify the tool tip value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2328046_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
             
        """
        Step17: Dismiss run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step18: Click Save in the toolbar > Save as "C2328046" > Click Save
        """     
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
             
        """
        Step19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
        
        """
        Step20: Reopen the saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2328046.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
            
        """
        Step21: Verify restored successfully
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step21:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'PCT.CNT Model', "Step21:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '5','10','15','20','25','30']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step21:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step21.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step21.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'PCT.CNT Model:8.81', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step21: Verify bar value")
        time.sleep(5)
        
        """ 
        Step 22: Right Click "PCT.CNT.Model" > More >Aggregations functions (pull right)
        Step 23: Verify "Percent of Count" option is selected (grey dot)
        """
        time.sleep(2)
        metaobj.querytree_field_click("PCT.CNT.Model", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(0.5)
        a=['Count','Count Distinct','Percent of Count']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Percent of Count'],msg='Step23: Verify "Percent of Count" option is selected')
        
        """
        Step 24: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        
if __name__ == '__main__':
    unittest.main()