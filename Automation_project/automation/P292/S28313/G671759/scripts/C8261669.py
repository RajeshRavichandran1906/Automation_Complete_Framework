'''
Created on March 27,2019

@author: varun
Testcase Name : Edit folder/page and subfolder page
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261669
''' 
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.pages import wf_mainpage
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.lib.global_variables import Global_variables
import time, unittest

class C8261669_TestClass(BaseTestCase):
    
    def test_C8261669(self):
        """
        Test_case objects
        """
        home_page = wf_mainpage.Wf_Mainpage(self.driver)
        page_designer_obj = Design(self.driver)
        login_obj = Login(self.driver)
        main_page_obj = Wf_Mainpage(self.driver)
        util_obj = UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
         
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
        Step 3: Expand 'V5 Domain Testing' -> 'v5portal1'
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing->v5portal1')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
         
        """
        Step 4: Right click on 'Page Blank' and select Edit
        """
        main_page_obj.right_click_folder_item_and_select_menu('Page Blank', 'Edit')
         
        """
        Step 5: Click on Properties -> Style  
        Verify page appears as below
        """
        core_util_obj.switch_to_new_window()
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(".pd-page-title", "Page Heading", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab('style')       
        page_color('Designer 2018', '05.00')
        time.sleep(5)
         
        """
        Step 6: Click on Theme drop down and select Light
        Verify theme applied as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Light')
        util_obj.wait_for_page_loads(5)
        page_color('Light','06.00')
         
        """
        Step 7: Click on Theme drop down and select Midnight
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Midnight')
        util_obj.wait_for_page_loads(5)
        page_color('Midnight','07.00')
        
        """
        Step 8: Click on Theme drop down and select Designer 2018
        Verify theme applied as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Designer 2018')
        util_obj.wait_for_page_loads(5)
        page_color('Designer 2018','08.00')
         
        """
        Step 9: Close designer
        """
        page_designer_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(window_close=False)
        core_util_obj.switch_to_default_content()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
         
        """
        Step 10: Right click on 'Page Default' from under v5portal1-1 -> v5folder1 -> v5subfolder1 and select Edit
        """
#         main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing->v5portal1-1->v5folder1->v5subfolder1') Its clicking v5portal1 instead of v5portal1-1 hence changed as below 
        home_page.double_click_on_content_area_items('v5portal1-1', 'Workspaces->V5 Domain Testing')
        home_page.double_click_on_content_area_items('v5folder1')
        home_page.double_click_on_content_area_items('v5subfolder1')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page Default', 'Edit')
        
        """
        Step 11: Click on Properties -> Style       
        Verify page appears as below
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(".pd-page-title", "Page Heading", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab('style')
        page_color('Designer 2018','11.00')
        
        """
        Step 12: Click on Theme drop down and select Light
        Verify theme has been applied as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Light')
        util_obj.wait_for_page_loads(5)
        page_color('Light','12.00')
      
        """
        Step 13: Click on Theme drop down and select Midnight
        Verify theme has been applied as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Midnight')
        util_obj.wait_for_page_loads(5)
        page_color('Midnight','13.00')
      
        """
        Step 14: Click on Theme drop down and select Designer 2018   
        Verify theme has been applied as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Designer 2018')
        util_obj.wait_for_page_loads(5)
        page_color('Designer 2018','14.00')
       
        """
        Step 15: Close designer
        """
        page_designer_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(window_close=False)
        core_util_obj.switch_to_default_content()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 16: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()