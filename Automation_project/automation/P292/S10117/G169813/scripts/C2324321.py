'''
Created on 26-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324321
TestCase Name = Portal Designer_Design Properties : Container_Freeze
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import visualization_resultarea, ia_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324321_TestClass(BaseTestCase):

    def test_C2324321(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal'
        portal_name = 'lock column portal'
        
        def verify_panel_data(panel_name, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(project_id, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
            
        def verify_column_data(column_no, expected_column_text_list, step_num):
            column_text = portal_canvas.get_column_obj(column_no)
            actual_column_text_list = [elem.strip() for elem in column_text.text.strip().split('\n') if elem != '']
            utillobj.as_List_equal(expected_column_text_list, actual_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
        
        def verify_coumn_panel_title(column_no, expected_column_text_list, step_num):
            elem = portal_canvas.get_column_obj(column_no)
            panel_titles = elem.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
            actual_column_text_list = [elem.strip() for elem in [elem.text.strip() for elem in panel_titles] if elem != '']
            utillobj.as_List_equal(expected_column_text_list, actual_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
            
        def verify_panel_frame_data(chart_type, panel_name, expected_legend, step_num, custom_css="svg g>text[class^='riser!s']"):
            portal_misobj.switch_to_frame_in_bip_page(frame_panel_name=panel_name)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'riser':
                ia_resultobj.verify_number_of_chart_segment("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify number of risers displayed in '" + str(panel_name) + "'.", custom_css=custom_css)   
            utillobj.switch_to_default_content(pause=3)
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
            Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        
        """ Step 2: Open P292->S10117 from domains tree if its not expanded.
                    Note : If not expanded already, Properties_Open_Automatically test should have failed
        """
        wf_mainpageobj.expand_tree(project_id)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        domain_tree_text = driver.find_elements_by_css_selector(parent_css)
        actual_domain_tree_text = [elem for elem in [elem.text.strip() for elem in domain_tree_text] if elem != '']
        if bool('BIP_V4_Portal' in actual_domain_tree_text):
            print(root_path+" expanded already")
        else:
            print(root_path+" not expanded already")
         
        """ Step 3: Right click on the lock column portal and choose Edit
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Edit')
        coreutillobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep)
         
        """ Step 4: Add another 4 columned page and name it as '4 Col panel locked test'
        """
        portal_canvas.add_page('4 Column',Page_title='4 Col panel locked test')
        time.sleep(1)
        portal_canvas.select_page_in_navigation_bar('4 Col panel locked test')
        time.sleep(2)
          
        """ Step 5: Unlock the page.
                    Freeze Column 1
        """
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 5: ')
        time.sleep(2)
        portal_canvas.select_column(1)
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Freeze Column', 'checkbox', checkbox_input='check', msg='Step 5.1: ')
        time.sleep(2)
          
        """ Step 6: Add an accordion into column 1, tabbed into column 2 and accordion into column3
                    Add a tree block and Category Sales, Units Profit Treemap and Accordion Datatable into each of the panels in Column 1,2 and 3 respectively
                    Verify that they all have 2 areas and tabs
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(1)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Accordion')
        time.sleep(1)
        portal_canvas.select_column(2)
        time.sleep(1)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Tabbed')
        time.sleep(1)
        portal_canvas.select_column(3)
        time.sleep(1)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Accordion')
        time.sleep(1)
        portal_canvas.select_panel('Panel 1')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        time.sleep(2)
        verify_panel_data('Panel 1', '6')
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 1")
        css_value = "tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])"
        resultobj.wait_for_property("[id*='BiPopup'][class*='menu']:not([style*='hidden'])", 1, 10)
        utillobj.select_or_verify_bipop_menu('Add As Area', custom_css=css_value)
        time.sleep(2)
        portal_canvas.select_panel('Panel 2')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        time.sleep(1)
        verify_panel_data('Panel 2', '6.1')
        time.sleep(1)
        item_path="Retail Samples->Portal->Large Widgets->Units Profit Treemap"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 2")
        resultobj.wait_for_property("[id*='BiPopup'][class*='menu']:not([style*='hidden'])", 1, 10)
        utillobj.select_or_verify_bipop_menu('Add As Tab', custom_css=css_value)
        time.sleep(2)
        portal_canvas.select_panel('Panel 3')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        time.sleep(1)
        verify_panel_data('Panel 3', '6.2')
        time.sleep(1)
        item_path="Retail Samples->Portal->Responsive Tables->Accordion DataTable"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3")
        resultobj.wait_for_property("[id*='BiPopup'][class*='menu']:not([style*='hidden'])", 1, 10)
        utillobj.select_or_verify_bipop_menu('Add As Area', custom_css=css_value)
        time.sleep(2)
          
        """ Step 7: Add another panel into each column.
                    Add tagCloud chart into each of those panels
        """
        portal_canvas.select_column(1)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(1)
        portal_canvas.select_column(2)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(1)
        portal_canvas.select_column(3)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(1)
        portal_canvas.select_panel('Panel 4')
        item_path=BIP_Portal_Path+"->tagCloud chart"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4")
        time.sleep(2)
        portal_canvas.select_panel('Panel 5')
        item_path=BIP_Portal_Path+"->tagCloud chart"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 5")
        time.sleep(2)
        portal_canvas.select_panel('Panel 6')
        item_path=BIP_Portal_Path+"->tagCloud chart"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 6")
        time.sleep(2)
         
        verify_column_data(1, ['Panel 1', 'Area 1', 'Category Sales', 'New Area', 'tagCloud chart'], '7')
        verify_column_data(2, ['Panel 2', 'Tab 1', 'Units Profit Treemap', 'New Tab', 'tagCloud chart'], '7.1')
        verify_column_data(3, ['Panel 3', 'Area 1', 'Accordion DataTable', 'New Area', 'tagCloud chart'], '7.2')
        time.sleep(1)
        verify_panel_frame_data('legend', 'Panel_1', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '7.3')
        verify_panel_frame_data('legend', 'Panel_2', ['Gross Profit'], '7.4')
        verify_panel_frame_data('riser', 'Panel_4', 5, '7.5')
        verify_panel_frame_data('riser', 'Panel_5', 5, '7.6')
        verify_panel_frame_data('riser', 'Panel_6', 5, '7.7')
         
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe'][name*='Panel_3']",frame_height_value=0)
        panel_3_text = driver.find_element_by_css_selector("#DataTables_Table_0_wrapper table[role='grid']:not([class*='collapsed']) thead tr:nth-child(1) th:nth-child(1)").text.strip()
        utillobj.asequal(panel_3_text, 'Subcategory', "Step 7.8: Verify Accordion DataTable is loaded.")
        utillobj.switch_to_default_content(pause=3)
          
          
        """ Step 8: Click on Panel 1 in Column 1
                    Verify that the container freeze is greyed out
        """
        portal_canvas.select_panel_in_column(1, 'tagCloud chart')
        portal_canvas.scroll_panel(0, 0, 'up', option='autohotkey', number_of_times=20)
        time.sleep(2)
        portal_canvas.select_panel('Panel 1')
        time.sleep(3)
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', "Step 8: Verify that the container freeze is grayed out", enable_status='disabled', enable_value=True, color_name='silver')
        time.sleep(1)
         
        """ Step 9: Click the panels on Column 2 and check the Container Freeze box for both of them
        """
        portal_canvas.select_panel('Panel 2')
        time.sleep(2)
        portal_properties.edit_input_control('panel', 'Freeze Container', 'checkbox', checkbox_input='check', msg='Step 9: ')
        time.sleep(2)
        portal_canvas.select_panel_in_column(2, 'tagCloud chart')
        time.sleep(2)
        portal_properties.edit_input_control('panel', 'Freeze Container', 'checkbox', checkbox_input='check', msg='Step 9.1: ')
        time.sleep(2)
        portal_canvas.select_panel_in_column(3, 'tagCloud chart')
        portal_canvas.scroll_panel(0, 0, 'up', option='autohotkey', number_of_times=20)
        time.sleep(2)
         
        """ Step 10: Click Column 4 and check the easy selector box and choose Retail Samples --> Portal --> Small Widgets
        """
        portal_canvas.select_column(4)
        time.sleep(1)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', launch_point='property_tab', button='OK', 
                                                section='column', item_name='Show Easy Selector', control='checkbox', checkbox_input='check', msg='Step 10:')
         
        """ Step 11: Add the easy selector container and lock it.
        """
        portal_canvas.select_column(4)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_EasySelector')
        time.sleep(2)
        portal_canvas.select_panel('Panel 7')
        time.sleep(2)
        portal_properties.edit_input_control('panel', 'Freeze Container', 'checkbox', checkbox_input='check', msg='Step 11:')
         
        """ Step 12: Add any content in that panel 7 container.
        """
        portal_canvas.select_easy_selector_item('Panel 7', 'Regional Sales Trend', button='Add')
        time.sleep(3)
#         verify_panel_frame_data('legend', 'Panel_7', ['EMEA', 'North America', 'Oceania', 'South America'], '12')
         
        """ Step 13: Add a responsive container.
                     Add some content (tabs and areas)
                     Freeze the container
        """
        portal_canvas.select_column(4)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Responsive')
        time.sleep(1)
        portal_canvas.select_panel('Panel 8')
        time.sleep(0.5)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Tabbed')
        time.sleep(1)
        portal_canvas.select_panel('Panel 8')
        time.sleep(0.5)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Accordion')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Freeze Container', 'checkbox', checkbox_input='check', msg='Step 13.1:')
         
        """ Step 14: Click on BIP icon then exit and yes on saving.
        """
        portal_ribbon.bip_save_and_exit('Yes')
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        time.sleep(1)
         
        """ Step 15: Run the portal
                     Click '4 Col panel locked test'
                     Verify that all 8 panels are present.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
        
        """ Step 16: Press F8
                     Drag something from the tree into the container in col2
                     Verify that you can't move anything into the report and tree block in column2.
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
        column2_obj = portal_canvas.get_column_obj(2)
        panel_elems = column2_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column2_panel = panel_elems[['tagCloud chart' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        portal_run.drag_portal_resource_tree_item(BIP_Portal_Path+'->cd7', column2_panel)
        verify_coumn_panel_title(2, ['Panel 2', 'tagCloud chart'], '16')
        
        """ Step 17: Drag tagCloud chart in column 3 to column 2
                     Verify that you can drag
        """
        column3_obj = portal_canvas.get_column_obj(3)
        panel_elems = column3_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column3_panel = panel_elems[['tagCloud chart' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column3_panel_title=column3_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        column2_obj = portal_canvas.get_column_obj(2)
        panel_elems = column2_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column2_panel = panel_elems[['tagCloud chart' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column2_panel_title=column2_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(column3_panel_title, column2_panel_title, trg_cord_type='top_middle', ty_offset=-5)
        time.sleep(3)
        verify_coumn_panel_title(2, ['Panel 2', 'tagCloud chart', 'tagCloud chart'], '17')
        
        """ Step 18: Try to drag the original panels from column 2 into column 3
                     Verify that you can't drag them out of that column cause they are locked
        """
        column2_obj = portal_canvas.get_column_obj(2)
        panel_elems = column2_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column2_panel = panel_elems[['Panel 2' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column2_panel_title=column2_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        column3_obj = portal_canvas.get_column_obj(3)
        panel_elems = column3_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column3_panel = panel_elems[['Panel 3' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column3_panel_title=column3_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(column2_panel_title, column3_panel_title, trg_cord_type='top_middle')
        time.sleep(3)
        verify_coumn_panel_title(3, ['Panel 3'], '18')
        
        """ Step 19: Try to drag the area/tab from the panels in column1 and 2
                     Verify that you cant drag them out
                     Verify that there is no new tab or new area menu option
        """
        column1_obj = portal_canvas.get_column_obj(1)
        panel_elems = column1_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column1_panel = panel_elems[['Panel 1' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column1_panel_title=column1_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        column3_obj = portal_canvas.get_column_obj(3)
        panel_elems = column3_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column3_panel = panel_elems[['Panel 3' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column3_panel_title=column3_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(column1_panel_title, column3_panel_title, trg_cord_type='top_middle')
        time.sleep(3)
        column2_obj = portal_canvas.get_column_obj(2)
        panel_elems = column2_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column2_panel = panel_elems[['Panel 2' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column2_panel_title=column2_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        column3_obj = portal_canvas.get_column_obj(3)
        panel_elems = column3_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column3_panel = panel_elems[['Panel 3' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column3_panel_title=column3_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(column2_panel_title, column3_panel_title, trg_cord_type='top_middle')
        time.sleep(3)
        verify_coumn_panel_title(3, ['Panel 3'], '19')
        portal_canvas.verify_accordian_panel_title('Panel 1', ['Area 1', 'Category Sales'], "Step 19.1: Verify that there is no new area menu option")
        portal_canvas.verify_tabbed_panel('Panel 2', ['Tab 1', 'Units Profit Treemap'], "Step 19.2: Verify that there is no new tab menu option")
        
        """ Step 20: Click the menu option for the freezed panels in column1 and column2
                     Verify that only minimize, maximize, refresh are there.
        """
        portal_run.verify_column_panel_title_menubar_button(1, 'Panel 1', expected_opt=['Minimize', 'Maximize', 'Refresh'], msg="Step 20: ")
        portal_run.verify_column_panel_title_menubar_button(2, 'Panel 2', expected_opt=['Minimize', 'Maximize', 'Refresh'], msg="Step 20.1: ")
        portal_run.verify_column_panel_title_menubar_button(1, 'tagCloud chart', expected_opt=['Minimize', 'Maximize', 'Refresh'], msg="Step 20.2: ")
        portal_run.select_panel_in_column(1, 'tagCloud chart')
        portal_canvas.scroll_panel(0, 0, 'down', option='autohotkey', number_of_times=30)
        portal_run.verify_column_panel_title_menu_with_index(2, 2,'tagCloud chart', ['Minimize', 'Maximize', 'Refresh'], "Step 20.3: ")
        
        """ Step 21: Click the menu for the placeholder container in column 4 and choose replace.
                     Choose any content.
        """
        portal_run.select_panel('Panel 8')
        portal_canvas.scroll_panel(0, 0, 'up', option='autohotkey', number_of_times=20)
        portal_canvas.manage_panel_title_menubar('Regional Sales Trend', verify=False, select_menu_opt='Replace')
        selector_items = self.driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        elem = selector_items[[elem.text.strip() for elem in selector_items].index('Discount by Region')]
        elem.find_element_by_css_selector("img").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnOK']").click()
        time.sleep(3)
        portal_canvas.verify_panel_caption('Discount by Region', "Step 21: Verify placeholder container in column 4 with Discount by Region.")
        verify_panel_frame_data('riser', 'Panel_7', 16, '21.1', custom_css=".chartPanel [tdgtitle]")
        
        """ Step 22: Click the easy selector and choose any content
        """
        portal_run.select_panel('Discount by Region')
        portal_canvas.scroll_panel(0, 0, 'down', option='autohotkey', number_of_times=20)
        portal_canvas.select_easy_selector_item(4, 'Regional Sales Trend', option='column', button='Add')
#         portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_11')
#         utillobj.synchronize_with_visble_text("#jschart_HOLD_0  text[class*='xaxisOrdinal'][class*='title']", 'Month', 90)
#         utillobj.switch_to_default_content()
        time.sleep(3)
#         verify_panel_frame_data('legend', 'Panel_11', ['EMEA', 'North America', 'Oceania', 'South America'], '22')
        portal_canvas.scroll_panel(0, 0, 'up', option='autohotkey', number_of_times=20)
        
        """ Step 23: Try to drag one of the panels out of the responsive container
                     Verify that you can't drag anything out or into this container.
        """
        column4_obj = portal_canvas.get_column_obj(4)
        panel_elems = column4_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column4_panel = panel_elems[['Panel 8' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column4_panel_title=column4_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        column3_obj = portal_canvas.get_column_obj(3)
        panel_elems = column3_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column3_panel = panel_elems[['Panel 3' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column3_panel_title=column3_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(column4_panel_title, column3_panel_title, trg_cord_type='top_middle')
        time.sleep(3)
        verify_coumn_panel_title(3, ['Panel 3'], '23')
        column4_obj = portal_canvas.get_column_obj(4)
        panel_elems = column4_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column4_panel = panel_elems[['Panel 9' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column4_panel_title=column4_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        column3_obj = portal_canvas.get_column_obj(3)
        panel_elems = column3_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column3_panel = panel_elems[['Panel 3' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column3_panel_title=column3_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(column4_panel_title, column3_panel_title, trg_cord_type='top_middle')
        time.sleep(3)
        verify_coumn_panel_title(3, ['Panel 3'], '23.1')
        column4_obj = portal_canvas.get_column_obj(4)
        panel_elems = column4_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column4_panel = panel_elems[['Panel 10' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column4_panel_title=column4_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        column3_obj = portal_canvas.get_column_obj(3)
        panel_elems = column3_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        column3_panel = panel_elems[['Panel 3' in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        column3_panel_title=column3_panel.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(column4_panel_title, column3_panel_title, trg_cord_type='top_middle')
        time.sleep(3)
        verify_coumn_panel_title(3, ['Panel 3'], '23.2')
        
        """ Step 24: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 25:Navigate URL to http://environment_name:port/alias/legacyhome"""
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css,workspace,60)
        
        
        """ Step 26: Rerun the portal
                     Verify that the changes did not take place for the locked columns and locked containers but easy selector content will still show.
                     The move into column 2 will still show cause the column is not locked.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 50)
        verify_coumn_panel_title(1, ['Panel 1', 'tagCloud chart'], '26.1')
        verify_coumn_panel_title(2, ['Panel 2', 'tagCloud chart', 'tagCloud chart'], '26.2')
        verify_coumn_panel_title(3, ['Panel 3'], '26.3')
        
        """ Step 27: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 28: In the banner link, click on the top right username > Click Sign Out.
        """
        time.sleep(2)        

if __name__ == '__main__':
    unittest.main()