'''
Created on Dec 4, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235623
TestCase Name = Verify creating a Report based on a Reporting Object
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_legacymainpage, ia_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2235623_TestClass(BaseTestCase):

    def test_C2235623(self):
        
        Test_Case_ID = "C2235623"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        legacymainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Logon to WF: http://machine:port/ibi_apps/
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        time.sleep(6)
        
        """
        Step 02: Expand folder "S10032" > Right-click "C2227520" > New > Report
        """
        legacymainobj.select_repository_menu('P292->S10032_infoassist_4->C2227520', 'New->Report')
        time.sleep(6)
        utillobj.switch_to_window(1)
        time.sleep(5)
        parent_css="#applicationButton"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 03: Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 03.a")
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 03.b")
        coln_list = ["CAR", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 03.c: Verify report titles")
#         iaresultobj.create_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds01.xlsx')
        iaresultobj.verify_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds01.xlsx', 'Step 03.d: Verify the report is displayed')
        
        """    
        Step 04: Click "IA" > "Close" > Click "Yes" to save prompt
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
        self.driver.find_element_by_css_selector("div[id^='loginForm'] div[id*='saveChangesLabel']").is_displayed()
        btn_css="div[id*='loginForm'] div[class^=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('Yes')].click()
        time.sleep(6)
        
        """    
        Step 05: Save as "C2235623" > Click "Save"
        """
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    
        Step 06: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 07: Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235623.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Report', 'S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 08: Verify Query pane and Preview
        """
        parent_css="#applicationButton"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 08.a")
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 08.b")
        coln_list = ["CAR", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 08.c: Verify report titles")
#         iaresultobj.create_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds02.xlsx')
        iaresultobj.verify_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds02.xlsx', 'Step 08.d: Verify the report in Preview')
        
        """
        Step 09: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()