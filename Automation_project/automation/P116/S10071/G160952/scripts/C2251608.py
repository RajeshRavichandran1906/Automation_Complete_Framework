'''
Created on Jan 16, 2018

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc&group_id=160949
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2251608
TestCase Name : Verify that reopening Document does not affect "Include ALL" option
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,visualization_ribbon,visualization_metadata,wf_legacymainpage
from common.lib import utillity

class C2251608_TestClass(BaseTestCase):

    def test_C2251608(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        legacy_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """        
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/GGSales&item=IBFS%3A%2FWFC%2FRepository%2FS10071
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 60)
        """
            Step 02 : Select Category, Product,Unit Sales to get a report        
        """ 
        metaobj.datatree_field_click("Category", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(4) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        metaobj.datatree_field_click("Product", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(5) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(3) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        """
            Step 03 : select Drop down button from 'Insert' tab        
        """
        vis_ribbon_obj.select_ribbon_item('Insert', 'drop_down')
        time.sleep(3)
        vis_ribbon_obj.repositioning_document_component('5', '1')
        """
            Step 04 : Right click on Drop down button select properties
                        In Active Dashboard Properties ssign UNIT SALES in 'Field'. Make sure Include All is checked already and Condition is Equal to.
                        Click Ok.
        """
        result_obj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        time.sleep(5)
        source={'select_field':'Unit Sales', 'verify_condition':'Equal to','includeall':'no' }
        result_obj.customize_active_dashboard_properties('None', source, 'None')
        """
            Step 05 : Save and close the report as AHTML as AR-AD-09a.fex.        
        """
        vis_ribbon_obj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as('AHTML as AR-AD-09a')
        time.sleep(8)
        
        """
            Step 06 :  Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp     
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 07: Open the report again in IA (Edit with - Info Assist), and right click on dropdown, and select properties. 
                        "Include All" should be checked on reopening the saved report
        """
        utillobj.infoassist_api_edit('AHTML_as_AR-AD-09a','document', 'P116/S10071_1',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        result_obj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        time.sleep(5)
        source={'verify_field':'Unit Sales','includeall':'no'}
        result_obj.customize_active_dashboard_properties('None', source, 'None')
        utillobj.wf_logout()
        """
            Step 08: Open the report again in IA (Edit with - Text Editor) 
                       Verify Include All gets generated in the syntax (ARFILTER_SHOWALL=ON)
        """
        utillobj.login_wf('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#PortalResourcevBOX table tr td", 'Domains', 65)
        legacy_obj.select_menu('P116->S10071_1->AHTML as AR-AD-09a', 'Edit With...->Text Editor')
        utillobj.synchronize_with_number_of_element("#bipEditor [class*='active'] #bipEditorArea", 1, 25)
        expected_syntax_list=["ARFILTER_SHOWALL='ON'"]
        texteditor_text = self.driver.find_element_by_css_selector("#bipEditor [class*='active'] #bipEditorArea").get_attribute('value')
        for syntax in expected_syntax_list :
            if syntax in texteditor_text :
                status=True
            else :
                status=False
                break
        utillity.UtillityMethods.asequal(self,True,status,"Step 8.1 : Verify text editor syntax.")
        elem = self.driver.find_element_by_css_selector("#bipEditor [class*='active'] [class*='window'][class*='close']")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(2)
        """
            Step 09 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        

if __name__ == "__main__":
    unittest.main()