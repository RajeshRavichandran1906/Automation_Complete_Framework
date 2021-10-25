'''
Created on DEC 01, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2241557
TestCase Name = API > New > Alert
'''
import unittest
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon,ia_resultarea,wf_alert_assist
from common.lib.basetestcase import BaseTestCase

class C2241557_TestClass(BaseTestCase):

    def test_C2241557(self):
        
        TestCase_ID = 'C2241557'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)  
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)  
        alertobj= wf_alert_assist.Wf_Alert_Assist(self.driver)

        """
            Step 01 : Launch Alert Assist with IA API:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=Alert
        """
        alertobj.api_login()
        utillobj.synchronize_with_visble_text("#aaTree table>tbody>tr:first-child", 'Alert', 60)
 
        """
            Step 02 : Verify Alert Assist is launched
        """
        alertobj.verify_aa_tree_item('Alert', "Step 02.01 : verify tool menu item Alert Assist is launched")
         
        """
            Step 03 : Right click on "Test" > WebFOCUS Test > baseapp/wf_reatil_lite > Open
        """
        alertobj.select_aa_tree_item('Test',1,'New', 'TIBCO WebFOCUS Test')   
        utillobj.switch_to_window(1)    
        utillobj.synchronize_with_visble_text("#IbfsOpenFileDialog7_btnOK", 'Open', 40)
        utillobj.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(2)", 'Sum', 30)
        
        """
            Step 04 : Double click on fields "Cost of Goods" and "Product,Category"
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table tr:nth-child(3) td", 'Cost of Goods', 30)
        
        metaobj.datatree_field_click('Product,Category', 2, 0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table tr:nth-child(5) td", 'Product,Category', 30)
        
        """
            Step 04.1 : Verify the canvas,
        """
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 7, 2, Test_Case_ID+'_DataSet_01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,TestCase_ID+'_DataSet_01.xlsx','Step 04.01 : Verify report')        
 
        """
            Step 05 : Click IA Globe > Exit > Yes to save prompt > OK
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        utillobj.synchronize_with_visble_text("#saveAllDlg #btnYes", 'Yes', 8)
        
        btnYes = self.driver.find_element_by_id('btnYes')
        utillobj.default_left_click(object_locator=btnYes)
        utillobj.switch_to_window(0)
        
        """
            Step 06 : Right click on "Result" > New Report > Report > baseapp/wf_reatil_lite > Open
        """
        alertobj.select_aa_tree_item('Result',1,'New', 'New Report', 'Report')
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_visble_text("#IbfsOpenFileDialog7_btnOK", 'Open', 40)
        utillobj.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(2)", 'Sum', 30)
        
        """
            Step 07 : Double click on fields "Cost of Goods" and "Product,Category"
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table tr:nth-child(3) td", 'Cost of Goods', 20)
        
        metaobj.datatree_field_click('Product,Category', 2, 0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table tr:nth-child(5) td", 'Product,Category', 20)
        
        """
            STEP 07.1 : Verify the canvas
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,TestCase_ID+'_DataSet_01.xlsx','Step 07.01 : Verify the canvas')       

        """
            Step 08 : Click IA Globe > Exit > Yes to save prompt > OK
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        utillobj.synchronize_with_visble_text("#saveAllDlg #btnYes", 'Yes', 8)
        
        btnYes = self.driver.find_element_by_id('btnYes')
        utillobj.default_left_click(object_locator=btnYes)
        utillobj.switch_to_window(0)
        
        """
            STEP 09 : Click "Save" > Save As "C2241557" > Click Save
        """
        alertobj.select_top_toolbar_item('toptoolbar_save')
        utillobj.ibfs_save_as(TestCase_ID)
           
        """
            Step 09 : Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main() 
