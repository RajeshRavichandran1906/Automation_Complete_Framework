'''
Created on November 15, 2018

@author: vpriya
Testcase Name : Verify able to see after stop shared personal pages using link to an existing pages for multiple users
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779804
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.pages import portal_sidebar,portal_canvas
from common.lib.webfocus import resource_dialog

class C6779804_TestClass(BaseTestCase):
    
    def test_C6779804(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_sidebar_obj=portal_sidebar.Two_Level_SideBar(self.driver)
        portal_navi_obj=portal_sidebar.New_Page_Template_Window(self.driver)
        portal_canvas_obj=portal_canvas.Portal_canvas(self.driver)
        resource_dialog_obj=resource_dialog.Resource_Dialog(self.driver)
        Plus_css = "div[class*='bundle-folder-item bundle-folder-pgbuilder']"
        crumb_css = "div[data-ibx-type='breadCrumbTrail']"
        new_page_css = "div.new-page-from-template"
        folder_name_path="P292_S19901_G520454"
        template_names=['Grid 2-1','Grid 2-1 Side','Grid 3-3-3','Grid 4-2-1']
        link_text_css=".np-open .ibx-label-text"
        resource_tab_css=".open-dialog-resources.pop-top .ibx-csl-items-container .ibx-tab-button"
        resource_dialog_css='.open-dialog-resources.pop-top'
        sales_item_css="div[class*='file-item file-item-published file-item-shown ibx-widget']"
        retail_title_css=".pd-page-header"
        retail_title="Retail Sales Dashboard"
        containers_title=['Category Sales','Regional Sales Trend','Discount by Region','Regional Profit by Category','Example of a Tab Container','Example of a Carousel Container']
        Stop_share_css="div[title*=Stop]"
        pop_top_css="div[class*='share-with-others-dialog ibx-widget']"
        user_verify_top_css =".share-with-container .share-with-item .sw-item-desc"
        dev_user = core_util_obj.parseinitfile('mriddev')
        basic_user = 'autobasuser08'
        expected_user_list = [basic_user,dev_user]
        user_close_css="div[class*='item-close-icon fa fa-close']"
        user_no_visible_css=".share-with-container .share-with-item .sw-item-desc"
        ok_css='div[class*="ibx-dialog-ok-button"]'
        LONG_WAIT=120
        MEDIUM_WAIT=60
        
        
        """
        Step 1: Sign in to WebFOCUS as Admin user
        """
        login_obj.invoke_home_page('mrid','mrpass')
        util_obj.synchronize_with_number_of_element(crumb_css, 1, LONG_WAIT)
        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454''.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(crumb_css, '1',MEDIUM_WAIT)

        """
        Step 3. Right click on 'V5 Portal Share' from the content area > Run.
        Verify 'Sales Dashboard (Filtere..' appear in the sidebar and 'Retail Sales Dashboard' appear as a title in the canvas.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(Plus_css, '1',MEDIUM_WAIT)
        portal_sidebar_obj.verify_pages_in_folder('My Pages',['Sales Dashboard (Filtered)','+']," Step 3.1 Verify sidebar with My Pages and a + sign under it.", assert_type='asin')
        portal_canvas_obj.verify_page_header_title(retail_title,"Step 8:Verify shared 'Retail Sales Dashboard' page appears on the canvas")
        
        """
        Step 4: Click on the Share button to stop sharing.
        Verify 'Share with Others' dialog opens with the multiple shared users 'autobasuser08' and 'autodevuser82'.
        """
        Stop_share_elem=util_obj.validate_and_get_webdriver_object(Stop_share_css,'share_button_css')
        Stop_share_elem.click()
        util_obj.synchronize_with_number_of_element(pop_top_css, '1',MEDIUM_WAIT)
        util_obj.verify_object_visible(pop_top_css,True,"step5.1 Verify Share with Others window appears")
        total_users = util_obj.validate_and_get_webdriver_objects(user_verify_top_css,"user-name")
        observed_users = []
        for user in total_users:
            observed_users.append(user.text.strip())
        util_obj.asequal(expected_user_list,observed_users,"Step 6.1: Verify the basic and dev user under share with ")
        
        
        """
        Step 5: Click the X button to remove the already shared multiple users 'autobasuser08' and 'autodevuser82''..
        Verify 'autobasuser08' and 'autodevuser82' users are removed under 'Shared with'
        """
        close_elem=util_obj.validate_and_get_webdriver_objects(user_close_css,'share_button_css')
        for elem in close_elem:
            elem.click()
        
        
        
        """
        Step 6: Click OK to close the 'Share with Others' dialog.
        """
        ok_elem=util_obj.validate_and_get_webdriver_object(ok_css,"ok_button_css")
        ok_elem.click()
        
        
        """
        Step 7: Close the portal run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 8: Sign out as Admin and Sigin as basic user
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.login_page('mridbas','mrpassbas')
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(crumb_css, '1',MEDIUM_WAIT)
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share',click_option='double_click')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(Plus_css, '1',MEDIUM_WAIT)
        
        """
        Step 9: Run the portal and Click + Sign > select Link to an existing page
        Verify Selection browser window opens with Repository and Shared Pages tabs
        """
        Plus_elem=util_obj.validate_and_get_webdriver_object(Plus_css," plus_icon_css")
        core_util_obj.python_left_click(Plus_elem)
        util_obj.verify_element_visiblty(element_css=new_page_css, visible=True, msg='Step 4.1. Verify Newpage windows open')
        util_obj.synchronize_with_number_of_element(link_text_css, '1',MEDIUM_WAIT)
        core_util_obj.python_left_click(util_obj.validate_and_get_webdriver_object(link_text_css, "link text"))
        util_obj.synchronize_with_number_of_element(resource_dialog_css, '1',MEDIUM_WAIT)
        resource_dialog_obj.verify_resource_dialog_is_visible(True,"Step5.1 verify resource dialog is visible")
        util_obj.verify_object_visible(resource_tab_css, True,"Step 5.2 verify resource dialog with repository and shared pages")
        
        """
        Step 10: Click on Shared Pages tab > double click on > Administrator.
        Verify 'Sales Dashboard' page shows.
        """
        
        resource_dialog_obj.select_tab_button('Shared Pages')
        resource_dialog_obj.select_resource_from_gridview('autoadmuser02',selection_type='double')
        util_obj.synchronize_with_number_of_element(sales_item_css, '1',MEDIUM_WAIT)
        resource_dialog_obj.verify_resource_item_in_gridview('Sales Dashboard (Filtered)','asin',"Step 6:verify shared multiple users in the content area")
        button_element=resource_dialog_obj.get_button_object('Cancel')
        core_util_obj.python_left_click(button_element)
        
        """
        Step 10:Click Cancel to close the selection browser window
        """
        button_element=resource_dialog_obj.get_button_object('Cancel')
        core_util_obj.python_left_click(button_element)
        
        """
        Step 11: Close the portal run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 12: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
    
        