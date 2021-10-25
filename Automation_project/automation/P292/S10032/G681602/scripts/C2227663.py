'''
Created on Mar 22, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227663
Test case Name =  Prompt Type - edit type from Multiple to List (Single Select)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization


class C2227663_TestClass(BaseTestCase):

    def test_C2227663(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227663'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual = Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        visual.wait_for_visible_text("#pfjTableChart_1", "Drop", 180)

        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        metaobj.datatree_field_click("Cost of Goods",2,1)
        visual.wait_for_visible_text("#queryTreeWindow", 'Cost of Goods', 60)
        
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        visual.wait_for_visible_text("#queryTreeWindow", 'Product,Category', 60)
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        Step 05: Click OK
        """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        visual.wait_for_visible_text("#avFilterOkBtn", "OK", 100)
        metaobj.create_visualization_filters("alpha")        
         
        """
        Step 06: Click Prompt menu in the upper right corner
        Step 07: Select "List (Single Select)"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.change_prompt_options("1","List (Single Select)")
         
        """
        Step 08: Verify Canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c: Verify first bar color")
        time.sleep(5)
        
        """
        Step 09: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(25)
        visual.switch_to_new_window()
        
        """
        Step 10: Verify output with no prompt
        """
        visual.wait_for_visible_text("#MAINTABLE_1", "Product", 180)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(25)
        
        """
        Step 11: Close the output window
        """
        visual.switch_to_previous_window()
        time.sleep(15)
        visual.wait_for_visible_text("#MAINTABLE_wbody1", "Product", 120)
        
        """
        Step 12: Click Save
        Step 13: Click Save in the toolbar > Save as "C2227663" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        visual.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel", 100)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 15: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227663.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        
        """
        Step 16: Verify Canvas
        """
        visual.wait_for_visible_text("#MAINTABLE_wbody1", "Product", 120)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        time.sleep(20)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()
