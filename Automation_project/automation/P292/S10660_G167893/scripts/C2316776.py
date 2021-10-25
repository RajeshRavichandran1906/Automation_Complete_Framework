'''
Created on Dec 14, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2316776
TestCase Name : Verify field Titles in the Compute dialog
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, define_compute, visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2316776_TestClass(BaseTestCase):

    def test_C2316776(self):
        
        Test_Case_ID = "C2316776"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomp_obj=define_compute.Define_Compute(self.driver)
        
        """
            Step 01:Launch Chart mode:
            http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css,1)
        
        """  
            Step 02:Add field "Product,Category"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        """ 
            Step 03:Select the Data Tab > Click "Summary(Compute)"
        """
        defcomp_obj.invoke_define_compute_dialog('compute')
        """ 
            Step 04:Click on the "Additional Options" button
        """
        defcomp_obj.select_menu_button_in_compute("additional_option")
        time.sleep(1)
        """ 
            Step 05:Verify "Use Field Titles" is displayed and selected by default
        """
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=['Use field titles', 'Preserve null value', 'Missing Values'], expected_ticked_list=['Use field titles'], msg='Step 06:01 Verify popup menu')
        defcomp_obj.select_menu_button_in_compute("additional_option")     
        """
            Step 06:Expand Measures > Sales > Drag "Revenue" into the Compute text area
        """

        defcomp_obj.drag_metadata_field_to_text_area("Revenue", 1)
        time.sleep(1)
            
        """ 
            Step 07:Verify text area displays the field title "Revenue"
        """
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        act_textarea_value=css_text.get_attribute("value").strip()
        print(act_textarea_value)
        expected_textarea_value='"Revenue"'
        utillobj.asequal(act_textarea_value, expected_textarea_value, "Step 06:01: Verify textarea displays the field title")
         
        """ 
            Step 08:Click on the minus - sign in the calculator keypad
        """
        defcomp_obj.select_calculation_btns(btn_series="minus")
        """ 
            Step 09:Drag "Cost of Goods" into the Compute text
        """
        defcomp_obj.drag_metadata_field_to_text_area("Cost of Goods", 1)
        time.sleep(1)
        """  
            Step 10:Verify text box displays the following:
            "Revenue" - "Cost of Goods"
        """
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        act_textarea_value=css_text.get_attribute("value").strip()
        print(act_textarea_value)
        expected_textarea_value='"Revenue" - "Cost of Goods"'
        utillobj.asequal(act_textarea_value, expected_textarea_value, "Step 10:01: Verify textarea displays the field title")       
        """ 
            Step 11:Click OK
        """
        defcomp_obj.close_define_compute_dialog("ok")
        time.sleep(2)    
        """ 
            Step 12:Verify Query pane, and Live Preview
        """
        metaobj.verify_query_pane_field("Vertical Axis", "Compute_1", 1, "Step 12:01:")
        """
            Verify Live Preview
        """
        parent_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 12:01: Verify X-Axis Title")
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 12:01: X and Y axis labels')
        resultobj.verify_number_of_riser('TableChart_1',1,7, 'Step 12:02: Verify Number of risers in the bar chart')
        resultobj.verify_yaxis_title("TableChart_1", 'Compute_1', "Step 12:03: Verify X-Axis Title")
        """ 
            Step 13:Click "Save" in the toolbar
            Step 14:Save As "C2316776" > Click Save
        """     
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """ 
            Step 15:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """ 
            Step 16:Reopen the saved fex:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2316776.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        parent_css= "#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 17:Right-click "Compute_1" in the Query pane > Edit Compute
        """
        metaobj.querytree_field_click("Compute_1", 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Edit Compute")
        parent_css="div[id^='QbDialog'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 18:Verify field Titles in the Text area
        """
        css_text=driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        act_textarea_value=css_text.get_attribute("value").strip()
        expected_textarea_value='"Revenue" - "Cost of Goods"'
        utillobj.asequal(act_textarea_value, expected_textarea_value, "Step 18:01: Verify textarea displays the field title")
        """ 
            Step 19:Click Cancel
        """
        defcomp_obj.close_define_compute_dialog("Cancel")     
        """ 
            Step 20:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()