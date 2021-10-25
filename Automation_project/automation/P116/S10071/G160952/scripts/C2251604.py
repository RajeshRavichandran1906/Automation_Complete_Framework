'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251604
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity

class C2251604_TestClass(BaseTestCase):

    def test_C2251604(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251604'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        oWith_ALL_expected=['[All]', '186534', '189217', '190081', '190695', '308986', '333414', '360570', '421377', '630054', '878063']
        oWithout_ALL_expected=['186534', '189217', '190081', '190695', '308986', '333414', '360570', '421377', '630054', '878063']
        
        """    1. Launch IA to develop a New Document.
        Select 'GGSales' as master file, and change output format as Active report.
        Select Category, Product,Unit Sales to get a report    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document') 
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=15)    
        metaobj.datatree_field_click("Product", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 8, expire_time=15)  
        ribbonobj.repositioning_document_component('0.5', '0.75')
        coln_list = ['Category', 'Product', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 01a: Verify column titles")
        
        
        """    2.     
                Now, select Radio button from 'Insert' tab    """
        ribbonobj.select_ribbon_item("Insert", "Radio_button")
        ribbonobj.repositioning_document_component('8', '1')
        
        """    3. Right click on Radio_button prompt    """
        resultobj.choose_right_click_menu_item_for_prompt("#Prompt_1", 'Properties')
        
        """    4. Select Field as "Unit Sales". Make sure condition = Equal to and Include All is checked.    """
        """    5. Click Ok    """
        source={'select_field':'Unit Sales', 'verify_condition':'Equal to','verify_includeall':True}
        resultobj.customize_active_dashboard_properties('None', source, 'None')
        
        """    6. Click run. Check 'All' option is present in the list box    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 30)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 06a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 06b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251604_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251604_Ds01.xlsx', 'Step 06c: Verify data.')
        p1=driver.find_elements_by_css_selector("#radiobuttonPROMPT_1 table tr")
        actual_prompt1_values=[el.text.strip() for el in p1]
        utillobj.asequal(actual_prompt1_values, oWith_ALL_expected, "Step 06d: Check 'All' option is present in the radiobutton box")
        oCheck=driver.find_element_by_css_selector("#radiobuttonPROMPT_1 table tr input[checked]").get_attribute('value')
        utillobj.asequal(oCheck, '[All]', "Step 06e: Verify the first radiobutton is 'All' and selected")
        
        """    7. Close dashboard runtime window by clicking 'X' button.    """
        utillobj.switch_to_default_content()
        time.sleep(3)
        resultobj.select_panel_caption_btn(0, select_type='close', custom_css="[class*='active'] [class*='caption'][class*='window']")
        
        """    8. Right click on list box prompt    """
        resultobj.choose_right_click_menu_item_for_prompt("#Prompt_1", 'Properties')
        
        """    9. uncheck "Include All" option    """
        source={'select_includeall':True}
        resultobj.customize_active_dashboard_properties('None', source, 'None')
        
#         oCheck_All=driver.find_element_by_css_selector("[id='adpPropertiesDlg'] #checkShowAll input[checked]")
#         utillobj.default_left_click(object_locator=oCheck_All)
#         time.sleep(2) 
#         oCheck_All_status=driver.find_element_by_css_selector("[id='adpPropertiesDlg'] #checkShowAll input").is_selected()       
#         utillobj.asequal(oCheck_All_status, False, "Step 09a: Verify 'Include All' checkbox is checked off")
        
        """    10. Click Ok. Run the dashboard. Verify 'All' option is no more available on dashboard prompt.    """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 30)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 10a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 10b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251604_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251604_Ds02.xlsx', 'Step 10c: Verify data.')
        p1=driver.find_elements_by_css_selector("#radiobuttonPROMPT_1 table tr")
        actual_prompt1_values=[el.text.strip() for el in p1]
        utillobj.asequal(actual_prompt1_values, oWithout_ALL_expected, "Step 10d: Check 'All' option is not present in the radiobutton box")
        oCheck=driver.find_element_by_css_selector("#radiobuttonPROMPT_1 table tr input[checked]").get_attribute('value')
        utillobj.asequal(oCheck, '186534', "Step 10e: Verify the first radiobutton is '186534' and selected")
        utillobj.switch_to_default_content()
        time.sleep(3)
                
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()