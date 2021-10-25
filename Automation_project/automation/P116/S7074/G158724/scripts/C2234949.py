'''
Created on JUN 22, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234949
TestCase Name = Verify Tree Map in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,ia_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2234949_TestClass(BaseTestCase):

    def test_C2234949(self):
        
        Test_Case_ID="C2234949"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES From Home tab Select Active Report as Output file format.
            Select Format > Other >HTML 5 and Select Treemap.
        """  
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(4)  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        ribbonobj.select_ribbon_item('Format', 'Other')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resobj._validate_page(elem1)
        ia_ribbobj.select_other_chart_type('html5', 'tree_map', 5, ok_btn_click=True)
        time.sleep(3)
        """
            Step 02:Add fields Product ID under Category and Double click  (will get added under Measures and Size)
        """
        metadataobj.datatree_field_click('Category', 2, 0)
        parent_css="#TableChart_1 g.chartPanel g text[class]"
        resobj.wait_for_property(parent_css, 1, string_value='Coffee', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product ID', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1,string_value='ProductID', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(4)
        utillobj.verify_chart_color('TableChart_1', 'riser!sCoffee-_-C141!g0!mnode', 'bar_blue1', 'Step 02.1:  Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 02.2: Expect to see the Series Selection',custom_css =".chartPanel g rect[class*='riser!s']")
        expected_datalabel=['Coffee', 'C141', 'C144']
        resobj.verify_data_labels("TableChart_1", expected_datalabel, 'Step 02.3: Verify riser datalabels', custom_css="g.chartPanel g text[fill='black']")
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['C141', 'C144'], "Step 02.4:",custom_css="text[class*='dataLabels']",same_group=True)
        """
            Step 03:Click run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!sFood-_-F102!g0!mnode", "bar_blue", "Step 03.1: Verify first bar color")
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['F103', 'F102', 'F101', 'C142', 'C141', 'C144', 'G100', 'G121', 'G104', 'G110'], "Step 03.2:",custom_css="text[class*='dataLabels']",same_group=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 03.3: Verify number of tree map", custom_css=".chartPanel g rect[class*='riser!s']")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product ID', 'Step 03.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_datalabel=['Food', 'Coffee', 'Gifts', 'F103', 'F102', 'F101', 'C142', 'C141', 'C144', 'G100', 'G121', 'G104', 'G110']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, 'Step 03.8: Verify riser datalabels', custom_css="svg g.chartPanel g text")
        """
        Step 04:Hover over C144 block.
        """
        expected_tooltip_list=['Category:Coffee', 'Product ID:C144', 'Unit Sales:189217', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!sCoffee-_-C144!g0!mnode", expected_tooltip_list, "Step 04: Verify bar value") 
        time.sleep(7)
        utillobj.switch_to_default_content(pause=5)
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
        
        
    