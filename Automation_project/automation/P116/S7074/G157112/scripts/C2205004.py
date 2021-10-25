'''
Created on Jul 26, 2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2205004
TestCase Name = AHTML:Stylesheet is not reflected in scatter plot(137111)

'''
import unittest
import time
from selenium.webdriver.support.color import Color
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon, active_chart_rollup
from common.lib import utillity


class C2205004_TestClass(BaseTestCase):

    def test_C2205004(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2205004'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollup_obj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step 01: Using infoassist, Create a new chart using the CAR master file.
                 Add Country as X-axis and Sales as measure (SUM)
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(2)
        metadataobj.datatree_field_click('COUNTRY', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="COUNTRY")
        metadataobj.datatree_field_click('SALES', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="SALES")
        expected_xval_list=['ENGLAND', 'FRANCE','ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 1a: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 5, 'Step 1b: ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 1c: Verify bar color")
        
        """
        Step 02 : Change the output format to AHTML
        """
        ribbonobj.change_output_format_type('active_report')
        time.sleep(4)       
        
        """
        Step 03 : Click on theme icon under report tab and select legacy temaplate
        Step 04 : Select "ENInformationBuilders_DarkComp.sty" and click apply
        """
        ribbonobj.select_theme('Legacy Templates', 'ENInformationBuilders_DarkComp.sty')
        time.sleep(6) 
        
        """
        Step 05 : Run the report. 
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 g.risers>g>rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 5)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY", "Step 05a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","SALES", "Step 05b: Verify Y-Axis Title")
        expected_xval_list=['ENGLAND', 'FRANCE','ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 05d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'blue_endeavour', 'Step 05e: Verify bar Color')
        expected_tooltip_list=['COUNTRY:ENGLAND', 'SALES:12000', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 05f: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES by COUNTRY', 'Step 05g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_frame_color=utillobj.color_picker('grey_mischka', 'rgba')
        actual_frame_color = Color.from_string(self.driver.find_element_by_css_selector("#MAINTABLE_0 svg g.chartPanel rect.chartFrame").value_of_css_property('fill')).rgba
        utillobj.asequal(expected_frame_color, actual_frame_color, "Step 05k(i): Verify Chart Frame color")
        expected_backgrnd_color=utillobj.color_picker('fun_blue', 'rgba')
        actual_backgrnd_color = Color.from_string(self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 svg>g>rect.background").value_of_css_property('fill')).rgba
        utillobj.asequal(expected_backgrnd_color, actual_backgrnd_color, "Step 05k(ii): Verify Chart Background color")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=5)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        
        """
        Step 06 : Select scatter icon in chart Rollup tool
        """
        rollup_obj.click_pivot_menu_bar_items('MAINTABLE_wmenu0', 1)
        rollup_obj.select_advance_chart('wall1', 'scatter(xy_plot)')
        time.sleep(5)
        
        """
        Step 07 : Verify that applied stylesheet has been reflected in the scatter plots
        """
        parent_css="#MAINTABLE_wbody0 circle[class^='riser']"
        result_obj.wait_for_property(parent_css, 5)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY", "Step 07a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","SALES", "Step 07b: Verify Y-Axis Title")
        expected_xval_list=['ENGLAND', 'FRANCE','ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 07c: ')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['SALES'],'Step 07d: Verify chart legend label')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mmarker!", 'blue_endeavour', 'Step 07e: Verify bar Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES by COUNTRY', 'Step 07f: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07g: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07h: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07i: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_frame_color=utillobj.color_picker('grey_mischka', 'rgba')
        actual_frame_color = Color.from_string(self.driver.find_element_by_css_selector("#MAINTABLE_0 svg g.chartPanel rect.chartFrame").value_of_css_property('fill')).rgba
        utillobj.asequal(expected_frame_color, actual_frame_color, "Step 07j: Verify Chart Frame color")
        expected_backgrnd_color=utillobj.color_picker('fun_blue', 'rgba')
        actual_backgrnd_color = Color.from_string(self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 svg>g>rect.background").value_of_css_property('fill')).rgba
        utillobj.asequal(expected_backgrnd_color, actual_backgrnd_color, "Step 07k: Verify Chart Background color")
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__=='__main__' :
    unittest.main()