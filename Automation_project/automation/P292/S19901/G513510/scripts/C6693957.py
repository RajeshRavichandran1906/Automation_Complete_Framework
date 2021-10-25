'''
Created on December 5, 2018

@author: vpriya
Testcase Name : Choose other filters using the icon
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6693957
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import chart,report
from common.lib import utillity
from common.lib import core_utility
from common.wftools.page_designer import Preview

class C6693957_TestClass(BaseTestCase):
    
    def test_C6693957(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        report_obj=report.Report(self.driver)
        page_preview=Preview(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        modal_window_css="div[class*='ibx-dialog-main-box ibx-widget']"
        frame1_css="iframe[name*='pdiframe1']"
        frame2_css="iframe[name*='pdiframe2']"
        submit_css="div[class*='pd-amper-submit']"
        expected_legends=['Product Category', 'Computers']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand 'P292_S19901' domain > G513510 folder
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """
        Step 3: Right click on 'V5 Personal Portal' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(modal_window_css,1,45)
        
        """
        Step 4: Select North America > dropdown > Choose 'North America'.
        """
        page_preview.select_filter_dropdown_option('Select North America', 'North America')
        
        """
        Step 5: Click Category > dropdown > choose Computers'.
        """
        page_preview.select_filter_dropdown_option('Category:', 'Computers')

        """
        Step 6: Click the Submit button..
        Verify the reports change accordingly. Only the controls which relate to a particular report should take affect.
        """
        Submit_elm=util_obj.validate_and_get_webdriver_object(submit_css,'Submit_css')
        core_util_obj.python_left_click(Submit_elm)
        util_obj.switch_to_frame(frame_css=frame1_css)
        chart_obj.verify_pie_label_in_single_group_in_run_window(["103.3M"], label_css="text[class^='totalLabel']", msg="Step 06:01:Verify x_axis label in runtime")
        chart_obj.verify_pie_label_in_single_group_in_run_window(["Revenue"], label_css="text[class^='pieLabel!g']", msg="Step 06:02:Verify x_axis label in runtime")
        chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 0, msg="Step 06:04:Verify x_axis label in runtime")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class^='riser!s0!g0!mwedge!']", 'bar_blue1', msg="Step 06:05:Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends,msg="Step 06:06: Verify legends")
        util_obj.switch_to_default_content()
        util_obj.switch_to_frame(frame_css=frame2_css)
        #report_obj.create_table_data_set(table_css=None,file_name="C6693957.xlsx")
        report_obj.verify_table_data_set(table_css=None,file_name="C6693957.xlsx", msg='Step 06.1:')
        util_obj.switch_to_default_content()
        
        """
        Step 7: Close the 'V5 Personal Portal' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()