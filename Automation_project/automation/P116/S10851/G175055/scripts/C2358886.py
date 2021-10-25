'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358886
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity
import keyboard

class C2358886_TestClass(BaseTestCase):

    def test_C2358886(self):
        
        """ TESTCASE VARIABLES """
        
        Test_Case_ID = 'C2358886'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Launch IA to develop a new Document.
        Select 'GGSales' as master file, and change output format as Active report
        Select Category,Product ID,Region and Unit Sales to get a report    """
        
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 65)
        
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=20)
            
        metaobj.datatree_field_click("Product ID", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=20)
        
        metaobj.datatree_field_click("Region", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 13, expire_time=20)
        
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 21, expire_time=20) 
        
        coln_list = ['Category', 'Product ID', 'Region', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1 ", coln_list, "Step 01a: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1 ', 7, 4, 'C2358886_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1 ', 7, 4, 'C2358886_Ds01.xlsx', 'Step 01b: Verify Preview report dataset')
        
        """    2. Click Insert tab and select Chart    """
        """    3. On a canvas you will see query pane to build a chart    """
        
        ribbonobj.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_2", 25, 35)
        
        """    4. Select Category and Budget Units fields    """
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='xaxisOrdinal-title']", "Category", 20)
        
        metaobj.datatree_field_click("Budget Units", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='yaxis-title']", "Budget Units", 20)
        
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 260, 0)
        time.sleep(2)
        resultobj.verify_number_of_riser("TableChart_2", 1, 1, 'Step 04a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 04b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue1", "Step 04c: Verify bar color")
        xaxis_value="Category"
        yaxis_value="Budget Units"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 04d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 04d(ii): Verify Y-Axis Title")
        
        """    5. Click on Insert tab and select Text box. Right Click on Text box and assign Budget Units for field value.    """
        ribbonobj.select_ribbon_item("Insert", "Text")
        ia_resultobj.drag_drop_document_component('#Prompt_1','#TableChart_2', 0,80, target_drop_point='bottom_middle')
        time.sleep(2)
        resultobj.choose_right_click_menu_item_for_prompt("#Prompt_1", 'Properties', msg='Step 11(i):')
        source_dict={'select_report':'Chart1','select_field':'Budget Units'}
        resultobj.customize_active_dashboard_properties(source=source_dict)
        time.sleep(1)
        
        """    6. Now save and run the report, and give input as "1385923" in text box and give enter    """
        
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 50)
        
        utillobj.switch_to_frame()
        xaxis_title_css="#MAINTABLE_1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(xaxis_title_css, "Category", 45)
        
        miscobj.verify_page_summary(0, '39of39records,Page1of1', 'Step 06r.a: Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Region', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 06r.b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2358886_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2358886_Ds02.xlsx', 'Step 06r.c: Verify data.')
        miscobj.verify_arChartToolbar("MAINTABLE_1",['More Options','Advanced Chart','Original Chart'],"Step 06g.a: Verify Chart toolbar")
        x_val_list=['Coffee', 'Food', 'Gifts']
        y_val_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_1', x_val_list, y_val_list, "Step 06g.b")
        expected_tooltip=['Category:  Coffee', 'Budget Units:  1385923', 'Filter Chart', 'Exclude from Chart']
        miscobj.verify_active_chart_tooltip('MAINTABLE_1', 'riser!s0!g0!mbar', expected_tooltip, "Step 06g.c: verify the chart tooltip with fill color")
        xaxis_value="Category"
        yaxis_value="Budget Units"
        resultobj.verify_xaxis_title("MAINTABLE_1", xaxis_value, "Step 06g.d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_1", yaxis_value, "Step 06g.d(ii): Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 06g.e: Verify bar color")
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Budget Units BY Category", "Step 06g.f : Verify chart title ")
        
        """    give input as "1385923" in text box and give enter    """
        
        element=self.driver.find_element_by_css_selector('#PROMPT_1_cs input')
        exec("element.clear()")
        exec("element.send_keys('1385923')")
        keyboard.send('enter')
        time.sleep(5)
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "Coffee", 25)
        miscobj.verify_page_summary(0, '39of39records,Page1of1', 'Step 07r.a: Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Region', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 07r.b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2358886_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2358886_Ds02.xlsx', 'Step 07r.c: Verify data.')
        miscobj.verify_arChartToolbar("MAINTABLE_1",['More Options','Advanced Chart','Original Chart'],"Step 07g.a: Verify Chart toolbar")
        x_val_list=['Coffee']
        y_val_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_1', x_val_list, y_val_list, "Step 07g.b")
        expected_tooltip=['Category:  Coffee', 'Budget Units:  1385923']
        miscobj.verify_active_chart_tooltip('MAINTABLE_1', 'riser!s0!g0!mbar', expected_tooltip, "Step 07g.c: verify the chart tooltip with fill color")
        xaxis_value="Category"
        yaxis_value="Budget Units"
        resultobj.verify_xaxis_title("MAINTABLE_1", xaxis_value, "Step 07g.d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_1", yaxis_value, "Step 07g.d(ii): Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 07g.e: Verify bar color")
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Budget Units BY Category", "Step 07g.f : Verify chart title ")
        utillobj.switch_to_default_content()
        
        """    Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
        
if __name__ == '__main__':
    unittest.main()