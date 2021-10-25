'''
Created on Nov 2, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case= http://172.19.2.180/testrail/index.php?/cases/view/2324453
TestCase Name = AHTML: Vertical Dual-Axis Clustered Bar Chart Column/Row bucket functionality.
'''
import unittest, time
from common.lib import utillity
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous

class C2324453_TestClass(BaseTestCase):

    def test_C2324453(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID="C2324453"
        
        """ 
            CLASS OBJECTS 
        """
        chart_obj = Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10661%2FVertical_Cluster_Bar.fex&tool=Chart
                Expect to see the following Preview pane, including axis on both sides of the canvas.
        
        """
        utillobj.infoassist_api_edit("New_VerticalCluster_Bar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        element_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01:")
        expected_yval2_list=['0', '3K', '6K', '9K', '12K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.02:", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 01.03: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!ay2!mbar!", "pale_green", "Step 01.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.06 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1","DEALER_COST","Step 01.07 :Verify Y1axis title")
        resobj.verify_yaxis_title("TableChart_1","WEIGHT","Step 01.08 :Verify Y2axis title",custom_css="text[class='y2axis-title']")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify legend")
      
        """
           Step 02: Click the Run button.Hover over the first blue bar for Alfa Romeo.
            Expect to see the following Vertical Dual-Axis Clustered Bar Chart, with Tooltip information for Alfa Romeo/Dealer_Cost.
        """     
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)    
        utillobj.switch_to_frame(pause=2)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT by CAR", "Step 02.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.02:")
        expected_yval2_list=['0', '3K', '6K', '9K', '12K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.03:", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!ay2!mbar!", "bar_green", "Step 02.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.07: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 02.08 :Verify Y1axis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","WEIGHT","Step 02.09 :Verify Y2axis title",custom_css="text[class='y2axis-title']")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify legend")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 02.11: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
        """
           Step 03: Drag Country to the Column bucket.Click the run button.
                        Hover over the first blue bar for Jaguar.
                        Expect to see the following bucketized Bar Chart, now organized with vertical divisions by Country.
                    Also expect To see Tooltip information for Jaguar/Dealer_Cost.
        """
        utillobj.switch_to_default_content(pause=3)
        chart_obj.drag_field_from_data_tree_to_query_pane('COUNTRY', 1, 'Columns')
        element_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY', expire_time=20)
        chart_obj.verify_field_listed_under_querytree('Columns','COUNTRY',1, msg='Step 03.01')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)    
        utillobj.switch_to_frame(pause=2)
        expected_label=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "COUNTRY",expected_label,"Step 03.02:")       
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT by COUNTRY, CAR", "Step 03.03: Verify chart title ")
        resobj.verify_xaxis_title("MAINTABLE_wbody0 ","COUNTRY : CAR","Step 03.04: Verify Xaxis title", custom_css="text[class='colHeader-label!']")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 03.05 :Verify Y1axis title")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.06: Verify legend")
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH', 'PEUGEOT', 'ALFA ROMEO', 'MASERATI', 'DATSUN', 'TOYOTA', 'AUDI', 'BMW']
        expected_yval1_list=['0', '15K', '30K', '45K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.07:")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 03.08: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c0!", "bar_blue", "Step 03.09: Verify  riser color")
        expected_tooltip_list=['COUNTRY:ENGLAND', 'CAR:JAGUAR', 'DEALER_COST:18,621', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c0!", expected_tooltip_list, "Step 03.10: Verify Tooltip value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.11: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
        """
           Step 04: Drag the Country field from Column to the Rows bucket.Click the Run button.
            Hover over the first blue bar for Jaguar.
            Expect to see the following bucketized Bar Chart, now organized with horizontal divisions by Country.
            Also expect To see Tooltip information for Jaguar/Dealer_Cost.
        """
        utillobj.switch_to_default_content(pause=3)
        chart_obj.drag_field_within_query_pane("COUNTRY", "Rows")
        element_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY', expire_time=20)
        chart_obj.verify_field_listed_under_querytree('Rows','COUNTRY',1, msg='Step 04.01')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)    
        utillobj.switch_to_frame(pause=2)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT by COUNTRY, CAR", "Step 04.02: Verify chart title ")
        expected_label1=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0","Rows","COUNTRY",expected_label1,"Step 04.03: Verify visualization Row header lables")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.04: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!r4!c0!", "bar_blue", "Step 04.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 04.07: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 04.08 :Verify Y1axis title")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.09: Verify legend")
        expected_tooltip_list=['COUNTRY:ENGLAND', 'CAR:JAGUAR', 'DEALER_COST:18,621', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c0!", expected_tooltip_list, "Step 04.10: Verify bar value")
         
        """
           Step 05: Drag Bodytype to the Columns bucket.Hover over the first blue bar for Jaguar, under Conv.
            Expect to see the following bucketized Bar Chart, now organized as a Matrix, with Bodytypes across the chart and Countries down the page. 
            Also expect To see Tooltip information for Jaguar/Dealer_Cost.
        """ 
        utillobj.switch_to_default_content(pause=3)
        chart_obj.drag_field_from_data_tree_to_query_pane('BODYTYPE', 1, 'Columns')
        element_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(element_css, 'BODYTYPE', expire_time=20)
        chart_obj.verify_field_listed_under_querytree('Rows','COUNTRY',1, msg='Step 05.01')
        chart_obj.verify_field_listed_under_querytree('Columns','BODYTYPE',1, msg='Step 05.02')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=20)    
        utillobj.switch_to_frame(pause=2)
        expected_label=['CONVERTIB...', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "BODYTYPE", expected_label,"Step 05.03: Verify visualization column header lables",label_length=2)
        expected_label1=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0","Rows","COUNTRY",expected_label1,"Step 05.04: Verify visualization Row header lables",label_length=2)
        expected_xval_list=['JAGUAR', 'TRIUMPH', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'PEUGEOT', 'TOYOTA', 'ALFA ROMEO', 'MASERATI', 'ALFA ROMEO']
        expected_yval1_list=['0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K', '0', '15K', '30K', '45K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.05: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 26, 'Step 05.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c0!", "bar_blue", "Step 05.07: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0 ","BODYTYPE : CAR","Step 05.08: Verify Xaxis title", custom_css="text[class='colHeader-label!']")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 05.08: Verify Xaxis title")
        legend=['DEALER_COST', 'WEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.09: Verify legend")
        expected_tooltip_list=['COUNTRY:ENGLAND', 'BODYTYPE:CONVERTIBLE', 'CAR:JAGUAR', 'DEALER_COST:7,427', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c0!", expected_tooltip_list, "Step 05.10: Verify bar value")
        utillobj.switch_to_default_content(pause=2)        
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
           Step 06: Close chart.Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """    

if __name__ == '__main__':
    unittest.main()