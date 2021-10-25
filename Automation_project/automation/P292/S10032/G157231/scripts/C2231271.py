'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231271
TestCase Name = Verify promoting HOLD file to Document mode
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C2231271_TestClass(BaseTestCase):

    def test_C2231271(self):
        
        Test_Case_ID = "C2231271"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        report = Report(self.driver)
        
        """
        Test case CSS
        """
        qwerty_css = "#queryBoxColumn"
        
        
        """    1. Reopen saved FEX created in precondition test case (C2231275): http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231275.fex&tool=Report    """
        oFolder=utillobj.parseinitfile('suite_id')
        time.sleep(5)
        utillobj.infoassist_api_edit("C2231275", 'report', oFolder, mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    2. Click "IA" menu > Save As > "C2231271" > Click Save     """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5) 
        
        """    3. Click "File" in the Home Tab to create hold file based on this report     """
        ribbonobj.select_ribbon_item('Home', 'File')
        
        """    4. Click "Save" in the "Temporary" dialog, keep default name "File1"    """
        utillobj.expand_domain_folders_in_open_dialog('foccache')
        utillobj.ibfs_save_as("File1")
        time.sleep(5)
        
        """    5. Verify Query and "Create Report" menu at the bottom of the Report    """
        metaobj.verify_query_pane_field("Files", "foccache/File1 (empdata)", 1, "Step 5a: ")
        utillobj.verify_object_visible("#createFromHoldButton img", True, "Step 05b: Verify 'Create Report' button at the bottom of report")
        
        """    6. Click the arrow in the "Create Report" menu > verify menu    """
        """    7. Select "Create Document" > Verify Document canvas    """
        ia_resultobj.create_hold_type('Create Document', verify=True, expected_popup_list=['Create Report', 'Create Chart', 'Create Document'], msg='Step 07:')
        time.sleep(5)
        
        """    8. Double-click fields NEWSITE, COURSECODE, NEWEXPENSES    """
        metaobj.datatree_field_click("Dimensions->NEWSITE", 2, 1)
        report.wait_for_visible_text(qwerty_css, "NEWSITE")
        
        metaobj.datatree_field_click("Dimensions->COURSECODE", 2, 1)
        report.wait_for_visible_text(qwerty_css, "COURSECODE")
       
        metaobj.datatree_field_click("Measures/Properties->NEWEXPENSES", 2, 1)
        report.wait_for_visible_text(qwerty_css, "NEWEXPENSES")
        
        """    9. Click Save button from QAT and OK to the message prompt    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        report.wait_for_visible_text("div[id*='BiDialog']", "OK")
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")   
         
        """    10. Verify Preview    """
        coln_list = ['NEWSITE', 'COURSECODE', 'NEWEXPENSES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 10a: Verify column titles")
#        ia_resultobj.create_report_data_set('TableChart_2', 15, 3, 'C2231271_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_2', 15, 3, 'C2231271_Ds01.xlsx', 'Step 10b: Verify Preview report dataset', no_of_cells=3)
        
        """    11. Click Run > Verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        report.switch_to_frame()
        miscobj.verify_page_summary(0, '35of35records,Page1of1', 'Step 11a: Verify the Report Heading')
        column_list=['NEWSITE', 'COURSECODE', 'NEWEXPENSES']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 11b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2231271_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2231271_Ds02.xlsx', 'Step 11c: Verify data.')
        report.switch_to_default_content()
        
        """    12. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    13. Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231271.fex&tool=Document    """
        oFolder=utillobj.parseinitfile('suite_id')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        time.sleep(2)
        
        """    14. Verify Canvas    """
        coln_list = ["NEWSITE","COURSECODE", "NEWEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 14a: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_2', 15, 3, 'C2231271_Ds01.xlsx', 'Step 14b: Verify Preview report dataset', no_of_cells=3)
        
        """    15. Right-click "File1 (empdata)" in the Query pane > Edit    """
        metaobj.querytree_field_click('foccache/File1 (empdata)', 1, 1, 'Edit')
        parent_css="#rtnToDocButton img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    16. Verify Preview    """
        coln_list = ["NEWSITE", "LASTNAME", "COURSECODE", "EXPENSES", "NEWEXPENSES"]
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 16a: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1', 10, 5, 'C2231271_Ds03.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 5, 'C2231271_Ds03.xlsx', 'Step 16b: Verify Preview report dataset', no_of_cells=5)
        
        """    17. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
        
if __name__ == '__main__':
    unittest.main()