'''
Created on November 15, 2018

@author: vpriya
Testcase Name : Verify able to view shared personal pages using Link to an existing pages in basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779803
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.pages import portal_sidebar,portal_canvas
from common.lib.webfocus import resource_dialog

class C8261707_TestClass(BaseTestCase):
    
    def test_C8261707(self):
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
        Link_css="div[class*='np-open ibx-widget ibx-flexbox']"
        resource_tab_css=".open-dialog-resources.pop-top .ibx-csl-items-container .ibx-tab-button"
        resource_dialog_css='.open-dialog-resources.pop-top'
        sales_item_css="div[class*='file-item file-item-published file-item-shown ibx-widget']"
        retail_title_css=".pd-page-header"
        retail_title="Retail Sales Dashboard"
        containers_title=['Category Sales','Regional Sales Trend','Discount by Region','Regional Profit by Category','Example of a Tab Container','Example of a Carousel Container']
        LONG_WAIT=120
        MEDIUM_WAIT=60
        
        
        """
        Step 1: Sign out as Admin and Sigin as basic user.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        util_obj.synchronize_with_number_of_element(crumb_css, 1, LONG_WAIT)
        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'.
        Verify that 'V5 Portal Share' shows as portal items.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(crumb_css, '1',MEDIUM_WAIT)
        main_page_obj.verify_items_in_grid_view(["V5 Portal Share"],'asin','Step 2:V5 Portal Share displays as item')

        """
        Step 3. Double click on 'V5 Portal Share' to run the portal.
        Verify 'V5 Portal Share tree' run in a new window and you see a sidebar with My Pages and a + sign under it.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share',click_option='double_click')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(Plus_css, '1',MEDIUM_WAIT)
        portal_sidebar_obj.verify_pages_in_folder('My Pages',['Page 1', '+']," Step 3.1 Verify sidebar with My Pages and a + sign under it.", assert_type='asin')
  
        """
        Step 4: Click on + Sign from the sidebar.
        Verify 'New Page' window opens with the 'Link to an existing page' link and four templates in it.
        """
        Plus_elem=util_obj.validate_and_get_webdriver_object(Plus_css," plus_icon_css")
        core_util_obj.python_left_click(Plus_elem)
        util_obj.verify_element_visiblty(element_css=new_page_css, visible=True, msg='Step 4.1. Verify Newpage windows open')
        portal_navi_obj.verify_new_page_template_window_is_displayed("Step 4:verify twopages windows are displayed")
        portal_navi_obj.verify_templates(template_names,"Step 4.1 verify templates")
        util_obj.verify_object_visible(Link_css,True," Step 4.2 Verify Link with existing page is available")
        
        """
        Step 5: Select 'Link to an existing page'..
        Verify Selection browser window opens with Repository and Shared Pages tabs.
        """
        portal_navi_obj.click_on_link_to_an_existing_page_button()
        util_obj.synchronize_with_number_of_element(resource_dialog_css, '1',MEDIUM_WAIT)
        resource_dialog_obj.verify_resource_dialog_is_visible(True,"Step5.1 verify resource dialog is visible")
        util_obj.verify_object_visible(resource_tab_css, True,"Step 5.2 verify resource dialog with repository and shared pages")
        
        """
        Step 6: Click on Shared Pages tab.
        Verify that it shows shared multiple users (Administrator and autodevuser82) in the content area
        """
        resource_dialog_obj.select_tab_button('Shared Pages')
        resource_dialog_obj.verify_resource_item_in_gridview('autoadmuser02','asin',"Step 6:verify shared multiple users in the content area")
        resource_dialog_obj.verify_resource_item_in_gridview('autodevuser82','asin',"Step 6:verify shared multiple users in the content area")
        
        """
        Step 7: Double click on > Administrator.
        Verify shared 'Sales Dashboard' page appears.
        """
        resource_dialog_obj.select_resource_from_gridview('autoadmuser02',selection_type='double')
        util_obj.synchronize_with_number_of_element(sales_item_css, '1',MEDIUM_WAIT)
        resource_dialog_obj.verify_resource_item_in_gridview('Sales Dashboard (Filtered)','asin',"Step 6:verify shared multiple users in the content area")
        
        """
        Step 8: Select 'Sales Dashboard'.
        Verify shared 'Retail Sales Dashboard' page appears on the canvas.
        """
        resource_dialog_obj.select_resource_from_gridview('Sales Dashboard (Filtered)')
        button_element=resource_dialog_obj.get_button_object('select')
        core_util_obj.python_left_click(button_element)
        util_obj.synchronize_with_number_of_element(retail_title_css, '1',MEDIUM_WAIT)
        portal_canvas_obj.verify_page_header_title(retail_title,"Step 8:Verify shared 'Retail Sales Dashboard' page appears on the canvas")
        portal_canvas_obj.verify_containers_title(containers_title,"Step8.1 verify containers title")
        
        """
        Step 9: Close the portal run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
    
        