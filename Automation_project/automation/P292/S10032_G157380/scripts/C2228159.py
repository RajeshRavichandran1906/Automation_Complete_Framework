'''
Created on Dec 20, 2017

@author: BM13368
TestCase ID:http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2228159
TestCase Name:Verify Pie chart and the output from outside the tool (82xx)
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity

class C2228159_TestClass(BaseTestCase):

    def test_C2228159(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228159'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        
        """
            Step 01:Launch WF, New > Chart with CAR.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10032_chart_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 02:Double click "COUNTRY","CAR","DEALER_COST","RETAIL_COST".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resultobj.wait_for_property(parent_css, 1)
         
        """  
            Step 03:Select "Format" > "Chart Types" > "Pie".
        """
        ribbonobj.select_ribbon_item("Format", "Pie")
        """  
            Step 04:Verify the following chart is displayed.
        """
        parent_css="#TableChart_1 [class*='colHeader']"
        resultobj.wait_for_property(parent_css, 1, )
        expected_label_list=['DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_riser_pie_labels_and_legends("TableChart_1", expected_label_list,"Step 04:01: Verify top level labels", same_group=True)
        resultobj.verify_number_of_pie_segments("TableChart_1", 1, 0, 'Step 04:02: Verify the total number of pie chart segment')
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g1!mwedge!r0!c4!", "dark_green", "Step 04:03: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g1!mwedge!r0!c4!", "pale_green", "Step 04:04: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g1!mwedge!r0!c3!", "pale_yellow", "Step 04:05: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mwedge!r0!c2!", "lochmara", "Step 04:06: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s7!g1!mwedge!r0!c1!", "tea_green", "Step 04:07: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g1!mwedge!r0!c0!", "brick_red", "Step 04:08: Verify first bar color")
        resultobj.verify_riser_legends('TableChart_1',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 04.09 : Verify chart legends')
        resultobj.verify_xaxis_title("TableChart_1", "COUNTRY", "Step 04:11: Verify colheader label COUNTRY is shown", custom_css="[class*='colHeader']")
        """
            Step 05:Select "Series" > "Data Labels".
        """
        ribbonobj.select_ribbon_item("Series", "data_labels")
         
        """  
            Step 06:Verify the following chart is displayed.
        """
        parent_css="#TableChart_1 svg > g.chartPanel text[class*='mdataLabels']"
        resultobj.wait_for_property(parent_css, 20)
        expected_label_list=['DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_riser_pie_labels_and_legends("TableChart_1", expected_label_list,"Step 06:01: Verify top level labels", same_group=True) 
        resultobj.verify_number_of_pie_segments("TableChart_1", 1, 0, 'Step 06:02: Verify the total number of pie chart segment')
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g1!mwedge!r0!c4!", "dark_green", "Step 06:03: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g1!mwedge!r0!c4!", "pale_green", "Step 06:04: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g1!mwedge!r0!c3!", "pale_yellow", "Step 06:05: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mwedge!r0!c2!", "lochmara", "Step 06:06: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s7!g1!mwedge!r0!c1!", "tea_green", "Step 06:07: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g1!mwedge!r0!c0!", "brick_red", "Step 06:08: Verify first bar color")
        resultobj.verify_riser_legends('TableChart_1',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 06.09 : Verify chart legends')
        expected_datalabel=['49%', '39%', '11%', '49%', '39%', '11%', '100%', '100%', '39%', '61%', '38%', '62%', '48%', '52%', '48%', '52%', '9%', '91%', '9%', '91%']
        total_datalabel=driver.find_elements_by_css_selector("#TableChart_1 svg > g.chartPanel text[class*='mdataLabels']")
        actual_datalabel_list=[el.text.strip() for el in total_datalabel]
        print(actual_datalabel_list)
        utillobj.asequal(expected_datalabel, actual_datalabel_list, "Step 06:11: Verify the x-labels visible in the top of the pie chart")
        time.sleep(2)
        resultobj.verify_xaxis_title("TableChart_1", "COUNTRY", "Step 06:12: Verify colheader label COUNTRY is shown", custom_css="[class*='colHeader']")
        top_level_x_labels=driver.find_elements_by_css_selector("#TableChart_1 svg>g text[class*='colLabel']")
        actual_top_x_labels=[el.text.strip() for el in top_level_x_labels]
        expected_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        utillobj.asequal(expected_list, actual_top_x_labels, "Step 06:13: Verify the x-labels visible in the top of the pie chart")
         
        """ 
            Step 07:Select "View" > "Output Window" > "Output Location" (dropdown) > "New Window".
        """
        ribbonobj.select_ribbon_item("View", "output_location")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("New Window")
        time.sleep(1)
        """ 
            Step 08:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        """  
            Step 09:Verify the following chart is displayed.
        """
        parent_css="#jschart_HOLD_0 svg > g.chartPanel text[class*='mdataLabels']"
        resultobj.wait_for_property(parent_css, 20)
        expected_label_list=['DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_riser_pie_labels_and_legends("jschart_HOLD_0", expected_label_list,"Step 09:01: Verify top level labels", same_group=True) 
        resultobj.verify_number_of_pie_segments("jschart_HOLD_0", 1, 0, 'Step 09:02: Verify the total number of pie chart segment')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g1!mwedge!r0!c4!", "dark_green", "Step 09:03: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mwedge!r0!c4!", "pale_green", "Step 09:04: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g1!mwedge!r0!c3!", "pale_yellow", "Step 09:05: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mwedge!r0!c2!", "lochmara", "Step 09:06: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s7!g1!mwedge!r0!c1!", "tea_green", "Step 09:07: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g1!mwedge!r0!c0!", "brick_red", "Step 09:08: Verify first bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 09.09 : Verify chart legends')
        time.sleep(1)
        expected_datalabel=['49%', '39%', '11%', '49%', '39%', '11%', '100%', '100%', '39%', '61%', '38%', '62%', '48%', '52%', '48%', '52%', '9%', '91%', '9%', '91%']
        total_datalabel=driver.find_elements_by_css_selector("#jschart_HOLD_0 svg > g.chartPanel text[class*='mdataLabels']")
        actual_datalabel_list=[el.text.strip() for el in total_datalabel]
        print(actual_datalabel_list)
        utillobj.asequal(expected_datalabel, actual_datalabel_list, "Step 09:10: Verify the x-labels visible in the top of the pie chart")
        time.sleep(2)
        resultobj.verify_xaxis_title("jschart_HOLD_0", "COUNTRY", "Step 09:11: Verify colheader label COUNTRY is shown", custom_css="[class*='colHeader']")
        time.sleep(2)
        expected_tooltip_list=['COUNTRY:W GERMANY', 'CAR:BMW', 'RETAIL_COST:58,762  (90.78%)']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s2!g1!mwedge!r0!c4!", expected_tooltip_list, "Step 09:12: Verify the tooltip value")
        time.sleep(2)
        top_level_x_labels=driver.find_elements_by_css_selector("#jschart_HOLD_0 svg>g text[class*='colLabel']")
        actual_top_x_labels=[el.text.strip() for el in top_level_x_labels]
        expected_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        utillobj.asequal(expected_list, actual_top_x_labels, "Step 09:13: Verify the x-labels visible in the top of the pie chart")
         
        """ 
            Step 10:Dismiss the "Run" window.
        """
        self.driver.close()
        """  
            Step 11:Click "IA" > "Save" > "C2021052" > "Save".
        """
        utillobj.switch_to_window(0)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """  
            Step 12:Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        """  
            Step 13:Highlight "C2021052" > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032_chart_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 svg > g.chartPanel text[class*='mdataLabels']"
        resultobj.wait_for_property(parent_css, 20)
        """  
            Step 14:Verify the following chart is displayed.
        """
        expected_label_list=['DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_riser_pie_labels_and_legends("TableChart_1", expected_label_list,"Step 14:01: Verify top level labels", same_group=True) 
        resultobj.verify_number_of_pie_segments("TableChart_1", 1, 0, 'Step 14:02: Verify the total number of pie chart segment')
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g1!mwedge!r0!c4!", "dark_green", "Step 14:03: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g1!mwedge!r0!c4!", "pale_green", "Step 14:04: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g1!mwedge!r0!c3!", "pale_yellow", "Step 14:05: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mwedge!r0!c2!", "lochmara", "Step 14:06: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s7!g1!mwedge!r0!c1!", "tea_green", "Step 14:07: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g1!mwedge!r0!c0!", "brick_red", "Step 14:08: Verify first bar color")
        resultobj.verify_riser_legends('TableChart_1',['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], 'Step 14.09 : Verify chart legends')
        expected_datalabel=['49%', '39%', '11%', '49%', '39%', '11%', '100%', '100%', '39%', '61%', '38%', '62%', '48%', '52%', '48%', '52%', '9%', '91%', '9%', '91%']
        total_datalabel=driver.find_elements_by_css_selector("#TableChart_1 svg > g.chartPanel text[class*='mdataLabels']")
        actual_datalabel_list=[el.text.strip() for el in total_datalabel]
        print(actual_datalabel_list)
        utillobj.asequal(expected_datalabel, actual_datalabel_list, "Step 14:10: Verify the x-labels visible in the top of the pie chart")
        time.sleep(2)
        resultobj.verify_xaxis_title("TableChart_1", "COUNTRY", "Step 14:11: Verify colheader label COUNTRY is shown", custom_css="[class*='colHeader']")
        top_level_x_labels=driver.find_elements_by_css_selector("#TableChart_1 svg>g text[class*='colLabel']")
        actual_top_x_labels=[el.text.strip() for el in top_level_x_labels]
        expected_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        utillobj.asequal(expected_list, actual_top_x_labels, "Step 14:12: Verify the x-labels visible in the top of the pie chart")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()