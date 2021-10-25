'''
Created on Jul 27, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2205000
TestCase Name = MED >> Project 140615 AHTML/AFLEX:Footers aren`t respected in Active Charts
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea,ia_styling,visualization_metadata,visualization_ribbon
from common.lib import utillity

class C2205000_TestClass(BaseTestCase):

    def test_C2205000(self):
        
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Create a simple chart using CAR master file in IA.
        Select the Active Report Output format.
        Add fields from data tab eg:car and sales.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/car','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        resultobj.wait_for_property(parent_css, 11)
        
        ribbonobj.change_output_format_type('active_report')
        time.sleep(4)
        
        """
        Add fields from data tab eg:car and sales.  
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 10)
        metaobj.datatree_field_click('SALES', 2, 1)
        
        parent_css= "#TableChart_1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        
        xaxis_value="CAR"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 01:a(i) Verify X-Axis Title", custom_css="svg g text[class*='xaxisOrdinal-title']")
        yaxis_value="SALES"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 1.1: Verify XY labels')
        resultobj.verify_number_of_riser('TableChart_1', 1, 10, 'Step 1.2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.3: Verify bar color")

        """ 
        Step 02: From home tab select Header and footer from that add page footer in the chart.
        """
        ia_styobj.create_header_footer('ribbon', 'Page Footer', 'Page Footer', btn_apply='btn_apply', btn_ok='btn_ok')
        parent_css="#TableChart_1 [class*='footnote'] span"
        resultobj.wait_for_property(parent_css, 1)
        xaxis_value="CAR"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title", custom_css="svg g text[class*='xaxisOrdinal-title']")
        yaxis_value="SALES"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2.1: Verify XY labels')
        resultobj.verify_number_of_riser('TableChart_1', 1, 10, 'Step 2.2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02.3: Verify bar color")
        
        expected_title="Page Footer"
        page_footer=self.driver.find_element_by_css_selector("#TableChart_1 [class*='footnote'] span").text.strip()
        print(page_footer)
        utillobj.asequal(page_footer,expected_title,'Step 02.4: Verify Chart Title')
        
        """ 
        Step 03: Run the Chart and check page footer is displayed in the chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 10)
        xaxis_value="CAR"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 03:a(i) Verify X-Axis Title", custom_css="svg g text[class*='xaxisOrdinal-title']")
        yaxis_value="SALES"
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.1: Verify XY labels')
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 03.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 03.3: Verify bar color")
        time.sleep(2)
        expected_title="Page Footer"
        page_footer=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='footnote'] span").text.strip()
        print(page_footer)
        utillobj.asequal(page_footer,expected_title,'Step 03.4: Verify Chart Title')
        time.sleep(5)
        expected_tooltip_list=['CAR:BMW', 'SALES:80390', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 03.6: verify the default tooltip values')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2205000_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
if __name__ == '__main__':
    unittest.main()