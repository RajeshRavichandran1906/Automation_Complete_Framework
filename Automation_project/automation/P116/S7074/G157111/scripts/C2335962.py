'''
Created on Nov 9, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case= http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2335962
TestCase Name =PIE chart feeler options from Fex.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea,ia_resultarea
from common.lib import utillity

class C2335962_TestClass(BaseTestCase):

    def test_C2335962(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2335962'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        
        """
        Step 01:Execute the attached repro - Feelers-Fex using the below API Url
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS7074&BIP_item=Active_Technologies/CHART-LAYOUT/Feelers-Fex.fex
        Expect to see the following PIE chart with No Feelers or Percentages.
        """
        
        utillobj.active_run_fex_api_login("Feelers-Fex.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 .legend text"
        result_obj.wait_for_property(parent_css,11)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by CAR", "Step 01.1 : Verify chart title ")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 01.2: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 01.3: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 01.6: Verify Legends ')
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (34.42%)', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s2!g0!mwedge!', expected_tooltip_list, 'Step 01.7: verify the default tooltip values')
        time.sleep(2)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['DEALER_COST'], "Step 01.8:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 01.9: Verify number of pie")
        utillobj.infoassist_api_logout()
        
        
        """
        Step 02:Edit the Fex and change the value from (0) to (1) ion the line - setPieFeelerTextDisplay(0); Save and Run.
        Expect to see Percentages and Feelers for each slice outside of the PIE Chart.
        """
        
        utillobj.active_run_fex_api_login("Feelers2-Fex.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 .legend text"
        result_obj.wait_for_property(parent_css,11)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by CAR", "Step 02.1 : Verify chart title ")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 02.2: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.3: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 02.6: Verify Legends ')
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (34.42%)', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s2!g0!mwedge!', expected_tooltip_list, 'Step 02.7: verify the default tooltip values')
        time.sleep(2)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['DEALER_COST'], "Step 02.8:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 02.9: Verify number of pie")
        utillobj.infoassist_api_logout()
        
        """
        Step 03:Edit the Fex and change the value from (1) to (2) ion the line - setPieFeelerTextDisplay(1); Save and Run.
            Expect to see only Percentages for each slice outside of the PIE Chart.
        """
        
        utillobj.active_run_fex_api_login("Feelers3-Fex.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 .legend text"
        result_obj.wait_for_property(parent_css,11)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by CAR", "Step 03.1 : Verify chart title ")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 03.2: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.3: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 03.6: Verify Legends ')
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (34.42%)', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s2!g0!mwedge!', expected_tooltip_list, 'Step 03.7: verify the default tooltip values')
        time.sleep(2)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['DEALER_COST'], "Step 03.8:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 03.9: Verify number of pie")
        utillobj.infoassist_api_logout()
        
        """
        Step 04:Edit the Fex and change the value from (2) to (3) ion the line - setPieFeelerTextDisplay(2); Save and Run.
        Expect to see Percentages for each slice inside the PIE Chart.
        """
        
        utillobj.active_run_fex_api_login("Feelers4-Fex.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 .legend text"
        result_obj.wait_for_property(parent_css,11)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by CAR", "Step 04.1 : Verify chart title ")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 04.2: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.3: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 04.6: Verify Legends ')
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (34.42%)', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s2!g0!mwedge!', expected_tooltip_list, 'Step 04.7: verify the default tooltip values')
        time.sleep(2)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['DEALER_COST'], "Step 04.8:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 04.9: Verify number of pie")
        time.sleep(3)
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()
