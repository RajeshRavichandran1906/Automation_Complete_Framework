'''
Created on Nov 14, 2017

@author: BM13368
Testcase_ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235435
Testcase_Name : Verify Changing the field Title
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase


class C2235435_TestClass(BaseTestCase):

    def test_C2235435(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2235435'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032 
        """
        utillobj.infoassist_api_login('report','new_retail/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        """
            Step 02 : Double click "Cost of Goods" and "Product,Category" 
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        coln_list = ['Product']
        resultobj.verify_report_titles_on_preview(1, 1, "TableChart_1", coln_list, "Step 02:00: Verify Canvas column titles ")
        time.sleep(2)
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 02:01: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 7, 2, "C2235435_Ds00.xlsx", "Step 02:02 verify preview data")
         
        """
            Step 03 : Right-click on "Product,Category" in the Query pane > Select "Change Title..."
        """
        metaobj.querytree_field_click('Product,Category', 1, 1, 'Change Title...')
        time.sleep(3)
        """
            Step 04 : Verify dialog
        """
        btn_css = "div[id^='BiDialog'] [class*='window-active']"
        utillobj.verify_object_visible(btn_css, True, "Step 04:01: Verify Dialog is visible")
        edit_title_obj=self.driver.find_element_by_css_selector(btn_css)
        actual_value=edit_title_obj.find_element_by_css_selector("input").get_attribute('value')
        utillobj.asequal(actual_value, 'Product,Category', "Step 04:02: Verify Edit Title text value appears.")
        """
            Step 05 : Change Title to "Product" > Click OK
        """
        text_field = edit_title_obj.find_element_by_css_selector("input")
        utillobj.set_text_field_using_actionchains(text_field, 'Product')
        utillobj.click_dialog_button(btn_css,"OK")
        time.sleep(1)
        """
            Step 06 : Verify Preview displays "Product" title, Query pane remains unchanged
        """
        coln_list = ['Product', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 06:00: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 7, 2, "C2235435_Ds01.xlsx", "Step 06:01 verify preview data")
        metaobj.verify_query_pane_field('By', 'Product,Category', 1, "Step 06:02: Verify Preview displays Product title, Query pane remains unchanged")
          
        """
            Step 07 : Right-click on "Cost of Goods" in the Preview > Select "Change Title..."
        """
        metaobj.querytree_field_click('Cost of Goods', 1, 1, 'Change Title...')
        time.sleep(3)
        """
            Step 08 : Verify dialog
        """
        btn_css = "div[id^='BiDialog'] [class*='window-active']"
        utillobj.verify_object_visible(btn_css, True, "Step 08:01: Verify Dialog is visible")
        edit_title_obj=self.driver.find_element_by_css_selector(btn_css)
        actual_value=edit_title_obj.find_element_by_css_selector("input").get_attribute('value')
        utillobj.asequal(actual_value, 'Cost of Goods', "Step 08:02: Verify Edit Title text value appears.")
        """
            Step 09 : Change Title to "Costs" > Click OK
        """
        text_field = edit_title_obj.find_element_by_css_selector("input")
        utillobj.set_text_field_using_actionchains(text_field, 'Cost')
        utillobj.click_dialog_button(btn_css,"OK")
        time.sleep(5)
        """
            Step 10 : Verify Preview displays "Costs" title, Query pane remains unchanged
        """
        coln_list = ['Product', 'Cost']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 10:00: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 7, 2, "C2235435_Ds02.xlsx", "Step 10:01 verify preview data")
        metaobj.verify_query_pane_field('Sum', 'Cost of Goods', 1, "Step 10:02: Verify Preview displays Cost of Goods, Query pane remains unchanged")
        """
            Step 11: Click Run > Verify output
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        ia_run_obj.verify_table_data_set("table[summary='Summary']", "C2235435_Ds03.xlsx", "Step 11:01 verify runtime data")
          
        """
            Step 12 : Click "Save" > save as "C2235435" > Click Save
        """
        utillobj.switch_to_default_content(pause=1)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """
            Step 13 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 14 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235435.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        """
            Step 15 : Verify Query pane and Preview
        """
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 7, 2, "C2235435_Ds02.xlsx", "Step 15:01 verify preview data")
        metaobj.verify_query_pane_field('Sum', 'Cost of Goods', 1, "Step 15:02: Verify Preview displays Cost title, Query pane remains unchanged")
        metaobj.verify_query_pane_field('By', 'Product,Category', 1, "Step 15:03: Verify Preview displays Product title, Query pane remains unchanged")
        """
            Step 16 : Right-click on "Costs" column in the Preview > Select "Change Title..."
        """
        ia_resultarea_obj.select_field_on_canvas('TableChart_1',2, click_type=1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Change Title...')
        time.sleep(2)
         
        """
            Step 17 : Remove "Costs" title
        """
        btn_css = "div[id^='BiDialog'] [class*='window-active']"
        utillobj.verify_object_visible(btn_css, True, "Step 17:01: Verify Dialog is visible")
        edit_title_obj=self.driver.find_element_by_css_selector(btn_css)
        text_field = edit_title_obj.find_element_by_css_selector("input").clear()
              
        """
            Step 18 : Click OK after removing title
        """
        utillobj.click_dialog_button(btn_css,"OK")
        time.sleep(5)
          
        """
            Step 19 : Verify default title is restored
        """
        coln_list = ['Product', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 19:00: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 7, 2, "C2235435_Ds01.xlsx", "Step 19:01 verify preview data")
        """
            Step 20 : Logout, do not save changes:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()