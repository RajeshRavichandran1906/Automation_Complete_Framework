'''
Created on Nov 16, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2208040
Testcase Name=AHTML:Changing CHART measures field from SUM to PRINT terminates the request during run time (ACT-598)

'''
import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous

class C2308040_TestClass(BaseTestCase):

    def test_C2308040(self):
        
        """
            CLASS & OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 01:Create chart from IA using ggsales master file
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7072', 'mrid', 'mrpass')
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 65)
        
        """
        Step 02:Change output format to Active Reports        
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        element_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        """
        Step 03:Add category product and unit sales.     
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        queryTree ="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(queryTree, 'Category', 15)
        
        metadataobj.datatree_field_click('Product', 2, 1)
        utillobj.synchronize_with_visble_text(queryTree, 'Product', 15)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        utillobj.synchronize_with_visble_text(queryTree, 'Unit Sales', 15)

        """
        Step 04:From Query pane from source chart eg:Chart(ggsales) right click it
        Step 05:By default it is set to SUM and change that to Print
        Step 06:Run the chart.
        Step 07:Verify chart runs properly during run time.        
        """
        metadataobj.querytree_field_click("Chart (ggsales)",1,1,"Print")
        utillobj.synchronize_with_number_of_element("#TableChart_1 svg g.risers >g>rect[class^='riser']", 500, 35)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 15)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 rect[class*='riser']", 4317, 45)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 07.01 : Verify chart title ")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 4317, 'Step 07.02: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g10!mbar!", "bar_blue1", "Step 07.03: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product","Step 07.04: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 07.05: Verify yaxis title")
        expected_tooltip_list=['Category:Coffee', 'Product:Capuccino', 'Unit Sales:1763', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g10!mbar!", expected_tooltip_list, "Step 07.06: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Detail'],"Step 07.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=2)
          
if __name__ == '__main__':
    unittest.main()     