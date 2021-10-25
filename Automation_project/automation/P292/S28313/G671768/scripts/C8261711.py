'''
Created on October 17, 2018

@author: Vpriya
Testcase Name : Edit portal with my pages, without alias
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261711
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables
from common.pages.wf_mainpage import Wf_Mainpage as wf_mainpage_obj

class C8261711_TestClass(BaseTestCase):
    
    def test_C8261711(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        wf_mainpages_obj=wf_mainpage_obj(self.driver)
            
        medium_wait=40
        folder_name_path="P292_S19901->G520448"
#         portals_css = "div[title='Portals'] .ibx-label-text"
        crumb_box_css = ".crumb-box .ibx-label-text"
        pop_top_css=".pop-top [data-ibx-name='vbMain'] [data-ibxp-text='Banner']"
        portal_name="v5-mypages-test1"
        portal_renamed="v5-mypages-test1-title-changed-contenttree"

        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.wait_for_page_loads(15)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
         
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-alias-test2' portal and select Edit
        Edit portal dialog appears;
        Verify below.
        Title and name appears as 'v5-alias-test2';
        Alias is not empty, shows 'abc123ABC+_)*&^%$#@!'
        Banner switch is on;
        Show portal title in banner box is checked;
        Logo stays Not selected;
        Two-level navigation is selected;
        Theme should be 'Midnight';
        URL: http://machinename:port/alias/portal/abc123ABC_@!
        Save button is highlighted and disabled by default;
        Cancel button is enabled.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.wait_for_page_loads(10)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Edit')
        util_obj.synchronize_with_number_of_element(pop_top_css, '1', medium_wait)
         
        designer_portal_obj.verify_caption_in_new_or_edit_portal_dialog('Edit Portal', step_number='03.00')
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name,  step_number='03.01')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, step_number='03.02')
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable', step_number='03.03')
        designer_portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable', step_number='03.04')
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='Not Selected', step_number='03.05')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable', step_number='03.06')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Light', current_mode='enable', step_number='03.07')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/'+portal_name, step_number='03.08')
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', step_number='03.09')
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode='enable', step_number='03.10')
         
        """
        Step 4.Add alias 'abcABCAD'
        Verify URL: http:machine_name:port/alias/portal/abcABCAD
        """
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value='abcABCAD')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/abcABCAD', step_number='04.00')
         
        """
        Step 5.Remove Alias
        Verify URL:  http:machine_name:port/alias/portal/P292_S19901/G520448/v5-mypages-test1
        """
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value='')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/'+portal_name, step_number='05.00')
         
        """
        Step 6. Hove over (x)
        Verify close tooltip appears
        """
        designer_portal_obj.close_button_inside_new_or_edit_portal_dialog(title_tooltip='Close', step_number='6.00')        
        """
        Step 7. Click Save
        Edit Portal dialog disappears
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_until_element_disappear(".ibx-dialog-main-box", 15)
        designer_portal_obj.verify_portal_dialog_open_or_close('close', 'Step 07.00: Verify Edit Portal dialog is closed')
         
        """
        Step 8. Open Portals tree from side bar,
        Right click on 'v5-mypages-test1' portal and select Edit
        """
        main_page_obj.select_portals_from_sidebar()
        util_obj.synchronize_with_visble_text(crumb_box_css, 'Portals', main_page_obj.chart_medium_timesleep)
        util_obj.synchronize_with_visble_text(".content-box", portal_name, main_page_obj.chart_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Edit')
        util_obj.synchronize_with_number_of_element('.ibx-dialog-content', 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 8.1. Edit Portal dialog opens.
        Verify below.
        Title and name appears as 'v5-mypages-test1';
        Banner switch is on;
        Show portal title in banner box is checked;
        Logo stays Not selected;
        Two-level navigation is selected;
        Theme should be 'light';
        URL: http:machine_name:port/alias/portal/P292_S19901/G520448/v5-mypages-test1;
        Save button is highlighted and disabled by default;
        Cancel button is enabled.
        """
        designer_portal_obj.verify_caption_in_new_or_edit_portal_dialog('Edit Portal', step_number='08.00')
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, step_number='08.01')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name,  step_number='08.02')
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable', step_number='08.03')
        designer_portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable', step_number='08.04')
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='Not Selected', step_number='08.05')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable', step_number='08.06')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Light', current_mode='enable', step_number='08.07')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/'+portal_name, step_number='08.08')
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', step_number='08.09')
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode='enable', step_number='08.10')
         
        
        """
        Step 9. Change title to 'v5-mypages-test1-title-changed-contenttree'
        """
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_renamed)
         
        """
        Step 10. Click Save
        Verify portal title appears as 'v5-mypages-test1-title-changed-contenttree' .
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        util_obj.synchronize_with_visble_text(".content-box", "v5-mypages-test1-title-changed-contenttree", main_page_obj.chart_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['v5-mypages-test1-title-changed-contenttree'], 'asin', 'Step 10.00: Verify portal title appears')
         
        """
        Step 11. Right click on 'v5-mypages-test1-title-changed-contenttree' portal and select Publish
        Verify portal is published (verify icon color too)
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_renamed,'Publish')
        time.sleep(Global_variables.longwait*3)
        portal_obj=wf_mainpages_obj.get_domain_folder_item(portal_renamed)
        
        util_obj.synchronize_with_number_of_element_within_parent_object(portal_obj, WfMainPageLocators.files_item_published_css, 1, 15)
        main_page_obj.verify_content_area_item_publish_or_unpublish(portal_renamed, 'publish', 'Step 11.00. Verify portal is published')
        main_page_obj.verify_item_icon_in_content_area(portal_renamed, 'portal', '11.01', verify_color_name='bar_blue', item_name_index=1)
        
        
        """
        Step 12. Click on Content from side bar;
        Click on 'G520448' folder under 'P292_S19901' domain
        """        
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder(folder_name_path)
        
        """
        Step 12.1. Verify portal title appears as 'v5-mypages-test1-title-changed-contenttree' and is published (icon color should be blue as below) in content area as below.
        """
        util_obj.wait_for_page_loads(15)
        util_obj.synchronize_with_visble_text(".content-box", portal_renamed, main_page_obj.chart_medium_timesleep)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(portal_renamed, 'publish', 'Step 12.00: Verify portal is published')
        main_page_obj.verify_folder_icon_in_content_area(portal_renamed, 'portal', '12.01', verify_color_name='bar_blue', item_name_index=1)
       
        """
        Step 13. Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()