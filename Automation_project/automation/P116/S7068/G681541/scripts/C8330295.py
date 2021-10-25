'''
Created on Jan 9, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330295
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 8)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330295_TestClass(BaseTestCase):

    def test_C8330295(self):

        """
           CLASS OBJECTS
        """ 
        
        utillobj = utillity.UtillityMethods(self.driver)
        active_report_obj=Active_Report(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+"/"+suite_id
        
        """
            TESTCASE VARIABLES
        """
        fex_name="AR-RP-141AL.fex"
        
        """
            CSS
        """
        table_css="ITableData0"
        data_value_css="#"+table_css+" tbody tr:nth-child(4) td:nth-child(2)"
        
        """
        Step 1: Execute AR-RP-141AL.fex from below API to produce the alphanumeric output
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='000001', repository_path=folder_path)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2:For the following ALPHA fields, select Filter, then Greater than or equal to these values:
        
        ALPHA ORDER - 000005
        ALPHA ANV - 000010
        ALPHA TEXT - 000015
        ALPHA A80 - 000020
        ALPHA Edit - G-104
        ALPHA Store Code - R1020
        ALPHA Vendor Code - V102
        ALPHA Vendor Name - Thermo Tech, Inc
        ALPHA Product Code - G100
        ALPHA Product Descr. - French Roast
        
        Verify that the report contains only those rows that are Greater than or equal to these values.
        
        Expect 996 rows - value 000005
        Expect 991 rows - value 000010
        Expect 986 rows - value 000015
        Expect 981 rows - value 000020
        Expect 200 rows - value G-104
        Expect 910 rows - value R1020
        Expect 566 rows - value V102
        Expect 215 rows - value Thermo Tech, Inc
        Expect 334 rows - value G100
        Expect 620 rows - value French Roast.
        """
        active_report_obj.select_menu_items('ITableData0', 1, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'large', value1='000005')
        filter1_0=['ALPHA ORDER','Greater than or equal to','000005']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.1: Verify filter dialog',filter1_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '996of1000records,Page1of18', "Step 03.2: Expect 996 rows - value 000005")
        active_report_obj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        active_report_obj.select_menu_items('ITableData0', 2, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'large', value1='000010')
        filter2_0=['ALPHA ANV','Greater than or equal to','000010']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.3: Verify filter dialog',filter2_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '991of1000records,Page1of18', "Step 03.4: Expect 991 rows - value 000010")
        active_report_obj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        active_report_obj.select_menu_items('ITableData0', 3, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'large', value1='000015')
        filter3_0=['ALPHA TEXT','Greater than or equal to','000015']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.5: Verify filter dialog',filter3_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '986of1000records,Page1of18', "Step 03.6: Expect 986 rows - value 000015")
        active_report_obj.close_filter_dialog()
         
        """ALPHA A80 - 000020"""
        active_report_obj.select_menu_items('ITableData0', 4, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'large', value1='000020')
        filter4_0=['ALPHA A80','Greater than or equal to','000020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.7: Verify filter dialog',filter4_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '981of1000records,Page1of18', "Step 03.8: Expect 981 rows - value 000020")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        active_report_obj.select_menu_items('ITableData0', 5, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'small', value1='G-104')
        filter5_0=['ALPHA Edit','Greater than or equal to','G-104']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.9: Verify filter dialog',filter5_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '200of1000records,Page1of4', "Step 03.10: Expect 200 rows - value G-104")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        active_report_obj.select_menu_items('ITableData0', 6, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'small', value1='R1020')
        filter6_0=['ALPHA Store Code','Greater than or equal to','R1020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.11: Verify filter dialog',filter6_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '910of1000records,Page1of16', "Step 03.12: Expect 910 rows - value R1020")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        active_report_obj.select_menu_items('ITableData0', 7, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'small', value1='V102')
        filter7_0=['ALPHA Vendor Code','Greater than or equal to','V102']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.13: Verify filter dialog',filter7_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '566of1000records,Page1of10', "Step 03.14: Expect 566 rows - value V102")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        active_report_obj.select_menu_items('ITableData0', 8, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'small', value1='ThermoTech, Inc')
        filter8_0=['ALPHA Vendor Name','Greater than or equal to','ThermoTech, Inc']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.15: Verify filter dialog',filter8_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '215of1000records,Page1of4', "Step 03.16: Expect 215 rows - value Thermo Tech, Inc")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        active_report_obj.select_menu_items('ITableData0', 9, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'small', value1='G100')
        filter9_0=['ALPHA Product Code','Greater than or equal to','G100']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.17: Verify filter dialog',filter9_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '334of1000records,Page1of6', "Step 03.18: Expect 334 rows - value G100")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        active_report_obj.select_menu_items('ITableData0', 10, 'Filter','Greater than or equal to')        
        active_report_obj.create_filter(1, 'Greater than or equal to', 'small', value1='French Roast')
        filter10_0=['ALPHA Product Descr.','Greater than or equal to','French Roast']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 03.19: Verify filter dialog',filter10_0)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '620of1000records,Page1of11', "Step 03.20: Expect 620 rows - value French Roast")
        active_report_obj.close_filter_dialog()


if __name__ == "__main__":
    unittest.main()