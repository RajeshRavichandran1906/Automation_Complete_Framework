'''
Created on May 21, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/3023975
TestCase Name = Verify Compute with Date field type and hyphen separator
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, define_compute, ia_run
from common.lib.basetestcase import BaseTestCase

class C3023975_TestClass(BaseTestCase):

    def test_C3023975(self):
        
        Test_Case_ID = "C3023975"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        defcomp_obj=define_compute.Define_Compute(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """        
        Step 01: Launch Report with wf_retail_lite:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/empdata&item=IBFS:/WFC/Repository/S10863
        """
        utillobj.invoke_infoassist_api_login('report','ibisamp/empdata','P292_S10863/G433143', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 65)
        
        """        
        Step 02: Select Data Tab > Compute
        """
        defcomp_obj.invoke_define_compute_dialog('compute')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """        
        Step 03: Add HIREDATE to expression area
        """
        defcomp_obj.select_define_compute_field('HIREDATE', 1)
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
        print(actual_popup_list)
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
        print(actual_popup_list)
        mdyy = menu_items[actual_popup_list.index('MDYY')]
        utillobj.default_left_click(object_locator=mdyy, click_option=0)
        time.sleep(2)
        
        """        
        Step 06: Click on the Separators dropdown > Select -(hyphen) > Click OK
        """
        combo_btn_elem=driver.find_element_by_css_selector("#dateSeparator div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        combo_css=('div[id*="BiList"] div[class^="bi-list-item"]')
        utillobj.select_or_verify_bipop_menu('- (hyphen)', custom_css=combo_css)
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgOk"]')
        utillobj.default_left_click(object_locator=close_elem)
        time.sleep(2)
        
        """        
        Step 07: Verify format written is MDYY-
        """
        format_text=driver.find_element_by_css_selector("input[id^='fformat']").get_attribute('value')
        print(format_text)
        utillobj.asequal(format_text, 'MDYY-', 'Step 07: Verify format written is MDYY.')
        defcomp_obj.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """        
        Step 08: Add field LASTNAME
        """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(6)
        
        """        
        Step 09: Verify Query pane and Live Preview with hyphen as the date separator for the Compute_1 column
        """
        metaobj.verify_query_pane_field('Sum', "Compute_1", 1, "Step 09.1")
        metaobj.verify_query_pane_field('By', "LASTNAME", 1, "Step 09.2")
        
        coln_list = ['LASTNAME', 'Compute_1']
        resobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 09:03: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds01.xlsx", "Step 09.4: Verify live preview data")
        
        """        
        Step 10: Run
        """
        time.sleep(4)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        
        """        
        Step 11: Verify output show hyphen as the date separator
        """
#         ia_runobj.create_table_data_set("table[summary='Summary']",Test_Case_ID+'_Ds02.xlsx',desired_no_of_rows=10) 
        ia_runobj.verify_table_data_set("table[summary='Summary']",Test_Case_ID+"_Ds02.xlsx", 'Step 11: Verify the output report is displayed.',desired_no_of_rows=10)  
        
        """        
        Step 12: Select Save > Save as "C3023975" > Save
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('infomini_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """        
        Step 13: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """        
        Step 14: Restore the saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10863/C3023975.fex&tool=Report
        """
        utillobj.infoassist_api_edit_(Test_Case_ID, 'report', 'P292_S10863/G433143',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        """        
        Step 15: Verify Query pane and Live Preview
        """
        metaobj.verify_query_pane_field('Sum', "Compute_1", 1, "Step 15.1")
        metaobj.verify_query_pane_field('By', "LASTNAME", 1, "Step 15.2")
        
        coln_list = ['LASTNAME', 'Compute_1']
        resobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 15.3: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds01.xlsx", "Step 15.4: Verify live preview data")
        
        """        
        Step 16: Right-click Compute_1 > Edit Compute
        """
        metaobj.querytree_field_click('Compute_1', 1, 1, 'Edit Compute')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """        
        Step 17: Verify Format is MDYY- > Click on Format button > Verify dialog
        Step 18: Click Cancel > Cancel
        """
        format_text=driver.find_element_by_css_selector("input[id^='fformat']").get_attribute('value')
        print(format_text)
        utillobj.asequal(format_text, 'MDYY-', 'Step 17.1: Verify format written is MDYY.')
        
        format_css=driver.find_element_by_css_selector('#btnFormat')
        time.sleep(2)
        utillobj.default_left_click(object_locator=format_css)
        parent_css="#format-types-list"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        
        field_type_text=driver.find_element_by_css_selector("#format-types-list div[id^='BiListItem'][class*='selected']").text.strip()
        print(field_type_text)
        utillobj.asequal(field_type_text, 'Date', 'Step 17.2: Verify format field type.')
        
        display_opt=driver.find_element_by_css_selector("#dateFormatList div[id^='BiListItem'][class*='selected']").text.strip()
        print(display_opt)
        utillobj.asequal(display_opt, 'MDYY', 'Step 17.3: Verify format written is MDYY.')
        
        combo_btn_elem=driver.find_element_by_css_selector("#dateSeparator div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        parent_css="div[id^='BiPopup'][style*='inherit']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        seperator_txt=driver.find_element_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id*='BiList'] div[class*='selected']").text.strip()
        print(seperator_txt)
        utillobj.asequal(seperator_txt, '- (hyphen)', 'Step 17.4: Verify seperator type.')
        
        combo_btn_elem=driver.find_element_by_css_selector("#dateSeparator div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgCancel"]')
        utillobj.default_left_click(object_locator=close_elem)
        time.sleep(2)
        close_button_elem=driver.find_element_by_css_selector('div[id="fldCreatorCancelBtn"]')
        utillobj.default_left_click(object_locator=close_button_elem)
        
        """        
        Step 19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()