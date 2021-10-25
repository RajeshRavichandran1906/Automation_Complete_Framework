'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234766
'''
import unittest
import time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_resultarea, active_miscelaneous, ia_run, metadata
from common.lib import utillity
from common.wftools.report import Report
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class C2234766_TestClass(BaseTestCase):

    def test_C2234766(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2234766'
        
        """ TESTCASE OBJECTS """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        report_obj = Report(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """    1. Launch IA Document mode with wf_retail_lite: http://machine:port/ibi_apps/ia?tool=Document&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032    """
        utillobj.infoassist_api_login('document','baseapp/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=10, string_value='Document')  
        time.sleep(1)
        
        """    2. Select Insert Tab > Click "Report"    """
        ribbonobj.select_ribbon_item("Insert", "Report")
        
        """    3. Right-click "Sum" in the Query pane > New Parameter    """
        metaobj.querytree_field_click('Sum',1,1,'New Parameter')
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Parameter1')
        
        """    4. Drag fields "Revenue", "Cost of Goods", and "Gross Profit" into the "Sum" bucket under "Parameter1" container    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit',1,'Parameter1',0)
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Gross Profit')
        metaobj.drag_drop_data_tree_items_to_query_tree('Cost of Goods',1,'Parameter1',0)
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Cost of Goods')
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue',1,'Parameter1',0)
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Revenue')
        time.sleep(2)
        
        """    5. Right-click "By" in the Query pane > New Parameter    """
        metaobj.querytree_field_click('By',1,1,'New Parameter')
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Parameter2')
        
        """    6. Multi-select "Product,Category" and "Product,Subcategory" in the Data pane > Drag these fields into the "By" bucket under "Parameter2" container    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Subcategory',1,'Parameter2',0)
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Product,Subcategory')
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category',1,'Parameter2',0)
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Product,Category')
        time.sleep(2)
        
        """    7. Right-click "Across" in the Query pane > New Parameter    """
        metaobj.querytree_field_click('Across',1,1,'New Parameter')
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Parameter3')
    
        
        """    8. Drag fields "Store,Business,Region" and "Store,Country" into the "Across" bucket under "Parameter3" container    """
        metadataobj.collapse_data_field_section('Measure Groups')
        time.sleep(3)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Country',1,'Parameter3',0)
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Store,Country')
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Business,Region',1,'Parameter3',0)
        resultobj.wait_for_property("#queryTreeColumn", 1,40,string_value='Store,Business,Region')
        
        """    9. Verify Query pane and Document canvas    """
        expected_fields = ['Report1 (wf_retail_lite)', 'Sum', 'Parameter1', 'Revenue', 'Cost of Goods', 'Gross Profit', 'By', 'Parameter2', 'Product,Category', 'Product,Subcategory', 'Across', 'Parameter3', 'Store,Business,Region', 'Store,Country', 'Coordinated']
        report_obj.verify_all_fields_in_query_pane(expected_fields, msg='Step 09.01 : Verify query pane')
        #iaresult.create_across_report_data_set('TableChart_1',3,5,7,5,Test_Case_ID+'_Ds_01.xlsx')         
        iaresult.verify_across_report_data_set('TableChart_1',3,5,7,5,Test_Case_ID+'_Ds_01.xlsx','Step 09.02 : Verify preview report')
            
        """    10. Click "Save" > save as "C2234766" > Click Save    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """    11. Run    """
        """    12. Verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#promptPanel label[class='autop-title']",1,20,string_value='Filter Values')
        actual_field1=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter1']").text.strip().replace('\n',' ')
        actual_field2=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter2']").text.strip().replace('\n',' ')
        actual_field3=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter3']").text.strip().replace('\n',' ')
        utillobj.asin('Parameter1 Revenue',actual_field1,'Step 12.01 : Verify default amper value for Paramater1')
        utillobj.asin('Parameter2 Product Category',actual_field2,'Step 12.02 : Verify default amper value for Paramater2')
        utillobj.asin('Parameter3 Store Business Region',actual_field3,'Step 12.03 : Verify default amper value for Paramater3')
        
        """    13. Click on the "Revenue" dropdown > Select "Cost of Goods"    """
        iarun.select_amper_value('Parameter1',['Cost of Goods'],False,verify_small_value_list=['Revenue', 'Cost of Goods', 'Gross Profit'])
        
        """    14. Click on the "Store Business Region " dropdown > Select "Store Country"    """
        iarun.select_amper_value('Parameter3',['Store Country'],False,verify_small_value_list=['Store Business Region', 'Store Country'])
        
        """    15. Click the Submit button    """
        iarun.select_amper_menu('Run')
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        
        """    16. Verify output    """
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', "Step 16.01: Verify the Run Report Heading")
        across_list=['Store,Country', 'Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        across=self.driver.find_elements_by_css_selector("#ITableData0 tr>td[id^='THEAD']")
        actual_list=[re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in across]]
        utillobj.asequal(across_list, actual_list, "Step 16.02: Verify the Run Report Across Heading")
        column_list=['Product Category', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US', 'COGS_US']
        miscelanousobj.verify_column_heading('ITableData0', column_list, "Step 16.03: Verify the Run Report column heading")
        #utillobj.create_data_set('ITableData0','I0r', Test_Case_ID +'_Ds_02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds_02.xlsx', "Step 16.04: Verify entire Data set in Run Report on Page 1") 
        utillobj.switch_to_default_content()
        time.sleep(2)
        
        """    17. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    18. Reopen FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2234766.fex&tool=document    """
        oFolder=utillobj.parseinitfile('suite_id')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        time.sleep(2)
        preview_report=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.default_left_click(object_locator=preview_report)
        time.sleep(2)
        
        """    19. Verify Query pane and Document canvas    """
        expected_fields = ['Report1 (wf_retail_lite)', 'Sum', 'Parameter1', 'Revenue', 'Cost of Goods', 'Gross Profit', 'By', 'Parameter2', 'Product,Category', 'Product,Subcategory', 'Across', 'Parameter3', 'Store,Business,Region', 'Store,Country', 'Coordinated']
        report_obj.verify_all_fields_in_query_pane(expected_fields, msg='Step 19.01 : Verify query pane')
        iaresult.verify_across_report_data_set('TableChart_1',3,5,7,5,Test_Case_ID+'_Ds_01.xlsx','Step 19.02 : Verify preview report')
         
        """    20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()