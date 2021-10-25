'''
Created on 10-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324325
TestCase Name = Page Designer : Create_page_within_page
'''
import unittest, time
from common.lib import utillity,core_utility
from common.pages import visualization_resultarea, ia_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_ribbon, vfour_miscelaneous, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324325_TestClass(BaseTestCase):

    def test_C2324325(self):
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
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal->Pages_Folder'
        
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
        Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 50)
        time.sleep(1)
        
        """ Step 2: Open P292 ->S10117 -> 'Pages_folder' from domains tree,
        """
        """ Step 3: Right on 'Page_designer1' and choose Edit
                    Verify that page designer is opened and the page is displayed properly
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->Page_designer1', 'Edit')
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
        time.sleep(2)
        verify_panel_frame_data('legend', 'Panel_1', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '3')
        verify_column_data(2, 'S10117', '3.1')
         
        """ Step 4: Add another container onto the page
        """
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(1)
         
        """ Step 5: Click the BIP icon and choose New page
                    Verify that you get prompted to save the portal
        """
        portal_ribbon.select_tool_menu_item('menu_NewPage')
        dialog_css = "#dlgSavepromptPortal [class*='active']"
        cancel_btn_css = dialog_css + " #noDialogbtnAction"
        resultobj.wait_for_property(cancel_btn_css, 1, expire_time=25)
        actual_dialog_text = [elem.strip() for elem in driver.find_element_by_css_selector(dialog_css).text.strip().split('\n') if elem != '']
        expected_dialog_text = ['Page Designer', 'Do you want to save the changes you made to', "'Page_designer1'?", 'Yes', 'No', 'Cancel']
        utillobj.as_List_equal(actual_dialog_text, expected_dialog_text, "Step 5: Verify that you get prompted to save the portal")
         
        """ Step 6: Click No
                    Verify that the New Page template window appears
        """
        canel_btn_elem = driver.find_element_by_css_selector(cancel_btn_css)
        utillobj.click_on_screen(canel_btn_elem, 'middle', click_type=0)
        time.sleep(1)
        add_page_css = "#dlgTitleExplorer [class*='active'] [class*='window-caption']"
        resultobj.wait_for_property(add_page_css, 1, expire_time=25)
        new_page = driver.find_element_by_css_selector(add_page_css).text.strip()
        utillobj.asequal('Add Page', new_page, "Step 6: Verify that the New Page template window appears")
         
        """ Step 7: Choose 1 column
                    Enter 'Page_within_page'
                    Verify that the new page takes over the original window
        """
        portal_misobj.select_page_template(page_template="1 Column", Page_title='Page_within_page', btn_name='Create')
        time.sleep(2)
        portal_properties.verify_breadcrumb_panel('Page_within_page', ['Page_within_page'], "Step 7.1: Verify that the new page takes over the original window.")
         
        """ Step 8: Press F8
                    Drag the Retail Samples domain onto the page canvas
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(1)
        item_path="Retail Samples"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 1)
        time.sleep(2)
        verify_panel_data('Panel 1', 'Retail Samples', "8")
         
        """ Step 9: Click the BIP icon and choose New Page
                    Verify that you are asked to save the page.
        """
        portal_ribbon.select_tool_menu_item('menu_NewPage')
        dialog_css = "#dlgSavepromptPortal [class*='active']"
        yes_btn_css = dialog_css + " #yesDialogbtnAction"
        resultobj.wait_for_property(cancel_btn_css, 1, expire_time=25)
        actual_dialog_text = [elem.strip() for elem in driver.find_element_by_css_selector(dialog_css).text.strip().split('\n') if elem != '']
        expected_dialog_text = ['Page Designer', 'Do you want to save the changes you made to', "'Page_within_page'?", 'Yes', 'No', 'Cancel']
        utillobj.as_List_equal(actual_dialog_text, expected_dialog_text, "Step 9: Verify that you get prompted to save the portal")
         
        """ Step 10: Click Yes
                     Verify that the New Page input window appears
        """
        yes_btn_elem = driver.find_element_by_css_selector(yes_btn_css)
        utillobj.click_on_screen(yes_btn_elem, 'middle', click_type=0)
        parent_css= "div[id^='dlgPortalSaveDialog']"
        resultobj.wait_for_property(parent_css, 1)
        utillity.UtillityMethods.click_dialog_button(self, parent_css, "OK")
        time.sleep(1)
        resultobj.wait_for_property(add_page_css, 1, expire_time=25)
        new_page = driver.find_element_by_css_selector(add_page_css).text.strip()
        utillobj.asequal('Add Page', new_page, "Step 10: Verify that the New Page template window appears")
         
        """ Step 11: Choose 2 column layout
                     Enter Page_within_page
                     Delete the 1 in the Name attribute. by default we enter1, _2 if the name already exists.
                     Verify that you get an error message
        """
        portal_misobj.select_page_template(page_template="2 Column", Page_title='Page_within_page', Page_name='Page_within_page', btn_name='Create')
        time.sleep(1)
        parent_css= "[id*='BiDialog'] [class*='window-active']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        actual_dialog_text = [elem.strip() for elem in driver.find_element_by_css_selector(parent_css).text.strip().split('\n') if elem != '']
        expected_dialog_text = ['Warning', 'Page already exists. Do you want to replace it?', 'All customizations will be lost!', 'Yes', 'No']
        utillobj.as_List_equal(actual_dialog_text, expected_dialog_text, "Step 11: Verify that you get an error message")
          
        """ Step 12: Click No in the message
        """
        utillity.UtillityMethods.click_dialog_button(self, parent_css, "No")
        time.sleep(1)
          
        """ Step 13: Enter 'Page2_within_page' for the name and title
        """
        portal_misobj.select_page_template(page_template="2 Column", Page_title='Page2_within_page', Page_name='Page2_within_page', btn_name='Create')
        time.sleep(2)
        portal_properties.verify_breadcrumb_panel('Page2_within_page', ['Page2_within_page'], "Step 13: Verify that the new page takes over the original window.")
          
        """ Step 14: Click Insert tab
                     Click the Resource Tree
                     Verify that the tree is present.
        """
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        time.sleep(1)
        verify_panel_data('Panel 1', project_id, "14")
          
        """ Step 15: Exit and save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        time.sleep(3)
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 50)
        time.sleep(1)
          
        """ Step 16: Verify the pages are present in the folder
        """
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path, 'Page_within_page', msg='16')
        time.sleep(1)
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path, 'Page2_within_page', msg='16.1')
          
        """ Step 17: Edit 'page2_within_page'
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path + '->Page2_within_page', 'Edit')
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
        time.sleep(1)
          
        """ Step 18: Click BIP then Save As
        """
        portal_ribbon.select_tool_menu_item('menu_SaveAs')
          
        """ Step 19: Enter "testing save as bip955"
        """
        utillobj.ibfs_save_as("testing save as bip955")
        parent_css= "div[id^='dlgPortalSaveDialog']"
        resultobj.wait_for_property(parent_css, 1)
        utillity.UtillityMethods.click_dialog_button(self, parent_css, "OK")
        time.sleep(1)
          
        """ Step 20: Click on BIP icon --> Exit
                     Verify that all pages appear
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        time.sleep(3)
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 50)
        time.sleep(1)
          
        """ Step 21: Re edit the page
                     Verify there are not issues
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path + '->testing save as bip955', 'Edit')
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
        time.sleep(5)
        verify_panel_data('Panel 1', project_id, "14")
          
        """ Step 22: Exit designer
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        time.sleep(3)
        coreutillobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
         
        """ Step 23: Right click on 'testing save as bip955' and choose delete
                     Verify that page is not on the list
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path + '->testing save as bip955', 'Delete')
        delete_dialog_css = "[id*='BiDialog'] [class*='window-active']"
        resultobj.wait_for_property(delete_dialog_css, 1)
        utillity.UtillityMethods.click_dialog_button(self, delete_dialog_css, "Yes")
        time.sleep(1)
        wf_mainpageobj.expand_tree(BIP_Portal_Path)
        tree_rows="#bipTreePanel #treeView table>tbody>tr"
        actual_tree_text = [elem.text.strip() for elem in driver.find_elements_by_css_selector(tree_rows) if elem != '']
        utillobj.as_notin('testing save as bip955', actual_tree_text, "Step 23: Verify 'testing save as bip955' page is not on the list.")
        
        """ Step 24: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()