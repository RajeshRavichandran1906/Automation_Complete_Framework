'''
Created on JUN 05, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204894
TestCase Name = Verify that Gradient right fill is applied in the output
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon, ia_styling
from common.lib import utillity

class C2204894_TestClass(BaseTestCase):

    def test_C2204894(self):
        
        Test_Case_ID="C2204894"
        """
            TESTCASE VARIABLES
        """   
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ribbon_obj = ia_ribbon.IA_Ribbon(driver)
        ia_stylingobj = ia_styling.IA_Style(driver)
        """
            Step 01:Right click on folder created in IA and 
            select New > Chart.Select Reporting server as GGSALES. On the Format tab, in the Output Types group, click Active report/Active PDF.        
        """  
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """
            Step 02:Right click on Category in Data window and select 
            Add to Query/Horizontal axis. Add "Unit Sales" to Vertical axis.
        """
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(3)
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 02.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K','600K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 1, 'Step 02.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02.4: Verify  bar color")
        """
            step 03:Right click on Chart frame, and select "More Frame & Background Option.
        """
        elem=driver.find_element_by_id("TableChart_1")
        utillobj.click_on_screen(elem, coordinate_type='start', click_type=1, x_offset=100, y_offset=50)
        utillobj.select_or_verify_bipop_menu('More Frame & Background Options...')
        time.sleep(5)
        """   
            Step 04. Select Gradient fill, then select 'Gradient right' for 'Direction.
        """
        ribbon_obj.select_frame_background_options('Frame', gradient_fill=True, direction='Gradient right', btnOk=True)
        """
            Step 05:click run.       
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 04.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.2: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee','Food','Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 3, 'Step 05.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 05.5: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category', 'Step 05.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.10: Verify bar value")
        ia_stylingobj.verify_Gradient_fill_bgcolor("MAINTABLE_wbody0", 'white', 'Trolley_Grey', 'Step 5.11')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
