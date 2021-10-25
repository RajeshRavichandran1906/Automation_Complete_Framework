'''
Created on 12-Sep-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10670
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2312985
TestCase Name = AHTML: StreamGraph basic procedure creation.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon, ia_resultarea, active_miscelaneous

class C2312985_TestClass(BaseTestCase):

    def test_C2312985(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2312985'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
            
        """ 
        Step 1: Launch new chart using the IA API
        http://machine:port/{alias}/ia?tool=chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamGraphBucketizedCharts
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/car', 'S10670', 'mrid', 'mrpass')
        parent_css = "#TableChart_1 text[class]"
        utillobj.synchronize_with_number_of_element(parent_css, 16, 65)
          
        """ 
            Step 2: Select Active Report.
            Click the Format tab and select Other.
            Select the HTML5 group, then select Streamgraph.
            Click OK.
        """
        ribbonobj.change_output_format_type('active_report')
        time.sleep(2)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'ActiveReport', 15)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'stream_graph', 3, ok_btn_click=True)
        time.sleep(5)
          
        """ 
            Expect to see the following Preview pane for Streamgraph.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval_list=[]
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3: Verify XY Label')
        expected_label_list=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 3.1 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s4!g0!marea', 'brick_red', 'Step 3.2: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 3.3: Verify Number of riser', custom_css="path[class^='riser']")
          
          
        """ 
            Step 3: Add fields CAR to the Horizontal axis, then DEALER_COST & RETAIL_COST to the Vertical axis
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        parent_css="#TableChart_1 text.xaxisOrdinal-title"
        utillobj.synchronize_with_visble_text(parent_css, 'CAR', 10)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(parent_css, 'DEALER_COST', 10)
        
        metadataobj.datatree_field_click('RETAIL_COST', 2, 1)
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COST', 10)
          
        """ 
            Expect to see the following Preview pane.
        """
        result_obj.verify_xaxis_title("TableChart_1", 'CAR', "Step 5.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 5.2: Verify XY Label')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 5.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!marea', 'bar_green', 'Step 5.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!marea', 'bar_blue1', 'Step 5.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 5.6: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_5")
        time.sleep(1)
#          
        """ 
            Step 4: Click the Run button.
            Expect to see the following Active Streamgraph.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 6.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 6.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 6.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 6.4: Verify Color')
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST BY CAR', 'Step 6.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 6.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 6.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 6.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_6")
          
        """ 
            Step 5: Save & close the IA procedure as StreamBasic.
        """
        time.sleep(1)
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 6 :    
            Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()