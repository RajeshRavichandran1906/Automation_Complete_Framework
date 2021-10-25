'''
Created on Jun 22, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227715
TestCase Name = Storyboard with multiple components 
'''

import unittest,time, os
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_properties
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
import pyautogui

class C2227715_TestClass(BaseTestCase):

    def test_C2227715(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227715'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        time.sleep(8)      
        elem1="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(elem1, 1, 120, 1)
        time.sleep(8)
        
        """
        Step 02: Click "Change" dropdown > "ESRI Choropleth"
        """
        time.sleep(4)
        ribbonobj.change_chart_type("choropleth_map")
        
        """
        Step 03: Double click "Store,Country", "Revenue"
        """
        time.sleep(10)
        metaobj.datatree_field_click('Store,Country', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 42,expire_time=50)
        time.sleep(4)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        
        """
        Step 04: Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34,expire_time=50)
       
        time.sleep(6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",34, 'Step 04.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step04:d(i) Verify legend Title")
        time.sleep(5)
#         expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mregion!",expected_tooltip, "Step 04.e: verify the default tooltip values")       
          
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
        resultobj.wait_for_property(parent_css, 1,expire_time=50)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='yaxis-title']"
        
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7,expire_time=50)
       
        time.sleep(5)
           
        """
        Step 07: Drag and drop "Store,Country" into the Rows bucket
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Country', 1, 'Rows', 0)
        time.sleep(4)
        
        """
        Step 08: Verify Preview
        """
        
        
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g4!mbar!r3!c0!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, 80, 1)
        
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
#         tooltip_val=['Store Country:Canada', 'Product Category:Stereo Systems', 'Revenue:$14,226,673.48', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
#         resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r3!c0!',tooltip_val,"Step 08.d: Verify output value")
          
        """
        Step 09: Drag and drop "Store,Country" into the Filter Pane
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_filter('Store,Country', 1)
        time.sleep(4)
        
        """
        Step 10: Uncheck [All] to de-select all values
        Step 11: Select values: Brazil, Canada, United States
        """
        elem='#avFilterOkBtn'
        utillobj.synchronize_with_number_of_element(elem, 1, 60, 1)
        time.sleep(3)
        l=['[All]','Brazil','Canada','United States']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(5)
        
        """
        Step 12: Verify Preview
        """
        
        raiser="[id^='MAINTABLE_2'] [class*='riser!s0!g4!mbar!r2!c0!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, 60, 1)
        
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 21,expire_time=50)
        
        time.sleep(10)
        metaobj.verify_filter_pane_field('Store,Country',1,"Step12:")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step12.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada', 'United States']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 12:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 21, 'Step 12.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g4!mbar!r2!c0!", "bar_blue", "Step 12.c: Verify bar color")
#         tooltip_val=['Store Country:United States', 'Product Category:Stereo Systems', 'Revenue:$148,805,886.44', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
#         resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g4!mbar!r2!c0!',tooltip_val,"Step 12.d: Verify output value")
        time.sleep(3)
        
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 3,expire_time=50)
        
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",3,'Step 12.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "persian_red", "Step 12.f: Verify first bar color")
        legend=['Revenue', '26M', '156M', '285.9M', '415.8M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step12.g: Verify legend Title")
        time.sleep(3)
#         expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 12.h: verify the default tooltip values")       
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, 'Brazil', verify=True, verify_type=True, msg="Step12.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Canada', verify=True, verify_type=True, msg="Step12.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'United States', verify=True, verify_type=True, msg="Step12.2: Verify values is checked in filter prompt", scroll_down=True)
        time.sleep(5)
        
        """
        Step 13: Drag and drop "Product,Category" into the Filter Pane
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        time.sleep(4)
        
        """
        Step 14: Uncheck [All] to de-select all values
        Step 15: Select values: Computers, Media Player, Televisions
        """
        elem='#avFilterOkBtn'
        
        utillobj.synchronize_with_number_of_element(elem, 1, 30, 1)
        time.sleep(3)
        l=['[All]','Computers','Media Player','Televisions']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(5)
        
        """
        Step 16: Verify Preview
        """
       
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 9,expire_time=50)
        
        time.sleep(10)
        metaobj.verify_filter_pane_field('Store,Country',1,"Step16:")
        metaobj.verify_filter_pane_field('Product,Category',2,"Step16:")
        expected_xval_list=['Computers', 'Media Player', 'Televisions']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step16.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada', 'United States']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 16:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 9, 'Step 16.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g1!mbar!r2!c0!", "bar_blue", "Step 16.c: Verify bar color")
