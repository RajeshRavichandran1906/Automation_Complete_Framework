'''
Created on November 14, 2018

@author: varun
Testcase Name : Verify shared personal pages using Link to an existing page
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779801
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.pages import portal_canvas,portal_sidebar
from common.lib.webfocus import resource_dialog

class C6779801_TestClass(BaseTestCase):
    
    def test_C6779801(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_canvas_obj = portal_canvas.Portal_canvas(self.driver)
        portal_sidebar_object = portal_sidebar.Two_Level_SideBar(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        resource_object = resource_dialog.Resource_Dialog(self.driver)
        page_title = "New Page"
        page_title_css=".ibx-title-bar-caption .ibx-label-text"
        link_text = "Link to an existing page"
        link_text_css=".np-open .ibx-label-text"
        item_options = ".np-item"
        dialog_box_title = ".open-dialog-resources .ibx-title-bar-caption .ibx-label-text"
        retail_samples_css = "div[title=\"Retail Samples\"] .ibx-label-text"
        info_apps_css = "div[title=\"InfoApps\"] .ibx-label-text"
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        domains_css = "div[title='Domains'] .ibx-label-text"
        select_button_css =".ibx-dialog-ok-button:not([style*='none'])"
        dialog_css = ".ibx-dialog-title-box"
        pd_title_css = ".pd-page-title .ibx-label-text"
        after_share_css = ".pd-header-button-share"
        drop_down_css = ".Share-with-menu-btn"
        menu_item_text_css = "div[data-ibx-type=\"ibxCheckMenuItem\"]"
        user_popup_css = ".Share-with-others-menu"
        folders_css = ".content-title-label .ibx-label-text"
        text_to_type_css = ".ibx-widget .share-with-txt-search"
        user_css = ".share-with-dropdown .item-user-group .sw-item-desc"
        container_dialog_css = ".share-with-container-dialog"
        shared_with_text_css = ".share-with-title .ibx-label-text"
        ok_css = ".ibx-dialog-ok-button .ibx-label-text"
        plus_icon_css = ".bundle-folder-pgbuilder"
        user_name_css = "#SignonUserName"
        shared_content_css = "div[title='Shared Content'] .ibx-label-text"
        adm_user = core_util_obj.parseinitfile('mrid')
        containers_title=['Category Sales','Regional Sales Trend','Discount by Region','Regional Profit by Category',
                          'Example of a Tab Container','Example of a Carousel Container']
        
        """
        Step 1: Sign in to WebFOCUS as Admin user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
          
        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, 'Domains',Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('Domains->P292_S19901_G520454')
          
        """
        Step 3: Right click on 'V5 Portal Share' from the content area > Run.
        """
        util_obj.synchronize_with_visble_text(folders_css,'Folders', Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share', 'Run')
        core_util_obj.switch_to_new_window()
          
        """
        Step 4: Click on + Sign from the sidebar
        Verify 'New Page' dialog appears with 'Link to an existing page' and 'four templates'
        """
        util_obj.synchronize_with_number_of_element(plus_icon_css,1, Global_variables.mediumwait)
        plus_element = util_obj.validate_and_get_webdriver_object(plus_icon_css,'plus-button')
        core_util_obj.python_left_click(plus_element)
        util_obj.synchronize_with_number_of_element(dialog_css,1,60)
        title_element_text = util_obj.validate_and_get_webdriver_object(page_title_css,"page_title").text
        util_obj.asequal(page_title,title_element_text,"Step 4.1: verify dialog box title")
        link_element_text = util_obj.validate_and_get_webdriver_object(link_text_css, "link text").text
        util_obj.asequal(link_text,link_element_text,"Step 4.2: verify link element text")
        total_items = len(util_obj.validate_and_get_webdriver_objects(item_options, 'total items'))
        util_obj.asequal(total_items,4,'Step 4.3: Verify the 4 items are displayed')
          
        """
        Step 5: Select 'Link to an existing page'
        Verify Selection browser window opens
        """
        core_util_obj.python_left_click(util_obj.validate_and_get_webdriver_object(link_text_css, "link text"))
        util_obj.synchronize_with_number_of_element(dialog_box_title,1 , Global_variables.mediumwait)
        dialog_box_element = util_obj.validate_and_get_webdriver_object(dialog_box_title, "dialog_title").text
        util_obj.asequal(dialog_box_element,'Select',"Step 5.1: Verify selection window opens")
          
        """
        Step 6: Navigate to Retail Samples domain > InfoApps folder > select 'Sales Dashboard (Filtered)' page > Click on Select button
        Verify 'Sales Dashboard (Filtere...' appear in the sidebar and 'Retail Sales Dashboard' appear as a title in the canvas. Also, 
        it shows additionally 'Show Filters' in the personal page toolbar
        """
        resource_object.select_crumb_item("Domains")
        util_obj.synchronize_with_visble_text(folders_css, 'Folders',Global_variables.longwait)
        resource_object.select_resource_from_gridview('Retail Samples',selection_type='double')
        util_obj.synchronize_with_visble_text(retail_samples_css, 'Retail Samples',Global_variables.mediumwait)
        resource_object.select_resource_from_gridview('InfoApps',selection_type='double')
        util_obj.synchronize_with_visble_text(info_apps_css, 'InfoApps',Global_variables.mediumwait)
        resource_object.select_resource_from_gridview('Sales Dashboard (Filtered)')
        select_element = util_obj.validate_and_get_webdriver_object(select_button_css, "Select")
        core_util_obj.python_left_click(select_element)
        util_obj.synchronize_with_visble_text(pd_title_css, 'Retail Sales Dashboard',60)
        portal_sidebar_object.verify_pages_in_folder('My Pages',['Sales Dashboard (Filtered)'], msg="Step 6.1: Verify Sales dashboard in side bar", assert_type='asin')
        portal_canvas_obj.verify_page_header_title("Retail Sales Dashboard", "Step 6.2: Verify Title matches")
        portal_canvas_obj.verify_page_header_buttons(['Show filters'], "Step 6.3: Verify Filter present", assert_type='asin')
  
        """
        Step 7: Click on Share button from the personal page toolbar
        """
        util_obj.synchronize_with_number_of_element("div[title='Share']", 1, Global_variables.mediumwait)
        portal_canvas_obj.click_on_page_header_button('Share')
          
        """
        Step 8: Click on drop-down in the search box > Choose Users in the drop-down list
        """
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css, "drop_down_element")
        core_util_obj.python_left_click(drop_down_button)
        util_obj.synchronize_with_number_of_element(user_popup_css, 1, Global_variables.shortwait)
        user_items = util_obj.validate_and_get_webdriver_objects(menu_item_text_css, "menu_item")
        for element in user_items:
            if element.text.strip() == 'Users':
                core_util_obj.python_left_click(element)
          
        """
        Step 9: Enter 'autodevuser82' user in the 'Enter user' search box
        """
        ### send_keys is used, as other functions are failing in high load
        input_element = util_obj.validate_and_get_webdriver_object(text_to_type_css,'text-css')
        core_util_obj.python_left_click(input_element)
        input_element.send_keys('autodevuser82') 
        util_obj.synchronize_with_number_of_element(container_dialog_css, 1 , Global_variables.shortwait)
          
        """
        Step 10: Click on 'autodevuser82' user > Click OK to close the 'Share with Others' dialog
        Verify after sharing 'Share icon' is changed into blue color
        """
        user_elements = util_obj.validate_and_get_webdriver_objects(user_css,"Basic_users")
        for element in user_elements:
            if element.text.strip() == 'autodevuser82':
                core_util_obj.python_left_click(element)
        util_obj.synchronize_with_visble_text(shared_with_text_css,'Shared with', Global_variables.shortwait )
        ok_element= util_obj.validate_and_get_webdriver_object(ok_css,"ok-element")
        core_util_obj.python_left_click(ok_element)
        util_obj.synchronize_with_number_of_element(after_share_css, 1, Global_variables.mediumwait)
        util_obj.verify_element_color_using_css_property(after_share_css, 'bright_cyan', "Step 10.1: Verify the blue color in share button",attribute='color')
          
        """
        Step 11: Close the portal run window
        """
        core_util_obj.switch_to_previous_window()
          
        """
        Step 12: Signout as Admin and Sigin as developer user
        """
        main_page_obj.signout_from_username_dropdown_menu()
        util_obj.synchronize_with_number_of_element(user_name_css, 1, Global_variables.longwait)
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 13: Expand the domain from the tree and click on 'P292_S19901_G520454'
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, 'Domains',Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('Domains->P292_S19901_G520454')
        
        """
        Step 14: Right click on 'V5 Portal Share' from the content area > Run and Click on + Sign from the sidebar > select 'Link to an existing page'
        Verify Selection browser window opens with Repository and Shared Pages tabs
        """
        util_obj.synchronize_with_visble_text(folders_css,'Folders', Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share', 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(plus_icon_css,1, Global_variables.mediumwait)
        plus_element = util_obj.validate_and_get_webdriver_object(plus_icon_css,'plus-button')
        core_util_obj.python_left_click(plus_element)
        util_obj.synchronize_with_number_of_element(dialog_css,1,60)
        core_util_obj.python_left_click(util_obj.validate_and_get_webdriver_object(link_text_css, "link text"))
        util_obj.synchronize_with_number_of_element(dialog_box_title,1 , Global_variables.mediumwait)
        dialog_box_element = util_obj.validate_and_get_webdriver_object(dialog_box_title, "dialog_title").text
        util_obj.asequal(dialog_box_element,'Select',"Step 14.1: Verify selection window opens")
         
        """
        Step 15: Click on 'Shared Pages' tab > double click on 'Administrator'
        Verify shared 'Sales Dashboard' page appears
        """
        resource_object.select_tab_button("Shared Pages")
        util_obj.synchronize_with_visble_text(shared_content_css, 'Shared Content', Global_variables.mediumwait)
        resource_object.select_resource_from_gridview(adm_user,selection_type='double')
         
        """
        Step 16: Select 'Sales Dashboard' > click 'Select' button
        Verify shared 'Retail Sales Dashboard' page appears in the canvas
        """
        resource_object.select_resource_from_gridview('Sales Dashboard (Filtered)')
        select_element = util_obj.validate_and_get_webdriver_object(select_button_css, "Select")
        core_util_obj.python_left_click(select_element)
        util_obj.synchronize_with_visble_text(pd_title_css, 'Retail Sales Dashboard',60)
        portal_canvas_obj.verify_page_header_title("Retail Sales Dashboard", "Step 16.1: Verify Title matches")
        portal_canvas_obj.verify_containers_title(containers_title,"Step 16.2: Verify container's title")
        
        """
        Step 17: Close the portal run window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 18: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 