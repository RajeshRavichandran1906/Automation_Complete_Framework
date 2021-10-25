'''
Created on Nov 21, 2017

@author: BM13368
Testcase Name :  Verify Data Pane context menus 
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227522
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, ia_ribbon, ia_resultarea 
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2227522_TestClass(BaseTestCase):

    def test_C2227522(self):
        
        Test_Case_ID = "C2227522"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
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
            Step 02 : Right-click "CAR" in the Data pane > Verify menu displayed
        """
        metaobj.datatree_field_click('CAR', 1, 1)
        a=['Sum', 'Sort', 'Create Group...', 'Across', 'Filter', 'Slicers']
        utillobj.select_or_verify_bipop_menu('Slicers', verify='true',expected_popup_list=a, msg='Step 02:01 Verify menu displayed')
        """
            Step 03 : Select "Slicers -> New Group"
        """
        utillobj.select_or_verify_bipop_menu('New Group')
        """
            Step 04 : Verify Slicer "Group 1" is created in Slicers Tab
        """
        expected_list = ['Group 1', 'CAR']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 04:01: Group 1 slicer is available')
        """
            Step 05 : Click on the CAR dropdown menu > Verify CAR values are displayed
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'CAR')
        expected_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 05:01: Verify CAR values are displayed")
        """
            Step 06 : Click Cancel
        """
        ia_ribbobj.close_slicer_dialog('cancel')
        """
            Step 07 : Right-click "CAR" in the Data pane > Select "Create Group..."
        """
        metaobj.datatree_field_click('CAR', 1, 1,'Create Group...')
        
        """
            Step 08 : Verify Group dialog > Click Cancel
        """
        expected_element_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        metaobj.verify_fields_in_ia_groupdialog(expected_element_list, close_button='cancel', msg='Step 08: Verify Group dialog')
        time.sleep(8)
        
        """
            Step 09 : Right-click "SALES" in the Data pane > Verify menu displayed
        """
        metaobj.datatree_field_click('SALES', 1, 1)
        a=['Sum', 'Create Bins...', 'Sort', 'Across', 'Filter', 'Slicers']
        utillobj.select_or_verify_bipop_menu('Filter', verify='true',expected_popup_list=a, msg='Step 09:01 Verify menu displayed')
        """
            Step 10 : Select "Filter" > Verify dialog displayed
        """
        css="#dlgWhere_btnCancel img"
        resultobj.wait_for_property(css, 1)
        time.sleep(4)
        ia_ribbobj.verify_join_filter_Condition("SALES Equal to <Value>", "Step 10:01: Verify filter condition")
             
        """
            Step : 11 : Click Cancel > Cancel > Click "No" to save prompt
        """
        try:
            parent_elem=driver.find_element_by_css_selector("#wndWhereValuePopup_btnCancel img")
            utillobj.click_on_screen(parent_elem, 'middle', 0)
        except:
            pass
        time.sleep(1)
        parent_elem=driver.find_element_by_css_selector("#dlgWhere_btnCancel img")
        utillobj.click_on_screen(parent_elem, 'middle', 0)
        time.sleep(1)
        utillobj.click_dialog_button("div[id^='BiDialog']", 'No')
        time.sleep(1)
        """
            Step 12: Right-click "SALES" in the Data pane > Select "Slicers -> Existing Group"
        """
        metaobj.datatree_field_click('SALES', 1, 1, 'Slicers', 'Existing Group')
        
        """
            Step 13 : Verify "Add Slicer" dialog > Click OK
        """
        ia_ribbobj.select_buttons_in_add_slicer_dialog("Ok")
        """
            Step 14 : Verify SALES slicer in Group1
        """
        expected_list = ['Group 1', 'CAR', 'SALES']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 14:01: "SALES" has been added to "Group 1"')
        """
            Step 15 : Click on the SALES dropdown menu > Verify SALES values are displayed
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'SALES')
        expected_list=['0', '4800', '7800', '8900', '8950', '12000', '12400', '13000']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 15:01: Verify CAR values are displayed")
        """
            Step 16 : Click Cancel
        """
        ia_ribbobj.close_slicer_dialog('cancel')
        time.sleep(2)
        """
            Step 17 : Right-click "SALES" in the Data pane > Select "Sum"
        """
        metaobj.datatree_field_click('SALES', 1, 1, 'Sum')
        time.sleep(0.5)
        """
            Step 18 : Right-click "COUNTRY" in the Data pane > Select "Across"
        """
        metaobj.datatree_field_click('COUNTRY', 1, 1, 'Across')
        time.sleep(0.5)
        
        """
            Step 19 : Right-click "CAR" in the Data pane > Select "Sort"
        """
        metaobj.datatree_field_click('CAR', 1, 1, 'Sort')
        time.sleep(0.5)
        
        """
            Step 20 : # Verify Query pane and Preview
            Verify SALES is added  underneath Sum querynode
            Verify COUNTRY is added  underneath Across
            Verify CAR is added Sort query
        """
        metaobj.verify_query_pane_field('Sum', 'SALES', 1, "Step 20:01: SALES is added  underneath Sum query bucket")
        metaobj.verify_query_pane_field('Across', 'COUNTRY', 1, "Step 20:02: Verify COUNTRY is added  underneath Across")
        metaobj.verify_query_pane_field('By', 'CAR', 1, "Step 20:03: Verify CAR is added  underneath By")
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 6, 5, 6,Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.compare_across_report_data_set('TableChart_1', 2, 6, 5, 6,Test_Case_ID+"_Ds01.xlsx")
        
        """
            Step 21 : Logout and disregard changes
            Logout and disregard changes:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()