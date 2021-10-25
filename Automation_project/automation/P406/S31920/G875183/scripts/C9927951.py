"""-------------------------------------------------------------------------------------------
Author Name : Robert/Rajesh
Automated On : 03 February 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9927951_TestClass(BaseTestCase):
    
    def test_C9927951(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        old_homepage = Wf_Mainpage(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        date_created_css = ".properties-general-file-created"
        last_modified_css = ".properties-general-LastModified"
        sort_order_input_css = ".properties-advanced-sort-order-item input"
        menu_icon_css = ".properties-advanced-menu-icon-item input"
        tag_css = ".properties-advanced-item-fex div[data-ibxp-placeholder='Enter comma separated values'] input"
        localization_button_css = ".properties-advanced-item-fex .properties-general-language-button-view"
        english_css = ".properties-advanced-item-fex .properties-advanced-returned-language"
        name_edit_button_css = ".properties-general-name-button-edit"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developers User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
 
        STEP_02 = """
            STEP 02 : From the 'WebFOCUS Home' tab, Under 'FAVORITES' section carousel > Right-click on 'V5 Context Menu Testing' > Click Properties
        """
        HomePage.Home.Favorites.right_click_on_item("V5 Context Menu Testing")
        HomePage.ContextMenu.select("Properties")
        utils.synchronize_with_visble_text(".properties-general-cancel-button", "Cancel", 30)
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify that properties dialog box opens with two tabs are General (By default selected) and Advanced.
            Verify that all the options appear under General tab as same in the below screenshot
            (Note: 1. Dates on this image will be different when this is being run
            2. For IE browser, refer the comment)
        """
        expected_tab = ['General', 'Advanced']
        old_homepage.verify_property_dialog_tab_list(expected_tab, "STEP 02.01 : Verify that properties dialog box opens with two tabs are General")
        old_homepage.verify_selected_tab_in_property_dialog('General', 'STEP 02.02 : Verify that properties dialog box opens with two tabs are General')
        old_homepage.verify_property_dialog_value('Title', 'text_value', 'V5 Context Menu Testing','Step 02.03: Verify title', user_name='autodevuser204')
        old_homepage.verify_property_dialog_value('Name', 'text_value', '2340005557','Step 02.04: Verify name', user_name='autodevuser204')
        old_homepage.verify_property_dialog_value('Summary', 'text_area' , '', 'Step 02.05: Verify Summary')
        expected_path= 'IBFS:/WFC/UserInfo/autodevuser204/Favorites/2340005557'
        old_homepage.verify_property_dialog_value('Path', 'text_value', expected_path,'Step 02.06: Verify path')
        expected_path = 'IBFS:/WFC/Repository/P406_S31920/G875179/V5_Context_Menu_Testing'
        old_homepage.verify_property_dialog_value('Target Path', 'text_value', expected_path,'Step 02.07: Verify path')
        old_homepage.verify_property_dialog_value('Tool', 'text', "", "Step 02.08 :Verify the Tool tab")
        old_homepage.verify_property_dialog_value('Owner', 'text', "autodevuser204","Step 02.09 :Verify the Owner tab")
        old_homepage.verify_property_dialog_value('Size', 'text', "-","Step 02.10 :Verify the Size tab")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 02.11: Verify save button disabled")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Cancel', 'enable', "Step 02.12: Verify cancel button enabled")
        date_created_obj = utils.validate_and_get_webdriver_object(date_created_css, "date created css")
        actual_output = date_created_obj.text
        msg = "Step 02.13 : Verify date created of file"
        utils.asequal(actual_output, "Tuesday, December 10, 2019 3:11:02 AM EST by autodevuser204", msg)
        last_modified_obj = utils.validate_and_get_webdriver_object(last_modified_css, "last modified css")
        actual_output = last_modified_obj.text
        msg = "Step 02.14 : Verify last modified of file"
        utils.asequal(actual_output, "Tuesday, December 10, 2019 3:11:02 AM EST by autodevuser204", msg)
        old_homepage.verify_label_in_property_dialog('General', 'Date created', '02.15')
        old_homepage.verify_label_in_property_dialog('General', 'Last modified', '02.16')
        name_edit_button_obj = utils.validate_and_get_webdriver_object(name_edit_button_css, "name edit button css")
        actual_output = name_edit_button_obj.get_attribute('role')
        msg = "Step 02.17 : Verify name edit button"
        utils.asequal(actual_output, "button", msg)
        utils.capture_screenshot("02.01", STEP_02_01, expected_image_verify = True)
        
        STEP_03 = """
            STEP 03 : Click the advanced tab
        """
        old_homepage.select_property_tab_value('Advanced')
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that all the options appear under Advanced tab as same in the below screenshot
        """
        old_homepage.verify_label_in_property_dialog("Advanced", "Home Page/Portal Properties", "03.01")
        old_homepage.verify_property_dialog_value('Sort order', 'text_value', '','Step 03.02 : Verify sort order', user_name='autodevuser204', tab_name = 'Advanced')
        old_homepage.verify_property_dialog_value('Menu Icon', 'text_value', '', 'Step 03.03 : Verify menu icon', user_name='autodevuser204', tab_name = 'Advanced')
        old_homepage.verify_property_dialog_value('Tags', 'text_value', '', 'Step 03.04 : Verify Tags',  user_name='autodevuser204', tab_name = 'Advanced')
        old_homepage.verify_selected_tab_in_property_dialog('Advanced', 'Step 03.05 : Verify Tab name')
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 03.06: Verify save button disabled")
        old_homepage.verify_property_dialog_save_cancel_button_enable_disable('Cancel', 'enable', "Step 03.07: Verify cancel button enabled")
        old_homepage.verify_label_in_property_dialog('Advanced', 'Localization',  '03.08')
        old_homepage.verify_label_in_property_dialog('Advanced', 'Search Properties',  '03.09')
        sort_order_obj = utils.validate_and_get_webdriver_object(sort_order_input_css, "sort order input css")
        actual_output = sort_order_obj.get_attribute('placeholder')
        msg = "Step 03.10 : Verify placeholder for sort order"
        utils.asequal(actual_output, 'Enter an integer value', msg)
        menu_icon_obj = utils.validate_and_get_webdriver_object(menu_icon_css, "menu icon input css")
        actual_output = menu_icon_obj.get_attribute('placeholder')
        msg = "Step 03.11 : Verify placeholder for menu icon"
        utils.asequal(actual_output, 'Enter CSS glyph classes', msg)
        tags_obj = utils.validate_and_get_webdriver_object(tag_css, "tag css")
        actual_output = tags_obj.get_attribute('placeholder')
        msg = "Step 03.12 : Verify placeholder for tags"
        utils.asequal(actual_output, 'Enter comma separated values', msg)
        localization_obj = utils.validate_and_get_webdriver_object(localization_button_css, "Localization css")
        actual_output = localization_obj.get_attribute('role')
        msg = "Step 03.13 : Verify localization button"
        utils.asequal(actual_output, 'button', msg)
        actual_output = localization_obj.text
        msg = "Step 03.14 : Verify localization button text"
        utils.asequal(actual_output, 'Manage options', msg)
        english_obj = utils.validate_and_get_webdriver_object(english_css, "english css")
        actual_output = english_obj.text
        msg = "Step 03.15 : Verify english text"
        utils.asequal(actual_output, "English", msg)
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04 : Click Cancel to close the properties dialog box
        """
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)
        
if __name__ == "__main__":
    unittest.main() 