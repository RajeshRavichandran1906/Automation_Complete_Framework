'''
Created on Nov 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2068136
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui
from common.wftools import active_report

class C2068136_TestClass(BaseTestCase):

    def test_C2068136(self):
        active_report_obj = active_report.Active_Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')

        """
        Step 01: Execute the attached repro - ACT-379-xlsx. This repro SETs AREXPEXCEL to XLSX
        """
        utillobj.active_run_fex_api_login("ACT-379-xlsx.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.create_data_set('ITableData0', 'I0r', 'ACT_379_xlsx.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT_379_xlsx.xlsx','Step 01.3: Verify data set')
          
        """
        Step 02: Click the drop down for Country.Select the Export option, then Excel.
        """
        val = ['All records','Filtered only']
        active_report_obj.verify_menu_items('ITableData0', 0, 'Export->Excel', val, 'Step 02: Expect to see the options menu.' )
          
        """
        Step 03: Select All Records. If an ActiveX screen appears, click Allow.
        Step 04: Click or open the Excel file just downloaded.
        Step 05: Click the Excel Save button in the upper left corner of the spreadsheet.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','Excel','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2068136_actual_1_'+browser)
        utillobj.verify_xml_xls('C2068136_actual_1_'+browser+'.xlsx', 'C2068136_base_1_'+browser+'.xlsx', 'Step 05.1: Expect to see the Excel spreadsheet.')
         
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
        utillobj.switch_to_main_window()
         
        utillobj.infoassist_api_logout()
        
        """
        STep 06: Cancel/Exit the Excel Save menu. Execute the attached repro - ACT-379-exl2k. This repro SETs AREXPEXCEL to EXL2K
        """
        utillobj.active_run_fex_api_login("ACT-379-exl2k.fex", "S7077", 'mrid', 'mrpass')
        time.sleep(9)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 06.1: Verify Page Summary")
#         miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 06.2: Verify all columns listed on the report')
        time.sleep(2)
        utillobj.create_data_set('ITableData0', 'I0r', 'ACT_379_exl2k.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT_379_exl2k.xlsx','Step 06.3: Verify data set')
        
        """
        Step 07: Click the drop down for Country. Select the Export option, then Excel.
        """
        val = ['All records','Filtered only']
        miscelanousobj.verify_menu_items('ITableData0', 0, 'Export->XML (Excel)', val, 'Step 07: Expect to see the options menu.')
        
        """
        Step 08: Select All Records. If an ActiveX screen appears, click Allow.
        Step 09: Click or open the Excel file just downloaded.
        Step 10: Click the Excel Save button in the upper left corner of the spreadsheet.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','XML (Excel)','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2068136_actual_2_'+browser)
        utillobj.verify_xml_xls('C2068136_actual_2_'+browser+'.xls', 'C2068136_base_2_'+browser+'.xls', 'Step 10: Expect to see the Excel spreadsheet.')
        
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
        utillobj.switch_to_main_window()
        
        utillobj.infoassist_api_logout()


if __name__ == "__main__":
    unittest.main()