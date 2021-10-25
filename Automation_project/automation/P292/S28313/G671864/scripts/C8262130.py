'''
Created on December 10, 2018

@author: varun
Testcase Name : Add Content to page with requirements parameters as basic user 
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262130
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility
from common.wftools import page_designer

class C8262130_TestClass(BaseTestCase):
    
    def test_C8262130(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        page_designer_obj = page_designer.Preview(self.driver)
        workspaces ="Workspaces"
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_portal_title = 'V5 Personal Portal'
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        page_container_css = ".pd-container-title"
        resource_box_css = ".open-dialog-resources .ibx-title-bar-caption .ibx-label-text"
        resource_text = 'Select Item'
        filter_list = ['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:', 'Select North America']
        submit_button_css = ".pd-amper-submit-button"
        reset_button_css = ".pd-amper-reset-button"
        labels_css= ".pd-amper-label"
        dialog_box_css = ".ibx-dialog-title-box"
        table_data = "td.x2"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder(workspaces+'->P292_S19901->G513510')
        
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
        Step 4: Click the + sign to add content to Panel 2.
        Click the + sign inside the Panel1 to add the content
        """
        util_obj.synchronize_with_number_of_element(page_container_css, 7,60)
        portal_obj.click_on_panel_add_content_button_in_container('Panel 2')
        util_obj.synchronize_with_visble_text(resource_box_css,resource_text,50)
        dialog_box_element = util_obj.validate_and_get_webdriver_object(resource_box_css, "dialog_title").text
        util_obj.asequal(dialog_box_element,resource_text,"Step 4.1: Verify selection window opens")
        
        """
        Step 5: Double click on 'P398_S10799' > 'Reference Items' > '28- Multi-Select Dynamic Required'.
        Verify that the modal window appears with 7 controls, submit and reset button.
        """
        portal_obj.select_repository_file_using_add_content_using_crumb_in_panel_container('Workspace','P398_S10799->Reference Items->28 - Multi-Select Dynamic Required', select_button='Add')
        util_obj.synchronize_with_number_of_element(labels_css,7,45)
        page_designer_obj.verify_filter_control_labels(filter_list, 'Step 5.1: Verify 7 Filter options are Present',model_window=True)
        util_obj.verify_object_visible(submit_button_css, True, "Step 5.2: Verify Sumbit button present ")
        util_obj.verify_object_visible(reset_button_css,True, "Step 5.3: Verify Reset button present")
        
        """
        Step 6: Click on North American > drop down > choose North America.
        """
        page_designer_obj.select_multiple_options_from_filter_dropdown('Select North America', 'North America',model_window=True)
        
        """
        Step 7: Click the Submit button.
        Verify filter modal window disappears and the panel 2 is populated with content.
        """
        main_page_obj.click_button_on_popup_dialog("Submit")
        time.sleep(15)
        page_designer_obj.switch_to_container_frame('28 - Multi-Select Dynamic Required', 1)
        util_obj.synchronize_with_number_of_element(table_data, 2,45)
        util_obj.verify_object_visible(dialog_box_css,False,"Step 7.1: Verify Filter box is closed")
        page_designer_obj.verify_html_report_data_set('C6694000', 'Step 7.2: Verify data inside container 2')
        
        """
        Step 8: Close the 'V5 Personal Portal' run window. 
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()