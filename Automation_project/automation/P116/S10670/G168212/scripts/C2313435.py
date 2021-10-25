'''
Created on Oct 12, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case =http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313435
TestCase Name = AHTML: Mekko Chart Basic chart limit tests.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata
from common.lib import utillity

class C2313435_TestClass(BaseTestCase):

    def test_C2313435(self):
        
        Test_Case_ID="C2313435"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        """
            Step 01:Open FEX:
                 
            http://machine:port/ibiapps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FMekkoBucketizedCharts%2FMekkoBasic.fex&tool=Char
        """
        utillobj.infoassist_api_edit("Mekko_Basic", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1,expire_time=50)
        
        """
            Step 02:Add additional Horizontal (X-axis) fields:
                    COUNTRY & MODEL.
            Expect to see the following Active Mekko Preview pane.
        """
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True, expire_time=25)
        metadataobj.datatree_field_click('MODEL', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        resobj.wait_for_property(parent_css, 1, string_value='MODEL', with_regular_exprestion=True, expire_time=25)
        resobj.verify_xaxis_title("TableChart_1", 'CAR : COUNTRY : MODEL', "Step 02.1: Verify X-Axis Title")
        expected_xval_list=['MASERATI : ITALY : DORA 2 DOOR', 'JENSEN : ENGLAND : INTERCEPTOR III', 'BMW : W GERMANY : 3.0 SI 4 DOOR AUTO', 'JAGUAR : ENGLAND : XJ12L AUTO', 'BMW : W GERMANY : 3.0 SI 4 DOOR', 'BMW : W GERMANY : 530I 4 DOOR AUTO', 'BMW : W GERMANY : 530I 4 DOOR', 'JAGUAR : ENGLAND : V12XKE AUTO', 'ALFA ROMEO : ITALY : 2000 SPIDER VELOCE', 'ALFA ROMEO : ITALY : 2000 GT VELOCE', 'BMW : W GERMANY : 2002 2 DOOR AUTO', 'BMW : W GERMANY : 2002 2 DOOR', 'AUDI : W GERMANY : 100 LS 2 DOOR AUTO', 'ALFA ROMEO : ITALY : 2000 4 DOOR BERLINA', 'PEUGEOT : FRANCE : 504 4 DOOR', 'TRIUMPH : ENGLAND : TR7', 'TOYOTA : JAPAN : COROLLA 4 DOOR DIX AUTO', 'DATSUN : JAPAN : B210 2 DOOR AUTO']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.2: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("TableChart_1", 1, 36, 'Step 02.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 02.4: Verify Color')                  
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 02.5: Verify Legends ')       
        expected_datalabel=['56,500', '32,790', '25,123', '24,685', '23,752', '17,895', '17,397', '16,305', '12,480', '12,480', '12,355', '11,740', '11,033', '10,840', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 02.6: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 02.7: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 02.8: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','MODEL',3,"Step 02.9: Verify query pane")
          
        """
            Step 03:Add BODYTYPE to the Horizontal axis.
                     
                    Expect to see BODYTYPE replace MODEL as the third Horizontal field. Limit is 3 fields.
        """
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        resobj.wait_for_property(parent_css, 1, string_value='BODYTYPE', with_regular_exprestion=True)
        resobj.verify_xaxis_title("TableChart_1", 'CAR : COUNTRY : BODYTYPE', "Step 03.1: Verify X-Axis Title")
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'MASERATI : ITALY : COUPE', 'JENSEN : ENGLAND : SEDAN', 'JAGUAR : ENGLAND : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'AUDI : W GERMANY : SEDAN', 'ALFA ROMEO : ITALY : SEDAN', 'PEUGEOT : FRANCE : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP', 'TOYOTA : JAPAN : SEDAN', 'DATSUN : JAPAN : SEDAN']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.2: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("TableChart_1", 1, 26, 'Step 03.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 03.3: Verify Color')                  
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 3.4: Verify Legends ')       
        expected_datalabel=['108K', '56,500', '32,790', '24,685', '16,305', '12,480', '12,480', '11,033', '10,840', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 03.5: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 03.6: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 03.7: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','BODYTYPE',3,"Step 03.8: Verify query pane")
 
        """
            Step 04:Click the Run button.
                    Hover over the lower area(blue) for BMW.
         
            Expect to see the following Tooltip information confirming that CAR, COUNTRY & BODYTYPE are shown,
            since all values are not visible in the chart X-axis labels.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5) 
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'MASERATI : ITALY : COUPE', 'JENSEN : ENGLAND : SEDAN', 'JAGUAR : ENGLAND : SEDAN','JAGUAR : ENGLAND : CONVERTIBLE','ALFA ROMEO : ITALY : COUPE','ALFA ROMEO : ITALY : ROADSTER','AUDI : W GERMANY : SEDAN','ALFA ROMEO : ITALY : SEDAN','PEUGEOT : FRANCE : SEDAN','TRIUMPH : ENGLAND : HARDTOP','TOYOTA : JAPAN : SEDAN','DATSUN : JAPAN : SEDAN']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.1: Verify XY labels")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 04.2: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 26, 'Step 04.3: Verify the total number of risers displayed on run')
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST by CAR, COUNTRY, BODYTYPE", "Step 04.4 : Verify chart title ")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g8!mbar!', 'pale_green', 'Step 04.5: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 04.9 Verify Legends ')
        expected_datalabel=['108K', '56,500', '32,790', '24,685', '16,305', '12,480', '12,480', '11,033', '10,840', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 04.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        expected_tooltip_list=['CAR:BMW', 'COUNTRY:W GERMANY', 'BODYTYPE:SEDAN', 'DEALER_COST:49,500  (45.72%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g4!mbar!', expected_tooltip_list, 'Step 04.11: verify the default tooltip values')
        time.sleep(2)
 
        """
            Step 05:Remove Measure(Vertical axis) fields DEALER_COST & RETAIL_COST.
                    Add new Measure fields:SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL.
                    Click the Run button.
             
            Expect to see all 8 Vertical axis fields appear both on the chart and as entries in the chart legend.
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        metadataobj.querytree_field_click('DEALER_COST', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.querytree_field_click('RETAIL_COST', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.datatree_field_click('SEATS', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='SEATS', with_regular_exprestion=True)
        metadataobj.datatree_field_click('LENGTH', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1, string_value='LENGTH', with_regular_exprestion=True)
        metadataobj.datatree_field_click('WIDTH', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        resobj.wait_for_property(parent_css, 1, string_value='WIDTH', with_regular_exprestion=True)
        metadataobj.datatree_field_click('WHEELBASE', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='WHEELBASE', with_regular_exprestion=True)
        metadataobj.datatree_field_click('FUEL_CAP', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='FUEL_CAP', with_regular_exprestion=True)
        metadataobj.datatree_field_click('BHP', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        resobj.wait_for_property(parent_css, 1, string_value='BHP', with_regular_exprestion=True)
        metadataobj.datatree_field_click('MPG', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(10) td"
        resobj.wait_for_property(parent_css, 1, string_value='MPG', with_regular_exprestion=True)
        metadataobj.datatree_field_click('ACCEL', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(11) td"
        resobj.wait_for_property(parent_css, 1, string_value='ACCEL', with_regular_exprestion=True)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)        
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'JAGUAR : ENGLAND : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'AUDI : W GERMANY : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP', 'TOYOTA : JAPAN : SEDAN', 'DATSUN : JAPAN : SEDAN', 'PEUGEOT : FRANCE : SEDAN', 'ALFA ROMEO : ITALY : SEDAN', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : COUPE']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.1: Verify XY labels")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 05.2: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 104, 'Step 05.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g8!mbar!', 'pale_green', 'Step 05.4: Verify Color')
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by CAR, COUNTRY, BODYTYPE", "Step 03.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['SEATS', 'LENGTH', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 05.8 Verify Legends ')
        expected_datalabel=['2,388', '793.5', '696.9', '668.8', '644.4', '512.8', '447.2', '439.5', '434.5', '397.9', '378.3', '359.1', '355.1']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 05.9: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        expected_tooltip_list=['CAR:BMW', 'COUNTRY:W GERMANY', 'BODYTYPE:SEDAN', 'SEATS:29', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g4!mbar!', expected_tooltip_list, 'Step 05.10: verify the default tooltip values')
        time.sleep(2)
         
 
        """
            Step 06:Move all 8 fields from the Vertical axis area to the Tooltip area.
             
            Expect to see all 8 fields now under the Tooltip area in the Preview pane.
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        metadataobj.drag_and_drop_query_items("SEATS", "Tooltip")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='SEATS', with_regular_exprestion=True)
        metadataobj.drag_and_drop_query_items("LENGTH", "SEATS")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='LENGTH', with_regular_exprestion=True)
        metadataobj.drag_and_drop_query_items("WIDTH", "LENGTH")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='WIDTH', with_regular_exprestion=True)
        metadataobj.drag_and_drop_query_items("WHEELBASE", "WIDTH")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='WHEELBASE', with_regular_exprestion=True)
        metadataobj.drag_and_drop_query_items("FUEL_CAP", "WHEELBASE")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='FUEL_CAP', with_regular_exprestion=True)
        metadataobj.drag_and_drop_query_items("BHP", "FUEL_CAP")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='BHP', with_regular_exprestion=True)
        metadataobj.drag_and_drop_query_items("MPG", "BHP")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='MPG', with_regular_exprestion=True)
        metadataobj.drag_and_drop_query_items("ACCEL", "MPG")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='ACCEL', with_regular_exprestion=True)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Tooltip','SEATS',1,"Step 06.1: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','LENGTH',2,"Step 06.2: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WIDTH',3,"Step 06.3: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WHEELBASE',4,"Step 06.4: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','FUEL_CAP',5,"Step 06.5: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','BHP',6,"Step 06.6: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','MPG',7,"Step 06.7: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','ACCEL',8,"Step 06.8: Verify query pane")    
        resobj.verify_xaxis_title("TableChart_1", 'CAR : COUNTRY : BODYTYPE', "Step 06.9: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 06.10: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("TableChart_1", 1, 13, 'Step 02.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 06.11: Verify Color')                  
        expected_datalabel=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 06.12: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        """
            Step 07:Add new fields DEALER_COST, RETAIL_COST, SALES & RPM to the Vertical axis area.
             
            Expect to see Preview pane, now with DEALER_COST, RETAIL_COST, SALES & RPM under the Vertical axis area.
        """
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='DEALER_COST', with_regular_exprestion=True)
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1, string_value='RETAIL_COST', with_regular_exprestion=True)
        metadataobj.datatree_field_click('SALES', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        resobj.wait_for_property(parent_css, 1, string_value='SALES', with_regular_exprestion=True)
        metadataobj.datatree_field_click('RPM', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='RPM', with_regular_exprestion=True)
        time.sleep(3)
        metadataobj.verify_query_pane_field('Vertical Axis', 'DEALER_COST', 1, "Step 07.1:")
        metadataobj.verify_query_pane_field('Vertical Axis', 'RETAIL_COST', 2, "Step 07.2:")
        metadataobj.verify_query_pane_field('Vertical Axis', 'SALES', 3, "Step 07.3:")
        metadataobj.verify_query_pane_field('Vertical Axis', 'RPM', 4, "Step 07.4:")
        resobj.verify_xaxis_title("TableChart_1", 'CAR : COUNTRY : BODYTYPE', "Step 07.5: Verify X-Axis Title")
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'MASERATI : ITALY : COUPE', 'DATSUN : JAPAN : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : COUPE', 'AUDI : W GERMANY : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'ALFA ROMEO : ITALY : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP', 'PEUGEOT : FRANCE : SEDAN']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 07.6: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("TableChart_1", 1, 52, 'Step 07.7: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 03.3: Verify Color')                  
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 07.8: Verify Legends ')       
        expected_datalabel=['189K', '61,500', '54,765', '47,055', '42,435', '37,490', '25,480', '24,880', '24,333', '22,055', '15,6...', '14,...', '10...']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 07.8: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
 
        """
            Step 08:Click the Run button.Expect to see the following Mekko Chart, now with 
                    4 Vertical axis and 3 Horizontal axis fields.8 Tool tip fields.
        """
        time.sleep(3)
        metadataobj.verify_query_pane_field('Vertical Axis', 'DEALER_COST', 1, "Step 08.1:")
        metadataobj.verify_query_pane_field('Vertical Axis', 'RETAIL_COST', 2, "Step 8.2:")
        metadataobj.verify_query_pane_field('Vertical Axis', 'SALES', 3, "Step 08.3:")
        metadataobj.verify_query_pane_field('Vertical Axis', 'RPM', 4, "Step 08.4:")  
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 08.5: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 08.6: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','BODYTYPE',3,"Step 08.7: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','SEATS',1,"Step 08.8: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','LENGTH',2,"Step 08.9: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WIDTH',3,"Step 08.10: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WHEELBASE',4,"Step 08.11: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','FUEL_CAP',5,"Step 08.12: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','BHP',6,"Step 08.12: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','MPG',7,"Step 08.13: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','ACCEL',8,"Step 08.14: Verify query pane") 
        time.sleep(3)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)       
        expected_xval_list=['BMW : W GERMANY : SEDAN', 'MASERATI : ITALY : COUPE', 'DATSUN : JAPAN : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : COUPE', 'AUDI : W GERMANY : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'ALFA ROMEO : ITALY : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP', 'PEUGEOT : FRANCE : SEDAN']
        expected_yval1_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.15: Verify XY labels")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 08.16: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 52, 'Step 08.17: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g8!mbar!', 'pale_green', 'Step 08.18: Verify Color')
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES, RPM, SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by CAR, COUNTRY, BODYTYPE", "Step 08.19: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.20: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.21: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.22: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST','SALES','RPM']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 08.23: Verify Legends ')
        expected_datalabel=['189K', '61,500', '54,765', '47,055', '42,435', '37,490', '25,480', '24,880', '24,333', '22,055', '15,6...', '14,...', '10...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 08.24: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']")
        """
            Step 09:Hover over the lower area(blue) for BMW.
            
            Expect to see the following Tooltip information, combining all Vertical axis fields, the applicable Horizontal fields and the 8 Tooltip fields.
        """
        time.sleep(3)
        expected_tooltip_list=['CAR:BMW', 'COUNTRY:W GERMANY', 'BODYTYPE:SEDAN', 'DEALER_COST:49,500  (26.24%)', 'SEATS:29', 'LENGTH:1,122', 'WIDTH:397', 'WHEELBASE:616.4', 'FUEL_CAP:103.2', 'BHP:0', 'MPG:120', 'ACCEL:0', 'Filter Chart', 'Exclude from Chart']        
        resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g4!mbar!', expected_tooltip_list, 'Step 09.1: verify the default tooltip values')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_07', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)

        """
            Step 10:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)

        
if __name__ == '__main__':
    unittest.main()