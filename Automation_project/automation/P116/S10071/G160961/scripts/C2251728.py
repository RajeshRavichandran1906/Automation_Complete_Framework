'''
Created on Jan 17, 2019

@author: Magesh

Testsuite =  http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_id=160961&group_order=asc
Testcase id = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251728
TestCase Name = Removing a Global Filter from Document display.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_report
from common.wftools import document
from common.lib import utillity
from common.pages import webfocus_editor

class C2251728_TestClass(BaseTestCase):

    def test_C2251728(self):
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID="C2251728"
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        webfocus_editor_obj=webfocus_editor.WebfocusEditor(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME=60
        folder_name="P116/S10071_4"
        fex_name="AR-AD-082-AHTML"
        run_report_css="ITableData0"
        table_css = "table[id='iLayTB$']"
        filter_css=".arDashboardBar .arDashboardBarGlobalButton [title='Global Filter'] img"
        heading_css='#ITableData0 #TCOL_0_C_0 span'
        
        """
        Step 01: Execute AR-AD-AHTML-082.fex from below API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S10071/G160961&BIP_item=AR-AD-AHTML-082.fex.
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name, 'mrid', 'mrpass', run_table_css=heading_css, no_of_element=1, wait_time=MEDIUM_WAIT_TIME)
        
        """
        Step 1.1: Expect to see the following AHTML Document with Global Filter symbol available.
        """
        utill_obj.verify_object_visible(filter_css,True,"Step 1.1: verify active filter icon is available")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step 1.2: verify page summary")
#         report_obj.create_table_data_set("#"+run_report_css,Testcase_ID+"_DS_1.xlsx")
        report_obj.verify_table_data_set("#"+run_report_css, Testcase_ID+"_DS_1.xlsx",msg="Step 1.3: verify table dataset for report1")
        report_obj.api_logout()
        
        """
        Step 02: Open saved AR-AD-AHTML-082.fex using the below API
        http://machine:port/alias/tools/portlets/resources/markup/sharep/SPEditorBoot.jsp?folderPath=IBFS%253A%252FWFC%252FRepository%252FP116_S20311/G683541description=AR-AD-AHTML-082&itemName=AR-AD-AHTML-082.fex&isReferenced=true&type=items
        Change the Keyword/value pair SHOW_GLOBALFILTER=ON to SHOW_GLOBALFILTER=OFF
        """
        webfocus_editor_obj.invoke_fex_using_text_editor(folder_name,fex_name, mrid='mrid', mrpass='mrpass')
        webfocus_editor_obj.find_and_replace_in_text_editor("SHOW_GLOBALFILTER=ON","SHOW_GLOBALFILTER=OFF")
        
        """
        Step 03: Click Run 
        """
        webfocus_editor_obj.click_text_editor_ribbon_button('Run')
        
        """
        Step 3.1: Expect to see the following AHTML Document, this time with no Global Filter symbol available.
        """
        report_obj.switch_to_new_window()
        utill_obj.verify_object_visible(filter_css,False,"Step 3.1: verify active Global Filter symbol is not available")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step 3.2: verify page summary")
        report_obj.verify_table_data_set("#"+run_report_css, Testcase_ID+"_DS_1.xlsx",msg="Step 3.3: verify table dataset for report1")
        doc_obj.verify_active_document_page_layout_menu_run_window(table_css,['Layouts','Page 1','Page 2','Page 3'], "Step 3.4: Verify Multipage_dashboard")
        
        """
        Step 04: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.switch_to_previous_window()
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()