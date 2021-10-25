'''
Created on Jan 17, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2251624
TestCase Name = Active Document: Chaining Does Not Work.
'''
import unittest, time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity

class C2251624_TestClass(BaseTestCase):

    def test_C2251624(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        fex_name='Chained_Filters.fex'
        
        """    1. Execute the attached repro - Chained_Filters.fex    """
            
        utillobj.active_run_fex_api_login(fex_name, 'S10071_2', 'mrid', 'mrpass')
        
        def select_listbox_item(listboxcss, list_item, **kwargs):
            menu_items=self.driver.find_elements_by_css_selector(listboxcss +" table tr td div")
            actual_popup_list=[el.text.strip() for el in menu_items]
            if 'verify' in kwargs:
                actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
                print ("im herefsdfsdfsdf")
                print(actual_popup_list)
                print ("im here")
                utillobj.as_List_equal(self,kwargs['expected_listbox_list'], actual_popup_list, kwargs['msg'])
        
            menu_items[actual_popup_list.index(list_item)].click()
            time.sleep(1)
            
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Region', 85)    
        
        """    1.1. Expect to see the following Document, with two sets of Drop down, ComboBox & Active reports.    """
            
        miscelanousobj.verify_page_summary('0','11of11records,Page1of1','Step 01.1a : Verify page summary for report 1')
        miscelanousobj.verify_page_summary('1','11of11records,Page1of1','Step 01.1b : Verify page summary for report 2')
#         iarun.create_table_data_set('#ITableData0','C2251624_Ds01a.xlsx')
#         iarun.create_table_data_set('#ITableData1','C2251624_Ds01b.xlsx')
        iarun.verify_table_data_set('#ITableData0','C2251624_Ds01a.xlsx','Step 01.1c : Verify report 1 data')
        iarun.verify_table_data_set('#ITableData1','C2251624_Ds01b.xlsx','Step 01.1d : Verify report 2 data')
        
        utillobj.verify_object_visible("#combobox_dPROMPT_1", True, 'Step 01.1e: Verify Combobox1 present')
        utillobj.verify_object_visible("#combobox_dPROMPT_3", True, 'Step 01.1f: Verify Combobox2 present')
        utillobj.verify_object_visible("#list_dPROMPT_2", True, 'Step 01.1g: Verify listbox1 present')
        utillobj.verify_object_visible("#list_dPROMPT_4", True, 'Step 01.1h: Verify listbox2 present')
        
        '''    '2. From the left Drop down, select Southeast.    '''
        '''    '2.1. Expect to see only Southeast states and data.    '''
        
        utillobj.select_dropdown("#combobox_dsPROMPT_1","visible_text","Southeast")
        
        
        #iarun.create_table_data_set('#ITableData0','C2251624_Ds02.xlsx')
        iarun.verify_table_data_set('#ITableData0','C2251624_Ds02.xlsx','Step 02.1a : Verify report 1 data with only Southeast')
        iarun.verify_table_data_set('#ITableData1','C2251624_Ds02.xlsx','Step 02.1b : Verify report 2 data with only Southeast')
        
        miscelanousobj.verify_page_summary('0','3of11records,Page1of1','Step 02.1c : Verify page summary for report 1')
        miscelanousobj.verify_page_summary('1','3of11records,Page1of1','Step 02.1d : Verify page summary for report 2')
        
        '''    '3. From the left ComboBox, select NY.    '''
        '''    '3.1. Expect to see only NY data on both reports.    '''
        
        select_listbox_item("#list_dPROMPT_2", "NY")
        
        #iarun.create_table_data_set('#ITableData0','C2251624_Ds03.xlsx')
        iarun.verify_table_data_set('#ITableData0','C2251624_Ds03.xlsx','Step 03.1a : Verify report 1 data with only NY')
        iarun.verify_table_data_set('#ITableData1','C2251624_Ds03.xlsx','Step 03.1b : Verify report 2 data with only NY')
        
        miscelanousobj.verify_page_summary('0','1of11records,Page1of1','Step 03.1c : Verify page summary for report 1')
        miscelanousobj.verify_page_summary('1','1of11records,Page1of1','Step 03.1d : Verify page summary for report 2')
        
        '''    4. From the right Drop down, select Northeast.    '''
        '''    4.1. Expect to see only Northeast states and data.    '''
        
        utillobj.select_dropdown("#combobox_dsPROMPT_3","visible_text","Northeast")
        
        #iarun.create_table_data_set('#ITableData0','C2251624_Ds04.xlsx')
        iarun.verify_table_data_set('#ITableData0','C2251624_Ds04.xlsx','Step 04.1a : Verify report 1 data with only Northeast')
        iarun.verify_table_data_set('#ITableData1','C2251624_Ds04.xlsx','Step 04.1b : Verify report 2 data with only Northeast')
        
        miscelanousobj.verify_page_summary('0','3of11records,Page1of1','Step 04.1c : Verify page summary for report 1')
        miscelanousobj.verify_page_summary('1','3of11records,Page1of1','Step 04.1d : Verify page summary for report 2')
        
        '''    5. From the right ComboBox, select TX.    '''
        '''    5.1. Expect to see only NY data on both reports.    '''
        
        select_listbox_item("#list_dPROMPT_4", "TX")
        
        #iarun.create_table_data_set('#ITableData0','C2251624_Ds05.xlsx')
        iarun.verify_table_data_set('#ITableData0','C2251624_Ds05.xlsx','Step 05.1a : Verify report 1 data with only TX')
        iarun.verify_table_data_set('#ITableData1','C2251624_Ds05.xlsx','Step 05.1b : Verify report 2 data with only TX')
        
        miscelanousobj.verify_page_summary('0','1of11records,Page1of1','Step 05.1c : Verify page summary for report 1')
        miscelanousobj.verify_page_summary('1','1of11records,Page1of1','Step 05.1d : Verify page summary for report 2')
        time.sleep(3)
        
        
        
if __name__=='__main__' :
    unittest.main()
        