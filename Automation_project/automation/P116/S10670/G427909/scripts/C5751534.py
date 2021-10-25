'''
Created on Jan 4, 2019

@author: Vpriya

Testsuite =  http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=427909&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/5751534
TestCase Name = Verify that reopening Document does not affect "Include ALL" option
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import chart
from common.wftools import document
from common.wftools import visualization
from common.pages import webfocus_editor
from common.lib import utillity

class C5751534_TestClass(BaseTestCase):

    def test_C5751534(self):
        
        """
            TESTCASE VARIABLES
        """
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        chart_obj=chart.Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        MEDIUM_WAIT=45
        webfocus_editor_obj=webfocus_editor.WebfocusEditor(self.driver)
        window_css="div[class*='bi-window active window ']"
        folder_name="P116_S10670/G427909"
        value_search="ARFILTER_SHOWALL='ON'"
        
        """
        Step 01:Execute the following URl to Launch Document
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS10071_1%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='Document', master='ibisamp/ggsales')
         
         
        """
        Step 02:Add Category,Product, Unit Sales to get a report
        """
        report_obj.double_click_on_datetree_item( 'Category',1)
        field_1_css="#queryTreeColumn tbody>tr:nth-child(4)"
        report_obj.wait_for_visible_text(field_1_css, 'Category',MEDIUM_WAIT)
        
        report_obj.double_click_on_datetree_item( 'Product',1)
        field_2_css="#queryTreeColumn tbody>tr:nth-child(5)"
        report_obj.wait_for_visible_text(field_2_css, 'Product',MEDIUM_WAIT)
        
        report_obj.double_click_on_datetree_item( 'Unit Sales',1)
        field_3_css="#queryTreeColumn tbody>tr:nth-child(3)"
        report_obj.wait_for_visible_text(field_3_css, 'Unit Sales',MEDIUM_WAIT)
        
        """
        Step 03:Now, select Drop down button from 'Insert' tab
        """
        
        vis_obj.select_ribbon_item('Insert','Drop_Down')
        doc_obj.drag_drop_document_component("#Prompt_1", "#TableChart_1", 230,0)
        
        
        """
        Step 04:Right click on Drop down button select properties
        """
        
        doc_obj.choose_right_click_menu_item_for_prompt("#Prompt_1", "Properties")
        report_obj.wait_for_number_of_element(window_css,1,MEDIUM_WAIT)
        
        """
        Step05:In Active Dashboard Properties assign UNIT SALES in 'Field'. Make sure Include All is checked already and Condition is Equal to.
        """
        """
        Step 06:Click Ok.
        """
        source={'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        targets ={'verify_target_name':['Report1']}
        doc_obj.customize_active_dashboard_properties(source=source, targets=targets, msg="Step 3:", btn_type='ok')
    
        """
        Step 07:Save and close the report as AHTML as AR-AD-09a.fex.
        """
        chart_obj.save_as_chart_from_menubar('AR-AD-09a')
        chart_obj.api_logout()
        
        """
        Step 08:Now reopen the saved document using following URL
        http://machine:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS10071_1%2FAR-RP-09a.fex
        """
        chart_obj.edit_fex_using_api_url(folder_name, 'Document', 'AR-AD-09a','mrid','mrpass')
        
        
        """
        Step 09:Right click on dropdown and select properties
        """
        doc_obj.choose_right_click_menu_item_for_prompt("#Prompt_1", "Properties")
        
        """
        Step 10:"Include All" should be checked on reopening the saved report
        """
        source={'verify_includeall':True}
        doc_obj.customize_active_dashboard_properties('None', source, 'None')
       
        
        """
        Step 11:Verify Include All gets generated in the syntax (ARFILTER_SHOWALL=ON)
        http://machine:port/alias/tools/portlets/resources/markup/sharep/SPEditorBoot.jsp?folderPath=IBFS%253A%252FWFC%252FRepository%252FP116/S10071_1&description=AR-AD-09&itemName=AR-AD-09.fex&isReferenced=true&type=items
        """
        webfocus_editor_obj.invoke_fex_using_text_editor(folder_name, 'AR-AD-09a')
        whole_text=self.driver.find_element_by_css_selector("#bipEditorArea")
        text_value=whole_text.get_attribute('value').strip()
        utill_obj.asin(value_search,text_value,"Step:11 verify include ALL option")



if __name__ == '__main__':
    unittest.main()