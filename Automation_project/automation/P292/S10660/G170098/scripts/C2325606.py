'''
Created on Oct 11, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325606
TestCase Name = Verify Parameter Drill Down with default Bar chart
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_run
from common.lib import utillity, core_utility
from common.wftools import visualization

class C2325606_TestClass(BaseTestCase):

    def test_C2325606(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID_1 = 'C2325606_base'
        Test_Case_ID = 'C2325606'

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_obj= core_utility.CoreUtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        visualobj=visualization.Visualization(self.driver)
        """
        Step 01: Launch the IA API with wf_retail_lite, Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element('#TableChart_1', 1, visualobj.chart_long_timesleep)
               
        """
        Step02: Double-click "Cost of Goods", located under Sales Measures
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeWindow', 'Cost of Goods', visualobj.chart_long_timesleep)
         
        """
        Step 3: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeWindow', 'Product,Category', visualobj.chart_long_timesleep)
         
        """
        Step 4: Select "Cost of Goods" in the Query pane > Click on "Drill Down" button in the Ribbon
        """
        metaobj.querytree_field_click("Cost of Goods", 1)
        parent_css="#FieldDrillDown img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, visualobj.chart_long_timesleep)
        ribbon_item=utillobj.validate_and_get_webdriver_object("#FieldDrillDown img", "Drill down")
        core_obj.left_click(ribbon_item)
           
        """
        Step 5: Click "Browse" button > Select "C2325606_rpt"
        Step 6: Click on the rename button above "Drill Down 1"
        Step 7: Type "Parameter Drill Down" in the Description area
        Step 8: Click on the Add Parameter button
        Step 9: Select Name dropdown > Select PRODUCT_CATEGORY
        Step 10: Select Type:Field
        Step 11: Select Value:Product,Category > Click OK
        Step 12: Click OK
        """
        parent_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        utillobj.synchronize_with_number_of_element(parent_css, 1, visualobj.chart_long_timesleep)
        iaribbonobj.create_drilldown_report('report', browse_file_name='C2325606_base', rename_drilldown=True, set_description="Parameter Drill Down", set_ampersand='add')        
        iaribbonobj.drilldown_parameter_popup(name_select = "PRODUCT_CATEGORY", type_select = "Field", value_select = "Product,Category", popup_close='ok')
        iaribbonobj.create_drilldown_report('report', click_ok=True)
             
        """
        Step 13: Hover over "Computers" riser > Verify drill down to "Parameter Drill Down" is displayed in the pop up menu
        """
        time.sleep(10)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 13.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 13.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 13.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.04: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Parameter Drill Down']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step 13.05: Verify drill down to 'Parameter Drill Down' is displayed in the pop up menu")
        time.sleep(5)
           
        """
        Step 14: Select "Parameter Drill Down" from the pop up menu
        """
        time.sleep(5)
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g2!mbar", 'Parameter Drill Down')
        time.sleep(8)
           
        """
        Step 15: Verify Report with output only for "Smartphone" and "Tablet" is displayed in a new window (or tab)
        """
        core_obj.switch_to_new_window(current_browser_window_title = Test_Case_ID_1)
        time.sleep(10)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx", 'Step 15.00: Verify Report with output only for "Smartphone" and "Tablet" is displayed in a new window (or tab)')
#         ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx")
        time.sleep(5)
           
        """
        Step 16: Close the output window
        """
        core_obj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element('#applicationButton img', 1, visualobj.chart_long_timesleep)
           
        """
        Step 17: Click "Save" in the toolbar > Save As "C2325606" > Click "Save"
        """
        utillobj.synchronize_with_number_of_element('#TableChart_1', 1, visualobj.chart_long_timesleep)
        ribbonobj.select_visualization_top_toolbar_item('save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
           
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step 19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2325606.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_2',mrid='mrid',mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css,7,visualobj.chart_long_timesleep)
        
        """
        Step 20: Hover over "Computers" riser > Verify drill down to "Parameter Drill Down" is displayed in the pop up menu
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 20.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 20.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 20.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 20.04: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Parameter Drill Down']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step 20.05: Verify drill down to 'Parameter Drill Down' is displayed in the pop up menu")
        time.sleep(5)
        
        """
        Step21: Click "Run" in the toolbar
        """
        ribbonobj.select_visualization_top_toolbar_item('run')
        core_obj.switch_to_new_window()
                  
        """
        Step 22: Hover over "Media Player" riser > Verify drill down to "Parameter Drill Down" is displayed in the pop up menu
        """
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css,7,visualobj.chart_long_timesleep)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 22.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 22.01: Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 22.02:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 22.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 22.04: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory', 'Parameter Drill Down']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar,"Step 22.05: Verify drill down to 'Parameter Drill Down' is displayed in the pop up menu")
        
        """
        Step 23: Select "Parameter Drill Down" from the pop up menu
        """
        visualobj.select_tooltip("riser!s0!g3!mbar",'Parameter Drill Down',parent_css='MAINTABLE_wbody1')
       
        """
        Step 24: Verify Report with only Media Player related subcategories is displayed in a new window (or tab)
        """
        time.sleep(10)
        core_obj.switch_to_new_window() 
        utillobj.synchronize_with_visble_text('table[summary="Summary"]','Cost of Goods', visualobj.chart_long_timesleep)          
#         ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds02.xlsx", 'Step 24.00: Verify Report with only Media Player related subcategories is displayed in a new window (or tab)')
        core_obj.switch_to_previous_window()
    
        """
        Step 25: Close output window
        """
        core_obj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element('#applicationButton img',1,visualobj.chart_long_timesleep)

        """
        Step 26: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()        