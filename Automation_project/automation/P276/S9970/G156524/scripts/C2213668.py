'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2213668
TestCase Name = Drilling down on ACROSS field create two breadcrumb lines
'''
import unittest, time, pyautogui
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, visualization_metadata, ia_ribbon, ia_resultarea
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2213668_TestClass(BaseTestCase):
    
    def test_C2213668(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2213668"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """    1. Launch the IA report API with wf_retail_lite    """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P276/S9970', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)   
        time.sleep(15)
        
        """    2. Add Store,Business,Region to BY    """
        metaobj.datatree_field_click("Store,Business,Region", 2, 1)
        
        """    3. Add a Filter for Store,Business,Region equal to North America    """
        """    4. Click OK twice to close the filter dialog    """
        metaobj.datatree_field_click("Store,Business,Region", 1, 1,'Filter')
        time.sleep(3)
        ia_ribbonobj.create_constant_filter_condition('All', ['North America'])
        time.sleep(5)
        
        """    5. In the ribbon click on File    """
        ribbonobj.select_ribbon_item("Home", "File")
        
        """    6. In the dialog select the baseapp folder and name it C2213668A And click the Save button   """
        apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
        x=[el.text.strip() for el in self.driver.find_elements_by_css_selector(apps_css)]
        apps=self.driver.find_elements_by_css_selector(apps_css)
        apps[x.index('baseapp')].find_element_by_css_selector("img[src*='folder']").click()
        time.sleep(5)
        utillobj.ibfs_save_as("C2213668A", "Binary (*.ftm)")
        
        """    7. At the bottom of the Live Preview screen click on Create Report    """
        ia_resultobj.create_hold_type("Create Report")
        
        """    8. Select Data > Switch > baseapp/wf_retail_lite    """
        ribbonobj.select_ribbon_item("Data", "switch")
        utillobj.select_or_verify_bipop_menu("baseapp/wf_retail_lite")
        time.sleep(5)
        
        """    9. Place Quantity,Sold in SUM and Store,Business,Sub Region in BY    """
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Store,Business,Sub Region", 2, 1)
        time.sleep(8)
        
        """    10. Select Data > Filter    """
        ribbonobj.select_ribbon_item("Data", "Filter")
        time.sleep(8)
        
        """    11. Double click where it says in red "Double-click or press F2 to edit!"    """
        cond_elem=driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span>span>span")
        if browser_type=='Firefox':
            utillobj.click_type_using_pyautogui(cond_elem,doubleClick=True)
        else:
            action1 = ActionChains(self.driver)
            action1.double_click(cond_elem).perform()
            del action1
        time.sleep(5)
        
        """    12. Change the Type from Field to Subquery    """
        driver.find_element_by_css_selector("#id_where_field_subquery_type_combo").click()
        time.sleep(5)
        menu_items=self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        actual_popup_list=[el.text.strip() for el in menu_items]
        menu_items[actual_popup_list.index('Subquery')].click()
        time.sleep(5)
        if browser_type=='Firefox':
            driver.find_element_by_css_selector("div[id^='InlineControlSubqueryOperator']").click()
            time.sleep(3)
        menu_items=self.driver.find_elements_by_css_selector("div[id='wndWhereSubqueryOperatorPopup'][style*='inherit'] div[id^='BiListItem']")
        actual_popup_list=[el.text.strip() for el in menu_items]
        menu_items[actual_popup_list.index('In list')].click()
        time.sleep(5)
        
        """    13. Click on <Subquery> and select baseapp/C2213668A    """
        if browser_type=='Firefox':
            condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2)  span[class*='selected']>span>span")
            get_browser_height = utillobj.get_browser_height()
            browser_height=get_browser_height['browser_height']
            x_fr=condition_elem[len(condition_elem)-1].location["x"]
            y_fr=condition_elem[len(condition_elem)-1].location["y"]
            pyautogui.moveTo(x_fr+10,y_fr+browser_height)
            time.sleep(2)
            pyautogui.doubleClick(x_fr+25,y_fr+browser_height+8,button='left')
            time.sleep(5)
        else:    
            driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree div[id^='InlineControlSubqueryValue']").click()
            time.sleep(1)
        utillobj.select_or_verify_bipop_menu("baseapp/C2213668A")
        time.sleep(5)
        
        """    14. Click OK to close the filter dialog    """
        ia_ribbonobj.close_filter_dialog(btn='ok')
        
        """    15. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    16. Click Run. A report with Auto Drill links should display.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 16a: Verify report data set")
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 1, text='Asia', font_color = 'cerulean_blue_2', msg='Step 16b ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 6, 1, text='East', font_color = 'cerulean_blue_2', msg='Step 16c ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 8, 1, text='Mexico', font_color = 'cerulean_blue_2', msg='Step 16d ')
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    17. Click "Save" in the toolbar > Type C2213668 > Click "Save" in the Save As dialog    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    18. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
