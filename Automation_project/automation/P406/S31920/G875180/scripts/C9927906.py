"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 31 January 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.javascript import JavaScript
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.pages.wf_mainpage import Wf_Mainpage as pages
from common.wftools.wf_mainpage import Wf_Mainpage

class C9927906_TestClass(BaseTestCase):
    
    def test_C9927906(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        old_homepage = Wf_Mainpage(self.driver)
        page = pages(self.driver)
        j_script = JavaScript(self.driver)

        """
        TESTCASE VARIABLES
        """
        tab_css = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        radio_button_css=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        
        
        STEP_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
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
            Step 04 : Right-click on 'V5 Context Menu Testing' from the resource tree > Select 'Properties'
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875179")
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5 Context Menu Testing")
        HomePage.ContextMenu.select("Properties")
        utils.capture_screenshot("04.00", STEP_04)

        STEP_04_01 = """Verification - Verify that Properties dialog opens with the three tabs are 'General' (Selected by default), 'Advanced' and 'Server.
        Verify all the options under the 'General' tab as per in the screenshot
        """
        utils.synchronize_with_number_of_element(tab_css, 3,90)
        old_homepage.verify_selected_tab_in_property_dialog("General", "Step 4.1: propery tab verification")
        old_homepage.verify_property_dialog_tab_list(['General','Advanced','Server'], "Step 4.2: tab list verification")
        old_homepage.verify_property_dialog_value('Title', 'text_value', "V5 Context Menu Testing","Step 4.1:Verify the title tab")
        old_homepage.verify_property_dialog_value('Name', 'text_value', "V5_Context_Menu_Testing","Step 4.2:Verify the Name tab")
        old_homepage.verify_property_dialog_enable_disable('Name', 'text_value', False, "Step 4.3: Verify Name - is disable.")
        old_homepage.verify_property_dialog_value('Summary', 'text_area',"","Step 4.4:Verify the Summary tab")
        old_homepage.verify_property_dialog_value('Path', 'text_value', "IBFS:/WFC/Repository/P406_S31920/G875179/V5_Context_Menu_Testing","Step 4.5:Verify the Path tab")
        old_homepage.verify_property_dialog_value('Owner','text',"-","Step 4.6:Verify the Owner tab")
        old_homepage.verify_created_modified_accessed_time_stamp_format('Created','admin',"step 4.7 verify the created tab value")
        old_homepage.verify_created_modified_accessed_time_stamp_format('Modified','autoadmuser59',"step 4.8 verify the Modified tab value")
        old_homepage.verify_created_modified_accessed_time_stamp_format('Accessed','autoadmuser59',"step 4.9 verify the Accessed tab value")
        old_homepage.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 4.10: Verify Publish - is enabled.")
        old_homepage.verify_property_dialog_value('Publish','radiobutton_value','Yes',"Step 4.11: Verify Publish - is available")
        old_homepage.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 4.12: Verify Publish - is enabled.")
        old_homepage.verify_property_dialog_value('Show','radiobutton_value','Yes',"Step 4.13: Verify Show - is enabled.")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 04.14: Verify save button disabled")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Cancel', 'enable', "Step 04.15: Verify cancel button enabled")
        utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)
        
        STEP_05 = """
        Click on the 'Advanced' tab
        """
        utils.capture_screenshot("05.00",STEP_05)
        old_homepage.select_property_tab_value("Advanced")
        
        
        STEP_05_01 =  """
        Verify all the options under 'Advanced tab' as per in the screenshot
        """
        old_homepage.verify_selected_tab_in_property_dialog("Advanced", "Step 5.1: property tab verification")
        old_homepage.verify_label_in_property_dialog('Advanced', 'Folder Properties', 'Step 5.2: Folder label verification')
        old_homepage.verify_property_dialog_enable_disable('Allow personal pages', 'check_box', False, 'Step 5.3: Verify Allow personal pages is Disabled', tab_name='Advanced')
        old_homepage.verify_property_dialog_enable_disable('Automatically open', 'check_box', False, 'Step 5.4: Verify Automatically Open is enabled', tab_name='Advanced')
        old_homepage.verify_label_in_property_dialog('Advanced', 'Explorer/Portal Properties', 'Step 5.5: Explorer label verification')
        old_homepage.verify_property_dialog_enable_disable('Thumbnail', 'radiobutton_value', False, "Step 5.6: Verify Thumbnail - is enabled.",tab_name='Advanced')
        thumbnail_row_obj=page.get_property_dialog_rows_object('Advanced','Thumbnail', '5.7')
        radio_options=thumbnail_row_obj.find_elements_by_css_selector(radio_button_css)
        actual_thumbnail_radiobutton_options=[elem.text.strip() for elem in radio_options]
        expected_thumbnail_radiobutton_options=['Default', 'Embedded', 'Link']
        utils.as_List_equal(expected_thumbnail_radiobutton_options, actual_thumbnail_radiobutton_options, "Step 5.8: Verify Thumbnail (Default, Embedded, Link radio buttons).")
        default_radiobutton_obj=radio_options[expected_thumbnail_radiobutton_options.index('Default')].find_element_by_css_selector("[class^='ibx-radio-button']")
        if 'ibx-radio-button-simple-marker-check' in j_script.get_element_all_attributes(default_radiobutton_obj)['class']:
            default_radiobutton_status='checked'
        else:
            default_radiobutton_status='unchecked'
        utils.asequal('checked', default_radiobutton_status, "Step 5.9: Verify Thumbnail Default is selected.")
        old_homepage.verify_property_dialog_value('Sort order', 'text_value', '','Step 5.11: Sort Order verification',tab_name='Advanced')
        old_homepage.verify_property_dialog_enable_disable('Language', 'text', False, "Step 5.12: Verify View All - is enabled.",tab_name='Advanced')
        old_homepage.verify_label_in_property_dialog('Advanced', 'Search Properties', 'Step 5.13:Search properties label verification')
        old_homepage.verify_property_dialog_value('Tags', 'text_value', '','Step 5.14: Tags verification',tab_name='Advanced')
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', 'Step 5.15: Save button disable verfication')
        utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Click on the 'Server' tab
        """
        old_homepage.select_property_tab_value("Server")
        utils.capture_screenshot("06.00",STEP_06)
        
        STEP_06_01 = """
        Verify all the options under 'Server tab' as per in the screenshot
        """
        old_homepage.verify_selected_tab_in_property_dialog("Server", "Step 6.1: propery tab verification")
        old_homepage.verify_property_dialog_enable_disable('Assign Server', 'check_box', False, 'Step 6.2: Verify Assign Server is Disabled', tab_name='Server')
        old_homepage.verify_property_dialog_enable_disable('EDASERVE', 'check_box', False, 'Step 6.3: Verify EDASERVE is Disabled', tab_name='Server')
        old_homepage.verify_property_dialog_enable_disable('Assign Application Path', 'check_box', False, 'Step 6.4: Verify Assign Application Path is disabled', tab_name='Server')
        utils.capture_screenshot("06.01",STEP_06_01)
        
        STEP_07 = """
        Click Cancel to close the properties dialog box
        """
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        utils.synchronize_until_element_disappear(tab_css, 30)
        utils.capture_screenshot("07.00",STEP_07)
        
        STEP_08 = """
            Step 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)

if __name__ == "__main__":
    unittest.main() 