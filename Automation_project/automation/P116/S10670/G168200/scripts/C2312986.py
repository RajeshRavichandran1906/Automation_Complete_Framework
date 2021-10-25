'''
Created on Sep 13, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2312986
TestCase Name = AHTML: StreamGraph ColorBy procedure creation.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2312986_TestClass(BaseTestCase):

    def test_C2312986(self):
        
        Test_Case_ID="C2312986"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_ribbobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
            
        """   
            Step 01:Launch new chart using the IA API
            http://machine:port/{alias}/ia?tool=chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamGraphBucketizedCharts
            
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/car', 'P116/S10670', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel g.risers"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
     
        """
            Step 02:Select Active Report.
            Click the Format tab and select Other.
            Select the HTML5 group, then select Streamgraph.
            Click OK.
        """
         
        ribbonobj.change_output_format_type('active_report', location='Home')
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(5)
        ia_ribbobj.select_other_chart_type('html5', 'stream_graph', 3, ok_btn_click=True)
        time.sleep(3)
        
        """
            Expect to see the following Preview pane for Streamgraph.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.01: Verify XY Label')
        expected_label_list=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 02.02: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s4!g0!marea', 'brick_red', 'Step 02.03: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 02.04: Verify Number of riser', custom_css="path[class^='riser']")
        
        """
            Step 03:Add fields CAR to the Horizontal axis, then DEALER_COST & RETAIL_COST to the Vertical axis
        """
         
        metadataobj.datatree_field_click('CAR', 2, 1)
        parent_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, 'CAR', 15)

        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(parent_css, 'DEALER_COST', 15)

        metadataobj.datatree_field_click('RETAIL_COST', 2, 1)
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COST', 15)
        
        """
            Expect to see the following Preview pane.
        """
        resobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 03.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.02: Verify XY Label')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03.03: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!marea', 'bar_green', 'Step 03.04: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!marea', 'bar_blue1', 'Step 03.05: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 03.06: Verify Number of riser', custom_css="path[class^='riser']")
        
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_03")
        time.sleep(1)
        
        """
            Step 04:Drag field COUNTRY to the Color area under Marker in the design pane.
        """
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Color',0)
        parent_css="#queryTreeWindow table tr:nth-child(10) td"
        utillobj.synchronize_with_visble_text(parent_css, 'COUNTRY', 15)
        
        """
            Expect to see the following Preview pane, with Color By added to the design pane.
            Also expect to see the Color By appear as distinct entries in the chart legend.
        """

        resobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 04.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04.02: Verify XY Label')
        expected_label_list=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE','DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 04.03: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!marea', 'bar_green', 'Step 04.04: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!marea', 'bar_blue1', 'Step 04.05: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s4!g0!marea', 'brick_red', 'Step 04.06: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 10, 'Step 04.07: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_04")
        time.sleep(1)
        
        """
            Step 05:Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", "CAR", 25)
        
        """
            Expect to see the following Active Streamgraph
        """
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.02: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 05.03: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 05.04: Verify Color')

        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by COUNTRY, CAR', 'Step 05.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_05")
        time.sleep(1)
         
        """
            Step 06: Save & close the IA procedure as StreamColorBy.
        """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
            Step 07: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        

if __name__ == '__main__':
    unittest.main()
