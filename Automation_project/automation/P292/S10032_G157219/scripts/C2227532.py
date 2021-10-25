'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227532
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_resultarea, active_miscelaneous
from common.lib import utillity

class C2227532_TestClass(BaseTestCase):

    def test_C2227532(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2227532'
        driver = self.driver
        driver.implicitly_wait(2)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        page1_report_id='TableChart_1'
        page1_chart_id='TableChart_2'
        page2_chart_id='TableChart_3'
        
            
        """    1. Launch IA Document mode: http://machine:port/ibi_apps/ia?tool=Document&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032    """
        utillobj.infoassist_api_login('document','ibisamp/car','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=10, string_value='Document')  
        time.sleep(1)
        
        """    2. Double click "CAR", "DEALER_COST", "SALES".    """
        metaobj.datatree_field_click("CAR", 2, 1)
        resultobj.wait_for_property("#" + page1_report_id + " div[class^='x']", 11, expire_time=8) 
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        resultobj.wait_for_property("#" + page1_report_id + " div[class^='x']", 22, expire_time=10) 
        metaobj.datatree_field_click("SALES", 2, 1)
        resultobj.wait_for_property("#" + page1_report_id + " div[class^='x']", 33, expire_time=10)
        
        """    3. Select "Insert" > "Chart".    """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        
        """    4. Double click "CAR", "DEALER_COST".    """
        metaobj.datatree_field_click("CAR", 2, 1)
        resultobj.wait_for_property("#" + page1_chart_id + " text[class^='xaxis'][class$='title']", 1, expire_time=10, string_value='CAR')    
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        resultobj.wait_for_property("#" + page1_chart_id + " text[class='yaxis-title']", 1, expire_time=10, string_value='DEALER_COST')
        
        """    5. Re-position the chart so that it will not be on top of the report.    """
        ribbonobj.repositioning_document_component('4.5', '1.25')
        time.sleep(4)
        
        """    6. Verify the following is displayed on the canvas.    """
        # verify Report
        list1 = ["CAR", "DEALER_COST", "SALES"]
        resultobj.verify_report_titles_on_preview(3, 3, page1_report_id, list1, "Step 06a: Verify column titles on preview")
        # verify Chart
        resultobj.verify_number_of_riser(page1_chart_id, 1, 10, 'Step 6b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 06c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color(page1_chart_id, "riser!s0!g2!mbar!", "bar_blue1", "Step 06d: Verify bar color")
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title(page1_chart_id, xaxis_value, "Step 06e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title(page1_chart_id, yaxis_value, "Step 06e(ii): Verify Y-Axis Title")
        
        """    7. Click "Page" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Page")
        
        """    8. Verify "Page 2" is displayed on a blank Document canvas.    """
        oPage2=driver.find_element_by_xpath("//div[@id='iaPagesMenuBtn']//div[contains(text(), 'Page 2')]")
        utillobj.verify_object_visible('css', True, "Step 08a: Verify Page changed to 'Page 2'", elem_obj=oPage2)
        oLengthClass=driver.find_elements_by_css_selector("#iaCanvasPanel #theCanvas>div")
        utillobj.asequal(len(oLengthClass), 1, "Step 08b: Verify blank page displayed")
        
        """    9. Click "Chart" icon.    """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        
        """    10. Double click "COUNTRY", "SALES".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        resultobj.wait_for_property("#" + page2_chart_id + " text[class^='xaxis'][class$='title']", 1, expire_time=10, string_value='COUNTRY')    
        metaobj.datatree_field_click("SALES", 2, 1)
        resultobj.wait_for_property("#" + page2_chart_id + " text[class='yaxis-title']", 1, expire_time=10, string_value='SALES')
        time.sleep(4)
        
        """    11. Verify the following chart is displayed.    """
        resultobj.verify_number_of_riser(page2_chart_id, 1, 5, 'Step 11a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels(page2_chart_id, expected_xval_list, expected_yval_list, 'Step 11b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color(page2_chart_id, "riser!s0!g2!mbar!", "bar_blue1", "Step 11c: Verify bar color")
        xaxis_value="COUNTRY"
        yaxis_value="SALES"
        resultobj.verify_xaxis_title(page2_chart_id, xaxis_value, "Step 11d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title(page2_chart_id, yaxis_value, "Step 11d(ii): Verify Y-Axis Title")
        
        """    12. From "Page Menu", select "Page 1".    """
        iaresult.select_or_verify_document_page_menu('Page 1')
        
        """    13. Verify report and chart are displayed.    """
        # verify Report
        list1 = ["CAR", "DEALER_COST", "SALES"]
        resultobj.verify_report_titles_on_preview(3, 3, page1_report_id, list1, "Step 13a: Verify column titles on preview")
        # verify Chart
        resultobj.verify_number_of_riser(page1_chart_id, 1, 10, 'Step 13b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 13c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color(page1_chart_id, "riser!s0!g2!mbar!", "bar_blue1", "Step 13d: Verify bar color")
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title(page1_chart_id, xaxis_value, "Step 13e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title(page1_chart_id, yaxis_value, "Step 13e(ii): Verify Y-Axis Title")
        
        """    14. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        
        """    15. Verify output window displays as followed.    """
        # verify Report
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 15a: Verify the Run Report Heading")
        column_list=['CAR', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, "Step 15b: Verify the Run Report column heading")
        #utillobj.create_data_set('ITableData0','I0r', Test_Case_ID +'_Ds_01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds_01.xlsx', "Step 15c: Verify entire Data set in Run Report on Page 1") 
        time.sleep(2)
        # verifyC Chart
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", "DEALER_COST", "Step 15d: Verify -yAxis Title")
        time.sleep(1)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", "CAR", "Step 15e: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15f: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 15g: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "bar_blue", "Step 15h: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody1_ft', 'DEALER_COST BY CAR', 'Step 15i: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 15j: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 15k: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 15l: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 15m: Verify bar value")
        time.sleep(2)
        
        """    16. Click "Page 2" on output window.    """
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        driver.find_element_by_css_selector(select_css).click()
        time.sleep(5)
        
        """    17. Verify output window displays as followed.    """
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", "SALES", "Step 17a: Verify -yAxis Title")
        time.sleep(1)
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", "COUNTRY", "Step 17b: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2", expected_xval_list, expected_yval_list, "Step 17c: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 5, 'Step 17d: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g2!mbar!", "bar_blue", "Step 17e: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody2_ft', 'SALES BY COUNTRY', 'Step 17f: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['More Options','Advanced Chart','Original Chart'],"Step 17g: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Aggregation'],"Step 17h: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Sum'],"Step 17i: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['COUNTRY:ITALY', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 17j: Verify bar value")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        
        """    18. Click "IA" > "Save As".    """
        """    19. Enter Title = "C2227532".    """
        """    20. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    21. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    22. Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227532.fex&tool=Document    """
        """    23. Verify successful restore    """
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#" + page1_chart_id + " text[class^='xaxis'][class$='title']", 1, expire_time=50, string_value='COUNTRY')
        
        """    24. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        # verify Report
        list1 = ["CAR", "DEALER_COST", "SALES"]
        resultobj.verify_report_titles_on_preview(3, 3, page1_report_id, list1, "Step 24a: Verify column titles on preview")
        # verify Chart
        resultobj.verify_number_of_riser(page1_chart_id, 1, 10, 'Step 24b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 24c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color(page1_chart_id, "riser!s0!g2!mbar!", "bar_blue1", "Step 24d: Verify bar color")
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title(page1_chart_id, xaxis_value, "Step 24e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title(page1_chart_id, yaxis_value, "Step 24e(ii): Verify Y-Axis Title")
        
if __name__ == '__main__':
    unittest.main()