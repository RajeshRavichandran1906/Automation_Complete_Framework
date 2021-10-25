'''
Created on Nov 15, 2017

@author: Praveen Ramkumar
Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324455
TestCase Name =  AHTML: Vertical Dual-Axis Stacked Bar Chart Column/Row bucket functionality.
'''
import unittest, time 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous

class C2324454_TestClass(BaseTestCase):

    def test_C2324454(self):

        """
            CLASS & OBJECTS 
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10661%2FVertical_DualAxis_StackedBar.fex&tool=Chart
        Expect to see the following Preview pane, including axis on both sides of the canvas. 
        """
        utillobj.infoassist_api_edit("Vertical_DualAxis_StackedBar", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.1: Verify XY labels")
        expected_yval2_list=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 01.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 01.4b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.5a : Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'WEIGHT', 'RPM']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.6: Verify legend")
             
        """
           Step 02: Click the Run button.
            Hover over the bottom left blue bar for Alfa Romeo.
            Expect to see the following Vertical Dual-Axis Stacked Bar Chart.
            Also expect to see Tooltip information for 
            Alfa Romeo/Dealer_Cost.
        """
              
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
#         parent_css="#resultArea [id^=ReportIframe-]"
#         resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30) 
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, WEIGHT, RPM by CAR", "Step 02.1 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.2: Verify XY labels")
        expected_yval2_list=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 02.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.5a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 02.5b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.6a: Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'WEIGHT', 'RPM']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.7: Verify legend")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 02.8: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.9a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.9:c Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 02.8: Verify bar value")

        
        """
           Step 03: Drag Country to the Columns bucket.Click the run button.
            Hover over the top yellow bar for Jaguar.
            Expect to see the following bucketized Bar Chart, now organized with vertical divisions by Country.
            Also expect to see Tooltip information for 
            Jaguar/RPM.
        """
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Columns',0)
        parent_css='#queryTreeWindow tr:nth-child(5) td'
        resobj.wait_for_property(parent_css, 1,string_value='COUNTRY',expire_time=50)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Columns','COUNTRY',1,"Step 03.1: Verify query pane")
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        expected_label=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "COUNTRY : CAR",expected_label,"Step 03.1: Verify visualization column header lables")       
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, WEIGHT, RPM by COUNTRY, CAR", "Step 03.2: Verify chart title ")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0 ","CAR","Step 03.3: Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'WEIGHT', 'RPM']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.4: Verify legend")
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH', 'PEUGEOT', 'ALFA ROMEO', 'MASERATI', 'DATSUN', 'TOYOTA', 'AUDI', 'BMW']
        expected_yval1_list=['0', '30K', '60K', '90K', '120K', '150K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.5: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 03.6: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c0!", "bar_blue", "Step 03.7: Verify  riser color")
        expected_tooltip_list=['COUNTRY:ENGLAND', 'CAR:JAGUAR', 'RPM:11500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", 'riser!s3!g4!ay2!mbar!r0!c0!', expected_tooltip_list, "Step 03.8: Verify Tooltip value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.9 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
           Step 04: Drag the Country field from Column to the Rows bucket.Click the Run button.
            Hover over the bottom blue bar for Jaguar.
            Expect to see the following bucketized Bar Chart, now organized with horizontal divisions by Country.
            Also expect to see Tooltip information for 
            Jaguar/Dealer_Cost.
        """
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        metadataobj.drag_and_drop_query_items("COUNTRY", "Rows")
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True)
        metadataobj.verify_query_pane_field('Rows','COUNTRY',1,"Step 04.1: Verify query pane")
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, WEIGHT, RPM by COUNTRY, CAR", "Step 04.2: Verify chart title ")
        expected_label1=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0","Rows","COUNTRY",expected_label1,"Step 04.3: Verify visualization Row header lables",label_length=2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '30K', '60K', '90K', '120K', '150K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.4: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 04.6: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c0!", "bar_blue", "Step 04.7: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 04.9: Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'WEIGHT', 'RPM']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.10: Verify legend")
        expected_tooltip_list=['COUNTRY:ENGLAND', 'CAR:JAGUAR', 'DEALER_COST:18,621', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c0!", expected_tooltip_list, "Step 04.11: Verify bar value")
        
        """
           Step 05: Drag Bodytype to the Columns bucket.Click the Run button.
            Hover over the bottom blue bar for Jaguar, under Sedan.
            Expect to see the following bucketized Bar Chart, now organized as a Matrix, with Bodytypes across the chart and Countries down the page. 
            Also expect to see Tooltip information for 
            Jaguar/Dealer_Cost.
        """
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('BODYTYPE', 1, 'Columns',0)
        parent_css='#queryTreeWindow tr:nth-child(6) td'
        resobj.wait_for_property(parent_css, 1,string_value='BODYTYPE',expire_time=50)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Rows','COUNTRY',1,"Step 05.1: Verify query pane")
        metadataobj.verify_query_pane_field('Columns','BODYTYPE',1,"Step 05.2: Verify query pane")
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        expected_label=['CONVERTIB...', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "BODYTYPE : CAR", expected_label,"Step 05.3a: Verify visualization column header lables",label_length=2)
        expected_label1=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0","Rows","COUNTRY",expected_label1,"Step 05.3b: Verify visualization Row header lables",label_length=2)
        expected_xval_list=['JAGUAR', 'TRIUMPH', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'PEUGEOT', 'TOYOTA', 'ALFA ROMEO', 'MASERATI', 'ALFA ROMEO']
        expected_yval1_list=['0', '30K', '60K', '90K', '120K', '150K', '0', '30K', '60K', '90K', '120K', '150K', '0', '30K', '60K', '90K', '120K', '150K', '0', '30K', '60K', '90K', '120K', '150K', '0', '30K', '60K', '90K', '120K', '150K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.4: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 52, 'Step 05.6: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!r0!c4!", "bar_blue", "Step 05.7a: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 05.8: Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'WEIGHT', 'RPM']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.9: Verify legend")
        expected_tooltip_list=['COUNTRY:ENGLAND', 'BODYTYPE:SEDAN', 'CAR:JAGUAR', 'DEALER_COST:11,194', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c4!", expected_tooltip_list, "Step 05.10: Verify bar value")
        time.sleep(5)
       
        """
           Step 06:Close chart.Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
            
if __name__ == '__main__':
    unittest.main()  