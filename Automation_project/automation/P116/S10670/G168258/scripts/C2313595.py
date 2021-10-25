'''
Created on Sep 22, 2017

@author: Magesh/ Updated by : Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313595
TestCase Name = AHTML: Horizontal Dual-Axis Clustered Bar Chart Filter/Exclude tests.
'''
import unittest, time 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.wftools import visualization

class C2313595_TestClass(BaseTestCase):

    def test_C2313595(self):
        
        """
        TESTCASE VARIABLES
        """ 
        time_out = 15
        source_xoffset = -15
        target_xoffset = 10
        
        """
        CLASS OBJECTS
        """ 
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        visual = visualization.Visualization(self.driver)
        driver = self.driver
               
        """
        Step 01: Open FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Cluster_Bar.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Horizontal_Cluster_Bar", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)

        """
        Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, time_out)
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 01.01: Verify X-Axis Title")  
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 01.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 01.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 01.06: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 01.07: Verify  1st bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 01.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify Y-Axis legend")
        
        """
        Step 02: Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.wait_for_page_loads(10)
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", "CAR", 20)
        
        """
        Expect to see the following Vertical Dual-Axis Clustered Bar Chart.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 02.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 02.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 02.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 02.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 02.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        
        """
        Step 03: Hover over the top(blue) bar for Alfa Romeo.
        Select Exclude from Chart.
        """
        raiser="[id^='MAINTABLE_wbody0'] [class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g0!mbar!", "Exclude from Chart")
        time.sleep(5)
        
        """
        Expect to see the following Bar Chart, with Alfa Romeo removed.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 03.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 03.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 03.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 03.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 18, 'Step 03.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 03.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 03.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 03.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        
        """
        Step 04: Hover over the blue bar for BMW. Select Exclude from Chart.
        """
        raiser="[id^='MAINTABLE_wbody0'] [class*='riser!s0!g1!mbar!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g1!mbar!", "Exclude from Chart")
        time.sleep(5)
        
        """
        Expect to see the following Bar Chart, with Alfa Romeo & BMW removed.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 04.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 04.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 04.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.04: Verify XY labels")
        expected_yval2_list=['0', '50', '100', '150', '200', '250', '300', '350', '400', '450']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 16, 'Step 04.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 04.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 04.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 04.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        
        """
        Step 05: Hover over the blue bar for Audi. Select Remove Filter.
        """
        raiser="[id^='MAINTABLE_wbody0'] [class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g0!mbar!", "Remove Filter")
        time.sleep(5)
        
        """
        Expect to see the original Bar Chart with Alfa Romeo and BMW restored.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 04.1: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.03: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.04: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 05.05: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 05.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 05.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 05.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        Step 06:  Left-click and draw a box around the bars for Alfa Romeo and Audi. Select Exclude from Chart.
        """
        time.sleep(5)
        raiser="#MAINTABLE_wbody0 [class*='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s0!g0!mbar']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s1!g1!ay2!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location='middle_left')
        visual.select_lasso_tooltip('Exclude from Chart')
#         resobj.create_lasso_using_action_chain('riser!s0!g0!mbar', 'riser!s1!g1!ay2!mbar!', 'MAINTABLE_wbody0')
#         resobj.create_lasso('MAINTABLE_wbody0','rect', 'riser!s0!g0!mbar', target_tag='rect', target_riser='riser!s1!g1!ay2!mbar!')
        
#         resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        
        """
        Expect to see the following Bar chart with both Alfa Romeo and Audi bars removed.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 06.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 06.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 06.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 16, 'Step 06.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 06.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 06.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 06.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        
        """
        Step 07: Hover over the blue bar for BMW. Select Remove Filter.
        """
        raiser="[id^='MAINTABLE_wbody0'] [class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g0!mbar!", "Remove Filter")
        time.sleep(5)
        
        """
        Expect to see the original Bar Chart with Alfa Romeo and Audi restored.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 07.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 07.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 07.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 07.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 07.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 07.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 07.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        Step 08:  Left-click and draw a box around the bars for Peugeot, Toyota & Triumph. Select Filter Chart.
        """
        time.sleep(5)
        raiser="#MAINTABLE_wbody0 [class*='riser!s0!g7!mbar!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)

#         resobj.create_lasso('MAINTABLE_wbody0','rect', 'riser!s0!g7!mbar!', target_tag='rect', target_riser='riser!s1!g9!ay2!mbar!')
#         resobj.select_or_verify_lasso_filter(select='Filter Chart')
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s0!g7!mbar!")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s1!g9!ay2!mbar!")
        visual.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location='middle_left')
        visual.select_lasso_tooltip('Filter Chart')
        
        """
        Expect to see the following Bar Chart with bars for Peugeot, Toyota & Triumph only.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 08.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 08.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 08.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.04: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 08.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 08.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 08.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 08.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        
        """
        Step 09: Hover over the blue bar for Toyota. Click Filter Chart.
        """
        raiser="[id^='MAINTABLE_wbody0'] [class*='riser!s0!g1!mbar!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)       
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g1!mbar!", "Filter Chart")
        time.sleep(5)
        
        """
        Expect to see the following Bar Chart with bars for only Toyota.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 09.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 09.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 09.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['TOYOTA']
        expected_yval1_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.04: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 09.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 2, 'Step 09.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 09.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 09.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 09.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        
        """
        Step 10: Hover over the green bar for Toyota. Select Remove Filter.
        """
        raiser="[id^='MAINTABLE_wbody0'] [class*='riser!s1!g0!ay2!mbar!']"
        utillobj.synchronize_with_number_of_element(raiser, 1, time_out)
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s1!g0!ay2!mbar!", "Remove Filter")
        time.sleep(5)
        
        """
        Expect to see only the Remove Filter selection. No additional Exclusion may be done.
        Expect to see the original Bar Chart with Alfa Romeo and Audi restored.
        """
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, time_out)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 10.01: Verify X-Axis Title")  
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 10.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 10.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 10.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 10.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 10.06: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 10.07: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 10.08: Verify  2nd bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 10.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 10.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        
        """
        Step 11: Close the chart.
        Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.switch_to_default_content(pause=1)
        elem1="#applicationButton img"
        utillobj.synchronize_with_number_of_element(elem1, 1, time_out)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()        