'''
Created on November 28, 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234978
TestCase Name = Verify user can change the aggregation type of the Measure to Count
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup
from common.lib import utillity

class C2204978_TestClass(BaseTestCase):

    def test_C2204978(self):
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        acroll= active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """ Step 1: Upload "C2204978.fex" in IA.
            Open fex in edit mode using 'Edit with InfoAssist' option.
            Chart will be opened in edit mode in Live Preview pane.
        """
        utillobj.infoassist_api_edit("C2204978",'Chart','S7074',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 .chartPanel", 1, 65)
        
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval1_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        resobj.verify_xaxis_title("TableChart_1","Category : Product","Step 01.02 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1","Unit Sales","Step 01.03: Verify yaxis title")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 01.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 01.05: Verify  riser color")        

        """Step 2:
        Right click on bar chart. Select Data Labels > Show
        """
        parent_css="#TableChart_1 .chartPanel g rect[class*='riser!s0!g0!mbar!']"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        utillobj.default_click(parent_obj, click_option=1)
#         utillobj.click_type_using_pyautogui(parent_obj, rightClick=True)
        parent_css="#FieldFilter [class*='label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Filter', 10)
       
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
        resobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 02.06: Verify labels",custom_css="svg g.datalabels text")

        """ Step 3:Verify Data will be displayed on top of each sample bar
               Under Query pane, Measure is set to SUM by default. Right click Measure
        Verify SUM is auto-selected.
        Verify PRINT, COUNT and LIST are displayed below SUM option
        Step 4:Change Measure from SUM to PRINT option.
        """
        
        metadataobj.querytree_field_click('Chart (ggsales)',1,1)
        utillobj.select_or_verify_bipop_menu('Print', verify=True,expected_popup_list=['Rename', 'Sum', 'Print', 'Count'], expected_ticked_list=['Sum'],msg="Step 03.01:Verify Aggregation option")
        
        """ Step 5:
        Now Click Run option.
        Verify Chart displays Data labels for default aggregation option SUM.        
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", "Category : Product", 15)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 05.01 : Verify chart title ")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 4317, 'Step 05.02: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 05.03: Verify  riser color")
        
        expected_datalabel=['1,387']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 05.04: Verify labels",custom_css=".chartPanel text[class^='dataLabels!s0!g0!mdataLabels!']")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.05: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Detail'],"Step 05.07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product","Step 05.08: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales","Step 05.09: Verify yaxis title")
        
        """Step 6:
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
        utillobj.asequal(expected_menu_list, actual_menu_list, "Step 06.01: Verify that calculation list shows 6 options for Numeric field ")  
    
        """ Step 7:
        Change the Aggregation to Count.
        Expect to see counts of 1 for each bar, as the aggregation has already been done.
        """
                
        acroll.select_aggregate_function("MAINTABLE_wmenu0",0, 'Count',3, verify=True)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 07.01: Verify chart title ")
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone', 'Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug', 'Gifts : Thermos']
        expected_yval1_list=['0', '200', '400', '600', '800', '1,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 07.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 07.04: Verify  riser color")
        
        expected_datalabel=['197', '333', '910', '424', '673', '343', '285', '288', '576', '288']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel, "Step 07.05: Verify labels",custom_css="svg g.datalabels text")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.06: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Count'],"Step 07.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_xaxis_title("MAINTABLE_wbody0","Category : Product","Step 07.09: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales","Step 07.10: Verify yaxis title")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)        
       
if __name__ == '__main__':
    unittest.main()