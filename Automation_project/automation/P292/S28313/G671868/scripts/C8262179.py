'''
Created on May 31, 2019.

@author: AA14564

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262179
TestCase Name = Row height section: The Px does not get added back after hitting the enter key like the page margin does
'''
import sys
import time
import unittest
from common.wftools.login import Login
from common.wftools import page_designer
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.core_utility import CoreUtillityMethods
from common.pages.page_designer_design import PageDesignerDesign
from common.locators.wf_mainpage_locators import WfMainPageLocators

if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class C8262179_TestClass(BaseTestCase):

    def test_C8262179(self):
        
        """
        TESTCASE OBJECTS
        """
        pd_design = page_designer.Design(self.driver)
        pd_run = page_designer.Run(self.driver)
        wf_login = Login(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        homepage = Wf_Mainpage(self.driver)
        homepage_locators = WfMainPageLocators()
        pd_designer_design = PageDesignerDesign(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".pd-page-canvas"
        settings_section_css = ".section-settings"
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_utils.parseinitfile('project_id')
        suite_id = core_utils.parseinitfile('suite_id')
        group_id = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        '''
        local methods
        '''
        def verify_setting_tab_properties(tab_name, property_name, expected, msg, property_tab_name='settings'):
            """
            Descriptions : This method used to verify specific setting tab properties
            example : verify_setting_tab_properties('General Settings', 'Row height', '30px', 'Step 06.3 : Verify General Settings properties')
            """
            tab_obj=pd_designer_design.get_setting_tab_object(tab_name, property_tab_name=property_tab_name)
            tab_properties_obj=utils.validate_and_get_webdriver_objects("div[data-ibx-type='ibxGrid']>div[class^='pd-ps'][data-ibx-row][data-ibx-col]", 'Grid', parent_object=tab_obj)
            for col in range(0, len(tab_properties_obj), 2):
                if tab_properties_obj[col].is_displayed()==True and tab_properties_obj[col].text == property_name:
                    textbox_obj=utils.validate_and_get_webdriver_object('input[type]', 'text box', parent_object=tab_properties_obj[col+1])
                    actual = utils.get_element_attribute(textbox_obj, 'value')
            utils.asequal(expected, actual, msg)
        
        
        Step1 = """
        Step 01: Login WF as domain developer
        """
        wf_login.invoke_home_page("mrid", "mrpass")
        utils.capture_screenshot('01.01', Step1)
        
        Step2 = """
        Step 02: Click on Content view from side bar
        """
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(homepage_locators.REPOSITORY_TREE_CSS, 1, pd_run.home_page_medium_timesleep)
        utils.capture_screenshot('02.01', Step2)
        
        Step3 = """
        Step 03: Click on 'P292_S28313' domain -> G671868 folder
        """
        homepage.click_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(homepage_locators.content_area_css, 'Designer', pd_run.home_page_medium_timesleep)
        utils.capture_screenshot('03.01', Step3)
        
        Step4 = """
        Step 04: Click on Page action tile from under Designer category
        """
        homepage.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(homepage_locators.content_area_css, 'Page', pd_run.home_page_medium_timesleep)
        homepage.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Grid 4-2-1', pd_run.home_page_medium_timesleep)
        utils.capture_screenshot('04.01', Step4)
        
        Step5 = """
        Step 05: Choose 'Grid 4-2-1' template
        """
        pd_design.select_page_designer_template('Grid 4-2-1')
        utils.synchronize_with_visble_text(containers_css, 'Panel 1', pd_run.home_page_medium_timesleep)
        utils.capture_screenshot('05.01', Step5)
        
        Step6 = """
        Step 06: Click the section area in the canvas and then open properties pane
        """
        pd_design.select_page_section(1, xoffset=6, yoffset=10)
        pd_design.click_property()
        utils.synchronize_with_visble_text(settings_section_css, 'Row height', pd_run.home_page_medium_timesleep)
        utils.capture_screenshot('06.01', Step6)
        
        Step7 = """
        Step 07: Enter 30 in the row height text box and hit enter
                Verify the value appears as '30px' now
        """
        pd_design.select_property_tab_settings_option('Section Settings', 'text_box', 'Row height', '30')
        time.sleep(3)
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard.send('enter')
        time.sleep(3)
        verify_setting_tab_properties('Section Settings', 'Row height', '30px', "Step 07.00 : Verify the value appears as '30px' now")
        utils.capture_screenshot('07.01', Step7, expected_image_verify=True)
        
        Step8 = """
        Step 08: Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(homepage_locators.content_area_css, 'Designer', pd_run.home_page_medium_timesleep)
        utils.capture_screenshot('08.01', Step8)
        
        Step9 = """
        Step 09: Signout WF
        """
        homepage.signout_from_username_dropdown_menu()
        utils.capture_screenshot('09.01', Step9)
      
if __name__ == '__main__':
    unittest.main()