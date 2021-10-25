'''
Created on Dec 4, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235623
TestCase Name = Verify creating a Report based on a Reporting Object
'''

import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase

class C2235623_TestClass(BaseTestCase):

    def test_C2235623(self):
        
        Test_Case_ID = "C2235623"
        Restore_fex = "C2227520"
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Logon to WF: http://machine:port/ibi_apps/
        """
        """
        Step 02: Launch MyReport (Report mode) using the below API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10032_G157237/C2227520.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Restore_fex, 'Report', 'S10032', mrid='mrid', mrpass='mrpass')
        table_preview_css="#TableChart_1"
        utillobj.synchronize_with_visble_text(table_preview_css, 'CAR', metaobj.chart_long_timesleep)
        
        """
        Step 03: Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 03.01")
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 03.02")
        coln_list = ["CAR", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 03.03: Verify report titles")
#         iaresultobj.create_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds01.xlsx')
        iaresultobj.verify_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds01.xlsx', 'Step 03.04: Verify the report is displayed')
        
        """    
        Step 04: Click "IA" > "Close" > Click "Yes" to save prompt
        """
        ribbonobj.select_tool_menu_item('menu_close')
        utillobj.synchronize_until_element_is_visible("div[id^='loginForm'] div[id*='saveChangesLabel']", metaobj.chart_long_timesleep)
        self.driver.find_element_by_css_selector("div[id^='loginForm'] div[id*='saveChangesLabel']").is_displayed()
        btn_css="div[id*='loginForm'] div[class^=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        core_utilobj.left_click(dialog_btns[btn_text_list.index('Yes')])
        utillobj.synchronize_until_element_disappear("div[id*='loginForm']", metaobj.chart_long_timesleep)
        
        """    
        Step 05: Save as "C2235623" > Click "Save"
        """
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
        Step 06: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.wf_logout()
              
        """
        Step 07: Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235623.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Report', 'S10032', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text(table_preview_css, 'CAR', metaobj.chart_long_timesleep)
             
        """
        Step 08: Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 08.01")
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 08.02")
        coln_list = ["CAR", "SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 08.03: Verify report titles")
#         iaresultobj.create_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds02.xlsx')
        iaresultobj.verify_across_report_data_set("TableChart_1", 1, 2, 10, 2,  Test_Case_ID+'_Ds02.xlsx', 'Step 08.04: Verify the report in Preview')
        
        """
        Step 09: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()