'''
Developed By  : KK14897
Developed Date: 21-09-2018

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/9970&group_by=cases:section_id&group_id=156524&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2274412
TestCase Name = AutoDrill enabled reports are not listed when creating New IA Document
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report

class C2274412_TestClass(BaseTestCase):
    
    def test_C2274412(self):
        
        report_obj=report.Report(self.driver)
        """    
            Step 01 : Launch IA, Report using Api link
            http://machine:port/alias/ia?tool=Report&master=ibisamp/carolap&item=IBFS%3A%2FWFC%2FRepository%2FP276_S9970/G156524    
        """
        report_obj.invoke_ia_tool_using_api_login("report", "ibisamp/carolap")
          
        """    
            Step 02 : Double click on "SALES", "COUNTRY"
        """
        element_css= "#queryTreeColumn"
        report_obj.double_click_on_datetree_item("SALES", 1)
        report_obj.wait_for_visible_text(element_css, "SALES")
        report_obj.double_click_on_datetree_item("COUNTRY->COUNTRY->COUNTRY", 3)
        report_obj.wait_for_visible_text(element_css, "COUNTRY")
          
        """    
            Step 03 : Select Format Tab -> click "Auto Drill"
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
          
        """    
            Step 04 : Click "IA" > Exit > Yes    
        """
        report_obj.select_visualization_application_menu_item('exit')
        report_obj.wait_for_number_of_element("div[id*='saveChangesLabel']", 1, 10)
        report_obj.ia_exit_save("Yes")
          
        """    
            Step 05 : Enter title = "C2106696" > Click Save   
        """
        report_obj.save_file_in_save_dialog("C2106696")
          
        """    
            Step  6 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
                     
        """    
            Step 07 : Launch IA, Document using Api link
            http://machine:port/alias/ia?tool=Report&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FP276_S9970/G156524    
        """
        report_obj.invoke_ia_tool_using_api_login("document", "ibisamp/car")
               
        """    
            Step 08 : Select Insert Tab -> click "Existing Report"    
        """
        report_obj.select_ia_ribbon_item("Insert", "Existing_Report")
         
        """   
            Step 09 : Verify auto drill enabled fex (C2106696) is listed in the dialog    
        """
        report_obj.verify_item_in_open_dialog("Domains->P276->S9970", 'C2106696', True, "step 09.01: verify existing fex")
         
        """    
            Step 10 : Select the C2106696 from the list > Click Open   
        """
        report_obj.select_masterfile_in_open_dialog("Domains->P276->S9970", 'C2106696')
        report_obj.wait_for_number_of_element('div[style*="position:absolute;"][class*="x"]', 13, 80)
         
        """    
            Step 11 : Verify Report is inserted on Canvas   
        """
        coln_list = ["COUNTRY", "SALES"]
        report_obj.verify_report_titles_on_preview(2, 2, "IncludeTable_1 ", coln_list, "Step 11.01: Verify column titles")
         
        """    
            Step 12 : Click IA > Save   
        """
        report_obj.select_visualization_application_menu_item('save')
         
        """    
            Step 13 : Enter title ="C2106696_Document" > Click save   
        """
        report_obj.save_file_in_save_dialog("C2106696_Document")
         
        """    
            Step 14 : Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
        """    
            Step 15 : Reopen the document using URL
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FP276_S9970/G156524%2FC2106696_Document.fex&tool=Document   
        """
        report_obj.edit_fex_using_api_url(fex_name='C2106696_Document',folder_name="P276/S9970", mrid='mrid', mrpass='mrpass')
         
        """    
            Step 16 : Verify report on canvas   
        """
        coln_list = ["COUNTRY", "SALES"]
        report_obj.wait_for_number_of_element('div[style*="position:absolute;"][class*="x"]', 13, 190)
        report_obj.verify_report_titles_on_preview(2, 2, "IncludeTable_1 ", coln_list, "Step 16.01: Verify column titles")
        
        """    
            Step 17 : Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        
        
if __name__ == '__main__':
    unittest.main()