'''
Created on Jul 04, 2017
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_styling,ia_ribbon
from common.lib import utillity


class C2316895_TestClass(BaseTestCase):

    def test_C2316895(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2316895'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_stylingobj = ia_styling.IA_Style(driver)
        ribbon_obj = ia_ribbon.IA_Ribbon(driver)
        """    1. Right click on folder created in IA and select New > Chart. Select Reporting server as GGSALES. On the Format tab, in the Output Types group, click Active report/Active PDF.    """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        
        """    2. Add Category to the Horizontal axis. Add Unit Sales to Vertical axis.    """
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Category")
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Unit Sales")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2a: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 1, 'Step 2b: ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 2c: Verify bar color")
        
        """    3. Right click on Chart frame, and select "More Frame & Background Option"    """
        elem=driver.find_element_by_id("TableChart_1")
        utillobj.click_on_screen(elem, coordinate_type='start', click_type=1, x_offset=100, y_offset=50)
        utillobj.select_or_verify_bipop_menu('More Frame & Background Options...')
        time.sleep(5)
        
        """    4. Select Gradient fill, then select 'Radial Pie inverted' for 'Direction.     """
        
        ribbon_obj.select_frame_background_options('Frame', gradient_fill=True, direction='Radial pie inverted', btnOk=True)
        time.sleep(5)               
         
        """    5. Click OK. Click the Run button.    """

        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 3)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Category", "Step 05a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 05b: Verify Y-Axis Title")
        expected_xval_list=['Coffee','Food', 'Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 3, 'Step 05d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", 'bar_blue', 'Step 05e: Verify bar Color')
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 05f: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category', 'Step 05g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_stylingobj.verify_Gradient_fill_bgcolor("MAINTABLE_wbody0", 'Trolley_Grey', 'white', 'Step 05k')
        utillobj.switch_to_default_content(pause=5)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
    
    
    