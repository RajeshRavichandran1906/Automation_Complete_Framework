'''
Created on May 11, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227633
TestCase Name = Filter using 'Values' in the Data pane under decomposed dates
'''

import unittest,time
import pyautogui
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from pyautogui import click
from selenium.webdriver import ActionChains

class C2227633_TestClass(BaseTestCase):

    def test_C2227633(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227633'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
            
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
             
        """
        Step 03: Expand Dimension "Product" > Double click "Product,Category"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
            
        """
        Step 04: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > "Values" > "2014" > 
        Drag and drop "2014 Q2" into the Filter pane
        """
        time.sleep(3)
        obj_cell_css = driver.find_element_by_css_selector("#iaMetaDataBrowser img[src*='search_cancel']")
        utillobj.default_left_click(object_locator=obj_cell_css)
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(6)
        metaobj.expand_field_tree('Sales_Related')
        time.sleep(2)
        metaobj.expand_field_tree('Sales_Related')
        time.sleep(2)
        metaobj.expand_field_tree('Transaction Date, Components')
        time.sleep(2)
        metaobj.expand_field_tree('Values')
        time.sleep(6)
        metaobj.expand_field_tree('2014')
        time.sleep(6)
        metaobj.expand_field_tree('2014 Q2', click_opt=1, x_offset=35)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Filter')
        time.sleep(6)
        """
        Step05: Right-click "Sale,Year/Quarter" filter in the Filter pane > select "Edit..."
        """ 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.filter_tree_field_click("Sale,Year/Quarter", 1, 1,"Edit...")
        
        """
        Step06: Verify dialog
        Step07: Check off values "2014 Q3", "2014 Q4", "2015 Q1", "2015 Q2"> Click OK
        """ 
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        print(d)
        print(d['text'])
        utillobj.asequal(d['text'],'Equal to',"Step06.a: Verify operator in Filter dialog")
        l=['2014 Q2']
        metaobj.select_or_verify_visualization_filter_values(l, verify='true', msg = 'Step06.b: Verify dialog 2014 Q2 is checked')
        time.sleep(5)         
        item_list2=['2014 Q4']
        metaobj.select_or_verify_visualization_filter_values(item_list2)
        time.sleep(1)
        item_list3=['2015 Q1']
        metaobj.select_or_verify_visualization_filter_values(item_list3)
        time.sleep(1)
        item_list4=['2015 Q2']
        metaobj.select_or_verify_visualization_filter_values(item_list4)
        time.sleep(8)         
        item_list1=['2014 Q3']
        metaobj.select_or_verify_visualization_filter_values(item_list1, Ok_button=True)
        
        """
        Step 08: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step08:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c: Verify first bar color")
        resultobj.verify_riser_legends("MAINTABLE_wbody1",  ['Cost of Goods','Gross Profit'],"Step 08: Verify Chart Legend")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$42,277,661.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar, "Step 08: Verify bar value")
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q2', verify=True, verify_type=True, msg="Step08: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q3', verify=True, verify_type=True, msg="Step08: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q4', verify=True, verify_type=True, msg="Step08: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2015 Q1', verify=True, verify_type=True, msg="Step08: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2015 Q2', verify=True, verify_type=True, msg="Step08: Verify true is checked in filter prompt")
             
        """
        Step 09: Click Save in the toolbar
        Step 10: Save as "C2158208" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """
        Step 11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step 12: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
          
        """
        Step 13: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step23:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.c: Verify first bar color")
        resultobj.verify_riser_legends("MAINTABLE_wbody1",  ['Cost of Goods','Gross Profit'],"Step 13: Verify Chart Legend")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$42,277,661.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar, "Step 13: Verify bar value")
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q2', verify=True, verify_type=True, msg="Step13: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q3', verify=True, verify_type=True, msg="Step13: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q4', verify=True, verify_type=True, msg="Step13: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2015 Q1', verify=True, verify_type=True, msg="Step13: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2015 Q2', verify=True, verify_type=True, msg="Step13: Verify true is checked in filter prompt")
        time.sleep(5)
        
        """
        Step14: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 15: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8) 
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 15:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.c: Verify first bar color")
        resultobj.verify_riser_legends("MAINTABLE_wbody1",  ['Cost of Goods','Gross Profit'],"Step 15: Verify Chart Legend")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$42,277,661.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar, "Step 15.d: Verify bar value")
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q2', verify=True, verify_type=True, msg="Step15: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q3', verify=True, verify_type=True, msg="Step15: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2014 Q4', verify=True, verify_type=True, msg="Step15: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2015 Q1', verify=True, verify_type=True, msg="Step15: Verify true is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '2015 Q2', verify=True, verify_type=True, msg="Step15: Verify true is checked in filter prompt")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227633_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 16: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
#     def expand_field_tree_right_click(self, folder_path,**kwargs):
#         utillobj = utillity.UtillityMethods(self.driver)
#         Datatree_rows = "#iaMetaDataBrowser div[id^='QbMetaDataTree']>.bi-tree-view-body-content tr"
#         click_opt=kwargs['click_opt'] if 'click_opt' in kwargs else 0
#         folder_list=folder_path.split('->')
#         for item in folder_list:
#             datetree_items = self.driver.find_elements_by_css_selector(Datatree_rows)
#             for i in range(len(datetree_items)-1):
#                 folder_img = datetree_items[i].find_element_by_css_selector("td>img")
#                 img_src=folder_img.get_attribute("src")
#                 if datetree_items[i].text.strip() == item and ('path_arrow_tree_closed' in img_src or 'blank_icon' in img_src):
#                     try:
#                         print("inside try")
#                         datetree_items = self.driver.find_elements_by_css_selector(Datatree_rows)
#                         time.sleep(2)
#                         obj_cell_css=datetree_items[i].find_element_by_css_selector("td>img")
#                         browser=utillobj.parseinitfile('browser')
#                         if browser == "Firefox":
#                             utillobj.click_on_screen(self, obj_cell_css, coordinate_type='middle',click_type=click_opt,**kwargs)
#                         else:
#                             action1 = ActionChains(self.driver)
#                             action1.context_click(obj_cell_css).perform()
#                         time.sleep(1)
#                         break
#                     except:
#                         print("except")
#                         datetree_items = self.driver.find_elements_by_css_selector(Datatree_rows)
#                         obj_cell_css=datetree_items[i].find_element_by_css_selector("td>img")
#                         browser=utillobj.parseinitfile('browser')
#                         if browser == "Firefox":
#                             utillobj.click_on_screen(self, obj_cell_css, coordinate_type='middle',click_type=click_opt,**kwargs)
#                         else:
#                             action1 = ActionChains(self.driver)
#                             action1.context_click(obj_cell_css).perform()
#                         time.sleep(1)
#                         break
            
if __name__ == '__main__':
    unittest.main()