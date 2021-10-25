'''
Created on May 26, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227614
TestCase Name = Lasso with multiple components on canvas
'''

import unittest,time, os
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_run, ia_run, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pyautogui

class C2227614_TestClass(BaseTestCase):

    def test_C2227614(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227614'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
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
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
          
        """
        Step 04: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",33, 'Step 04.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
#         utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mregion!", "vermilion", "Step 04.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step04:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mregion!",expected_tooltip, "Step 04.e: verify the default tooltip values")       
          
        """
        Step 05: Select Insert > Chart
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(10)
          
        """
        Step 06: Add fields "Revenue" and "Product,Category"
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
        Step 07: Drag and drop "Store,Country" into the Rows bucket
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
          
        """
        Step 08: Verify Preview
        """
        time.sleep(5)
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g4!mbar!r3!c0!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '0', '40M', '80M', '120M', '160M', '0', '40M', '80M', '120M', '160M', '0', '40M', '80M', '120M', '160M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step08.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 08:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 08:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 237, 'Step 08.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g4!mbar!r3!c0!", "bar_blue", "Step 08.c: Verify bar color")
        time.sleep(2)
        tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r3!c0!',tooltip_val,"Step 08.d: Verify output value")
          
        """
        Step 09:  Lasso values for Brazil and Canada
        Step 10: Select "Filter Chart" (14 points)
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody2 [class*='riser!s0!g0!mbar!r2!c0!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
         
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
#         resultobj.create_lasso('MAINTABLE_wbody2','rect', 'riser!s0!g0!mbar!r2!c0!', target_tag='rect', target_riser='riser!s0!g6!mbar!r3!c0!')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
          
        """
        Step 11: Verify Preview
        """
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g4!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 14)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(10)
        metaobj.verify_filter_pane_field('COUNTRY_NAME and PRODUCT_CATEGORY',1,"Step11:")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step11.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 11:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 11:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 14, 'Step 11.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g4!mbar!r1!c0!", "bar_blue", "Step 11.c: Verify bar color")
        tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r1!c0!',tooltip_val,"Step 11.d: Verify output value")
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",2, 'Step 11.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mregion!", "elf_green", "Step 11.f: Verify first bar color")
        legend=['Revenue', '26M', '32.3M', '38.6M', '44.9M', '51.1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11.g: Verify legend Title")
        time.sleep(3)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 11.h: verify the default tooltip values")       
        time.sleep(5)
          
        """
        Step 12: Select Insert > Grid
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        time.sleep(10)
          
        """
        Step 13: Add fields "Revenue", "Store,Country" and "Product,Category"
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
        Step 14: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody3')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody3 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14)
        time.sleep(5)
        heading = ['Store Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody3',heading, 'Step 14.1: Verify column titles')
        row_val=['Brazil', 'Accessories', '$3,174,057.03']
        resultobj.verify_grid_row_val('MAINTABLE_wbody3',row_val,'Step 14.2: verify grid 1st row value')
        metaobj.verify_filter_pane_field('COUNTRY_NAME and PRODUCT_CATEGORY',1,"Step14.3:")
        expected_tooltip=['Store Country:Brazil', 'Product Category:Accessories', 'Revenue:$3,174,057.03', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 14.d: verify the default tooltip values")
         
        """
        Step 15: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
         
        """
        Step 16: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mcellFill!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        chart_type_css="rect[class*='riser!s0!g0!mbar!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        chart_type_css="path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,2)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        time.sleep(5)
        heading = ['Store Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody3',heading, 'Step 16.1: Verify column titles')
        row_val=['Brazil', 'Accessories', '$3,174,057.03']
        resultobj.verify_grid_row_val('MAINTABLE_wbody3',row_val,'Step 16.2: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Accessories', 'Revenue:$3,174,057.03', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 16.4: verify the default tooltip values")
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step16.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 16:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 14, 'Step 16.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g4!mbar!r1!c0!", "bar_blue", "Step 16.c: Verify bar color")
        tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r1!c0!',tooltip_val,"Step 16.d: Verify output value")
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",2, 'Step 16.e: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "persian_red", "Step 16.f: Verify first bar color")
        legend=['Revenue', '26M', '32.3M', '38.6M', '44.9M', '51.1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16.g: Verify legend Title")
        time.sleep(3)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 16.h: verify the default tooltip values")       
         
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227614_Base_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
         
         
        """
        Step 17: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 18: Click "Add" in the Home Tab
        Step 19: Click OK to message
        """
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,2)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        time.sleep(5)
        ribbonobj.select_ribbon_item('Home','add_storyboard')
        time.sleep(10)
        self.driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='infomark']").is_displayed()
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(5)
        
        """
        Step 20: Click "Show" in the Home Tab to view storyboard
        """
        ribbonobj.select_ribbon_item('Home','show_storyboard')
        time.sleep(10)
        
        """
        Step 21: Verify Storyboard page in PowerPoint
        Step 22: Close the PowerPoint application
        """
        if browser == 'Chrome':
            actual_file=Test_Case_ID+'_actual_20_'+browser
            if os.path.isfile(os.getcwd()+"\\data\\"+actual_file+".pptx"):
                os.remove(os.getcwd()+"\\data\\"+actual_file+".pptx")
            pyautogui.typewrite(os.getcwd()+"\\data\\"+actual_file, pause=2)
            pyautogui.press('enter',  pause=7)
            os.startfile(os.getcwd()+"\\data\\"+actual_file+".pptx")
            time.sleep(5)
        else:
            os.system(os.getcwd()+"\\common\\lib\\Open_file.exe "+browser)
        time.sleep(15)
        pyautogui.press('f5', pause=5)
        time.sleep(1)
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step20', image_type='actual', left=145, top=0, right=145, bottom=0)  
        time.sleep(7)
        pyautogui.press('esc', pause=5)
        utillobj.kill_process('POWERPNT')
        time.sleep(9)
        utillobj.switch_to_main_window()
        time.sleep(2)
        utillobj.switch_to_default_content()
        
         
        """
        
        Step 23: Click "Save" icon > "C2166456" > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
          
        """
        Step 24: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
               
        """
        Step 25: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
              
        """
        Step 26: Verify Preview 
        """
        time.sleep(8)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,2)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        time.sleep(5)
        chart_type_css="rect[class*='riser!s0!g0!mcellFill!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        chart_type_css="rect[class*='riser!s0!g0!mbar!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        chart_type_css="path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        heading = ['Store Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_3',heading, 'Step 26.1: Verify column titles')
        row_val=['Brazil', 'Accessories', '$3,174,057.03']
        resultobj.verify_grid_row_val('TableChart_3',row_val,'Step 26.2: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Accessories', 'Revenue:$3,174,057.03', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 26.3: verify the default tooltip values")
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step26.5: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 26:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 26:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada']
        resultobj.verify_visualization_row_column_header_labels('TableChart_2','Rows',expected_header,expected_label,"Step 26:a(iii):")
        resultobj.verify_number_of_riser("TableChart_2", 1, 14, 'Step 26.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g4!mbar!r1!c0!", "bar_blue", "Step 26.c: Verify bar color")
        tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('TableChart_2','riser!s0!g4!mbar!r1!c0!',tooltip_val,"Step 26.d: Verify output value")
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("TableChart_1",2, 'Step 26.e: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mregion!", "persian_red", "Step 26.f: Verify first bar color")
        legend=['Revenue', '26M', '32.3M', '38.6M', '44.9M', '51.1M']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step26.g: Verify legend Title")
        time.sleep(3)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mregion!",expected_tooltip, "Step 26.h: verify the default tooltip values")       
        
         
        """
        Step 27: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()