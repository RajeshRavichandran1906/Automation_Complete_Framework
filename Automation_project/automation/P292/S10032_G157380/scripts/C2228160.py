'''
Created on Dec 22, 2017

@author: BM13368
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/tests/view/14045879
TestCase Name: Verify Style Dialog with series color (82xx)
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_styling, ia_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2228160_TestClass(BaseTestCase):

    def test_C2228160(self):
        
        Test_Case_ID1 = "IA-VAL-CHART-009"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_styling_obj=ia_styling.IA_Style(driver)
        ia_result_obj=ia_resultarea.IA_Resultarea(driver)
        
        """
            Step 01:Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10660_chart_1', 'mrid', 'mrpass')
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02:Double click "LAST_NAME", "CURR_SAL", "SALARY".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("SALARY", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resultobj.wait_for_property(parent_css, 1)
        
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 22, 'Step 02.03: Verify Number chart segment')
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 02:04: Verify X-Axis Title")
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 02:05: Verify legends in the created chart")
        
        """  
            Step 03:Select "Series" tab.
        """
        ribbonobj.switch_ia_tab("Series")
        time.sleep(0.5)
        
        """
            Step 04:Click "All Series" (dropdown) in "Select" group.
            Step 05:Select "Series 0 - CURR_SAL" from the list.
        """
        elem=driver.find_element_by_css_selector("#SeriesChartSelect")
        utillobj.select_any_combobox_item(elem, "Series 0 - CURR_SAL")
        
#         utillobj.select_or_verify_bipop_menu("Series 0 - CURR_SAL")
        """  
            Step 06:Click "Style" in the ribbon.
        """
        ribbonobj.select_ribbon_item("Series", "Style")
        parent_css="div[id^='QbDialog'] [class*='active window'] [class*='caption']"
        resultobj.wait_for_property(parent_css, 1)
        elem_obj=driver.find_element_by_css_selector("#seriesFillColorBtn")
        utillobj.click_on_screen(elem_obj, "middle", click_type=0,pause=0.50) 
        """ 
            Step 07:Click "Color" icon.
            Step 08:Select Red and click "OK".
        """ 
        ia_styling_obj.set_color('red')  
         
        """  
            Step 09:Click "OK".
        """
        elem_obj=driver.find_element_by_css_selector("#BiColorPickerOkBtn")
        utillobj.click_on_screen(elem_obj, "middle", click_type=0,pause=0.50)
        
        """  
            Step 10:Click "OK" in the "Format Series" window.
        """
        elem_obj=driver.find_element_by_css_selector("#seriesGradientOkBtn")
        utillobj.click_on_screen(elem_obj, "middle", click_type=0,pause=0.50)
        
        """  
            Step 11:Verify "CURR_SAL" series in "Live Preview" is red.
        """
        parent_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        resultobj.wait_for_property(parent_css, 1) 
        utillobj.verify_chart_color("TableChart_1","riser!s0!g0!mbar!","red","Step 11:01:Verify first bar colour")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 11:02: Verify second bar color")
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 11:03: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "red", "Step 11:04: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 22, 'Step 11:04: Verify Number chart segment')
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 11:05: Verify X-Axis Title")
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 11:06: Verify legends in the created chart")
        
        
        """ 
            Step 12:In Select group, click "Series 0 - CURR_SAL" (dropdown).
        """
        ribbonobj.switch_ia_tab("Series")
        
        """  
            Step 13:Select "Series 1 - SALARY".
        """
        elem=driver.find_element_by_css_selector("#SeriesChartSelect")
        utillobj.select_any_combobox_item(elem, "Series 1 - SALARY")
        """  
            Step 14:Click "Style" in the ribbon.
        """
        ribbonobj.select_ribbon_item("Series", "Style")
        parent_css="div[id^='QbDialog'] [class*='active window'] [class*='caption']"
        resultobj.wait_for_property(parent_css, 1)
        
        """  
            Step 15:Select "Gradient fill" radio button.
        """
        elem_obj=driver.find_element_by_css_selector("#rightPane #gradientFillRadioBtn")
        utillobj.click_on_screen(elem_obj, "middle", click_type=0,pause=0.50)
        """ 
            Step 16:Click "OK" in the "Format Series" window.
        """
        elem_obj=driver.find_element_by_css_selector("#seriesGradientOkBtn")
        utillobj.click_on_screen(elem_obj, "middle", click_type=0,pause=0.50)
        parent_css="#TableChart_1 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 17:Verify "SALARY" series in "Live Preview" has gradient fill.
        """
        ia_result_obj.verify_stop_color("#TableChart_1 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']","fill",['white','Trolley_Grey'],"Step 17:01:Verify bar color in the created chart")
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 17:03: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1 svg>g.chartPanel g.groupPanel", "riser!s0!g0!mbar!", "red", "Step 17:04: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 22, 'Step 17:05: Verify Number chart segment')
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 17:06: Verify X-Axis Title")
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 17:07: Verify legends in the created chart")

        
        """ 
            Step 18:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(2)
        parent_css="#jschart_HOLD_0 [class='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 19:Verify the chart displayed is the same as in "Live Preview".
        """
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 19:01: X and Y axis labels')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 22, 'Step 19:02: Verify Number chart segment')
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'LAST_NAME', "Step 19:03: Verify X-Axis Title")
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 19:04: Verify legen3ds in the created chart")
        ia_result_obj.verify_stop_color("#jschart_HOLD_0 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']", "fill", ['white','Trolley_Grey'], "Step 19:05: Verify gradient color is present in the second bar")
        time.sleep(1)
        expected_tooltip_list=['LAST_NAME:MCKNIGHT', 'SALARY:$31,100.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g7!mbar!", expected_tooltip_list, "Step 19:06:Verify tooltip value")
        utillobj.verify_chart_color("jschart_HOLD_0 svg>g.chartPanel g.groupPanel", "riser!s0!g0!mbar!", "red", "Step 19:07: Verify first bar color")
        utillobj.switch_to_default_content(pause=1)
        """ 
            Step 20:Click "IA" > "Save".
            Step 21:Enter Title = "IA-VAL-CHART-015".
            Step 22:Click "Save".
        """
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID1)
        time.sleep(5)
        
        """   
            Step 23:Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        """  
            Step 24:Locate the saved fex > Right mouse click > "Run".
        """ 
        utillobj.active_run_fex_api_login(Test_Case_ID1+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="#jschart_HOLD_0 [class='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css,1)   
        """ 
            Step 25:Verify the following chart is displayed.
        """ 
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 25:01: X and Y axis labels')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 22, 'Step 25:02: Verify Number chart segment')
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'LAST_NAME', "Step 25:03: Verify X-Axis Title")
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 25:04: Verify legen3ds in the created chart")
        ia_result_obj.verify_stop_color("#jschart_HOLD_0 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']", "fill", ['white','Trolley_Grey'], "Step 25:05: Verify gradient color is present in the second bar")
        time.sleep(1)
        expected_tooltip_list=['LAST_NAME:MCKNIGHT', 'SALARY:$31,100.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g7!mbar!", expected_tooltip_list, "Step 25:06:Verify tooltip value")
        time.sleep(0.5)
        utillobj.verify_chart_color("jschart_HOLD_0 svg>g.chartPanel g.groupPanel", "riser!s0!g0!mbar!", "red", "Step 25:07: Verify first bar color")
          
        """  
            Step 26:Dismiss the chart run window.
        """
        utillobj.infoassist_api_logout()  
        """  
            Step 27:Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID1, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 28:Verify IA is launched preserving the chart in "Live Preview".
        """
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 28:01: X and Y axis labels')
        resultobj.verify_number_of_riser('TableChart_1', 1, 22, 'Step 28:02: Verify Number chart segment')
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 28:03: Verify X-Axis Title")
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 28:04: Verify legends in the created chart")
        ia_result_obj.verify_stop_color("#TableChart_1 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']", "fill", ['white','Trolley_Grey'], "Step 28:05: Verify gradient color is present in the second bar")
        utillobj.verify_chart_color("TableChart_1 svg>g.chartPanel g.groupPanel", "riser!s0!g0!mbar!", "red", "Step 28:06: Verify first bar color")
        
        """ 
            Step 29:Click "IA" > "Exit".
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()