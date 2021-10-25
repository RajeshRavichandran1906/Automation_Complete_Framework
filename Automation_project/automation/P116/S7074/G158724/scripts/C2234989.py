'''
Created on JUL 18, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234989
TestCase Name = Verify PIE in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon,ia_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2234989_TestClass(BaseTestCase):

    def test_C2234989(self):
        
        Test_Case_ID="C2234989"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        """
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
            Select Active Report as the output format. 
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)    
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        
        """
            Step 02: Right click on Category in Data window and select "Add to Query/Horizontal axis".
            Right click on Unit Sales in Data window and select "Add to Query/Vertical axis".     
        """  
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 02.01: Verify -yAxis Title")
        time.sleep(1)
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 02.02: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K','600K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.03: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 1, 'Step 02.04: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 02.05: Verify  bar color")
        
        """
            Step 03:Run the report    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 03.01: Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 03.02: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.03: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 3, 'Step 03.04: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 03.05: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category', 'Step 03.06: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expectedtooltip_list=['Category:Coffee', 'Unit Sales:1376266', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", 'riser!s0!g0!mbar', expectedtooltip_list, "Step 03.10: Verify bar value")
        
        """
            Step 04:Select Format > Other, Switch to Pie on Others tab and verify available pie types
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ribbonobj.select_ribbon_item('Format', 'Other')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resobj._validate_page(elem1)
        ia_ribbonobj.select_other_chart_type('pie', 'pie', 1)
        time.sleep(1)
        expected_visible=['Pie_Pie', 'Pie_Ring', 'Pie_Multi', 'Pie_Multi_Ring']
        ia_ribbonobj.verify_check_visible_chart_list(expected_visible, 'Step 04.01: Verify it shows 4 different Pie chart types')
        time.sleep(2)
        """
            Step 05:Select first Pie (The most widely used chart for displaying percentages of a total. Click OK.
            Expect to see the Bar chart converted into the PIE chart Preview pane.
        """
        ia_ribbonobj.select_other_chart_type('pie', 'pie', 1, ok_btn_click=True)
        time.sleep(8)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Unit Sales'], "Step 05.01:",custom_css="text[class*='pieLabel']",same_group=True) 
        expected_label_list=['Category', 'Coffee']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 05.02: Verify pie lablesList ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue1", "Step 05.03: Verify first bar color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, "Step 05.04: Verify number of pie", custom_css=".chartPanel path[class*='riser!']")
        """
            Step 06:Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales'], "Step 06.01:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Category', 'Coffee', 'Food', 'Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 06.02: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge", "bar_blue", "Step 06.03: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category', 'Step 06.04: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.05: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, "Step 06.08: Verify number of pie", custom_css=".chartPanel path[class*='riser!']")    
        expected_tooltip_list=['Category:  Coffee', 'Unit Sales:  1376266  (37.31%)', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s0!g0!mwedge", expected_tooltip_list, "Step 08.9: Verify bar value") 
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()