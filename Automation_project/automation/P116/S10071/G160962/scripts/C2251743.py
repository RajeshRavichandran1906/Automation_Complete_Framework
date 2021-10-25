'''
Created on Jan 19, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251743
Test_Case Name : AHTML:CMPD:.ALL. option not selected in Radiobutton & Checkbox (142482)
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous
from common.lib import utillity

class C2251743_TestClass(BaseTestCase):

    def test_C2251743(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251743'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
            
        """
            Step 01 : Using infoassist, Create a new document report using Car Masterfile.Change the format to Active report.
            Insert a new report with COUNTRY,CAR, MODEL and SEATS fields
        """
        utillobj.infoassist_api_login('document','ibisamp/car','P116/S10071_1', 'mrid', 'mrpass')
        visul_result.wait_for_property("#canvasFrame svg", 1, 40)
        time.sleep(3)
        
        metadata.datatree_field_click('COUNTRY',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'COUNTRY', 8)
        
        metadata.datatree_field_click('CAR',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(5)>td", 'CAR', 8)
         
        metadata.datatree_field_click('MODEL',2,1) 
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(6)>td", 'MODEL', 8)
        
        metadata.datatree_field_click('SEATS',2,1) 
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(3)>td", 'SEATS', 8)
        
        """
            Step 02 : Insert a checkbox and Radiobutton
        """
        visul_ribbon.select_ribbon_item('Insert', 'checkbox')
        visul_ribbon.repositioning_document_component('6.5', '1.04')
        
        visul_ribbon.select_ribbon_item('Insert', 'radio_button')
        visul_ribbon.repositioning_document_component('6.5', '2.5')
        
        """
            Step 03 : Right click on checkbox and select properties option then choose COUNTRY for field dropdown.
        """
        check_box=self.driver.find_element_by_id('Prompt_1')
        utillobj.default_click(check_box, click_option=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Properties')
        visul_result.customize_active_dashboard_properties(source={'select_field':'COUNTRY'})
        
        """
            Step 04 : Right click on Radiobutton and select properties option then choose CAR for field dropdown
        """
        radio_btn=self.driver.find_element_by_id('Prompt_2')
        utillobj.default_click(radio_btn, click_option=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Properties')
        visul_result.customize_active_dashboard_properties(source={'select_field':'CAR'})
        
        """
            Step 05 : Run the report
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'COUNTRY', 35)
        
        """
            Step 05.1 : Verify Report and ALL option selected in Radiobutton & Checkbox 
        """
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx', 'Step 05.1 : Verify Report data')
        active.verify_page_summary(0, '18of18records,Page1of1', 'Step 05.2 : Verify page summary')
        expected_ckeckbox_values=['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_radiobtn_values=['[All]', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        iarun.verify_active_dashboard_prompts('listbox', '#PROMPT_1_cs ', expected_ckeckbox_values, "Step 05.3 : Verify checkbox value and ['All'] is selected as default", '[All]')
        iarun.verify_active_dashboard_prompts('listbox', '#PROMPT_2_cs ', expected_radiobtn_values, "Step 05.4 : Verify radio button value and ['All'] is selected as default", '[All]')
        
if __name__ == '__main__':
    unittest.main()