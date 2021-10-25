'''
Created on Nov 8, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case= http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2335961
TestCase Name =PIE chart feeler options from IA..
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_resultarea
from common.lib import utillity

class C2335961_TestClass(BaseTestCase):

    def test_C2335961(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2335961'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        
        """
        Step 01: Launch new chart using the IA API
        http://machine:port/{alias}/ia?tool=chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS7074%2FCHART-LAYOUT
        Create a new Chart using the Car file.Select Active Report as the output type.
        Select PIE chart.Expect to see the following PIE chart Preview pane.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/car','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(4)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        ribbonobj.select_ribbon_item('Format', 'Pie')
        time.sleep(5)
        
        """
        Step 02: Add Car to the Color bucket.Add Dealer_Cost to the Maasure bucket.
        Click the Run button.Expect to see the following PIE chart.
        """
         
        metadataobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        result_obj.wait_for_property(parent_css, 1, string_value='CAR', with_regular_exprestion=True)
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        result_obj.wait_for_property(parent_css, 1, string_value='DEALER_COST', with_regular_exprestion=True)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
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
          
        """
        Step 03: Click the Series button at the top.
        Click the Data Labels down arrow.Click Outside Slice.
        Click the Run button.Expect to see Percentages for each slice outside of the PIE Chart.
        """
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_ribbon_item('Series','data_labels_menubtn',opt='Outside Slice')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
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
        expected_datalabel=['11%', '4%', '34%', '2%', '13%', '10%', '17%', '3%', '2%', '3%']
        result_obj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 03.10: Verify datalabels ',custom_css=".chartPanel text[class^='dataLabels']") 
        
        """
        Step 04: Click the Data labels down arrow again.Click Outside with Feeler Lines.
        Click the Run button.Expect to see Feelers and Percentages for each slice outside of the PIE Chart.
        """
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        ribbonobj.select_ribbon_item('Series','data_labels_menubtn',opt='Outside with feeler lines')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
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
        expected_datalabel=['11%', '4%', '34%', '2%', '13%', '10%', '17%', '3%', '2%', '3%']
        result_obj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 04.10: Verify datalabels ',custom_css=".chartPanel text[class^='dataLabels']") 
        
        
        """
        Step 05: Click the Data labels down arrow again.
        Click On Slice.Click the Run button.
        Expect to see Percentages for each slice inside the PIE Chart.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        ribbonobj.select_ribbon_item('Series','data_labels_menubtn',opt='On Slice')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by CAR", "Step 05.1 : Verify chart title ")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 05.2: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.3: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05.6: Verify Legends ')
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500  (34.42%)', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s2!g0!mwedge!', expected_tooltip_list, 'Step 05.7: verify the default tooltip values')
        time.sleep(2)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['DEALER_COST'], "Step 05.8:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 05.9: Verify number of pie")
        expected_datalabel=['11%', '4%', '34%', '2%', '13%', '10%', '17%', '3%', '2%', '3%']
        result_obj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 05.10: Verify datalabels ',custom_css=".chartPanel text[class^='dataLabels']") 
        time.sleep(2)   
        utillobj.switch_to_default_content(pause=2)        
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
                
if __name__ == '__main__':
    unittest.main()