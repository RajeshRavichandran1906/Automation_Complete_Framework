'''
Created on Jan 24, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358895
Test_Case Name : Verify that an Inserted HTML5 Chart in an AHMTL Document works properly.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, active_miscelaneous
from common.lib import utillity

class C2358895_TestClass(BaseTestCase):

    def test_C2358895(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2358895'
        Html5_Chart_Name='Bar_HTML5'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        def verify_bar_chart(parent_id, step_num):
            visul_result.verify_xaxis_title(parent_id, 'COUNTRY', 'Step ' + step_num + '.1 : Verify X-Axis title')
            visul_result.verify_yaxis_title(parent_id, 'DEALER_COST', 'Step ' + step_num + '.2 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels(parent_id, ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], ['0', '10K', '20K', '30K', '40K', '50K', '60K'], 'Step ' + step_num + '.3 :')
            visul_result.verify_number_of_riser(parent_id, 1, 5, 'Step ' + step_num + '.4 : Verify number of bar chart risers')
            utillobj.verify_chart_color(parent_id, 'riser!s0!g0!mbar!', 'bar_blue', 'Step ' + step_num + '.5 : Verify bar chart riser color')
            
        """
            Step 01 : Using InfoAssist, create a new Chart, using CAR.
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series0', 30, 3)
        
        """
            Step 01.1 : Expect to see the following design pane for HTML5.
        """
        utillobj.verify_element_text("#HomeFormatType>div[id^='BiLabel']", 'HTML5', 'Step 01.1 : Verify Expect to see the following design pane for HTML5')
        
        """
            Step 02 : Select fields Country and Dealer_Cost.
        """
        metadata.datatree_field_click('COUNTRY',2,1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'COUNTRY', 15)
        
        metadata.datatree_field_click('DEALER_COST',2,1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='yaxis-title']", 'DEALER_COST', 15)
        
        """
            Step 02.1 : Expect to see the design pane for the default Bar Chart.
        """
        verify_bar_chart('pfjTableChart_1', '03')
        
        """
            Step 03 : Save the HTML5 Bar Chart as 'Bar_HTML5'.
        """
        visul_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Html5_Chart_Name)
        
        """
            Step 04 : Exit IA.
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 05 : Open IA again, this time for a Dashboard, again using CAR.
        """
        utillobj.infoassist_api_login('document','ibisamp/car','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame svg", 1, 30, 5)
        
        """
            Step 05.1 : Expect to see the following Dashboard design pane. Make sure that the output type is AHTML for the Dashboard.
        """
        utillobj.verify_element_text("#HomeFormatType>div[id^='BiLabel']", 'Active Report', 'Step 05.1 : Verify Expect to see the following Dashboard design pane. Make sure that the output type is AHTML for the Dashboard')
        
        """
            Step 06 : Select Country and Dealer_Cost for the Report.
        """
        metadata.datatree_field_click('COUNTRY',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'COUNTRY', 8)
        
        metadata.datatree_field_click('DEALER_COST',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(3)>td", 'DEALER_COST', 8)
        
        """
            Step 06.1 : Verify Expect to see the following Report design frame.
        """
        #iaresult.create_across_report_data_set('TableChart_1', 1, 2, 5, 2, Test_Case_ID+'DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1', 1, 2, 5, 2, Test_Case_ID+'_DataSet_01.xlsx', 'Step 06.1 : Verify preview report data')
        
        """
            Step 07 : Click the Insert button at the top of the design pane, then Existing Report.
        """
        visul_ribbon.select_ribbon_item('Insert', 'existing_report')
        
        """
            Step 08 : Select Bar_HTML5.
        """
        utillobj.ibfs_save_as(Html5_Chart_Name)
        utillobj.synchronize_with_visble_text("#pfjIncludeChart_1 text[class='yaxis-title']", 'DEALER_COST', 10)
    
        """
            Step 08.1 : Expect to see the Inserted Bar Chart. Move the Bar Chart to the right, so the report appears.
        """
        verify_bar_chart('pfjIncludeChart_1', '08')
        visul_ribbon.repositioning_document_component('4', '1.04')
        
        """
            Step 09 : Click the Run button.
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 25, string_value='COUNTRY')
        
        """
            Step 09.1 : Expect to see the following Dashboard, with no execution errors.
        """
        verify_bar_chart('MAINTABLE_wbody1_f', '09')
        active.verify_chart_title('MAINTABLE_wbody1_ft', 'DEALER_COST BY COUNTRY', 'Step 09.6 : Verify chart title')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation'], 'Step 09.7 : Verify chart tool menus', custom_css='[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['Sum'], 'Step 09.8 : Verify Aggregation menu text', text=True, custom_css="[id^='SUM'] td[class^='tabPagingTex']")
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_02.xlsx', 'Step 09.9 : Verify report data')
        active.verify_page_summary('0', '5of5records,Page1of1', 'Step 09.10 : Verify report page summary')
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f ', 'riser!s0!g0!mbar!', ['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Filter Chart', 'Exclude from Chart'], 'Step 09.11 : Verify tooltip')
        utillobj.switch_to_default_content(2)
        sceenshot=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(sceenshot, Test_Case_ID+'_Actual_Step_09')
        
if __name__ == '__main__':
    unittest.main()