'''
Created on Jan 22, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251739
Test_Case Name : AHTML:CMPD:Filter:No Nest relat w/MERGE=AUTO & MultiTab(116685)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_run, active_miscelaneous, active_filter_selection
from common.lib import utillity

class C2251739_TestClass(BaseTestCase):

    def test_C2251739(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251739'
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter=active_filter_selection.Active_Filter_Selection(self.driver)
        
        """
            Step 01 : Execute the attached repro - 116685.fex
        """
        utillobj.active_run_fex_api_login('116685.fex', 'S10071_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0>tt", 'COUNTRY', 60)
        
        """
            Step 01.1 : Expect to see the following AHTML Document.
        """
        iarun.verify_active_document_page_layout_menu("table[id='iLayTB$']", ['Layouts', 'Page layout 1', 'Page layout 2', 'COUNTRY', 'ENGLAND\nFRANCE\nITALY\nJAPAN\nW GERMANY', ''], 'Step 01.1 : Verify Page layout menu')
        utillobj.verify_dropdown_value("select[name='mergeval']", ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN' ,'W GERMANY'], 'Step 01.2 : Verify country dropdown box values', 'ENGLAND', 'Step 01.3 : Verify ENGLAND is selected as default in country dropdown box')
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX1", ['[All]', 'JAGUAR', 'JENSEN', 'TRIUMPH'], 'Step 01.4 : Verify car values dropdown box values', '[All]', 'Step 01.5 : Verify [All] is selected as default in car dropdown box')
        iarun.verify_active_dashboard_prompts('drop_down','#radiobutton_dRADIO1', ['[All]', '0', '12000'], "Step 01.6 : Verify radio button value and ['All'] is selected as default", '[All]')
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_01.xlsx', 'Step 01.7 : Verify Report data')
        active.verify_page_summary(0, '4of18records,Page1of1', 'Step 01.8 : Verify page summary')
        
        """
            Step 02 : Select Japan from country dropdown
        """
        utillobj.select_dropdown("select[name='mergeval']", 'visible_text', 'JAPAN')
        
        """
            Step 02.1 : Verify that check box and report get filtered based on value "Japan" in page layout 1 and page layout 2, Page layout 1
        """
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX1", ['[All]', 'DATSUN', 'TOYOTA'], 'Step 02.1 : Verify car values dropdown box values in page layou 1', '[All]', 'Step 01.2 : Verify [All] is selected as default in car dropdown box in page layou 1')
        iarun.verify_active_dashboard_prompts('drop_down', '#radiobutton_dRADIO1', ['[All]', '35030', '43000'], "Step 02.3 : Verify radio button value and ['All'] is selected as default in page layout 1", '[All]')
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_02.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_02.xlsx', 'Step 02.4 : Verify Report data in page layout 1')
        active.verify_page_summary(0, '2of18records,Page1of1', 'Step 02.5 : Verify page summary in page layout 1')
        
        page2=self.driver.find_element_by_css_selector("table[id='iLayTB$'] div[id='iLay$2']")
        utillobj.default_click(page2, 0)
        time.sleep(3)
        
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX2", ['[All]', '35030', '43000'], 'Step 02.7 : Verify  dropdown box values in page layou 2', '[All]', 'Step 02.6 : Verify [All] is selected as default in dropdown box in page layou 2')
        iarun.verify_active_dashboard_prompts('text', '#radiobutton_dRADIO2', ['[All]', 'TOYOTA', 'DATSUN'], "Step 02.8 : Verify radio button value and ['All'] is selected as default in page layout 2", '[All]')
        #iarun.create_table_data_set("#ITableData1", Test_Case_ID+'_Dataset_03.xlsx')
        iarun.verify_table_data_set("#ITableData1", Test_Case_ID+'_Dataset_03.xlsx', 'Step 02.9 : Verify Report data in page layout 2')
        active.verify_page_summary(1, '2of18records,Page1of1', 'Step 02.10 : Verify page summary in page layout 2')
        
        """
            Step 03 : Select global filter icon. Select Add condition for field Sales.From the value drop down, select 35030.
        """
        filter_icon=self.driver.find_element_by_css_selector("table[id='iLayTB$'] td[id='iLayM4$']>div[class='arDashboardBarGlobalButton']")
        utillobj.default_click(filter_icon, 0)
        time.sleep(3)
        active.verify_popup_appears('wall1', 'Global Filter', 'Step 03.1 : Verify Expect to see the following Global Filter panel.')
        active_filter.add_global_condition_field('SALES', "0_globalop_x__0")
        active_filter.select_filter_values('0', 'small', "ftp1_1_0", '35030', 1, 0, temp_val=0)
        
        """
            Step 04 : Click the Filter button.
        """
        active_filter.filter_button_click('Filter')
        
        """
            Step 04.1 : Verify report gets filtered based on global filter in both page layout 1 and page layout 2
        """
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX2", ['[All]', '35030', '43000'], 'Step 04.2 : Verify  dropdown box values in page layou 2', '[All]', 'Step 04.1 : Verify [All] is selected as default in dropdown box in page layou 2')
        iarun.verify_active_dashboard_prompts('text', '#radiobutton_dRADIO2', ['[All]', 'TOYOTA', 'DATSUN'], "Step 04.3 : Verify radio button value and ['All'] is selected as default in page layout 2", '[All]')
        #iarun.create_table_data_set("#ITableData1", Test_Case_ID+'_Dataset_04.xlsx')
        iarun.verify_table_data_set("#ITableData1", Test_Case_ID+'_Dataset_04.xlsx', 'Step 04.4 : Verify Report data in page layout 2')
        active.verify_page_summary(1 ,'1of18records,Page1of1', 'Step 04.5 : Verify page summary in page layout 2')
        
        page1=self.driver.find_element_by_css_selector("table[id='iLayTB$'] div[id='iLay$1']")
        utillobj.default_click(page1, 0)
        time.sleep(3)
        
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX1", ['[All]', 'DATSUN', 'TOYOTA'], 'Step 04.7 : Verify car values dropdown box values in page layou 1', '[All]', 'Step 04.6 : Verify [All] is selected as default in car dropdown box in page layou 1')
        iarun.verify_active_dashboard_prompts('drop_down', '#radiobutton_dRADIO1', ['[All]', '35030', '43000'], "Step 04.8 : Verify radio button value and ['All'] is selected as default in page layout 1", '[All]')
        #iarun.create_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_05.xlsx')
        iarun.verify_table_data_set("#ITableData0", Test_Case_ID+'_Dataset_05.xlsx', 'Step 04.9 : Verify Report data')
        active.verify_page_summary(0, '1of18records,Page1of1', 'Step 04.10 : Verify page summary')
        
if __name__ == '__main__':
    unittest.main()