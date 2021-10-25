'''
Created on Jan 10, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330296&group_by=cases:section_id&group_order=asc&group_id=681541
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 9)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330296_TestClass(BaseTestCase):

    def test_C8330296(self):

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
        Step 2:For the following ALPHA fields, select Filter, then Less than and use these values:
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
        
        Verify that the report contains only those rows that are Less than these values.
        
        Expect 4 rows - value 000005
        Expect 9 rows - value 000010
        Expect 14 rows - value 000015
        Expect 19 rows - value 000020
        Expect 800 rows - value G-104
        Expect 90 rows - value R1020
        Expect 434 rows - value V102
        Expect 785 rows - value Thermo Tech, Inc
        Expect 666 rows - value G100
        Expect 380 rows - value French Roast
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'large', value1='000005')
        filter1_1=['ALPHA ORDER','Less than','000005']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.1: Verify filter dialog',filter1_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '4of1000records,Page1of1', "Step 2.2: Expect 4 rows - value 000005")
        active_report_obj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'large', value1='000010')
        filter2_1=['ALPHA ANV','Less than','000010']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.3: Verify filter dialog',filter2_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '9of1000records,Page1of1', "Step 2.4: Expect 9 rows - value 000010")
        active_report_obj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'large', value1='000015')
        filter3_1=['ALPHA TEXT','Less than','000015']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.5: Verify filter dialog',filter3_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '14of1000records,Page1of1', "Step 2.6: Expect 14 rows - value 000015")
        active_report_obj.close_filter_dialog()
         
        """ALPHA A80 - 000020"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'large', value1='000020')
        filter4_1=['ALPHA A80','Less than','000020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.7: Verify filter dialog',filter4_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '19of1000records,Page1of1', "Step 2.8: Expect 19 rows - value 000020")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'small', value1='G-104')
        filter5_1=['ALPHA Edit','Less than','G-104']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.9: Verify filter dialog',filter5_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '800of1000records,Page1of15', "Step 2.10: Expect 800 rows - value G-104")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'small', value1='R1020')
        filter6_1=['ALPHA Store Code','Less than','R1020']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.11: Verify filter dialog',filter6_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '90of1000records,Page1of2', "Step 2.12: Expect 90 rows - value R1020")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'small', value1='V102')
        filter7_1=['ALPHA Vendor Code','Less than','V102']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.13: Verify filter dialog',filter7_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '434of1000records,Page1of8', "Step 2.14: Expect 434 rows - value V102")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'small', value1='ThermoTech, Inc')
        filter8_1=['ALPHA Vendor Name','Less than','ThermoTech, Inc']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.15: Verify filter dialog',filter8_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '785of1000records,Page1of14', "Step 2.16: Expect 785 rows - value Thermo Tech, Inc")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'small', value1='G100')
        filter9_1=['ALPHA Product Code','Less than','G100']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.17: Verify filter dialog',filter9_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '666of1000records,Page1of12', "Step 2.18: Expect 666 rows - value G100")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Less than')        
        active_report_obj.create_filter(1, 'Less than', 'small', value1='French Roast')
        filter10_1=['ALPHA Product Descr.','Less than','French Roast']
        active_report_obj.verify_filter_selection_dialog(True, 'Step 2.19: Verify filter dialog',filter10_1)
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '380of1000records,Page1of7', "Step 2.20: Expect 380 rows - value French Roast")
        active_report_obj.close_filter_dialog()
        


if __name__ == "__main__":
    unittest.main()