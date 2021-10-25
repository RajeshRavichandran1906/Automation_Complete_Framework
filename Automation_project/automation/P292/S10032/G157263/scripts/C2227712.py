'''
Created on Jun 16, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227712
TestCase Name = Preview Lasso menu
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227712_TestClass(BaseTestCase):

    def test_C2227712(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227712'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(5)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step04: Click "Camcorder" riser > Verify menu
        """ 
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(2)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step04:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step04:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step04.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", bar,"Step04: Verify bar value")
        time.sleep(5) 
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g1!mbar!']")
        utillobj.click_on_screen(parent_elem, 'middle', click_type=1)
        time.sleep(6)
        resultobj.select_or_verify_lasso_filter(verify=['1 point', 'Filter Chart', 'Exclude from Chart'],msg='Step 04: Expect to see the Right-click options appear')
        
        """
        Step05: Select "Filter Chart" > Verify Preview
        """ 
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step05: Verify Filter created")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step05:a(i) Verify Y-Axis Title")
        expected_xval_list=['Camcorder']
        expected_yval_list=['0', '20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step05.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step05: Verify bar value")
        time.sleep(5) 
    
        """
        Step06: Click Undo button in the toolbar 
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        time.sleep(5)
        
        """
        Step07: Verify Filter pane and Preview
        """ 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(3)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step07:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", bar,"Step07: Verify bar value")
        time.sleep(5) 
        
        """
        Step 08: Lasso risers: Media Player and Stereo Systems > Verify menu shows 2 points selected
        Step 09: Select "Filter Chart"
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g3!mbar!', target_tag='rect', target_riser='riser!s0!g4!mbar!')
        time.sleep(5)
        resultobj.select_or_verify_lasso_filter(verify=['2 points', 'Filter Chart', 'Exclude from Chart'],msg='Step 08: Expect to see the Right-click options appear')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        """
        Step 10: Verify Preview and Filter pane
        """ 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step10: Verify Filter created")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step10:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step10.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step10: Verify bar value")
        time.sleep(5) 
         
        """
        Step 11: Right-click "Product,Category" in the Filter pane > Select "Edit..."
        """ 
        parent_css="#resultAreaQueryGrid div[id^='filterBox']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.filter_tree_field_click("Product,Category", 1, 1,"Edit...")
         
        """
        Step12: Verify dialog
        Step13: Click Cancel
        """ 
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        elem=self.driver.find_element_by_css_selector("#avAlphaOperatorComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        print(d)
        print(d['text'])
        utillobj.asequal(d['text'],'Equal to',"Step12.a: Verify operator in Filter dialog")
        l=['Media Player', 'Stereo Systems']
        metaobj.select_or_verify_visualization_filter_values(l, verify='true', msg = 'Step12.b: Verify dialog Media Player, Stereo Systems is checked')
        time.sleep(5)         
        parent_elem=driver.find_element_by_id("avFilterCancelBtn")
        utillobj.click_on_screen(parent_elem, 'middle', click_type=0)
         
        """
        Step 14: Right-click "Product,Category" in the Filter pane > Select "Show Prompt"
        """ 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.filter_tree_field_click("Product,Category", 1, 1,"Show Prompt")
         
        """
        Step 15: Verify Preview
        """ 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step15: Verify Filter created")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step15:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step15:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step15.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step15: Verify bar value")
        time.sleep(5) 
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player', verify=True, verify_type=True, msg="Step15: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', verify=True, verify_type=True, msg="Step15: Verify true is checked in filter prompt")
         
        """
        Step 16: Click "Save" > Save as "C2164834" > click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
           
        """
        Step 18: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
         
        """
        Step 19: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step19: Verify Filter created")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step19:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step19:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step19.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step19: Verify bar value")
        time.sleep(5) 
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player', verify=True, verify_type=True, msg="Step19: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', verify=True, verify_type=True, msg="Step19: Verify true is checked in filter prompt")
         
        """
        Step 20: Click Run > Verify output
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        chart_type_css="#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(3)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step20:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step20:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step20.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step20: Verify bar value")
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player', verify=True, verify_type=True, msg="Step20: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', verify=True, verify_type=True, msg="Step20: Verify true is checked in filter prompt")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227712_Actual_step20', image_type='actual',x=1, y=1, w=-1, h=-1)       
         
        """
        Step 21: Close output window
        """
        time.sleep(5)
        driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        """
        Step 22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()