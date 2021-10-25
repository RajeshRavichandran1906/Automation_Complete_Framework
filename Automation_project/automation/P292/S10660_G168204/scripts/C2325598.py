'''
Created on Oct 9, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325598
TestCase Name = Verify Drill Down to Procedure with default Bar chart
'''

import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2325598_TestClass(BaseTestCase):

    def test_C2325598(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID_1 = 'C2325598_rpt'
        Test_Case_ID = 'C2325598'

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
#         ia_resultobj.create_report_data_set('TableChart_1', 21, 2, Test_Case_ID_1+"_Ds01.xlsx",no_of_cells=4)
        ia_resultobj.verify_report_data_set('TableChart_1', 21, 2, Test_Case_ID_1+"_Ds01.xlsx", 'Step 3: Verify report dataset', no_of_cells=4)
             
        """
        Step04: Click "Save" in the toolbar > Save As "C2325598_rpt" > Click "Save"
        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID_1)
        time.sleep(5)
             
        """
        Step05: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step06: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
           
        """
        Step07: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1) 
                       
        """
        Step08: Double-click "Product,Category", located under Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
           
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step08: Verify bar value")
        time.sleep(5)
           
        """
        Step09: Select "Cost of Goods" in the Query pane > Click on "Drill Down" button in the Ribbon
        """
        metaobj.querytree_field_click("Cost of Goods", 1)
        time.sleep(5)
        parent_css="#FieldDrillDown img"
        resultobj.wait_for_property(parent_css, 1)
        ribbon_item=driver.find_element_by_css_selector("#FieldDrillDown img")
        utillobj.default_left_click(object_locator=ribbon_item)
           
        """
        Step10: Click "Browse" button > Select "C2325598_rpt"
        Step11: Click OK
        """
        time.sleep(8)
        parent_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        resultobj.wait_for_property(parent_css, 1)
        iaribbonobj.create_drilldown_report('report', browse_file_name='C2325598_rpt', click_ok=True)
         
# 
#         utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_2',mrid='mrid',mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)

        """
        Step12: Hover over "Computers" riser > Verify drill down to "C2325598_rpt" is displayed in the pop up menu
        """
        time.sleep(10)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step12.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'C2325598_rpt']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step12: Verify drill down to 'C2325598_rpt' is displayed in the pop up menu")
        time.sleep(5)
        
        """
        Step13: Select "C2325598_rpt" from the pop up menu
        """
        time.sleep(5)
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g2!mbar", 'C2325598_rpt')
        time.sleep(10)
        
        """
        Step14: Verify Report is displayed in a new window (or tab)
        """
        utillobj.switch_to_window(1,window_title=Test_Case_ID_1)
        time.sleep(10)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx", 'Step 14: Verify Report is displayed in a new window')
#         ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx")
        time.sleep(5)
        
        """
        Step15: Close the output winow
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step16: Click "Run" in the toolbar
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)                 
        time.sleep(15)
                  
        """
        Step17: Hover over "Media Player" riser > Verify drill down to "C2325598_rpt" is displayed in the pop up menu
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step17:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step17.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'C2325598_rpt']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step17: Verify drill down to 'C2325598_rpt' is displayed in the pop up menu")
        
        """
        Step18: Select "C2325598_rpt" from the pop up menu
        """
        time.sleep(5)
        wind_handle=driver.window_handles 
        print(wind_handle)       
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g2!mbar", 'C2325598_rpt')
        wind_handle1=driver.window_handles 
        time.sleep(5)
        print(wind_handle1)
        
        """
        Step19: Verify Report is displayed in a new window (or tab)
        """
        time.sleep(10)
        utillobj.switch_to_window(2, custom_windows=wind_handle, window_title=Test_Case_ID_1)                 
        time.sleep(15)
#         ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds02.xlsx", 'Step 19: Verify Report is displayed in a new window')
        time.sleep(10)
        wind_handle=driver.window_handles 
        print(wind_handle) 
        self.driver.close()
        wind_handle=driver.window_handles 
        print(wind_handle) 
        time.sleep(10)
        utillobj.switch_to_window(1,win_num=1)                 
        time.sleep(15)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step19', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step 20: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
            
        """
        Step 21: Click "Save" in the toolbar > Save As "C2325598" > Click "Save"
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
            
        """
        Step 22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()