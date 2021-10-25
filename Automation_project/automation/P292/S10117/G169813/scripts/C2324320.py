'''
Created on 18-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324320
TestCase Name = Portal Designer_Design Properties : Freeze_Column
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon
from common.pages import vfour_miscelaneous, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException

class C2324320_TestClass(BaseTestCase):

    def test_C2324320(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
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
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
         
        """ step 2: Expand P292 domain , right click on S10117 folder and choose New > Collaborative Portal
        """
        """ Step 3: Enter lock column portal
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        coreutillobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
        portal_misobj.verify_page_template("Step 02.00: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
           
        """ Step 4: Add a 2 column page and name it as 'two_column_page'
        """
        portal_misobj.select_page_template(page_template="2 Column", Page_title='two_column_page', btn_name='Create')
           
        """ Step 5: Click on the page and uncheck the Lock page box in the properties section
        """
        portal_canvas.select_page_in_navigation_bar('two_column_page')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 05.00: ')
        time.sleep(2)
           
        """ Step 6: Click on Column 1. Check the Freeze Column box
        """
        portal_canvas.select_page_in_navigation_bar('two_column_page')
        time.sleep(2)
        portal_canvas.select_column(1)
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Freeze Column', 'checkbox', checkbox_input='check', msg='Step 06.00: ')
        time.sleep(2)
           
        """ Step 7: Click the Insert tab
        """
        """ Step 8: Add a tabbed container.
                    Add the resource tree in Tab 1
        """
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Tabbed')
        time.sleep(2)
        portal_canvas.select_panel('Panel 1')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
           
        """ Step 9: Click new tab and add the portal list there.
        """
        portal_canvas.select_tabbed_panel('Panel 1', 'New Tab')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_PortalList')
           
        """ Step 10: Add a panel container as well.
                     Drag Accordion_title from the BIP_V4_Portal folder there.
        """
        time.sleep(2)
        portal_canvas.select_column(1)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(1)
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(4)
        item_path=BIP_Portal_Path+"->Accordion_title"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 2", ty_offset=-63)
        time.sleep(5)
           
        """ Step 11: Click on Column 2, leave the Freeze Column box unchecked
        """
        portal_canvas.select_column(2)
           
        """ Step 12: Add the accordion container with the resource tree in Area 1 and drag the domain over the panel and choose Add as area
                     Verify Area 2 was created with the domain
        """
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Accordion')
        time.sleep(2)
        portal_canvas.select_panel('Panel 3')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        item_path=root_path
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3")
        utillobj.select_or_verify_bipop_menu('Add As Area', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        time.sleep(2)
        portal_canvas.verify_accordian_panel_title('Panel 3', ['Area 1', 'Area 2', 'New Area'], "Step 12.00: Verify Area 2 was created.")
        panel_3_obj = portal_canvas.get_panel_obj('Panel 3')
        actual_text = panel_3_obj.text.strip().replace(' ','').split('\n')
        expected_text =['Panel3', 'Area1', 'Area2', 'S10117', 'BIP_V4_Portal', 'BIP_xxx_Portal123_V4Resources', 'C2324318Resources', 'BIP_xxx_Portal123_V4', 'C2324318', 'NewArea']
        utillobj.as_List_equal(actual_text, expected_text, "Step 12.01: Verify Area 2 was created with the domain.")
        """ Step 13: Add a panel container as well. 
                     Drag Category Sales report from the Retail Samples --> Portal --> Small Widgets folder
        """
        time.sleep(2)
        portal_canvas.select_column(2)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(1)
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", ty_offset=-63)
        time.sleep(5)
           
        """ Step 14: Add another page and name it as 'Two_Col_placeholder_easy'
        """
        portal_canvas.add_page('1 Column',Page_title='Two_Col_placeholder_easy')
        time.sleep(1)
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        time.sleep(2)
           
        """ Step 15: Right click on the page tab and choose layout and 2 columns
        """
        portal_canvas.manage_page_menu('Two_Col_placeholder_easy', 'Page Layout', page_layout='Two Column')
           
        """ Step 16: Unlock the page and freeze Column 1
        """
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 16.00: ')
        time.sleep(2)
        portal_canvas.select_column(1)
        time.sleep(2)
        portal_properties.edit_input_control('page', 'Freeze Column', 'checkbox', checkbox_input='check', msg='Step 16.01: ')
        time.sleep(4)
           
        """ Step 17: Click Easy Selector check box
        """
        """ Step 18: Choose Retail Samples --> Portal --> Small Widgets folder
                     Verify that a + sign appears in that column1 area.
        """
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', launch_point='property_tab', button='OK', 
                                                section='column', item_name='Show Easy Selector', control='checkbox', checkbox_input='check', msg='Step 06.00:')
        status = False
        try:
            column_elem1 = portal_canvas.get_column_obj(1)
            status = column_elem1.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']").is_displayed()
        except NoSuchElementException:
            status = False
        utillobj.asequal(status, True, "Step 18.00: Verify that a + sign appears in that column1 area.")
        time.sleep(1)
           
        """ Step 19: Click Insert tab
                     Choose Easy selector
                     Verify that the browse folder window does not pops up
                     Verify that the new panel is on top
        """
        portal_canvas.select_column(1)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_EasySelector')
           
        """ ''' Step done by manual team '''
            Verify that the browse folder window does not pops up"""
        panel_obj = portal_canvas.get_panel_obj('Panel 1')
        x_location = panel_obj.location['x']
        y_location = panel_obj.location['y']
        statu_x = bool(x_location in range(7,20))
        statu_y = bool(y_location in range(200,230))
        utillobj.asequal(statu_x, True, "Step 19.00: Verify that the new panel is on top")
        utillobj.asequal(statu_y, True, "Step 19.01: Verify that the new panel is on top")
           
        """ Step 20: Leave Column 2 unfreeze, repeat steps from 17 to 19 for Column 2.
        """
        time.sleep(2)
        portal_canvas.select_column(2)
        time.sleep(2)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', launch_point='property_tab', button='OK', 
                                                section='column', item_name='Show Easy Selector', control='checkbox', checkbox_input='check', msg='Step 20.01:')
        status = False
        try:
            column_elem1 = portal_canvas.get_column_obj(1)
            status = column_elem1.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']").is_displayed()
        except NoSuchElementException:
            status = False
        utillobj.asequal(status, True, "Step 20.02: Verify that a + sign appears in that column1 area.")
        time.sleep(1)
        portal_canvas.select_column(2)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_EasySelector')
        panel_obj = portal_canvas.get_panel_obj('Panel 2')
        x_location = panel_obj.location['x']
        y_location = panel_obj.location['y']
        statu_x = bool(x_location in range(700,860))
        statu_y = bool(y_location in range(200,230))
        utillobj.asequal(statu_x, True, "Step 20.03: Verify that the new panel is on top")
        utillobj.asequal(statu_y, True, "Step 20.04 Verify that the new panel is on top")
           
        """ Step 21: Add a report/graph/image into each of those containers
        """
        time.sleep(2)
        portal_canvas.select_easy_selector_item('Panel 1', 'Category Sales', button='Add')
        time.sleep(2)
        portal_canvas.select_easy_selector_item('Panel 2', 'Regional Sales Trend', button='Add')
        time.sleep(2)
        portal_canvas.verify_panel_caption('Category Sales', "Step 21.00: Verify Category Sales added in Panel 1.")
        portal_canvas.verify_panel_caption('Regional Sales Trend', "Step 21.01: Verify Regional Sales Trend added in Panel 1.")
#           
        """ Step 22: Exit and save the portal
        """
        portal_ribbon.bip_save_and_exit(btn_name='Yes')
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
          
        """ Step 23: Run the portal
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
           
        """ Step 24: Click two_column_page
        """
        portal_canvas.select_page_in_navigation_bar('two_column_page')
           
        """ Step 25: Try to drag Panel 3 into column 1
                     Verify that you get the no drop icon as you should NOT be able to do that.
                     Verify that you dont get the normal panel outline into column 1 and that the panels dont adjust their positions.
        """
        panel3_obj = portal_canvas.get_panel_obj('Panel 3')
        x_loc = int(panel3_obj.location['x'])
        y_loc = int(panel3_obj.location['y'])
        panelobj =  portal_canvas.get_panel_obj('Accordion_title')
        panel3_title_obj = panel3_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel3_title_obj, panelobj)
        time.sleep(5)
        panel3_obj1 = portal_canvas.get_panel_obj('Panel 3')
        x_loc1 = int(panel3_obj1.location['x'])
        y_loc1 = int(panel3_obj1.location['y'])
        if x_loc == x_loc1 and  y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 25.00: Verify that you get the no drop icon as you should NOT be able to do that.")
        status=False
        try:
            if driver.find_element_by_css_selector("[id*='ReplaceMarker'][class*='drop-target']").is_displayed():
                status=False
        except NoSuchElementException:
            status=True
        utillobj.asequal(True, status, "Step 25.01: Verify that you dont get the normal panel outline into column 1 and that the panels dont adjust their positions.")
#           
        """ Step 26: Press F8 and try to drag anything into column 1
                     Verify that you get the no drop icon as you should NOT be able to do that.
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        item_path = BIP_Portal_Path+"->cd7"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        col_obj = portal_canvas.get_column_obj(1)
        panel_elems = col_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        col_status = 'cd7' not in [elem.text.strip() for elem in panel_elems]
        utillobj.asequal(True, col_status, "Step 26.00: Verify that you get the no drop icon as you should NOT be able to do that.")
           
        """ Step 27: Try to drag panel 2 into column 2
                     Verify that you can't move that panel out of column 1
        """
        panel2_obj = portal_canvas.get_panel_obj('Accordion_title')
        x_loc = int(panel2_obj.location['x'])
        y_loc = int(panel2_obj.location['y'])
        panelobj =  portal_canvas.get_panel_obj('Panel 3')
        panel2_title_obj = panel2_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel2_title_obj, panelobj)
        time.sleep(5)
        panel2_obj1 = portal_canvas.get_panel_obj('Accordion_title')
        x_loc1 = int(panel2_obj1.location['x'])
        y_loc1 = int(panel2_obj1.location['y'])
        if x_loc == x_loc1 and y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 27: Verify that you get the no drop icon as you should NOT be able to do that.")
           
        """ Step 28: Try to arrange the order of panel 1 and panel2 in column1.
                     Verify that you can't move the containers around.
        """
        panel1_obj = portal_canvas.get_panel_obj('Panel 1')
        x_loc = int(panel1_obj.location['x'])
        y_loc = int(panel1_obj.location['y'])
        panelobj =  portal_canvas.get_panel_obj('Accordion_title')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, panelobj)
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Panel 1')
        x_loc1 = int(panel1_obj1.location['x'])
        y_loc1 = int(panel1_obj1.location['y'])
        if x_loc == x_loc1 and y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 28: Verify that you can't move the containers around.")
           
        """ Step 29: Try to arrange the order of panel 3 and panel 4 in column2.
                     Verify that the change did take place.
        """
        panel1_obj = portal_canvas.get_panel_obj('Category Sales')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        panelobj =  portal_canvas.get_panel_obj('Panel 3')
        paneltitleobj = panelobj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, paneltitleobj, trg_cord_type='top_middle')
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Category Sales')
        y_loc1 = int(panel1_obj1.location['y'])
        statu_y = bool(y_loc1 in range(70, 100))
        utillobj.asequal(True, statu_y, "Step 29.00: Verify that the change did take place.")
          
        """ Step 30: Try to drag tab 1 out of that panel into column 1 and column2
                     Verify that you can't drag it out.
        """
        panel1_obj = portal_canvas.get_panel_obj('Panel 1')
        panel_tab= panel1_obj.find_elements_by_css_selector("[id^='BipTabBar'] [id^='BipTabButton']")
        x_loc = int(panel_tab[0].location['x'])
        y_loc = int(panel_tab[0].location['y'])
        panelobj =  portal_canvas.get_panel_obj('Category Sales')
        portal_misobj.drag_drop_in_bip(panel_tab[0], panelobj)
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Panel 1')
        panel_tab1= panel1_obj1.find_elements_by_css_selector("[id^='BipTabBar'] [id^='BipTabButton']")
        x_loc1 = int(panel_tab1[0].location['x'])
        y_loc1 = int(panel_tab1[0].location['y'])
        if x_loc == x_loc1 and y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 30: Verify that you can't drag it out tab 1.")
          
        """ Step 31: Try to drag Area 1 out of that container into column1 and column2
                     Verify that you can't drag it into column1 but you can into column 2
        """
        panel1_obj = portal_canvas.get_panel_obj('Panel 3')
        panel_tab= panel1_obj.find_elements_by_css_selector("[id^='BipAccordionPane'] [id^='BipAccordionButton'] [class*='bip-accordion-button']")
        x_loc = int(panel_tab[0].location['x'])
        y_loc = int(panel_tab[0].location['y'])
        panelobj =  portal_canvas.get_panel_obj('Accordion_title')
        portal_misobj.drag_drop_in_bip(panel_tab[0], panelobj)
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Panel 3')
        panel_tab1= panel1_obj1.find_elements_by_css_selector("[id^='BipAccordionPane'] [id^='BipAccordionButton'] [class*='bip-accordion-button']")
        x_loc1 = int(panel_tab1[0].location['x'])
        y_loc1 = int(panel_tab1[0].location['y'])
        if x_loc == x_loc1 and  y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 31.00: Verify that you can't drag it out Area 1 into column 1.")
          
        panel1_obj = portal_canvas.get_panel_obj('Panel 3')
        panel_tab= panel1_obj.find_elements_by_css_selector("[id^='BipAccordionPane'] [id^='BipAccordionButton'] [class*='bip-accordion-button']")
        panelobj =  portal_canvas.get_panel_obj('Panel 3')
        panel1_title_obj = panelobj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel_tab[0], panel1_title_obj, trg_cord_type='top_middle')
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_column_obj(2)
        panel_text = panel1_obj1.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        actual_panel_text = [elem.text.strip() for elem in panel_text]
        expected_panel_text = ['Category Sales', 'Area 1', 'Panel 3']
        utillobj.asequal(expected_panel_text, actual_panel_text, "Step 31.01: Verify that you can drag it out Area 1 into column 1.")
          
        """ Step 32: Click on 'Two_Col_placeholder_easy page'
        """
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        time.sleep(3)
            
        """ Step 33: Try to drag Panel 2 into column 1
                     Verify that you get the no drop icon as you should NOT be able to do that.
                     Verify that you don't get the normal panel outline into column 1 and that the panels dont adjust their positions.
        """
        panel1_obj = portal_canvas.get_panel_obj('Regional Sales Trend')
        x_loc = int(panel1_obj.location['x'])
        y_loc = int(panel1_obj.location['y'])
        panelobj =  portal_canvas.get_panel_obj('Category Sales')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, panelobj)
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Regional Sales Trend')
        x_loc1 = int(panel1_obj1.location['x'])
        y_loc1 = int(panel1_obj1.location['y'])
        if x_loc == x_loc1 and y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 33.00: Verify that you can't move those in column 1 around.")
           
        """ Step 34: Press F8 and try to drag anything into column 1
                     Verify that you get the no drop icon as you should NOT be able to do that.
        """
        item_path = BIP_Portal_Path+"->cd7"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'column', 1)
        col_obj = portal_canvas.get_column_obj(1)
        panel_elems = col_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        col_status = 'cd7' not in [elem.text.strip() for elem in panel_elems]
        utillobj.asequal(True, col_status, "Step 34.00: Verify that you get the no drop icon as you should NOT be able to do that.")
           
        """ Step 35: Try to drag panel 1 into column 2
                     Verify that you cant move that panel out of column 1
        """
        panel1_obj = portal_canvas.get_panel_obj('Category Sales')
        x_loc = int(panel1_obj.location['x'])
        y_loc = int(panel1_obj.location['y'])
        panelobj =  portal_canvas.get_panel_obj('Regional Sales Trend')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, panelobj)
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Category Sales')
        x_loc1 = int(panel1_obj1.location['x'])
        y_loc1 = int(panel1_obj1.location['y'])
        if x_loc == x_loc1 and y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 35: Verify that you can't move those in column 1 around.")
           
        """ Step 36: Click the + sign in column 1 and add anything.
                     Try to move that new container around
                     Verify that a new panel has been added.
                     Verify that you can't move it around
        """
        portal_canvas.select_easy_selector_item(1, 'Discount by Region', option='column', button='Add')
        time.sleep(3)
        portal_canvas.verify_panel_caption('Discount by Region', "Step 36.00: Verify that a new panel has been added.")
        panel1_obj = portal_canvas.get_panel_obj('Discount by Region')
        x_loc = int(panel1_obj.location['x'])
        y_loc = int(panel1_obj.location['y'])
        panelobj =  portal_canvas.get_panel_obj('Regional Sales Trend')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, panelobj)
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Discount by Region')
        x_loc1 = int(panel1_obj1.location['x'])
        y_loc1 = int(panel1_obj1.location['y'])
        if x_loc == x_loc1 and y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 36.1: Verify that you can't move those in column 1 around.")
           
        """ Step 37: Click the + sign in column 2 and anything.
                     Try to move that new container around
                     Verify that a new panel has been added.
                     Verify that you can move it around within that column only
        """
        portal_canvas.select_easy_selector_item(2, 'Regional Profit by Category', option='column', button='Add')
        time.sleep(3)
        portal_canvas.verify_panel_caption('Regional Profit by Category', "Step 37.00: Verify that a new panel has been added.")
        panel1_obj = portal_canvas.get_panel_obj('Regional Profit by Category')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        panelobj =  portal_canvas.get_panel_obj('Regional Sales Trend')
        panel1_title_obj1 = panelobj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, panel1_title_obj1, trg_cord_type='top_middle')
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Regional Profit by Category')
        y_loc1 = int(panel1_obj1.location['y'])
        statu_y = False
        statu_y = bool(y_loc1 in range(70, 100))
        utillobj.asequal(True, statu_y, "Step 37.01: Verify that the change did take place.")
          
        """ Step 38: Click the menu in the easy selector containers for both columns and choose replace.
                     Add some new content there for both columns
        """
        time.sleep(2)
        portal_canvas.manage_panel_title_menubar('Discount by Region', verify=False, select_menu_opt='Replace')
        time.sleep(1)
        parent_css = "[id^='dlgIbfsOpenFile'] [class*='active'] [class*='window-caption']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep)
        time.sleep(4)
        selector_items = driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        elem = selector_items[[elem.text.strip() for elem in selector_items].index('Average Cost v Sales')]
        elem.find_element_by_css_selector("img").click()
        time.sleep(6)
        btn_css="[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnOK']"
        add_button=utillobj.validate_and_get_webdriver_object(btn_css, "Button CSS")
        coreutillobj.left_click(add_button)
#         driver.find_element_by_css_selector(btn_css).click()
        time.sleep(3)
        portal_canvas.verify_panel_caption('Average Cost v Sales', "Step 38.00: Verify Panel Repalced in column 1.")
        time.sleep(1)
        portal_canvas.manage_panel_title_menubar('Regional Sales Trend', verify=False, select_menu_opt='Replace')
        time.sleep(1)
        parent_css = "[id^='dlgIbfsOpenFile'] [class*='active'] [class*='window-caption']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep)
        time.sleep(1)
        selector_items = driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        elem = selector_items[[elem.text.strip() for elem in selector_items].index('Discount by Region')]
        elem.find_element_by_css_selector("img").click()
        time.sleep(6)
        btn_css="[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnOK']"
        add_button=utillobj.validate_and_get_webdriver_object(btn_css, "Button CSS")
        coreutillobj.left_click(add_button)
        time.sleep(9)
        portal_canvas.verify_panel_caption('Discount by Region', "Step 38.01: Verify Panel Repalced in column 1.")
          
        """ Step 39: Try to arrange the order of panel 1 and panel2 in column1
                     Verify that you cant move the containers around.
        """
        panel1_obj = portal_canvas.get_panel_obj('Category Sales')
        x_loc = int(panel1_obj.location['x'])
        y_loc = int(panel1_obj.location['y'])
        panelobj =  portal_canvas.get_panel_obj('Average Cost v Sales')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, panelobj)
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Category Sales')
        x_loc1 = int(panel1_obj1.location['x'])
        y_loc1 = int(panel1_obj1.location['y'])
        if x_loc == x_loc1 and y_loc == y_loc1:
            stats_x = True
        else:
            stats_x = False
        utillobj.asequal(True, stats_x, "Step 39: Verify that you can't move those in column 1 around.")
          
        """ Step 40: Try to arrange the order of panel 3 and panel 4 in column2
                     Verify that the change did take place.
        """
        panel1_obj = portal_canvas.get_panel_obj('Discount by Region')
        panel1_title_obj = panel1_obj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        panelobj =  portal_canvas.get_panel_obj('Regional Profit by Category')
        paneltitleobj = panelobj.find_element_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        portal_misobj.drag_drop_in_bip(panel1_title_obj, paneltitleobj, trg_cord_type='top_middle')
        time.sleep(5)
        panel1_obj1 = portal_canvas.get_panel_obj('Discount by Region')
        y_loc1 = int(panel1_obj1.location['y'])
        statu_y = bool(y_loc1 in range(70, 100))
        utillobj.asequal(True, statu_y, "Step 40.00: Verify that the change did take place.")
         
        portal_canvas.select_page_in_navigation_bar('two_column_page')
        time.sleep(3)
         
        ''' Verification in two_column_page for panel 1  in lock column '''
        portal_canvas.verify_panel_caption('Panel 1', 'Step 40.01: Verify "Panel 1" title in two_column_page visible.')
        panel1_obj = portal_canvas.get_panel_obj('Panel 1')
        panel1_obj_x_loc = panel1_obj.location['x']
        panel1_obj_y_loc = panel1_obj.location['y']
          
        ''' Verification in two_column_page for Accordion_title  in lock column '''
        portal_canvas.verify_panel_caption('Accordion_title', 'Step 40.02: Verify "Accordion_title" title in two_column_page visible.')
        Accordion_title_obj = portal_canvas.get_panel_obj('Accordion_title')
        Accordion_title_obj_x_loc = Accordion_title_obj.location['x']
        Accordion_title_obj_y_loc = Accordion_title_obj.location['y']
          
        ''' Verification in two_column_page for Category Sales  in Unlock column '''
        portal_canvas.verify_panel_caption('Category Sales', 'Step 40.03: Verify "Category Sales" title in two_column_page visible.')
        category_sales_obj = portal_canvas.get_panel_obj('Category Sales')
        category_sales_obj_y_loc = category_sales_obj.location['y']
          
        ''' Verification in two_column_page for Area 1  in Unlock column '''
        portal_canvas.verify_panel_caption('Area 1', 'Step 40.04: Verify "Area 1" title in two_column_page visible.')
        area1_obj = portal_canvas.get_panel_obj('Area 1')
        area1_obj_y_loc = area1_obj.location['y']
          
        ''' Verification in two_column_page for Panel 3  in Unlock column '''
        portal_canvas.verify_panel_caption('Panel 3', 'Step 40.05: Verify "Panel 3" title in two_column_page visible.')
        panel3_obj = portal_canvas.get_panel_obj('Panel 3')
        panel3_obj_y_loc = panel3_obj.location['y']
          
        ''' verification for Two_Col_placeholder_easy page        '''
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        time.sleep(3)
          
        ''' Verification in Two_Col_placeholder_easy for Category Sales  in lock column '''
        portal_canvas.verify_panel_caption('Category Sales', 'Step 40.06: Verify "Category Sales" title in Two_Col_placeholder_easy visible.')
        category_sales_obj1 = portal_canvas.get_panel_obj('Category Sales')
        category_sales_obj1_x_loc = category_sales_obj1.location['x']
        category_sales_obj1_y_loc = category_sales_obj1.location['y']
          
        ''' Verification in Two_Col_placeholder_easy for Average Cost v Sales  in lock column '''
        portal_canvas.verify_panel_caption('Average Cost v Sales', 'Step 40.07: Verify "Average Cost v Sales" title in Two_Col_placeholder_easy visible.')
        average_cost_v_sales_obj1 = portal_canvas.get_panel_obj('Average Cost v Sales')
        average_cost_v_sales_x_loc = average_cost_v_sales_obj1.location['x']
        average_cost_v_sales_y_loc = average_cost_v_sales_obj1.location['y']
          
        ''' Verification in Two_Col_placeholder_easy for Regional Profit by Category  in Unlock column '''
        portal_canvas.verify_panel_caption('Regional Profit by Category', 'Step 40.08: Verify "Regional Profit by Category" title in Two_Col_placeholder_easy visible.')
        regional_profit_by_category_obj1 = portal_canvas.get_panel_obj('Regional Profit by Category')
        regional_profit_by_category_y_loc = regional_profit_by_category_obj1.location['y']
          
        ''' Verification in Two_Col_placeholder_easy for Discount by Region  in Unlock column '''
        portal_canvas.verify_panel_caption('Discount by Region', 'Step 40.09: Verify "Discount by Region" title in Two_Col_placeholder_easy visible.')
        discount_by_region_obj1 = portal_canvas.get_panel_obj('Discount by Region')
        discount_by_region_obj1_y_loc = discount_by_region_obj1.location['y']
        
        """ Step 41: Click close and Navigate URL to http://environment_name:port/alias/legacyhome"""
        
        
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)

        """
        Step 42: Rerun the portal Verify that the changes are still there for the unlocked columns.
        Verify that changes appear for the locked columns for the easy selector container and easy selector
        """
        
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
        portal_canvas.select_page_in_navigation_bar('two_column_page')
        time.sleep(3)
        
        ''' Verification in two_column_page for panel 1  in lock column '''
        portal_canvas.verify_panel_caption('Panel 1', 'Step 42.00: Verify "Panel 1" title in two_column_page visible.')
        panel1_obj = portal_canvas.get_panel_obj('Panel 1')
        panel1_obj_x_loc1 = panel1_obj.location['x']
        panel1_obj_width_loc1 = panel1_obj.size['width']
        panel1obj_actualwidht = panel1_obj_x_loc1 + panel1_obj_width_loc1
        panel1_obj_y_loc1 = panel1_obj.location['y']
        status_panel1 = False
        if panel1_obj_x_loc == panel1_obj_x_loc1 and panel1_obj_y_loc == panel1_obj_y_loc1:
            status_panel1 = True
        else:
            status_panel1 = False
        utillobj.asequal(True, status_panel1, 'Step 42.01: Verify Panel 1 still there without any changes in two_column_page.')
         
        ''' Verification in two_column_page for Accordion_title  in lock column '''
        portal_canvas.verify_panel_caption('Accordion_title', 'Step 42.02: Verify "Accordion_title" title in two_column_page visible.')
        Accordion_title_obj = portal_canvas.get_panel_obj('Accordion_title')
        Accordion_title_obj_x_loc1 = Accordion_title_obj.location['x']
        Accordion_title_obj_y_loc1 = Accordion_title_obj.location['y']
        Accordion_title_status = False
        if Accordion_title_obj_x_loc == Accordion_title_obj_x_loc1 and Accordion_title_obj_y_loc == Accordion_title_obj_y_loc1:
            Accordion_title_status = True
        else:
            Accordion_title_status = False
        utillobj.asequal(True, Accordion_title_status, 'Step 42.03: Verify Accordion_title still there without any changes in two_column_page.')
         
        ''' Verification in two_column_page for Category Sales  in Unlock column '''
        portal_canvas.verify_panel_caption('Category Sales', 'Step 42.04: Verify "Category Sales" title in two_column_page visible.')
        category_sales_obj = portal_canvas.get_panel_obj('Category Sales')
        category_sales_obj_x_loc1 = category_sales_obj.location['x']
        category_sales_obj_y_loc1 = category_sales_obj.location['y']
        
        category_sales_status = False
        if category_sales_obj_x_loc1 > panel1obj_actualwidht and category_sales_obj_y_loc == category_sales_obj_y_loc1:
            category_sales_status = True
        else:
            category_sales_status = False
        utillobj.asequal(True, category_sales_status, 'Step 42.05: Verify Category Sales still there without any changes in two_column_page.')
         
        ''' Verification in two_column_page for Area 1  in Unlock column '''
        portal_canvas.verify_panel_caption('Area 1', 'Step 42.06: Verify "Area 1" title in two_column_page visible.')
        area1_obj = portal_canvas.get_panel_obj('Area 1')
        area1_obj_x_loc1 = area1_obj.location['x']
        area1_obj_y_loc1 = area1_obj.location['y']
        area1_status = False
        if area1_obj_x_loc1 > panel1obj_actualwidht and area1_obj_y_loc == area1_obj_y_loc1:
            area1_status = True
        else:
            area1_status = False
        utillobj.asequal(True, area1_status, 'Step 42.07: Verify Category Sales still there without any changes in two_column_page.')
         
        ''' Verification in two_column_page for Panel 3  in Unlock column '''
        portal_canvas.verify_panel_caption('Panel 3', 'Step 42.08: Verify "Panel 3" title in two_column_page visible.')
        panel3_obj = portal_canvas.get_panel_obj('Panel 3')
        panel3_obj_x_loc1 = panel3_obj.location['x']
        panel3_obj_y_loc1 = panel3_obj.location['y']
        panel3_status = False
        if panel3_obj_x_loc1 > panel1obj_actualwidht and panel3_obj_y_loc == panel3_obj_y_loc1:
            panel3_status = True
        else:
            panel3_status = False
        utillobj.asequal(True, panel3_status, 'Step 42.09: Verify Panel 3 still there without any changes in two_column_page.')
        
        two_column_page_column_obj = portal_canvas.get_column_obj(1)
        panel_text = two_column_page_column_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        actual_panel_text = [elem.text.strip() for elem in panel_text]
        expected_panel_text = ['Panel 1', 'Accordion_title']
        utillobj.asequal(expected_panel_text, actual_panel_text, "Step 42.10: Verify column 1 panel still there without any changes in two_column_page.")
        
        two_column_page_column_obj1 = portal_canvas.get_column_obj(2)
        panel_text = two_column_page_column_obj1.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        actual_panel_text = [elem.text.strip() for elem in panel_text]
        expected_panel_text = ['Category Sales', 'Area 1', 'Panel 3']
        utillobj.asequal(expected_panel_text, actual_panel_text, "Step 42.11: Verify column 2 panel still there without any changes in two_column_page.")
        
        ''' verification for Two_Col_placeholder_easy page        '''
        portal_canvas.select_page_in_navigation_bar('Two_Col_placeholder_easy')
        time.sleep(3)
         
        ''' Verification in Two_Col_placeholder_easy for Category Sales  in lock column '''
        portal_canvas.verify_panel_caption('Category Sales', 'Step 42.12: Verify "Category Sales" title in Two_Col_placeholder_easy visible.')
        category_sales_obj1 = portal_canvas.get_panel_obj('Category Sales')
        category_sales_obj1_x_loc1 = category_sales_obj1.location['x']
        category_sales_obj1_width_loc1 = category_sales_obj1.size['width']
        panel2obj_actualwidht = category_sales_obj1_x_loc1 + category_sales_obj1_width_loc1
        category_sales_obj1_y_loc1 = category_sales_obj1.location['y']
        category_sales_status = False
        if category_sales_obj1_x_loc == category_sales_obj1_x_loc1 and category_sales_obj1_y_loc == category_sales_obj1_y_loc1:
            category_sales_status = True
        else:
            category_sales_status = False
        utillobj.asequal(True, category_sales_status, 'Step 42.13: Verify Category Sales still there without any changes in Two_Col_placeholder_easy.')
         
        ''' Verification in Two_Col_placeholder_easy for Average Cost v Sales  in lock column '''
        portal_canvas.verify_panel_caption('Average Cost v Sales', 'Step 42.14: Verify "Average Cost v Sales" title in Two_Col_placeholder_easy visible.')
        average_cost_v_sales_obj1 = portal_canvas.get_panel_obj('Average Cost v Sales')
        average_cost_v_sales_x_loc1 = average_cost_v_sales_obj1.location['x']
        average_cost_v_sales_y_loc1 = average_cost_v_sales_obj1.location['y']
        average_cost_v_sales_status = False
        if average_cost_v_sales_x_loc == average_cost_v_sales_x_loc1 and average_cost_v_sales_y_loc == average_cost_v_sales_y_loc1:
            average_cost_v_sales_status = True
        else:
            average_cost_v_sales_status = False
        utillobj.asequal(True, average_cost_v_sales_status, 'Step 42.15: Verify Average Cost v Sales still there without any changes in Two_Col_placeholder_easy.')
         
        ''' Verification in Two_Col_placeholder_easy for Regional Profit by Category  in Unlock column '''
        portal_canvas.verify_panel_caption('Regional Profit by Category', 'Step 42.16: Verify "Regional Profit by Category" title in Two_Col_placeholder_easy visible.')
        regional_profit_by_category_obj1 = portal_canvas.get_panel_obj('Regional Profit by Category')
        regional_profit_by_category_x_loc1 = regional_profit_by_category_obj1.location['x']
        regional_profit_by_category_y_loc1 = regional_profit_by_category_obj1.location['y']
        regional_profit_by_category_status = False
        if regional_profit_by_category_x_loc1 > panel2obj_actualwidht and regional_profit_by_category_y_loc == regional_profit_by_category_y_loc1:
            regional_profit_by_category_status = True
        else:
            regional_profit_by_category_status = False
        utillobj.asequal(True, regional_profit_by_category_status, 'Step 42.17: Verify Regional Profit by Category still there without any changes in two_column_page.')
         
        ''' Verification in Two_Col_placeholder_easy for Discount by Region  in Unlock column '''
        portal_canvas.verify_panel_caption('Discount by Region', 'Step 42.18: Verify "Discount by Region" title in Two_Col_placeholder_easy visible.')
        discount_by_region_obj1 = portal_canvas.get_panel_obj('Discount by Region')
        discount_by_region_obj1_x_loc1 = discount_by_region_obj1.location['x']
        discount_by_region_obj1_y_loc1 = discount_by_region_obj1.location['y']
        discount_by_region_obj1_status = False
        if discount_by_region_obj1_x_loc1 > panel2obj_actualwidht and discount_by_region_obj1_y_loc == discount_by_region_obj1_y_loc1:
            discount_by_region_obj1_status = True
        else:
            discount_by_region_obj1_status = False
        utillobj.asequal(True, discount_by_region_obj1_status, 'Step 42.19: Verify Discount by Region still there without any changes in Two_Col_placeholder_easy.')
        
        panel1_obj1 = portal_canvas.get_column_obj(1)
        panel_text = panel1_obj1.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        actual_panel_text = [elem.text.strip() for elem in panel_text]
        expected_panel_text = ['Category Sales', 'Average Cost v Sales']
        utillobj.asequal(expected_panel_text, actual_panel_text, "Step 42.20: Verify column 1 panel still there without any changes in Two_Col_placeholder_easy.")
        
        panel1_obj1 = portal_canvas.get_column_obj(2)
        panel_text = panel1_obj1.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel'] [id^='BiLabel'][class*='bip-title-bar']")
        actual_panel_text = [elem.text.strip() for elem in panel_text]
        expected_panel_text = ['Discount by Region', 'Regional Profit by Category']
        utillobj.asequal(expected_panel_text, actual_panel_text, "Step 42.21: Verify column 2 panel still there without any changes in Two_Col_placeholder_easy.")
        
        """ Step 43: Click close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 44: In the banner link, click on the top right username > Click Sign Out.
        """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()