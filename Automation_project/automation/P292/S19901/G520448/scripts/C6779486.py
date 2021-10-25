'''
Created on October 17, 2018

@author: Robert/Magesh
Testcase Name : Create portal with my pages, without alias
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779486
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal, page_designer, chart, active_report
from common.pages import page_designer_design
from common.lib import utillity,core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C6779486_TestClass(BaseTestCase):
    
    def test_C6779486(self):
        
        """
        CLASS OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        designer_portal_2level=designer_portal.Two_Level_Side(self.driver)
        pg_designer_portal_obj=page_designer_design.PageDesignerDesign(self.driver)
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

        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
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
        main_page_obj.select_action_bar_tabs_option('Portal')
         
        """
        Step 4. Enter title as 'v5-mypages-test1'
        Name text box is filled automatically as 'v5-mypages-test1'
        """
        util_obj.synchronize_with_visble_text(edit_portal_css, 'New Portal', 20)
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_name)
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, step_number="Step 4.1. Verify name textbox")
         
        """
        Step 5. Click on Theme dropdown;
        Select 'light'
        Verify Theme selection is updated.
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme="Light")
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme="Light", step_number="Step 5. Verify Light theme")
         
        """
        Step 6. Click on 'Create My Pages menu' check box
        """
        designer_portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox="check")
         
        """
        Step 7. Click Create
        Verify 'Create Portal' dialog is closed;
        'v5-mypages-test1' portal folder is created under P292_S19901 domain > G520448 folder in content tree;
        Portal is unpublished, title appears in Italic in both content tree and in content area.
        """
        designer_portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        designer_portal_obj.verify_portal_dialog_open_or_close("close", "Step 7. Verify dialog closed")
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
        main_page_obj.verify_crumb_box('Domains->P292_S19901->G520448->v5-mypages-test1', 'Step 10.2')
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
        pg_designer_portal_obj.close_page_designer_from_application_menu()
         
        """
        Step 14. Click on 'My Pages' folder and click on 'Page' tile from action bar.
        """
        util_obj.switch_to_main_window()
        main_page_obj.expand_repository_folder(folder_name_path+"->"+portal_name+"->My Pages")
        main_page_obj.select_action_bar_tabs_option('Page')
         
        """
        Step 15. Choose blank template;
        Drag and drop 'Sales Metrics YTD' from Retail Samples -> Reports to Page.
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("div[data-ibx-type='pdNewPage'] ", 1, 30)
        page_design_obj.select_page_designer_template('Blank')
        page_design_obj.collapse_content_folder('G520448->P292_S19901')
        page_design_obj.drag_content_item_to_blank_canvas('Sales Metrics YTD', 3, content_folder_path='Retail Samples->Reports')
         
        """
        Step 16. Save page as 'Page2' and exit designer.
        """
        page_design_obj.save_page_from_toolbar('Page2', wait_time=10)
        pg_designer_portal_obj.close_page_designer_from_application_menu()
         
        """ 
        Step 17. Right click on 'v5-mypages-test1' and click on Run
        Verify portal run mode appears as below and pages under MY Pages menu.
        Verify the browser tab is the title of the portal
        """
        util_obj.switch_to_main_window()
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run', 'G520448')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(".ibx-accordion-button-text", 3, 30)
        designer_portal_2level.verify_folders_in_left_sidebar(['Page1','My Pages'], 'Step 17.1: Verify folders in the left side bar')
        designer_portal_2level.expand_folder_in_left_sidebar('My Pages')
        time.sleep(Global_variables.mediumwait)
        page2=util_obj.validate_and_get_webdriver_object("div[class*='pvd-left-main-panel'][data-ibx-type='ibxAccordionPane']  div[data-ibx-type='ibxAccordionPage'] .ibx-accordion-page-content .bundle-folder-item", 'Page2 button')
        actual_folder_item = page2.text.strip()
        print(actual_folder_item)
        util_obj.asequal(actual_folder_item, expected_folder_item, 'Step17.2: pages under MY Pages menu.')
        run_parent_css= 'jschart_HOLD_0'
        expected_datalabel_y=['0','50M','100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M', '500M', '550M','600M']
        expected_datalabel_x=['Oceania','South America','EMEA','North America']
        custom_css_y_label=" g text.label"
        custom_css_x_labels=" g.group-labels text"
        color_css=".chartPanel .group-main path[class*='riser!s0!g0!mbar!']"
        chart_obj.wait_for_number_of_element("[data-ibxp-file*='Sales_by_Region_Arc.fex'] .ibx-iframe-frame", 1, 30)
        chart_obj.switch_to_frame(frame_css="[data-ibxp-file*='Sales_by_Region_Arc.fex'] .ibx-iframe-frame")
        chart_obj.verify_x_axis_label_in_run_window(expected_datalabel_x, xyz_axis_label_css=custom_css_x_labels, msg="Step 17.3: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(expected_datalabel_y, xyz_axis_label_css=custom_css_y_label, msg="Step 17.4: Verify y-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(color_css, "dark_green2", attribute='fill', msg="Step 17.5: Verify chart colour")
        chart_obj.verify_number_of_chart_segment(run_parent_css, 4, "Step 17.6: Verify number of chart segments in run window")
        chart_obj.switch_to_default_content()
        
        """
        Step 18. Click on Page2
        Verify Page2
        """
        chart_obj.wait_for_number_of_element(".ibx-accordion-page-content .bundle-folder-item", 1, 30)
        page2=util_obj.validate_and_get_webdriver_object("div[class*='pvd-left-main-panel'][data-ibx-type='ibxAccordionPane']  div[data-ibx-type='ibxAccordionPage'] .ibx-accordion-page-content .bundle-folder-item", 'Page2 button')
        util_obj.default_click(page2)
        chart_obj.wait_for_number_of_element("[data-ibxp-file='Sales_Metrics_YTD.fex'] .ibx-iframe-frame", 1, 30)
        chart_obj.switch_to_frame(frame_css="[data-ibxp-file='Sales_Metrics_YTD.fex'] .ibx-iframe-frame")
#         active_report_obj.create_reporttable_dataset('C6779486_Ds01.xlsx', table_css="#ITableData0", desired_no_of_rows=5, starting_rownum=2)
        active_report_obj.verify_table_data_set('C6779486_Ds01.xlsx', table_css="#ITableData0", desired_no_of_rows=5, starting_rownum=2, msg="Step18: Verify Page2 report")
        chart_obj.switch_to_default_content()
        
        """
        Step 19. Close portal
        """    
        util_obj.switch_to_main_window()
        
        """
        Step 20. Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()