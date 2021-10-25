'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2230843
TestCase Name = Test that Auto Drill works with Table of Contents option
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous
from common.lib import utillity  
import time, pyautogui
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2230843_TestClass(BaseTestCase):
    def test_C2230843(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2230843"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(40)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    3. Select Format > Table of Contents    """
        ribbonobj.select_ribbon_item("Format", "Table_of_contents")
        time.sleep(15)
        
        """    4. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        iframe_height=iframe.size['height']
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04a: Verify dataset")
        
        """    5. Double click Table of Contents icon on Upper left and drag the TOC panel to bottom    """
        toc_btn=driver.find_element_by_css_selector("#divtocDHTMLDummy > img")
        utillobj.click_type_using_pyautogui(obj_locator=toc_btn, doubleClick=True)
        time.sleep(10)
        toc_tree=driver.find_element_by_css_selector("#divtocDHTML #move")
        x_toc=toc_tree.location['x']
        y_toc=toc_tree.location['y']
        w_toc=toc_tree.size['width']
        pyautogui.moveTo(x_toc + x_fr + (w_toc/2), y_toc + y_fr + 75)
        time.sleep(2)
        pyautogui.dragTo(x_fr+450,y_fr+175)
        time.sleep(2)
                
        """    6. Expand North America and click Stereo Systems.     """
        iarun.select_toc_item('North America->Stereo Systems')
        time.sleep(15)
        #iarun.create_table_data_set("table[id='IBI_Page1'][summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        #iarun.verify_table_data_set("table[id='IBI_Page1'][summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 06a: Verify the Report should move to that entry")
        pyautogui.moveTo(x_fr + 50, y_fr + (iframe_height-15) + 75)
        pyautogui.click(x_fr + 50, y_fr + (iframe_height-15) + 75)
        time.sleep(3)
        
        """    7. Click on Stereo Systems in the Product Category column and select "Drill down to Product Subcategory".     """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[id='IBI_Page1'][summary='Summary']",7,2,'Drill down to Product Subcategory', "Step 7")
        time.sleep(15)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 07a: Verify auto drill down dataset")
        time.sleep(3)
        
        """    8. Double click Table of Contents icon on Upper left and drag the TOC panel to bottom.    """
        toc_btn=driver.find_element_by_css_selector("#divtocDHTMLDummy > img")
        utillobj.click_type_using_pyautogui(obj_locator=toc_btn, doubleClick=True)
        time.sleep(3)
        iarun.expand_toc("North America")
        time.sleep(1)
        toc_list=['North America','Boom Box','Home Theater Systems','Receivers','Speaker Kits','iPod Docking Station']
        iarun.verify_toc_item(toc_list, "Step 08a: Verify the TOC panel reflects the proper entries based on the drilldown")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        
        """    9. Click IA > Save As> Type C2230843 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    10. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2230843.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(35)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14)
         
        """    11. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 11a: Verify Autodrill button should be active")
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatReportToc").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 11b: Verify Table of Contents button should be active")
        time.sleep(4)
        
        """    12. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    13. Click RUN    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(1)
        time.sleep(4)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '7of28records,Page1of1', 'Step 13a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 13b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 13c: Verify the report data')
        
        """    14. Expand North America and click Stereo Systems    """
        driver.find_element_by_css_selector("#MAINTABLE_0 table[class='arByToc'] td[id='XFD_0_1']>span[class='arByTocItem']").click()
        time.sleep(3)
        #miscelanousobj.toc_select_item(0, 'Stereo Systems')
        self.driver.find_element(By.XPATH,"//*[@id='FD_0_1:4']//span[contains(text(),'Stereo Systems')]").click()
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '1of28records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 14c: Verify the report data')
        
        """    15. Click on Stereo Systems in the Product Category column and select "Drill down to Product Subcategory"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0, 1, 'Drill down to Product Subcategory')
        time.sleep(6)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 15a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Subcategory', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx', 'Step 15c: Verify the report data')
        
        """    16. Expand North America and Verify the TOC panel reflects the proper entries based on the drilldown    """
        driver.find_element_by_css_selector("#MAINTABLE_0 table[class='arByToc'] td[id='XFD_0_0']>span[class='arByTocItem']").click()
        time.sleep(3)
        expected_toc_items=['[All]', '-', 'North America', 'Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        actual_toc_items=[]
        item_css="#MAINTABLE_0 table[class='arByToc'] span[class='arByTocItem']"
        items=driver.find_elements_by_css_selector(item_css)
        for i in range(len(items)):
            print(items[i].text)
            actual_toc_items.append(items[i].text.strip())
        utillobj.asequal(expected_toc_items, actual_toc_items, "Step 16a: Verify the TOC panel reflects the proper entries based on the drilldown")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        
        """    17. Click IA > Save As> Type C2230843b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    18. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2230843b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    19. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 19a: Verify Autodrill button should be active")
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatReportToc").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 19b: Verify Table of Contents button should be active")
        time.sleep(4)
        
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
