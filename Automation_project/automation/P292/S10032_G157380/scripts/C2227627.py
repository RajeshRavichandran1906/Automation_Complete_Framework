'''
Created on Jun 9, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227627
TestCase Name = Lasso with multiple components on canvas
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class C2227627_TestClass(BaseTestCase):

    def test_C2227627(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227627'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
             
        """
        Step 02: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type("choropleth_map")
            
        """
        Step 03: Double click "Store,Country", "Revenue"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Store,Country', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        time.sleep(4)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",33, 'Step 03.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step03:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mregion!",expected_tooltip, "Step 03.e: verify the default tooltip values")       
           
        """
        Step 04: Select Insert > Chart
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(10)
           
        """
        Step 05: Add fields "Revenue" and "Product,Category"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody2 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody2 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        time.sleep(5)
           
        """
        Step 06: Drag and drop "Store,Country" into the Rows bucket
        """
        time.sleep(4)
        metaobj.datatree_field_click('Store,Country',1, 1, 'Add To Query', 'Rows')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 237)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody2 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 170)
        time.sleep(5)
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g4!mbar!r3!c0!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '0', '40M', '80M', '120M', '160M', '0', '40M', '80M', '120M', '160M', '0', '40M', '80M', '120M', '160M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step06.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 06:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 06:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 06:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 237, 'Step 06.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g4!mbar!r3!c0!", "bar_blue", "Step 06.c: Verify bar color")
        time.sleep(2)
        tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r3!c0!',tooltip_val,"Step 06.d: Verify output value")
           
        """
        Step 07: Lasso values for Brazil and Canada
        Step 08: Select "Filter Chart" (14 points)
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody2 [class*='riser!s0!g0!mbar!r2!c0!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        source=driver.find_element_by_css_selector("#MAINTABLE_wbody2 rect[class*='riser!s0!g0!mbar!r2!c0']")
        get_source = utillobj.get_object_screen_coordinate(source, x_offset=-10, y_offset=-10)
        target=driver.find_element_by_css_selector("#MAINTABLE_wbody2 rect[class*='riser!s0!g6!mbar!r3!c0!']")
        get_target = utillobj.get_object_screen_coordinate(target, coordinate_type='bottom_right', x_offset=10, y_offset=10)
        utillobj.drag_drop_on_screen(sx_offset=get_source['x'],sy_offset=get_source['y'],tx_offset=get_target['x'],ty_offset=get_target['y'])
        time.sleep(1)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
           
        """
        Step 09: Verify Preview
        """
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g4!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 14)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(10)
        metaobj.verify_filter_pane_field('COUNTRY_NAME and PRODUCT_CATEGORY',1,"Step09:")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step09.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 09:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 09:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 14, 'Step 09.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g4!mbar!r1!c0!", "bar_blue", "Step 09.c: Verify bar color")
        tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r1!c0!',tooltip_val,"Step 09.d: Verify output value")
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",2, 'Step 09.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mregion!", "elf_green", "Step 09.f: Verify first bar color")
        legend=['Revenue', '26M', '32.3M', '38.6M', '44.9M', '51.1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step09.g: Verify legend Title")
        time.sleep(3)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 09.h: verify the default tooltip values")       
        time.sleep(5)
           
        """
        Step 10: Select Insert > Grid
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        time.sleep(10)
           
        """
        Step 11: Add fields "Revenue", "Store,Country" and "Product,Category"
        """
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        metaobj.datatree_field_click('Store,Country', 2, 1)
        time.sleep(4)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,2)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
  
        """
        Step 12: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody3')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody3 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14)
        time.sleep(5)
        heading = ['Store Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody3',heading, 'Step 12.1: Verify column titles')
        row_val=['Brazil', 'Accessories', '$3,174,057.03']
        resultobj.verify_grid_row_val('MAINTABLE_wbody3',row_val,'Step 12.2: verify grid 1st row value')
        metaobj.verify_filter_pane_field('COUNTRY_NAME and PRODUCT_CATEGORY',1,"Step12.3:")
        expected_tooltip=['Store Country:Brazil', 'Product Category:Accessories', 'Revenue:$3,174,057.03', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 12.d: verify the default tooltip values")
        
        """
        Step 13: Hover over "Stereo Systems" for "Canada" > Verify pop up menu and Drill down sub menu.
        Step 14: Select "Drill down to" > "Store State Province"
        """
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g4!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 14)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r1!c0!',tooltip_val,"Step 13.d: Verify output value")
        time.sleep(6)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody2")
        utillobj.click_on_screen(css, coordinate_type='start')
        utillobj.synchronize_with_number_of_element(parent_css, 7, 25)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody2", "riser!s0!g4!mbar!r1!c0!",'Drill down to->Store State Province')
        
        """
        Step 15: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody3')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody3 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        heading = ['Store Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody3',heading, 'Step 15.1: Verify column titles')
        row_val=['Canada', 'Stereo Systems', '$14,226,673.48']
        resultobj.verify_grid_row_val('MAINTABLE_wbody3',row_val,'Step 15.2: verify grid 1st row value')
        expected_tooltip=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 15.d: verify the default tooltip values")
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g0!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('COUNTRY_NAME and PRODUCT_CATEGORY',1,"Step15:")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step15.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 15:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 15:a(ii) Verify Y-Axis Title")
        expected_header='Store State Pro'
        expected_label=['British Columbia', 'Ontario']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 15:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 2, 'Step 15.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar!r1!c0!", "bar_blue", "Step 15.c: Verify bar color")
        tooltip_val=['Store State Province:Ontario', 'Product Category:Stereo Systems', 'Revenue:$7,153,326.32', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g0!mbar!r1!c0!',tooltip_val,"Step 15.d: Verify output value")
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step 15.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "persian_red", "Step 15.f: Verify first bar color")
        legend=['Revenue', '14,226,672.5', '14,226,673', '14,226,673.5', '14,226,674', '14,226,674.5']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step15.g: Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion!']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',x_offset=-10, y_offset=-55)
        expected_tooltip=['Store Country:Canada', 'Revenue:$14,226,673.48', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 15.e: verify the default tooltip values", default_move=True)
        time.sleep(5)
         
        """
        Step 16: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
         
        """
        Step 17: Hover over riser for "Ontario" > Verify menu
        """
        chart_type_css="[id^='MAINTABLE_2'] [class*='riser!s0!g0!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(4)
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step17.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 17:a(ii) Verify Y-Axis Title")
        expected_header='Store State Province'
        expected_label=['British Columbia', 'Ontario']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 17:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 2, 'Step 17.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar!r1!c0!", "bar_blue", "Step 17.c: Verify bar color")
        time.sleep(4)
        expected_tooltip=['Store State Province:Ontario', 'Product Category:Stereo Systems', 'Revenue:$7,153,326.32', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g0!mbar!r1!c0!",expected_tooltip, "Step 17: verify the default tooltip values", y_offset=5)       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227627_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
     
        """
        Step 18: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 19: Click "Save" icon > "C2167749" > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
           
        """
        Step 20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
                
        """
        Step 21: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
               
        """
        Step 22: Verify Preview 
        """
        time.sleep(8)
        elem=(By.CSS_SELECTOR,'#TableChart_3')
        resultobj._validate_page(elem)
        parent_css="#TableChart_3 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        heading = ['Store Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_3',heading, 'Step 22.1: Verify column titles')
        row_val=['Canada', 'Stereo Systems', '$14,226,673.48']
        resultobj.verify_grid_row_val('TableChart_3',row_val,'Step 22.2: verify grid 1st row value')
        expected_tooltip=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48']
        resultobj.verify_default_tooltip_values("TableChart_3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 22.d: verify the default tooltip values")
        raiser="[id^='TableChart_2'] [class*='riser!s0!g0!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        parent_css="#TableChart_2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#TableChart_2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('COUNTRY_NAME and PRODUCT_CATEGORY',1,"Step22:")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step22.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 22:a(ii) Verify Y-Axis Title")
        expected_header='Store State Pro'
        expected_label=['British Columbia', 'Ontario']
        resultobj.verify_visualization_row_column_header_labels('TableChart_2','Rows',expected_header,expected_label,"Step 22:a(iii):")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 22.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!r1!c0!", "bar_blue", "Step 22.c: Verify bar color")
        tooltip_val=['Store State Province:Ontario', 'Product Category:Stereo Systems', 'Revenue:$7,153,326.32', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to']
        resultobj.verify_default_tooltip_values('TableChart_2','riser!s0!g0!mbar!r1!c0!',tooltip_val,"Step 22.d: Verify output value")
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#TableChart_1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#TableChart_1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("TableChart_1",1, 'Step 22.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mregion!", "persian_red", "Step 22.f: Verify first bar color")
        legend=['Revenue', '14,226,672.5', '14,226,673', '14,226,673.5', '14,226,674', '14,226,674.5']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step22.g: Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mregion!']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',x_offset=-10, y_offset=-55)
        expected_tooltip=['Store Country:Canada', 'Revenue:$14,226,673.48', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mregion!",expected_tooltip, "Step 22.e: verify the default tooltip values", default_move=True)
        time.sleep(5)    
        
        """
        Step 23: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()