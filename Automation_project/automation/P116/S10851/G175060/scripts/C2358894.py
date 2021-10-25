'''
Created on Jan 29, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358894
TestCase Name = Active Document with 2 pages, using two inserted Reports on Page 2.
'''

import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, active_miscelaneous, ia_run
from common.lib.basetestcase import BaseTestCase

class C2358894_TestClass(BaseTestCase):

    def test_C2358894(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2358894'
        report_fex = 'C46268a'
        chart_fex = 'C46268b'
        save_fex = 'AR-AD-078-AHTML'
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj = ia_run.IA_Run(self.driver)

        """
        Step 01: Create Report using GGORDER. master file 
        """
        utillobj.infoassist_api_login('report', 'ibisamp/ggorder', 'S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#singleReportCaptionLabel span:nth-child(2)", "Live Preview", 60)
       
        """
        Add fields Product Code, Product, Vendor ID and Unit Sales fields.
        """
        
        vis_metadata.datatree_field_click('Product,Code', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 25)
            
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 24, 25)
        
        vis_metadata.datatree_field_click('Vendor ID', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 36, 25)
        
        vis_metadata.datatree_field_click("Measures/Properties->Unit,Price", 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 48, 25)
        
        
        coln_list = ["ProductCode", "Product", "Vendor ID", "UnitPrice"]
        vis_resultobj.verify_report_titles_on_preview(4, 8, "TableChart_1 ", coln_list, "Step 1.1: Verify report1 titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 10, 4, 'C2358894_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, 'C2358894_Ds01.xlsx', 'Step 1.2: Verify Preview report dataset')
        
        """
        Step 02: Save the report as C46268a.fex
        """
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(report_fex)
        time.sleep(3)
        utillobj.wf_logout()
        signin_css="#SignonbtnLogin"
        utillobj.synchronize_with_number_of_element(signin_css, 1, 40)
        
        """
        Step 03: Create Chart using GGORDER. master file 
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggorder', 'S10851_1', 'mrid', 'mrpass')
        element_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 25, 60)
        
        """
        Add fields Product Code, Product, Vendor Name and Order Units fields.
        """
        vis_metadata.datatree_field_click('Product,Code', 2, 0)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 25)
        
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#TableChart_1 svg g [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Product Code : Product', 25)
        
        vis_metadata.datatree_field_click('Vendor Name', 2, 0)
        utillobj.synchronize_with_visble_text(element_css, 'Product Code : Product : Vendor Name', 25)
         
        vis_metadata.datatree_field_click('Ordered,Units', 2, 0)
        parent_css="#TableChart_1 svg g [class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Ordered Units', 25)
        
        xaxis_value="Product Code : Product : Vendor Name"
        vis_resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 3: Verify X-Axis Title")
        yaxis_value="Ordered Units"
        vis_resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 3.1: Verify y-Axis Title")
        expected_xval_list=['B141 : Hazelnut : Coffee Connection', 'B142 : French Roast : European Special', 'B144 : Kona : Evelina Imports, Ltd', 'F101 : Scone : Ridgewood Bakeries', 'F102 : Biscotti : Delancey Bakeries', 'F103 : Croissant : West Side Bakers', 'G100 : Mug : NY Ceramic Supply', 'G104 : Thermos : ThermoTech, Inc', 'G110 : Coffee Grinder : Appliance Craft', 'G121 : Coffee Pot : Appliance Craft']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 3.2:Verify XY labels", x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 3.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 3.4: Verify first bar color")
        time.sleep(5)
        
        """
        Step 04: Save the chart as C46268b.fex
        """
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(chart_fex)
        time.sleep(3)
        utillobj.wf_logout()
        time.sleep(2)
        
        """
        Step 05: Create new document using GGORDER master file and add following fields
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggorder', 'S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 65)
        
        """
        Product Code, Product, Vendor Name and Size fields.
        """
        vis_metadata.datatree_field_click('Product,Code', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 25)
        
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 24, 25)
         
        vis_metadata.datatree_field_click('Vendor Name', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 36, 25)
        
        vis_metadata.datatree_field_click('Size', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 48, 25)
        
        """ 
        Expect to see the following Reporting canvas.
        """  
        coln_list = ["ProductCode", "Product", "Vendor Name", "Size"]
        vis_resultobj.verify_report_titles_on_preview(4, 8, "TableChart_1 ", coln_list, "Step 5.1: Verify report1 titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 10, 4, 'C2358894_Ds02.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, 'C2358894_Ds02.xlsx', 'Step 5.2: Verify Preview report dataset')
        
        """ 
        Step 06: Create Page 2 by clicking on the Insert button, then the Page icon in the upper right.
        """
        vis_ribbon.select_ribbon_item("Insert", "Page")
        parent_css="#iaPagesMenuBtn div[class='bi-button-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Page 2', 45)
        
        exp_page_text = 'Page 2'
        elem_css = driver.find_element_by_css_selector("#iaPagesMenuBtn div[class='bi-button-label']")
        act_page_text = elem_css.text.strip()
        utillobj.asequal(act_page_text, exp_page_text,  "Step 06: Verify Page 2 appears on the canvas")
        
        """ 
        Click Insert, then select Existing Report and select C46268a.fex. 
        """
        vis_ribbon.select_ribbon_item('Insert', 'existing_report')
        utillobj.synchronize_with_visble_text("#IbfsOpenFileDialog7_btnOK div", 'Open', 35)
        utillobj.ibfs_save_as(report_fex)
        utillobj.synchronize_with_number_of_element("#IncludeTable_1", 1, 20)
        
        """ 
        Expect to see the following canvas for Page 2 of the Dashboard, with an inserted Report.
        """
        coln_list = ['ProductCode', 'Product', 'Vendor ID', 'UnitPrice']
        vis_resultobj.verify_report_titles_on_preview(4, 8, "IncludeTable_1 ", coln_list, "Step 06.1: Verify report1 titles")
#         ia_resultobj.create_report_data_set('IncludeTable_1', 10, 4, 'C2358894_Ds03.xlsx')
        ia_resultobj.verify_report_data_set('IncludeTable_1', 10, 4, 'C2358894_Ds03.xlsx', 'Step 06.2: Verify Preview report dataset')
        
        """ 
        Step 07: Click Insert, then select Existing Report and select C46268b.fex. Position the Report and Bar Chart so they do not overlay each other.
        """
        vis_ribbon.select_ribbon_item('Insert', 'existing_report')
        utillobj.synchronize_with_visble_text("#IbfsOpenFileDialog7_btnOK div", "Open", 45)
        utillobj.ibfs_save_as(chart_fex)
        parent_css="#IncludeChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 25)
        ia_resultobj.drag_drop_document_component('#IncludeChart_1', '#IncludeTable_1', 270, 0)
        
        """ 
        Expect to see the following canvas for Page 2 of the Dashboard, with an inserted Bar Chart.
        """
        xaxis_value="Product Code : Product : Vendor Name"
        vis_resultobj.verify_xaxis_title("IncludeChart_1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        yaxis_value="Ordered Units"
        vis_resultobj.verify_yaxis_title("IncludeChart_1", yaxis_value, "Step 07:a(ii) Verify y-Axis Title")
        expected_xval_list=['B141 : Hazelnut : Coffee Connection', 'B142 : French Roast : European Special', 'B144 : Kona : Evelina Imports, Ltd', 'F101 : Scone : Ridgewood Bakeries', 'F102 : Biscotti : Delancey Bakeries', 'F103 : Croissant : West Side Bakers', 'G100 : Mug : NY Ceramic Supply', 'G104 : Thermos : ThermoTech, Inc', 'G110 : Coffee Grinder : Appliance Craft', 'G121 : Coffee Pot : Appliance Craft']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K']
        vis_resultobj.verify_riser_chart_XY_labels("IncludeChart_1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels", x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("IncludeChart_1", 1, 10, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("IncludeChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        
        """ 
        Step 08: Click run to generate the two page Dashboard.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        
        utillobj.switch_to_frame(pause=3)
        tab_css="#IBILAYOUTDIV0 div[id='iLay$1'][class*='arDashboardBarButton']"
        utillobj.synchronize_with_number_of_element(tab_css, 1, 35)
        ia_runobj.verify_active_document_page_layout_menu("table[id='iLayTB$']",['Layouts','Page 1','Page 2'], "Step008: To generate the two page Dashboard")
        
        """
        Expect to see the following Dashboard.,
        Page 1:
        """
        page1_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0 div[id='iLay$1'][class*='arDashboardBarButton']")
        utillobj.click_on_screen(page1_css, 'middle')
        utillobj.click_on_screen(page1_css, 'middle', click_type=0)
        time.sleep(5)
        miscelaneousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 08.1: Verify page summary")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds05.xlsx', " Step 08.2: Verify report at run time.")
        time.sleep(5)
        
        """
        Expect to see the following Dashboard.,
        Page 2:
        """
        page2_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0 div[id='iLay$2'][class*='arDashboardBarButton']")
        utillobj.click_on_screen(page2_css, 'middle')
        utillobj.click_on_screen(page2_css, 'middle', click_type=0)
        time.sleep(5)
        
        miscelaneousobj.verify_page_summary(1, '10of10records,Page1of1', "Step 8.3: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData1', 'I1r', test_case_id + '_Ds06.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', test_case_id + '_Ds06.xlsx', " Step 8.4: Verify report at run time.")
        
        parent_css="#MAINTABLE_wbody2 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 25)
        xaxis_value="Product Code : Product : Vendor Name"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 8.5: Verify X-Axis Title")
        yaxis_value="Ordered Units"
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 8.6: Verify y-Axis Title")
        expected_xval_list=['B141 : Hazelnut : Coffee Connection', 'B142 : French Roast : European Special', 'B144 : Kona : Evelina Imports, Ltd', 'F101 : Scone : Ridgewood Bakeries', 'F102 : Biscotti : Delancey Bakeries', 'F103 : Croissant : West Side Bakers', 'G100 : Mug : NY Ceramic Supply', 'G104 : Thermos : ThermoTech, Inc', 'G110 : Coffee Grinder : Appliance Craft', 'G121 : Coffee Pot : Appliance Craft']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2", expected_xval_list, expected_yval_list, "Step 8.7:Verify XY labels", x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 10, 'Step 8.8: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step 8.9: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody2","Ordered Units by Product Code, Product, Vendor Name", "Step 8.10 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['More Options','Advanced Chart','Original Chart'],"Step 8.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Aggregation'],"Step 8.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Sum'],"Step 8.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """ 
        Step 09: Save the Dashboard as AR-AD-078-AHTML by clicking the Save As button in the upper left.
        """
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(save_fex)
        time.sleep(3)
        utillobj.wf_logout()
        time.sleep(5)
        
        """ 
        Step 10: Re-execute the saved Fexes to make sure both pages display and the Reports and Bar Chart appear correctly.
        """
        utillobj.active_run_fex_api_login(save_fex+'.fex', 'S10851_1', 'mrid', 'mrpass')
        parent_css="table[id='iLayTB$']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        ia_runobj.verify_active_document_page_layout_menu("table[id='iLayTB$']",['Layouts','Page 1','Page 2'], "Step10: Verify both pages display")
        
        page1_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0 div[id='iLay$1'][class*='arDashboardBarButton']")
        utillobj.click_on_screen(page1_css, 'middle')
        utillobj.click_on_screen(page1_css, 'middle', click_type=0)
        time.sleep(5)
        miscelaneousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 10.1: Verify page summary")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds07.xlsx', " Step 10.2: Verify report at run time.")
        time.sleep(5)
        
        page2_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0 div[id='iLay$2'][class*='arDashboardBarButton']")
        utillobj.click_on_screen(page2_css, 'middle')
        utillobj.click_on_screen(page2_css, 'middle', click_type=0)
        time.sleep(5)
        miscelaneousobj.verify_page_summary(1, '10of10records,Page1of1', "Step 10.3: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData1', 'I1r', test_case_id + '_Ds08.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', test_case_id + '_Ds08.xlsx', " Step 10.4: Verify report at run time.")
        parent_css="#MAINTABLE_wbody2 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 25)
        xaxis_value="Product Code : Product : Vendor Name"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step 10.5 Verify X-Axis Title")
        yaxis_value="Ordered Units"
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody2", yaxis_value, "Step 10.6 Verify y-Axis Title")
        expected_xval_list=['B141 : Hazelnut : Coffee Connection', 'B142 : French Roast : European Special', 'B144 : Kona : Evelina Imports, Ltd', 'F101 : Scone : Ridgewood Bakeries', 'F102 : Biscotti : Delancey Bakeries', 'F103 : Croissant : West Side Bakers', 'G100 : Mug : NY Ceramic Supply', 'G104 : Thermos : ThermoTech, Inc', 'G110 : Coffee Grinder : Appliance Craft', 'G121 : Coffee Pot : Appliance Craft']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2", expected_xval_list, expected_yval_list, "Step 10.7:Verify XY labels", x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 10, 'Step 10.8: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step 10.9: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody2","Ordered Units by Product Code, Product, Vendor Name", "Step 10.10 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['More Options','Advanced Chart','Original Chart'],"Step 10.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Aggregation'],"Step 10.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Sum'],"Step 10.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
if __name__ == '__main__':
    unittest.main()