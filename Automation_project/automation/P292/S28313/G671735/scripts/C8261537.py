'''
Created on October 24, 2018

@author: vpriya
Testcase Name : Test Properties menu using Developers
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261537
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,javascript
from common.pages import wf_mainpage as pages
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261537_TestClass(BaseTestCase):
    
    def test_C8261537(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        j_scrip=javascript.JavaScript(self.driver)
        pages_obj=pages.Wf_Mainpage(self.driver)
        project_id = util_obj.parseinitfile('project_id')
        suite_id = util_obj.parseinitfile('suite_id')
        group_id = util_obj.parseinitfile('group_id')
        folder_path='{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        url_path='{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        radio_button_css=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        properties_css = '.properties-tab-pane'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.click_repository_folder('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(folder_path)
        
        """
        Step 4: Right click on 'Portal for Context Menu ...'. 
        Right click on 'Portal for Context Menu ...' > Click Properties
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Properties')
        util_obj.synchronize_with_visble_text(properties_css, 'General', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_tab_in_property_dialog('General',"Step 4:Verify the Property dialog default selected to general")
        main_page_obj.verify_property_dialog_value('Title', 'text_value', "Portal for Context Menu Testing","Step 4.1:Verify the title tab")
        main_page_obj.verify_property_dialog_value('Name', 'text_value', "Portal_for_Context_Menu_Testing","Step 4.2:Verify the Name tab")
        main_page_obj.verify_property_dialog_enable_disable('Name', 'text_value', False, "Step 4.3: Verify Name - is disable.")
        main_page_obj.verify_property_dialog_value('Summary', 'text_area',"","Step 4.4:Verify the Summary tab")
        main_page_obj.verify_property_dialog_value('Path', 'text_value', 'IBFS:/WFC/Repository/'+url_path+'/Portal_for_Context_Menu_Testing',"Step 4.5:Verify the Path tab")
        main_page_obj.verify_property_dialog_value('Owner','text',"-","Step 4.6:Verify the Owner tab")
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Created','admin',"step 4.7 verify the created tab value")
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Modified','admin',"step 4.8 verify the Modified tab value")
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Accessed','admin',"step 4.9 verify the Accessed tab value")
        main_page_obj.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 4.10: Verify Publish - is enabled.")
        main_page_obj.verify_property_dialog_value('Publish','radiobutton_value','Yes',"Step 4.11: Verify Publish - is available")
        main_page_obj.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 4.12: Verify Publish - is enabled.")
        main_page_obj.verify_property_dialog_value('Show','radiobutton_value','Yes',"Step 4.13: Verify Show - is enabled.")
        
        """
        Step 5:Click the advanced tab
        Verify all the options under 'Advanced tab' as per in the screenshot
        """
        main_page_obj.select_property_tab_value("Advanced")
        util_obj.synchronize_with_visble_text(properties_css, 'Advanced', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Folder Properties', 'Step 5.1: Folder label verification')
        main_page_obj.verify_property_dialog_enable_disable('Allow personal pages', 'check_box', 'Allow personal pages', 'Step 5.2: Verify Allow personal pages is Disabled', tab_name='Advanced')
        main_page_obj.verify_property_dialog_enable_disable('Automatically open', 'check_box', False, 'Step 5.3: Verify Automatically Open is enabled', tab_name='Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Explorer/Portal Properties', 'Step 5.4: Explorer label verification')
        main_page_obj.verify_property_dialog_enable_disable('Thumbnail', 'radiobutton_value', False, "Step 5.5: Verify Thumbnail - is enabled.",tab_name='Advanced')
        thumbnail_row_obj=pages_obj.get_property_dialog_rows_object('Advanced','Thumbnail', '5')
        radio_optoins_elems=thumbnail_row_obj.find_elements_by_css_selector(radio_button_css)
        actual_thumbnail_radiobutton_options=[elem.text.strip() for elem in radio_optoins_elems]
        expected_thumbnail_radiobutton_options=['Default', 'Embedded', 'Link']
        util_obj.as_List_equal(expected_thumbnail_radiobutton_options, actual_thumbnail_radiobutton_options, "Step 5.6: Verify Thumbnail (Default, Embedded, Link radio buttons).")
        default_radiobutoon_obj=radio_optoins_elems[expected_thumbnail_radiobutton_options.index('Default')].find_element_by_css_selector("[class^='ibx-radio-button']")
        if 'ibx-radio-button-simple-marker-check' in j_scrip.get_element_all_attributes(default_radiobutoon_obj)['class']:
            default_radiobutoon_status='checked'
        else:
            default_radiobutoon_status='unchecked'
        util_obj.asequal('checked', default_radiobutoon_status, "Step 5.7: Verify Thumbnail Default is selected.")
        util_obj.verify_picture_using_sikuli("Thumbnail_image.png","Step 5.8:Verify the thumbnail image")
        main_page_obj.verify_property_dialog_value('Sort order', 'text_value', '','Step 5.9: Sort Order verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 5.10: Verify View All - is enabled.",tab_name='Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Search Properties', 'Step 5.11:Search properties label verification')
        main_page_obj.verify_property_dialog_value('Tags', 'text_value', '','Step 5.12: Tags verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', 'Step 5.13: Save button disable verfication')

        """
        Step 6:Click Cancel to close the properties dialog box
        """
        main_page_obj.select_property_dialog_save_cancel_button('Cancel')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        