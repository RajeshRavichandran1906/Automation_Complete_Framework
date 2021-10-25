'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226957
TestCase Name = Test drilling all the way down and up an ACROSS hierarchy path - HTML
'''

from common.pages import visualization_ribbon, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
import unittest, time
from common.wftools.report import Report
from common.lib.global_variables import Global_variables

class C2226957_TestClass(BaseTestCase):
    
    def test_C2226957(self):
        
        """
        TEST CASE VARIABLES
        """
        Test_ID="C2226957"
        
        """
        OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=Global_variables.browser_name
        Test_Case_ID = Test_ID+"_"+browser_type
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        report_ = Report(self.driver)
        
        """    
            STEP 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_visble_text("div[class^='x']", 'Sale,Year', 180)
        
        """    
            STEP 02 : Click Format tab > Autodrill button     
        """
#         ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)  # giving time to click format properly
        report_.select_ia_ribbon_item("Format", "auto_drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, 15)
        
        """    
            STEP 03 : Click RUN     
        """
        frame_css = "iframe[id^='ReportIframe-']"
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe-']", 1, 80)
        iframe_location = self.driver.find_element_by_css_selector(frame_css).location
        utillobj.switch_to_frame(pause=3)
        utillobj.switch_to_frame(pause=3, frame_css='iframe[src]')
        utillobj.browser_x = iframe_location['x']
        utillobj.browser_y = iframe_location['y']
        
        """
            STEP 03.00 : Verify output 
        """
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:first-child>td:first-child", 'Sale,Year', 80)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 03.00: verify Auto Drill, drill down data set")
        
        """    
            STEP 04 : Click on 2016 in the ACROSS labels and Select "Drill down to Sale Year/Quarter "    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",1,2,'Drill down to Sale Year/Quarter')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:first-child", 'Sale,Year/Quarter', 20)
        
        """
            STEP 04.00 : Verify output
        """
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 04.00: Verify Drill down to Sale Year/Quarter Report")
        
        """    
            STEP 05 : Click on 2016 Q4 and Select "Drill down to Sale Year/Month"    
        """
#         iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",3,2,'Drill down to Sale Year/Month', "Step 05",browser_height=80, x_offset=x_fr, y_offset=y_fr-7)
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,2,'Drill down to Sale Year/Month')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:first-child", 'Sale,Year/Month', 20)
        
        """
            STEP 05.00 : Verify output
        """
        iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 05.00: Verify Drill down to Sale Year/Month Report")
        
        """    
            STEP 06 : Click on 2016/12 and Select "Drill down to Sale Day"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,2,'Drill down to Sale Day')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:first-child", 'Sale,Day', 20)
        
        """
            STEP 06.00 : Verify output
        """
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx", "Step 06.00: Verify Drill down to Sale Day Report")
            
        """    
            STEP 07 : Click on 2016/12/31 and select "Drillup to Sale Year/Month"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,2,'Go up to Sale Year/Month')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:first-child", 'Sale,Year/Month', 20)
        
        """
            STEP 07.00 : Verify output
        """
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 07.00: Verify Drill up to Sale Year/Month Report")
        
        """    
            STEP 08 : Click on 2016/12 and select "Drillup to Sale Year/Quarter"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,2,'Go up to Sale Year/Quarter')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:first-child", 'Sale,Year/Quarter', 20)
        
        """
            STEP 08.00 : Verify output
        """
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 08.00: Verify Drill up to Sale Year/Quarter Report")
        
        """    
            STEP 09 : Click on 2016 Q4 and select "Drillup to Sale Year"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,2,'Go up to Sale Year')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        #utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:first-child>td:first-child", 'Sale,Year', 20)
        
        """
            STEP 09.00 : Verify output
        """
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 09.00: Verify Drill up to Sale Year Report")
        utillobj.switch_to_default_content()
        
        """    
            STEP 10 : Click IA > Save As> Type C2226957 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
            STEP 11 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226957.fex&tool=report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        
        """    
            STEP 12 : Click format tab and see Autodrill button is still selected    
        """
        time.sleep(13)  # giving time to click format properly
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_visble_text('#FormatTab', 'Features', ribbonobj.report_short_timesleep)
        report_.verify_ribbon_item_is_enabled('format_auto_drill', '12.00')
        
        """    
            STEP 13 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    