'''
Created on Jan 24, 2018
TestSuite Name :8201M Baseline 
TestSuite ID :http://172.19.2.180/testrail/index.php?/suites/view/10851&group_by=cases:section_id&group_order=asc&group_id=175059
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2358911
TestCase Name :AHTML:Document:Applying style color to the chart is not reflected during run time (ACT-630)
@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_styling, ia_resultarea
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException

class C2358911_TestClass(BaseTestCase):

    def test_C2358911(self):
        
        """ TESTCASE VARIABLES """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_styling_obj=ia_styling.IA_Style(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        
        """
            Step 01:Launch IA to develop a Document
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 80)
        """
            Step 02:Select 'GGSales' as master file, and change output format as Active report.
        """
        format_type=self.driver.find_element_by_css_selector("#HomeFormatType").text
        expected_format_type='Active Report'
        utillobj.asequal(expected_format_type, format_type, "Step 02:Verify output format shows Active Report bydefault")
        """
            Step 03:Choose 'Chart' from 'Insert' tab, then add fields eg: Product and Dollar Sales to get a chart.
        """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_1 svg g.risers >g>rect[class^='riser']", 25, 20)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class^='xaxis'][class$='title']",'Product',20)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 text[class^='xaxis'][class$='title']", 1, 20)
        
        """
            Verify the chart
        """
        resultobj.verify_yaxis_title("TableChart_1", 'Dollar Sales', "Step 03:01: Verify Y-axis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'Product', "Step 03:02: Verify X-axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 03:03: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M','4M']
        expected_xval_list=['Capuccino', 'Espresso']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 03:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 03:05: Verify first bar color")
        
        """
            Step 04:Right click the chart in live preview and select More Style options
        """
        try:
            elem=self.driver.find_element_by_css_selector("#TableChart_1 rect[class='riser!s0!g1!mbar!']")
            core_utillobj.left_click(elem)
        except NoSuchElementException :
            raise AttributeError("{0} the given table chart element is not added in the page".format(elem))
        time.sleep(5)
            
        ia_resultobj.right_click_on_barchart("#TableChart_1", "rect[class='riser!s0!g1!mbar!']")
        time.sleep(1)
        bipopup_css="div[id^='BiPopup'][style*='inherit']"
        utillobj.synchronize_with_number_of_element(bipopup_css, 1, 25)
        utillobj.select_or_verify_bipop_menu("More Style Options...")
        utillobj.synchronize_with_number_of_element("div[id^='QbDialog'] [class*='active'] [class*='window'][class*='caption']", 1, 15)
        
        """
            Step 05:Select Solid Fill and change the color option eg: Red Color
            Step 06:Click apply button and check the changes reflected in live preview and execute the report.
        """
        
        elem_obj=self.driver.find_element_by_css_selector("#fillPane #seriesFillColorBtn img")
        core_utillobj.left_click(elem_obj)
        ok_btn_css="#seriesGradientOkBtn"
        utillobj.synchronize_with_number_of_element(ok_btn_css, 1, 20)
        ia_styling_obj.set_color('red')
        elem_ok_obj=self.driver.find_element_by_css_selector(ok_btn_css)
        core_utillobj.left_click(elem_ok_obj)
        
        """
            Step 07:Verify the changed color is reflected during run time
        """
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "red", "Step 07:01: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "red", "Step 07:02: Verify first bar color")


if __name__ == "__main__":
    unittest.main()