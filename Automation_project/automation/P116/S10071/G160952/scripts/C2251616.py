'''
Created on Jan 16, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251616
Test_Case Name : Verify Text Box prompt shows content as expected in a simple document with report and chart.
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, active_miscelaneous
from common.lib import utillity

class C2251616_TestClass(BaseTestCase):

    def test_C2251616(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251616'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        def verify_bar_chart(parent_id, yaxis_labels, step_num):
            visul_result.verify_xaxis_title(parent_id, 'Region', 'Step ' + step_num + '.1 : Verify X-Axis title')
            visul_result.verify_yaxis_title(parent_id, 'Budget Units', 'Step ' + step_num + '.2 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels(parent_id, ['Midwest', 'Northeast', 'Southeast', 'West'], yaxis_labels, 'Step ' + step_num + '.3 :')
            visul_result.verify_number_of_riser(parent_id, 1, 4, 'Step ' + step_num + '.4 : Verify number of bar chart risers')
            utillobj.verify_chart_color(parent_id, 'riser!s0!g0!mbar!', 'bar_blue', 'Step ' + step_num + '.5 : Verify bar chart riser color')
            
        """
            Step 01 : Launch IA to develop a Document. Select 'GGSales' as master file, and change output format as Active report.
            From Insert menu click Text Box prompt to create text new object in the canvas
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text('#iaCanvasContainer', 'Document', visul_result.home_page_long_timesleep)
        visul_result.wait_for_property("#canvasFrame svg", 1, 40)
        
        
        visul_ribbon.select_ribbon_item('Insert', 'text_box')
        visul_result.wait_for_property("#theCanvas #Text_1", 1, 8)
        
        """
            Step 01.1 : Verify that text box created on canvas with the following text content default ("Enter text here")
        """
        iaresult.verify_text_in_Textbox('#Text_1', 'Enter text here', 'Step 01.1 : Verify that text box created on canvas with the following text content default ("Enter text here")')
        
        """
            Step 02 : Double click on the text box to modify the text content. Enter text as "Test to verify the text content in textbox with document"
        """
        visul_ribbon.resizing_document_component('0.40', '5')
        iaresult.enter_text_in_Textbox('Text_1', 'Test to verify the text content in textbox with document')
        time.sleep(5)
        
        """
            Step 02.1 : Verify that text box contain the modified text content on the canvas
        """
        iaresult.verify_text_in_Textbox('#Text_1', 'Test to verify the text content in textbox with document', 'Step 02.1 : Verify that text box contain the modified text content on the canvas')
        
        """
            Step 03 : Go to Home menu and make sure default format selection is Report.
        """
        visul_ribbon.switch_ia_tab('Home')
        utillobj.verify_element_color_using_css_property("[id='HomeOutputReport'][class*='tool-bar-button-checked']", 'Pale_Cornflower_Blue', 'Step 03.1 : Verify default format selection is Report', attribute='background-color')
        
        """
            Step 04 : From Query pane, double click on the Category, Product, Unit Sales to generate a report.
        """
        metadata.datatree_field_click('Category',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 1, 15, string_value='Category')
         
        metadata.datatree_field_click('Product',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(5)>td", 1, 15, string_value='Product')
         
        metadata.datatree_field_click('Unit Sales',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(3)>td", 1, 15, string_value='Unit Sales') 
        
        """
            Step 05 : Click on Insert tab and click on chart icon to create a chart in document
        """
        visul_ribbon.select_ribbon_item('Insert', 'chart')
        visul_result.wait_for_property("#pfjTableChart_2 text[class='legend-labels!s0!']", 1, 15, string_value='Series0')
        
        """
            Step 06 : Double click on "Region" and "Budget Units"
        """
        metadata.datatree_field_click('Region',2,1)
        visul_result.wait_for_property("#pfjTableChart_2 text[class='xaxisOrdinal-title']", 1, 15, string_value='Region')
         
        metadata.datatree_field_click('Budget Units',2,1)
        visul_result.wait_for_property("#pfjTableChart_2 text[class='yaxis-title']", 1, 15, string_value='Budget Units')
        
        """
            Step 07 : Adjust the report and chart accordingly not overlapped by each other in the canvas
        """
        chart_table=self.driver.find_element_by_id('TableChart_2')
        utillobj.click_on_screen(chart_table, 'middle', 0)
        visul_ribbon.repositioning_document_component('4.5', '1.6')
        
        report_table=chart_table=self.driver.find_element_by_id('TableChart_1')
        utillobj.click_on_screen(report_table, 'middle', 0)
        visul_ribbon.repositioning_document_component('1.04', '1.6')
        
        textbox=self.driver.find_element_by_id('Text_1')
        utillobj.click_on_screen(textbox, 'middle', 0)
        visul_ribbon.repositioning_document_component('3', '1.04')
        
        """
            Step 07.1 : Verify preview
        """
        verify_bar_chart('pfjTableChart_2', ['0', '40K', '80K', '120K', '160K'], '07')
        #iaresult.create_across_report_data_set('TableChart_1 ', 2, 3, 1, 2, Test_Case_ID+'_DataSet_Step_07.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1 ', 2, 3, 1, 2, Test_Case_ID+'_DataSet_Step_07.xlsx', 'Step 07.6 : Verify report data')
#         sceenshot=self.driver.find_element_by_id('resultArea')
#         utillobj.take_screenshot(sceenshot, Test_Case_ID+'_Actual_Step_07')
        
        """
            Step 08 : Run the Document.
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 25, string_value='Region')
        
        """
            Step 08.1 : Verify that text box displayed in the document with report and chart with 
            the following text content on the report out put "Test to verify the text content in textbox with document"
        """
        verify_bar_chart('MAINTABLE_wbody1_f', ['0', '200K', '400K', '600K', '800K', '1,000K'], '08')
        active.verify_chart_title('MAINTABLE_wbody1_ft', 'Budget Units by Region', 'Step 08.6 : Verify chart title')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation'], 'Step 08.7 : Verify chart tool menus', custom_css='[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['Sum'], 'Step 08.8 : Verify Aggregation menu text', text=True, custom_css="[id^='SUM'] td[class^='tabPagingTex']")
        #iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_Step_08.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_Step_08.xlsx', 'Step 08.9 : Verify report data')
        active.verify_page_summary('0', '10of10records,Page1of1', 'Step 08.10 : Verify data report')
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f ', 'riser!s0!g0!mbar!', ['Region:Midwest', 'Budget Units:907107', 'Filter Chart', 'Exclude from Chart'], 'Step 08.11 : Verify tooltip')
        utillobj.verify_element_text("#allLayoutObjects td[id^='LOBJText']>span", 'Test to verify the text content in textbox with document', 'Step 08.12 : Verify textbox text')
        utillobj.switch_to_default_content()
#         sceenshot=self.driver.find_element_by_id('resultArea')
#         utillobj.take_screenshot(sceenshot, Test_Case_ID+'_Actual_Step_08')
        
if __name__ == '__main__':
    unittest.main()