'''
Created on 26-Feb-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324333
TestCase Name = Portal Designer_Design Properties : Adding Comments
'''
import unittest, time, re
from common.lib import utillity
from common.pages import wf_mainpage, vfour_portal_canvas, wf_legacymainpage, ia_resultarea, vfour_portal_properties, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException

class C2324333_TestClass(BaseTestCase):

    def test_C2324333(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02', 'wfinst03', 'wfinst04','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = str(project_id)+'->'+str(suite_id)+'->BIP_V4_Portal'
        portal_name = 'Comments'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        
        def verify_panel_frame_data(panel_name, expected_value, step_num):
            portal_misobj.switch_to_frame_in_bip_page(frame_panel_name=panel_name)
            ia_resultobj.verify_number_of_chart_segment("jschart_HOLD_0", expected_value, "Step "+str(step_num)+": Verify number of risers displayed in '" + str(panel_name) + "'.")   
            utillobj.switch_to_default_content(pause=3)
        
        def select_show_comment_check_box_from_property_section():
            item_name='Show Comments'
            parent_css="[id^='idProperties']:not([style*='hidden'])"
            elem=portal_properties.get_vbox_object(parent_css, item_name)
            checkbox_elems=elem.find_elements_by_css_selector("div[id^='BiCheckBox']:not([style*='hidden'])")
            elem=checkbox_elems[[el.text.strip() for el in checkbox_elems].index(item_name)]
            try:
                elem.find_element_by_css_selector("input[checked]")
                current_status=True
            except NoSuchElementException:
                current_status=False
            if current_status == True:
                print(item_name.upper()+" is already checked.")
            else:
                utillobj.default_click(elem)
        
        def select_show_comment_from_panel_menu():
            panel_name='IA_Chart1'
            menu_css="table tr"
            menu_dialog_css="div[id^='BiPopup'][style*='inherit']"
            panel_elem = portal_canvas.get_panel_obj(panel_name)
            panel_title_obj = panel_elem.find_element_by_css_selector("[id^='BipTitleBarMenuButton'][class*='button']")
            portal_canvas.select_panel(panel_name)
            utillobj.default_click(panel_title_obj)
            portal_misobj.wait_for_property_in_bip_page(menu_dialog_css, 1)
            menu_dialog_obj=self.driver.find_elements_by_css_selector(menu_dialog_css)
            for menu in menu_dialog_obj:
                if menu.value_of_css_property('visibility') == 'visible':
                    menu_obj = menu
                    break
            menu_items=menu_obj.find_elements_by_css_selector(menu_css)
            menu_list_items = [el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
            if 'Show Comments' in menu_list_items:
                portal_canvas.manage_panel_title_menubar(panel_name, verify=False, select_menu_opt='Show Comments')
                portal_canvas.select_panel(panel_name)
            else:
                portal_canvas.select_panel(panel_name)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        
        """ Step 2: Expand P292 domain, right Click on S10117 folder and choose New-> Collaborative Portal
        """
        """ Step 3: Enter the title as 'Comments'
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        portal_misobj.verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
         
        """ Step 4: Click Create New page using One Column named Page 1 and add a regular panel
                    Verify Page 1 is created
        """
        portal_misobj.select_page_template(page_template="1 Column", Page_title='Page 1', btn_name='Create')
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 4: Verify 'Page 1' in Navigation bar.")
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
         
        """ Step 5: Click Page 1
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(1)
         
        """ Step 6: Look at the Comments drop down in the Properties bar on the bottom of the page
                    Verify it is None by default
        """
        portal_properties.verify_input_control('page', 'Comments', 'combobox', "Step 6: Verify that the Comments is displayed 'None'.", combobox_value='None')
         
        """ Step 7: Open the drop down
        """
        """ Step 8: Select Top
        """
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Top')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Top', "Step 8: Verify Comment Section is Displayed on Top of the page.")
        portal_canvas.verify_comments_section_text("Step 8.1: Verify Comment Section is Displayed.")
         
        """ Step 9: Adjust the size of the Comment panel
                    Verify the page adjusts for size of the Comment panel
        """
        ''' comment section bottom height location before resize'''
        comment_section_obj = portal_canvas.get_comments_section()
        portal_canvas.get_current_page()
        comment_section_bottom_height_before_resize = utillobj.get_object_screen_coordinate(comment_section_obj, coordinate_type='bottom_middle')
        ''' panel top height location before comment section resize'''
        panel_obj = portal_canvas.get_panel_obj('Panel 1')
        panel_top_height_before_resize = utillobj.get_object_screen_coordinate(panel_obj, coordinate_type='top_middle')
        portal_canvas.resize_comments_section('resize_down', "Step 9: Verify the page adjusts for size of the Comment panel", target_offset_y=45)
        time.sleep(2)
        ''' comment section bottom height location after resize'''
        comment_section_obj1 = portal_canvas.get_comments_section()
        comment_section_bottom__height_after_resize = utillobj.get_object_screen_coordinate(comment_section_obj1, coordinate_type='bottom_middle')
        ''' panel top height location after comment section resize'''
        panel_obj1 = portal_canvas.get_panel_obj('Panel 1')
        panel_top_height_after_resize = utillobj.get_object_screen_coordinate(panel_obj1, coordinate_type='top_middle')
        status_ = True if comment_section_bottom__height_after_resize['y'] > comment_section_bottom_height_before_resize['y'] and panel_top_height_after_resize['y'] > panel_top_height_before_resize['y'] else False
        utillobj.asequal(True, status_, "Step 9.1: Verify the page adjusts for size of the Comment panel")
         
        """ Step 10: Check for Bottom, Left, and Right
                     as of now BIP-973 Comment Options Are Cut Off. : where the icons all don't show in the comments section. as you make the comments window 
                     bigger they will show 
                     Bottom:
                     Left:
                     Right:
        """ 
        '''Bottom:'''
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Bottom')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Bottom', "Step 10: Verify Comment Section is Displayed on Bottom of the page.")
        '''Left:'''
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Left')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Left', "Step 10.1: Verify Comment Section is Displayed on Left of the page.")
        '''Right'''
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Right')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Right', "Step 10.2: Verify Comment Section is Displayed on Right of the page.")
         
        """ Step 11: With the Comment panel on the Right, press F8 to invoke the Resource Tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
         
        """ Step 12: Press F8 to close the Resource Tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=False)
         
        """ Step 13: Select Add Comment...
                     Add a comment and post
                     Verify that the user matches the name that is first in the Menu Bar
        """
        portal_canvas.add_comment_on_comment_section('This is a test for a Page', pause_time=2)
        time.sleep(2)
        portal_canvas.verify_comments_section_text("Step 8.1: Verify that the user matches the name that is first in the Menu Bar.", 'This is a test for a Page')
         
        """ Step 14: Change the Comments to be on the Top
                     Verify the comment you posted is still there
        """
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Top')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Top', "Step 14: Verify Comment Section is Displayed on Top of the page.")
        portal_canvas.verify_comments_section_text("Step 14.1: Verify that the user matches the name that is first in the Menu Bar.", 'This is a test for a Page')
         
        """ Step 15: Check for Bottom and Left
        """
        '''Bottom'''
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Bottom')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Bottom', "Step 15: Verify Comment Section is Displayed on Bottom of the page.")
        portal_canvas.verify_comments_section_text("Step 15.1: Verify that the user matches the name that is first in the Menu Bar.", 'This is a test for a Page')
        '''Left'''
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Left')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Left', "Step 15.2: Verify Comment Section is Displayed on Left of the page.")
        portal_canvas.verify_comments_section_text("Step 15.1: Verify that the user matches the name that is first in the Menu Bar.", 'This is a test for a Page')
         
        """ Step 16: Change the Comments to be None
                     Verify the Comment panel disappeared
        """
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='None')
        time.sleep(2)
        portal_canvas.verify_comment_section_displayed("Step 16: Verify the Comment panel disappeared", expected_display_status=False)
         
        """ Step 17: Change the Comments to be Top
                     Verify the Comment panel reappears with the comment you posted
        """
        portal_properties.edit_input_control('page', 'Comments', 'combobox', combobox_input='Top')
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Top', "Step 17: Verify Comment Section is Displayed on Top of the page.")
        portal_canvas.verify_comments_section_text("Step 17.1: Verify that the user matches the name that is first in the Menu Bar.", 'This is a test for a Page')
         
        """ Step 18: Save and exit
        """
        portal_ribbon.bip_save_and_exit('Yes')
        utillobj.switch_to_window(0, pause=9)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        time.sleep(1)
 
        """ Step 19: Run the portal
                     Verify the Comment panel still appears on the top with your comment
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 19: Verify 'Page 1' in Navigation bar.")
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Top', "Step 19.1: Verify Comment Section is Displayed on Top of the page.")
        portal_canvas.verify_comments_section_text("Step 19.2: Verify the Comment panel still appears on the top with your comment.", 'This is a test for a Page')
         
        """ Step 20: Click the Close link in the menu bar
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
         
        """ Step 21: Right click and publish the portal
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->'+portal_name, 'Publish')
         
        """ Step 22: Edit the comments portal.
                     Press F8 to invoke the resource tree and open P292->S10117.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Edit')
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 22: Verify 'Page 1' in Navigation bar.")
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Top', "Step 22.1: Verify Comment Section is Displayed on Top of the page.")
        portal_canvas.verify_comments_section_text("Step 22.2: Verify the Comment panel still appears on the top with your comment.", 'This is a test for a Page')
        portal_ribbon.invoke_and_verify_wf_resource_tree()
          
        """ Step 23: Drag IA_Chart1 into Panel 1
        """
        portal_canvas.dragdrop_repository_item_to_canvas(BIP_Portal_Path+'->IA_Chart1', 'panel', 'Panel 1')
        time.sleep(2)
        verify_panel_frame_data('Panel_1', 5, '23')
          
        """ Step 24: Click panel 1 and check the comments box in the properties section if not checked already.
                     If its checked then skip this test step.
        """
        portal_canvas.select_panel('IA_Chart1')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        select_show_comment_check_box_from_property_section()
          
        """ Step 25: Click on the down arrow on IA_Chart1's title bar to bring down the menu options
        """
        """ Step 26: Select Show Comments
                     Verify a Comment panel appears in the IA_Chart1 panel
        """
        select_show_comment_from_panel_menu()
        time.sleep(2)
        portal_canvas.verify_comment_section_location('Bottom', "Step 26: Verify Comment Section is Displayed on Bottom of the IA_Chart1 panel.", comment_section_exist_in='panel', panel_name='IA_Chart1')
        portal_canvas.verify_comments_section_text("Step 26.1: Verify a Comment panel appears in the IA_Chart1 panel.", comment_section_exist_in='panel', panel_name='IA_Chart1')
         
        """ Step 27: Add a comment This is a test for a panel
                     Verify that the comment is there
        """
        portal_canvas.add_comment_on_comment_section('This is a test for a Panel', pause_time=2, comment_section_exist_in='panel', panel_name='IA_Chart1')
        time.sleep(2)
        portal_canvas.verify_comments_section_text("Step 27: Verify a Comment appears in the IA_Chart1 panel.", 'This is a test for a Panel', comment_section_exist_in='panel', panel_name='IA_Chart1')
         
        """ Step 28: Save and exit
        """
        portal_ribbon.bip_save_and_exit('Yes')
        utillobj.switch_to_window(0, pause=9)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        time.sleep(1)
        
        """ Step 29: Run the portal
                     Verify all comments are there
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        utillobj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 29: Verify 'Page 1' in Navigation bar.")
        time.sleep(2)
        verify_panel_frame_data('Panel_1', 5, '29.1')
        portal_canvas.verify_comments_section_text("Step 29.2:  Verify a Comment appears in the page.", 'This is a test for a Page')
        portal_canvas.verify_comments_section_text("Step 29.3: Verify a Comment appears in the IA_Chart1 panel.", 'This is a test for a Panel', comment_section_exist_in='panel', panel_name='IA_Chart1')
        
        """ Step 30: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        
        """ Step 31: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()