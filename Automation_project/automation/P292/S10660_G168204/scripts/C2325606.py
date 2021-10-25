'''
Created on Oct 11, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325606
TestCase Name = Verify Parameter Drill Down with default Bar chart
'''

import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2325606_TestClass(BaseTestCase):

    def test_C2325606(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID_1 = 'C2325606_rpt'
        Test_Case_ID = 'C2325606'

        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('report','new_retail/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
             
        """
        Step02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
                         
        """
        Step03: Double-click "Product,Subcategory", located under Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(4)
        coln_list = ['ProductSubcategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 3.1: Verify report title")
        ia_resultobj.create_report_data_set('TableChart_1', 21, 2, Test_Case_ID_1+"_Ds01.xlsx",no_of_cells=4)
#         ia_resultobj.verify_report_data_set('TableChart_1', 21, 2, Test_Case_ID_1+"_Ds01.xlsx", 'Step 3: Verify report dataset', no_of_cells=4)
          
        """
        Step04: Drag "Product,Category" from Data pane into the Filter pane
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category',1, 1, 'Filter')
        time.sleep(4)
          
        """
        Step05: Select Type:Parameter
        Step06: Click OK, OK
        """
        elem=(By.CSS_SELECTOR,'#dlgWhere')
        resultobj._validate_page(elem)
        iaribbonobj.create_parameter_filter_condition('Simple', 'parameter')
          
        """
        Step07: Click "Save" in the toolbar > Save As "C2325606_rpt" > Click "Save"
        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID_1)
        time.sleep(5)
             
        """
        Step08: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
           
        """
        Step09: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
           
        """
        Step10: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1) 
                       
        """
        Step11: Double-click "Product,Category", located under Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
           
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step11:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step11.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step11: Verify bar value")
        time.sleep(5)
           
        """
        Step12: Select "Cost of Goods" in the Query pane > Click on "Drill Down" button in the Ribbon
        """
        metaobj.querytree_field_click("Cost of Goods", 1)
        time.sleep(5)
        parent_css="#FieldDrillDown img"
        resultobj.wait_for_property(parent_css, 1)
        ribbon_item=driver.find_element_by_css_selector("#FieldDrillDown img")
        utillobj.default_left_click(object_locator=ribbon_item)
         
        """
        Step13: Click "Browse" button > Select "C2325606_rpt"
        Step14: Click on the rename button above "Drill Down 1"
        Step15: Type "Parameter Drill Down" in the Description area
        Step16: Click on the Add Parameter button
        Step17: Select Name dropdown > Select PRODUCT_CATEGORY
        Step18: Select Type:Field
        Step19: Select Value:Product,Category > Click OK
        Step20: Click OK
        """
        time.sleep(8)
        parent_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        resultobj.wait_for_property(parent_css, 1)
        iaribbonobj.create_drilldown_report('report', browse_file_name='C2325606_rpt', rename_drilldown=True, set_description="Parameter Drill Down", set_ampersand='add', name_select='PRODUCT_CATEGORY', type_select='Field', value_select='Product,Category', popup_close='ok', click_ok=True)        
         
        """
        Step21: Hover over "Computers" riser > Verify drill down to "Parameter Drill Down" is displayed in the pop up menu
        """
        time.sleep(10)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step21:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step21:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step21:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step21.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step21.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Parameter Drill Down']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step21: Verify drill down to 'Parameter Drill Down' is displayed in the pop up menu")
        time.sleep(5)
         
        """
        Step22: Select "Parameter Drill Down" from the pop up menu
        """
        time.sleep(5)
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g2!mbar", 'Parameter Drill Down')
        time.sleep(8)
         
        """
        Step23: Verify Report with output only for "Smartphone" and "Tablet" is displayed in a new window (or tab)
        """
        utillobj.switch_to_window(1, window_title=Test_Case_ID_1)
        time.sleep(10)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx", 'Step23: Verify Report with output only for "Smartphone" and "Tablet" is displayed in a new window (or tab)')
#         ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx")
        time.sleep(5)
         
        """
        Step24: Close the output winow
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step25: Click "Save" in the toolbar > Save As "C2325606" > Click "Save"
        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """
        Step26: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step27: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2325606.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step28: Hover over "Computers" riser > Verify drill down to "Parameter Drill Down" is displayed in the pop up menu
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step28:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step28:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step28:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step28.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step28.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Parameter Drill Down']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step28: Verify drill down to 'Parameter Drill Down' is displayed in the pop up menu")
        time.sleep(5)
        
        """
        Step29: Click "Run" in the toolbar
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)                 
        time.sleep(15)
                  
        """
        Step30: Hover over "Media Player" riser > Verify drill down to "Parameter Drill Down" is displayed in the pop up menu
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step30:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step30:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step30:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step30.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step30.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Parameter Drill Down']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step30: Verify drill down to 'Parameter Drill Down' is displayed in the pop up menu")
        
        """
        Step31: Select "Parameter Drill Down" from the pop up menu
        """
        time.sleep(5)
        wind_handle=driver.window_handles 
        print(wind_handle)       
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g3!mbar", 'Parameter Drill Down')
        wind_handle1=driver.window_handles 
        time.sleep(5)
        print(wind_handle1)
        
        """
        Step32: Verify Report with only Media Player related subcategories is displayed in a new window (or tab)
        """
        time.sleep(10)
        utillobj.switch_to_window(2, custom_windows=wind_handle, window_title=Test_Case_ID_1)                 
        time.sleep(15)
#         ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds02.xlsx", 'Step 32: Verify Report with only Media Player related subcategories is displayed in a new window (or tab)')
        time.sleep(8)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(1,win_num=1)                 
        time.sleep(15)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step32', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step33: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
    
        """
        Step34: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()        
