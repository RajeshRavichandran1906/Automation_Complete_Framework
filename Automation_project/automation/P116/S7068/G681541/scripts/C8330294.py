'''
Created on Jan 9, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/833294&group_by=cases:section_id&group_order=asc&group_id=681541
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 7)
'''

from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330294_TestClass(BaseTestCase):

    def test_C8330294(self):

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
        Step 2: For the following ALPHA fields, select Filter, then Greater than and use these values:

        ALPHA ORDER - 000005
        ALPHA ANV - 000010
        ALPHA TEXT - 000015
        ALPHA A80 - 00020
        ALPHA Edit - G-104
        ALPHA Store Code - R120
        ALPHA Vendor Code - V12
        ALPHA Vendor Name - Thermo Tech, Inc
        ALPHA Product Code - G100
        ALPHA Product Descr. - French Roast
        
        Verify that the report contains only those rows that are Greater than the value.
        
        Expect 995 rows - value 000005
        Expect 990 rows - value 000010
        Expect 985 rows - value 000015
        Expect 980 rows - value 00020
        Expect 133 rows - value G-104
        Expect 820 rows - value R120
        Expect 482 rows - value V12
        Expect 148 rows - value Thermo Tech, Inc
        Expect 200 rows - value G100
        Expect 42 rows - value French Roast.
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'large', value1='000005')
        filter1=['ALPHA ORDER','Greater than','000005']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.1: Verify filter dialog',filter1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '995of1000records,Page1of18', "Step 2.2: Expect 995 rows - value 000005")
        active_report_obj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'large', value1='000010')
        filter2=['ALPHA ANV','Greater than','000010']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.3: Verify filter dialog',filter2)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '990of1000records,Page1of18', "Step 2.4: Expect 990 rows - value 000010")
        active_report_obj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'large', value1='000015')
        filter3=['ALPHA TEXT','Greater than','000015']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.5: Verify filter dialog',filter3)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '985of1000records,Page1of18', "Step 2.6: Expect 985 rows - value 000015")
        active_report_obj.close_filter_dialog()
         
        """ALPHA A80 - 00020"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'large', value1='000020')
        filter4=['ALPHA A80', 'Greater than', '000020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.7: Verify filter dialog',filter4)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '980of1000records,Page1of18', "Step 2.8: Expect 980 rows - value 000020")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'small', value1='G-104')
        filter5=['ALPHA Edit','Greater than','G-104']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.9: Verify filter dialog',filter5)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '133of1000records,Page1of3', "Step 2.10: Expect 133 rows - value G-104")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'small', value1='R1020')
        filter6=['ALPHA Store Code','Greater than','R1020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.11: Verify filter dialog',filter6)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '820of1000records,Page1of15', "Step 2.12: Expect 820 rows - value R120")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'small', value1='V102')
        filter7=['ALPHA Vendor Code','Greater than','V102']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.13: Verify filter dialog',filter7)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '482of1000records,Page1of9', "Step 2.14: Expect 482 rows - value V12")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'small', value1='ThermoTech, Inc')
        filter8=['ALPHA Vendor Name','Greater than','ThermoTech, Inc']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.15: Verify filter dialog',filter8)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '148of1000records,Page1of3', "Step 2.16: Expect 148 rows - value Thermo Tech, Inc")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'small', value1='G100')
        filter9=['ALPHA Product Code','Greater than','G100']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.17: Verify filter dialog',filter9)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '200of1000records,Page1of4', "Step 2.18: Expect 200 rows - value G100")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Greater than')        
        active_report_obj.create_filter(1, 'Greater than', 'small', value1='French Roast')
        filter10=['ALPHA Product Descr.','Greater than','French Roast']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.19: Verify filter dialog',filter10)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '402of1000records,Page1of8', "Step 2.20: Expect 42 rows - value French Roast")
        
        
        
        

if __name__ == "__main__":
    unittest.main()