'''
Created on Mar 31, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227667
Test case Name =  Sort Descending and Ascending
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity, core_utility
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization


class C2227667_TestClass(BaseTestCase):

    def test_C2227667(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227667'
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visualization = Visualization(self.driver)
        
        """
        TESTCASE CSS
        """
        qwery_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        visualization.wait_for_visible_text("#pfjTableChart_1", "Drop")

        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        visualization.double_click_on_datetree_item("Cost of Goods", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Cost of Goods")
        
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        visualization.double_click_on_datetree_item("Product,Category", 1)
        visualization.wait_for_visible_text(qwery_tree_css, "Product,Category")
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        Step 05: Click OK
        """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        visualization.wait_for_visible_text("#avFilterCancelBtn", "Cancel")
        ok_ele = utillobj.validate_and_get_webdriver_object('#avFilterOkBtn', 'ok')
        core_utils.left_click(ok_ele)
        
        """
        Step 06: Select values in the Filter Prompt: "Media Player" and "Stereo Systems"
        Step 07: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visualization.wait_for_visible_text(parent_css, 'Media Player')
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player') 
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems')  
        
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, visualization.home_page_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        #bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        #resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 07: Verify bar value")
             
        """
        Step08: Right-click "Product,Category" in the Filter pane > Select Edit...
        Step09: Check off value: "Video Production" > Click OK
        Step10: Verify Canvas
        """
        metaobj.filter_tree_field_click('Product,Category', 1, 1, 'Edit...')
        metaobj.create_visualization_filters('alpha',['GridItems',['Video Production']])
        
        time.sleep(6)        
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player', verify=True,verify_type=True,msg="Step10: Verify Media Player checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems', verify=True,verify_type=True,msg="Step10: Verify Stereo Systems checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Video Production', verify=True,verify_type=True,msg="Step10: Verify Video Production checked")
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, visualization.home_page_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems','Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(5)
        #bar=['Product Category:Video Production', 'Cost of Goods:$40,105,657.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        #resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 10: Verify bar value")
        
        """
        Step11: Click Save
        Step12: Click Save in the toolbar > Save as "C2227667" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        visualization.wait_for_visible_text('#IbfsOpenFileDialog7_btnCancel', "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", visualization.home_page_short_timesleep)
           
        """
        Step13: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step14: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227667.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
           
        """
        Step15: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, visualization.home_page_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 15:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 15:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.c: Verify first bar color")
        time.sleep(5)
        #bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        #resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 15: Verify bar value")
         
        time.sleep(6)        
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player', verify=True,verify_type=True,msg="Step15: Verify Media Player checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems', verify=True,verify_type=True,msg="Step15: Verify Stereo Systems checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Video Production', verify=True,verify_type=True,msg="Step15: Verify Video Production checked")
         
        """
        Step 16: Check off value "Computers" in the Filter Prompt
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, visualization.home_page_long_timesleep)
        propertyobj.select_or_verify_show_prompt_item('1', 'Computers')
        time.sleep(5)      
                 
        """
        Step 17: Verify Canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, visualization.home_page_long_timesleep)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step17:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step17.c: Verify first bar color")
        time.sleep(5)
        #bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        #resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step17: Verify bar value")
         
        propertyobj.select_or_verify_show_prompt_item('1', 'Computers', verify=True,verify_type=True,msg="Step17: Verify Computers checked")
        time.sleep(5) 
       
        """
        Step 18: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        visualization.switch_to_new_window()
        time.sleep(15)
           
        """
        Step 19: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 19:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 19:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 19.c: Verify first bar color")
        time.sleep(5)
        #bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        #resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 19: Verify bar value")
        
        time.sleep(6)        
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player', verify=True,verify_type=True,msg="Step19: Verify Media Player checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems', verify=True,verify_type=True,msg="Step19: Verify Stereo Systems checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Video Production', verify=True,verify_type=True,msg="Step19: Verify Video Production checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Computers', verify=True,verify_type=True,msg="Step19: Verify Computers checked")
                 
        time.sleep(20)
        #ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        #utillobj.take_screenshot(ele,'C2227667_Actual_step19', image_type='actual',x=1, y=1, w=-1, h=-1) 
            
        """
        Step20: Close the output window
        Step21: Logout
        """
        visualization.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)          
                 

        
if __name__ == '__main__':
    unittest.main()
        