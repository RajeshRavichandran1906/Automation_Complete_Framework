'''
Created on Oct 11, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case= http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313441
TestCase Name =AHTML: Mekko Chart Color By chart limit tests.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata
from common.lib import utillity


class C2313441_TestClass(BaseTestCase):

    def test_C2313441(self):
        
        Test_Case_ID="C2313441"
        """
            TESTCASE VARIABLES
        """     
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
            Step 01:Launch new chart using the IA API
           http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FMekko_ColorBy.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Mekko_ColorBy",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
        
        """
        Step 02:Add additional Dimension(X-axis) fields:
        COUNTRY & MODEL.
        Click the Run button.
        Expect to see the following Active Mekko Chart Preview pane.
        The limit for X-axis fields is 3.
        """
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_visble_text(parent_css, 'COUNTRY', 50)
        metadataobj.datatree_field_click('MODEL', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, 'MODEL', 50)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_ft", 1, 60)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST by COUNTRY, CAR, COUNTRY, MODEL", "Step 02.1 : Verify chart title ")
        expected_xval_list=['MASERATI : ITALY : DORA 2 DOOR', 'JENSEN : ENGLAND : INTERCEPTOR III', 'BMW : W GERMANY : 3.0 SI 4 DOOR AUTO', 'JAGUAR : ENGLAND : XJ12L AUTO','BMW : W GERMANY : 3.0 SI 4 DOOR','BMW : W GERMANY : 530I 4 DOOR AUTO','BMW : W GERMANY : 530I 4 DOOR','JAGUAR : ENGLAND : V12XKE AUTO','ALFA ROMEO : ITALY : 2000 SPIDER VELOCE','ALFA ROMEO : ITALY : 2000 GT VELOCE','BMW : W GERMANY : 2002 2 DOOR AUTO','BMW : W GERMANY : 2002 2 DOOR','AUDI : W GERMANY : 100 LS 2 DOOR AUTO','ALFA ROMEO : ITALY : 2000 4 DOOR BERLINA','PEUGEOT : FRANCE : 504 4 DOOR','TRIUMPH : ENGLAND : TR7','TOYOTA : JAPAN : COROLLA 4 DOOR DIX AUTO','DATSUN : JAPAN : B210 2 DOOR AUTO']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.2: Verify XY labels")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : MODEL', "Step 02.3: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 36, 'Step 02.4: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g13!mbar!', 'pale_green', 'Step 02.5: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND','DEALER_COST:FRANCE','RETAIL_COST:FRANCE','DEALER_COST:ITALY','RETAIL_COST:ITALY','DEALER_COST:JAPAN','RETAIL_COST:JAPAN','DEALER_COST:W GERMANY','RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 02.9 Verify Legends ')
        expected_datalabel=['56,500', '32,790', '25,123', '24,685', '23,752', '17,895', '17,397', '16,305', '12,480', '12,480','12,355','11,740','11,...','10,...','10,...','9,...','6...','5...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 02.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
#         expected_tooltip_list=['CAR:JENSEN', 'COUNTRY:ENGLAND', 'MODEL:INTERCEPTOR III', 'RETAIL_COST:17,850', 'COUNTRY:ENGLAND', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s1!g13!mbar!', expected_tooltip_list, 'Step 02.11: verify the default tooltip values')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(1)
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 02.12: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 02.13: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','MODEL',3,"Step 02.14: Verify query pane")
         
        """
        Step 03:Add additional Dimension(X-axis) field BODYTYPE.
            Click the Run button.
            Expect to see the following Active Mekko Chart Preview pane, with BODYTYPE replacing MODEL.
            The limit for X-axis fields is 3.
        """
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, 'BODYTYPE', 50)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_ft", 1, 60)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST by COUNTRY, CAR, COUNTRY, BODYTYPE", "Step 03.1 : Verify chart title ")
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'MASERATI : ITALY : COUPE', 'JENSEN : ENGLAND : SEDAN', 'JAGUAR : ENGLAND : SEDAN','JAGUAR : ENGLAND : CONVERTIBLE','ALFA ROMEO : ITALY : COUPE','ALFA ROMEO : ITALY : ROADSTER','AUDI : W GERMANY : SEDAN','ALFA ROMEO : ITALY : SEDAN','PEUGEOT : FRANCE : SEDAN','TRIUMPH : ENGLAND : HARDTOP','TOYOTA : JAPAN : SEDAN','DATSUN : JAPAN : SEDAN']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 03.3: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 26, 'Step 03.4: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g8!mbar!', 'pale_green', 'Step 03.5: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND','DEALER_COST:FRANCE','RETAIL_COST:FRANCE','DEALER_COST:ITALY','RETAIL_COST:ITALY','DEALER_COST:JAPAN','RETAIL_COST:JAPAN','DEALER_COST:W GERMANY','RETAIL_COST:W GERMANY']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 03.9 Verify Legends ')
        expected_datalabel=['108K', '56,500', '32,790', '24,685', '16,305','12,480', '12,480', '11,...', '10,...', '10,...','9,...','6...','5...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 03.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
#         expected_tooltip_list=['CAR:JENSEN', 'COUNTRY:ENGLAND', 'BODYTYPE:SEDAN', 'RETAIL_COST:17,850', 'COUNTRY:ENGLAND', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s1!g8!mbar!', expected_tooltip_list, 'Step 03.11: verify the default tooltip values')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(1)
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 03.12: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 03.13: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','BODYTYPE',3,"Step 03.14: Verify query pane")
          
        """
         Step 04:Hover over the lower area(light green) for BMW.
         Expect to see the following Tooltip information confirming that CAR, COUNTRY & BODYTYPE are shown, since all values are not visible in the chart X-axis labels.
        """
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0", 1, 60)
        expected_tooltip_list=['CAR:BMW', 'COUNTRY:W GERMANY', 'BODYTYPE:SEDAN', 'DEALER_COST:49,500  (45.72%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s8!g4!mbar!', expected_tooltip_list, 'Step 04.1: verify the default tooltip values')
        time.sleep(2)
         
        """
         Step 05:Remove Measure(Vertical axis) fields DEALER_COST & RETAIL_COST.
            Add new Measure fields:
            SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL.
            Click the Run button.
            Expect to see all 8 Vertical axis fields appear both on the chart and as entries in the chart legend.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(1)
        metadataobj.querytree_field_click("DEALER_COST",1,1,"Delete")
        time.sleep(1)
        metadataobj.querytree_field_click("RETAIL_COST",1,1,"Delete")
        time.sleep(1)
        metadataobj.datatree_field_click('SEATS', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, 'SEATS', 50)
        metadataobj.datatree_field_click('LENGTH', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        utillobj.synchronize_with_visble_text(parent_css, 'LENGTH', 50)
        metadataobj.datatree_field_click('WIDTH', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WIDTH', 50)
        metadataobj.datatree_field_click('WHEELBASE', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WHEELBASE', 50)
        metadataobj.datatree_field_click('FUEL_CAP', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_visble_text(parent_css, 'FUEL_CAP', 50)
        metadataobj.datatree_field_click('BHP', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, 'BHP', 50)
        metadataobj.datatree_field_click('MPG', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(10) td"
        utillobj.synchronize_with_visble_text(parent_css, 'MPG', 50)
        metadataobj.datatree_field_click('ACCEL', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(11) td"
        utillobj.synchronize_with_visble_text(parent_css, 'ACCEL', 50)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_ft", 1, 60)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY, CAR, COUNTRY, BODYTYPE", "Step 05.1 : Verify chart title ")
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'JAGUAR : ENGLAND : SEDAN','JAGUAR : ENGLAND : CONVERTIBLE','AUDI : W GERMANY : SEDAN','TRIUMPH : ENGLAND : HARDTOP','TOYOTA : JAPAN : SEDAN','DATSUN : JAPAN : SEDAN','PEUGEOT : FRANCE : SEDAN','ALFA ROMEO : ITALY : SEDAN','ALFA ROMEO : ITALY : ROADSTER','ALFA ROMEO : ITALY : COUPE']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 05.3: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 104, 'Step 05.4: Verify the total number of risers displayed on run')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['SEATS:ENGLAND', 'LENGTH:ENGLAND', 'WIDTH:ENGLAND', 'WHEELBASE:ENGLAND', 'FUEL_CAP:ENGLAND', 'BHP:ENGLAND', 'MPG:ENGLAND', 'ACCEL:ENGLAND', 'SEATS:FRANCE', 'LENGTH:FRANCE', 'WIDTH:FRANCE', 'WHEELBASE:FRANCE', 'FUEL_CAP:FRANCE', 'BHP:FRANCE', 'MPG:FRANCE', 'ACCEL:FRANCE', 'SEATS:ITALY', 'LENGTH:ITALY', 'WIDTH:ITALY', 'WHEELBASE:ITALY', 'FUEL_CAP:ITALY', 'BHP:ITALY', 'MPG:ITALY', 'ACCEL:ITALY', 'SEATS:JAPAN', 'LENGTH:JAPAN', 'WIDTH:JAPAN', 'WHEELBASE:JAPAN', 'FUEL_CAP:JAPAN', 'BHP:JAPAN', 'MPG:JAPAN', 'ACCEL:JAPAN', 'SEATS:W GERMANY', 'LENGTH:W GERMANY', 'WIDTH:W GERMANY', 'WHEELBASE:W GERMANY', 'FUEL_CAP:W GERMANY', 'BHP:W GERMANY', 'MPG:W GERMANY', 'ACCEL:W GERMANY']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05.8: Verify Legends ')
        expected_datalabel=['2,388', '793.5', '696.9', '668.8', '644.4','512.8', '447.2', '439.5', '434.5', '397.9','378.3','359.1','355.1']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 05.9: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
#         expected_tooltip_list=['CAR:BMW', 'COUNTRY:W GERMANY', 'BODYTYPE:SEDAN', 'LENGTH:1,121', 'COUNTRY:W GERMANY', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s33!g4!mbar!', expected_tooltip_list, 'Step 05.10: verify the default tooltip values')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(1)
        metadataobj.verify_query_pane_field('Vertical Axis','SEATS',1,"Step 05.11: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','LENGTH',2,"Step 05.12: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','WIDTH',3,"Step 05.13: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','WHEELBASE',4,"Step 05.14: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','FUEL_CAP',5,"Step 05.15: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','BHP',6,"Step 05.16: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','MPG',7,"Step 05.17: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','ACCEL',8,"Step 05.18: Verify query pane")
        
        """
        Step 06:Move all 8 fields from the Vertical axis area to the Tooltip area.
        Expect to see all 8 fields now under the Tooltip area in the Preview pane.
        """
        metadataobj.drag_and_drop_query_items("SEATS", "Tooltip")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'SEATS', 50)
        metadataobj.drag_and_drop_query_items("LENGTH", "SEATS")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'LENGTH', 50)
        metadataobj.drag_and_drop_query_items("WIDTH", "LENGTH")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WIDTH', 50)
        metadataobj.drag_and_drop_query_items("WHEELBASE", "WIDTH")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WHEELBASE', 50)
        metadataobj.drag_and_drop_query_items("FUEL_CAP", "WHEELBASE")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'FUEL_CAP', 50)
        metadataobj.drag_and_drop_query_items("BHP", "FUEL_CAP")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'BHP', 50)
        metadataobj.drag_and_drop_query_items("MPG", "BHP")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'MPG', 50)
        metadataobj.drag_and_drop_query_items("ACCEL", "MPG")
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        utillobj.synchronize_with_visble_text(parent_css, 'ACCEL', 50)
        time.sleep(1)
        metadataobj.verify_query_pane_field('Tooltip','SEATS',1,"Step 06.1: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','LENGTH',2,"Step 06.2: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WIDTH',3,"Step 06.3: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WHEELBASE',4,"Step 06.4: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','FUEL_CAP',5,"Step 06.5: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','BHP',6,"Step 06.6: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','MPG',7,"Step 06.7: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','ACCEL',8,"Step 06.8: Verify query pane")
        
        """
         Step 07:Add new fields 
        DEALER_COST, RETAIL_COST, SALES & RPM 
        to the Vertical axis area.
        Expect to see Preview pane, now with
        DEALER_COST, RETAIL_COST, SALES & RPM under the Vertical axis area.
        """
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, 'DEALER_COST', 50)
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COST', 50)
        metadataobj.datatree_field_click('SALES', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        utillobj.synchronize_with_visble_text(parent_css, 'SALES', 50)
        metadataobj.datatree_field_click('RPM', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_visble_text(parent_css, 'RPM', 50)
        time.sleep(2)
        metadataobj.verify_query_pane_field('Vertical Axis','DEALER_COST',1,"Step 07.1: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','RETAIL_COST',2,"Step 07.2: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','SALES',3,"Step 07.3: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','RPM',4,"Step 07.4: Verify query pane")
       
        """
         Step 08:Click the Run button.
                 
        Expect to see the following Streamgraph, 
        now with 
        4 Vertical axis and 
        3 Horizontal axis fields.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_ft", 1, 60)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES, RPM, SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY, CAR, COUNTRY, BODYTYPE", "Step 08.1 : Verify chart title ")
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'MASERATI : ITALY : COUPE', 'DATSUN : JAPAN : SEDAN', 'TOYOTA : JAPAN : SEDAN','JAGUAR : ENGLAND : SEDAN','JENSEN : ENGLAND : SEDAN','ALFA ROMEO : ITALY : ROADSTER','ALFA ROMEO : ITALY : COUPE','AUDI : W GERMANY : SEDAN','JAGUAR : ENGLAND : CONVERTIBLE']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.2: Verify XY labels")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 08.3: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 52, 'Step 08.4: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g7!mbar!', 'med_green', 'Step 08.5: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'SALES:ENGLAND', 'RPM:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'SALES:FRANCE', 'RPM:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'SALES:ITALY', 'RPM:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'SALES:JAPAN', 'RPM:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY', 'SALES:W GERMANY', 'RPM:W GERMANY']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 08.9 Verify Legends ')
        expected_datalabel=['189K', '61,500', '54,...', '47...', '42...','3...', '2', '2', '2', '2','1','1']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 03.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        utillobj.switch_to_default_content(pause=3)
        time.sleep(1)
        metadataobj.verify_query_pane_field('Tooltip','SEATS',1,"Step 06.1: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','LENGTH',2,"Step 06.2: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WIDTH',3,"Step 06.3: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WHEELBASE',4,"Step 06.4: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','FUEL_CAP',5,"Step 06.5: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','BHP',6,"Step 06.6: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','MPG',7,"Step 06.7: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','ACCEL',8,"Step 06.8: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','DEALER_COST',1,"Step 07.1: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','RETAIL_COST',2,"Step 07.2: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','SALES',3,"Step 07.3: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','RPM',4,"Step 07.4: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 08.1: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 08.2: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','BODYTYPE',3,"Step 08.3: Verify query pane")
        
        """
         Step 09:Hover over the lower area(green) for Maserati.
         Expect to see the following Tooltip information, combining all Vertical axis fields, the applicable Horizontal fields and the 8 Tooltip fields.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_f", 1, 60)
#         expected_tooltip_list=['CAR:MASERATI', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:25,000', 'COUNTRY:ITALY', 'SEATS:2', 'LENGTH:177', 'WIDTH:69', 'WHEELBASE:102.3', 'FUEL_CAP:25.0', 'BHP:315', 'MPG:0', 'ACCEL:6', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s8!g9!mbar!', expected_tooltip_list, 'Step 05.10: verify the default tooltip values')
        time.sleep(2)   
        utillobj.switch_to_default_content(pause=2)        
        ele=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 10 http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
             
        
if __name__ == '__main__':
    unittest.main()