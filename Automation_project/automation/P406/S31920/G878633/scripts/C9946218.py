"""----------------------------------------------------
Author Name  : Robert
Automated on : 10-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.javascript import JavaScript
from common.pages.wf_mainpage import Wf_Mainpage as pages

class C9946218_TestClass(BaseTestCase):
    
    def test_C9946218(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        old_homepage = Wf_Mainpage(self.driver)
        page = pages(self.driver)
        j_script = JavaScript(self.driver)
       
        """
            TESTCASE VARIABLES
        """
        PORTAL_NAME="V5Portal_Context"
        TAB_CSS = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        RADIO_BUTTON_CSS=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"

        
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : Click on 'My Workspaces' view
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5Portal_Context' > Select 'Properties'
        """
        HomePage.MyWorkspace.right_click_on_item(PORTAL_NAME)
        HomePage.ContextMenu.select("Properties")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that Properties dialog opens with the three tabs are 'General' (Selected by default), 'Advanced' and 'Server.
                        Verify all the options under the 'General' tab as per in the screenshot
        """
        HomePage.Home._utils.synchronize_with_number_of_element(TAB_CSS, 3,90)
        old_homepage.verify_selected_tab_in_property_dialog("General", "Step 3.1: propery tab verification")
        old_homepage.verify_property_dialog_tab_list(['General','Advanced','Server'], "Step 3.2: tab list verification")
        old_homepage.verify_property_dialog_value('Title', 'text_value', "V5 Context Menu Testing","Step 3.3:Verify the title tab")
        old_homepage.verify_property_dialog_value('Name', 'text_value', "V5_Context_Menu_Testing","Step 3.4:Verify the Name tab")
        old_homepage.verify_property_dialog_enable_disable('Name', 'text_value', False, "Step 3.5: Verify Name - is disable.")
        old_homepage.verify_property_dialog_value('Summary', 'text_area',"","Step 3.6:Verify the Summary tab")
        old_homepage.verify_property_dialog_value('Path', 'text_value', "IBFS:/WFC/Repository/P406_S31920/~autoadmuser59/"+PORTAL_NAME,"Step 3.7:Verify the Path tab")
        old_homepage.verify_property_dialog_value('Owner','text',"autoadmuser59","Step 3.8:Verify the Owner tab")
        old_homepage.verify_created_modified_accessed_time_stamp_format('Date created','autoadmuser59',"step 3.9 verify the created tab value")
        old_homepage.verify_created_modified_accessed_time_stamp_format('Last modified','autoadmuser59',"step 3.10 verify the Modified tab value")
        old_homepage.verify_created_modified_accessed_time_stamp_format('Accessed','autoadmuser59',"step 3.11 verify the Accessed tab value")
        old_homepage.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 3.12: Verify Publish - is enabled.")
        old_homepage.verify_property_dialog_value('Publish','radiobutton_value','Yes',"Step 3.13: Verify Publish - is available")
        old_homepage.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 3.14: Verify Publish - is enabled.")
        old_homepage.verify_property_dialog_value('Show','radiobutton_value','Yes',"Step 3.15: Verify Show - is enabled.")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 03.16: Verify save button disabled")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Cancel', 'enable', "Step 03.17: Verify cancel button enabled")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)

        
        STEP_04 = """
            STEP 04.00 : Click on the 'Advanced' tab
        """
        old_homepage.select_property_tab_value("Advanced")
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify all the options under 'Advanced tab' as per in the screenshot
        """
        old_homepage.verify_selected_tab_in_property_dialog("Advanced", "Step 4.1: property tab verification")
        old_homepage.verify_label_in_property_dialog('Advanced', 'Folder Properties', 'Step 4.2: Folder label verification')
        old_homepage.verify_property_dialog_enable_disable('Allow personal pages', 'check_box', False, 'Step 4.3: Verify Allow personal pages is Disabled', tab_name='Advanced')
        old_homepage.verify_property_dialog_enable_disable('Automatically open', 'check_box', False, 'Step 4.4: Verify Automatically Open is enabled', tab_name='Advanced')
        old_homepage.verify_label_in_property_dialog('Advanced', 'Explorer/Portal Properties', 'Step 4.5: Explorer label verification')
        old_homepage.verify_property_dialog_enable_disable('Thumbnail', 'radiobutton_value', False, "Step 4.6: Verify Thumbnail - is enabled.",tab_name='Advanced')
        thumbnail_row_obj=page.get_property_dialog_rows_object('Advanced','Thumbnail', '4.7')
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
        old_homepage.verify_property_dialog_enable_disable('Language', 'text', False, "Step 4.11: Verify View All - is enabled.",tab_name='Advanced')
        old_homepage.verify_label_in_property_dialog('Advanced', 'Search Properties', 'Step 4.12:Search properties label verification')
        old_homepage.verify_property_dialog_value('Tags', 'text_value', '','Step 4.13: Tags verification',tab_name='Advanced')
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', 'Step 4.14: Save button disable verfication')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)

        STEP_05 = """
            STEP 05.00 : Click on the 'Server' tab
        """
        old_homepage.select_property_tab_value("Server")
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify all the options under 'Server tab' as per in the screenshot
        """
        old_homepage.verify_selected_tab_in_property_dialog("Server", "Step 5.1: propery tab verification")
        old_homepage.verify_property_dialog_enable_disable('Assign Server', 'check_box', False, 'Step 5.2: Verify Assign Server is Disabled', tab_name='Server')
        old_homepage.verify_property_dialog_enable_disable('EDASERVE', 'check_box', False, 'Step 5.3: Verify EDASERVE is Disabled', tab_name='Server')
        old_homepage.verify_property_dialog_enable_disable('Assign Application Path', 'check_box', False, 'Step 5.4: Verify Assign Application Path is disabled', tab_name='Server')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
        
        
        STEP_06 = """
            STEP 06.00 : Click Cancel to close the properties dialog box
        """
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        HomePage.Home._utils.synchronize_until_element_disappear(TAB_CSS, 30)
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)

        STEP_07 = """
            STEP 07.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
