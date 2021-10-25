'''
Reautomated by Niranjan on 28th November 2017.

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227575
TestCase Name = Verify report with Pages on Demand
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase

class C2227575_TestClass(BaseTestCase):

    def test_C2227575(self):
        
        Test_Case_ID = "C2227575"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/MOVIES&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/movies','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        
        """ 2. Double click "MOVIECODE", "TITLE", "WHOLESALEPR".        """
        metaobj.datatree_field_click("MOVIECODE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("TITLE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('WHOLESALEPR', 2, 1)
        time.sleep(4)
        
        
        """ 3. Verify the following report is displayed.            """
        parent_css="TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        coln_list = ['MOVIECODE', 'TITLE', 'WHOLESALEPR']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 25, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 3.2: Verify report dataset in live preview.')
        
        
        """ 4. Select "Format" > "Pages On Demand" (Navigation Group).        """
        ribbonobj.select_ribbon_item('Format', 'pages_on_demand')
        
        
        """ 5. Click "Run".            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        """ 6. Verify that a new window is opened on demand paging toolbar            """
        utillobj.switch_to_frame(pause=2, frame_css="html > frameset > frame[title='Report']",frame_height_value=0)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds02.xlsx", 'Step 6.1: Verify page on demand report dataset', desired_no_of_rows=25)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2, frame_css="html > frameset > frame[title='Control']",frame_height_value=0)
        on_demand_paging_toolbar_obj=self.driver.find_element_by_css_selector("table>tbody")
        condition1=bool('Page' in on_demand_paging_toolbar_obj.text)
        utillobj.asequal(True, condition1, "Step 6.2: Verify 'Page' text available inside 'on demand paging toolbar'.") 
        condition2=bool('Search' in on_demand_paging_toolbar_obj.text)
        utillobj.asequal(True,condition2, "Step 6.3: Verify 'Search' text available inside 'on demand paging toolbar'.")
        val = on_demand_paging_toolbar_obj.find_element_by_css_selector("input#gotopageedit").get_attribute("value")
        utillobj.asequal('1',val, "Step 6.4: Verify '1' is displayed on Page search box inside 'on demand paging toolbar'.")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        report_height=self.driver.find_element_by_css_selector("html > frameset > frame[title='Report']").size['height']
        y_location=self.driver.find_element_by_css_selector("html > frameset > frame[title='Control']").location['y']
        utillobj.as_GE(y_location, report_height, "Step 6.5: Verify 'on demand paging toolbar' is being displayed at the bottom of the report.")
        """ 7. Dismiss the new window.            """
        driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        
        """ 8. Click "IA" > "Save".                  """
        """ 9. Enter Title = "C2227575".             """
        """ 10. Click "Save".                        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
        """ 11. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp            """
        utillobj.infoassist_api_logout()
        
        
        """ 12. Run saved FEX:    
                http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2227575.fex
        """
        suite_id=utillobj.parseinitfile('suite_id')
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", suite_id, 'mrid', 'mrpass')
        time.sleep(20)
        utillobj.switch_to_frame(pause=2, frame_css="html > frameset > frame[title='Report']",frame_height_value=0)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds03.xlsx", 'Step 12.1: Verify page on demand report dataset', desired_no_of_rows=25)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2, frame_css="html > frameset > frame[title='Control']",frame_height_value=0)
        on_demand_paging_toolbar_obj=self.driver.find_element_by_css_selector("table>tbody")
        condition1=bool('Page' in on_demand_paging_toolbar_obj.text)
        utillobj.asequal(True,condition1, "Step 12.2: Verify 'Page' text available inside 'on demand paging toolbar'.") 
        condition2=bool('Search' in on_demand_paging_toolbar_obj.text)
        utillobj.asequal(True,condition2, "Step 12.3: Verify 'Search' text available inside 'on demand paging toolbar'.")
        val = on_demand_paging_toolbar_obj.find_element_by_css_selector("input#gotopageedit").get_attribute("value")
        utillobj.asequal('1',val, "Step 12.4: Verify '1' is displayed on Page search box inside 'on demand paging toolbar'.")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        report_height=self.driver.find_element_by_css_selector("html > frameset > frame[title='Report']").size['height']
        y_location=self.driver.find_element_by_css_selector("html > frameset > frame[title='Control']").location['y']
        utillobj.as_GE(y_location, report_height, "Step 12.5: Verify 'on demand paging toolbar' is being displayed at the bottom of the report.")
        
        """ 13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp              """
        utillobj.infoassist_api_logout()
        
        
        """ 14. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227575.fex&tool=Report
        """
        parent_css="input[id='SignonUserName']"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        
        
        """ 15. Select Format Tab > Verify "Pages On Demand" is toggled ON            """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(2)
        page_on_demant_elem=self.driver.find_element_by_css_selector("#FormatReportPod")
        utillobj.verify_checked_class_property(page_on_demant_elem, "Step 15.1: Verify 'Pages On Demand' is toggled ON.")
       
        """ 16. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()