'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229710
TestCase Name = Test that AutoDrill works in a MultiDrill - AHTML
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_ribbon, active_miscelaneous
from common.lib import utillity  
import time, pyautogui
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229710_TestClass(BaseTestCase):
    def test_C2229710(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2229710"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    3. Click on Store,Business,Region on the canvas.    """
        metaobj.querytree_field_click("Store,Business,Region", 1)
        time.sleep(5)
        
        """    4. Click on Drill Down on the ribbon.    """
        ribbonobj.select_ribbon_item("Field", "Drilldown")
        time.sleep(4)
        
        """    5. Click on the Web Page radio button. Under URL, type "http://www.informationbuilders.com"
                Change the Description to say "Go to Information Builders Home Page" Press the Tab key.    """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.informationbuilders.com', set_description='Go to Information Builders Home Page')
        
        """    6. Click on the "Create a new drill down" icon.
                On the Report line click on Browse and choose "Drilldown-Region". In the Parameter section click on the Add Parameter icon.    """
        new_btn=driver.find_element_by_css_selector("#drillDownNew")
        utillobj.default_left_click(object_locator=new_btn)
        time.sleep(3)
        ia_ribbonobj.create_drilldown_report("report", browse_file_name="Drilldown-Region")
        amper=driver.find_element_by_css_selector("div[id^='QbDialog'] #btnNewParam")
        utillobj.default_left_click(object_locator=amper)
        time.sleep(5)
        
        """    7. In the Name drop down pick BUSINESS_REGION.
                In the Value drop down pick Store,Business,Region. Click OK twice to close the dialog.    """
        ia_ribbonobj.drilldown_parameter_popup(name_select='BUSINESS_REGION', value_select="Store,Business,Region",popup_close='ok')
        time.sleep(2)
        ok_btn_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(12)
        
        """    8. Select Format tab > Auto Drill. Then select Enable Auto Linking.     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
        time.sleep(4)
        
        """    9. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]') 
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 9a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 9b: Verify the column heading')            
        utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds01.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds01.xlsx', 'Step 9c: Verify the report data ', desired_no_of_rows=15)
        time.sleep(5)
        
        """    10. Click on 2016 in Sales Year from ACROSS label and verify the drill down menu.    """
        utillobj.asequal(False,True, "Step 10: ACT-618 already exist for not able to click on across cells, once the case is fixed, scripts will be updated")
        
        """    11. Click on Accessories under North America and verify the drill down menu.    """
        values=['Drill down to Product Subcategory', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 7, 1, values, "Step 11: Verify the Accessories menu")
        time.sleep(5)
        pyautogui.moveTo(x_fr + 15, y_fr + 85)
        time.sleep(1)
        pyautogui.click(x_fr + 15, y_fr + 85, button='left')
        time.sleep(3)
        
        """    12. Click on North America and verify the drill down menu.    """
        values=['Drill down to Store Business Sub Region', 'Go to Information Builders Home Page', 'Drilldown-Region', 'Auto Links', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 7, 0, values, "Step 12: Verify the North America menu")
        time.sleep(5)
        
        """    13. Hover over the Auto Link tab and verify that shows "Target-Region"    """
        expected_value = ["Target-Region"]
        miscelanousobj.hover_field_menu_items_using_pyautogui('ITableData0', 7, 0, "Auto Links")
        x = driver.find_elements_by_css_selector("div[id='dt0_I0r7.0C0_x__0_5'][style*='block']")
        sub_menu = x[-1].find_elements_by_css_selector("span[id^='set0_I0r7']")
        actual_value=[el.text for el in sub_menu if el.text != '']
        utillity.UtillityMethods.asequal(self, expected_value, actual_value, "Step 13: Verify the autolink submenu")
        time.sleep(5)
        table_object=driver.find_element_by_css_selector("#ITableData0")
        x_fr1=table_object.location['x']
        y_fr1=table_object.location['y']
        pyautogui.click(x_fr +x_fr1 + 5, y_fr + y_fr1 + 95, button='left')
        time.sleep(5)
        
        """    14. Click on "Go to Information Builders Home Page" from drill down menu and verify the page opens. Close the page.    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, "Go to Information Builders Home Page")
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary= 'Summary']", 12,1, "Go to Information Builders Home Page", "Step 13a", browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7, x_offset_menu=x_fr+5, y_offset_menu=y_fr-7)
        time.sleep(6)
        utillobj.switch_to_default_content(1)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(2)
        owebpage=driver.current_url
        utillobj.asequal('https://www.informationbuilders.com/', owebpage, "Step 14a: Verify Information Builder page is displayed")
        time.sleep(2)
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        
        """    15. Click on North America and select "Drilldown-Region" and verify the page opens. Close the page.    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, "Drilldown-Region")
        time.sleep(10)
        utillobj.switch_to_default_content(1)
        time.sleep(2)
        utillobj.switch_to_window(1)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        #iarun.verify_table_data_set("table[summary= 'Summary']", "C2226967_Ds02.xlsx", "Step 15a: Verify that 'Drilldown-Region' report opens on separate page")
        time.sleep(1)
        self.driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        
        """    16. Click on North America and select "Auto Link tab" > "Target-Region" and verify the page opens. Close the page.    """
        miscelanousobj.select_field_menu_items('ITableData0', 7, 0, 'Auto Links->Target-Region', browser_height=80, x_offset=x_fr, y_offset=y_fr-7)
        time.sleep(10)
        utillobj.switch_to_default_content(1)
        time.sleep(2)
        utillobj.switch_to_window(1)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.verify_table_data_set("table[summary= 'Summary']", "C2226967_Ds03.xlsx", "Step 16a: Verify that 'Target-Region' report opens on separate page")
        time.sleep(2)
        utillobj.switch_to_default_content(1)
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        
        """    17. Click on North America and Click on Drill down to Store Business Sub Region.    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, "Drill down to Store Business Sub Region")
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 17a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 17b: Verify the column heading')            
        utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', 'Step 17c: Verify the report data ', desired_no_of_rows=15)
        time.sleep(5)
        
        """    18. Click on Canada and verify the drill menu    """
        values = ['Restore Original', 'Drill up to Store Business Region', 'Drill down to Store Country', 'Go to Information Builders Home Page', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 0, values, "Step 18: Verify the menu")
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    19. Click IA > Save As> Type C2229710 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    20. Open saved fex. http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2229710a.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    21. Click format tab and Verify that Auto Drill is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 21a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
        
        """    22. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
