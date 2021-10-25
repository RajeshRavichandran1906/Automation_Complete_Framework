'''
Created on Jan 10, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330299
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 12)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8330299_TestClass(BaseTestCase):

    def test_C8330299(self):

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
        Step 2:For the following ALPHA fields, select Filter, then Not Between, using a pair of values.

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
        
        Verify that the report contains only those rows that are Not Between these values:
        
        Expect 994 rows - values 000005 - 000010
        Expect 979 rows - values 000100 - 000120
        Expect 984 rows - values 000555 - 000570
        Expect 998 rows - values 000001 - 000002
        Expect 799 row - values G-100 - G-104
        Expect 731 rows - values R1020 - R1041
        Expect 666 rows - values V303 - V305
        Expect 749 rows - values European Specialties, - Evelina Imports,Ltd
        Expect 852 rows - values F103 - F103
        Expect 698 rows - values French Roast - Hazelnut
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'large', value1='000005', value2='000010')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.move_active_popup('1', '600', '200')
        active_report_obj.verify_page_summary(0, '994of1000records,Page1of18', "Step 2.1: Expect 994 rows - value 000005 - 000010")
        active_report_obj.close_filter_dialog()
        
        """ALPHA ANV - 000100 - 000120"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'large', value1='000100',value2='000120')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '979of1000records,Page1of18', "Step 2.2: Expect 979 rows - values 000100 - 000120")
        active_report_obj.close_filter_dialog()
        
        """ALPHA TEXT - 000555 - 000570"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'large', value1='000555',value2='000570')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '984of1000records,Page1of18', "Step 2.3: Expect 984 rows - values 000555 - 000570")
        active_report_obj.close_filter_dialog()
        
        """ALPHA A80 - 000001 - 000002"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'large', value1='000001',value2='000002')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '998of1000records,Page1of18', "Step 2.4: Expect 998 rows - values 000001 - 000002")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Edit - G-100 - G104"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'small',value1='G-100', value2='G-104')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '799of1000records,Page1of15', "Step 2.5: Expect 799 row - values G-100 - G-104")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Store Code - R1020 - R1041"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'small', value1='R1020',value2='R1041')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '731of1000records,Page1of13', "Step 2.6: Expect 731 rows - values R1020 - R1041")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Code - V303 - V305"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'small', value1='V303',value2='V305')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '666of1000records,Page1of12', "Step 2.7: Expect 666 rows - values V303 - V305")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Name - European Specialties, - Evelina Imports,Ltd"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'small', value1='European Specialities,',value2='Evelina Imports, Ltd')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '749of1000records,Page1of14', "Step 2.8: Expect 749 rows - values European Specialties, - Evelina Imports,Ltd")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Code - F103 - F103"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'small', value1='F103',value2='F103')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '852of1000records,Page1of15', "Step 2.9: Expect 852 rows - values F103 - F103")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Descr. - French Roast - Hazelnut"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Not Between')        
        active_report_obj.create_filter(1, 'Not Between', 'small', value1='French Roast',value2='Hazelnut')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '698of1000records,Page1of13', "Step 2.10: Expect 698 rows - values French Roast - Hazelnut")
        active_report_obj.close_filter_dialog()

if __name__ == "__main__":
    unittest.main()