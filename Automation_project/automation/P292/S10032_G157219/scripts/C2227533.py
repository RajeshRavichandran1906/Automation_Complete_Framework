'''
Created on Jan'25, 2017
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227533
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon
from common.lib import utillity

class C2227533_TestClass(BaseTestCase):

    def test_C2227533(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2227533'
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ Step 01: Launch IA Report mode:- http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/EMPDATA&item=IBFS%3A%2FWFC%2FRepository%2FS10032 """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P292/S10032_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=20)
        
        """ 2. Select "Data" > "Join". """
        """ 3. Click "Add New" > TRAINING.MAS > "Open" """
        ia_ribbonobj.create_join("training")
        
        """ 4. Verify the following Join window is displayed """
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 04a: Verify join created successfully")
        
        """ 5. lick > "OK". """
        driver.find_element_by_css_selector("#dlgJoin_btnOK img").click()
        time.sleep(5)
        
        """ 6. Double click "LASTNAME", "COURSECODE", "EXPENSES". """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("COURSECODE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        time.sleep(4) 
        
        """ 7. Verify the following report is displayed. """
        coln_list = ["LASTNAME", "COURSECODE", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 07a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30,3, "C2227533_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 30,3,'C2227533_Ds01.xlsx',"Step 07b: Verify report data set")
        
        """ 8. Select "Home" > "Document". """
        ribbonobj.select_ribbon_item("Home", "Document")
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document') 
        
        """ 9. Verify the format is "Active Report" """
        utillobj.verify_object_visible("#HomeFormatType img[src$='active_reports_32.png']", True, "Step 09a: Verify the Format is Active Report")
        
        """ 10. Click "Active Report" dropdown button > Select "PDF" """
        ribbonobj.change_output_format_type("pdf")
        time.sleep(2)
        
        """ 11. Verify the following report is displayed in "Live Preview". """
        coln_list = ["LASTNAME", "COURSECODE", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 11a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 3, "C2227533_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 30,3,'C2227533_Ds01.xlsx',"Step 11b: Verify report data set")
        
        """ 12. Click "Run". """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        """ 13. Verify the report is displayed. """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step13_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """ 14. Click "IA" > "Save". """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)

        """ 15. Enter Title = "C2227533" """
        """ 16. Click "Save". """
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """ 17. Logout and dismiss prompt for Report1: http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
        driver.find_element_by_css_selector("#saveAllDlg #btnNo").click()
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ 18. Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227533.fex&tool=Document """
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document') 
        
        """ 19. Verify that it launches IA tool and displays the Report on "Canvas". """
        coln_list = ["LASTNAME", "COURSECODE", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 19a: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 30,3,'C2227533_Ds01.xlsx',"Step 11b: Verify report data set")
        
        """ 20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()