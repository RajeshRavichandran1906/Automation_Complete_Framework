'''
Created on Nov 1, 2017
@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case= http://172.19.2.180/testrail/index.php?/cases/view/2313438
TestCase Name =AHTML: Mekko Chart Color By chart using additional Buckets.

'''
import unittest
import time
from common.wftools import active_chart
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata

class C2313438_TestClass(BaseTestCase):

    def test_C2313438(self):
        
        Test_Case_ID="C2313438"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        active_chartobj = active_chart.Active_Chart(self.driver)
        
        """
            Step 01 : Launch new chart using the IA API
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FMekko_ColorBy.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Mekko_ColorBy",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 .chartPanel", 1, 60)
        
        """
            Step 02 : Click the Run button.
            Expect to see the following Active Mekko Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
         
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST by COUNTRY, CAR", "Step 02.1 : Verify chart title ")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PE...', 'T...', 'T', 'D']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        active_chartobj.verify_x_axis_label_and_length_in_run_window(expected_xval_list, msg="Step 02.02")
        active_chartobj.verify_y_axis_label_and_length_in_run_window(expected_yval1_list, msg="Step 02.03")
#         resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.2a: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue", "Step 02.4a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s8!g2!mbar!", "moss_green", "Step 02.4b: Verify  riser color")
        legend=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.5: Verify legend")
         
        expected_datalabel=['108K','56,500','40,990','35,800']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 02.7: Verify labels", data_label_length=4, custom_css=".chartPanel text[class^='stackTotalLabel']")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.8a: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.8c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#          
        """
            Step 03 : Drag the field SALES to the Tooltip area.
            Expect to see the SALES field under the Tooltip area in the Query panel.
        """
        
        utillobj.switch_to_default_content(pause=3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('SALES', 1, 'Tooltip',0)
        parent_css='#queryTreeWindow tr:nth-child(12) td'
        utillobj.synchronize_with_visble_text(parent_css, "SALES", 35)
        
        metadataobj.verify_query_pane_field('Tooltip','SALES',1,"Step 03.1: Verify query pane")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'P...', 'T...', 'T', 'D']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels", x_axis_label_length=1)
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 03.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue", "Step 03.5a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s8!g2!mbar!", "moss_green", "Step 03.5b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 03.7: Verify Xaxis title")
        legend=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.8: Verify legend")
        expected_datalabel=['108K','56,500','40,990','35,800']
        resobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 03.9: Verify labels",data_label_length=4, custom_css=".chartPanel text[class^='stackTotalLabel']")
        
        """
            Step 04 : Click the Run button.Hover over lower area(red) for Alfa Romeo.
            Expect to see the SALES field added to the Tooltip information for CAR, DEALER_COST & COUNTRY.  
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES by COUNTRY, CAR", "Step 04.1 : Verify chart title ")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PE...', 'T...', 'T', 'D']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels", x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue", "Step 0.5a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s8!g2!mbar!", "moss_green", "Step 04.5b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 04.6: Verify Xaxis title")
        legend=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.7: Verify legend")
        expected_datalabel=['108K','56,500','40,990']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 04.8: Verify labels",data_label_length=3,custom_css=".chartPanel text[class^='stackTotalLabel']")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235  (45.35%)', 'COUNTRY:ITALY', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s4!g0!mbar!", expected_tooltip_list, "Step 04.9: Verify bar value")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.10a: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.10b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
        """
            Step 05 : Drag the field SEATS to the Multigraph area.
            Expect to see the SEATS field under the Multigraph area in the Query panel.  
        """
        utillobj.switch_to_default_content(pause=3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('SEATS', 1,'Multi-graph',0)
        parent_css='#queryTreeWindow tr:nth-child(14) td'
        utillobj.synchronize_with_visble_text(parent_css, "SEATS", 30)
         
        metadataobj.verify_query_pane_field('Multi-graph','SEATS',1,"Step 05.1: Verify query pane")
        expected_xval_list=['MASERATI','ALFA ROMEO','JAGUAR','TRIUMPH']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        legend=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 05.3: Verify legend")
        resobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 05.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g1!mbar!", "pale_green", "Step 05.5a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g3!mbar!", "bar_blue", "Step 05.5b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 05.6: Verify Xaxis title")
        expected_datalabel=['56,500','24,960','16,305','9,392']
        resobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 05.7: Verify labels",custom_css=".chartPanel text[class^='stackTotalLabel']")
        
        """
            Step 06 : Click the Run button.Expect to see the data reordered, with Alfa Romeo first and Peugeot last.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES by COUNTRY, CAR", "Step 06.1 : Verify chart title ")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 06.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue", "Step 6.4a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s8!g2!mbar!", "moss_green", "Step 6.4b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 6.5: Verify Xaxis title")
        legend=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.6: Verify legend")
        if Global_variables.browser_name == 'firefox':
            expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '1...', '1...', '6', '5']
        else:
            expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '1...', '1', '6', '5']
        active_chartobj.verify_x_axis_label_and_length_in_run_window(expected_datalabel, xyz_axis_label_css="text[class*='stackTotalLabel']",msg="Step 06.07")
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 06.7: Verify labels",custom_css=".chartPanel text[class^='stackTotalLabel']", data_label_length=4)
        expected_tooltip_list=['SEATS:2', 'CAR:JAGUAR', 'DEALER_COST:18,621  (45.43%)', 'COUNTRY:ENGLAND', 'SALES:12000', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 06.8: Verify bar value")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.9a: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.9c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
        """
            Step 07 : Hover over the lower area(red) for Alfa Romeo.Expect to see 2 Seats for Alfa Romeo.This is the lowest value of SEATS.
        """
        css="#MAINTABLE_wbody0_f"
        elem=utillobj.validate_and_get_webdriver_object(css, 'Runtime bar chart')
        core_utility_obj.move_to_element(elem, element_location="bottom_middle")
        
        expected_tooltip_list=['SEATS:2', 'CAR:ALFA ROMEO', 'RETAIL_COST:16,235  (45.35%)', 'COUNTRY:ITALY', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s4!g0!mbar!", expected_tooltip_list, "Step 07.1: Verify bar value")
        
        """
            Step 08 : Hover over the lower area(red) for Alfa Romeo.Expect to see 2 Seats for Alfa Romeo.This is the lowest value of SEATS.
        """
        css="#MAINTABLE_wbody0_f"
        elem=utillobj.validate_and_get_webdriver_object(css, 'Runtime bar chart')
        core_utility_obj.move_to_element(elem, element_location="bottom_middle")
        
        expected_tooltip_list=['SEATS:5', 'CAR:PEUGEOT', 'DEALER_COST:4,631  (45.22%)', 'COUNTRY:FRANCE', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s2!g7!mbar!", expected_tooltip_list, "Step 08.1: Verify bar value")
        
        
        """
            Step 09 : Move the SEATS field from the Multigraph area to the Animate area.
            Expect to see the SEATS field under the Animate area in the Query panel.
        """
        utillobj.switch_to_default_content(pause=3)
        metadataobj.drag_and_drop_query_items("SEATS", "Animate")
        parent_css="#queryTreeWindow table tr:nth-child(15) td"
        utillobj.synchronize_with_visble_text(parent_css, "SEATS", 35)
        
        metadataobj.verify_query_pane_field('Animate','SEATS',1,"Step 09.1: Verify query pane")
        utillobj.verify_object_visible("#TableChart_1 rect[class='sliderBody']",True,"Step 09.2: verify slider object visible")
        resobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 09.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue", "Step 09.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g4!mbar!", "pale_green", "Step 09.4b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 09.5: Verify Xaxis title")
        expected_xval_list=['D', 'ALFA ROMEO', 'JAGUAR', 'TRIUMPH', 'MASERATI', 'B', 'J', 'A', 'P', 'T']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 9.6: Verify XY labels")
        legend=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 09.7: Verify legend")
        expected_datalabel=['24,960', '16,305', '9,392', '56,500']
        resobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 09.8: Verify labels",custom_css=".chartPanel text[class^='stackTotalLabel']")
        
        """
            Step 10 : Click the Run button.Hover over the lower area(blue) for Jaguar.
            Expect to see the following Streamgraph, showing only CARs with 2 SEATS.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES by SEATS, COUNTRY, CAR", "Step 10.1 : Verify chart title ")
        expected_xval_list=['D', 'ALFA ROMEO', 'JAGUAR', 'TRIUMPH', 'MASERATI', 'B', 'J', 'A', 'P', 'T']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 10.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 8, 'Step 10.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue", "Step10.4a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!mbar!", "pale_green", "Step 10.4b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 10.5: Verify Xaxis title")
        legend=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 10.6: Verify legend")
        expected_datalabel=['24,960', '16,305', '9,392', '56,500']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 10.7: Verify labels",custom_css=".chartPanel text[class^='stackTotalLabel']")
        expected_tooltip_list=['SEATS:2', 'CAR:JAGUAR', 'DEALER_COST:7,427  (45.55%)', 'COUNTRY:ENGLAND', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 10.8: Verify bar value")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.9a: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.9c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 11 : Move the slider control at the top to position 4.Hover over the lower area(blue) for Jensen.
            Expect to see the following Streamgraph, showing only CARs with 4 SEATS.        
        """
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj, coordinate_type='middle', click_type=0)
        time.sleep(5)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,10, 'Step 11.1: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!", "bar_blue", "Step 11.2a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g5!mbar!", "pale_green", "Step 11.2b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 11.3: Verify Xaxis title")
        expected_xval_list=['T', 'BMW', 'ALFA ROMEO', 'TOYOTA', 'DATSUN', 'JENSEN', 'A', 'M', 'P', 'J']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 11.4a: Verify XY labels")
        legend=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 11.5: Verify legend")
        expected_tooltip_list=['SEATS:4', 'CAR:JENSEN', 'DEALER_COST:14,940  (45.56%)', 'COUNTRY:ENGLAND', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g5!mbar!", expected_tooltip_list, "Step 11.6: Verify bar value")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES by SEATS, COUNTRY, CAR", "Step 11.7: Verify chart title ")
        expected_datalabel=['12,355', '10,840', '6,225', '5,765', '32,790']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 11.8: Verify labels",custom_css=".chartPanel text[class^='stackTotalLabel']")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.9a: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.9c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
       
        """
            Step 12 : Move the slider control at the top to position 5.Hover over the lower area(green) for Peugeot.
            Expect to see the following Streamgraph, showing only CARs with 5 SEATS.
        """
        
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj, coordinate_type='right', click_type=0)
        time.sleep(5)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,8, 'Step 12.1: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue", "Step 12.2a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!mbar!", "pale_green", "Step 12.2b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 12.3: Verify Xaxis title")
        expected_xval_list=['T', 'JAGUAR', 'AUDI', 'PEUGEOT', 'BMW', 'A', 'J', 'M', 'D', 'T']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 12.4a: Verify XY labels", x_axis_label_length=1)
        legend=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 12.5: Verify legend")
        expected_tooltip_list=['SEATS:5', 'CAR:PEUGEOT', 'DEALER_COST:4,631  (45.22%)', 'COUNTRY:FRANCE', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s2!g7!mbar!", expected_tooltip_list, "Step 12.6: Verify bar value")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES by SEATS, COUNTRY, CAR", "Step 12.7: Verify chart title ")
        expected_datalabel=['24,685', '11,033', '10,241', '95,907']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 12.8: Verify labels",custom_css=".chartPanel text[class^='stackTotalLabel']")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12.9a: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 12.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12.9c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)        
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
    
        """
            Step 13  :Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        
if __name__ == '__main__':
    unittest.main()