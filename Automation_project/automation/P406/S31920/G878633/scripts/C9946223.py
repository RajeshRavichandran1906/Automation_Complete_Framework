"""-------------------------------------------------------------------------------------------
Author Name : Joyal
Automated On : Dec 1, 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.javascript import JavaScript
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9946223_TestClass(BaseTestCase):
    
    def test_C9946223(self):
        
        """
            TESTCASE OBJECTS
        """
        j_script = JavaScript(self.driver)
        HomePage = ParisHomePage(self.driver)
        old_homepage = Wf_Mainpage(self.driver)
        
        """
            TESTCASE CSS
        """
        TAB_CSS = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        expected_url = 'IBFS:/WFC/Repository/P406_S31920/~autodevuser204/Portal_Pages/V5Portal_Context'
        RADIO_BUTTON_CSS=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : Click on 'My Workspaces' view
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
            
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5Portal_Context' > Click Properties
        """
        HomePage.MyWorkspace.right_click_on_item("V5Portal_Context")
        HomePage.ContextMenu.select("Properties")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that Properties dialog opens with the two tabs are 'General' (Selected by default) and 'Advanced'.
            Verify all the options under the 'General' tab as per in the below screenshot
        """
        HomePage.Home._utils.synchronize_with_number_of_element(TAB_CSS, 2,90)
        old_homepage.verify_property_dialog_tab_list(['General','Advanced'], "Step 03.01: Verify two tabs General and Advanced")
        old_homepage.verify_selected_tab_in_property_dialog("General", "Step 03.02: General tab is selected by default")
        old_homepage.verify_property_dialog_value('Title', 'text_value', "V5Portal_Context","Step 03.03:Verify the title tab")
        old_homepage.verify_property_dialog_value('Name', 'text_value', "V5Portal_Context","Step 03.04:Verify the Name tab")
        old_homepage.verify_property_dialog_enable_disable('Name', 'text_value', False, "Step 03.05: Verify Name tab- is disabled")
        old_homepage.verify_property_dialog_value('Summary', 'text_area',"","Step 03.06:Verify the Summary tab")
        old_homepage.verify_property_dialog_value('Path', 'text_value', expected_url,"Step 03.07:Verify the Path tab")
        old_homepage.verify_created_modified_accessed_time_stamp_format('created','autodevuser204',"step 03.08 verify date created value")
        old_homepage.verify_created_modified_accessed_time_stamp_format('Last','autodevuser204',"step 03.09 verify last modified value")
        
        old_homepage.verify_property_dialog_value('Owner','text',"autodevuser204","Step 03.10:Verify the Owner tab")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 03.11: Verify save button disabled")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Cancel', 'enable', "Step 03.12: Verify cancel button enabled")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04.00 : Click on the 'Advanced' tab
        """
        old_homepage.select_property_tab_value("Advanced")
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify all the options under 'Advanced tab' as per in the screenshot
        """
        old_homepage.verify_selected_tab_in_property_dialog("Advanced", "Step 04.01: Advanced tab is selected")
        old_homepage.verify_label_in_property_dialog('Advanced', 'Folder Properties', 'Step 04.02: Folder label verification')

        old_homepage.verify_label_in_property_dialog('Advanced', 'Home Page/Portal Properties', 'Step 4.5')

        thumbnail_row_obj=old_homepage.get_property_dialog_rows_object('Advanced','Thumbnail', '4.7')
        radio_options=thumbnail_row_obj.find_elements_by_css_selector(RADIO_BUTTON_CSS)
        actual_thumbnail_radiobutton_options=[elem.text.strip() for elem in radio_options]
        expected_thumbnail_radiobutton_options=['Default', 'Embedded', 'Link']
        HomePage.Home._utils.as_List_equal(expected_thumbnail_radiobutton_options, actual_thumbnail_radiobutton_options, "Step 4.8: Verify Thumbnail (Default, Embedded, Link radio buttons).")
        default_radiobutton_obj=radio_options[expected_thumbnail_radiobutton_options.index('Default')].find_element_by_css_selector("[class^='ibx-radio-button']")
        if 'ibx-radio-button-simple-marker-check' in j_script.get_element_all_attributes(default_radiobutton_obj)['class']:
            default_radiobutton_status='checked'
        else:
            default_radiobutton_status='unchecked'
        HomePage.Home._utils.asequal('checked', default_radiobutton_status, "Step 4.9: Verify Thumbnail Default is selected.")
        old_homepage.verify_property_dialog_value('Sort order', 'text_value', '','Step 4.10: Sort Order verification',tab_name='Advanced')

        old_homepage.verify_label_in_property_dialog('Advanced', 'Search Properties', 'Step 4.12:Search properties label verification')
        old_homepage.verify_property_dialog_value('Tags', 'text_value', '','Step 4.13: Tags verification',tab_name='Advanced')
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', 'Step 4.14: Save button disable')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)

        STEP_05 = """
            STEP 05.00 : Click Cancel to close the properties dialog box
        """
        old_homepage.select_property_dialog_save_cancel_button('Cancel')
#         HomePage.ModalDailogs.V5Portal.CancelButton.click()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_05)
        
        
        STEP_06 = """
            STEP 06.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)