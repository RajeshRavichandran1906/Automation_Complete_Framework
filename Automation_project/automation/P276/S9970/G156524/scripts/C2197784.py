'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197784
TestCase Name = AutoDrill - Drill up then Drill down loses Restore Original
'''
import unittest
from common.wftools.report import Report 
from common.pages import visualization_ribbon, ia_run, visualization_metadata
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase


class C2197784_TestClass(BaseTestCase):
    
    def test_C2197784(self):
        
        report_ = Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2197784"
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver.implicitly_wait(60)
        #resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        report_.wait_for_visible_text('#TableChart_1', 'Sale,Year', report_.report_long_timesleep)
        
#         time.sleep(40)
#         elem1=(By.CSS_SELECTOR, "#TableChart_1")
#         resultobj._validate_page(elem1)
#         time.sleep(8)
        
        """    2. Click on Store,Business,Region in the Query panel. From the ribbon click on Subtotal and Line Break to remove them from the report    """
        metaobj.querytree_field_click("Store,Business,Region", 1)
        time.sleep(12)
        ribbonobj.select_ribbon_item("Field", "Subtotal_icon")
        time.sleep(12)
        ribbonobj.select_ribbon_item("Field", "Line_break")
        time.sleep(12)
        
        """    3. Right click on Product,Category in the Query panel and select Delete to remove it from the report.    """
        metaobj.querytree_field_click("Product,Category", 1, 1, "Delete")
        time.sleep(8)
        
        """    4. Replace Store,Business,Region with Store,State,Province    """
        metaobj.querytree_field_click("Store,Business,Region", 1, 1, "Delete")
        time.sleep(12)
        metaobj.datatree_field_click("Store,State,Province", 2, 1)
        report_.wait_for_visible_text('#queryTreeColumn','Store,State,Province')
        
        """    5. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(8)
        
        """    6. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        #time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        report_.wait_for_visible_text('table[summary="Summary"]', 'Sale,Year',report_.report_long_timesleep)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=7)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 11a: Verify dataset", desired_no_of_rows=7)
        
        """    7. Click on Alabama and choose Drill up to Store Country.     """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,1,'Go up to Store Country')
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",3,1,'Drill up to Store Country', "Step 7")
        time.sleep(8)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=7)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 7a: Verify dataset drilldown displayed", desired_no_of_rows=7)
        time.sleep(3)
        
        """    8. Click on Australia and choose Drill down to Store State Province.    """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,1,'Drill down to Store State Province')
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",3,1,'Drill down to Store State Province', "Step 7")
        time.sleep(8)
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 11a: Verify dataset")
        
        """    9. Click on New South Wales    """
        expected_tooltip_list = ['Reset', 'Go up to Store Country', 'Drill down to Store City']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",5,1, expected_tooltip_list, "Step 09: Restore Original is in the list of options")
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        
        """    10. Click IA > Save As> Type C2197784 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        report_.wait_for_visible_text('[id*="dlgIbfsOpenFile"]', 'Save')
        #time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """    11. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()