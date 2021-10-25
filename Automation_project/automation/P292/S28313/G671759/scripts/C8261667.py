'''
Created on March 28,2019

@author: Niranjan
Testcase Name : Create page with InfoApp 1 templates and change Page Theme to Midnight
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261667
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools import page_designer
import time
import sys
from common.pages.wf_mainpage import Wf_Mainpage
from common.lib.global_variables import Global_variables
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as system_keybord

class C8261667_TestClass(BaseTestCase):
    
    def test_C8261667(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        main_pages_obj = Wf_Mainpage(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        template_prompt_css ="[class*='pop-top']"
        style_tab_css = "[class*= 'ibx-glyph-paint-brush']"
        page_canvas_css = "[class*='pd-page-canvas']"
        close_css = ".pop-top  [class*='close-button']"
        frame_css = "iframe[src*='V5_Domain_Testing']"
        
        """
        Test case variables
        """
        expected_domain = "V5 Domain Testing"
        expected_portal = 'v5portal1'
        expected_theme = 'Midnight'
        expected_page_heading = ['Page Heading']

        def page_color():
            
             
            if Global_variables.browser_name == 'chrome':
                sweet_pink_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color5', 'Run page')
                actual_color = sweet_pink_ele.value_of_css_property('background').strip().replace(' ', '')
                expected_color = 'rgba(0,0,0,0)linear-gradient(rgba(249,144,144,0.4)0%,rgba(249,144,144,0.6)100%)repeatscroll0%0%/autopadding-boxborder-box'
                util_obj.asequal(actual_color, expected_color, 'Step 09.01: Verify the Sweet Pink color in top section')
                
                summer_sky_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color2', 'Run page')
                actual_color = summer_sky_ele.value_of_css_property('background').strip().replace(' ','') 
                expected_color = 'rgba(0,0,0,0)linear-gradient(rgba(1,96,178,0.4)0%,rgba(32,157,225,0.7)100%)repeatscroll0%0%/autopadding-boxborder-box'
                util_obj.asequal(actual_color, expected_color, 'Step 09.02 : Verify Summer Sky color in second section')
                
                white_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-default-color','Run page')
                actual_color = white_ele.value_of_css_property('background').strip().replace(' ', '')
                expected_color = 'rgba(0,0,0,0)linear-gradient(rgba(255,255,255,0.2)0%,rgba(255,255,255,0.4)100%)repeatscroll0%0%/autopadding-boxborder-box'
                util_obj.asequal(actual_color, expected_color, 'Step 09.03 : Verify white color in second section')
                
                expected_color = 'rgba(0,0,0,0)linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)repeatscroll0%0%/autopadding-boxborder-box'
                actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page-runner", "page_tab"), 'background').strip().replace(' ','')
            else:  
                sweet_pink_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color5', 'Run page')
                actual_color = sweet_pink_ele.value_of_css_property('background-image').strip().replace(' ', '')
                expected_color = 'linear-gradient(rgba(249,144,144,0.4)0%,rgba(249,144,144,0.6)100%)'
                util_obj.asequal(actual_color, expected_color, 'Step 09.01: Verify the Sweet Pink color in top section')
                
                summer_sky_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color2', 'Run page')
                actual_color = summer_sky_ele.value_of_css_property('background-image').strip().replace(' ','') 
                expected_color = 'linear-gradient(rgba(1,96,178,0.4)0%,rgba(32,157,225,0.7)100%)'
                util_obj.asequal(actual_color, expected_color, 'Step 09.02 : Verify Summer Sky color in second section')
                
                white_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-default-color','Run page')
                actual_color = white_ele.value_of_css_property('background-image').strip().replace(' ', '')
                expected_color = 'linear-gradient(rgba(255,255,255,0.2)0%,rgba(255,255,255,0.4)100%)'
                util_obj.asequal(actual_color, expected_color, 'Step 09.03 : Verify white color in second section')
                expected_color = 'linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)'
                actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page-runner", "page_tab"), 'background-image').strip().replace(' ','')
            
            util_obj.asequal(expected_color, actual_color, "Step 09.04 : Verify background theme of page")
        
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 3: Click on 'V5 Domain Testing' -> 'v5portal1' and choose Page tile from action bar
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_portal)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        
        """
        Step 4: Choose 'InfoApp 1' template
        """
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(template_prompt_css, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('InfoApp 1')
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_medium_timesleep)
 
        """
        Step 5: Click on Properties panel -> Style
        """
        page_designer_obj.click_property()
        util_obj.synchronize_until_element_is_visible(style_tab_css, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_property_tab('style')
 
        """
        Step 6: Click on Theme drop down and select 'Midnight'
        Verify Midnight theme has been selected as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', expected_theme)
        time.sleep(5)
        page_designer_obj.verify_setting_tab_properties('Page Style', ['Theme=Midnight', 'Margin=off', 'Maximum width=off'], 'Step 06.01 : Verify Midnight theme has been selected', property_tab_name='style')
        
        """
        Step 7: Click save;
        Enter 'Page InfoApp 1' and click save button
        """
        page_designer_obj.save_page_from_toolbar('Page InfoApp 1')
         
        """
        Step 8: Close designer
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9: Right click on 'Page InfoApp 1' and click Run
        Verify page appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu('Page InfoApp 1', 'Run')
        util_obj.synchronize_until_element_is_visible(frame_css, main_page_obj.home_page_medium_timesleep)
        core_utill_obj.switch_to_frame(frame_css)
        page_designer_obj.verify_page_heading_title(expected_page_heading, 'Step 09.00 : Verify page heading')
        page_color()
        core_utill_obj.switch_to_default_content()
        
        """
        Step 10: Close page
        """
        close_btn = util_obj.validate_and_get_webdriver_object(close_css, "close button")
        core_utill_obj.left_click(close_btn)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 11: Multi select 'Page Blank', 'Page Grid 2-1','Page Grid 2-1 Side','Page Grid 3-3-3', 
                'Page Grid 4-2-1', 'Page InfoApp 1' pages; Right click and select Publish
        Verify all pages are published and appears as below
        """
        main_page_obj.expand_repository_folder('Domains'+'->'+expected_domain+'->'+expected_portal)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        try:
            if sys.platform == 'linux':
                pykeyboard.press_key(pykeyboard.control_key)
            else:
                system_keybord.press('ctrl')
            pages_obj = main_pages_obj.get_domain_folder_item('Page Blank')
            core_utill_obj.python_left_click(pages_obj)
            pages_obj = main_pages_obj.get_domain_folder_item('Page Grid 2-1')
            core_utill_obj.python_left_click(pages_obj)
            pages_obj = main_pages_obj.get_domain_folder_item('Page Grid 2-1 Side')
            core_utill_obj.python_left_click(pages_obj)
            pages_obj = main_pages_obj.get_domain_folder_item('Page Grid 3-3-3')
            core_utill_obj.python_left_click(pages_obj)
            pages_obj = main_pages_obj.get_domain_folder_item('Page Grid 4-2-1')
            core_utill_obj.python_left_click(pages_obj)
            pages_obj = main_pages_obj.get_domain_folder_item('Page InfoApp 1')
            core_utill_obj.python_left_click(pages_obj)
            time.sleep(5)
            main_page_obj.right_click_folder_item_and_select_menu('Page InfoApp 1', 'Publish')
        
        finally:
            if sys.platform == 'linux':
                pykeyboard.release_key(pykeyboard.control_key)
            else:
                system_keybord.release('ctrl')
        
        """
        Step 12: Signout WF
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()