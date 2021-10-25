'''
Created on May 18, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2967558
TestCase Name = Verify download data with output format CSV 
'''

import unittest
import time
from common.lib import utillity
from common.pages import ia_resultarea, ia_ribbon, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C2967558_TestClass(BaseTestCase):

    def test_C2967558(self):
        
        Test_Case_ID = "C2967558"
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        report = Report(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        live_preview_css = "#TableChart_1"
        query_css = "#queryBoxColumn"
        cancel_css = "#IbfsOpenFileDialog7_btnCancel"
        
        """ 
        Step 01: Launch Report with car:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/S10863
        """
        utillobj.invoke_infoassist_api_login('Report','ibisamp/car','P292_S10863/G427910', 'mrid', 'mrpass')
        report.wait_for_visible_text(live_preview_css, "Drag and drop") 
        
        """    
        Step 02: Add fields: country, car, model, sales    
        """
        report.double_click_on_datetree_item("COUNTRY", 1)
        report.wait_for_visible_text(query_css, "COUNTRY")
        
        report.double_click_on_datetree_item("CAR", 1)
        report.wait_for_visible_text(query_css, "CAR")
        
        report.double_click_on_datetree_item("MODEL", 1)
        report.wait_for_visible_text(query_css, "MODEL")
        
        report.double_click_on_datetree_item("SALES", 1)
        report.wait_for_visible_text(query_css, "SALES")
        
        """    
        Step 03: Home Tab > Select output formats button > Excel (xlsx) > "Excel (csv)"
        """
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel (xlsx)->Excel (csv)')
        time.sleep(4)
        
        """    
        Step 04: Verify Home Tab ribbon and Status bar reflect the selected output format
        """
        utillobj.verify_element_text("#HomeFormatType>div[id^='BiLabel']",'Excel (csv)','Step 04: Verify Output format is set to "Excel (csv)')
        
        """
        Step 05: Select View Source in the toolbar
        Step 06: Verify syntax generated for CSV format > Close source window
        ON TABLE PCHOLD FORMAT COMT
        """
        expected_syntax_list=["ON TABLE PCHOLD FORMAT COMT"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 06: Verify syntax generated for CSV format')
        time.sleep(4)
        
        """    
        Step 07: Run
        """
        time.sleep(4)
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        
        """    
        Step 08: Verify .csv file is downloaded
        Step 09: Open the .csv file > Verify output
        Step 10: Close the Excel application
        """
        utillobj.save_file_from_browser('C2967558_actual_1', custom_cr_re="Untitled")
        utillobj.verify_xml_xls('C2967558_actual_1.csv', 'C2967558_base_1.csv', 'Step 08. Verify .csv file is downloaded > Open the .csv file > Verify output')
        time.sleep(2)
        utillobj.switch_to_main_window()
        
        """    
        Step 11: Select Save > Save as "C2967558" > Save
        """
        report.save_report_from_toptoolbar()
        report.wait_for_visible_text(cancel_css, "Cancel")
        input_obj = utillobj.validate_and_get_webdriver_object("#IbfsOpenFileDialog7_cbFileName input", "Input css")
        input_obj.clear()
        time.sleep(5)
        input_obj.send_keys(Test_Case_ID)
        time.sleep(2)
        save_button_obj = utillobj.validate_and_get_webdriver_object("#IbfsOpenFileDialog7_btnOK", "save css")
        save_button_obj.click()
        time.sleep(5)
        
        
        """    
        Step 12: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """    
        Step 13: Reopen saved FEX:
        Step 14: Verify Excel (csv) option remains selected   
        """
        utillobj.infoassist_api_edit_(Test_Case_ID, 'report', 'P292_S10863/G427910', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.verify_element_text("#HomeFormatType>div[id^='BiLabel']",'Excel (csv)','Step 14. Verify Excel (csv) option remains selected')
        
        """    
        Step 15: Logout    
        """
        time.sleep(3)   

if __name__ == "__main__":
    unittest.main()