'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2230844
TestCase Name = Test that Auto Drill works with Pages on Demand option
'''
import unittest, time
from common.pages import ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.wftools.report import Report

class C2230844_TestClass(BaseTestCase):
    
    def test_C2230844(self):
        
        """
        Test case variable
        """
        Test_ID="C2230844"
        
        """
        Class & Objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=Global_variables.browser_name
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        report_ = Report(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        expected_pages_on_demand=['PageForm', 'AllForm', 'TopForm', 'PrevForm', 'NextForm', 'BottomForm', 'FindForm', 'CaseForm', 'DirForm', 'HelpForm', 'CloseForm']
        
        """    
            Step 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(120)
        
        #utillobj.synchronize_with_visble_text("div[class^='x']", 'Sale,Year', 180)
        
        """    
            Step 02 : Click Format tab > Autodrill button     
        """
        report_.select_ia_ribbon_item("Format", "auto_drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, 30)
        
        """    
            Step 03 : Select Format > Freeze    
        """
        report_.select_ia_ribbon_item("Format", "pages_on_demand")
        utillobj.synchronize_with_number_of_element("[id='FormatReportPod'][class*='checked']", 1, 30)
        
        """    
            Step 04 : Click RUN     
        """
        report_.run_report_from_toptoolbar()
        utillobj.switch_to_window(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.switch_to_frame(pause=3,frame_css="frame[name='report']")
        utillobj.synchronize_with_visble_text("table[summary='Summary']>tbody>tr:nth-child(1)>td:nth-child(1)", 'Sale,Year', 180)
        
        """
            Step 04.1 : Verify the ODP report opens in new window.
        """
        #iarun.create_table_data_set("table[summary='Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=7)
        iarun.verify_table_data_set("table[summary='Summary']", Test_ID+"_Ds01.xlsx", "Step 04.01: Verify dataset drilldown displayed", desired_no_of_rows=7)
        utillobj.switch_to_default_content(1)
        
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.switch_to_frame(pause=3,frame_css="frame[name='vcp']")
        table_forms=driver.find_elements_by_css_selector("table > tbody > tr > td > form")
        actual_pages_on_demand = [f.get_attribute("name") for f in table_forms]
        utillobj.asequal(expected_pages_on_demand, actual_pages_on_demand, "Step 04.02: Verify Pages on Demand opens in New window")
        utillobj.switch_to_default_content(1)
    
        """    
            Step 05. Click on North America and select "Drill down to Store Business Sub Region".     
        """
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.switch_to_frame(pause=3,frame_css="frame[name='report']")
        
        cell_css="table[summary='Summary'] > tbody > tr:nth-child(12) > td:nth-child(1) > a"
        obj_cell_css=self.driver.find_element_by_css_selector(cell_css)
        utillobj.left_click_with_offset(obj_cell_css)
        time.sleep(2)
        
        tooltip_css="div.clsMDMenu > table > tbody > tr > td > a > span" 
        tooltip=self.driver.find_element_by_css_selector(tooltip_css)
        utillobj.left_click_with_offset(tooltip)
        time.sleep(10)
        
        """
            Step 05.1 : Verify that report has Auto Drill links and still be in ODP mode.
        """
        utillobj.switch_to_default_content(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.switch_to_frame(pause=3,frame_css="frame[name='report']")
        utillobj.switch_to_frame(pause=3,frame_css="frame[name='report']")
        utillobj.synchronize_with_visble_text("table[summary='Summary']", 'Canada', 120)
         
#         iarun.create_table_data_set("table[summary='Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=7)
        iarun.verify_table_data_set("table[summary='Summary']", Test_ID+"_Ds02.xlsx", "Step 05.01: Verify dataset drilldown displayed", desired_no_of_rows=7)
        utillobj.switch_to_default_content(1)
        
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]') 
        utillobj.switch_to_frame(pause=3,frame_css="frame[name='report']")
        utillobj.switch_to_frame(pause=3,frame_css="frame[name='vcp']")
        table_forms=driver.find_elements_by_css_selector("table > tbody > tr > td > form")
        actual_drilldown_pages_on_demand = [f.get_attribute("name") for f in table_forms]
        utillobj.asequal(expected_pages_on_demand, actual_drilldown_pages_on_demand, "Step 05.02: Verify Pages on Demand opens retains for Drilldown report")
        utillobj.switch_to_default_content(1)
        
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """    
            Step 06 : Click IA > Save As> Type C2230844 > click Save    
        """
        report_.save_as_from_application_menu_item(Test_Case_ID)
        utillobj.infoassist_api_logout()
        
        """    
            Step 07. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2230844.fex&tool=report    
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(120)
        utillobj.synchronize_with_visble_text("div[class^='x']", 'Sale,Year', 180)
         
        """    
            Step 08 : Click on the Format tab. Verify that Auto Drill and On Demand Page are still selected.   
        """
        report_.switch_ia_ribbon_tab('Format')
        utillobj.synchronize_with_visble_text('#FormatTab', 'Features', report_.report_short_timesleep)
        report_.verify_ribbon_item_is_enabled('format_auto_drill', '08.01')
        report_.verify_ribbon_item_is_enabled('format_pages_on_demand', '08.02')
        
        """    
            Step 09 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()