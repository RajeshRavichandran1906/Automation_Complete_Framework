'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226970
TestCase Name = Test that AutoDrill works with Traffic Light conditions(Conditional Styling)
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous, visualization_metadata, ia_styling, ia_ribbon
from common.lib import utillity  
import time, pyautogui
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226970_TestClass(BaseTestCase):
    
    def test_C2226970(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226970"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(40)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Right click on Product,Category in the query pane and select More > Traffic Light Conditions.    """
        metaobj.querytree_field_click("Product,Category", 1, 1, 'More', 'Traffic Light Conditions...')
        time.sleep(10)
        
        """    3. Select the empty drop down next to Equal to. Click on Get Values > All. Select Camcorder and click OK. Click on the Drill Down button    """
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='All', value='Camcorder')
        dd_btn=driver.find_element_by_css_selector("#cstyDrillDownBtn img")
        utillobj.default_left_click(object_locator=dd_btn)
        time.sleep(5)
        
        """    4. Click on the Web Page radio button. Under URL, type "http://www.informationbuilders.com"
                Change the Description to say "Go to Information Builders Home Page" Press the Tab key.
                Click OK twice to close.    """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.informationbuilders.com', set_description='Go to Information Builders Home Page')
        ok_btn_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(12)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(8)
        
        """    5. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    6. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 06a: Verify dataset", desired_no_of_rows=15)
        
        """    7. Click on Accessories under Product Category for EMEA region    """
        expected_tooltip_list = ['Drill down to Product Subcategory']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",3,2, expected_tooltip_list, "Step 07: Verify drilldown menu for Accessories")
        time.sleep(5)
        
        """    8. Click on Camcorder under Product Category for EMEA region    """
        expected_tooltip_list = ['Drill down to Product Subcategory', 'Go to Information Builders Home Page']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,2, expected_tooltip_list, "Step 08: Verify drilldown menu for Camcorder")
        time.sleep(5)
        
        """    9. Select Go to Information Builders Home Page and Verify the IBI home page opens. Close the page.    """
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",4,2,'Go to Information Builders Home Page', "Step 08")
        iarun.select_report_autolink_tooltip("table[summary='Summary']",4,2,'Go to Information Builders Home Page')
        time.sleep(6)
        utillobj.switch_to_default_content(1)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(2)
        owebpage=driver.current_url
        utillobj.asin('www.informationbuilders.com', owebpage, "Step 09a: Verify Information Builder page is displayed")
        time.sleep(2)
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        
        """    10. Click on Computers under Product Category for EMEA region    """
        expected_tooltip_list = ['Drill down to Product Subcategory']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",5,2, expected_tooltip_list, "Step 10: Verify drilldown menu for Computers")
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        
        """    11. Click IA > Save As> Type C2226970a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    12. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226970a.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(35)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14)
         
        """    13. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 13a: Verify Autodrill button should be active")
        time.sleep(4)
         
        """    14. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    15. Click RUN    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(1)
        time.sleep(4)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 15a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 15c: Verify the report data', desired_no_of_rows=15)
        
        """    16.    Click on Accessories under Product Category for EMEA region    """
        values=['Drill down to Product Subcategory', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 1, values, "Step 16a: Verify the drilldown menu for Accessories")
        time.sleep(5)
        pyautogui.click(x_fr + 5, y_fr + 95, button='left')
        time.sleep(5)
        
        """    17.    Click on Camcorder  under Product Category for EMEA region    """
        values=['Drill down to Product Subcategory', 'Go to Information Builders Home Page', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 1, 1, values, "Step 17a: Verify the drilldown menu for Camcorder")
        time.sleep(5)
        
        """    18. Select Go to Information Builders Home Page and Verify the IBI home page opens. Close the page   """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 1, 1, 'Go to Information Builders Home Page')
        time.sleep(6)
        utillobj.switch_to_default_content(1)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(2)
        owebpage=driver.current_url
        utillobj.asin('www.informationbuilders.com', owebpage, "Step 18a: Verify Information Builder page is displayed")
        time.sleep(2)
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        
        """    19.    Click on Camcorder  under Product Category for EMEA region    """
        values=['Drill down to Product Subcategory', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 2, 1, values, "Step 19a: Verify the drilldown menu for Computers")
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(8)
        
        """    20. Click IA > Save As> Type C2226970b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    21. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    22. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 22a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
        
        """    23. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
