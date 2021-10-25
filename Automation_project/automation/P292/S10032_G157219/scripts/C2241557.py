'''
Created on DEC 01, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2241557
TestCase Name = API > New > Alert
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_resultarea,wf_alert_assist
from common.lib.basetestcase import BaseTestCase

class C2241557_TestClass(BaseTestCase):

    def test_C2241557(self):
        
        Test_Case_ID = "C2241557"
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)  
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)  
        alertobj= wf_alert_assist.Wf_Alert_Assist(self.driver)

        """
            Step 01:Launch Alert Assist with IA API:
                    http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=Alert
        """
        alertobj.api_login()
        time.sleep(8)
 
        """
            Step 02:Verify Alert Assist is launched
        """
        alertobj.verify_aa_tree_item('Alert', "Step 02:verify tool menu item Alert Assist is launched")
         
        """
            Step 03:Right click on "Test" > WebFOCUS Test > baseapp/wf_reatil_lite > Open
        """
        alertobj.select_aa_tree_item('Test',1,'New', 'WebFOCUS Test')   
        utillobj.switch_to_window(1)    
        time.sleep(5)
        utillobj.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        time.sleep(5)
        parent_css="div[align='justify']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(2)
        """
            Step 04:Double click on fields "Cost of Goods" and "Product,Category"
            Verify the canvas.
        """
         
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(3) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=50)
        time.sleep(3)
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 7, 2, Test_Case_ID+'_DataSet_01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 02 : Verify report')        
 
        """
            Step 05:Click IA Globe > Exit > Yes to save prompt > OK
        """
        alertobj.select_aa_tool_menu_item("menu_exit")
        btn_yes=driver.find_element_by_id('btnYes')
        utillobj.default_left_click(object_locator=btn_yes)
        """
            Step 06:Right click on "Result" > New Report > Report > baseapp/wf_reatil_lite > Open
        """
        utillobj.switch_to_main_window()
        alertobj.select_aa_tree_item('Result',1,'New', 'New Report', 'Report')
        utillobj.switch_to_window(1)
        time.sleep(5)
        utillobj.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        parent_css="div[align='justify']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(2)
        
        """
            Step 07:Double click on fields "Cost of Goods" and "Product,Category"
                    Verify the canvas,
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(3) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=50)
        time.sleep(3)
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 02 : Verify report')       

        """
            Step 08:Click "Save" > Save As "C2241557" > Click Save
        """
        time.sleep(6)
        ribbonobj.select_tool_menu_item('menu_save')
        btn_ok=driver.find_element_by_css_selector("[id^='BiOptionPane'] [id^='BiButton'] div[class='bi-button-label']")
        utillobj.default_left_click(object_locator=btn_ok)
        time.sleep(3)
        ribbonobj.select_tool_menu_item("menu_exit")
        time.sleep(3)
        utillobj.switch_to_main_window()
        time.sleep(3)
        alertobj.select_aa_tool_menu_item("menu_save_as")
        utillobj.ibfs_save_as(Test_Case_ID) 
        time.sleep(5)   
        """
            Step 09:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main() 
