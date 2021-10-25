'''
Created on Dec 22, 2017

@author: BM13368
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/tests/view/14045879
TestCase Name: Verify Style Dialog with series color (82xx)
'''
import unittest, time
from common.lib import utillity,core_utility 
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_styling

class C2228160_TestClass(BaseTestCase):

    def test_C2228160(self):
        
        """
            COMMON TEST CASE VARIABLES 
        """
        Test_Case_ID = "C2228160"
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        expected_color = 'url("#pfjTableChart_1__lineargradient_0_0_100p_0_0_255255255_1_1_128128128_1")'
        expected_color1 = 'url("#jschart_HOLD_0__lineargradient_0_0_100p_0_0_255255255_1_1_128128128_1")'
        
        """
            CLASS OBJECTS 
        """
        driver = self.driver
        ia_styling_obj=ia_styling.IA_Style(driver)
        utillobj = utillity.UtillityMethods(driver)
        core_utils = core_utility.CoreUtillityMethods(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
            
        """
            Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/EMPLOYEE
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02:Double click "LAST_NAME", "CURR_SAL", "SALARY".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeWindow', "LAST_NAME", 30)
#         time.sleep(4)
        
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeWindow', "CURR_SAL", 30)
#         time.sleep(4)
        
        metaobj.datatree_field_click("SALARY", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
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
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
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
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        
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
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
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
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        """  
            Step 17:Verify "SALARY" series in "Live Preview" has gradient fill.
        """
        time.sleep(4)
        elem = utillobj.validate_and_get_webdriver_object("#pfjTableChart_1 rect[class='riser!s1!g1!mbar!']", 'bar color')
        actual_color= utillobj.get_element_css_propery(elem, 'fill')
        utillobj.asequal(actual_color, expected_color, "Step 17.01: Verify bar color in the created chart")
#         ia_result_obj.verify_stop_color("#TableChart_1 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']","fill",['white','Trolley_Grey'],"Step 17:01:Verify bar color in the created chart")
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
        core_utils.switch_to_frame()
        parent_css="#jschart_HOLD_0 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
        
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
        time.sleep(4)
        elem = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class='riser!s1!g1!mbar!']", 'bar color')
        actual_color = utillobj.get_element_css_propery(elem, 'fill')
        utillobj.asequal(actual_color, expected_color1, "Step 19.05: Verify bar color in the created chart")
#         ia_result_obj.verify_stop_color("#jschart_HOLD_0 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']", "fill", ['white','Trolley_Grey'], "Step 19:05: Verify gradient color is present in the second bar")
        time.sleep(1)
        expected_tooltip_list=['LAST_NAME:MCKNIGHT', 'SALARY:$31,100.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g7!mbar!", expected_tooltip_list, "Step 19:06:Verify tooltip value")
        utillobj.verify_chart_color("jschart_HOLD_0 svg>g.chartPanel g.groupPanel", "riser!s0!g0!mbar!", "red", "Step 19:07: Verify first bar color")
        utillobj.switch_to_default_content(pause=1)
        """ 
            Step 20:Click Save in the toolbar > Save as "C2228160" > Click Save
            Step 21:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
            
        """
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        utillobj.infoassist_api_logout()
        time.sleep(4)
        """  
            Step 22:Run from bip
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228160.fex
        """ 
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="#jschart_HOLD_0 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
           
        """ 
            Step 23:Verify the following chart is displayed.
        """ 
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 23:01: X and Y axis labels')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 22, 'Step 23:02: Verify Number chart segment')
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'LAST_NAME', "Step 23:03: Verify X-Axis Title")
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 23:04: Verify legen3ds in the created chart")
        time.sleep(4)
        elem = utillobj.validate_and_get_webdriver_object("#jschart_HOLD_0 rect[class='riser!s1!g1!mbar!']", 'bar color')
        actual_color = utillobj.get_element_css_propery(elem, 'fill')
        utillobj.asequal(actual_color, expected_color1, "Step 23.05: Verify bar color in the created chart")
#         ia_result_obj.verify_stop_color("#jschart_HOLD_0 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']", "fill", ['white','Trolley_Grey'], "Step 25:05: Verify gradient color is present in the second bar")
        time.sleep(1)
        expected_tooltip_list=['LAST_NAME:MCKNIGHT', 'SALARY:$31,100.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g7!mbar!", expected_tooltip_list, "Step 23:06:Verify tooltip value")
        time.sleep(0.5)
        utillobj.verify_chart_color("jschart_HOLD_0 svg>g.chartPanel g.groupPanel", "riser!s0!g0!mbar!", "red", "Step 23:07: Verify first bar color")
          
        """  
            Step 24:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout() 
        time.sleep(4) 
        """  
            Step 25:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228160.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 22, 65)
        
        """  
            Step 26:Verify IA is launched preserving the chart in "Live Preview".
        """
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 25:01: X and Y axis labels')
        resultobj.verify_number_of_riser('TableChart_1', 1, 22, 'Step 25:02: Verify Number chart segment')
        expected_legend_list=['CURR_SAL','SALARY']
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 25:03: Verify X-Axis Title")
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 25:04: Verify legends in the created chart")
        time.sleep(4)
        elem = utillobj.validate_and_get_webdriver_object("#pfjTableChart_1 rect[class='riser!s1!g1!mbar!']", 'bar color')
        actual_color = utillobj.get_element_css_propery(elem, 'fill')
        utillobj.asequal(actual_color, expected_color, "Step 25.05: Verify bar color in the created chart")
#         ia_result_obj.verify_stop_color("#TableChart_1 svg>g.chartPanel g.groupPanel [class='riser!s1!g0!mbar!']", "fill", ['white','Trolley_Grey'], "Step 28:05: Verify gradient color is present in the second bar")
        utillobj.verify_chart_color("TableChart_1 svg>g.chartPanel g.groupPanel", "riser!s0!g0!mbar!", "red", "Step 25:06: Verify first bar color")
        
        """ 
            Step 27:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()