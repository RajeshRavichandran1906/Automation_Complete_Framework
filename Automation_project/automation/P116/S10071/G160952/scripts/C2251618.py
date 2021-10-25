'''
Created on Jan 17, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251618
Test_Case Name : Verify Image prompt shows selected image as expected in a simple document with report and chart.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, active_miscelaneous
from common.lib import utillity

class C2251618_TestClass(BaseTestCase):

    def test_C2251618(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251618'
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
        
        def verify_chat_report_img_align():
            img=self.driver.find_element_by_css_selector("#orgdivouter0 #allLayoutObjects #EMBEDIMG0 img[src^='data']")
            report=self.driver.find_element_by_css_selector("#MAINTABLE_0")
            chart=self.driver.find_element_by_css_selector("#MAINTABLE_1")
            img_bottom_position=utillobj.get_object_screen_coordinate(img, 'bottom_middle')
            report_top_position=utillobj.get_object_screen_coordinate(report, 'top_middle')
            report_right_position=utillobj.get_object_screen_coordinate(report, 'right')
            chart_left_position=utillobj.get_object_screen_coordinate(chart, 'left')
            status=True if (img_bottom_position['y']+80)<report_top_position['y'] and (report_right_position['x']+5)<chart_left_position['x'] else False
            utillobj.asequal(False, status, 'Step 09.13 : Verify Report, Image and Chart are not overlapped' )
            
        """
            Step 01 : Launch IA to develop a Document Select 'GGSales' as master file, and change output format as Active report.
            From Insert menu click Image prompt to add an image
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_1', 'mrid', 'mrpass')
        visul_result.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=60, string_value='Document')
        
        visul_ribbon.select_ribbon_item('Insert', 'image')
        visul_result.wait_for_property("#IbfsOpenFileDialog7_btnOK div", 1, 45, string_value='Open')
        
        """
            Step 02 : Select "SMLOGO1" from the image list
        """
        utillobj.ibfs_save_as('smplogo1')
        visul_result.wait_for_property("#PageItemImage_1 img[src*='config']", 1, 25)
        
        """
            Step 03 : Click Ok and verify expected image appears on the document canvas.
        """
        img_displayed=self.driver.find_element_by_css_selector("#canvasFrame #PageItemImage_1 [id^='BiDockPanel'] img[src*='config']").is_displayed()
        utillobj.asequal(True, img_displayed, 'Step 03 : Verify expected image appears on the document canvas')
        
        """
            Step 04 : Go to Home menu and make sure default format selection is Report.
        """
        visul_ribbon.switch_ia_tab('Home')
        utillobj.verify_element_color_using_css_property("[id='HomeOutputReport'][class*='tool-bar-button-checked']", 'Pale_Cornflower_Blue', 'Step 04.1 : Verify default format selection is Report', attribute='background-color')
        
        """
            Step 05 : From Data pane, double click on the Category, Product, Unit Sales to generate a report. Place report under image.
        """
        metadata.datatree_field_click('Category',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 1, 25, string_value='Category')
         
        metadata.datatree_field_click('Product',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(5)>td", 1, 25, string_value='Product')
         
        metadata.datatree_field_click('Unit Sales',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(3)>td", 1, 25, string_value='Unit Sales')
        
        """
            Step 06 : Click on Insert tab and click on chart icon to create a chart in document
        """
        visul_ribbon.select_ribbon_item('Insert', 'chart')
        visul_result.wait_for_property("#pfjTableChart_2 text[class='legend-labels!s0!']", 1, 35, string_value='Series0')
        
        """
            Step 07 : Double click on "Region" and "Budget Units"
        """
        metadata.datatree_field_click('Region',2,1)
        visul_result.wait_for_property("#pfjTableChart_2 text[class='xaxisOrdinal-title']", 1, 25, string_value='Region')
         
        metadata.datatree_field_click('Budget Units',2,1)
        visul_result.wait_for_property("#pfjTableChart_2 text[class='yaxis-title']", 1, 25, string_value='Budget Units')
        
        """
            Step 08 : Adjust the report and chart accordingly not overlapped by each other in the canvas
        """
        chart_table=self.driver.find_element_by_id('TableChart_2')
        utillobj.click_on_screen(chart_table, 'middle', 0)
        visul_ribbon.repositioning_document_component('4', '2')
        
        report_table=chart_table=self.driver.find_element_by_id('TableChart_1')
        utillobj.click_on_screen(report_table, 'middle', 0)
        visul_ribbon.repositioning_document_component('1.04', '2')
        
        """
            Step 08.1 : Verify preview
        """
        verify_bar_chart('pfjTableChart_2', ['0', '40K', '80K', '120K', '160K'], '08')
        #iaresult.create_across_report_data_set('TableChart_1 ', 2, 3, 1, 2, Test_Case_ID+'_DataSet_Step_08.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1 ', 2, 3, 1, 2, Test_Case_ID+'_DataSet_Step_08.xlsx', 'Step 08.6 : Verify report data')
        sceenshot=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(sceenshot, Test_Case_ID+'_Actual_Step_08')
        
        """
            Step 09 : Run the Document.
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame()
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 25, string_value='Region')
        
        """
            Step 09.1 : Verify that Image, Report and chart displays correctly under Active document.
        """
        verify_bar_chart('MAINTABLE_wbody1_f', ['0', '200K', '400K', '600K', '800K', '1,000K'], '09')
        active.verify_chart_title('MAINTABLE_wbody1_ft', 'Budget Units by Region', 'Step 09.6 : Verify chart title')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation'], 'Step 09.7 : Verify chart tool menus', custom_css='[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu1 ', ['Sum'], 'Step 09.8 : Verify Aggregation menu text', text=True, custom_css="[id^='SUM'] td[class^='tabPagingTex']")
        #iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_Step_09.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_Step_09.xlsx', 'Step 09.9 : Verify report data')
        active.verify_page_summary('0', '10of10records,Page1of1', 'Step 09.10 : Verify data report')
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f ', 'riser!s0!g0!mbar!', ['Region:Midwest', 'Budget Units:907107', 'Filter Chart', 'Exclude from Chart'], 'Step 09.11 : Verify tooltip')
        img_displayed=self.driver.find_element_by_css_selector("#orgdivouter0 #allLayoutObjects #EMBEDIMG0 img[src^='data']").is_displayed()
        utillobj.asequal(True, img_displayed, 'Step 09.12 : Verify expected image appears on the document canvas')
        verify_chat_report_img_align()
        
        utillobj.switch_to_default_content()
        sceenshot=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(sceenshot, Test_Case_ID+'_Actual_Step_09')
        
if __name__ == '__main__':
    unittest.main()