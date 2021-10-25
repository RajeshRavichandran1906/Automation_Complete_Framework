'''
Created on Nov 29, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227557
TestCase Name = Verify promoting Chart to Document mode
'''

import unittest, time
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea

class C2227557_TestClass(BaseTestCase):

    def test_C2227557(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227557'
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """   
        Step 01: Launch IA Chart mode:http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS1003 
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 g.legend path[class^='legend-markers']", 5, expire_time=25)
        time.sleep(1)
       
        """    
        Step 02: Double-click "Product,Category", "Cost of Goods", and "Revenue"    
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 text[class^='xaxis'][class$='title']", 1, expire_time=10, string_value='Product Category')    
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        resultobj.wait_for_property("#TableChart_1 text[class='yaxis-title']", 1, expire_time=10, string_value='Cost of Goods')
        metaobj.datatree_field_click("Revenue", 2, 1)
        parent_css="#TableChart_1 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 14)
        
        """    
        Step 03: Click "Document" in the Home Tab ribbon   
        """
        ribbonobj.select_ribbon_item("Home", "Document")
        time.sleep(8) 
        
        """    
        Step 04: Verify chart on Document canvas   
        """
        resultobj.wait_for_property("#resultArea div[id*='iaCanvasCaptionLabel']", 1, expire_time=25, string_value='Document')
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 04.01: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 04.02: Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 04.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 04.04: Verify first bar color")
        legend=['Cost of Goods', 'Revenue']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 04.05: Verify legend Title")
        time.sleep(5)
        
        """    
        Step 05: Select View Tab > Click 'Switch Report' button 
        """
        ribbonobj.select_ribbon_item("View", "switch_report")
        time.sleep(2) 
        
        """    
        Step 06: Verify Chart1 and Document1 (only) are listed in the menu
        """
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Document1'],msg='Step 06.01:')
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Chart1', 'Document1'],msg='Step 06.02:')
        
        """    
        Step 07: Click "Save" > Save As "C2227557" > Click "Save"
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    
        Step 08: Click "IA" menu > Close to close Document fex
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(8)
        
        """    
        Step 09: Click "IA" menu > Close to close Chart fex
        Step 10: Click "No" in the Chart1 save prompt
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
        self.driver.find_element_by_css_selector("div[id^='loginForm'] div[id*='saveChangesLabel']").is_displayed()
        btn_css="div[id*='loginForm'] div[class^=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        core_utils.python_left_click(dialog_btns[btn_text_list.index('No')])
        time.sleep(10)
        
        """
        Step 11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.wf_logout() #changed due to alert issue
        time.sleep(2)
              
        """
        Step 12: Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227557.fex&tool=Document
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Document', 'S10032',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 13: Verify canvas
        """
        resultobj.wait_for_property("#resultArea div[id*='iaCanvasCaptionLabel']", 1, expire_time=25, string_value='Document')
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 13.01: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 13.02: Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 13.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 13.04: Verify first bar color")
        legend=['Cost of Goods', 'Revenue']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 13.05: Verify legend Title")
      
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()