'''
Created on October 27, 2018

@author: Ragunath
Testcase Name : Test Properties menu
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261544
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,javascript
from common.pages import wf_mainpage as pages
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility

class C8261544_TestClass(BaseTestCase):
    
    def test_C8261544(self):
        
        """
        Test_case variables
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        j_scrip=javascript.JavaScript(self.driver)
        pages_obj=pages.Wf_Mainpage(self.driver)
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        breadcrumb_path="Domains->{0}_{1}->{2}".format(project_id, suite_id, group_id)
        radio_button_css=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        tab_css = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        properties_css = '.properties-tab-pane'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        
        """
        Step 4: Right click on 'Portal for Context Menu ...' > Click Properties from the Resource Tree
        Verify that Properties dialog opens with the three tabs are 'General' (Selected by default), 'Advanced' and 'Server.
        Verify all the options under 'General' tab as per in the screenshot
        """
        main_page_obj.select_repository_folder_context_menu('Portal for Context Menu Testing','Properties',verification_state='collpase')
        util_obj.synchronize_with_visble_text(properties_css, 'General', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_tab_in_property_dialog("General", "Step 4.1: propery tab verification")
        main_page_obj.verify_property_dialog_tab_list(['General','Advanced','Server'], "Step 4.2: tab list verification")
        main_page_obj.verify_property_dialog_value('Title', 'text_value', "Portal for Context Menu Testing","Step 4.1:Verify the title tab")
        main_page_obj.verify_property_dialog_value('Name', 'text_value', "Portal_for_Context_Menu_Testing","Step 4.2:Verify the Name tab")
        main_page_obj.verify_property_dialog_enable_disable('Name', 'text_value', False, "Step 4.3: Verify Name - is disable.")
        main_page_obj.verify_property_dialog_value('Summary', 'text_area',"","Step 4.4:Verify the Summary tab")
        main_page_obj.verify_property_dialog_value('Path', 'text_value', "IBFS:/WFC/Repository/{0}_{1}/{2}/Portal_for_Context_Menu_Testing".format(project_id, suite_id, group_id),"Step 4.5:Verify the Path tab")
        main_page_obj.verify_property_dialog_value('Owner','text',"-","Step 4.6:Verify the Owner tab")
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Created','admin',"step 4.7 verify the created tab value")
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Modified','admin',"step 4.8 verify the Modified tab value")
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Accessed','admin',"step 4.9 verify the Accessed tab value")
        main_page_obj.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 4.10: Verify Publish - is enabled.")
        main_page_obj.verify_property_dialog_value('Publish','radiobutton_value','Yes',"Step 4.11: Verify Publish - is available")
        main_page_obj.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 4.12: Verify Publish - is enabled.")
        main_page_obj.verify_property_dialog_value('Show','radiobutton_value','Yes',"Step 4.13: Verify Show - is enabled.")
        
        """
        Step 5: Click the advanced tab
        Verify all the options under 'Advanced tab' as per in the screenshot
        """
        util_obj.synchronize_with_number_of_element(tab_css, 3, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_property_tab_value("Advanced")
        util_obj.synchronize_with_visble_text(properties_css, 'Advanced', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_tab_in_property_dialog("Advanced", "Step 5.1: Verify propery tab ")
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Folder Properties', 'Step 5.2: Folder label verification')
        main_page_obj.verify_property_dialog_enable_disable('Allow personal pages', 'check_box', False, 'Step 5.3: Verify Allow personal pages is Disabled', tab_name='Advanced')
        main_page_obj.verify_property_dialog_enable_disable('Automatically open', 'check_box', False, 'Step 5.4: Verify Automatically Open is enabled', tab_name='Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Explorer/Portal Properties', 'Step 5.5: Explorer label verification')
        main_page_obj.verify_property_dialog_enable_disable('Thumbnail', 'radiobutton_value', False, "Step 5.6: Verify Thumbnail - is enabled.",tab_name='Advanced')
        thumbnail_row_obj=pages_obj.get_property_dialog_rows_object('Advanced','Thumbnail', '5.7')
        radio_options=thumbnail_row_obj.find_elements_by_css_selector(radio_button_css)
        actual_thumbnail_radiobutton_options=[elem.text.strip() for elem in radio_options]
        expected_thumbnail_radiobutton_options=['Default', 'Embedded', 'Link']
        util_obj.as_List_equal(expected_thumbnail_radiobutton_options, actual_thumbnail_radiobutton_options, "Step 5.8: Verify Thumbnail (Default, Embedded, Link radio buttons).")
        default_radiobutton_obj=radio_options[expected_thumbnail_radiobutton_options.index('Default')].find_element_by_css_selector("[class^='ibx-radio-button']")
        if 'ibx-radio-button-simple-marker-check' in j_scrip.get_element_all_attributes(default_radiobutton_obj)['class']:
            default_radiobutton_status='checked'
        else:
            default_radiobutton_status='unchecked'
        util_obj.asequal('checked', default_radiobutton_status, "Step 5.9: Verify Thumbnail Default is selected.")
        util_obj.verify_picture_using_sikuli("Thumbnail_image.png","Step 5.10:Verify the thumbnail image")
        main_page_obj.verify_property_dialog_value('Sort order', 'text_value', '','Step 5.11: Sort Order verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 5.12: Verify View All - is enabled.",tab_name='Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Search Properties', 'Step 5.13:Search properties label verification')
        main_page_obj.verify_property_dialog_value('Tags', 'text_value', '','Step 5.14: Tags verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', 'Step 5.15: Save button disable verfication')
        
        """
        Step 6: Click the server tab
        Verify server which the portal is using should be checked
        """
        util_obj.synchronize_with_number_of_element(tab_css, 3, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_property_tab_value("Server")
        util_obj.synchronize_with_visble_text(properties_css, 'Server', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_tab_in_property_dialog("Server", "Step 6.1: propery tab verification")
        main_page_obj.verify_property_dialog_enable_disable('Assign Server', 'check_box', False, 'Step 6.2: Verify Assign Server is Disabled', tab_name='Server')
        main_page_obj.verify_property_dialog_enable_disable('EDASERVE', 'check_box', False, 'Step 6.3: Verify EDASERVE is Disabled', tab_name='Server')
        main_page_obj.verify_property_dialog_enable_disable('Assign Application Path', 'check_box', False, 'Step 6.4: Verify Assign Application Path is disabled', tab_name='Server')
        
        """
        Step 7: Click Cancel to close the properties dialog box
        """
        main_page_obj.select_property_dialog_save_cancel_button("Cancel")
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()   