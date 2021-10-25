'''
Created on Jun 26, 2019

@author: Varun/Prasanth
Testcase Name : Insight - Wheres in Reporting Object are ignored when Insight is on
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/5823688

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.wftools import report
from common.pages.wf_reporting_object import Wf_Reporting_Object
from common.lib import core_utility
from common.lib import utillity
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage

class C5823688_TestClass(BaseTestCase):
    
    def test_C5823688(self):
        
        """
            CLASS OBJECTS 
        """
        reporting_obj=Wf_Reporting_Object(self.driver)
        chart_obj = chart.Chart(self.driver)
        report_obj = report.Report(self.driver)
        util_obj=utillity.UtillityMethods(self.driver)
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
        
        expected_x_axis_title_list=['Store Business Region']
        expected_x_axis_label_list=['North America']
        expected_y_axis_title_list=['Cost of Goods']
        expected_y_axis_label_list=['0', '100M', '200M', '300M', '400M', '500M']
        
        """
        STEP 1: Launch the API to create new Chart.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=reportingobject&master=baseapp/wf_retail_lite
        """
        util_obj.invoke_infoassist_api_login("reportingobject", "baseapp/wf_retail_lite", folder_path, "mrid", "mrpass")
        chart_obj.wait_for_visible_text("#roTree", "Reporting Object")
        
        """
        STEP 2: Right Click Where Statements > New > Store Business Region EQ North America
        """
        reporting_obj.select_ro_tree_item("Where Statements", 1, "New")
        chart_obj.wait_for_visible_text("#dlgWhereWhereTree", "WHERE")
        report_obj.open_where_field_popup_in_filter_dialog(1)
        report_obj.select_field_in_filter_tree("Dimensions->Store->Store->Store,Business,Region", 1)
        ok_button=util_obj.validate_and_get_webdriver_object("#wndWhereFieldPopup_btnOK img", "OK button")
        core_util_obj.left_click(ok_button)
        
        
        report_obj.open_where_value_popup_in_filter_dialog(1)
        util_obj.set_text_to_textbox_using_keybord("North America", "#id_wv_text_value")
        add_button=util_obj.validate_and_get_webdriver_object("#dlgWhereValue #dlgWhereValue_btnConstAdd", "Add button")
        core_util_obj.left_click(add_button)
        report_obj.close_filter_where_value_popup_dialog()
        report_obj.close_filter_dialog()
        
        """
        STEP 3: Click Save > type "C5823688" > save
        """
        reporting_obj.select_top_toolbar_item("toptoolbar_save")
        chart_obj.wait_for_visible_text("#dlgIbfsOpenFile7", "Save")
        util_obj.set_text_to_textbox_using_keybord("C5823688", "#IbfsOpenFileDialog7_cbFileName input")
        save_button=util_obj.validate_and_get_webdriver_object("#IbfsOpenFileDialog7_btnOK", "Save button")
        core_util_obj.left_click(save_button)
        
        
        """
        STEP 4: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        STEP 5: Right click on C5823688 > New > Infoassist > Chart
        """
        login_obj.invoke_home_page(None, None)
        chart_obj.wait_for_visible_text(content_css, "Content")
        main_page_obj.select_content_from_sidebar()
        main_page_obj.click_repository_folder("Domains->P309_S10666->G169735")
        main_page_obj.right_click_folder_item_and_select_menu('C5823688', "New->InfoAssist->Chart")
        chart_obj.switch_to_new_window()
        
        """
        STEP 6: Drag Store Business Region to Horizontal Axis
        """
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        chart_obj.drag_field_from_data_tree_to_query_pane("Store,Business,Region", 1, "Horizontal Axis")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Store Business Region")
        
        """
        STEP 7: Drag Cost of Goods to Vertical Axis
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Cost of Goods", 1, "Vertical Axis")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Cost of Goods")
        
        """
        STEP 8: Click Save > type "C5823688_chart" > save
        """
        chart_obj.select_item_in_top_toolbar("save")
        chart_obj.save_file_in_save_dialog("C5823688_chart")
        
        """
        STEP 9: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        STEP 10 : Run the fex from the BIP using API
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP309_S10666%2FG169735&BIP_item=C5823688_chart.fex
        """
        chart_obj.run_fex_using_api_url(folder_path, "C5823688_chart", mrid="mrid", mrpass="mrpass")
        
        """
        STEP 11 : Verify that the Horizontal Axis is populated only with the North America Region
        """
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 11.01")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, msg="Step 11.02")
        
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 11.03")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, msg="Step 11.04")
        
        """
        STEP 12: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        STEP 13: Restore "C5823688_chart.fex" using API Code.
        http://domain:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735%2FC5823688_chart.fex
        """
        chart_obj.edit_fex_using_api_url(folder_path, fex_name="C5823688_chart")
        
        """
        STEP 14 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 15 : Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text("#runbox_id","North America")
        
        """
        STEP 16 : Verify that the Horizontal Axis is populated only with the North America Region
        """
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#runbox_id", msg="Step 16.01")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css="#runbox_id", msg="Step 16.02")
        
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#runbox_id", msg="Step 16.03")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css="#runbox_id", msg="Step 16.04")
        
        """
        STEP 17 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()
        
        """
        STEP 18 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        