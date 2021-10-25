'''
Created on November 27, 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234975
TestCase Name = Verify user can change the aggregation type of the Measure to Avg
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C2204975_TestClass(BaseTestCase):

    def test_C2204975(self):
        
#         Test_Case_ID="C2204975"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        acroll= active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """ Step 1:Upload "C2204975.fex" in IA.
        Open fex in edit mode using 'Edit with InfoAssist' option.
        Chart will be opened in edit mode in Live Preview pane.        
        """
        utillobj.infoassist_api_edit("C2204975",'Chart','S7074',mrid='mrid', mrpass='mrpass')
#         time.sleep(5)
#         parent_css="#pfjTableChart_1 .chartPanel"
#         resobj.wait_for_property(parent_css, 1)
#         time.sleep(10)
        utillobj.synchronize_with_number_of_element( "#TableChart_1 svg g.risers >g>rect[class^='riser']", 2, 30)
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval1_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        resobj.verify_xaxis_title("TableChart_1","Category : Product","Step 01.02 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1","Unit Sales","Step 01.03: Verify yaxis title")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 01.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 01.05: Verify  riser color")
        
        
        """Step 2: Right click on bar chart. Select Data Labels > Show
        Verify the Preview pane shows sample data on the top of each bar.
        """
        
        parent_css="#TableChart_1 .chartPanel g rect[class*='riser!s0!g0!mbar!']"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        if Global_variables.browser_name == 'firefox':
            core_utils.left_click(parent_obj)
            utillobj.synchronize_with_visble_text('#FieldAggregation', 'Aggregation', 30)
            time.sleep(2)
            utillobj.click_type_using_pyautogui(parent_obj, rightClick=True)
        else:
            utillobj.click_type_using_pyautogui(parent_obj, rightClick=True)
        parent_css="#FieldFilter [class*='label']"
        resobj.wait_for_property(parent_css, 1, string_value='Filter', with_regular_exprestion=True)
        time.sleep(5)
        utillobj.select_or_verify_bipop_menu('Data Labels')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Show')
        time.sleep(2)
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval1_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.01: Verify XY labels")
        resobj.verify_xaxis_title("TableChart_1","Category : Product","Step 02.02 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1","Unit Sales","Step 02.03: Verify yaxis title")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 02.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 02.05: Verify  riser color")
        expected_datalabel=['189K','294K']
        resobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 02.7: Verify labels",custom_css="svg g.datalabels text")
        
               
        """Step 3:Right-click on Chart (ggsales) in the query panel.
        Verify SUM is the default aggregation method.
        Verify PRINT and COUNT are also displayed as aggregation options."""         
        metadataobj.querytree_field_click('Chart (ggsales)',1,1)
        utillobj.select_or_verify_bipop_menu(verify=True,expected_popup_list=['Rename', 'Sum', 'Print', 'Count'],msg="Step 03.01:Verify Aggregation option")
        
        """Step 4:
        Now Click Run option.
        Verify Chart displays Data labels for default aggregation option SUM.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
#         time.sleep(5)
        utillobj.synchronize_with_number_of_element( "#MAINTABLE_wbody0 svg g.risers >g>rect[class^='riser']", 10, 30)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 04.01 : Verify chart title ")
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone', 'Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug', 'Gifts : Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 04.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 04.04: Verify  riser color")
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 04.05: Verify bar value")
        expected_datalabel=['189K', '309K', '878K', '421K', '630K', '333K', '187K', '191K', '361K', '190K']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 04.06: Verify labels",custom_css="svg g.datalabels text")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
    
        """Step 5:
        Click aggregation icon
        Verify that calculation list shows these options for Numeric field.
        - Sum
        - Avg
        - Min
        - Max
        - Count
        - Distinct
        Note:Non-numeric field shows Count and Distinct options."""
         
        expected_menu_list=['Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct']
        actual_menu_list=[]
        acroll.click_chart_menu_bar_items('MAINTABLE_wmenu0', 3)
        time.sleep(2)
        sum_css="[id^='dt0_SUM'][id$='_x__0'][style*='block'] span[id ^='set']"
        x=self.driver.find_elements_by_css_selector(sum_css)
        for i in range(len(x)):
            actual_menu_list.append(x[i].text.strip())
        utillobj.asequal(expected_menu_list, actual_menu_list, "Step 05.01: Verify that calculation list shows 6 options for Numeric field ")  

        """Step 6:
        Change the aggregation type of the Measure to Avg
        Verify Chart displays Data labels aggregation option AVG"""
        
        acroll.select_aggregate_function("MAINTABLE_wmenu0",0, 'Avg',3, verify=True)
        
if __name__ == '__main__':
    unittest.main()