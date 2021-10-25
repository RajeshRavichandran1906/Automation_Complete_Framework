'''
Created on Jun 25, 2019

@author: Varun/Prasanth
Testcase Name : Verify that disabled "Enable Autodrill" check box in properties pane for Insight enabled fex
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/5852965

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import core_utility
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage

class C5852965_TestClass(BaseTestCase):
    
    def test_C5852965(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        main_page_obj=Wf_Mainpage(self.driver)
        login_obj=Login(self.driver)
        
        """
        Test case variables
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text"
        
        expected_x_axis_title_list=['Product Category']
        expected_x_axis_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_title_list=['Cost of Goods']
        expected_y_axis_label_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        
        """
        STEP 1:Launch the API to create new Chart.
        http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P309_S10666/G169735
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : From Data pane, Expand Dimensions > Product
        STEP 3 : Double click on field "Product,Category"
        """
        chart_obj.double_click_on_datetree_item("Product,Category", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Product Category")
        
        """
        STEP 4 : From Data pane, Expand Measures > Sales
        STEP 5 : Double click on field "Cost of Goods"
        """
        chart_obj.double_click_on_datetree_item("Cost of Goods", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Cost of Goods")
        
        """
        STEP 5.01 Expected : Verify the Data pane, Query pane and canvas,
        """
        expected_query_fields=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Cost of Goods', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        chart_obj.verify_all_fields_in_query_pane(expected_query_fields, "Step 5.01 : Verify Query Pane")
        
        
        chart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, msg="Step 5.02")
        chart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg="Step 5.03")
        
        chart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, msg="Step 5.04")
        chart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg="Step 5.05")
        
        """
        STEP 6 : Select "Insight" from "Run with" cluster under format tab
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 7: Select Save from QAT
        """
        chart_obj.select_item_in_top_toolbar("save")
        
        """
        STEP 8: Enter "C5852965" in title
        STEP 9: Click Save
        """
        chart_obj.save_file_in_save_dialog("C5852965")
        
        """
        STEP 10 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        STEP 11 : Launch WF,
        http://machine:port/ibi_apps/
        """
        login_obj.invoke_home_page(None, None)
        chart_obj.wait_for_visible_text(content_css, "Content")
        main_page_obj.select_content_from_sidebar()
        main_page_obj.click_repository_folder("Domains->P309_S10666->G169735")
        
        """
        STEP 12 : Right click on the saved fex (C5852965)
        STEP 13 : Select Properties from menu
        """
        main_page_obj.right_click_folder_item_and_select_menu('C5852965', "Properties")
        
        """
        STEP 14 : Select Advanced tab in Properties dialog
        """
        chart_obj.wait_for_visible_text(".properties-tab-pane", "Advanced")
        main_page_obj.select_property_tab_value("Advanced")
        
        """
        STEP 15 : Verify "Enable Autodrill" check box is disabled
        """
        chart_obj.wait_for_visible_text(".properties-tab-pane", "Enable AutoDrill")
        main_page_obj.verify_property_dialog_enable_disable("Enable AutoDrill", "check_box", "Enable AutoDrill", msg="Step 15.01 : Verify 'Enable Autodrill' check box is disabled", tab_name="Advanced")
        
        """
        STEP 16 : Click Cancel
        """
        main_page_obj.select_property_dialog_save_cancel_button("Cancel")
        
        """
        STEP 17 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()
        
