'''
Created on Dec 22, 2017

@author: BM13368
TestCase Name : Verify Frame Dialog:Set Frame Color,add transparency,Set Gradient Background color (82xx)
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2228158
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_styling, ia_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.color import Color

class C2228158_TestClass(BaseTestCase):

    def test_C2228158(self):
        
        Test_Case_ID1 = "IA-VAL-CHART-009"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_styling_obj=ia_styling.IA_Style(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        ia_result_obj=ia_resultarea.IA_Resultarea(driver)
        
        """
            Step 01:Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10660_chart_1', 'mrid', 'mrpass')
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 02:Double click on "LAST_NAME", "SALARY".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resultobj.wait_for_property(parent_css, 1)
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 02.03: Verify Number chart segment')
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 02:04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'CURR_SAL', "Step 02:05: Verify Y-Axis Title")
        """  
            Step 03:Click "Format" tab.
            Step 04:Expand Features group (if not already expanded).
            Step 05:Click on "Frame & Background".
        """
        ribbonobj.select_ribbon_item("Format", "frame_and_background")
        time.sleep(0.5)
        
        """  
            Step 06:Verify the following window
        """
        parent_css="div[id^='QbDialog'] [class*='active window'] [class*='caption']"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 07:Select "Solid fill" radio button
        """
        ia_ribbon_obj.set_format_frame_and_background('radiobutton','solid_fill', None)
        """ 
            Step 08:Click on "Color" picker icon.
            Step 09:Select Yellow and click "OK".
        """
        ia_ribbon_obj.set_format_frame_and_background('styleimage_objects','style_button', None)
        ia_styling_obj.set_color('yellow') 
        elem_ok=driver.find_element_by_css_selector("#BiColorPickerOkBtn")
        utillobj.click_on_screen(elem_ok, "middle", click_type=0, pause=0.50) 
            
        """  
            Step 10:Slide "Transparency" glider to 50%.
        """
        ia_ribbon_obj.set_format_frame_and_background('textbox','depth_radius','50')
        """  
            Step 11:Click "OK".
        """
        elem_ok=driver.find_element_by_css_selector("#frameOkBtn")
        utillobj.click_on_screen(elem_ok, "middle", click_type=0, pause=0.50)
        
        """  
            Step 12:Verify the background color change is applied to the chart in "Live Preview".
        """
        elem="#TableChart_1 .chartPanel .chartFrame"
        resultobj.wait_for_property(elem, 1)
        expected_font_color=utillobj.color_picker('yellow', 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#TableChart_1 .chartPanel .chartFrame").get_attribute("fill")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Step 12:01: Verify chart backgroudn color is displayed in yellow color")
        """ 
            Step 13:Click "Frame & Background" in "Format" tab.
        """
        ribbonobj.select_ribbon_item("Format", "frame_and_background")
        time.sleep(0.5)
        """  
            Step 14:Select the "Gradient fill" radio button.
        """
        ia_ribbon_obj.set_format_frame_and_background('radiobutton','gradient_fill', None)
        """  
            Step 15:Click "OK".
        """
        elem_ok=driver.find_element_by_css_selector("#frameOkBtn")
        utillobj.click_on_screen(elem_ok, "middle", click_type=0, pause=0.50)
        """  
            Step 16:Verify the chart background in "Live Preview" has gradient fill.
        """
        elem_obj="#TableChart_1 svg>g>g>g .chartFrame"
        resultobj.wait_for_property(elem_obj, 1)
        ia_result_obj.verify_stop_color("#TableChart_1 svg>g>g>g .chartFrame", "fill", ['white','Trolley_Grey'], "Step 16:01: Verify chart background in livepreview has gradient fill")
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 16:02: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 16:03: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 16:04: Verify Number chart segment')
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 16:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'CURR_SAL', "Step 16:06: Verify Y-Axis Title")
        time.sleep(1)
        """ 
            Step 17:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(2)
        parent_css="#jschart_HOLD_0 svg>g>g>g .chartFrame"
        resultobj.wait_for_property(parent_css, 1)
        
        """  
            Step 18:Verify the chart displayed is that same as in "Live Preview".
        """
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 18:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 18:02: Verify first bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 11, 'Step 18:03: Verify Number chart segment')
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'LAST_NAME', "Step 18:04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'CURR_SAL', "Step 18:05: Verify Y-Axis Title")
        time.sleep(1)
        expected_tooltip_list=['LAST_NAME:BANNING', 'CURR_SAL:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 18:06:Verify tooltip value")
        ia_result_obj.verify_stop_color("#jschart_HOLD_0 svg>g>g>g .chartFrame", "fill", ['white','Trolley_Grey'], "Step 18:07: Verify chart background in livepreview has gradient fill")
        """  
            Step 19:Click "IA" > "Save".
            Step 20:Enter Title = "IA-VAL-CHART-009".
            Step 21:Click "Save" and dismiss IA.
        """
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID1)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        """  
            Step 22:Locate the saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_ID1+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="#jschart_HOLD_0 svg>g>g>g .chartFrame"
        resultobj.wait_for_property(parent_css,1)
        """  
            Step 23:Verify the chart displayed is the correct.
        """
        ia_result_obj.verify_stop_color("#jschart_HOLD_0 svg>g>g>g .chartFrame", "fill", ['white','Trolley_Grey'], "Step 23:01: Verify chart background in livepreview has gradient fill")
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 23:02: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 23:03: Verify first bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 11, 'Step 23:04: Verify Number chart segment')
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'LAST_NAME', "Step 23:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'CURR_SAL', "Step 23:06: Verify Y-Axis Title")
        time.sleep(1)
        expected_tooltip_list=['LAST_NAME:BANNING', 'CURR_SAL:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 23:07:Verify tooltip value")
        ia_result_obj.verify_stop_color("#jschart_HOLD_0 svg>g>g>g .chartFrame", "fill", ['white','Trolley_Grey'], "Step 23:08: Verify chart background in livepreview has gradient fill")
        """ 
            Step 24:Dismiss the chart run window.
        """
        utillobj.infoassist_api_logout()
        """  
            Step 25:Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID1, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 26:Verify IA is launched with the correct chart displayed in "Live Preview".
        """
        elem_obj="#TableChart_1 svg>g>g>g .chartFrame"
        resultobj.wait_for_property(elem_obj, 1)
        ia_result_obj.verify_stop_color("#TableChart_1 svg>g>g>g .chartFrame", "fill", ['white','Trolley_Grey'], "Step 26:01: Verify chart background in livepreview has gradient fill")
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 26:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 26:02: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 26:03: Verify Number chart segment')
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 26:04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'CURR_SAL', "Step 26:56: Verify Y-Axis Title")
        time.sleep(1)
        """ 
            Step 27:Click "IA" > "Exit".
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()