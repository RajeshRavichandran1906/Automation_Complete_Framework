'''
Created on Jun 24, 2019

@author: Varun/Prasanth
Testcase Name : Insight: Parm lists should limit Group/Matrix Bucket list w/parm prompting OFF
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/5831079

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import core_utility
from common.wftools.login import Login
from common.pages.insight_header import Insight_Header
from common.wftools.wf_mainpage import Wf_Mainpage

class C5831079_TestClass(BaseTestCase):
    
    def test_C5831079(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        main_page_obj=Wf_Mainpage(self.driver)
        login_obj=Login(self.driver)
        insight_header_obj= Insight_Header(self.driver)
        
        """
        Test case variables
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text"

        
        """
        STEP 1:Launch the API to create new Chart.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Right-click the Horizontal Axis > Select 'New Parameter'
        """
        chart_obj.right_click_on_field_under_query_tree("Horizontal Axis", 1, "New Parameter")
        chart_obj.wait_for_visible_text("#queryTreeWindow", "Parameter1")
        
        """
        STEP 3 : Drag COUNTRY into Parameter1 container
                 Drag CAR into Parameter1 container
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("COUNTRY", 1, "Parameter1", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "COUNTRY")
        
        chart_obj.drag_field_from_data_tree_to_query_pane("CAR", 1, "COUNTRY", 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow", "CAR")
        
        """
        STEP 4 : Right-click the Vertical Axis > Select 'New Parameter'
        """
        chart_obj.right_click_on_field_under_query_tree("Vertical Axis", 1, "New Parameter")
        chart_obj.wait_for_visible_text("#queryTreeWindow", "Parameter2")
        
        """
        STEP 5 : Drag SALES into Parameter2 container
                 Drag DEALER_COST into Parameter2 container
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("SALES", 1, "Parameter2", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "SALES")
        
        chart_obj.drag_field_from_data_tree_to_query_pane("DEALER_COST", 1, "SALES", 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow", "DEALER_COST")
        
        """
        STEP 6 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 7: Save fex as 'C5823713'
        """
        chart_obj.select_item_in_top_toolbar("save")
        chart_obj.save_file_in_save_dialog("C5823713")
        
        """
        STEP 8 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        STEP 9 : Right-click 'C5823713' > choose Properties
        """
        login_obj.invoke_home_page(None, None)
        chart_obj.wait_for_visible_text(content_css, "Content")
        main_page_obj.select_content_from_sidebar()
        main_page_obj.click_repository_folder("Domains->P309_S10666->G169735")
        main_page_obj.right_click_folder_item_and_select_menu('C5823713', "Properties")
        
        """
        STEP 10 : Uncheck 'Prompt for Parameters' under the Advanced tab and click OK
        """
        chart_obj.wait_for_visible_text(".properties-tab-pane", "Advanced")
        main_page_obj.select_property_tab_value("Advanced")
        main_page_obj.edit_property_dialog_value("Prompt for parameters", "checkbox", "uncheck", tab_name="Advanced")
        main_page_obj.select_property_dialog_save_cancel_button("Save")
        
        """
        STEP 11 : Close properties dialog.
        """
        main_page_obj.close_property_dialog()
        
        """
        STEP 12 : Run C5823713.fex using the below API:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P309_S10666%2FG169735&BIP_item=C5823713.fex
        """
        chart_obj.logout_chart_using_api()
        chart_obj.run_fex_using_api_url(folder_path, "C5823713", mrid="mrid", mrpass="mrpass", run_chart_css="#runbox_id")
        
        """
        STEP 13 : Click on SALES > Verify only on SALES and DEALER_COST are displayed
        """
        chart_obj.wait_for_visible_text("#runbox_id", "COUNTRY")
        insight_header_obj.click_plus_icon_in_query_bucket_container("Vertical Axis")
        expected_fields_list=["Measures","SALES","DEALER_COST"]
        insight_header_obj.verify_data_fields(expected_fields_list, "Step 13.01 : Verify only SALES and DEALER_COST are displayed ")
        
        """
        STEP 14 : Click on COUNTRY > Verify only on COUNTRY and CAR are displayed
        """
        insight_header_obj.click_plus_icon_in_query_bucket_container("Group")
        expected_fields_list=["Dimensions","COUNTRY","CAR"]
        insight_header_obj.verify_data_fields(expected_fields_list, "Step 14.01 : Verify only COUNTRY and CAR are displayed ")
        
        """
        STEP 15 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()