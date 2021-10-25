'''
Created on 08-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324324
TestCase Name = Page Designer : Create_New_Page
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import visualization_resultarea, ia_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324324_TestClass(BaseTestCase):

    def test_C2324324(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        Test_case_id = 'C2324324'
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
        
        def verify_panel_data(panel_name, expected_panel_text, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_panel_text, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
            
        def verify_column_data(column_no, expected_column_text, step_num):
            column_text = portal_canvas.get_column_obj(column_no)
            actual_column_text_list = [elem.strip() for elem in column_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_column_text, actual_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
        
        def verify_panel_frame_data(chart_type, panel_name, expected_legend, step_num, custom_css="svg g>text[class^='riser!s']"):
            utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe'][name*='" + panel_name + "']",frame_height_value=0)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'riser':
                ia_resultobj.verify_number_of_chart_segment("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify number of risers displayed in '" + str(panel_name) + "'.", custom_css=custom_css)   
            utillobj.switch_to_default_content(pause=3)
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
            Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 50)
        time.sleep(1)
        
        """ Step 2: Expand P292 domain, right click on S10117 folder and choose New Folder.
                    Enter 'Pages_Folder'
        """
        wf_mainpageobj.create_folder(BIP_Portal_Path, 'Pages_Folder')
         
        """ Step 3: Right Click on 'Pages_Folder' and choose New > Portal Page.
                    Verify that the "portal page" option is now seen in the folder context menu.
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->Pages_Folder', 'New', item_exit=True, expected_menu_list=['Portal Page'], msg="Step 3:")
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->Pages_Folder', 'New->Portal Page')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        coreutillobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 50)
         
        """ Step 4: Choose 2 columns
                    Enter 'Page_designer1'
                    Verify that the breadscrumbs have the correct terminology and not say Portals but says Page_designer1
        """
        portal_misobj.select_page_template(page_template="2 Column", Page_title='Page_designer1', btn_name='Create')
        portal_properties.verify_breadcrumb_panel('Page_designer1', ['Page_designer1'], "Step 4: Verify that the breadscrumbs have the correct terminology and not say Portals but says Page_designer1")
          
        """ Step 5: Add Category Sales in column 1 and drag and drop domain in column2
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(1)
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 1)
        time.sleep(1)
        item_path=root_path
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 2)
        time.sleep(2)
        verify_panel_frame_data('legend', 'Panel_1', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '5')
        verify_column_data(2, 'S10117', '5.1')
         
        """ Step 6: Click BIP icon then Save As
        """
        portal_ribbon.select_tool_menu_item('menu_SaveAs')
        cancel_btn_css = "#dlgIbfsOpenFile7 [class*='active'] #IbfsOpenFileDialog7_btnCancel"
        utillobj.synchronize_with_number_of_element(cancel_btn_css, 1, 50)
        canel_btn_elem = driver.find_element_by_css_selector(cancel_btn_css)
        utillobj.click_on_screen(canel_btn_elem, 'middle', click_type=0)
        time.sleep(3)
         
        """ Step 7: Click Cancel button
                    Verify that the save button is still enabled.
        """
        save_btn_status = driver.find_element_by_css_selector("#topToolBar #saveButton").is_enabled()
        utillobj.asequal(True, save_btn_status, "Step 7: Verify that the save button is still enabled.")
         
        """ Step 8: Save and exit
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        time.sleep(2)
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 50)
        time.sleep(1)
         
        """ Step 9: Right click on the folder and choose Publish
                    Verify that both the folder and page are now published
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->Pages_Folder', 'Publish')
        time.sleep(1)
        wf_mainpageobj.verify_folder_status(BIP_Portal_Path+'->Pages_Folder', status='published', msg="9")
        time.sleep(1)
        wf_mainpageobj.verify_folder_status(BIP_Portal_Path+'->Pages_Folder->Page_designer1', status='published', msg="9.1")
        
        """ Step 10: Right Click on Pages_Folder and choose New > Portal Page.
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->Pages_Folder', 'New', item_exit=True, expected_menu_list=['Portal Page'], msg="Step 9:")
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->Pages_Folder', 'New->Portal Page')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        coreutillobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 11: Choose fluid canvas as the layout
                     Enter 'Page_designer_fluid'
        """
        portal_misobj.select_page_template(page_template="Fluid Canvas", Page_title='Page_designer_fluid', btn_name='Create')
        time.sleep(3)
        portal_properties.verify_breadcrumb_panel('Page_designer_fluid', ['Page_designer_fluid'], "Step 4: Verify that the breadscrumbs have the correct terminology and not say Portals but says Page_designer1")
        
        """ Step 12: Click on Insert tab
                     Press F8
                     Drag and drop the Retail Samples domain
                     Verify Panel 1 gets created
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(1)
        item_path="Retail Samples"
        curent_page = portal_canvas.get_current_page()
        portal_run.drag_portal_resource_tree_item(item_path, curent_page)
        time.sleep(1)
        portal_canvas.verify_panel_caption('Panel 1', 'Step 12: Verify Panel 1 gets created')
        verify_panel_data('Panel 1', "Retail Samples", '12.1')
        time.sleep(1)
        
        """ Step 13: Choose Accordion under Containers
                     Verify that panel 2 is outlined. if not then bip-3038 needs to be reopened.
                     Choose Portal List under Content
        """
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Accordion')
        time.sleep(1)
        portal_canvas.verify_panel_caption('Panel 2', 'Step 13: Verify Panel 2 gets created')
        time.sleep(0.2)
        portal_canvas.verify_selected_panel_border('Panel 2', "Step 13.1: Verify that panel 2 is outlined. if not then bip-3038 needs to be 'Re-open'.")
        time.sleep(0.5)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_PortalList')
        time.sleep(1)
        verify_panel_data('Panel 2', 'lock column portal', "Step 13.2 Verify Portal List under Content")
        
        """ Step 14: Choose the middle to next last option for panel2. As you drag honda_integra image over the Cross you will see the areas being highlighted in red
                     Verify that "Column 2" has 2 panels in it.
        """
        item_path = BIP_Portal_Path + "->honda_integra"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', "Panel 2", ty_offset=150)
        
        '''Panle 1 location'''
        panel1_obj = portal_canvas.get_panel_obj('Panel 1')
        panel1_x_location = int(panel1_obj.location['x'])
        panel1_width = int(panel1_obj.size['width'])
        panel1_width_plus_x_location = panel1_x_location + panel1_width
        
        ''' Panel 2 location '''
        panel2_obj = portal_canvas.get_panel_obj('Panel 2')
        panel2_x_location = int(panel2_obj.location['x'])
        
        portal_canvas.select_panel('Panel 1')
        ''' honda Integra location '''
        honda_integra_panel_obj = portal_canvas.get_panel_obj('honda_integra')
        honda_integra_panel_x_location = int(honda_integra_panel_obj.location['x'])
        column2_status = True if panel2_x_location == honda_integra_panel_x_location and honda_integra_panel_x_location > panel1_width_plus_x_location and panel2_x_location > panel1_width_plus_x_location else False
        utillobj.asequal(True, column2_status, "Step 14: Verify that 'Column 2' has 2 panels in it, and 'Panel 2', 'honda_integra' added in column 2.")
        
        """ Step 15: Choose the lower option. As you drag the domain over, you will see the areas being highlighted in blue
                     Verify that it is added at the bottom of the page
        """
        item_path =root_path
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, 'panel', "honda_integra", drop_point='bottom_middle', ty_offset=-5)
        time.sleep(3)
        verify_panel_data('Panel 4', 'S10117', '15')
        
        '''Panle 1 location'''
        panel1_elem = portal_canvas.get_panel_obj('Panel 1')
        panel1_y_loc = int(panel1_elem.location['y'])
        panel1_width = int(panel1_elem.size['width'])
        panel1_height = int(panel1_elem.size['height'])
        panel1_height_plus_y_location = panel1_height + panel1_y_loc
        
        ''' Panel 2 location '''
        panel2_elem = portal_canvas.get_panel_obj('Panel 2')
        panel2_x_loc = int(panel2_elem.location['x'])
        panel2_width = int(panel2_elem.size['width'])
        panel2_x_plus_width = panel2_x_loc + panel2_width
        
        ''' honda Integra location '''
        honda_integra_panel_elem = portal_canvas.get_panel_obj('honda_integra')
        honda_integra_panel_y_loc = int(honda_integra_panel_elem.location['y'])
        honda_integra_panel_height = int(honda_integra_panel_elem.size['height'])
        honda_integra_height_plus_y_location = honda_integra_panel_height + honda_integra_panel_y_loc
        portal_canvas.select_panel('Panel 1')
        utillobj.take_screenshot(honda_integra_panel_elem, Test_case_id+"_Actual_Step_15")
        time.sleep(9)
        portal_canvas.select_panel('honda_integra')
        time.sleep(1)
        
        ''' panel 4 location '''
        panel4_obj = portal_canvas.get_panel_obj('Panel 4')
        panel4_x_location = int(panel4_obj.location['x'])
        panel4_y_location = int(panel4_obj.location['y'])
        panel4_width_size = int(panel4_obj.size['width'])
        panel4_x_plus_width = int(panel4_x_location) + int(panel4_width_size)
        column4_status = True if panel4_y_location > panel1_height_plus_y_location and panel4_y_location > honda_integra_height_plus_y_location else False
        utillobj.asequal(True, column4_status, "Step 15.1: Verify that domain panel added at the bottom of the page")
        column4_cover_full_widht = True if panel4_x_plus_width == panel2_x_plus_width else False
        utillobj.asequal(True, column4_cover_full_widht, "Step 15.2: Verify that domain panel cover full width on screen.")
        time.sleep(3)
        
        
        """ Step 16: Exit and save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        time.sleep(2)
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 50)
        time.sleep(1)
        
        """ Step 17: Publish the page
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->Pages_Folder->Page_designer_fluid', 'Publish')
        time.sleep(1)
        wf_mainpageobj.verify_folder_status(BIP_Portal_Path+'->Pages_Folder->Page_designer_fluid', status='published', msg="17")
        
        """ Step 18: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()