'''
Created on October 17, 2018

@author: Robert/Magesh
Testcase Name : Create portal with my pages, without alias
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261710
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal, page_designer, chart, active_report
from common.lib import utillity,core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators.portal_designer import Vfive_Designer
from common.lib.global_variables import Global_variables

class C8261710_TestClass(BaseTestCase):
    
    def test_C8261710(self):
        
        """
        CLASS OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_portal_2level=designer_portal.Two_Level_Side(self.driver)
        page_design_obj=page_designer.Design(self.driver)
        chart_obj=chart.Chart(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        expected_folder_item='Page2'
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        portal_name='v5-mypages-test1'
        workspaces = "Workspaces"

        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait*5)
           
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', 15)
        main_page_obj.select_action_bar_tab('Designer')
        designer_portal_2level.delete_portal_if_exists(portal_name)
        main_page_obj.select_action_bar_tabs_option('Portal')
             
        """
        Step 4. Enter title as 'v5-mypages-test1'
        Name text box is filled automatically as 'v5-mypages-test1'
        """
        util_obj.synchronize_with_visble_text(edit_portal_css, 'New Portal', 20)
        designer_portal_2level.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_name)
        designer_portal_2level.name_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, step_number="Step 4.1. Verify name textbox")
             
        """
        Step 5. Click on Theme dropdown;
        Select 'light'
        Verify Theme selection is updated.
        """
        designer_portal_2level.theme_dropdown_in_new_or_edit_portal_dialog(select_theme="Light")
        designer_portal_2level.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme="Light", step_number="Step 5. Verify Light theme")
             
        """
        Step 6. Click on 'Create My Pages menu' check box
        """
        designer_portal_2level.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox="check")
             
        """
        Step 7. Click Create
        Verify 'Create Portal' dialog is closed;
        'v5-mypages-test1' portal folder is created under P292_S19901 domain > G520448 folder in content tree;
        Portal is unpublished, title appears in Italic in both content tree and in content area.
        """
        designer_portal_2level.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        designer_portal_2level.verify_portal_dialog_open_or_close("close", "Step 7. Verify dialog closed")
        folder_name_list=['v5-mypages-test1']
        main_page_obj.expand_repository_folders_and_verify(folder_name_path, folder_name_list, 'Step 7.1: Verify repository folders')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(portal_name, 'unpublish', 'Step 7.2: Verify folder published')
        main_page_obj.verify_repository_folder_font_style(portal_name, 'italic', 'Step 7.3: Verify font is italic in content tree')
             
        """
        Step 8. Click on 'v5-mypages-test1' from tree
        Verify only the below four action tiles are available for selection.
        Folder
        Workbook
        Page
        Shortcut
        """
        main_page_obj.click_repository_folder(portal_name)
        labels_list=['Folder','Workbook','Page','Shortcut']
        main_page_obj.verify_action_bar_tab_all_options(labels_list, 'Step 8. Verify action tiles')
             
        """
        Step 9. Click on 'G520448' folder from tree
        """
        main_page_obj.expand_repository_folder(folder_name_path)
             
        """
        Step 10. Double click open 'v5-mypages-test1' from content area
        'My Pages' folder appears;
        Verify breadcrumbs appears as Domains > P292_S19901 > G520448 > v5-mypages-test1
        'My Pages' folder is unpublished, title appears in Italic in content tree;
        Verify 'My Pages' folder in content area.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, click_option='double_click')
        folder_name_list=['My Pages']
        main_page_obj.verify_folders_in_grid_view(folder_name_list, 'asin', 'Step 10.1: Verify content folders')
        main_page_obj.verify_crumb_box(workspaces+'->P292_S19901->G520448->v5-mypages-test1', 'Step 10.2')
        main_page_obj.verify_content_area_folder_publish_or_unpublish('My Pages', 'unpublish', 'Step 10.3: Verify folder is unpublished.')
        main_page_obj.verify_repository_folder_font_style('My Pages', 'italic', 'Step 10.4: Verify folder tilte is italic')
             
        """
        Step 11. Click on 'v5-mypages-test1' from under Domains > P292_S19901 > G520448;
        Click on 'Page' tile from action bar.
        """
        main_page_obj.expand_repository_folder(folder_name_path+"->"+portal_name)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
             
        """
        Step 12. Choose Grid 2-1 template;
        Drag and drop 'Arc-Sales by Region' from Retail Samples -> Charts to Panel1.
        """   
        util_obj.synchronize_with_number_of_element("div[data-ibx-type='pdNewPage']", 1, 30)
        page_design_obj.select_page_designer_template('Grid 2-1')
        page_design_obj.collapse_content_folder('G520448->P292_S19901')
        page_design_obj.drag_content_item_to_container('Arc - Sales by Region', 'Panel 1', container_position=1, content_folder_path='Retail Samples->Charts')
             
        """
        Step 13. Save page as 'Page1' and exit designer.
        """
        page_design_obj.save_page_from_toolbar('Page1', wait_time=10)
        page_design_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
            
        """
        Step 14. Click on 'My Pages' folder and click on 'Page' tile from action bar.
        """
        main_page_obj.expand_repository_folder(folder_name_path+"->"+portal_name+"->My Pages")
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("div[data-ibx-type='pdNewPage'] ", 1, 30)
             
        """
        Step 15. Choose blank template;
        Drag and drop 'Sales Metrics YTD' from Retail Samples -> Reports to Page.
        """
        page_design_obj.select_page_designer_template('Blank')
        page_design_obj.collapse_content_folder('G520448->P292_S19901')
        page_design_obj.drag_content_item_to_blank_canvas('Sales Metrics YTD', 3, content_folder_path='Retail Samples->Reports')
             
        """
        Step 16. Save page as 'Page2' and exit designer.
        """
        page_design_obj.save_page_from_toolbar('Page2', wait_time=10)
        page_design_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
           
        """ 
        Step 17. Right click on 'v5-mypages-test1' and click on Run
        Verify portal run mode appears as below and pages under MY Pages menu.
        Verify the browser tab is the title of the portal
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run', 'G520448')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(Vfive_Designer.left_panel_page_folders_container_css, 1, 45)
        designer_portal_2level.verify_folders_in_left_sidebar(['Page1','My Pages'], 'Step 17.1: Verify folders in the left side bar')
        designer_portal_2level.switch_to_panel_frame('Arc - Sales by Region')
        run_parent_css= 'jschart_HOLD_0'
        util_obj.synchronize_until_element_is_visible('#{0}'.format(run_parent_css), active_report_obj.home_page_long_timesleep)
        expected_datalabel_y = ['$0.00', '$50,000,000.00', '$100,000,000.00', '$150,000,000.00', '$200,000,000.00', '$250,000,000.00', '$300,000,000.00', '$350,000,000.00', '$400,000,000.00', '$450,000,000.00', '$500,000,000.00', '$550,000,000.00', '$600,000,000.00']
        expected_datalabel_x=['Oceania','South America','EMEA','North America']
        custom_css_y_label="g text.label"
        custom_css_x_labels="g.group-labels text"
        color_css=".chartPanel .group-main path[class*='riser!s0!g0!mbar!']"
        chart_obj.verify_x_axis_label_in_run_window(expected_datalabel_x, parent_css='#'+run_parent_css, xyz_axis_label_css=custom_css_x_labels, msg="Step 17.2: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(expected_datalabel_y, parent_css='#'+run_parent_css, xyz_axis_label_css=custom_css_y_label, msg="Step 17.3: Verify y-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(color_css, "dark_green", attribute='fill', msg="Step 17.4: Verify chart colour")
        chart_obj.verify_number_of_chart_segment(run_parent_css, 4, "Step 17.5: Verify number of chart segments in run window")
        chart_obj.switch_to_default_content()
        designer_portal_2level.expand_folder_in_left_sidebar('My Pages')
        time.sleep(Global_variables.mediumwait)
        page_2_css = Vfive_Designer.left_panel_page_folders_container_css+' '+Vfive_Designer.left_panel_folder_item_css
        actual_folder_item=util_obj.validate_and_get_webdriver_object(page_2_css, 'Page2 button').text.strip()
        util_obj.asequal(actual_folder_item, expected_folder_item, 'Step17.6: pages under MY Pages menu.')
          
        """
        Step 18. Click on Page2
                 Verify Page2 has been selected;
                 Verify the width of side bar;
                 Verify alignment and position of all menus (Page 1, My Pages and Page 2) in side bar as shown below
        """
        page2=util_obj.validate_and_get_webdriver_object(page_2_css, 'Page2 button')
        core_util_obj.left_click(page2)
        designer_portal_2level.switch_to_panel_frame('Sales Metrics YTD')
        util_obj.synchronize_with_visble_text('#ITableData0', 'Sales Metrics YTD', active_report_obj.home_page_long_timesleep)
        active_report_obj.verify_page_summary(0, '113of113records,Page1of5', 'Step 18: verify page summary')
        active_report_obj.verify_active_report_dataset('C6779486_Ds01.xlsx', "Step 18.1: Verify Page2 report", table_css="#ITableData0")
        chart_obj.switch_to_default_content()
        util_obj.verify_object_visible(page_2_css+ ".pvd-left-main-panel-content-button-active", True, 'Step 18.2: Verify Page2 has been selected')
          
        '''
        Verify side bar width
        '''
        Vfive_Designer.left_panel_page_folders_container_css
        widht = int(util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(Vfive_Designer.left_panel_page_folders_container_css, 'Left panel'), 'width').replace('px',''))
        util_obj.asequal(200, widht, 'Step 18.2: Verify the width of side bar')
        Vfive_Designer.left_panel_page_folders_container_css
        widht = int(util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(Vfive_Designer.left_panel_page_folders_container_css, 'Left panel'), 'max-width').replace('px',''))
        util_obj.asequal(205, widht, 'Step 18.3: Verify the max-width of side bar')
        
        '''
        Verify alignment and position of all menus 
        '''
        main_folder_css = Vfive_Designer.left_panel_page_folder_css
        count=4
        for option in util_obj.validate_and_get_webdriver_objects(main_folder_css, 'all left button'):
            if util_obj.get_element_css_propery(option, 'padding') == '5px 12px' or  (util_obj.get_element_css_propery(option, 'padding-top') == '5px' and util_obj.get_element_css_propery(option, 'padding-bottom') == '5px' and util_obj.get_element_css_propery(option, 'padding-left') == '12px' and util_obj.get_element_css_propery(option, 'padding-right') == '12px'):
                util_obj.asequal(True, True, "Step 18.{0}: '{1}' alignment is correct.".format(count, option.text.strip()))
            else:
                util_obj.asequal('not correct', util_obj.get_element_css_propery(option, 'padding'), "Step 18.{0}: '{1}' alignment is not correct.".format(count, option.text.strip()))
            count += 1
        for option in util_obj.validate_and_get_webdriver_objects(page_2_css, 'Page 2'):
            if util_obj.get_element_css_propery(option, 'padding') == '5px 12px 5px 24px' or  (util_obj.get_element_css_propery(option, 'padding-top') == '5px' and util_obj.get_element_css_propery(option, 'padding-bottom') == '5px' and util_obj.get_element_css_propery(option, 'padding-left') == '24px' and util_obj.get_element_css_propery(option, 'padding-right') == '12px'):
                util_obj.asequal(True, True, "Step 18.{0}: '{1}' alignment is correct.".format(count, option.text.strip()))
            else:
                util_obj.asequal('not correct', util_obj.get_element_css_propery(option, 'padding'), "Step 18.{0}: '{1}' alignment is not correct.".format(count, option.text.strip()))
            count += 1
        
        """
        Step 19. Close portal
        """    
        core_util_obj.switch_to_previous_window()
        
        """
        Step 20. Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()