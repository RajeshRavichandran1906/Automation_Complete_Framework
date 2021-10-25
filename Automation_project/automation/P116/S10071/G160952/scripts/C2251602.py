'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251602
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity

class C2251602_TestClass(BaseTestCase):

    def test_C2251602(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251602'
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
        
        
        """    2. Now, select List box from 'Insert' tab    """
        ribbonobj.select_ribbon_item("Insert", "List")
        ribbonobj.repositioning_document_component('8', '1')
        
        """    3. Right click on list box prompt    """
        oListbox=driver.find_element_by_id("Prompt_1")
        utillobj.default_click(oListbox, click_option=1)
        utillobj.select_or_verify_bipop_menu('Properties')
        
        """    4. Select Field as "Unit Sales". Make sure condition = Equal to and Include All is checked.    """
        utillobj.select_combobox_item('comboSourceFields', 'Unit Sales')
        elem1=driver.find_element_by_css_selector("#comboConditions>div")
        d=utillobj.get_attribute_value(elem1, "text")
        utillobj.asequal(d['text'], 'Equal to', "Step 04a: Verify condition is 'Equal to'")
        utillobj.verify_object_visible("[id='adpPropertiesDlg'] #checkShowAll input[checked]", True, 'Step 04b: Verify Include All checkbox is enabled')
        
        """    5. Click Ok    """
        ok_Btn=driver.find_element_by_css_selector('#btnADPOK img')
        utillobj.default_left_click(object_locator=ok_Btn)
        time.sleep(5)
        
        """    6. Click run. Check 'All' option is present in the list box    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 06a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 06b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251602_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251602_Ds01.xlsx', 'Step 06c: Verify data.')
        p1=driver.find_elements_by_css_selector("#list_dPROMPT_1 table tr")
        actual_prompt1_values=[el.text.strip() for el in p1]
        utillobj.asequal(actual_prompt1_values, oWith_ALL_expected, "Step 06d: Check 'All' option is present in the list box")
        
        """    7. Close dashboard runtime window by clicking 'X' button.    """
        utillobj.switch_to_default_content()
        time.sleep(3)
        resultobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        
        """    8. Right click on list box prompt    """
        oListbox=driver.find_element_by_id("Prompt_1")
        utillobj.default_click(oListbox, click_option=1)
        utillobj.select_or_verify_bipop_menu('Properties')
        
        """    9. uncheck "Include All" option    """
        oCheck_All=driver.find_element_by_css_selector("[id='adpPropertiesDlg'] #checkShowAll input[checked]")
        utillobj.default_left_click(object_locator=oCheck_All)
        time.sleep(2) 
        oCheck_All_status=driver.find_element_by_css_selector("[id='adpPropertiesDlg'] #checkShowAll input").is_selected()       
        utillobj.asequal(oCheck_All_status, False, "Step 09a: Verify 'Include All' checkbox is checked off")
        
        """    10. Click Ok. Run the dashboard. Verify 'All' option is no more available on dashboard prompt.    """
        ok_Btn=driver.find_element_by_css_selector('#btnADPOK img')
        utillobj.default_left_click(object_locator=ok_Btn)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 10a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 10b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251602_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251602_Ds02.xlsx', 'Step 10c: Verify data.')
        p1=driver.find_elements_by_css_selector("#list_dPROMPT_1 table tr")
        actual_prompt1_values=[el.text.strip() for el in p1]
        utillobj.asequal(actual_prompt1_values, oWithout_ALL_expected, "Step 10d: Check 'All' option is present in the list box")
        utillobj.switch_to_default_content()
        time.sleep(3)
                
        """   Click "IA" > "Save".    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()