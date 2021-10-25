'''
Created on Nov 10, 2017

@author: BM13368
Testcase_Name : Verify Query view
Testcase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2235375
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, ia_ribbon, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2235375_TestClass(BaseTestCase):

    def test_C2235375(self):
        
        Test_Case_ID = "C2235375"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
        """ 
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','new_retail/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        """
            Step 02 : Click "Query" in the Home Tab ribbon
        """
        vis_ribbon_obj.select_ribbon_item('Home', 'Query')
        time.sleep(8)
        
        """
            Step 03 : Verify canvas (with no live Preview)
        """
        elem=self.driver.find_element_by_css_selector("#TableChart_1")
        act=elem.is_displayed()
        utillobj.asequal(act, False, "Step 03: Verify canvas live preview")
        """
            Step 04 : Double click fields "Product,Category" and "Cost of Goods"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        """
            Step 05 : Drag "Product,Category" from "By" container to the Filter panel
        """
        metaobj.querytree_field_click('Product,Category', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Filter Values...')
        time.sleep(5)
         
        """
            Step 06 : Verify Filter dialog is opened for "Product,Category" and "By" container still shows "Product,Category" 
        """
        filter_condition_list="Product,Category Equal to <Value>"
        ia_ribbonobj.verify_join_filter_Condition(filter_condition_list, "Step 06: Verify filter dialog is opened for Product, Category")
         
        """
            Step 07 : Click on the Type dropdown in the Filter dialog > Select "Parameter"
            Step 08 : Click OK > OK
        """
        ia_ribbonobj.create_parameter_filter_condition('dummy','dummy')
        """
           Step 09: Verify Query and Filter panel 
        """
        metaobj.verify_query_pane_field('By', 'Product,Category', 1, "Step 09::01: Verify Product, Category is visible underneath By")
        metaobj.verify_query_pane_field('Sum', 'Cost of Goods', 1, "Step 09::02: Verify Cost of Goods is visible underneath Sum")
        metaobj.verify_filter_pane_field('Product,Category Equal to Simple Parameter (Name: PRODUCT_CATEGORY)', 1, "Step 09:03 Verify the filter pane")
        """
           Step 10 : Click "IA" menu > "Save" > save as "C2227586" > Click Save
        """
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """
            Step 11: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 12: Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227586.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        """
            Step 13: Verify Query View
        """
        metaobj.verify_query_pane_field('By', 'Product,Category', 1, "Step 13::01: Verify Product, Category is visible underneath By")
        """
            Step 14 : Logout and do not save changes:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
 
if __name__ == "__main__":
    unittest.main()