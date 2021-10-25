'''
Created on Nov 6, 2017

@author: Magesh
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313658
TestCase Name = AHTML: Horizontal Dual-Axis Stacked Bar Chart Filter/Exclude tests.
'''

import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.wftools import visualization


class C2313658_TestClass(BaseTestCase):

    def test_C2313658(self):
        
        """
        CLASS OBJECTS
        """            
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        visualobj = visualization.Visualization(self.driver)
        
        """
            Step 01: Open FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Stacked_Bar.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Horizontal_Stacked_Bar", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        element_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        """
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 01.01: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 01.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 01.05: Verify  1st bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 01.06: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.07: Verify Y-Axis legend")
        
        """
            Step 02: Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_until_element_is_visible("[id^='ReportIframe']", ribbonobj.home_page_long_timesleep)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30) 
        
        """
            Expect to see the following Vertical Dual-Axis Stacked Bar Chart.
        """
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 02.04: Verify the total number of risers displayed on preview')
        bar=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 02.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 02.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 02.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 02.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 03: Hover over the top left bar for Alfa Romeo. Select Exclude from Chart.
        """
              
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g0!mbar!", "Exclude from Chart")     
        
        """
            Expect to see the following Bar Chart, with Alfa Romeo removed.
        """ 
        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 9, 20)       
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 03.01: Verify X-Axis Title")
        expected_xval_list=['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 03.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 36, 'Step 03.04: Verify the total number of risers displayed on preview')
        bar=['CAR:AUDI', 'DEALER_COST:5,063', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 03.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 03.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 03.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 03.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
       
        """
            Step 04: Hover over the top left bar for BMW. Select Exclude from Chart.
        """        
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g1!mbar!", "Exclude from Chart")
               
        """
            Expect to see the following Bar Chart, with Alfa Romeo & BMW removed.
        """
        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 8, 20)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 04.01: Verify X-Axis Title")
        expected_xval_list=['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.02: Verify XY labels")
        expected_yval2_list=['0', '100', '200', '300', '400', '500', '600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 32, 'Step 04.04: Verify the total number of risers displayed on preview')
        bar=['CAR:AUDI', 'DEALER_COST:5,063', 'Filter Chart', 'Exclude from Chart', 'Undo Filter', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 04.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 04.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 04.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 04.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
            
        """
            Step 05: Hover over the top left bar for Audi. Select Remove Filter.
        """    
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g0!mbar!", "Remove Filter")       
        
        """
            Expect to see the original Bar Chart with Alfa Romeo and BMW restored.
        """         
        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 10, 20)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 05.04: Verify the total number of risers displayed on preview')
        bar=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 05.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 05.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 05.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 05.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
            
        """
            Step 06: Left-click and draw a box around the bars for Jaguar & Jensen. Select Exclude from Chart.
        """
        parent_element = driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_type_using_pyautogui(parent_element)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s0!g4!mbar!")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s2!g5!ay2!mbar!")
        visualobj.create_lasso(source_element, target_element, source_xoffset=-15, target_xoffset=10, source_element_location='middle_left')
        visualobj.select_lasso_tooltip('Exclude from Chart')
#         resobj.create_lasso('MAINTABLE_wbody0','rect', 'riser!s0!g4!mbar!', target_tag='rect', target_riser='riser!s2!g5!ay2!mbar!')
#         resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
         
        """
            Expect to see the following Bar chart with both Jaguar & Jensen bars removed.
        """
        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 8, 20) 
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 06.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 32, 'Step 06.04: Verify the total number of risers displayed on preview')
        bar=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 06.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 06.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 06.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 06.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
            
        """
            Step 07: Hover over the bottom left bar for Alfa Romeo. Select Remove Filter.
        """       
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s2!g0!ay2!mbar!", "Remove Filter")       
         
        """
            Expect to see the original Bar Chart with Jaguar and Jensen bars restored.
        """
        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 10, 20) 
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 07.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 07.04: Verify the total number of risers displayed on preview')
        bar=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 07.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 07.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 07.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 07.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
                
        """
            Step 08:  Left-click and draw a box around the bars for Peugeot, Toyota & Triumph. Select Filter Chart.
        """  
             
        parent_element = driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_type_using_pyautogui(parent_element)
#         resobj.create_lasso('MAINTABLE_wbody0','rect', 'riser!s0!g7!mbar!', target_tag='rect', target_riser='riser!s2!g9!ay2!mbar!')
#         resobj.select_or_verify_lasso_filter(select='Filter Chart')
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s0!g7!mbar!")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s2!g9!ay2!mbar!")
        visualobj.create_lasso(source_element, target_element, source_xoffset=-15, target_xoffset=10, source_element_location='middle_left')
        visualobj.select_lasso_tooltip('Filter Chart')
         
        """
            Expect to see the following Bar Chart with bars for Peugeot, Toyota & Triumph only.
        """

        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 3, 20) 
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 08.01: Verify X-Axis Title")
        expected_xval_list=['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000', '8,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.02: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200', '240', '280']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 12, 'Step 08.04: Verify the total number of risers displayed on preview')
        bar=['CAR:PEUGEOT', 'DEALER_COST:4,631', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 08.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 08.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 08.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 08.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
                 
        """
            Step 09: Hover over the top left bar for Toyota. Click Filter Chart.
        """
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s0!g1!mbar!", "Filter Chart")       
         
        """
            Expect to see the following Bar Chart with bars for only Toyota.
        """         
        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20) 
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 09.01: Verify X-Axis Title")
        expected_xval_list=['TOYOTA']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.02: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200','240']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 09.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 4, 'Step 09.04: Verify the total number of risers displayed on preview')
        bar=['CAR:TOYOTA', 'DEALER_COST:2,886', 'Undo Filter', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 09.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 09.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 09.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 09.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
        """
            Step 10: Hover over the bottom left bar for Toyota. Select Remove Filter.
        """       
        resobj.select_default_tooltip_menu('MAINTABLE_wbody0', "riser!s2!g0!ay2!mbar!", "Remove Filter")         
         
        """
            Expect to see only the Remove Filter selection.
            No additional Exclusion may be done.
            Expect to see the original Bar Chart with
            Alfa Romeo and Audi restored.
        """
              
        element_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(element_css, 10, 20)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 10.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 10.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 10.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 10.04: Verify the total number of risers displayed on preview')
        bar=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", bar, "Step 10.05: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 10.06: Verify  1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 10.07: Verify  2nd bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 10.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 10.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)

        """
            Step 11: Close the chart.
            Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()        