'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226954
TestCase Name = Test placing a hierarchy field as a verb object - This field will not be eligible for drill down since it is not used as a sorting field
'''
import unittest
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon, visualization_metadata, ia_run, active_miscelaneous

class C2226954_TestClass(BaseTestCase):
    
    def test_C2226954(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226954"
        Test_Case_ID = Test_ID+"_"+browser_type
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    
            STEP 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("div[id^='BiDockPanel'] div[class^='x']", 'Sale,Year', 200)
        
        """    
            STEP 02 : Drag Product,Category to SUM bucket as the first field (Product > Product > Product,Category)    
        """
        metaobj.drag_and_drop_from_data_tree_to_query_tree('Product,Category', 1, 'Sum', 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:nth-child(3)", 'MAX.Product,Category', 30, pause_time=5)      
        
        """
            STEP 02.1 : Verify MAX added as prefix to Product,Category  
        """
        metaobj.verify_query_pane_field('Sum', 'MAX.Product,Category', 1, 'Step 02.01 : Verify MAX added as prefix to Product,Category')
        
        """    
            STEP 03 : Right click on "MAX.Product,Category" in Sum and select More > Aggregation Functions > None    
        """
        metaobj.querytree_field_click("MAX.Product,Category", 1, 1,'More', 'Aggregation Functions', '(None)')
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:nth-child(3)", 'Product,Category', 30, pause_time=5)
        
        """
            STEP 03.1 : Verify Aggregation Functions > None applied 
        """
        metaobj.verify_query_pane_field('Sum', 'Product,Category', 1, 'Step 03.01 : Verify Aggregation Functions > None applied')
        
        """    
            STEP 04 : Click Format tab > Autodrill button     
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        utillobj.synchronize_with_number_of_element("div[id='FormatAutoDrill'][class*='checked']", 1, 10, pause_time=3)
         
        """    
            STEP 05 : Click Run and verify The first Product,Category (By) should show with links. The 2nd one (Sum) should not    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe']", 1, 10, pause_time=5)

        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:first-child>td:first-child", 'Sale,Year', 120)
        
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 05.01 : verify Auto Drill, drill down data set")
        iarun.verify_table_cell_property("table[summary= 'Summary']", 5, 2, text='Computers', font_color = 'cerulean_blue_2', msg='Step 05.02 : Verify first Product,Category (By) should show with links: ')
        table_css="table[summary= 'Summary'] > tbody > tr:nth-child(5) > td:nth-child(2) > a"
        cell_obj=self.driver.find_element_by_css_selector(table_css)
        actual_decoration=True if 'underline' in cell_obj.value_of_css_property("text-decoration") else False
        utillobj.asequal(True, actual_decoration, "Step 05.03 : Verify first Product,Category (By) should show with links:. Verification of Cell is underlined.")
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 3, text='Accessories', font_color = 'gray8', msg='Step 05.04 : Verify The 2nd one (Sum) should not')
        utillobj.switch_to_default_content(1)
        
        """    
            STEP 06 : Click on HTML output format in status bar and select Active format    
        """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        utillobj.synchronize_with_visble_text("#sbpOutputFormat .bi-button-label", 'ActiveReport', 20)
        
        """    
            STEP 07 : Click Run and verify The first Product,Category (By) should show with links. The 2nd one (Sum) should not    
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe']", 1, 10, pause_time=8)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:first-child>td:first-child", 'Sale,Year', 120)
        
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 07.01 : Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Product Category', 'Quantity Sold', 'Revenue', 'Product Category', 'Quantity Sold', 'Revenue', 'Product Category', 'Quantity Sold', 'Revenue', 'Product Category', 'Quantity Sold', 'Revenue', 'Product Category', 'Quantity Sold', 'Revenue', 'Product Category', 'Quantity Sold', 'Revenue', 'Product Category', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07.02 : Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', 'Step 07.03 : Verify the report data ')
        miscelanousobj.verify_cell_property('ITableData0', 2,1, 'Computers', "Step 07.04 :", text_color='cerulean_blue_2')
        miscelanousobj.verify_cell_property('ITableData0', 5,2, 'Televisions', "Step 07.05 :", text_color='gray8')
        utillobj.switch_to_default_content(pause=2)
    
        """    
            STEP 08 : Click IA > Save As> Type C2226954 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
            STEP 09 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226954.fex&tool=report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("div[id^='BiDockPanel'] div[class^='x']", 'Sale,Year', 200)
        
        """    
            STEP 10 : Click format tab and see Autodrill button should be active    
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("div[id='FormatAutoDrill'][class*='checked']", 1, 20, pause_time=3)
        
        """
            STEP 10.1 : Verify that Auto Drill is still selected.
        """
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 10.01 : Verify that Auto Drill is still selected")
         
        """    
            STEP 11 : Click Run    
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe']", 1, 10, pause_time=8)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:first-child>td:first-child", 'Sale,Year', 120)
        
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 11.01 : Verify the Report Records')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', 'Step 11.02 : Verify the report data ')
        miscelanousobj.verify_cell_property('ITableData0', 2,1, 'Computers', "Step 11.03 :", text_color='cerulean_blue_2')
        miscelanousobj.verify_cell_property('ITableData0', 5,2, 'Televisions', "Step 11.04 :", text_color='gray8')
        
        utillobj.switch_to_default_content(pause=2)
        utillobj.infoassist_api_logout()
        
        """    
            STEP 12 : Run from BIP using API
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9970&BIP_item=C2226954.fex    
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S9970", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("iframe[src*='contentDrill']", 1, 120, pause_time=8)
        
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:first-child>td:first-child", 'Sale,Year', 120)
        
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 12.01 : Verify the Report Records')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', 'Step 12.02 : Verify the report data ')
        miscelanousobj.verify_cell_property('ITableData0', 2,1, 'Computers', "Step 12.03 :", text_color='cerulean_blue_2')
        miscelanousobj.verify_cell_property('ITableData0', 5,2, 'Televisions', "Step 12.04 :", text_color='gray8')
        utillobj.switch_to_default_content(pause=2)
        
        """    
            STEP 13 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    