#         tooltip_val=['Store Country:United States', 'Product Category:Media Player', 'Revenue:$123,949,415.80', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
#         resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g1!mbar!r2!c0!',tooltip_val,"Step 16.d: Verify output value")
        time.sleep(3)
        
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 3,expire_time=50)
        
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",3, 'Step 16.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "persian_red", "Step 16.f: Verify first bar color")
        legend=['Revenue', '10.4M', '63.2M', '116.1M', '169M', '222M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16.g: Verify legend Title")
        time.sleep(3)
#         expected_tooltip=['Store Country:Brazil', 'Revenue:$10,357,820.49', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 16.h: verify the default tooltip values")       
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(2, 'Computers', verify=True, verify_type=True, msg="Step16.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(2, 'Media Player', verify=True, verify_type=True, msg="Step16.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(2, 'Televisions', verify=True, verify_type=True, msg="Step16.2: Verify values is checked in filter prompt")
        time.sleep(5)
        
        """
        Step 17: Click "Add" in the Home Tab
        Step 18: Click OK to message
        """
        time.sleep(5)
        ribbonobj.select_ribbon_item('Home','add_storyboard')
        element_css="div[id^='BiDialog']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 360, 1)
        time.sleep(10)
        btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        time.sleep(5)
        
        """
        Step 19: Click "Show" in the Home Tab to view storyboard
        """
        ribbonobj.select_ribbon_item('Home','show_storyboard')
        time.sleep(10)
        
        """
        Step 20: Verify Storyboard page in PowerPoint
        Step 21: Close the PowerPoint application
        """
        browser = utillobj.parseinitfile('browser')
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
        time.sleep(20)
        pyautogui.press('f5', pause=5)
        time.sleep(7)
        utillobj.verify_picture_using_sikuli("C2227715_Step20.png", 'Step 20. Verify powerpoint slide image')
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step20', image_type='actual', left=145, top=0, right=145, bottom=0)  
        time.sleep(7)
        pyautogui.press('esc', pause=5)
        utillobj.kill_process('POWERPNT')
        time.sleep(9)
        utillobj.switch_to_main_window()
        time.sleep(2)
        utillobj.switch_to_default_content()
        time.sleep(2)
        
        """
        Step 22: Click Run in IA
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 23: Verify output
        """
        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        parent_css="#MAINTABLE_wbody2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 9,expire_time=50)
        
        time.sleep(10)
        expected_xval_list=['Computers', 'Media Player', 'Televisions']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step23.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 23:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 23:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada', 'United States']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody2','Rows',expected_header,expected_label,"Step 23:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 9, 'Step 23.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g1!mbar!r2!c0!", "bar_blue", "Step 23.c: Verify bar color")
#         tooltip_val=['Store Country:United States', 'Product Category:Media Player', 'Revenue:$123,949,415.80', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
#         resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g1!mbar!r2!c0!',tooltip_val,"Step 23.d: Verify output value")
        time.sleep(3)
        
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 3,expire_time=50)
       
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",3, 'Step 23.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "persian_red", "Step 23.f: Verify first bar color")
        legend=['Revenue', '10.4M', '63.2M', '116.1M', '169M', '222M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step23.g: Verify legend Title")
        time.sleep(3)
#         expected_tooltip=['Store Country:Brazil', 'Revenue:$10,357,820.49', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 23.h: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227715_Actual_step23', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(2, 'Computers', verify=True, verify_type=True, msg="Step23.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(2, 'Media Player', verify=True, verify_type=True, msg="Step23.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(2, 'Televisions', verify=True, verify_type=True, msg="Step23.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Brazil', verify=True, verify_type=True, msg="Step23.4: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Canada', verify=True, verify_type=True, msg="Step23.5: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'United States', verify=True, verify_type=True, msg="Step23.6: Verify values is checked in filter prompt", scroll_down=True)
        time.sleep(5)
        
        """
        Step 24: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
       
        """
        Step 25: Click "Save" icon > "C2167749" > click Save
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
           
        """
        Step 26: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
                
        """
        Step 27: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
               
        """
        Step 28: Verify Preview 
        """
        time.sleep(8)
       
        parent_css="#TableChart_2 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 9,expire_time=50)
        
        time.sleep(10)
        metaobj.verify_filter_pane_field('Store,Country',1,"Step28:")
        metaobj.verify_filter_pane_field('Product,Category',2,"Step28:")
        expected_xval_list=['Computers', 'Media Player', 'Televisions']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step28.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 28:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 28:a(ii) Verify Y-Axis Title")
        expected_header='Store Country'
        expected_label=['Brazil', 'Canada', 'United States']
        resultobj.verify_visualization_row_column_header_labels('TableChart_2','Rows',expected_header,expected_label,"Step 28:a(iii):")
        resultobj.verify_number_of_riser("TableChart_2", 1, 9, 'Step 28.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar!r2!c0!", "bar_blue", "Step 28.c: Verify bar color")
#         tooltip_val=['Store Country:United States', 'Product Category:Media Player', 'Revenue:$123,949,415.80', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
#         resultobj.verify_default_tooltip_values('TableChart_2','riser!s0!g1!mbar!r2!c0!',tooltip_val,"Step 28.d: Verify output value")
        time.sleep(3)
        
        parent_css="#TableChart_1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 3,expire_time=50)
        
        iaresultobj.verify_number_of_chart_segment("TableChart_1",3, 'Step 28.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mregion!", "persian_red", "Step 28.f: Verify first bar color")
        legend=['Revenue', '10.4M', '63.2M', '116.1M', '169M', '222M']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step28.g: Verify legend Title")
        time.sleep(3)
#         expected_tooltip=['Store Country:Brazil', 'Revenue:$10,357,820.49', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
#         resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mregion!",expected_tooltip, "Step 28.h: verify the default tooltip values")       
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(2, 'Computers', verify=True, verify_type=True, msg="Step28.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(2, 'Media Player', verify=True, verify_type=True, msg="Step28.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(2, 'Televisions', verify=True, verify_type=True, msg="Step28.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Brazil', verify=True, verify_type=True, msg="Step28.4: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Canada', verify=True, verify_type=True, msg="Step28.5: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'United States', verify=True, verify_type=True, msg="Step28.6: Verify values is checked in filter prompt", scroll_down=True)
        time.sleep(5)
        
        """
        Step 29: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()