'''
Created on May 21, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/3023977
TestCase Name = Verify Define with Date field type and period separator
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, define_compute, ia_run, metadata
from common.lib.basetestcase import BaseTestCase

class C3023977_TestClass(BaseTestCase):

    def test_C3023977(self):
        
        Test_Case_ID = "C3023977"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        defcomp_obj=define_compute.Define_Compute(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        metadataobj=metadata.MetaData(self.driver)
        
        """        
        Step 01: Launch Report with wf_retail_lite:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10863
        """
        utillobj.invoke_infoassist_api_login('report','baseapp/wf_retail_lite','P292_S10863/G433144', 'mrid', 'mrpass')
        time.sleep(2)
        
        """        
        Step 02: Select Data Tab > Define
        """
        defcomp_obj.invoke_define_compute_dialog('define')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """        
        Step 03: Add "Sale,Date" to expression area
        """
        defcomp_obj.select_define_compute_field('Sale,Date', 1)
        time.sleep(2)
        
        """        
        Step 04: Click on "Format" button > Select Field Type "Date"
        """
        format_css=driver.find_element_by_css_selector('#btnFormat')
        time.sleep(2)
        utillobj.default_left_click(object_locator=format_css)
        parent_css="#format-types-list"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        menu_items=driver.find_elements_by_css_selector("#format-types-list div[id^='BiListItem']")
        actual_popup_list=[el.text.strip() for el in menu_items]
        date=menu_items[actual_popup_list.index('Date')]
        utillobj.default_left_click(object_locator=date, click_option=0)
        time.sleep(2)
        
        """        
        Step 05: Select "MDYY" from Display Options
        """
        parent_css="#dateFormatList"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        menu_items=driver.find_elements_by_css_selector("#dateFormatList div[id^='BiListItem']")
        actual_popup_list=[el.text.strip() for el in menu_items]
        mdyy = menu_items[actual_popup_list.index('MDYY')]
        utillobj.default_left_click(object_locator=mdyy, click_option=0)
        time.sleep(2)
        
        """        
        Step 06: Click on the Separators dropdown > Select .(period) > Click OK
        """
        combo_btn_elem=driver.find_element_by_css_selector("#dateSeparator div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        combo_css=('div[id*="BiList"] div[class^="bi-list-item"]')
        utillobj.select_or_verify_bipop_menu('. (period)', custom_css=combo_css)
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgOk"]')
        utillobj.default_left_click(object_locator=close_elem)
        time.sleep(2)
        
        """        
        Step 07: Verify format written is MDYY.
        """
        format_text=driver.find_element_by_css_selector("input[id^='fformat']").get_attribute('value')
        utillobj.asequal(format_text, 'MDYY.', 'Step 07: Verify format written is MDYY.')
        
        """        
        Step 08: Click OK
        """
        defcomp_obj.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """        
        Step 09: Add fields "Sale,Date", "Product,Category", "Quantity,Sold"
        """
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(4)
        metaobj.datatree_field_click("Dimensions->Sales_Related->Transaction Date, Simple->Sale,Day->Attributes->Define_1", 2, 1)
        time.sleep(2)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(2)
        parent_css="#queryTreeWindow tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        time.sleep(2)
        parent_css="#queryTreeWindow tr:nth-child(3) td"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """        
        Step 10: Verify Query Pane and Live Preview with period as the date separator for the Define_1 column
        """
        time.sleep(6)
        metaobj.verify_query_pane_field('Sum', "Quantity,Sold", 1, "Step 10.1")
        metaobj.verify_query_pane_field('By', "Define_1", 1, "Step 10.2")
        metaobj.verify_query_pane_field('Define_1', "Product,Category", 1, "Step 10.3")
        
        coln_list = ['Define_1', 'ProductCategory', 'QuantitySold']
        resobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 10:04: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 5, 3, Test_Case_ID+"_Ds01.xlsx", no_of_cells=6)
        ia_resultobj.verify_report_data_set('TableChart_1', 5, 3, Test_Case_ID+"_Ds01.xlsx", "Step 10.5: Verify live preview data", no_of_cells=6)
        
        """        
        Step 11: Run
        """
        time.sleep(4)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        
        """        
        Step 12: Verify output displays period as the date separator
        """
#         ia_runobj.create_table_data_set("table[summary='Summary']",Test_Case_ID+'_Ds02.xlsx',desired_no_of_rows=10) 
        ia_runobj.verify_table_data_set("table[summary='Summary']",Test_Case_ID+"_Ds02.xlsx", 'Step 12: Verify the output report is displayed.',desired_no_of_rows=10)  
        
        """        
        Step 13: Select Save > Save as "C3023977" > Save
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('infomini_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """        
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """        
        Step 15: Restore the saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10863/C3023977.fex&tool=Report
        """
        utillobj.infoassist_api_edit_(Test_Case_ID, 'report', 'P292_S10863/G433144',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """        
        Step 16: Verify Query pane and Live Preview
        """
        metaobj.verify_query_pane_field('Sum', "Quantity,Sold", 1, "Step 16.1")
        metaobj.verify_query_pane_field('By', "Define_1", 1, "Step 16.2")
        metaobj.verify_query_pane_field('Define_1', "Product,Category", 1, "Step 16.3")
        
        coln_list = ['Define_1', 'ProductCategory', 'QuantitySold']
        resobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 16:04: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 5, 3, Test_Case_ID+"_Ds01.xlsx", "Step 16.5: Verify live preview data", no_of_cells=6)
        
        """        
        Step 17: Right-click Define_1 in the Data pane > Edit...
        """
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(4)
        metaobj.datatree_field_click('Dimensions->Sales_Related->Transaction Date, Simple->Sale,Day->Attributes->Define_1', 1, 1, 'Edit...')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """        
        Step 18: Verify Format > Click on the Format button > Verify selections
        Step 19: Click Cancel > Cancel
        """
        format_text=driver.find_element_by_css_selector("input[id^='fformat']").get_attribute('value')
        utillobj.asequal(format_text, 'MDYY.', 'Step 18.1: Verify format written is MDYY.')
        
        format_css=driver.find_element_by_css_selector('#btnFormat')
        time.sleep(2)
        utillobj.default_left_click(object_locator=format_css)
        parent_css="#format-types-list"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        
        field_type_text=driver.find_element_by_css_selector("#format-types-list div[id^='BiListItem'][class*='selected']").text.strip()
        utillobj.asequal(field_type_text, 'Date', 'Step 18.2: Verify format field type.')
        
        display_opt=driver.find_element_by_css_selector("#dateFormatList div[id^='BiListItem'][class*='selected']").text.strip()
        utillobj.asequal(display_opt, 'MDYY', 'Step 18.3: Verify format written is MDYY.')
        
        combo_btn_elem=driver.find_element_by_css_selector("#dateSeparator div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        parent_css="div[id^='BiPopup'][style*='inherit']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        seperator_txt=driver.find_element_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id*='BiList'] div[class*='selected']").text.strip()
        utillobj.asequal(seperator_txt, '. (period)', 'Step 18.4: Verify seperator type.')
        
        combo_btn_elem=driver.find_element_by_css_selector("#dateSeparator div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgCancel"]')
        utillobj.default_left_click(object_locator=close_elem)
        time.sleep(2)
        close_button_elem=driver.find_element_by_css_selector('div[id="fldCreatorCancelBtn"]')
        utillobj.default_left_click(object_locator=close_button_elem)
        
        """        
        Step 20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()