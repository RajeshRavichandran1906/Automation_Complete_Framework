'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197853
TestCase Name = Drilling down on ACROSS field create two breadcrumb lines
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, visualization_metadata, active_miscelaneous
from common.lib import utillity  
import time, pyautogui
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

class C2197853_TestClass(BaseTestCase):
    def test_C2197853(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2197853"
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        """    2. Multi select the fields "Product,Category" and "Quantity,Sold" from query pane by holding CTRL key    """       
        """    3. Right click on selected fields and select Delete.    """
        metaobj.querytree_field_click("Product,Category", 1)
        time.sleep(1)
        get_browser_height = utillobj.get_browser_height()
        browser_height = get_browser_height['browser_height']
        row_css="#queryTreeColumn td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()=='Quantity,Sold']
            new_element1=l[0].find_element_by_css_selector("img[class='icon']")
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()=='Quantity,Sold']
            new_element1=l[0].find_element_by_css_selector("img[class='icon']")
        time.sleep(2)
        x_fr=new_element1.location['x']
        y_fr=new_element1.location['y']
        pyautogui.moveTo(x_fr+40,y_fr+browser_height)
        time.sleep(2)
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        pyautogui.click(x_fr+40,y_fr+browser_height,button='left')
        keyboard.release(Key.ctrl)
        time.sleep(2)
        row_css="#queryTreeColumn tr[class*='selected'] img[class='icon']"
        new_element = self.driver.find_element_by_css_selector(row_css)
        x_fr=new_element.location['x']
        y_fr=new_element.location['y']
        pyautogui.moveTo(x_fr+40,y_fr+browser_height)
        time.sleep(2)
        pyautogui.click(x_fr+40,y_fr+browser_height,button='right')
        time.sleep(4)
        utillobj.select_or_verify_bipop_menu("Delete")
        time.sleep(8)
        
        """    4. Drag Store,Business,Sub Region (Store > Store > Store,Business,Sub Region ) from data pane
        and drop over Sale,Year under ACROSS bucket in query pane to replace    """
        metaobj.querytree_field_click("Sale,Year", 1, 1, "Delete")
        time.sleep(8)
        metaobj.datatree_field_click("Store,Business,Sub Region", 1, 1, "Across")
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
        iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04a: Verify Drill down to Store Business Sub Region data set")
        
        """    7. Click on Africa in the ACROSS labels and Select "Drill down to Store Country".    """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",1,2,'Drill down to Store Country', "Step 07")
        time.sleep(15)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]') 
        time.sleep(3)
        iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 07a: Verify Drill down to Store Country data set")
        time.sleep(4)
        utillobj.switch_to_default_content()
        time.sleep(4)
        
        """    8. Click IA > Save As> Type C2197853a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        
        """    9. Close the IA+ window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    10. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2197853.fex&tool=report    """
        """    11. Enter credentials if needed    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14) 
        
        """    12. Click format tab and see Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 12a: Active_Report - Verify Autodrill button is still selected")
        time.sleep(4)
        
        """    13. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    14. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]') 
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '4of4records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['Store Business Region', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US', 'REVENUE_US']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 14c: Verify the report data ')
        time.sleep(4)
        utillobj.switch_to_default_content()
        time.sleep(4)
        
        """    15. Click on Africa in the ACROSS labels and Select "Drill down to Store Country".    """
        status=False
        utillobj.asequal(True, status, "Step 15a: ACT-618 exist for this case, once it is fixed, script will be updated")
        
        """    16. Click IA > Save As> Type C2197853b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    17. Close the IA+ window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    18. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2197853b.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14) 
        
        """    19. Click format tab and see Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 19a: Active_Report - Verify Autodrill button is still selected")
        time.sleep(4)
        
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
