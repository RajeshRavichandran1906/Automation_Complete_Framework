'''
Created on Jan 7, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330288&group_by=cases:section_id&group_order=asc&group_id=681541
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 1)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330292_TestClass(BaseTestCase):

    def test_C8330292(self):

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
            Step 01:Execute AR-RP-141AL to produce the alphanumeric output..
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='000001', repository_path=folder_path)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2 : For the following ALPHA fields, select Filter, then Not equal and use these multiple values:

        ALPHA ORDER - 000001 & 000005
        ALPHA ANV - 000010 & 000015
        ALPHA TEXT - 000020 & 000025
        ALPHA A80 - 000030 & 000035
        ALPHA Edit - B-141, B-142 & B-144
        ALPHA Store Code - R1100 & R1109
        ALPHA Vendor Code - V081, V100 & V303
        ALPHA Vendor Name - Coffee Connection & Thermo Tech, Inc
        ALPHA Product Code - B144, F101 & G121
        ALPHA Product Descr. - Coffee Grinder & Coffee Pot

        Verify that the report contains only those rows that do Not match the selected values.
        .
        Expect 998 rows - not values 000001 & 000005
        Expect 998 rows - not values 000010 & 000015
        Expect 998 rows - not values 000020 & 000025
        Expect 998 rows - not values 000030 & 000035
        Expect 665 rows - not values B-141, B-142 & B-144
        Expect 839 rows - not values R1100 & R1109
        Expect 802 rows - not values V081, V100 & V303
        Expect 849 rows - not values Coffee Connection & Thermo Tech, Inc
        Expect 816 rows - not values B144, F101 & G121
        Expect 867 rows - not values Coffee Grinder & Coffee Pot
        """
        #Expect 998 rows - not values 000001 & 000005
        active_report_obj.select_menu_items(table_css, "1", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal','large',value1='000001', value2='000005')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '998of1000records,Page1of18', "Step 2:01: Expect 998 rows - not values 000001 & 000005")
        active_report_obj.close_filter_dialog()
        
        #Expect 998 rows - not values 000010 & 000015
        active_report_obj.select_menu_items(table_css, "2", "Filter" ,"Not equal")
        active_report_obj.create_filter(1, 'Not equal','large',value1='000010', value2='000015')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '998of1000records,Page1of18', "Step 2:02: Expect 998 rows - not values 000010 & 000015")
        active_report_obj.close_filter_dialog()
        
        #Expect 998 rows - not values 000020 & 000025
        active_report_obj.select_menu_items(table_css, "3", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal','large',value1='000020', value2='000025')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '998of1000records,Page1of18', "Step 2:03: Expect 998 rows - not values 000020 & 000025")
        active_report_obj.close_filter_dialog()
        
        #Expect 998 rows - not values 000030 & 000035
        active_report_obj.select_menu_items(table_css, "4", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal','large',value1='000030',value2='000035')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '998of1000records,Page1of18', "Step 2:04: Expect 998 rows - not values 000030 & 000035")
        active_report_obj.close_filter_dialog()    
         
        #Expect 665 rows - not values B-141, B-142 & B-144
        active_report_obj.select_menu_items(table_css, "5", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='B-141', value2='B-142', value3='B-144')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '665of1000records,Page1of12', "Step 2:05: Expect 665 rows - not values B-141, B-142 & B-144")
        active_report_obj.close_filter_dialog()
         
        #Expect 839 rows - not values R1100 & R1109
        active_report_obj.select_menu_items(table_css, "6", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='R1100', value2='R1109')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '839of1000records,Page1of15', "Step 2:06: Expect 939 rows - not values R1100 & R1109")
        active_report_obj.close_filter_dialog()
         
        #Expect 802 rows - not values V081, V100 & V303
        active_report_obj.select_menu_items(table_css, "7", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='V081', value2='V100', value3='V303' )
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '802of1000records,Page1of15', "Step 2:07: Expect 802 rows - not values V081, V100 & V303")
        active_report_obj.close_filter_dialog()
 
         
        # Expect 849 rows - not values Coffee Connection & Thermo Tech, Inc
        active_report_obj.select_menu_items(table_css, "8", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='Coffee Connection',value2='ThermoTech, Inc')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '849of1000records,Page1of15', "Step 2:08: Expect 933 rows - not value Thermo Tech, Inc")
        active_report_obj.close_filter_dialog()
         
        # Expect 816 rows - not values B144, F101 & G121
        active_report_obj.select_menu_items(table_css, "9", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='B144', value2='F101',value3='G121')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '816of1000records,Page1of15', "Step 2:  Expect 816 rows - not values B144, F101 & G121")
        active_report_obj.close_filter_dialog()
 
        #  Expect 867 rows - not values Coffee Grinder & Coffee Pot
        active_report_obj.select_menu_items(table_css, "10", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='Coffee Grinder',value2='Coffee Pot')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '867of1000records,Page1of16', "Step 2:09:  Expect 867 rows - not values Coffee Grinder & Coffee Pot")
        active_report_obj.close_filter_dialog()
        
if __name__ == '__main__':
    unittest.main()