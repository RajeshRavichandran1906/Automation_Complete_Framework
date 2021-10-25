'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227565
TestCase Name = Verify Report with Multi Drill
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.lib.basetestcase import BaseTestCase

class C2227565_TestClass(BaseTestCase):

    def test_C2227565(self):
        
        Test_Case_ID = "C2227565"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ 
        Step01: Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_ia_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 30)
         
        """
        Step02: Double click "DEALER_COST".
        Step03: Double click "COUNTRY".     
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 30)
        coln_list = ['COUNTRY','DEALER_COST']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02: Verify Column titles ")
        time.sleep(2)        
         
        """
        Step04: Click "COUNTRY" on Preview Canvas.
        """
        metaobj.querytree_field_click("COUNTRY", 1, 0)
        time.sleep(2)        
         
        """
        Step05: Click "Drill Down" in the Field Tab Ribbon
        """
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
         
        """
        Step06: Click "Web Page" radio button
        Step07: Click URL input box -> Type "http://www.ibi.com"
        Step08: Click "Create a new drill down" button
        """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.ibi.com", create_new_drilldown=True)
         
        """
        Step09: Click "Web Page" radio button
        Step10: Click URL input box -> Type "http://www.google.com"
        Step11: Click OK
        """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.google.com", click_ok=True)
         
        """
        Step12: Verify Report preview with hyperlinks
        """
        ia_resultobj.verify_autolink("TableChart_1","ENGLAND",5,"Step 12: Verify Report preview with hyperlinks")
 
        """
        Step13: Click "IA" > "Save As" > C2227565 > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
        Step14: Click "IA" > Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_frame(pause=3)
        """
        Step15: Click "ENGLAND" -> Verify Drill Down menu
        """
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227565_run_Ds01.xlsx" , 'Step 15: Verify report data set on run window')
        expected_tooltip_list=['Drill Down 1', 'Drill Down 2']
        ia_runobj.verify_autolink_tooltip_values("table[summary='Summary']",2,1, expected_tooltip_list, "Step 15:Verify drilldown at run time")
        
        """
        Step16: Select "Drill Down 1" -> Verify page
        Step17 :Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """        
        time.sleep(3)
        ia_runobj.select_autolink_tooltip_menu("table[summary='Summary']",2,1,'Drill Down 1', "Step 16: Select the Auto Drill menu Drill Down 1")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=1)
        utillobj.switch_to_window(1)
        time.sleep(8)
        expected_title='Data and Analytics Company | ibi'
        drill1=(driver.title in expected_title)
        utillobj.asequal(True, drill1, "Step 17: Verify IBI page is displayed")
        time.sleep(2) 
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(1)
        

if __name__ == '__main__':
    unittest.main()
    