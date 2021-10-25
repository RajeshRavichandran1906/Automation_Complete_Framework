'''
Created on Jan 10, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330298
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 11)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8330298_TestClass(BaseTestCase):

    def test_C8330298(self):

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
        Step 2:For the following ALPHA fields, select Filter, then Between, using a pair of values.

        ALPHA ORDER - 000005 - 000010
        ALPHA ANV - 000100 - 000120
        ALPHA TEXT - 000555 - 000570
        ALPHA A80 - 000001 - 000002
        ALPHA Edit - G-100 - G104
        ALPHA Store Code - R1020 - R1041
        ALPHA Vendor Code - V303 - V305
        ALPHA Vendor Name - European Specialties, - Evelina Imports,Ltd
        ALPHA Product Code - F103 - F103
        ALPHA Product Descr. - French Roast - Hazelnut
        
        Verify that the report contains only those rows that are Between these values:
        
        Expect 6 rows - values 000005 - 000010
        Expect 21 rows - values 000100 - 000120
        Expect 16 rows - values 000555 - 000570
        Expect 2 rows - values 000001 - 000002
        Expect 201 row - values G-100 - G-104
        Expect 269 rows - values R1020 - R1041
        Expect 334 rows - values V303 - V305
        Expect 251 rows - values European Specialties, - Evelina Imports,Ltd
        Expect 148 rows - values F103 - F103
        Expect 302 rows - values French Roast - Hazelnut
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'large', value1='000005', value2='000010')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '6of1000records,Page1of1', "Step 06.1: Expect 6 rows - value 000005 - 000010")
        active_report_obj.close_filter_dialog()
         
        """ALPHA ANV - 000100 - 000120"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'large', value1='000100',value2='000120')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '21of1000records,Page1of1', "Step 06.2: Expect 21 rows - values 000100 - 000120")
        active_report_obj.close_filter_dialog()
         
        """ALPHA TEXT - 000555 - 000570"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'large', value1='000555',value2='000570')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '16of1000records,Page1of1', "Step 06.3: Expect 16 rows - values 000555 - 000570")
        active_report_obj.close_filter_dialog()
         
        """ALPHA A80 - 000001 - 000002"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'large', value1='000001',value2='000002')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '2of1000records,Page1of1', "Step 06.4: Expect 2 rows - values 000001 - 000002")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Edit - G-100 - G104"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'small',value1='G-100', value2='G-104')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '201of1000records,Page1of4', "Step 06.5: Expect 201 row - values G-100 - G-104")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Store Code - R1020 - R1041"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'small', value1='R1020',value2='R1041')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '269of1000records,Page1of5', "Step 06.6: Expect 269 rows - values R1020 - R1041")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Code - V303 - V305"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'small', value1='V303',value2='V305')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '334of1000records,Page1of6', "Step 06.7: Expect 334 rows - values V303 - V305")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Vendor Name - European Specialties, - Evelina Imports,Ltd"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'small', value1='European Specialities,',value2='Evelina Imports, Ltd')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '251of1000records,Page1of5', "Step 06.8: Expect 251 rows - values European Specialties, - Evelina Imports,Ltd")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Code - F103 - F103"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'small', value1='F103',value2='F103')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '148of1000records,Page1of3', "Step 06.9: Expect 331 rows - values F103 - F103")
        active_report_obj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast - Hazelnut"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Between')        
        active_report_obj.create_filter(1, 'Between', 'small', value1='French Roast',value2='Hazelnut')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '302of1000records,Page1of6', "Step 06.10: Expect 302 rows - values French Roast - Hazelnut")
        active_report_obj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()