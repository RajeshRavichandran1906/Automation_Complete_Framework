'''
Created on Dec 27, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228167
TestCase Name = Verify HTML5 Bevel effect on the Bar edges(82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2228167_TestClass(BaseTestCase):

    def test_C2228167(self):
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228167'
        Test_Case_saveas_ID ="IA-VAL-CHART-002"
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch WF, New > Chart with GGSALES.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P292/S10032_chart_1', 'mrid', 'mrpass')
        time.sleep(5)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)

        """
        Step 02: Click on "Theme" (Report Grouping).
        """
        ribbonobj.select_ribbon_item('Home', 'Theme')
        time.sleep(3)
        parent_css="#IbfsOpenFileDialog7_btnOK"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 03: Select "Dark.sty" template.
        Step 04: Click "Open".
        """
        utillobj.ibfs_save_as("Dark.sty")
        
        """
        Step 05: Double click "Product", "Unit Sales".
        """
        time.sleep(3)
        metaobj.datatree_field_click('Product', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
         
        metaobj.datatree_field_click('Unit Sales', 2, 1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        
        """
        Step 06: Verify the following chart is displayed with the theme applied.
        """
        xaxis_value="Product"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step06:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step06:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step06.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "dark_orange1", "Step 06.c: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "background", "nero", "Step 06.d: Verify background color")
        time.sleep(5)
        
        """
        Step 07: Click "Run".
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        
        """
        Step 08: Verify the following chart is displayed.
        """
        time.sleep(6)
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 10)
        time.sleep(5)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step08:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "dark_orange1", "Step 08.c: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "background", "nero", "Step 08.d: Verify background color")
        
        """
        Step 09: Hover over any bar to see tooltip information is displayed for the selected bar.
        """
        time.sleep(5)
        bar=['Product:Croissant', 'Unit Sales:630054']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g4!mbar", bar,"Step 09: Verify bar value")
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 10: Click "IA" > "Save".
        Step 11: Enter Title = "IA-VAL-CHART-002".
        Step 12: Click "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_saveas_ID)
        time.sleep(10)
           
        """
        Step 13: Click "IA" > "Exit".
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 14: Locate the saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_saveas_ID+'.fex','S10032_chart_1','mrid','mrpass')
        time.sleep(10) 
        
        """
        Step 15: Verify the saved fex can be executed and output is the same chart that was displayed on "Live Preview".
        """
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 10)
        time.sleep(5)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step15:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step015:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "dark_orange1", "Step 15.c: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "background", "nero", "Step 15.d: Verify background color")
        time.sleep(5)
        bar=['Product:Croissant', 'Unit Sales:630054']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g4!mbar", bar,"Step 15.e: Verify bar value")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 16: Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_saveas_ID, 'idis', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 17: Verify that it launches IA tool and display the chart on "Live Preview".
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 17:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 17:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "dark_orange1", "Step 17.c: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "background", "nero", "Step 17.d: Verify background color")
        
        """
        Step 18: Click "IA" > "Exit".
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()