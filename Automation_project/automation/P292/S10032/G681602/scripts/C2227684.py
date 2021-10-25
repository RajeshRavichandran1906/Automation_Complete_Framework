'''
Created on Mar 31, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227684
Test case Name =  Change Filter Operator from Range to Equals - verify List of Values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By
from datetime import datetime


class C2227684_TestClass(BaseTestCase):

    def test_C2227684(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227684'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        time.sleep(5)
        metaobj.datatree_field_click("Cost of Goods",2,1)
         
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        time.sleep(5)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click("Product,Category", 2, 1)
         
        """
        Step 04: Drag and drop "Cost of Goods" to the Filter pane
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.drag_drop_data_tree_items_to_filter("Cost of Goods", 1) 
 
        """
        Step 05: Click "Operator" dropdown box > select "Equal to"
        Step 06: Verify dialog
        Step 07: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 06.a: Verify dialog') 
        time.sleep(2)
        item_list=['[All]']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', msg = 'step06.b: Verify dialog')
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
         
        """
        Step 08: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step08:")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 08: Verify bar value")
        time.sleep(5)
         
        """
        Step09: Select values $16.00 through $50.00 in the Filter Prompt
        """
        time.sleep(8)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
#         item_list=['$16.00', '$23.00', '$32.00', '$34.00', '$36.00', '$42.00', '$45.00', '$46.00', '$48.00', '$50.00']
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00')
        time.sleep(1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00')
        time.sleep(1)
        print(str(datetime.now()))
         
        """
        Step 10: Verify Canvas
        """
        time.sleep(8)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step10:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$1,896,614.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 10.d: Verify bar value")
        time.sleep(5)
#         item_list=['$16.00', '$23.00', '$32.00', '$34.00', '$36.00', '$42.00', '$45.00', '$46.00', '$48.00', '$50.00']
#         propertyobj.select_or_verify_show_prompt_item(1, item_list, verify=True, verify_type=True, msg="Step10.e: Verify values is checked in filter prompt")        
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00', verify=True, verify_type=True, msg="Step10.1: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00', verify=True, verify_type=True, msg="Step10.2: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00', verify=True, verify_type=True, msg="Step10.3: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step10.4: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step10.5: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step10.6: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step10.7: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step10.8: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step10.9: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step10.10: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        time.sleep(5)
         
        """
        Step11: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
          
        """
        Step 12: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$1,896,614.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 12.d: Verify bar value")
        time.sleep(5)
#         item_list=['$16.00', '$23.00', '$32.00', '$34.00', '$36.00', '$42.00', '$45.00', '$46.00', '$48.00', '$50.00']
#         propertyobj.select_or_verify_show_prompt_item(1, item_list, verify=True, verify_type=True, msg="Step12.e: Verify values is checked in filter prompt")        
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00', verify=True, verify_type=True, msg="Step12.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00', verify=True, verify_type=True, msg="Step12.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00', verify=True, verify_type=True, msg="Step12.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step12.4: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step12.5: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step12.6: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step12.7: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step12.8: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step12.9: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step12.10: Verify values is checked in filter prompt")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227684_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1) 
         
        """
        Step 13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
          
        """
        Step 14: Click Save in the toolbar
        Step 15: Save as "C2158215" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
          
        """
        Step 16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step 17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
         
        """
        Step 18: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step18:")
        time.sleep(6)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 18:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 18:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 18.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$1,896,614.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 18.d: Verify bar value")
        time.sleep(5)
#         item_list=['$16.00', '$23.00', '$32.00', '$34.00', '$36.00', '$42.00', '$45.00', '$46.00', '$48.00', '$50.00']
#         propertyobj.select_or_verify_show_prompt_item(1, item_list, verify=True, verify_type=True, msg="Step18.e: Verify values is checked in filter prompt")        
        propertyobj.select_or_verify_show_prompt_item(1, '$16.00', verify=True, verify_type=True, msg="Step18.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$23.00', verify=True, verify_type=True, msg="Step18.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$32.00', verify=True, verify_type=True, msg="Step18.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step18.4: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step18.5: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step18.6: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step18.7: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step18.8: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step18.9: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step18.10: Verify values is checked in filter prompt")
        time.sleep(5)
        
        """
        Step 19: Right click "Cost of Goods" filter in the Filter pane > Edit
        Step 20: Verify dialog
        Step 21: Deselect values $16.00, $23.00 and $32.00 > Click OK
        """
        metaobj.filter_tree_field_click('Cost of Goods',1,1,'Edit...')
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(5)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 20: Verify dialog') 
        time.sleep(8)
        item_list=['$16.00', '$23.00', '$32.00']
#         metaobj.create_visualization_filters('numeric',['GridItems',item_list])
        metaobj.select_or_verify_visualization_filter_values(item_list, Ok_button=True)
        time.sleep(20)
        
        """
        Step 22: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step22:")
        time.sleep(3)
        propertyobj.select_or_verify_show_prompt_item(1, '$34.00', verify=True, verify_type=True, msg="Step22.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$36.00', verify=True, verify_type=True, msg="Step22.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$42.00', verify=True, verify_type=True, msg="Step22.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$45.00', verify=True, verify_type=True, msg="Step22.4: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$46.00', verify=True, verify_type=True, msg="Step22.5: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$48.00', verify=True, verify_type=True, msg="Step22.6: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$50.00', verify=True, verify_type=True, msg="Step22.7: Verify values is checked in filter prompt")
        time.sleep(5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 22:a(ii) Verify Y-Axis Title")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels!m1!']"
        resultobj.wait_for_property(parent_css, 1, string_value='0.3M', with_regular_exprestion=True)
        expected_xval_list=['Accessories', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 22:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 22.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 22.c: Verify first bar color")
        time.sleep(10)
        bar=['Product Category:Accessories', 'Cost of Goods:$591,166.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 22.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 23: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()