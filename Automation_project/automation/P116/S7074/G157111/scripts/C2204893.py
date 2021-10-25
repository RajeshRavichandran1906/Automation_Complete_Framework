'''
Created on JUN 01, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204893
TestCase Name = Verify that applied Angle and Radius are reflected in the output
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon
from common.lib import utillity

class C2204893_TestClass(BaseTestCase):

    def test_C2204893(self):
        
        Test_Case_ID="C2204893"
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

        """
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
            On the Format tab, in the Output Types group, click Active report/Active PDF.
            Add Category into Horizontal Axis and Unit Sales and Dollar sales into Vertical axis.        
        """  
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        time.sleep(6)
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 03.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M','6M', '7M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 03.2: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 04.e: Verify  bar color")
        """
            step 02:Right click on Chart frame, and select "More Frame & Background Option
        """
        parent_css="#TableChart_1 .chartPanel .groupPanel"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        utillobj.click_type_using_pyautogui(parent_obj, cord_type='start', leftClick=True)
        time.sleep(5)
        utillobj.click_type_using_pyautogui(parent_obj,cord_type='start', rightClick=True)
        utillobj.select_or_verify_bipop_menu('More Frame & Background Options...')
        time.sleep(2)
        ribbon_obj.select_frame_background_options('Frame', depth_angle='100', depth_radius='75', btnOk=True)
        """
            Step 03:Check the Angle and Radius are reflected
        """
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 03.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M','6M', '7M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 03.2: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 04.e: Verify  bar color", custom_css=".chartPanel .groupPanel .risers rect[fill='#5388be']")
        """
            Step 04:click run.       
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(8)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 04.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee','Food','Gifts']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 04.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 04.4: Verify  bar color", custom_css=".chartPanel .groupPanel .risers rect[fill='#5388be']")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category', 'Step 04.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step4', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()