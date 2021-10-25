'''
Created on Dec 21, 2017

@author: BM13368
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2228157 
TestCase Name :Verify Gridline dialog with Bar chart (82xx)
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_styling
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.color import Color

class C2228157_TestClass(BaseTestCase):

    def test_C2228157(self):
        
        Test_Case_ID = "C2228157"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_styling_obj=ia_styling.IA_Style(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
        css variables
        """
        grid_types_css = ".bi-menu"
        
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10660_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """  
            Step 02:Double click "LAST_NAME", "SALARY".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        time.sleep(4)
        
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        time.sleep(4)
        
        """
            Preview Chart
        """
        parent_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 40)
        expected_yval_list = ['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 02.03: Verify Number chart segment')
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 02:04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'CURR_SAL', "Step 02:05: Verify Y-Axis Title")
        time.sleep(1)
        
        """  
            Step 03:Click on "Format" tab.
            Step 04:Expand the "Features" group.
            Step 05:Click "Grid" (dropdown).
        """
        ribbonobj.select_ribbon_item("Format", "Grid")
        utillobj.synchronize_until_element_is_visible(grid_types_css, metaobj.home_page_short_timesleep)
        
        """
            Step 06:Go to "Horizontal Gridlines" > "More Grid Lines Options...".
        """
        utillobj.select_or_verify_bipop_menu("Horizontal Gridlines")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("More Grid Lines Options...")
        time.sleep(2)
        parent_css="div[id^='QbDialog'] [class*='active window'] [class*='caption']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        """    
            Step 07:Check "Show Grid Lines".
        """
        ia_ribbon_obj.set_format_horizontal_grid_lines_major('checkbox','show_grid_lines','uncheck')
        
        """  
            Step 08:Click "OK".
        """
        elem_ok=driver.find_element_by_css_selector("#gridLineOkBtn")
        utillobj.default_click(elem_ok, click_option=0)
        
        """    
            Step 09:Verify horizontal grid lines on the chart.
        """
        elem_css="#TableChart_1 [class='yaxis-majorGrid']"
        utillobj.synchronize_with_number_of_element(elem_css, 1, 30)
        
        expected_font_color=utillobj.color_picker("whisper", 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#TableChart_1 [class='yaxis-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Verify text color of ") 

        """ 
            Step 10:Click "Grid" (dropdown).
        """
        ribbonobj.select_ribbon_item("Format", "Grid")
        utillobj.synchronize_until_element_is_visible(grid_types_css, metaobj.home_page_medium_timesleep)
        """  
            Step 11:Go to "Vertical Gridlines" > "More Grid Lines Options...".
        """
        utillobj.select_or_verify_bipop_menu("Vertical Gridlines")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("More Grid Lines Options...")
        time.sleep(2)
        parent_css="div[id^='QbDialog'] [class*='active window'] [class*='caption']"
        
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 12:Check "Show Grid Lines".
        """
        ia_ribbon_obj.set_format_vertical_grid_lines_major('checkbox','show_grid_lines','uncheck')

        
        """  
            Step 13:Click on the "Line Style" icon.
        """
        ia_ribbon_obj.set_format_vertical_grid_lines_major('styleimage_objects','style_button_1', None)
        """ 
            Step 14:Click on "Color" button within Line Style dialog.
        """
        parent_css="#lineStyleDlg [class*='active'] [class*='caption']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 25)
        
        line_color_elem=driver.find_element_by_css_selector("#lineStyleDlg #lineStyleColorBtn")
        utillobj.click_on_screen(line_color_elem, "middle", click_type=0, pause=0.75)
        """  
            Step 15:Select Red and click "OK".
        """
        ia_styling_obj.set_color('red')
        
        """
            Step 16:Click "Weight" dropdown > "2px - Medium".
        """
        elem_weight=driver.find_element_by_css_selector("#lineStyleDlg #lineStyleWeightBtn")
        utillobj.click_on_screen(elem_weight, "middle",click_type=0,pause=0.75)
        utillobj.select_or_verify_bipop_menu("2px - Medium")
         
        """  
            Step 17:Click "Style" (dropdown) > "Dashed".
        """
        elem_style=driver.find_element_by_css_selector("#lineStyleDlg #lineStyleBtn")
        utillobj.click_on_screen(elem_style, "middle", click_type=0,pause=0.75)
        utillobj.select_or_verify_bipop_menu("Dashed")
#         utillobj.click_on_screen(elem_style, "middle", click_type=0,pause=0.75)
        
        """  
            Step 18:Click "OK".
        """
        elem_ok=driver.find_element_by_css_selector("#lineStyleDlg #lineStyleApplyBtn")
        utillobj.click_on_screen(elem_ok, "middle", click_type=0, pause=0.50)
        """  
            Step 19:Click "OK" in the Format Vertical Grid Lines window.
        """
        elem_ok=driver.find_element_by_css_selector("#gridLineOkBtn")
        utillobj.click_on_screen(elem_ok, "middle", click_type=0, pause=0.75)
        """  
            Step 20:Verify the chart in "Live Preview" displays the following chart:
        """
        parent_css="#TableChart_1 [class='xaxisOrdinal-majorGrid']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        expected_font_color=utillobj.color_picker('red', 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#TableChart_1 [class='xaxisOrdinal-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Step 20: Verify grid line is applied in the created chart")
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 20:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 20:02: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 20.03: Verify Number chart segment')
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 20:04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'CURR_SAL', "Step 20:05: Verify Y-Axis Title")
        time.sleep(1)
        
        """ 
            Step 21:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(2)
        parent_css="#jschart_HOLD_0 [class='xaxisOrdinal-majorGrid']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """  
            Step 22:Verify the same chart is displayed as in "Live Preview".
        """
        expected_font_color=utillobj.color_picker("red", 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#jschart_HOLD_0 [class='xaxisOrdinal-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Verify text color of vertical grid")
        
        expected_font_color=utillobj.color_picker("whisper", 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#jschart_HOLD_0 [class='yaxis-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Verify text color of vertical grid")
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 22:03: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 22:04: Verify first bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 11, 'Step 22:04: Verify Number chart segment')
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'LAST_NAME', "Step 22:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'CURR_SAL', "Step 22:06: Verify Y-Axis Title")
        time.sleep(1)
        expected_tooltip_list=['LAST_NAME:BANNING', 'CURR_SAL:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 22:07:Verify tooltip value")
        utillobj.switch_to_default_content(pause=1)
        
        """ 
            Step 23:Click Save in the toolbar > Save as "C2228157" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """  
            Step 24:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        """  
            Step 25:Run from bip
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228157.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="#jschart_HOLD_0 [class='xaxisOrdinal-majorGrid']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        """  
            Step 26:Verify the same chart is displayed.
        """
        expected_font_color=utillobj.color_picker("red", 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#jschart_HOLD_0 [class='xaxisOrdinal-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Step 28:01:Verify color of vertical grid")
        
        expected_font_color=utillobj.color_picker("whisper", 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#jschart_HOLD_0 [class='yaxis-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Step 28:02:Verify color of horizontal grid")
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 28:03: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue", "Step 28:04: Verify first bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 11, 'Step 28:04: Verify Number chart segment')
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'LAST_NAME', "Step 28:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'CURR_SAL', "Step 28:06: Verify Y-Axis Title")
        
        """ 
            Step 27:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        """  
            Step 28:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228157.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 65)
        
        """  
            Step 29:Verify IA is launched and the grid lines changes are preserved "in Live Preview"..
        """
        expected_font_color=utillobj.color_picker("red", 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#TableChart_1 [class='xaxisOrdinal-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Step 31:01Verify color of vertical grid")
        
        expected_font_color=utillobj.color_picker("whisper", 'rgba')
        actual_font_color=Color.from_string(driver.find_element_by_css_selector("#TableChart_1 [class='yaxis-majorGrid']").get_attribute("stroke")).rgba
        utillobj.asequal(expected_font_color, actual_font_color, "Step 31:02:Verify color of horizontal grid")
        
        expected_yval_list=['0','5K','10K','15K','20K','25K','30K','35K']
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 31:03: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue", "Step 31:04: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 31:04: Verify Number chart segment')
        resultobj.verify_xaxis_title("TableChart_1", 'LAST_NAME', "Step 31:05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'CURR_SAL', "Step 31:06: Verify Y-Axis Title")
        """ 
            Step 30:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()