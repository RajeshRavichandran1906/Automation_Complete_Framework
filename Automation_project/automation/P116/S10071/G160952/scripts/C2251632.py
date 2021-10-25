'''
Created on Jan 16, 2018

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc&group_id=160949
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2251632
TestCase Name : Verify Dashboard report, Checkbox lined up correctly (130924)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous, ia_run,visualization_ribbon,visualization_metadata
from common.lib import utillity

class C2251632_TestClass(BaseTestCase):

    def test_C2251632(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251632'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """        
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10071
        """
        utillobj.infoassist_api_login('document','ibisamp/car','P116/S10071_2', 'mrid', 'mrpass')
        parent_css="#resultArea"
        result_obj.wait_for_property(parent_css, 1,expire_time=50)
        """
            Step 02 : Add CAR and COUNTRY field in a report
                        Insert active control checkbox in a report
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(4) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=30)
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(5) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=30)     
        vis_ribbon_obj.select_ribbon_item('Insert', 'checkbox')
        time.sleep(3)
        vis_ribbon_obj.repositioning_document_component('5','1')
        vis_ribbon_obj.resizing_document_component('3', '1.5')
        """
            Step 03 : Right click the Checkbox and select Properties option
        """
        check_box_css="#Prompt_1"
        check_box_elem=self.driver.find_element_by_css_selector(check_box_css)
        utillobj.default_click(obj_locator=check_box_elem, click_option=1)
        time.sleep(2)
        utillobj.select_bipopup_list_item('Properties')
        time.sleep(2)
        """
            Step 04 : In Field dropdown box, select CAR and click Apply and OK
        """
        utillobj.select_combobox_item('comboSourceFields', 'CAR')
        apply_btn=self.driver.find_element_by_css_selector('#btnADPApply')
        utillobj.default_left_click(object_locator=apply_btn)
        time.sleep(5)
        ok_Btn=self.driver.find_element_by_css_selector('#btnADPOK img')
        utillobj.default_left_click(object_locator=ok_Btn)
        time.sleep(5)
        """
            Step 05 : Run the report and verify Values in checkbox are lined up correctly
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=3)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 05.01:  10of10records,Page1of1 Active Report. - page summary verification of table 1")
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+'_Ds01.xlsx', msg='Step 05.02 : Verify table')
        icon_css = "#checkbox_dPROMPT_1 > table > tbody > tr td:nth-child(1)"
        icon_elem = self.driver.find_elements_by_css_selector(icon_css)
        text_css = "#checkbox_dPROMPT_1 > table > tbody > tr td:nth-child(2)"
        text_elem = self.driver.find_elements_by_css_selector(text_css)
        for i in range(len(icon_elem)):
                icon_bottom_cord = utillobj.get_object_screen_coordinate(icon_elem[i], 'bottom_middle')
                icon_top_cord = utillobj.get_object_screen_coordinate(icon_elem[i], 'top_middle')
                text_middle_cord = utillobj.get_object_screen_coordinate(text_elem[i], 'middle')
                if int(text_middle_cord['y']) in range (int((icon_top_cord['y'])),(int(icon_bottom_cord['y']))):
                    status = True
                else:
                    status = False
        utillobj.asequal(status, True,'Step 05.03 : Verify alignment')
        time.sleep(5)
        """
            Step 06 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        

if __name__ == "__main__":
    unittest.main()