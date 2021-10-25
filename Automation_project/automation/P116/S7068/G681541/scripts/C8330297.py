'''
Created on Jan 10, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330297
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 10)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8330297_TestClass(BaseTestCase):

    def test_C8330297(self):

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
        Step 1:Execute AR-RP-141AL.fex from below API to produce the alphanumeric output
        Expect to see the following Active Report.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='000001', repository_path=folder_path)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")

        """
        Step 2 :For the following ALPHA fields, select Filter, then Less than or equal and these values:
        
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
        
        Verify that the report contains only those rows that are Less than or equal to these values.
        
        Expect 5 rows - value 000005
        Expect 10 rows - value 000010
        Expect 15 rows - value 000015
        Expect 20 rows - value 000020
        Expect 867 row - value G-104
        Expect 180 rows - value R1020
        Expect 518 rows - value V102
        Expect 852 rows - value Thermo Tech, Inc
        Expect 800 rows - value G100
        Expect 598 rows - value French Roast
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'large', value1='000005')
        filter1_2=['ALPHA ORDER','Less than or equal to','000005']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.1: Verify filter dialog',filter1_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '5of1000records,Page1of1', "Step 2.2: Expect 5 rows - value 000005")
        active_report_obj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'large', value1='000010')
        filter2_2=['ALPHA ANV','Less than or equal to','000010']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.3: Verify filter dialog',filter2_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '10of1000records,Page1of1', "Step 2.4: Expect 10 rows - value 000010")
        active_report_obj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'large', value1='000015')
        filter3_2=['ALPHA TEXT','Less than or equal to','000015']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.5: Verify filter dialog',filter3_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '15of1000records,Page1of1', "Step 2.6: Expect 15 rows - value 000015")
        active_report_obj.close_filter_dialog()
         
        """ALPHA A80 - 000020"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'large', value1='000020')
        filter4_2=['ALPHA A80','Less than or equal to','000020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.7: Verify filter dialog',filter4_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '20of1000records,Page1of1', "Step 2.8: Expect 20 rows - value 000020")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'small', value1='G-104')
        filter5_2=['ALPHA Edit','Less than or equal to','G-104']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.9: Verify filter dialog',filter5_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '867of1000records,Page1of16', "Step 2.10: Expect 867 rows - value G-104")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'small', value1='R1020')
        filter6_2=['ALPHA Store Code','Less than or equal to','R1020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.11: Verify filter dialog',filter6_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '180of1000records,Page1of4', "Step 2.12: Expect 180 rows - value R1020")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'small', value1='V102')
        filter7_2=['ALPHA Vendor Code','Less than or equal to','V102']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.13: Verify filter dialog',filter7_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '518of1000records,Page1of10', "Step 2.14: Expect 518 rows - value V102")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'small', value1='ThermoTech, Inc')
        filter8_2=['ALPHA Vendor Name','Less than or equal to','ThermoTech, Inc']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.15: Verify filter dialog',filter8_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '852of1000records,Page1of15', "Step 2.16: Expect 852 rows - value Thermo Tech, Inc")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'small', value1='G100')
        filter9_2=['ALPHA Product Code','Less than or equal to','G100']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.17: Verify filter dialog',filter9_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '800of1000records,Page1of15', "Step 2.18: Expect 800 rows - value G100")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Less than or equal to')        
        active_report_obj.create_filter(1, 'Less than or equal to', 'small', value1='French Roast')
        filter10_2=['ALPHA Product Descr.','Less than or equal to','French Roast']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.19: Verify filter dialog',filter10_2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '598of1000records,Page1of11', "Step 2.20: Expect 598 rows - value French Roast")
        active_report_obj.close_filter_dialog()



if __name__ == "__main__":
    unittest.main()