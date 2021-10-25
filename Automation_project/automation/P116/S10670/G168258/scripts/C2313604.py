'''
Created on Sep 18, 2017

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313604
TestCase Name =  AHTML: Vertical Dual-Axis Stacked Bar Chart Filter/Exclude tests.
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.wftools import visualization

class C2313604_TestClass(BaseTestCase):

    def test_C2313604(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID="C2313604"
        time_out=30
        source_xoffset = -15
        target_xoffset = 10
        
        """
            CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        visualobj = visualization.Visualization(self.driver)
        driver = self.driver
         
        """
        Step 01:Open IA.Create a Chart Expect to see the following Preview pane
        """
        utillobj.infoassist_api_edit("Vertical_Stacked_Bar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 01.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 01.05: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 01.06: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 01.07: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.08: Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify legend")
         
        """
        Step 02:Click the Run button.Expect to see the following Vertical Dual-Axis Stacked Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
#         parent_css="#resultArea [id^=ReportIframe-]"
#         utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 02.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.02: Verify XY labels") 
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.04 : Verify Xaxis title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 02.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.06: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 02.07: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 02.08: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 02.09: Verify  riser color")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.11: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
          
        """
        Step 03:Hover over the lower left bar(Dealer_Cost) for Alfa Romeo.Select Exclude from Chart.
            Expect to see the following Bar Chart, with all bars for Alfa Romeo removed.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", 'Exclude from Chart')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 03.01 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 03.05: Filter Button Visible')
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 03.06: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.07: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 03.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 36, "Step 03.09: Verify the total number of risers displayed on preview")
        time.sleep(2)
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.10: Verify legend")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", "bar_blue", "Step 03.11: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g1!ay2!mbar!", "dark_green", "Step 03.12: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g1!ay2!mbar!", "pale_yellow", "Step 03.13: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!", "pale_green", "Step 03.14: Verify  riser color")
        
        """
        Step 04:Hover over the upper right bar(Height) for BMW.Select Exclude from Chart.
            Expect to see the following Bar Chart, with all bars for Alfa Romeo & BMW removed.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0_f", "riser!s3!g1!ay2!mbar!", 'Exclude from Chart')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 04.01 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.05: Filter Button Visible')
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 04.06: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['AUDI','DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K','30K','35K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.07: Verify XY labels")
        expected_yval2_list=['0', '100', '200', '300', '400','500','600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 32, "Step 04.09: Verify the total number of risers displayed on preview")
        time.sleep(2)
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.10: Verify legend")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 04.11: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 04.12: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 04.13: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 04.14: Verify  riser color")    
        
        """
        Step 05:Hover over the bottom right bar(Length) for Audi.Select Remove Filter.
            Expect to see the original Bar Chart with Alfa Romeo and BMW restored.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0_f", "riser!s2!g0!ay2!mbar!", 'Remove Filter')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 05.01 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 05.05: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.06: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.07: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, "Step 05.08: Verify the total number of risers displayed on preview")
        time.sleep(2)
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.09: Verify legend")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 05.10: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 05.11: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 05.12: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s1!g2!mbar!", "pale_green", "Step 05.13: Verify  riser color")
  
        """
        Step 06:Left-click and draw a box around the bars for Alfa Romeo and Audi.Select Exclude from Chart.
            Expect to see the following Bar chart with both Alfa Romeo and Audi bars removed.
        """
#         resobj.create_lasso('MAINTABLE_wbody0','rect', 'riser!s1!g0!mbar!', target_tag='rect', target_riser='riser!s2!g1!ay2!mbar!')
#         time.sleep(3)
#         resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s1!g0!mbar!")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s2!g1!ay2!mbar!")
        visualobj.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location='middle_left')
        visualobj.select_lasso_tooltip('Exclude from Chart')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 06.01 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 06.05: Filter Button Visible')
        time.sleep(2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 06.06: Verify -xAxis Title")
        expected_xval_list=['BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.07: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,32, "Step 06.09: Verify the total number of risers displayed on preview")
        time.sleep(2)
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.10: Verify legend")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 06.11: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 06.12: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 06.13: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s1!g2!mbar!", "pale_green", "Step 06.14: Verify  riser color")
      
        """
        Step 07:Hover over the upper left bar(Weight) for BMWSelect Remove Filter.
            Expect to see the original Bar Chart with Alfa Romeo and Audi restored.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0_f", "riser!s1!g0!mbar!", 'Remove Filter')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 07.01 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 07.05: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.06: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.07: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,40, "Step 07.08: Verify the total number of risers displayed on preview")
        time.sleep(2) 
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.09: Verify legend")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 07.10: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 07.11: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 07.12: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s1!g2!mbar!", "pale_green", "Step 07.13: Verify  riser color")
        
        """
        Step 08:Left-click and draw a box around the bars for Peugeot, Toyota & Triumph.Select Filter Chart.
            Expect to see the following Bar Chart with bars for Peugeot, Toyota & Triumph only.
        """
#         resobj.create_lasso('MAINTABLE_wbody0','rect', 'riser!s1!g7!mbar!', target_tag='rect', target_riser='riser!s2!g9!ay2!mbar!')
#         time.sleep(3)
#         resobj.select_or_verify_lasso_filter(select='Filter Chart')
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s1!g7!mbar!")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 rect[class*='riser!s2!g9!ay2!mbar!")
        visualobj.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location='middle_left')
        visualobj.select_lasso_tooltip('Filter Chart')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 08.01 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 08.05: Filter Button Visible')
        time.sleep(2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 08.06: Verify -xAxis Title")
        expected_xval_list=['PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000','6,000','7,000','8,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.07: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240','280']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,12, "Step 08.09: Verify the total number of risers displayed on preview")
        time.sleep(2)
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.10: Verify legend")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 08.11: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 08.12: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 08.13: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s1!g2!mbar!", "pale_green", "Step 08.14: Verify  riser color")
        
         
        """
        Step 09:Hover over the bottom left bar for Toyota.Click Filter Chart.
        Expect to see the following Bar Chart with bars for only Toyota.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0_f", "riser!s0!g1!mbar!", 'Filter Chart')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 09.01 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.02: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 09.05: Filter Button Visible')
        time.sleep(2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 09.06: Verify -xAxis Title")
        expected_xval_list=['TOYOTA']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000','6,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.07: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 09.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,4, "Step 09.09: Verify the total number of risers displayed on preview")
        time.sleep(2)
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.10: Verify legend")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 09.11: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g0!ay2!mbar!", "dark_green", "Step 09.12: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g0!ay2!mbar!", "pale_yellow", "Step 09.13: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s1!g0!mbar!", "pale_green", "Step 09.14: Verify  riser color")
        
        """
        Step 10:Hover over the green bar for Toyota.Select Remove Filter.
            Expect to see only the Remove Filter selection.Expect to see the original Bar Chart with Alfa Romeo and Audi restored.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0_f", "riser!s2!g0!ay2!mbar!", 'Remove Filter')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 10.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 10.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 10.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 10.04 : Verify Xaxis title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 10.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 10.06: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 10.07: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 10.08: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 10.09: Verify  riser color")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 10.10: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.11: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
                
if __name__ == '__main__':
    unittest.main()  