'''
Created on 17-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227470
TestCase Name = Verify Slicer based on a joined field
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon
from common.pages import define_compute 
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase

class C2227470_TestClass(BaseTestCase):

    def test_C2227470(self):
        
        Test_Case_ID = "C2227470"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        
        """ 1. Launch the IA API with CAR, Report mode:    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P292/S10032_infoassist_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1)
        
        """ 2. Select "Data" > "Join".        """
        """ 3. Click "Add New" > TRAINING.MAS > "Open" > "OK".        """
        ia_ribbobj.create_join("ibisamp", "training")
        time.sleep(2)
        driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        
        
        """ 4. Double click "LASTNAME", "COURSECODE".    """
        resultobj.wait_for_property("#TableChart_1", 1)
        metaobj.datatree_field_click("Dimensions->LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Dimensions->COURSECODE", 2, 1)
        
        """ 5. Select "Data" > "Define".        """
        defcomp.invoke_define_compute_dialog('define')
        resultobj.wait_for_property("#fname", 1)
        
        """ 6. Enter Field = "JOINDEFEXPENSES"        """
        """ 7. Double click "EXPENSES" > "OK".        """
        defcomp.enter_define_compute_parameter("JOINDEFEXPENSES", 'D12.2', 'Measures/Properties->EXPENSES', 1)
        defcomp.close_define_compute_dialog('ok')
        
        """ 8. Double click "JOINDEFEXPENSES" from Data panel        """
        resultobj.wait_for_property("#TableChart_1", 1)
        metaobj.datatree_field_click("Measures/Properties->JOINDEFEXPENSES", 2, 1)
        
        """ 9. Verify "JOINDEFEXPENSES" field is displayed in "Live Preview".        """
        coln_list = ["LASTNAME", "COURSECODE", "JOINDEFEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 09.01: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, Test_Case_ID+"_Ds01.xlsx", "Step 09.02: verify preview data", no_of_cells=3)
        
        """ 10. Select Slicers Tab > Drag and drop "JOINDEFEXPENSES" from Data pane into Group 1 in the Slicers Ribbon    """
#         ribbonobj.switch_ia_tab('Slicers')
#         time.sleep(5)
#         metaobj.datatree_field_click("Measures/Properties->JOINDEFEXPENSES", 1, 1, "Slicers", "Existing Group")
#         driver.find_element_by_css_selector("#addSlicerDlg #addSlicerOkBtn").click()
        metaobj.drag_drop_data_tree_items_to_slicers('JOINDEFEXPENSES', 1, 1)
        #ia_ribbobj.drag_drop_fields_to_slicer('JOINDEFEXPENSES', 1, 1)
        time.sleep(8)
        expected_list = ['Group 1', 'JOINDEFEXPENSES']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 10.00: Drop "JOINDEFEXPENSES" from Data pane into Group 1 in the Slicers Ribbon')
        
        """ 11. Change the operator in the Slicer group to "greater than or equal to"        """
        time.sleep(2)
        ia_ribbobj.select_slicer_condition(1, 0, 'gte')
        
        """ 12. Click "JOINDEFEXPENSES" dropdown menu > verify list of values > Select value 3,000.00 and click OK  """
        ia_ribbobj.select_group_slicer_dropdown(1, "JOINDEFEXPENSES")
        time.sleep(5)
        value_css=driver.find_elements_by_css_selector("#filterValuesList tr td")
        actual_list=[el.text.strip() for el in value_css]
        expected_list=['.00 (0)', '975.00 (975)', '1,000.00 (1000)', '1,150.00 (1150)', '1,200.00 (1200)', '1,250.00 (1250)', '1,580.00 (1580)', '1,630.00 (1630)', '1,730.00 (1730)']
        utillobj.as_List_equal(actual_list,expected_list, "Step 12.00: verify list of values")
        ia_ribbobj.close_slicer_dialog('ok')
        time.sleep(5)
        combo_item_list = ['3,000.00 (3000)']
        ia_ribbobj.create_slicer(1, 'JOINDEFEXPENSES', combo_item_list, 'large', 'ok', last_combo_item_no=27)
        
        """ 13. Click to Update Preview in Slicers->Options->Update Preview    """
        resultobj.wait_for_property("#TableChart_1", 1)
        ribbonobj.select_ribbon_item('Slicers', 'Update_preview')
        time.sleep(8)
        
        """ 14. Verify Report                                    """
        coln_list = ["LASTNAME", "COURSECODE", "JOINDEFEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 14.01: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, Test_Case_ID+"_Ds02.xlsx", "Step 14.02: verify preview data", no_of_cells=3)
            
        """ 15. Click "Save" in the toolbar > "C2227470" > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """ 16. Logout:  'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """ 17. Reopen fex using IA API: 'http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227470.fex&tool=report'    """
        resultobj.wait_for_property("input[id=SignonUserName]", 1)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(2)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_1')
        
        """ 18. Verify Report        """
        resultobj.wait_for_property("#TableChart_1", 1)
        coln_list = ["LASTNAME", "COURSECODE", "JOINDEFEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 18.01: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, Test_Case_ID+"_Ds02.xlsx", "Step 18.02: verify preview data", no_of_cells=3)
        time.sleep(4)
        
        """ 19. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp"""
        
if __name__ == '__main__':
    unittest.main()