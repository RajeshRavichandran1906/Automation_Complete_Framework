'''
Created on 15-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227466
TestCase Name = Verify create Slicer by drag and drop
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run 
from common.lib import utillity
import time
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility

class C2227466_TestClass(BaseTestCase):

    def test_C2227466(self):
        
        Test_Case_ID = "C2227466"
        driver = self.driver
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        parent_id_css= '#TableChart_1'
        
        """ 1. Launch the IA API with CAR, Report mode:    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(parent_id_css, 1, 190)
        
        """ 2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".     """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_visble_text(parent_id_css, 'COUNTRY', 90)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text(parent_id_css, 'CAR', 90)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        utillobj.synchronize_with_visble_text(parent_id_css, 'DEALER_COST', 90)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        utillobj.synchronize_with_visble_text(parent_id_css, 'RETAIL_COST', 90)
        
        """ 3. Verify the following report is displayed.       """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 3: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, 'C2227466_Ds01.xlsx', 'Step 3.1: Verify report dataset', no_of_cells=4)
        
        """ 4. Select "Slicers" tab.   """
        ribbonobj.switch_ia_tab('Slicers')
        
        """ 5. Verify "Group1" slicer is available.    """
        time.sleep(3)
        expected_list = ['Group 1', 'Drag Fields Here to Create Slicers']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 5: Group 1 slicer is available')
        
        """ 6. Select "COUNTRY" in Data pane.          """
        """ 7. Drag it to the "Group1" area.            """
        metaobj.datatree_field_click("COUNTRY", 1, 1, "Slicers", "Existing Group")
        time.sleep(3)
        driver.find_element_by_css_selector("#addSlicerDlg #addSlicerOkBtn").click()
        time.sleep(8)
        #metaobj.drag_drop_data_tree_items_to_slicers("COUNTRY", 1, 1)
        
        """ 8. Verify "COUNTRY" has been added to "Group 1". """
        time.sleep(2)
        expected_list = ['Group 1', 'COUNTRY']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 8:"COUNTRY" has been added to "Group 1"')
        
        
        """ 9. Click on "COUNTRY" slicer.        """
        """ 10. Select COUNTRY = (ENGLAND, ITALY AND W GERMANY) by holding Ctrl key.    """
        """ 11. Click "OK". """
        combo_item_list = ['ENGLAND', 'ITALY', 'W GERMANY']
        ia_ribbobj.create_slicer(1, 'COUNTRY', combo_item_list, 'small', 'ok', last_combo_item_no=5)
        
        
        """ 12. Verify it shows "Multiple" as an option.        """
        expected_list = ['Group 1', 'COUNTRY', 'Multiple']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 12: Verify it shows "Multiple" as an option')
        
        """ 13. Click "Run".                                    """
        ribbonobj.select_tool_menu_item('menu_run')
         
        """ 14. Verify the report is displayed with the selected countries.    """
        utillobj.switch_to_frame()
        ia_runobj.verify_table_data_set('table[summary="Summary"]', Test_Case_ID+'_Ds02.xlsx', 'Step 14: Verify the report data-set is displayed with the selected countries')
         
        """ 15. Click "IA" > "Save" > "C2227466" > click Save    """
        core_util_obj.switch_to_default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """ 16. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """ 17. Reopen fex using IA API: 'http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227466.fex&tool=report'        """
        utillobj.login_wf('mrid', 'mrpass')
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        utillobj.synchronize_with_visble_text(parent_id_css, 'RETAIL_COST', 190)
         
        """ 18. Verify Slicer is preserved > only ENGLAND, ITALY and W GERMANY should be displayed        """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 18.1: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 4, 'C2227466_Ds03.xlsx', 'Step 18.2: Verify report dataset')
        
        
        
if __name__ == '__main__':
    unittest.main()