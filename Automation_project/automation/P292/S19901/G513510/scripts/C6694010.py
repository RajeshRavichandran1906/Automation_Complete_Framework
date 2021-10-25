'''
Created on December 10, 2018

@author: varun
Testcase Name : Choose other filters using the icon as basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6694010
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.wftools import page_designer

class C6694010_TestClass(BaseTestCase):
    
    def test_C6694010(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        page_designer_obj = page_designer.Preview(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_portal_title = 'V5 Personal Portal'
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        submit_button_css = ".pd-amper-submit-button"
        labels_css= ".pd-amper-label"
        table_data = "td.x2"
        dropdown_select_list = ['Accessories','Camcorder','Media Player']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """
        Step 3: Run the portal by double click on 'V5 Personal Portal'.
        Verify 'V5 Personal Portal' opens in a new tab.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal',click_option='double_click')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_portal_title,45)
        observed_title = util_obj.validate_and_get_webdriver_object(portal_title_css, "Title css").text
        util_obj.asequal(expected_portal_title,observed_title,"Step 3.1: Verify the portal opens in a new window")
        
        """
        Step 4: Click on Select North America drop down > choose North America
        Verify filter modal window opens.
        """
        util_obj.synchronize_with_number_of_element(labels_css,7,120)
        page_designer_obj.select_filter_dropdown_option('Select North America', 'North America')
        
        """
        Step 5: Click Category > drop down > choose Accessories,Camcorder and Media Player.
        """
        page_designer_obj.select_multiple_options_from_filter_dropdown('Category:', dropdown_select_list)
        
        """
        Step 6: Click the Submit button.
        Verify the reports change accordingly. Only the controls which relate to a particular report should take effect.
        """
        submit_button_obj = util_obj.validate_and_get_webdriver_object(submit_button_css,"submit-button")
        core_util_obj.python_left_click(submit_button_obj)
        page_designer_obj.switch_to_container_frame('28 - Multi-Select Dynamic Required', 1)
        util_obj.synchronize_with_number_of_element(table_data, 2,45)
        page_designer_obj.verify_html_report_data_set('C6694010', 'Step 7.1: Verify data inside container 2 is changed')
        
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