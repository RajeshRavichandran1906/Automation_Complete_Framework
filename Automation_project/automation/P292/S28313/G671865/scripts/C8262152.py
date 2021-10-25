'''
Created on December 21, 2018

@author: KK14897
Testcase Name : Choose other filters using the icon as basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262152
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.wftools import page_designer
from common.wftools import active_report

class C8262152_TestClass(BaseTestCase):
    
    def test_C8262152(self):
        """
        Test_case variables
        """
        active_report_obj = active_report.Active_Report(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        page_designer_obj = page_designer.Preview(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_portal_title = 'V5 Personal Portal_Nav-2'
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        labels_css= ".pd-amper-label"
        table_data = "td.x2"
        case_id = 'C8262152'
        dropdown_select_list = ['Accessories','Camcorder','Computers']
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=str("Domains->"+project_id+"_"+ suite_id +"->"+ group_id)
        items_css = 'div[data-ibxp-text="Items "] .ibx-label-text'
        
        """
        Step 1:Sign into WebFOCUS Home Page as Basic User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(folder_path)
        util_obj.synchronize_with_visble_text(items_css,'Items', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Run the portal by double click on 'V5 Personal Portal_Nav-2'.
                Verify filter modal window opens.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal_Nav-2',click_option='double_click')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_portal_title, main_page_obj.home_page_medium_timesleep)
        observed_title = util_obj.validate_and_get_webdriver_object(portal_title_css, "Title css").text
        util_obj.asequal(expected_portal_title,observed_title,"Step 3.1: Verify the portal opens in a new window")
        
        """
        Step 4: Select North America in Select North America dropdown control.
                Verify North America value selected in dropdown control.
        """
        util_obj.synchronize_with_number_of_element(labels_css, 7, main_page_obj.home_page_long_timesleep)
        page_designer_obj.select_multiple_options_from_filter_dropdown('Select North America', 'North America',model_window=True)
        page_designer_obj.verify_selected_value_of_filter_dropdown('Select North America', ['North America'], 'Step 4.1: Verify North America value selected in dropdown control.',model_window=True)
        
        """
        Step 5: Click Category > dropdown > choose Accessories,Camcorder and Computers, Click the Submit button
        """
        page_designer_obj.select_multiple_options_from_filter_dropdown('Category:', dropdown_select_list,model_window=True)
        main_page_obj.click_button_on_popup_dialog("Submit")
        page_designer_obj.switch_to_container_frame('28 - Multi-Select Dynamic Required', 1)
        util_obj.synchronize_with_number_of_element(table_data, 2, main_page_obj.home_page_long_timesleep)
        active_report_obj.create_active_report_dataset('C8262152.xlsx', table_css='table[summary]')
        active_report_obj.verify_active_report_dataset(case_id +'.xlsx', 'Step 7.2: Verify data inside container 2 is changed', table_css='table[summary]')
        
        """
        Step 6: Close the 'V5 Personal Portal' run window.
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(items_css,'Items', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()