'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197788
TestCase Name = Use a measure as a BY field generates hyperlinks when Auto Drill is enabled
'''
import unittest, time
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, visualization_metadata, active_miscelaneous
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2197788_TestClass(BaseTestCase):
    def test_C2197788(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2197788"
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        miscelanousobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Launch the IA report API with wf_retail_lite    """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P276/S9970', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)   
        time.sleep(15)
        
        """    2. Double click on "Shipment Unit(s)" from data pane. (Measures > Shipments > Shipment Unit(s))    """
        metaobj.datatree_field_click("Shipment Unit(s)", 2, 1)
        time.sleep(5)
        metaobj.verify_query_pane_field("Sum", "Shipment Unit(s)", 1, "Step 02a: Verify Shipment Unit(s) added in Sum")
        
        """    3. Drag and drop the field "Days,Delayed" from data pane to By bucket in query pane    """
        #metaobj.datatree_field_click("Days,Delayed", 1, 1,'Sort')
        metaobj.drag_drop_data_tree_items_to_query_tree('Days,Delayed',1,'By',0)
        time.sleep(5)
        metaobj.verify_query_pane_field("By", "Days,Delayed", 1, "Step 03a: Verify Days,Delayed added in Sort")
        
        """    4. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    5. Click Run.     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 5a: Verify report data set")
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 1, text='-2', font_color = 'gray8', msg='Step 5b ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 6, 1, text='1', font_color = 'gray8', msg='Step 5c ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 8, 1, text='3', font_color = 'gray8', msg='Step 5d ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 13, 1, text='8', font_color = 'gray8', msg='Step 5e ')
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    6. Click "Save" in the toolbar > Type C2197788a > Click "Save" in the Save As dialog    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        
        """    7. Close the IA+ window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    8. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2197788a.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(35)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14)
        
        """    9. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 9a: Verify Autodrill button should be active")
        time.sleep(4)
        
        """    10. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    11. Click RUN    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        miscelanousobj.verify_page_summary(0, '12of12records,Page1of1', 'Step 11a: Verify the Report Records')
        column_list=['Days Delayed', 'Shipment Unit(s)']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', 'Step 11c: Verify the report data')
        miscelanousobj.verify_cell_property("ITableData0", 1, 0, "-2", "Step 11d: ", text_color='gray8')
        miscelanousobj.verify_cell_property("ITableData0", 5, 0, "2", "Step 11e: ", text_color='gray8')
        miscelanousobj.verify_cell_property("ITableData0", 10, 0, "7", "Step 11f: ", text_color='gray8')
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    12. Click IA > Save As > Type C2197788b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    13. Close the IA+ window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    14. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2197788b.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(35)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14)
        
        """    16. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 16a: Verify Autodrill button should be active")
        time.sleep(4)
        
        """    16. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
