"""-------------------------------------------------------------------------------------------
Author Name : Niranjan
Automated On : Feb 04, 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage
from common.pages.wf_mainpage import Wf_Mainpage as pages

class C9927923_TestClass(BaseTestCase):
    
    def test_C9927923(self):
        
        """
        TESTCASE OBJECTS
        """
        page = pages(self.driver)
        j_script = JavaScript(self.driver)
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        old_homepage = Wf_Mainpage(self.driver)    
        
        """
        TESTCASE VARIABLES
        """
        tab_css = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        radio_button_css=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        
        
        STEP_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Developers User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Expand 'P406_S31920' workspace > Click on 'G875179' folder in the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04 : Right-click on 'V5 Context Menu Testing' from the repository tree > Click 'Properties'
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875179->V5 Context Menu Testing")
        HomePage.ContextMenu.select('Properties')
        utils.capture_screenshot("04.00", STEP_04)

        STEP_04_01 = """Verification - Verify that Properties dialog opens with the two tabs are 'General' (Selected by default), and 'Advanced'.
        Verify all the options under the 'General' tab as per in the below screenshot
        """
        utils.synchronize_with_number_of_element(tab_css, 2,90)
        expcted_tab = ['General', 'Advanced']
        old_homepage.verify_property_dialog_tab_list(expcted_tab, "Step 04.01: Verify three tab in properties dialog")
        old_homepage.verify_selected_tab_in_property_dialog('General', 'Step 04.02: Verify General selected by default')
        old_homepage.verify_property_dialog_value('Title', 'text_value', 'V5 Context Menu Testing','Step 04.03: Verify title', user_name='autoadmuser59')
        old_homepage.verify_property_dialog_value('Name', 'text_value', 'V5_Context_Menu_Testing','Step 04.04: Verify name', user_name='autoadmuser59')
        old_homepage.verify_created_modified_accessed_time_stamp_format('Created', 'admin', 'Step 04.05: Verify Created time stamp')
        old_homepage.verify_created_modified_accessed_time_stamp_format('Modified', 'autoadmuser59', 'Step 04.06: Verify Modified time stamp')
        old_homepage.verify_created_modified_accessed_time_stamp_format('Accessed', 'autoadmuser59', 'Step 04.07: Verify Accessed time stamp')
        old_homepage.verify_property_dialog_value('Publish', 'radiobutton_value', 'Yes','Step 04.08: Verify publish is yes')
        old_homepage.verify_property_dialog_value('Show', 'radiobutton_value', 'Yes','Step 04.09: Verify Show is yes')
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 04.10: Verify save button disabled")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Cancel', 'enable', "Step 04.11: Verify cancel button enabled")
        expected_path= 'IBFS:/WFC/Repository/P406_S31920/G875179/V5_Context_Menu_Testing'
        old_homepage.verify_property_dialog_value('Path', 'text_value', expected_path,'Step 04.12: Verify path')
        old_homepage.verify_property_dialog_value('Summary', 'text_area' , '', 'Step 04.13: Verify Summary')
        old_homepage.verify_property_dialog_value('Owner','text',"-","Step 04.14:Verify the Owner tab")
        old_homepage.verify_property_dialog_enable_disable('Name', 'text_value', False, "Step 04.15: Verify Name - is disable.")
        old_homepage.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 04.16: Verify Show - is enabled.")
        old_homepage.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 04.17: Verify Show - is enabled.")
        utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)
        
        STEP_05 = """
        Click on the 'Advanced' tab
        """
        old_homepage.select_property_tab_value('Advanced')
        utils.capture_screenshot("05.00",STEP_05)
        
        STEP_05_01 =  """
        Verify all the options under 'Advanced tab' as per in the screenshot
        """
        old_homepage.verify_selected_tab_in_property_dialog("Advanced", "Step 05.01: property tab verification")
        old_homepage.verify_label_in_property_dialog('Advanced', 'Folder Properties', '05.02')
        old_homepage.verify_property_dialog_enable_disable('Allow personal pages', 'radiobutton_value', False, 'Step 05.03: Verify Allow personal pages is Disabled', tab_name='Advanced')
        old_homepage.verify_property_dialog_enable_disable('Automatically open', 'check_box', False, 'Step 05.04: Verify Automatically Open is enabled', tab_name='Advanced')
        old_homepage.verify_label_in_property_dialog('Advanced', 'Explorer/Portal Properties', '05.05')
        old_homepage.verify_property_dialog_enable_disable('Thumbnail', 'radiobutton_value', False, "Step 05.06: Verify Thumbnail - is enabled.",tab_name='Advanced')
        thumbnail_row_obj=page.get_property_dialog_rows_object('Advanced','Thumbnail', '05.07')
        radio_options=thumbnail_row_obj.find_elements_by_css_selector(radio_button_css)
        actual_thumbnail_radiobutton_options=[elem.text.strip() for elem in radio_options]
        expected_thumbnail_radiobutton_options=['Default', 'Embedded', 'Link']
        utils.as_List_equal(expected_thumbnail_radiobutton_options, actual_thumbnail_radiobutton_options, "Step 05.08: Verify Thumbnail (Default, Embedded, Link radio buttons).")
        default_radiobutton_obj=radio_options[expected_thumbnail_radiobutton_options.index('Default')].find_element_by_css_selector("[class^='ibx-radio-button']")
        if 'ibx-radio-button-simple-marker-check' in j_script.get_element_all_attributes(default_radiobutton_obj)['class']:
            default_radiobutton_status='checked'
        else:
            default_radiobutton_status='unchecked'
        utils.asequal('checked', default_radiobutton_status, "Step 05.09: Verify Thumbnail Default is selected.")
        old_homepage.verify_property_dialog_value('Sort order', 'text_value', '','Step 05.10: Sort Order verification',tab_name='Advanced')
        old_homepage.verify_property_dialog_enable_disable('Language', 'text', False, "Step 05.11: Verify View All - is enabled.",tab_name='Advanced')
        old_homepage.verify_label_in_property_dialog('Advanced', 'Search Properties', '05.12')
        old_homepage.verify_property_dialog_value('Tags', 'text_value', '','Step 05.13: Tags verification',tab_name='Advanced')
        utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
            Step 06 : Click Cancel to close the properties dialog box
        """
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        utils.synchronize_until_element_disappear(tab_css, 30)
        utils.capture_screenshot("06.00",STEP_06)
        
        STEP_07 = """
            Step 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)

if __name__ == "__main__":
    unittest.main()  