'''
Created on Jan 22, 2018
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10851&group_by=cases:section_id&group_order=asc&group_id=175052
TestCase ID: http://172.19.2.180/testrail/index.php?/cases/view/2358881
TestCase Name : AHTML:COMP-Rpt:Minimize conditional window popups goes hidden - 146948

@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity

class C2358881_TestClass(BaseTestCase):

    def test_C2358881(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2358881'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        """
            Step 01:Create an Document using Car master file.
            Add COUNTRY, CAR as By and DEALER_COST and RETAIL_COST as SUM
        """
        utillobj.infoassist_api_login('document','ibisamp/car','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 60)
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6, 25)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 17, 25)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 28, 25)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 39, 25)
        """
            Verify querypane to verify whether the following fileds are added in the corresponsing bucket
        """
        metaobj.verify_query_pane_field('Sum', 'DEALER_COST', 1, "Step 01:01")
        metaobj.verify_query_pane_field('Sum', 'RETAIL_COST', 2, "Step 01:02")
        metaobj.verify_query_pane_field('By', 'COUNTRY', 1, "Step 01:03")
        metaobj.verify_query_pane_field('By', 'CAR', 2, "Step 01:04")
        
        """
            Verify report data at live-preview
        """
        coln_list = ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1 ", coln_list, "Step 01:05: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 01:06: Verify Preview report dataset')
        """
            Step 02:Verify output format as AHTML.
        """
        format_type=driver.find_element_by_css_selector("#HomeFormatType").text
        expected_format_type='Active Report'
        utillobj.asequal(expected_format_type, format_type, "Step 02:Verify output format shows Active Report bydefault")
        """
            Step 03:Run the report.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=1)
        
        """
            Verify report at runtime 
        """
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 03:01: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 03:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 03:03: Verify data')
        
        """
            Step 04:Apply filter or rollup or chart or any other condition to the
            report and minimize the popup window.
            Eg:Car->Chart->Pie->Group By(x) ->Country
            Verify applied condition to the report is displayed properly.
        """
        miscobj.select_menu_items("ITableData0", "1", "Chart","Pie","COUNTRY")
        utillobj.synchronize_with_visble_text("#wall1 table>tbody>tr>td.arWindowBarTitle", "CAR BY COUNTRY", 15)
        miscobj.move_active_popup("1", "700", "500")
        miscobj.verify_chart_title("wall1","CAR BY COUNTRY", "Step 04:1 : Verify chart title ")
        
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 04:02: Verify Color')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 04:03: Verify Color')
        miscobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 04:04: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 04:05: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('wall1', ['Count'],"Step 04:06: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_riser_pie_labels_and_legends('wall1', ['CAR'], "Step 04:07:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('wall1', 5, "Step 04:08: Verify number of pie")
        expected_label_list=['ENGLAND', 'FRANCE', 'ITALY','JAPAN','W GERMANY']
        resultobj.verify_riser_legends('wall1', expected_label_list, 'Step 04:09: Verify Legends')

        """
            Step 05:Now minimize the the window.
            Verify whether window as minimized without any error.
        """
        driver.find_element_by_css_selector("#WCS1 div[onclick*='minwin']").click()
        time.sleep(5)
        wall1_css=driver.find_element_by_css_selector("#wall0")
        chart_window_left=wall1_css.location['x']
        chart_window_top=wall1_css.location['y']
        if chart_window_top >= 600:
            utillobj.asequal(True, True, 'Step 05:01 : Verify top of the chart window is gretaer than 600 and minimized')
        else:
            utillobj.asequal(False, True, 'Step 05:01 : Verify top of the chart window is not gretaer than 600 and not minimized')
        
        if chart_window_left == 0:
            utillobj.asequal(True, True, 'Step 05:02 : Verify left of the chart window is equal to 0 and minimized')
        else:
            utillobj.asequal(False, True, 'Step 05:02 : Verify left of the chart window is not equal to 0 and minimized')
              
        
if __name__ == "__main__":
    unittest.main()