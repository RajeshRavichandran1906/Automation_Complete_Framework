'''
Created on Aug 18, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050556
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity


class C2050556_TestClass(BaseTestCase):

    def test_C2050556(self):
        """
            Step 01: Execute repro AR-RP-141AL.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141AL.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01.1: Execute AR-RP-141AL.fex")
        columns1=['Order Number INTEGER', 'ALPHA ORDER', 'ALPHA ANV', 'ALPHA TEXT', 'ALPHA A80', 'ALPHA Edit', 'ALPHA Store Code', 'ALPHA Vendor Code', 'ALPHA Vendor Name', 'ALPHA Product Code', 'ALPHA Product Descr.']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01.2: Verify all columns listed on the report')
         
        """
        Step 02: For the following ALPHA fields, select Filter, then Greater than and use these values:
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
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'large', value1='000005')
        filter1=['ALPHA ORDER','Greater than','000005']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.1: Verify filter dialog',filter1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '995of1000records,Page1of18', "Step 02.2: Expect 995 rows - value 000005")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'large', value1='000010')
        filter2=['ALPHA ANV','Greater than','000010']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.3: Verify filter dialog',filter2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 02.4: Expect 990 rows - value 000010")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'large', value1='000015')
        filter3=['ALPHA TEXT','Greater than','000015']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.5: Verify filter dialog',filter3)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 02.6: Expect 985 rows - value 000015")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA A80 - 000020"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'large', value1='000020')
        filter4=['ALPHA A80','Greater than','000020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.7: Verify filter dialog',filter4)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '980of1000records,Page1of18', "Step 02.8: Expect 980 rows - value 000020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'small', value1='G-104')
        filter5=['ALPHA Edit','Greater than','G-104']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.9: Verify filter dialog',filter5)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '133of1000records,Page1of3', "Step 02.10: Expect 133 rows - value G-104")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'small', value1='R1020')
        filter6=['ALPHA Store Code','Greater than','R1020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.11: Verify filter dialog',filter6)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 02.12: Expect 820 rows - value R1020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'small', value1='V102')
        filter7=['ALPHA Vendor Code','Greater than','V102']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.13: Verify filter dialog',filter7)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '482of1000records,Page1of9', "Step 02.14: Expect 482 rows - value V102")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'small', value1='ThermoTech, Inc')
        filter8=['ALPHA Vendor Name','Greater than','ThermoTech, Inc']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.15: Verify filter dialog',filter8)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '148of1000records,Page1of3', "Step 02.16: Expect 148 rows - value Thermo Tech, Inc")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'small', value1='G100')
        filter9=['ALPHA Product Code','Greater than','G100']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.17: Verify filter dialog',filter9)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '200of1000records,Page1of4', "Step 02.18: Expect 200 rows - value G100")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Greater than')        
        filterselectionobj.create_filter(1, 'Greater than', 'small', value1='French Roast')
        filter10=['ALPHA Product Descr.','Greater than','French Roast']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.19: Verify filter dialog',filter10)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '402of1000records,Page1of8', "Step 02.20: Expect 402 rows - value French Roast")
        filterselectionobj.close_filter_dialog()
         
        """
        Step 03: For the following ALPHA fields, select Filter, then Greater than or equal to these values:
         
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
        """
         
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'large', value1='000005')
        filter1_0=['ALPHA ORDER','Greater than or equal to','000005']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.1: Verify filter dialog',filter1_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '996of1000records,Page1of18', "Step 03.2: Expect 996 rows - value 000005")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'large', value1='000010')
        filter2_0=['ALPHA ANV','Greater than or equal to','000010']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.3: Verify filter dialog',filter2_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '991of1000records,Page1of18', "Step 03.4: Expect 991 rows - value 000010")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'large', value1='000015')
        filter3_0=['ALPHA TEXT','Greater than or equal to','000015']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.5: Verify filter dialog',filter3_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '986of1000records,Page1of18', "Step 03.6: Expect 986 rows - value 000015")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA A80 - 000020"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'large', value1='000020')
        filter4_0=['ALPHA A80','Greater than or equal to','000020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.7: Verify filter dialog',filter4_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '981of1000records,Page1of18', "Step 03.8: Expect 981 rows - value 000020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'small', value1='G-104')
        filter5_0=['ALPHA Edit','Greater than or equal to','G-104']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.9: Verify filter dialog',filter5_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '200of1000records,Page1of4', "Step 03.10: Expect 200 rows - value G-104")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'small', value1='R1020')
        filter6_0=['ALPHA Store Code','Greater than or equal to','R1020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.11: Verify filter dialog',filter6_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '910of1000records,Page1of16', "Step 03.12: Expect 910 rows - value R1020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'small', value1='V102')
        filter7_0=['ALPHA Vendor Code','Greater than or equal to','V102']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.13: Verify filter dialog',filter7_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '566of1000records,Page1of10', "Step 03.14: Expect 566 rows - value V102")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'small', value1='ThermoTech, Inc')
        filter8_0=['ALPHA Vendor Name','Greater than or equal to','ThermoTech, Inc']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.15: Verify filter dialog',filter8_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '215of1000records,Page1of4', "Step 03.16: Expect 215 rows - value Thermo Tech, Inc")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'small', value1='G100')
        filter9_0=['ALPHA Product Code','Greater than or equal to','G100']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.17: Verify filter dialog',filter9_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '334of1000records,Page1of6', "Step 03.18: Expect 334 rows - value G100")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Greater than or equal to')        
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'small', value1='French Roast')
        filter10_0=['ALPHA Product Descr.','Greater than or equal to','French Roast']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03.19: Verify filter dialog',filter10_0)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '620of1000records,Page1of11', "Step 03.20: Expect 620 rows - value French Roast")
        filterselectionobj.close_filter_dialog()
         
        """
        Step 04: For the following ALPHA fields, select Filter, then Less than and use these values:
         
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
        """
         
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'large', value1='000005')
        filter1_1=['ALPHA ORDER','Less than','000005']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.1: Verify filter dialog',filter1_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '4of1000records,Page1of1', "Step 04.2: Expect 4 rows - value 000005")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'large', value1='000010')
        filter2_1=['ALPHA ANV','Less than','000010']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.3: Verify filter dialog',filter2_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '9of1000records,Page1of1', "Step 04.4: Expect 9 rows - value 000010")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'large', value1='000015')
        filter3_1=['ALPHA TEXT','Less than','000015']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.5: Verify filter dialog',filter3_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '14of1000records,Page1of1', "Step 04.6: Expect 14 rows - value 000015")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA A80 - 000020"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'large', value1='000020')
        filter4_1=['ALPHA A80','Less than','000020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.7: Verify filter dialog',filter4_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '19of1000records,Page1of1', "Step 04.8: Expect 19 rows - value 000020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'small', value1='G-104')
        filter5_1=['ALPHA Edit','Less than','G-104']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.9: Verify filter dialog',filter5_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '800of1000records,Page1of15', "Step 04.10: Expect 800 rows - value G-104")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'small', value1='R1020')
        filter6_1=['ALPHA Store Code','Less than','R1020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.11: Verify filter dialog',filter6_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '90of1000records,Page1of2', "Step 04.12: Expect 90 rows - value R1020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'small', value1='V102')
        filter7_1=['ALPHA Vendor Code','Less than','V102']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.13: Verify filter dialog',filter7_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '434of1000records,Page1of8', "Step 04.14: Expect 434 rows - value V102")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'small', value1='ThermoTech, Inc')
        filter8_1=['ALPHA Vendor Name','Less than','ThermoTech, Inc']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.15: Verify filter dialog',filter8_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '785of1000records,Page1of14', "Step 04.16: Expect 785 rows - value Thermo Tech, Inc")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'small', value1='G100')
        filter9_1=['ALPHA Product Code','Less than','G100']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.17: Verify filter dialog',filter9_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '666of1000records,Page1of12', "Step 04.18: Expect 666 rows - value G100")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Less than')        
        filterselectionobj.create_filter(1, 'Less than', 'small', value1='French Roast')
        filter10_1=['ALPHA Product Descr.','Less than','French Roast']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.19: Verify filter dialog',filter10_1)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '380of1000records,Page1of7', "Step 04.20: Expect 380 rows - value French Roast")
        filterselectionobj.close_filter_dialog()
         
        """
        Step 05: For the following ALPHA fields, select Filter, then Less than or equal and these values:
 
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
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'large', value1='000005')
        filter1_2=['ALPHA ORDER','Less than or equal to','000005']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.1: Verify filter dialog',filter1_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 05.2: Expect 5 rows - value 000005")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA ANV - 000010"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'large', value1='000010')
        filter2_2=['ALPHA ANV','Less than or equal to','000010']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.3: Verify filter dialog',filter2_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 05.4: Expect 10 rows - value 000010")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA TEXT - 000015"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'large', value1='000015')
        filter3_2=['ALPHA TEXT','Less than or equal to','000015']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.5: Verify filter dialog',filter3_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 05.6: Expect 15 rows - value 000015")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA A80 - 000020"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'large', value1='000020')
        filter4_2=['ALPHA A80','Less than or equal to','000020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.7: Verify filter dialog',filter4_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 05.8: Expect 20 rows - value 000020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Edit - G-104"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'small', value1='G-104')
        filter5_2=['ALPHA Edit','Less than or equal to','G-104']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.9: Verify filter dialog',filter5_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '867of1000records,Page1of16', "Step 05.10: Expect 867 rows - value G-104")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Store Code - R1020"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'small', value1='R1020')
        filter6_2=['ALPHA Store Code','Less than or equal to','R1020']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.11: Verify filter dialog',filter6_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 05.12: Expect 180 rows - value R1020")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Code - V102"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'small', value1='V102')
        filter7_2=['ALPHA Vendor Code','Less than or equal to','V102']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.13: Verify filter dialog',filter7_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '518of1000records,Page1of10', "Step 05.14: Expect 518 rows - value V102")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Name - Thermo Tech, Inc"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'small', value1='ThermoTech, Inc')
        filter8_2=['ALPHA Vendor Name','Less than or equal to','ThermoTech, Inc']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.15: Verify filter dialog',filter8_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '852of1000records,Page1of15', "Step 05.16: Expect 852 rows - value Thermo Tech, Inc")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Code - G100"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'small', value1='G100')
        filter9_2=['ALPHA Product Code','Less than or equal to','G100']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.17: Verify filter dialog',filter9_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '800of1000records,Page1of15', "Step 05.18: Expect 800 rows - value G100")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Less than or equal to')        
        filterselectionobj.create_filter(1, 'Less than or equal to', 'small', value1='French Roast')
        filter10_2=['ALPHA Product Descr.','Less than or equal to','French Roast']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.19: Verify filter dialog',filter10_2)
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '598of1000records,Page1of11', "Step 05.20: Expect 598 rows - value French Roast")
        filterselectionobj.close_filter_dialog()
         
         
        """
        Step 06: For the following ALPHA fields, select Filter, then Between, using a pair of values.
 
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
        """
         
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'large', value1='000005', value2='000010')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '6of1000records,Page1of1', "Step 06.1: Expect 6 rows - value 000005 - 000010")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA ANV - 000100 - 000120"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'large', value1='000100',value2='000120')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '21of1000records,Page1of1', "Step 06.2: Expect 21 rows - values 000100 - 000120")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA TEXT - 000555 - 000570"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'large', value1='000555',value2='000570')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '16of1000records,Page1of1', "Step 06.3: Expect 16 rows - values 000555 - 000570")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA A80 - 000001 - 000002"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'large', value1='000001',value2='000002')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 06.4: Expect 2 rows - values 000001 - 000002")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Edit - G-100 - G104"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'small',value1='G-100', value2='G-104')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '201of1000records,Page1of4', "Step 06.5: Expect 201 row - values G-100 - G-104")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Store Code - R1020 - R1041"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'small', value1='R1020',value2='R1041')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '269of1000records,Page1of5', "Step 06.6: Expect 269 rows - values R1020 - R1041")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Code - V303 - V305"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'small', value1='V303',value2='V305')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '334of1000records,Page1of6', "Step 06.7: Expect 334 rows - values V303 - V305")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Vendor Name - European Specialties, - Evelina Imports,Ltd"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'small', value1='European Specialities,',value2='Evelina Imports, Ltd')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '251of1000records,Page1of5', "Step 06.8: Expect 251 rows - values European Specialties, - Evelina Imports,Ltd")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Code - F103 - F103"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'small', value1='F103',value2='F103')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '148of1000records,Page1of3', "Step 06.9: Expect 331 rows - values F103 - F103")
        filterselectionobj.close_filter_dialog()
         
        """ALPHA Product Descr. - French Roast - Hazelnut"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Between')        
        filterselectionobj.create_filter(1, 'Between', 'small', value1='French Roast',value2='Hazelnut')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '302of1000records,Page1of6', "Step 06.10: Expect 302 rows - values French Roast - Hazelnut")
        filterselectionobj.close_filter_dialog()
        
        """
        STep 07: For the following ALPHA fields, select Filter, then Not Between, using a pair of values.

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
        """
                
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'large', value1='000005', value2='000010')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.move_active_popup('1', '600', '200')
        miscelanousobj.verify_page_summary(0, '994of1000records,Page1of18', "Step 07.1: Expect 994 rows - value 000005 - 000010")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA ANV - 000100 - 000120"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'large', value1='000100',value2='000120')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '979of1000records,Page1of18', "Step 07.2: Expect 979 rows - values 000100 - 000120")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA TEXT - 000555 - 000570"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'large', value1='000555',value2='000570')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '984of1000records,Page1of18', "Step 07.3: Expect 984 rows - values 000555 - 000570")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA A80 - 000001 - 000002"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'large', value1='000001',value2='000002')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '998of1000records,Page1of18', "Step 07.4: Expect 998 rows - values 000001 - 000002")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Edit - G-100 - G104"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'small',value1='G-100', value2='G-104')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '799of1000records,Page1of15', "Step 07.5: Expect 799 row - values G-100 - G-104")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Store Code - R1020 - R1041"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'small', value1='R1020',value2='R1041')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '731of1000records,Page1of13', "Step 07.6: Expect 731 rows - values R1020 - R1041")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Code - V303 - V305"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'small', value1='V303',value2='V305')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '666of1000records,Page1of12', "Step 07.7: Expect 666 rows - values V303 - V305")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Name - European Specialties, - Evelina Imports,Ltd"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'small', value1='European Specialities,',value2='Evelina Imports, Ltd')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '749of1000records,Page1of14', "Step 07.8: Expect 749 rows - values European Specialties, - Evelina Imports,Ltd")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Code - F103 - F103"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'small', value1='F103',value2='F103')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '852of1000records,Page1of15', "Step 07.9: Expect 852 rows - values F103 - F103")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Descr. - French Roast - Hazelnut"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Not Between')        
        filterselectionobj.create_filter(1, 'Not Between', 'small', value1='French Roast',value2='Hazelnut')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '698of1000records,Page1of13', "Step 07.10: Expect 698 rows - values French Roast - Hazelnut")
        filterselectionobj.close_filter_dialog()
        
        """
        Step 08: For the following ALPHA fields, select Filter, then Contains, using the string value: Case does NOT matter.

        ALPHA ORDER - 00001
        ALPHA ANV - 27
        ALPHA TEXT - 000010
        ALPHA A80 - 00000
        ALPHA Edit - b-1
        ALPHA Store Code - 44
        ALPHA Vendor Code - V082
        ALPHA Vendor Name - Bakeries
        ALPHA Product Code - F1
        ALPHA Product Descr. - COFFEE
        """
        
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='00001')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '11of1000records,Page1of1', "Step 08.1: Expect 11 rows - containing '00001' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA ANV - 27"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='27')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 08.2: Expect 20 rows - containing '27' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA TEXT - 000010"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='000010')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 08.3: Expect 1 row - containing '000010' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA A80 - 00000"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='00000')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '9of1000records,Page1of1', "Step 08.4: Expect 9 rows - containing '00000' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Edit - b-1"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='b-1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '335of1000records,Page1of6', "Step 08.5: Expect 335 rows - containing 'b-1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Store Code - 44"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='44')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '165of1000records,Page1of3', "Step 08.6: Expect 165 rows - containing '44' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Code - V082"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='V082')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 08.7: Expect 84 rows - containing 'V082' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='Bakeries')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 08.8: Expect 183 rows - containing 'Bakeries' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Code - F1"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='F1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '331of1000records,Page1of6', "Step 08.9: Expect 331 rows - containing 'F1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Descr. - COFFEE"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Contains')        
        filterselectionobj.create_filter(1, 'Contains',  value1='COFFEE')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '133of1000records,Page1of3', "Step 08.10: Expect 133 rows - containing 'COFFEE' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """
        Step 09: For the following ALPHA fields, select Filter, then Contains, using the Case matching string value:
        ALPHA Edit - b-1
        ALPHA Edit - B-1
        ALPHA Store Code - r1019
        ALPHA Store Code - R1019
        ALPHA Vendor Code - V303
        ALPHA Vendor Name - BAKERIES
        ALPHA Vendor Name - Bakeries
        ALPHA Product Code - f101
        ALPHA Product Code - F101
        ALPHA Product Descr. - cr
        ALPHA Product Descr. - Cr
        """
        
        """ALPHA Edit - b-1"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='b-1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.1: Expect 0 rows - containing 'b-1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Edit - B-1"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='B-1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '335of1000records,Page1of6', "Step 09.2: Expect 335 rows - containing 'B-1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Store Code - r1019    """
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='r1019')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.3: Expect 0 rows - containing 'r1019' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Store Code - R1019    """
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='R1019')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '90of1000records,Page1of2', "Step 09.4: Expect 90 rows - containing 'R1019' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Code - V303"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='V303')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '66of1000records,Page1of2', "Step 09.5: Expect 66 rows - containing 'V303' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Name - BAKERIES"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='BAKERIES')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.6: Expect 0 rows - containing 'BAKERIES' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='Bakeries')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 09.7: Expect 183 rows - containing 'Bakeries' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Code - f101"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='f101')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.8: Expect 0 rows - containing 'f101' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """ALPHA Product Code - F101"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='F101')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 09.9: Expect 84 rows - containing 'F101' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """ALPHA Product Descr. - cr"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='cr')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.10: Expect 0 rows - containing 'cr' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """ALPHA Product Descr. - Cr"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Contains (match case)')        
        filterselectionobj.create_filter(1, 'Contains (match case)',  value1='Cr')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '148of1000records,Page1of3', "Step 09.11: Expect 148 rows - containing 'Cr' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """
        Step 10: For the following ALPHA fields, select Filter, then Omits, using the string value:Case does NOT matter.

        ALPHA ORDER - 00001
        ALPHA ANV - 27
        ALPHA TEXT - 000010
        ALPHA A80 - 00000
        ALPHA Edit - b-1
        ALPHA Store Code - 44
        ALPHA Vendor Code - V082
        ALPHA Vendor Name - Bakeries
        ALPHA Product Code - F1
        ALPHA Product Descr. - COFFEE
        """
        
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='00001')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '989of1000records,Page1of18', "Step 10.1: Expect 989 rows - containing '00001' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA ANV - 27"""
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='27')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '980of1000records,Page1of18', "Step 10.2: Expect 980 rows - containing '27' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA TEXT - 000010"""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='000010')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of1', "Step 10.3: Expect 999 row - containing '000010' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA A80 - 00000"""
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='00000')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '991of1000records,Page1of18', "Step 10.4: Expect 991 rows - containing '00000' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Edit - b-1"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='b-1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '665of1000records,Page1of12', "Step 10.5: Expect 665 rows - containing 'b-1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Store Code - 44"""
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='44')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '835of1000records,Page1of15', "Step 10.6: Expect 835 rows - containing '44' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Code - V082"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='V082')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 10.7: Expect 916 rows - containing 'V082' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='Bakeries')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 10.8: Expect 817 rows - containing 'Bakeries' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Code - F1"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='F1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '669of1000records,Page1of12', "Step 10.9: Expect 669 rows - containing 'F1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Descr. - COFFEE"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Omits')        
        filterselectionobj.create_filter(1, 'Omits',  value1='COFFEE')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '867of1000records,Page1of16', "Step 10.10: Expect 867 rows - containing 'COFFEE' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """
        Step 11: For the following ALPHA fields, select Filter, then Omits, using the Case matching string value:
        Case does not apply to fields with numeric digits only.
        ALPHA Edit - b-1
        ALPHA Edit - B-1
        ALPHA Store Code - r1019
        ALPHA Store Code - R1019
        ALPHA Vendor Code - V303
        ALPHA Vendor Name - BAKERIES
        ALPHA Vendor Name - Bakeries
        ALPHA Product Code - f101
        ALPHA Product Code - F101
        ALPHA Product Descr. - cr
        ALPHA Product Descr. - Cr
        """
        
        """ALPHA Edit - b-1"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='b-1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11.1: Expect 100 rows - containing 'b-1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Edit - B-1"""
        miscelanousobj.select_menu_items('ITableData0', 5, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='B-1')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '665of1000records,Page1of12', "Step 11.2: Expect 665 rows - containing 'B-1' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Store Code - r1019    """
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='r1019')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11.3: Expect 1000 rows - containing 'r1019' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Store Code - R1019    """
        miscelanousobj.select_menu_items('ITableData0', 6, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='R1019')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '910of1000records,Page1of16', "Step 11.4: Expect 910 rows - containing 'R1019' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Code - V303"""
        miscelanousobj.select_menu_items('ITableData0', 7, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='V303')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '934of1000records,Page1of17', "Step 11.5: Expect 934 rows - containing 'V303' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Name - BAKERIES"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='BAKERIES')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11.6: Expect 1000 rows - containing 'BAKERIES' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        miscelanousobj.select_menu_items('ITableData0', 8, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='Bakeries')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 11.7: Expect 817 rows - containing 'Bakeries' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        """ALPHA Product Code - f101"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='f101')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11.8: Expect 0 rows - containing 'f101' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """ALPHA Product Code - F101"""
        miscelanousobj.select_menu_items('ITableData0', 9, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='F101')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 11.9: Expect 916 rows - containing 'F101' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """ALPHA Product Descr. - cr"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='cr')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11.10: Expect 1000 rows - containing 'cr' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
        """ALPHA Product Descr. - Cr"""
        miscelanousobj.select_menu_items('ITableData0', 10, 'Filter','Omits (match case)')        
        filterselectionobj.create_filter(1, 'Omits (match case)',  value1='Cr')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '852of1000records,Page1of15', "Step 11.11: Expect 852 rows - containing 'Cr' anywhere in the field")
        filterselectionobj.close_filter_dialog()
        
        
if __name__ == '__main__':
    unittest.main() 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        