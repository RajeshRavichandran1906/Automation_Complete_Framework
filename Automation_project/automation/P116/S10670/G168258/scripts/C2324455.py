'''
Created on Nov 13, 2017

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324455
TestCase Name =  Horizontal Dual-Axis Clustered Bar Chart Column/Row bucket functionality.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2324455_TestClass(BaseTestCase):

    def test_C2324455(self):
       
        """
        TESTCASE OBJECTS
        """ 
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10661%2FHorizontal_DualAxisClusterBar.fex&tool=Chart
        Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Horizontal_DualAxis_ClusterBar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1, expire_time=65)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        expected_yval2_list=['0', '3K', '6K', '9K', '12K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 01.03: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!ay2!mbar!", "bar_green", "Step 01.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.06: Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1","DEALER_COST","Step 01.07 :Verify Y1axis title")
        resobj.verify_yaxis_title("TableChart_1","WEIGHT","Step 01.08:Verify Y2axis title",custom_css="text[class='y2axis-title']")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify legend")
               
        """
        Step 02:Click the Run button.Hover over the top blue bar for Triumph.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT by CAR", "Step 02.01 : Verify chart title ")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.02 : Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 02.03 :Verify Y1axis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","WEIGHT","Step 02.04:Verify Y2axis title",custom_css="text[class='y2axis-title']")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.05: Verify legend")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.06: Verify XY labels")
        expected_yval2_list=['0', '3K', '6K', '9K', '12K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.07: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.08: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!ay2!mbar!", "bar_green", "Step 02.09: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.10: Verify  riser color")
        time.sleep(2)
        expected_tooltip_list=['CAR:TRIUMPH', 'DEALER_COST:4,292', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g9!mbar!", expected_tooltip_list, "Step 02.11: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
              
        """
        Step 03:Drag Country to the Columns bucket.Click the run button.Hover over the top blue bar for Jaguar.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Columns',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value="COUNTRY",expire_time=50)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        
        expected_label=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "COUNTRY : CAR",expected_label,"Step 03.01: Verify visualization column header lables")       
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT by COUNTRY, CAR", "Step 03.02: Verify chart title ")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0 ","CAR","Step 03.03: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0 ","DEALER_COST","Step 03.04:Verify Yaxis title")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.05: Verify legend")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.06: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 03.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!ay2!mbar!", "bar_green", "Step 03.08: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 03.09: Verify  riser color")
        expected_tooltip_list=['COUNTRY:ENGLAND', 'CAR:JAGUAR', 'DEALER_COST:18,621', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c0!", expected_tooltip_list, "Step 03.10: Verify Tooltip value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.11 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
          
        """
        Step 04:Drag the Country field from Columns to the Rows bucket.Click the Run button.Hover over the bottom green bar for BMW.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(8)
        elm=driver.find_element_by_css_selector("#queryTreeWindow")
        utillobj.click_on_screen(elm, coordinate_type='middle', click_type=0)
        time.sleep(10)
        metadataobj.drag_and_drop_within_query_tree('COUNTRY', 'Rows')
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value="COUNTRY",expire_time=50)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        
        expected_label=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Rows", "COUNTRY", expected_label,"Step 04.01: Verify visualization column header lables",label_length=2)
#         resobj.verify_xaxis_title("MAINTABLE_wbody0 ","CAR","Step 04.02: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0 ","DEALER_COST","Step 04.03 :Verify Yaxis title")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.04: Verify legend")
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH', 'PEUGEOT','ALFA ROMEO','MASERATI','DATSUN','TOYOTA','AUDI','BMW']
        expected_yval_list=['0', '15K', '30K', '45K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.05: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!ay2!mbar!r4!c0!", "bar_green", "Step 04.07: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!r4!c0!", "bar_blue", "Step 04.08: Verify  riser color")
        expected_tooltip_list=['COUNTRY:W GERMANY', 'CAR:BMW', 'WEIGHT:11,300', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s1!g2!ay2!mbar!r4!c0!", expected_tooltip_list, "Step 04.09: Verify tooltip value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.10 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT by COUNTRY, CAR", "Step 04.13 : Verify chart title ") 
        
        """
        Step 05:Drag Bodytype to the Columns bucket.Click the Run button.Hover over the top blue bar for Jaguar.
        """
        utillobj.switch_to_default_content(pause=3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('BODYTYPE',1,'Columns',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value="BODYTYPE",expire_time=50)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        
        expected_label=['CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "BODYTYPE : CAR", expected_label,"Step 05.01: Verify visualization column header lables",label_length=2)
        expected_label1=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0","Rows","COUNTRY",expected_label1,"Step 05.02: Verify visualization Row header lables",label_length=2)
#         resobj.verify_xaxis_title("MAINTABLE_wbody0 ","CAR","Step 05.03: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0 ","DEALER_COST","Step 05.04:Verify Yaxis title")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.05: Verify legend")
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH', 'PEUGEOT', 'ALFA ROMEO', 'MASERATI', 'DATSUN', 'TOYOTA', 'AUDI', 'BMW']
        expected_yval1_list=['0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K']
        
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.06: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 26, 'Step 05.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!ay2!mbar!r0!c0!", "bar_green", "Step 05.08: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c0!", "bar_blue", "Step 05.09: Verify  riser color") 
           
        expected_tooltip_list=['COUNTRY:ENGLAND', 'BODYTYPE:CONVERTIBLE', 'CAR:JAGUAR', 'DEALER_COST:7,427', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c0!", expected_tooltip_list, "Step 05.10: Verify tooltip value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.11: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT by COUNTRY, BODYTYPE, CAR", "Step 05.14 : Verify chart title ")
        utillobj.switch_to_default_content(pause=5)
            
        
if __name__ == '__main__':
    unittest.main()  