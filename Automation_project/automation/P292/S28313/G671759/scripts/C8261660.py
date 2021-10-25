'''
Created on March 26,2019

@author: varun
Testcase Name : Test page themes
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261660
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.wftools.page_designer import Preview
from common.lib.global_variables import Global_variables

class C8261660_TestClass(BaseTestCase):
    
    def test_C8261660(self):
        """
        Test_case objects
        """
        page_preview_obj = Preview(self.driver)
        page_designer_obj = Design(self.driver)
        login_obj = Login(self.driver)
        main_page_obj = Wf_Mainpage(self.driver)
        util_obj = UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        repository_css = ".ibfs-tree"
        page_run_title_css = "div[data-ibx-name=\"_title\"]"
        
        def page_color(itemname, stepno):
             
            if Global_variables.browser_name == 'chrome':
                actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page", "page_tab"), 'background').strip().replace(' ','')
                if itemname == 'Designer 2018':
                    expected_color = 'rgba(0,0,0,0)nonerepeatscroll0%0%/autopadding-boxborder-box'
                elif itemname == 'Light':  
                    expected_color = 'rgb(255,255,255)nonerepeatscroll0%0%/autopadding-boxborder-box'
                elif itemname == 'Midnight': 
                    expected_color = 'rgba(0,0,0,0)linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)repeatscroll0%0%/autopadding-boxborder-box'
                
            else:
                if itemname == 'Designer 2018':
                    expected_color = 'rgba(0,0,0,0)'
                    actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page-canvas", "page_canvas"), 'background-color').strip().replace(' ','')
                elif itemname == 'Light':
                    expected_color = 'rgb(255,255,255)'
                    actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page-tab-content-wrapper", "page_tab"), 'background-color').strip().replace(' ','')
                elif itemname == 'Midnight':       
                    expected_color = 'linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)'
                    actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page-tab-content-wrapper", "page_tab"), 'background-image').strip().replace(' ','')
            util_obj.asequal(expected_color, actual_color, "Step {0}: Verify whether background has {1} theme".format(stepno, itemname))
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'V5 Domain Testing' -> v5portal1 -> v5folder1 -> v5subfolder1
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains->V5 Domain Testing->v5portal1->v5folder1->v5subfolder1')
        
        """
        Step 4: Right click on 'Page default ' and click Run          
        Verify page appears as below
        """
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"] ", 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page Default', 'Run')
        util_obj.synchronize_with_number_of_element('.ibx-iframe-frame', 1, main_page_obj.home_page_medium_timesleep)
        core_util_obj.switch_to_frame(".ibx-iframe-frame")
        page_title = util_obj.validate_and_get_webdriver_object(page_run_title_css, "page_title").text.strip()
        util_obj.asequal(page_title, "Page Heading", "Step 04.00: Verify the page run title")
        
        """
        Step 5: Close page
        """
        core_util_obj.switch_to_default_content()
        close_button = util_obj.validate_and_get_webdriver_object("div[title='Close']", 'closebutton')
        core_util_obj.left_click(close_button)
        
        """
        Step 6: Right click on 'Page default ' and click Edit
        """
        main_page_obj.right_click_folder_item_and_select_menu('Page Default', 'Edit')
        core_util_obj.switch_to_new_window()
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(".pd-page-title", "Page Heading", main_page_obj.home_page_medium_timesleep)

        """
        Step 7: Click on Properties pane -> Style
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab('style')   
        
        """
        Step 8: Click on Theme drop down and select Light
        Verify theme is applied in design time
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Light')
        page_color('Light','08.00')
        
        """
        Step 9: Click Preview
        Verify page appears as below
        """
        page_designer_obj.click_preview()
        page_obj = util_obj.validate_and_get_webdriver_object("div[data-ibx-name=\"_title\"]", "page_heading").text.strip()
        util_obj.asequal(page_obj, 'Page Heading', "Step 09.00: Verify the new page heading")
        page_color('Light','09.01')
        
        """
        Step 10: Click on <- to bring back to designer
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """
        Step 11: Click on Theme drop down and select Midnight
        Verify theme is applied in design time
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Midnight')
        page_color('Midnight','11.00')
        
        """
        Step 12: Click Preview
        Verify page appears as below
        """
        page_designer_obj.click_preview()
        page_obj = util_obj.validate_and_get_webdriver_object("div[data-ibx-name=\"_title\"]", "page_heading").text.strip()
        util_obj.asequal(page_obj, 'Page Heading', "Step 12.00: Verify the new page heading")
        page_color('Midnight','12.01')
        
        """
        Step 13: Click on <- to bring back to designer
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """
        Step 14: Click on Theme drop down and select 'Designer 2018'
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Designer 2018')
        
        """
        Step 15: Close without saving
        """
        page_designer_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(window_close=False)
        core_util_obj.switch_to_default_content()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 16: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    