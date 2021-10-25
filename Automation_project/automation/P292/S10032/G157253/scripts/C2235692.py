'''
Created on Nov 24, 2017

@author: BM13368
TestCase Name : Verify drag/drop to Query and Preview
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/2235692
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon 
from common.lib import utillity  
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase

class C2235692_TestClass(BaseTestCase):

    def test_C2235692(self):
        
        Test_Case_ID = "C2235692"
        
        report_ = Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        """
            Step 02 : Drag "CAR" from Data pane into the Query pane > By
        """
        metaobj.datatree_field_click('CAR', 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'CAR', 30)
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 02:01: ")
        
        """
            Step 03 : Drag "COUNTRY" from Data pane into the Query pane > Across
        """
        metaobj.datatree_field_click('COUNTRY', 1, 1, 'Across')
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'COUNTRY', 30)
        metaobj.verify_query_pane_field('Across', 'COUNTRY', 1, "Step 03:01:")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 2, 2, "C2235692_Ds01.xlsx")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 2, 2, 2, "C2235692_Ds01.xlsx")
        """ 
            Step 04 : Drag "SALES" from Data pane into the Query pane > Sum
        """
        metaobj.datatree_field_click('SALES', 1, 1, 'Sum')
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'SALES', 30)
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 04:01: ")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 2, 2, "C2235692_Ds02.xlsx")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 2, 2, 2,"C2235692_Ds02.xlsx")
        
        """ 
            Step 05 : Drag "COUNTRY" from Data pane into the Filter pane
        """
        metaobj.datatree_field_click('COUNTRY', 1, 1, 'Filter')
        time.sleep(1)
        parent_css="#dlgWhere"
        resultobj.wait_for_property(parent_css, 1)
                
        """
            Step 06 : Click on the "Value:" input area > Type ENGLAND
            Step 07 : Click the top >> button to move value to the right panel
            Step 08: Click OK > OK
        """
        ia_ribbobj.create_constant_filter_condition_for_textfield('ENGLAND')
        utillobj.synchronize_with_visble_text('#qbFilterBox table>tbody', 'ENGLAND', 30)
        
        """
            Step 09: Verify Filter pane and Preview
        """
        metaobj.verify_filter_pane_field('COUNTRY Equal to ENGLAND', 1, "Step 09 : Verify Filter pane")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 2, 2, "C2235692_Ds03.xlsx")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 2, 2, 2,"C2235692_Ds03.xlsx")
        
        """ 
            Step 10: Drag "CAR" from Query pane into Filter pane
        """
        metaobj.querytree_field_click('CAR', 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Filter Values...')
        
        """ 
            Step 11: Verify dialog
        """
        parent_css="#dlgWhere"
        resultobj.wait_for_property(parent_css, 1)
        
        """ 
            Step 12: Click on the "Value:" input area > Type JAGUAR
            Step 13: Click the top >> button to move value to the right panel
            Step 14: Click OK > OK
        """
        ia_ribbobj.create_constant_filter_condition_for_textfield('JAGUAR',rownum=3)
        utillobj.synchronize_with_visble_text('#qbFilterBox table>tbody', 'JAGUAR', 30)
        
        """  
            Step 15: Verify Filter pane and Preview
        """
        metaobj.verify_filter_pane_field('CAR Equal to JAGUAR', 2, "Step 15: Verify Filter pane and Preview")
        """
            Step 16: Drag "MODEL" from Data pane into Preview
        """
        metaobj.datatree_field_click('MODEL', 2, 1)
        time.sleep(4)
        """ 
            Step 17: Verify Query and Preview
        """
        metaobj.verify_query_pane_field('By', 'MODEL', 2, "Step 17:01: Verify MODEL is added underneath By bucket")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 3, 1, 3, "C2235692_Ds04.xlsx")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 3, 1, 3,"C2235692_Ds04.xlsx")
        """ 
            Step 18: Drag "DEALER_COST" from Data pane into Preview
        """
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        """ 
            Step 19: Verify Query and Preview
        """
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 19:01: Verify SALES is added underneath By bucket")
        metaobj.verify_query_pane_field('Sum', 'DEALER_COST', 2, "Step 19:02: Verify DEALER_COST is added underneath By bucket")
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 19:03: Verify CAR is added underneath By bucket")
        metaobj.verify_query_pane_field('By', 'MODEL', 2, "Step 19:04: Verify MODEL is added underneath By bucket")
        metaobj.verify_query_pane_field('Across', 'COUNTRY', 1, "Step 19:05: Verify COUNTRY is added underneath Across bucket")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 3, 2, 3, "C2235692_Ds05.xlsx")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 3, 2, 3, "C2235692_Ds05.xlsx")
        """ 
            Step 20: Click "IA" > "Save" > save as "C2235692" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        """  
            Step 21: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """  
            Step 22: Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2235692.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 23: Verify Query, Filter and Preview
        """
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 23:01: Verify SALES is added underneath By bucket")
        metaobj.verify_query_pane_field('Sum', 'DEALER_COST', 2, "Step 23:02: Verify DEALER_COST is added underneath By bucket")
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 23:03: Verify CAR is added underneath By bucket")
        metaobj.verify_query_pane_field('By', 'MODEL', 2, "Step 23:04: Verify MODEL is added underneath By bucket")
        metaobj.verify_query_pane_field('Across', 'COUNTRY', 1, "Step 23:05: Verify COUNTRY is added underneath Across bucket")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 4, 4, 4, "C2235692_Ds03.xlsx")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 3, 2, 3, "C2235692_Ds05.xlsx")
        """ 
            Step 24: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()