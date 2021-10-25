'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234768
TestCase Name = Verify promoting HOLD file to Document mode
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

class C2234768_TestClass(BaseTestCase):

    def test_C2234768(self):
        
        Test_Case_ID = "C2234768"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Launch IA Document mode: http://machine:port/ibi_apps/ia?tool=Document&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032    """
        utillobj.infoassist_api_login('document','ibisamp/CAR','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=10, string_value='Document')  
        time.sleep(1)
        
        """    2. Select Insert Tab > Click "Report"        """
        ribbonobj.select_ribbon_item("Insert", "Report")
        
        """    3. Select Home Tab > Click "Theme" icon.    """
        ribbonobj.select_ribbon_item("Home", "Theme")
        
        """    4. Verify new themes in default "Templates" folder    """
        exp_item_list=['Dark.sty', 'Flat.sty', 'Warm.sty']
        act_item_list=[el.text.strip() for el in driver.find_elements_by_css_selector("#paneIbfsExplorer_exList div[class$='content']>table>tbody>tr>td:nth-child(1)") if el.text.strip()!='']
        time.sleep(3)
        print(act_item_list)
        utillobj.asequal(act_item_list, exp_item_list, 'Step 04: Verify new themes file listed in default "Templates" folder')
        
        """    5. Select Theme = "Dark.sty".    """
        """    6. Click "Open".    """
        utillobj.select_item_from_ibfs_explorer_list('Dark.sty')
        time.sleep(10)
        
        """    7. Double click "COUNTRY", "CAR", "DEALER_COST".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 6, expire_time=10)
        metaobj.datatree_field_click("CAR", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 17, expire_time=10) 
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 28, expire_time=10) 
        
        """    8. Verify the selected theme has been applied to the report.    """
        oBackgrnd_color=driver.find_element_by_css_selector("#TableChart_1 div[style*='user-select'] div[style*='user-select']>div")
        actual_background_color=Color.from_string(oBackgrnd_color.value_of_css_property("background-color")).rgba
        print(actual_background_color)
        expected_background_color=utillobj.color_picker('nero', 'rgba')
        utillobj.asequal(actual_background_color, expected_background_color , "Step 08: Verification of Background color.")
        coln_list = ["COUNTRY", "CAR", "DEALER_COST"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 08a: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1', 10, 3, 'C2234768_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, 'C2234768_Ds01.xlsx', 'Step 08b: Verify Preview report dataset')
        
        """    9. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        
        """    10. Verify the report is displayed.    """
        utillobj.switch_to_frame()
        miscobj.verify_cell_property('ITableData0', 0, 0, 'ENGLAND', 'Step 10(1):Verify the cell ENGLAND ',text_color='white',bg_color='nero')
        miscobj.verify_cell_property('ITableData0', 5, 1, 'MASERATI', 'Step 10(2):Verify the cell MASERATI ',text_color='white',bg_color='nero')
        miscobj.verify_cell_property('ITableData0', 9, 2, '49,500', 'Step 10(3):Verify the cell 49,500 ',text_color='white',bg_color='nero')
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 10a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "DEALER_COST"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 10b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2234768_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2234768_Ds02.xlsx', 'Step 10c: Verify data.')
        utillobj.switch_to_default_content()
        
        """    11. Select Insert Tab > Click "Page" to add a new page    """
        ribbonobj.select_ribbon_item("Insert", "Page")
        
        """    12. Double click "MODEL", "SALES"    """
        metaobj.datatree_field_click("MODEL", 2, 1)
        resultobj.wait_for_property("#TableChart_2 div[class^='x']", 19, expire_time=10)
        metaobj.datatree_field_click("SALES", 2, 1)
        resultobj.wait_for_property("#TableChart_2 div[class^='x']", 38, expire_time=10)
        
        """    13. Verify the selected default Warm.sty theme is applied to the report on new page    """        
        oBackgrnd_color=driver.find_element_by_css_selector("#TableChart_2 div[style*='user-select'] div[style*='user-select']>div")
        actual_background_color=Color.from_string(oBackgrnd_color.value_of_css_property("background-color")).rgba
        expected_background_color=utillobj.color_picker('white', 'rgba')
        utillobj.asequal(actual_background_color, expected_background_color , "Step 13: Verification of Background color.")
        
        coln_list = ["MODEL", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_2", coln_list, "Step 13a: Verify column titles")
        ia_resultobj.create_report_data_set('TableChart_2', 15, 2, 'C2234768_Ds03.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_2', 15, 2, 'C2234768_Ds03.xlsx', 'Step 13b: Verify Preview report dataset', no_of_cells=2)
        
        """    14. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        
        """    15. Verify Dark Theme on Page 1    """
        utillobj.switch_to_frame()
        miscobj.verify_cell_property('ITableData0', 0, 0, 'ENGLAND', 'Step 15(1):Verify the cell ENGLAND ',text_color='white',bg_color='nero')
        miscobj.verify_cell_property('ITableData0', 5, 1, 'MASERATI', 'Step 15(2):Verify the cell MASERATI ',text_color='white',bg_color='nero')
        miscobj.verify_cell_property('ITableData0', 9, 2, '49,500', 'Step 15(3):Verify the cell 49,500 ',text_color='white',bg_color='nero')
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 15a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "DEALER_COST"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2234768_Ds02.xlsx', 'Step 15c: Verify data.')
        
        """    16. Click "Page 2" in the Active Report output window > Verify Warm Theme on Page 2    """
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        driver.find_element_by_css_selector(select_css).click()
        time.sleep(5)
        miscobj.verify_cell_property('ITableData1', 0, 1, '7800', 'Step 16(1):Verify the cell 7800 ',text_color='gray8',bg_color='transparent')
        miscobj.verify_cell_property('ITableData1', 9, 0, '530I 4 DOOR', 'Step 16(2):Verify the cell 530I 4 DOOR ',text_color='gray8',bg_color='transparent')
        miscobj.verify_cell_property('ITableData1', 17, 1, '12000', 'Step 16(3):Verify the cell 12000 ',text_color='gray8',bg_color='transparent')
        miscobj.verify_page_summary(1, '18of18records,Page1of1', 'Step 16a: Verify the Report Heading')
        column_list=["MODEL", "SALES"]
        miscobj.verify_column_heading('ITableData1', column_list, 'Step 16b: Verify the column heading')
        #utillobj.create_data_set('ITableData1', 'I1r', 'C2234768_Ds04.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', 'C2234768_Ds04.xlsx', 'Step 16c: Verify data.')
        utillobj.switch_to_default_content()
        
        """    17. Click "IA" > "Save".    """
        """    18. Enter Title = "C2234768".    """
        """    19. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    21. Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2234768.fex&tool=Document    """
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=10, string_value='Document')  
        
        """    22. Verify Dark.sty Theme on Page 1    """
        oBackgrnd_color=driver.find_element_by_css_selector("#TableChart_1 div[style*='user-select'] div[style*='user-select']>div")
        actual_background_color=Color.from_string(oBackgrnd_color.value_of_css_property("background-color")).rgba
        expected_background_color=utillobj.color_picker('nero', 'rgba')
        utillobj.asequal(actual_background_color, expected_background_color , "Step 22: Verification of Background color.")
        
        coln_list = ["COUNTRY", "CAR", "DEALER_COST"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 22a: Verify column titles")
        
        """    23. Click on the "Page 1" menu in the upper right corner > Select "Page 2"    """
        ia_resultobj.select_or_verify_document_page_menu('Page 2')
        
        """    24. Verify Warm.sty Theme on Page 2    """
        oBackgrnd_color=driver.find_element_by_css_selector("#TableChart_2 div[style*='user-select'] div[style*='user-select']>div")
        actual_background_color=Color.from_string(oBackgrnd_color.value_of_css_property("background-color")).rgba
        print(actual_background_color)
        expected_background_color=utillobj.color_picker('white', 'rgba')
        utillobj.asequal(actual_background_color, expected_background_color , "Step 24: Verification of Background color.")
        coln_list = ["MODEL", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_2", coln_list, "Step 24a: Verify column titles")
        
        """    25. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
        
if __name__ == '__main__':
    unittest.main()