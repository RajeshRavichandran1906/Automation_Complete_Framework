'''
Created on December 5, 2018

@author: vpriya
Testcase Name : Choose other filters using the icon
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8262118
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import chart,report
from common.lib import utillity
from common.lib import core_utility
from common.wftools.page_designer import Preview

class C8262118_TestClass(BaseTestCase):
    
    def test_C8262118(self):
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
        page_preview.select_multiple_options_from_filter_dropdown('Select North America', 'North America',model_window=True)
        
        """
        Step 5: Click Category > dropdown > choose Computers'.
        """
        page_preview.select_multiple_options_from_filter_dropdown('Category:', 'Computers',model_window=True)

        """
        Step 6: Click the Submit button..
        Verify the reports change accordingly. Only the controls which relate to a particular report should take affect.
        """
        main_page_obj.click_button_on_popup_dialog("Submit")
        page_preview.switch_to_container_frame('Category Sales', 1)
        util_obj.synchronize_with_visble_text(".chartPanel text[class^='totalLabel']", '103.3M', main_page_obj.home_page_long_timesleep)
        chart_obj.verify_pie_label_in_single_group_in_run_window(["103.3M"], parent_css='', label_css="text[class^='totalLabel']", msg="Step 06:01:Verify x_axis label in runtime")
        chart_obj.verify_pie_label_in_single_group_in_run_window(["Revenue"], parent_css='[id^=jschart]', label_css="text[class^='pieLabel!g']", msg="Step 06:02:Verify x_axis label in runtime")
        chart_obj.verify_number_of_pie_segments('[id^=jschart]', 1, 1, msg="Step 06:04:Verify x_axis label in runtime")
        chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'bar_blue1', parent_css='[id^=jschart]', msg="Step 06:05:Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, parent_css='[id^=jschart]',msg="Step 06:06: Verify legends")
        core_util_obj.switch_to_default_content()
        page_preview.switch_to_container_frame('28 - Multi-Select Dynamic Required', 1)
        report_obj.verify_table_data_set(table_css=None,file_name="C8262118.xlsx", msg='Step 06.1:')
        core_util_obj.switch_to_default_content()
        
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