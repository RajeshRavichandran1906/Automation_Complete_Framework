'''
Created on Nov 30, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227559
TestCase Name = Verify InfoMini with Chart mode
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon
from common.lib import utillity

class C2227559_TestClass(BaseTestCase):

    def test_C2227559(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227559'
        Test_Case_ID_IM = 'C2227559_IM'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """   
        Step 01: Launch IA Chart mode:http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS1003 
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 g.legend path[class^='legend-markers']", 5, expire_time=25)
        time.sleep(1)
         
        """    
        Step 02: Double-click "Product,Category" and "Revenue"  
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 text[class^='xaxis'][class$='title']", 1, expire_time=10, string_value='Product Category')    
        metaobj.datatree_field_click("Revenue", 2, 1)
        parent_css="#TableChart_1 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 7)
         
        """
        Step 03 : Select Format Tab > Click "InfoMini"
        """
        ribbonobj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(1)
         
        """
        Step 04 : Click on the InfoMini menu > Verify default options
        Step 05 : Select "Resources/Field Tab"
        """
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Home Tab', 'Format Tab', 'Slicers Tab', 'Data Tab', 'Slicer Tab (Edit)', 'Layout Tab', 'Series Tab', 'Resources/Field Tab', 'Run Immediately', 'Run Deferred', 'Save'],msg='Step 04:')
        utillobj.select_or_verify_bipop_menu("Resources/Field Tab")
        time.sleep(2)
         
        """
        Step 06 : Click InfoMini menu again > Select "Series Tab"
        """
        ribbonobj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Series Tab")
        time.sleep(2)
         
        """    
        Step 07: Click "Save" > save as "C2227559" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """
        Step 08 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        time.sleep(8)
         
        """
        Step 09 : Verify InfoMini Application is launched in a new window
        """
        parent_css="#interactiveModeButton"
        resultobj.wait_for_property(parent_css, 1)
        css_obj=self.driver.find_element_by_css_selector("#interactiveModeButton")
        status=css_obj.is_displayed()
        utillobj.asequal(status, True, "Step 09: Verify InfoMini Application is launched in a new window")
        utillobj.switch_to_frame(pause=2)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 09.1: X and Y axis labels')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 09.2: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'Revenue', "Step 09.3: Verify Y-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 09.4: Verify first bar color")
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 09.5: Verify tooltiptip values")
        utillobj.switch_to_default_content(pause=1)
         
        """
        Step 10 : Click "Edit" in the InfoMini toolbar
        """
        ribbonobj.select_top_toolbar_item('infomini_edit')
        parent_css="#IaToolbar"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
         
        """
        Step 11: Verify canvas
        """
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 11.1: X and Y axis labels')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 11.2: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'Revenue', "Step 11.3: Verify Y-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 11.4: Verify first bar color")
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 11.5: Verify tooltiptip values")
        utillobj.switch_to_default_content(pause=1)
         
        """
        Step 12: Double-click "Cost of Goods"
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(10)
         
        """
        Step 13: Verify Query pane is updated
        """
        metaobj.verify_query_pane_field('Vertical Axis', "Cost of Goods",2, "Step 13")
        time.sleep(10)
         
        """
        Step 14: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        time.sleep(10)
         
        """
        Step 15: Verify output is updated
        """
        parent_css="#interactiveModeButton"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 14)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 15.1: X and Y axis labels')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 15.2: Verify X-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 15.4: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "bar_green", "Step 15.5: Verify first bar color")
        legend=['Revenue', 'Cost of Goods']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 15.6: Verify legend Title")
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 15.7: Verify tooltiptip values")
        utillobj.switch_to_default_content(pause=1)
         
        """
        Step 16: Click "Save" in the InfoMini toolbar > Save as "C2227559_IM" > Click Save
        """
        ribbonobj.select_top_toolbar_item('infomini_save')
        utillobj.ibfs_save_as(Test_Case_ID_IM)
        time.sleep(3)
         
        """
        Step 17: Close the InfoMini window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        parent_css="#applicationButton img"
        resultobj.wait_for_property(parent_css, 1)
         
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 19: Run the saved InfoMini FEX: http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2227559_IM.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID_IM+'.fex','S10032_infoassist_3','mrid','mrpass')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        parent_css="#jschart_HOLD_0"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 20: Verify InfoMini Application is launched
        """
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 14)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 20.1: X and Y axis labels')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 20.2: Verify X-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 20.4: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "bar_green", "Step 20.5: Verify first bar color")
        legend=['Revenue', 'Cost of Goods']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 20.6: Verify legend Title")
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 20.7: Verify tooltiptip values")
        utillobj.switch_to_default_content(pause=1)
        
        """
        Step 21: Click "Edit"
        """
        ribbonobj.select_top_toolbar_item('infomini_edit')
        
        """
        Step 22: Drag "Product,Category" to the Filter pane
        """
        time.sleep(6)
        metaobj.datatree_field_click('Product,Category',1, 1, 'Filter')
        
        """
        Step 23: Click Get Values > All
        Step 24: Double-click values "Computers" and "Televisions" > Click OK > OK
        """
        parent_css="#dlgWhere  #dlgWhere_btnOK"
        resultobj.wait_for_property(parent_css, 1, expire_time=20)            
        time.sleep(2)
        iaribbonobj.create_constant_filter_condition('All', ['Computers', 'Televisions'])
        time.sleep(5)
        
        """
        Step 25: Verify filter is displayed in the Filter pane
        """
        metaobj.verify_filter_pane_field('Product,Category Equal to Computers or Televisions',1,"Step25:")  
        time.sleep(5)
        
        """
        Step 26: Click Run > Verify filter is applied
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#interactiveModeButton"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 4)
        expected_xval_list=['Computers','Televisions']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 26.1: X and Y axis labels')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 26.2: Verify X-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 26.3: Verify first bar color")
        expected_tooltip_list=['Product Category:Computers', 'Revenue:$103,316,482.12']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 26.4: Verify tooltiptip values")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,'C2227559_Actual_step26', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.switch_to_default_content(pause=1)
        
        """    
        Step 27: Click "Save" > Verify "Save As" dialog is displayed
        Step 28: Click "Save" in the dialog > Click "Yes" to replace existing fex
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('infomini_save')
        utillobj.ibfs_save_as(Test_Case_ID_IM)
        time.sleep(5)
        
        """
        Step 29: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()