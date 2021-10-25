'''
Created on Jan 22, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251742
Test_Case Name : AHTML:CMPD/ALL is NOT in list but all records shown in o/p (128951)
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous
from common.lib import utillity

class C2251742_TestClass(BaseTestCase):

    def test_C2251742(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251742'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
            
        """
            Step 01 : Using infoassist, Create a new Document using Car masterfile Insert a new report with COUNTRY,CAR, and SEATS fields
        """
        utillobj.infoassist_api_login('document','ibisamp/car','P116/S10071_5', 'mrid', 'mrpass')
        visul_result.wait_for_property("#canvasFrame svg", 1, 40)
        time.sleep(3)
        
        metadata.datatree_field_click('COUNTRY',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'COUNTRY', 8)
        
        metadata.datatree_field_click('CAR',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(5)>td", 'CAR', 8)
        
        metadata.datatree_field_click('SEATS',2,1) 
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(3)>td", 'SEATS', 8)
        
        """
            Step 02 : Click insert tab and select dropdown list box
        """ 
        visul_ribbon.select_ribbon_item('Insert', 'drop_down')
        visul_ribbon.repositioning_document_component('4.5', '1.05')
        
        """
            Step 03 : Right click dropdown list and select properties
        """
        visul_result.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        
        """
            Step 04 : Now Active Dashboard Properties dialog box appears
        """
        utillobj.verify_element_text("#adpPropertiesDlg div[class*='bi-window-caption'] div[class='bi-label']", 'Active Dashboard Properties', 'Step 04.1 : Verify Active Dashboard Properties dialog box appears')
        
        """
            Step 05 : From that assign report1 in report box and assign seats in field box and assign equal to in condition box
            Step 06 : Uncheck include all and click apply and click ok button
        """
        visul_result.customize_active_dashboard_properties(source={'select_field':'SEATS', 'select_includeall':'yes'})

        """
            Step 07 : Run the report
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'COUNTRY', 35)
        
        """
            Step 08 : Check that the report displays all records instead of specified records in the list 
        """
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx', 'Step 08.1 : Verify report displays all records instead of specified records in the list ')
        active.verify_page_summary(0, '2of10records,Page1of1', 'Step 08.2 : Verify page summary')
        utillobj.verify_dropdown_value('#combobox_dsPROMPT_1', ['2', '4', '5', '7', '8', '29'], 'Step 08.1 : Verify dropdown box values', '2', 'Step 08.2 : Verify 2 is selected as default in dropdown box')
        
if __name__ == '__main__':
    unittest.main()