'''
Created on Nov 13, 2017

@author: BM13368
TestCase_Name : Verify Sample Data 
Testcase_ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227586
'''
import unittest, time, re
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C2227586_TestClass(BaseTestCase):

    def test_C2227586(self):
        
        Test_Case_ID = "C2227586"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 02 : Click "Use Sample Data" in the Home Tab ribbon
        """
        vis_ribbon_obj.select_ribbon_item('Home', 'Use_Sample_Data')
        time.sleep(2)
        
        """
            Step 03 : Double click fields "Product,Category" and "Cost of Goods"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        """
            Step 04 : Drag "Sales_Related->Trasaction Date, Simple" > "Sale,Year" into the Across container in the Query pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Year", 1, 'Across', 0)
#         metaobj.datatree_field_click("Sale,Year", 1, 0,'Across')
        time.sleep(4)
        
        """
            Step 05 : Verify sample data is displayed in the Preview
        """
#         ia_resultarea_obj.create_across_report_data_set('TableChart_1', 3, 11, 3, 11, "C2227586_Ds01.xlsx")
        ia_resultarea_obj.verify_across_report_data_set('TableChart_1', 3, 11, 3, 11, "C2227586_Ds01.xlsx", "Step 05.01: Verify report data")
#         ia_resultarea_obj.compare_across_report_data_set('TableChart_1', 3, 11, 3, 11, "C2227586_Ds01.xlsx")
        """
            Step 06 : Click "Save" in the toolbar > save as "C2227586" > Click Save
        """
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """
            Step 07 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.wf_logout()
#         utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 08 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227586.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        """
            Step 09 : Verify Preview
        """
#         ia_resultarea_obj.create_across_report_data_set('TableChart_1', 3, 11, 3, 11, "C2227586_Ds01.xlsx")
        ia_resultarea_obj.compare_across_report_data_set('TableChart_1', 3, 11, 3, 11, "C2227586_Ds01.xlsx")
        """
            Step 10 : Verify "Use Sample Data" button remains selected
        """
        elem=self.driver.find_element_by_css_selector("#HomeSampleData")
        status=True if bool(re.match('.*-checked.*', elem.get_attribute("class"))) else False
        utillobj.asequal(True, status, "Step 10.01: Verify canvas live preview")
        """
            Step 11 : Click "Data from Source" in the Home Tab ribbon > Verify warning message is displayed 
            Step 12: Check off "Do not show this message again" > Click OK
        """
        vis_ribbon_obj.select_ribbon_item('Home', 'Data_from_Source')
        time.sleep(2)
        css="#promptDlg"
        popup_txt_css="#chkBox #doNotShow"
        utillobj.verify_popup(css, "Step 12.01: Verify popup message", popup_text_css=popup_txt_css, popup_text='Do not show this message again')
        check_css=self.driver.find_element_by_css_selector(css+ " "+popup_txt_css)
        utillobj.click_on_screen(check_css, 'left', 0)
        time.sleep(0.5)
        btncss_obj=self.driver.find_element_by_css_selector("#btnOK")
        utillobj.click_on_screen(btncss_obj, 'middle', 0)
        time.sleep(10)
        """
            Step 13 : Verify live data is displayed on Preview
        """
#         ia_resultarea_obj.create_across_report_data_set('TableChart_1', 3, 7, 3, 7, "C2227586_Ds02.xlsx")
        ia_resultarea_obj.compare_across_report_data_set('TableChart_1', 3, 7, 3, 7, "C2227586_Ds02.xlsx")
        
        """
            Step 14 : Click "Use Sample Data" in the Home Tab ribbon
        """
        vis_ribbon_obj.select_ribbon_item('Home', 'Use_Sample_Data')
        time.sleep(2)
        """
            Step 15 : Click "Data from Source" in the Home Tab ribbon > Verify warning message is NOT displayed this time
        """
        vis_ribbon_obj.select_ribbon_item('Home', 'Data_from_Source')
        time.sleep(2)
        utillobj.verify_object_visible('#promptDlg', False, "Step 15.01: Verify popup message is NOT displayed")
        """
            Step 16 : Logout and do not save changes:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(2)

if __name__ == "__main__":
    unittest.main()