'''
Created on December 18, 2018

@author: Vpriya
Testcase Name : Add Content to page with requirements parameters 
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262138
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility
from common.wftools import page_designer
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables
from common.wftools import active_report

class C8262138_TestClass(BaseTestCase):
    
    def test_C8262138(self):
        """
        Test_case variables
        """
        active_report_obj = active_report.Active_Report(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        page_designer_obj = page_designer.Preview(self.driver)
        case_id = 'C8262138'
        page_container_css = ".pd-container-title"
        filter_list = ['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:', 'Select North America']
        labels_css= ".pop-top .pd-amper-label"
        dialog_box_css = ".pop-top .ibx-dialog-title-box"
        table_data = "table[summary='Summary']"
        resource_dialog_css = '.open-dialog-resources.pop-top'
        project_id=core_util_obj.parseinitfile('project_id')
        suite_id=core_util_obj.parseinitfile('suite_id')
        group_id=core_util_obj.parseinitfile('group_id')
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
                Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        main_page_obj.expand_repository_folder('Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id))
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal_Nav-2','Run')
        core_util_obj.switch_to_new_window()
        
        """
        Step 4: Click the + sign to add content to Panel 2.
        Verify Select Item browse window appears.
        """
        util_obj.synchronize_with_number_of_element(page_container_css, 3,90)
        portal_obj.click_on_panel_add_content_button_in_container('Panel 2')
        util_obj.synchronize_until_element_is_visible(resource_dialog_css, 45)
        main_page_obj.verify_resource_dialog_is_visible(True, 'Step 4: Verify window appears.')
        main_page_obj.verify_caption_title_in_resource_dialog('Select Item', 'Step 4.1: Verify window appears.')
         
        """
        Step 5: Double click on 'P398_S10799' > 'Reference Items' > '28- Multi-Select Dynamic Required'.
        Verify that the modal window appears with 7 controls, submit and reset button.
        """
        portal_obj.select_repository_file_using_add_content_using_crumb_in_panel_container('Domain','P398_S10799->Reference Items->28 - Multi-Select Dynamic Required', select_button='Add')
        util_obj.synchronize_with_number_of_element(labels_css, 7, 90)
        page_designer_obj.verify_filter_control_labels(filter_list, 'Step 5.1: Verify 7 Filter options are Present',model_window=True)
        main_page_obj.verify_button_text_on_popup_dialog("Submit",'Step 5.2:Verify Submit button is present')
        main_page_obj.verify_button_text_on_popup_dialog("Reset",'Step 5.3:Verify Reset button is present')
         
        """
        Step 6: Click on North American > drop down > choose North America.
        """
        page_designer_obj.select_multiple_options_from_filter_dropdown('Select North America', 'North America', model_window=True)
         
        """
        Step 7: Click the Submit button.
        Verify filter modal window disappears and the panel 2 is populated with content.
        """
        main_page_obj.click_button_on_popup_dialog("Submit")
        page_designer_obj.switch_to_container_frame('28 - Multi-Select Dynamic Required', 1)
        util_obj.synchronize_with_number_of_element(table_data, 1, 90)
        util_obj.verify_object_visible(dialog_box_css,False,"Step 7.1: Verify Filter box is closed")
        active_report_obj.verify_active_report_dataset(case_id +'.xlsx', 'Step 7.2: Verify data inside container 2', table_css='table[summary]')
        
        """
        Step 8: Close the 'V5 Personal Portal_Nav-2' run window. 
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()