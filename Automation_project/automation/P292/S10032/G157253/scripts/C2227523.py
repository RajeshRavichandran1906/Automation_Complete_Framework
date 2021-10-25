'''
Created on Nov 24, 2017

@author: BM13368
Testcase Name :  Verify Query Pane context menus  
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227523
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon 
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2227523_TestClass(BaseTestCase):

    def test_C2227523(self):
        
        """
            Testcase variable
        """
        Test_Case_ID = "C2227523"
        
        """
            Class Objects
        """
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
        Step 02 : Double-click fields "CAR" and "SALES"
        """
        metaobj.datatree_field_click('CAR', 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='CAR', with_regular_exprestion=True)
        
        metaobj.datatree_field_click('SALES', 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='SALES', with_regular_exprestion=True)
        
        """
        Step 03 : Drag and drop "COUNTRY" into "Across" container in the Query Pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("COUNTRY", 1, 'Across', 0)
#         metaobj.datatree_field_click('COUNTRY', 1, 1, 'Across')
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='COUNTRY', with_regular_exprestion=True)
        
        """
        Verify query tree CAR is added under By, SALES is added under Sum and COUNTRY is added under Across
        """
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 03.01")
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 03.02")
        metaobj.verify_query_pane_field('Across', 'COUNTRY', 1, "Step 03.03")
        
        """
        Step 04 : Right-click "Report1 (car)" > Verify menu 
        Step 05 : Select "Print"
        """
        metaobj.querytree_field_click("Report (car)", 1, 1)
        a=['Rename', 'Sum', 'Print', 'Count', 'List']
        utillobj.select_or_verify_bipop_menu('Print', verify='true',expected_popup_list=a, msg='Step 05.01 Verify menu displayed')
        
        """
        Step 06 : Verify Query and Preview
        """
        metaobj.verify_query_pane_field('Print', 'SALES', 1, "Step 06.01: SALES is available underneath Print bucket")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 6, 4, 6,"C2227523_Ds01.xlsx")
        
        """
        Step 07 : Right-click COUNTRY in Across > Verify menu
        """
        metaobj.querytree_field_click("COUNTRY", 1, 1)
        a=['Filter Values...', 'Sort', 'Break', 'Visibility', 'Create Group...', 'Change Title...', 'Drill Down', 'Delete']
        utillobj.select_or_verify_bipop_menu('Delete', verify='true',expected_popup_list=a, msg='Step 07.01 Verify menu displayed')
        
        """
        Step 08 : Select > "Delete" > Verify Query and Preview
        """
        metaobj.verify_query_pane_field_available('Print', 'COUNTRY', 'Across', 'Step 08.01: Verify Query field is not available under Across bucket', availability=False)
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, "C2227523_Ds02.xlsx", 'Step 08.02: Verify report dataset')
        
        """
        Step 09 : Right-click SALES in Query > Verify menu 
        """
        metaobj.querytree_field_click("SALES", 1, 1)
        a=['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Edit Format', 'Drill Down', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a, msg='Step 09.01 Verify menu displayed')
        
        """
        Step 10 : Right-click "Print" > Verify menu > Select "New Parameter"
        """
        metaobj.querytree_field_click("Print", 1, 1)
        a=['New Parameter']
        utillobj.select_or_verify_bipop_menu('New Parameter', verify='true',expected_popup_list=a, msg='Step 10.01 Verify menu displayed')
        
        """
        Step 11 : Click SALES in Query > Drag SALES into "Parameter1" container
        """
        metaobj.drag_and_drop_query_items('SALES', 'Parameter1')
        metaobj.verify_query_pane_field('Parameter1', 'SALES', 1, "Step 11.01: SALES is available underneath Print bucket")
        
        """
        Step 12 : Right-click SALES under Parameter1 > Verify menu
        Step 13 : Select "Delete" > Verify Query and Preview
        """
        metaobj.querytree_field_click("SALES", 1, 1)
        a=['Aggregation Functions', 'Delete']
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Delete', verify='true', expected_popup_list=a, msg='Step 13.01 Verify menu displayed')
        ia_resultobj.verify_report_data_set('TableChart_1', 1, 1, "C2227523_Ds03.xlsx", 'Step 13.02: Verify report dataset')
       
        """
        Step 14 : Right-click "By" container in the Query > Verify menu
        """
        metaobj.querytree_field_click("By", 1, 1)
        a=['New Parameter']
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=a, msg='Step 14.01 Verify menu displayed')
        
        """
        Step 15 : Right-click "Across" container in the Query > Verify menu
        """
        metaobj.querytree_field_click("Across", 1, 1)
        a=['New Parameter']
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=a, msg='Step 15.01 Verify menu displayed')
        
        """
        Step 16 : Double-click DEALER_COST
        """
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        
        """
        Step 17 : Right-click DEALER_COST in Query > Sort > Sort > Descending
        """
        metaobj.querytree_field_click("DEALER_COST", 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Sort')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Sort')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Descending')
        time.sleep(0.5)
        
        """
        Step 18 : Verify Query and Preview
        """
        metaobj.verify_query_pane_field('By', 'DEALER_COST', 1, "Step 18.01 : Verify DEALER_COST is disabled under neath By query bucket", color='Trolley_Grey', font_style='italic')
        
        """
        Step 19 : Right-click CAR in Query > Select "Filter Values..."
        """
        metaobj.querytree_field_click("CAR", 1, 1, 'Filter Values...')
        time.sleep(0.5)
        
        """
        Step 20 : Click "Get Values > All" 
        Step 21 : Double-click value "JAGUAR"
        Step 22 : Click OK > OK
        """
        ia_ribbobj.create_constant_filter_condition('All',['JAGUAR'])
        utillobj.synchronize_with_visble_text("#qbFilterBox", "CAR", 30)
        
        """
        Step 23 : Verify Query and Preview
        """
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, "C2227523_Ds04.xlsx", 'Step 23.01: Verify report dataset')
        
        """
        Step 24 : Click "Save" > save as "C2227523" > Click "Save" 
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
        Step 25 : Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 26 : Reopen saved FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227523.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        
        """
        Step 27 : Verify Query, Filter, and Preview
        """
        metaobj.verify_query_pane_field('By', 'DEALER_COST', 1, "Step 27.01: Verify DEALER_COST is disabled under neath By query bucket", color='Trolley_Grey', font_style='italic')
        metaobj.verify_query_pane_field('By', 'CAR', 2, "Step 27.02: Verify CAR is added underneath By query bucket")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, "C2227523_Ds04.xlsx", 'Step 27:03: Verify report dataset')
                
        """
        Step 28 : Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()