'''
Created on 21-Feb-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324332
TestCase Name = Portal Designer_Design Content : Place_Holder (Easy Selector)
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, ia_resultarea, vfour_portal_properties, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage

class C2324332_TestClass(BaseTestCase):

    def test_C2324332(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        wf_mainpage_obj = wf_mainpage.Wf_Mainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal'
        portal_name = 'BIP_Place_holder'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        easy_selector_image = "[class*='bip'][class*='easy'][class*='selector'][class*='image']"
        
        def verify_panel_data(panel_name, expected_panel_text, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_panel_text, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
            
        def verify_column_data(column_no, expected_panel_in_column_text_list, step_num):
            columns_obj = portal_canvas.get_column_obj(column_no)
            actual_panel_in_column_text_list = [elem.text.strip() for elem in columns_obj.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']") if elem != '']
            utillobj.asequal(expected_panel_in_column_text_list, actual_panel_in_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
        
        def verify_panel_frame_data(chart_type, panel_name, expected_value, step_num, custom_css="svg g>text[class^='riser!s']"):
            portal_misobj.switch_to_frame_in_bip_page(frame_panel_name=panel_name)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_value, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'riser':
                ia_resultobj.verify_number_of_chart_segment("jschart_HOLD_0", expected_value, "Step "+str(step_num)+": Verify number of risers displayed in '" + str(panel_name) + "'.")   
            elif chart_type == 'text':
                actual_text = self.driver.find_element_by_css_selector(custom_css).text.strip()
                utillobj.asequal(actual_text, expected_value, "Step "+str(step_num)+": Verify table data displayed in '" + str(panel_name) + "'.")
            utillobj.switch_to_default_content(pause=3)
        
        def verify_easy_selector_plus_image_icon_into_panel(panel_name, step_num):
            panel_obj = portal_canvas.get_panel_obj(panel_name)
            easy_selector_image_obj = panel_obj.find_element_by_css_selector(easy_selector_image).is_displayed()
            utillobj.asequal(True, easy_selector_image_obj, "Step "+str(step_num)+": Verify that that "+str(panel_name)+" appears in column 2 with a + sign")
        
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 2: Expand P292 domain, right click on S10117 folder and choose New -> Collaborative Portal 
                    Enter title as 'BIP_Place_holder'
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        core_utilobj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        portal_misobj.verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
         
        """ Step 3: Choose page layout of 3 columns
                    Enter Page 1    
        """
        """ Step 4: Maximize the portal
        """
        portal_misobj.select_page_template(page_template="3 Column", Page_title='Page 1', btn_name='Create')
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 4: Verify 'Page 1' in Navigation bar.")
         
        """ Step 5: Click the theme button and choose Neutral theme if its not the default
        """
        portal_ribbon.select_or_verify_layout_base_theme(default_theme_name='Neutral', msg='Step 5:Verify the Neutral theme is set as default', theme_name='Neutral')
         
        """ Step 6: Column 1
                    Click insert tab
        """
        portal_canvas.select_column(1)
        time.sleep(2)
         
        """ Step 7: Click the Easy selector container
                    Verify that a browse window appears
        """
        """ Step 8: Choose Retail Samples --> Portal --> Small Widgets
                    Verify that that Panel 1 appears in column1 with a + sign
        """
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', button='OK')
        time.sleep(1)
        verify_easy_selector_plus_image_icon_into_panel('Panel 1', '8')
         
        """ Step 9: Add a tab container with a tree block and an accordion portal list into column 1
        """
        ''' Add tab container with a tree block '''
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Tabbed')
        time.sleep(2)
        portal_canvas.select_panel('Panel 2')
        portal_ribbon.select_ribbon_item("Insert", 'Insert_ResourceTree')
        time.sleep(2)
        verify_panel_data('Panel 2', workspace, '9')
         
        ''' Add an accordion with portal list '''
        portal_canvas.select_panel('Panel 2')
        portal_canvas.scroll_panel(0, 0, 'up', option='uiautomation', number_of_times=30, waitTime=0.5)
        portal_canvas.select_column(1)
        time.sleep(1)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Accordion')
        time.sleep(1)
        portal_canvas.select_column(2)
        time.sleep(1)
        portal_canvas.scroll_panel(0, 0, 'down', option='uiautomation', number_of_times=25, waitTime=0.5)
        time.sleep(1)
        portal_canvas.select_panel('Panel 3')
        portal_ribbon.select_ribbon_item("Insert", 'Insert_PortalList')
        time.sleep(2)
        verify_panel_data('Panel 3', portal_name, '9.1')
        portal_canvas.select_panel_border('Panel 3', click_on_panel_location='right')
        portal_canvas.scroll_panel(0, 0, 'up', option='uiautomation', number_of_times=30, waitTime=0.5)
         
        """ Step 10: Click Column 2 and Click the Easy selector container and click ok for the same folder
                     Verify that that Panel 4 appears in column 2 with a + sign
        """
        portal_canvas.select_column(2)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', button='OK')
        time.sleep(1)
        verify_easy_selector_plus_image_icon_into_panel('Panel 4', '10')
         
        """ Step 11: Add Accordion report into column 2
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(1)
        item_path = BIP_Portal_Path+"->Accordion_change_title"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', 'Panel 4', drop_point='bottom_middle')
        time.sleep(2)
        verify_panel_frame_data('text', 'Panel_5_1', 'Budget Units', '11', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
         
        """ Step 12: Click Column 3 and Click the Easy selector container and click ok for the same folder
                     Verify that that Panel 6 appears in column 3 with a + sign
        """
        portal_canvas.select_column(3)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', button='OK')
        time.sleep(1)
        verify_easy_selector_plus_image_icon_into_panel('Panel 6', '12')
         
         
        """ Step 13: Click the + sign and choose Category Sales report
                     Verify that the report appears in that panel
        """
        portal_canvas.select_easy_selector_item('Panel 6', 'Category Sales', button='Add')
        time.sleep(1)
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_6', expected_legend, '13')
 
        """ Step 14: Click the menu icon for that panel
                     Verify the menu options (i.e) minimize, maximize, replace, remove, refresh, delete.
        """
        portal_canvas.manage_panel_title_menubar('Category Sales', expected_opt=['Minimize', 'Maximize', 'Replace', 'Remove', 'Refresh', 'Delete'], msg="Step 14: Verify the menu options (i.e) minimize, maximize, replace, remove, refresh, delete.")
         
        """ Step 15: Click Column 3 and Click the Easy selector container
                     Verify that the browse window does appear
        """
        portal_canvas.select_column(3)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', button='OK')
        time.sleep(1)
        verify_easy_selector_plus_image_icon_into_panel('Panel 7', '15')
        portal_canvas.select_panel('Panel 7')
         
        """ Step 16: Multi-select IA_Chart1 and babydeer from resource tree and drag them into Panel 7
                     Verify that a tabbed container appears in column 3
        """
        item_path_list=[BIP_Portal_Path+"->Accordion_change_title", BIP_Portal_Path+"->IA_Chart1", BIP_Portal_Path+"->babydeer"]
        portal_canvas.multi_select_dragdrop_repository_item_into_canvas(item_path_list, 'panel', 'Panel 7')
        time.sleep(2)
        portal_canvas.verify_tabbed_panel('Panel 7', ['IA_Chart1', 'babydeer'], "Step 16: Verify that a tabbed container appears in Panel 7.")
        portal_canvas.verify_panel_image('Panel 7', 'babydeer', "Step 16.1: Verify 'babydeer' image visible inside tabbed container appears in column 3.")
         
        """ Step 17: Click the BIP icon and exit then save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        time.sleep(1)
        
        """ Step 18: Run the portal
                     Verify that all containers show and the + signs as well.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 18: Verify 'Page 1' in Navigation bar.")
        
        ''' Column 1 assertion '''
        verify_column_data(1, ['Panel 1', 'Panel 2', 'Panel 3'], '18.1')
        verify_easy_selector_plus_image_icon_into_panel('Panel 1', '18.2')
        verify_panel_data('Panel 2', 'Tab 1', '18.3')
        verify_panel_data('Panel 2', workspace, '18.4')
        verify_panel_data('Panel 3', 'Area 1', '18.5')
        verify_panel_data('Panel 3', portal_name, '18.6')
        
        ''' Column 2 assertion '''
        verify_column_data(2, ['Panel 4', 'Accordion_change_title'], '18.7')
        verify_easy_selector_plus_image_icon_into_panel('Panel 4', '18.8')
        verify_panel_frame_data('text', 'Panel_5_1', 'Budget Units', '18.9', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        
        ''' Column 3 assertion '''
        verify_column_data(3, ['Category Sales', 'Panel 7'], '18.10')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_6', expected_legend, '18.11')
        verify_panel_frame_data('riser', 'Panel_7', 5, '18.12')
        
        """ Step 19: Click the + sign for panel 1 and choose the Regional Sales Trend then click OK
                     Verify the chart shows
        """
        portal_canvas.select_easy_selector_item('Panel 1', 'Regional Sales Trend', button='Add')
        time.sleep(1)
        portal_canvas.verify_panel_caption('Regional Sales Trend', 'Step 19: Verify Regional Sales Trend added in Panel 1')
        expected_legend= ['EMEA', 'North America', 'Oceania', 'South America']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '19.1')
        
        """ Step 20: Click the + sign for the panel in column 2 and Double click Discount by Region
                     Verify the chart shows
        """
        portal_canvas.select_easy_selector_item('Panel 4', 'Discount by Region', button='Add')
        time.sleep(1)
        portal_canvas.verify_panel_caption('Discount by Region', 'Step 20: Verify Discount by Region added in Panel 1')
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_4')
        utillobj.synchronize_with_number_of_element('#jschart_HOLD_0 .chartPanel [tdgtitle]', 16, 90)
        utillobj.switch_to_default_content()
        time.sleep(2)
        verify_panel_frame_data('riser', 'Panel_4', 16, '20.1')
        
        """ Step 21: Click the menu option for Category Sales report and choose replace.
                     Pick another report,
                     Verify that the chart shows
        """
        portal_run.verify_column_panel_title_menubar_button(3, 'Category Sales', verify=False, select_menu_opt='Replace')
        portal_canvas.select_easy_selector_item('Category Sales', 'Regional Profit by Category', option='frame', button='Add')
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_6')
        utillobj.synchronize_with_number_of_element('#jschart_HOLD_0 .chartPanel [tdgtitle]', 28, 90)
        utillobj.switch_to_default_content()
        time.sleep(2)
        verify_panel_frame_data('riser', 'Panel_6', 28, '21')
        
        """ Step 22: Close and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
         
        """Step 23: Rerun the portal
                     Verify all the changes are not there. NO changes should be saved if the page is locked.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 22: Verify 'Page 1' in Navigation bar.")
        
        ''' Column 1 assertion '''
        verify_column_data(1, ['Panel 1', 'Panel 2', 'Panel 3'], '22.1')
        verify_easy_selector_plus_image_icon_into_panel('Panel 1', '22.2')
        verify_panel_data('Panel 2', 'Tab 1', '22.3')
        verify_panel_data('Panel 2', workspace, '22.4')
        verify_panel_data('Panel 3', 'Area 1', '22.5')
        verify_panel_data('Panel 3', portal_name, '22.6')
        
        ''' Column 2 assertion '''
        verify_column_data(2, ['Panel 4', 'Accordion_change_title'], '22.7')
        verify_easy_selector_plus_image_icon_into_panel('Panel 4', '22.8')
        verify_panel_frame_data('text', 'Panel_5_1', 'Budget Units', '22.9', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        
        ''' Column 3 assertion '''
        verify_column_data(3, ['Category Sales', 'Panel 7'], '22.10')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_6', expected_legend, '22.11')
        verify_panel_frame_data('riser', 'Panel_7', 5, '22.12')
        
        """ Step 24: Close the portal and Close and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 25: Edit the portal
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Edit')
        core_utilobj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        
        """ Step 26: Unlock the page and freeze all columns
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg="Step 25: ")
        time.sleep(2)
        portal_canvas.select_column(1)
        time.sleep(3)
        portal_properties.edit_input_control('page', 'Freeze Column', 'checkbox', checkbox_input='check', msg="Step 25.1: ")
        time.sleep(2)
        portal_canvas.select_column(2)
        time.sleep(3)
        portal_properties.edit_input_control('page', 'Freeze Column', 'checkbox', checkbox_input='check', msg="Step 25.2: ")
        time.sleep(2)
        portal_canvas.select_column(3)
        time.sleep(3)
        portal_properties.edit_input_control('page', 'Freeze Column', 'checkbox', checkbox_input='check', msg="Step 25.3: ")
        time.sleep(2)
        
        """ Step 27: SSave and run the portal
        """
        portal_ribbon.bip_save_and_exit('Yes')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        time.sleep(1)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 26: Verify 'Page 1' in Navigation bar.")
        
        ''' Column 1 assertion '''
        verify_column_data(1, ['Panel 1', 'Panel 2', 'Panel 3'], '26.1')
        verify_easy_selector_plus_image_icon_into_panel('Panel 1', '26.2')
        verify_panel_data('Panel 2', 'Tab 1', '26.3')
        verify_panel_data('Panel 2', workspace, '26.4')
        verify_panel_data('Panel 3', 'Area 1', '26.5')
        verify_panel_data('Panel 3', portal_name, '26.6')
        
        ''' Column 2 assertion '''
        verify_column_data(2, ['Panel 4', 'Accordion_change_title'], '26.7')
        verify_easy_selector_plus_image_icon_into_panel('Panel 4', '26.8')
        verify_panel_frame_data('text', 'Panel_5_1', 'Budget Units', '26.9', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        
        ''' Column 3 assertion '''
        verify_column_data(3, ['Category Sales', 'Panel 7'], '26.10')
        expected_legend= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_panel_frame_data('legend', 'Panel_6', expected_legend, '26.11')
        verify_panel_frame_data('riser', 'Panel_7', 5, '26.12')
        
        """ Step 28: Click the + sign for panel 1 and choose the Regional Sales trend then click OK
                     Click the + sign for the panel in column 2 and Double click discount by region
                     Click the menu option for Category Sales and choose replace.
                     Pick another report
                     Close and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_canvas.select_easy_selector_item('Panel 1', 'Regional Sales Trend', button='Add')
        time.sleep(1)
        portal_canvas.verify_panel_caption('Regional Sales Trend', 'Step 28: Verify Regional Sales Trend added in Panel 1')
        expected_legend= ['EMEA', 'North America', 'Oceania', 'South America']
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '28.1')
        
        portal_canvas.select_easy_selector_item('Panel 4', 'Discount by Region', button='Add')
        time.sleep(1)
        portal_canvas.verify_panel_caption('Discount by Region', 'Step 28.2: Verify Discount by Region added in Panel 1')
        verify_panel_frame_data('riser', 'Panel_4', 16, '28.3')
        
        portal_run.verify_column_panel_title_menubar_button(3, 'Category Sales', verify=False, select_menu_opt='Replace')
        portal_canvas.select_easy_selector_item('Category Sales', 'Regional Profit by Category', option='frame', button='Add')
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_6')
        utillobj.synchronize_with_number_of_element('#jschart_HOLD_0 .chartPanel [tdgtitle]', 28, 90)
        utillobj.switch_to_default_content()
        time.sleep(2)
        verify_panel_frame_data('riser', 'Panel_6', 28, '28.4')
        
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 29: Re-run the portal
                     Verify that now the changes are saved cause only the column is frozen.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 29.1: Verify 'Page 1' in Navigation bar.")
        
        ''' Column 1 assertion '''
        verify_column_data(1, ['Regional Sales Trend', 'Panel 2', 'Panel 3'], '29.2')
        expected_legend= ['EMEA', 'North America', 'Oceania', 'South America']
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_1')
        utillobj.synchronize_with_number_of_element("#jschart_HOLD_0 .legend text", 4, 90)
        utillobj.switch_to_default_content()
        verify_panel_frame_data('legend', 'Panel_1', expected_legend, '29.3')
        verify_panel_data('Panel 2', 'Tab 1', '29.4')
        verify_panel_data('Panel 2', workspace, '29.5')
        verify_panel_data('Panel 3', 'Area 1', '29.6')
        verify_panel_data('Panel 3', portal_name, '29.7')
        
        ''' Column 2 assertion '''
        verify_column_data(2, ['Discount by Region', 'Accordion_change_title'], '29.8')
        verify_panel_frame_data('riser', 'Panel_4', 16, '29.10')
        verify_panel_frame_data('text', 'Panel_5_1', 'Budget Units', '29.11', custom_css="table[ibiattr='table1'] tr:nth-child(1) td:nth-child(2)")
        
        ''' Column 3 assertion '''
        verify_column_data(3, ['Regional Profit by Category', 'Panel 7'], '29.12')
        verify_panel_frame_data('riser', 'Panel_6', 28, '29.13')
        verify_panel_frame_data('riser', 'Panel_7', 5, '29.14')
        
        """ Step 30: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 31: In the banner link, click on the top right username > Click Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()