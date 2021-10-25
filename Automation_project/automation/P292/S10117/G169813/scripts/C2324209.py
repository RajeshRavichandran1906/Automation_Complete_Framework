'''
Created on Sep 10, 2017

@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import vfour_miscelaneous, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_properties, security_center, wf_legacymainpage
from common.lib import utillity
from common.lib import core_utility

class C2324209_TestClass(BaseTestCase):


    def test_C2324209(self):
        driver = self.driver #Driver reference object created
        """
            TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        Test_Case_ID = 'C2324209'
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_portal_canvasobj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        vfour_miscelaneousobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        vfour_portal_properties_obj = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        securityobj = security_center.Security_Center(self.driver)
        Portal_Name = 'BIP_xxx_Portal123_V4'
        Portal_Name1='BIP_xxx_Portal123_V4.prtl'
        proj_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        parent_folder_name='BIP_V4_Portal'
        BIP_Portal_Path = str(proj_id)+'->'+str(suite_id)+'->'+parent_folder_name
        Portal_Resource_Name ='BIP_xxx_Portal123_V4 Resources'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        
        
        """
            Step 01 : Sign in as WF Developer
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """
            Step 02: Expand P292 domain, Right click on 'S10117' folder and choose New > Collaborative Portal
            Step 03 : Enter the title as 'BIP_xxx_Portal123_V4' and click on Create button
            Step 03:01 : Verification Steps : Verify that both input boxes are being propagated with the name
        """
        wf_mainobj.create_portal(BIP_Portal_Path, Portal_Name)
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        
        """
            Step 03:02 : Verification Step : Verify that the Page Templates dialog showed.
            Step 04 : If the page templates are there click Cancel.
            Step 04:01 : Verify that the layout button is disabled since there is no page.
        """
        css="#dlgTitleExplorer"
        css1 = css + "[style*='inherit'] [class*='active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup(css, "Step 03:02 : Verify that the Page Templates dialog showed.", caption_css=css1, caption_text='Add Page')
        page_tempcss=css+" div[class*='tile_exp_header']"
        utillobj.verify_popup(css, "Step 04:Add Page dialog window shown", popup_text_css=page_tempcss, popup_text='Page Templates')
        utillobj.click_dialog_button("#dlgTitleExplorer", "Cancel")
        time.sleep(3)
        vfour_ribbonobj.verify_ribbon_item_property('Layout', 'Layout', 'Step 04:01:Verify that the layout button is disabled since there is no page.', item_property='disabled', property_value=True)
        
        """
            Step 05: Click the Theme Button and verify the Neutral theme is set as default
            Step 05:01:Verification: Verify the Neutral theme is set as default
        """
        vfour_ribbonobj.select_or_verify_layout_base_theme(button_click='Cancel', default_theme_name='Neutral', msg='Step05:01:Verify the Neutral theme is set as default' )
        """
            Step 06 : Press F8 and invoke resource tree
            Step 06:01 : Verify the WebFOCUS Resource Tree appears on the right of the screen.
           
        """
        vfour_ribbonobj.invoke_and_verify_wf_resource_tree(launch_point='keybord')
         
        """
            Step 07 : Press F5 to refresh the portal
            Step 07 :01 : Verification : Verify that pressing F5 refreshes the portal designer
        """
        resource_tree_css="#ResourcesPanelID #bipResourcesPanel"
        resource_tree_css_obj=self.driver.find_element_by_css_selector(resource_tree_css)
        vfour_ribbonobj.refresh_portal_page([resource_tree_css_obj], launch_point='keyboard')
        
        """
            Step 08 : Add the portal list container from the insert tab to the page canvas
            Step 08:01 : Verify that the content in this section are disabled.Image.
            Step 08:02 : Verify that the content Resource Tree is disabled
            Step 08:03 : Verify that the content -Portal list is disabled.
            Step 08:04 : Verify that the content-Text is disabled in this section.
        """
        vfour_ribbonobj.select_tab("Insert")
        time.sleep(4)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'Image', 'Step 08:01:Verify that the content in this section are disabled.Image', item_property='disabled', property_value=True)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'ResourceTree', 'Step 08:02:Verify that the content in this section are disabled.Resource Tree', item_property='disabled', property_value=True)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'PortalList', 'Step 08:03:Verify that the content in this section are disabled.Resource Tree', item_property='disabled', property_value=True)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'Text', 'Step 08:04:Verify that the content in this section are disabled.Resource Tree', item_property='disabled', property_value=True)
        """
            Step 09: Click on the banner
            Verification : Verify that all the things in the insert tab are now enabled
            Step 09:01 : Verify that the Image content is enabled 
            Step 09:02 : Verify that the content Resource Tree is enabled
            Step 09:03 : Verify that the content -Portal list is enabled
            Step 09:04 : Verify that the content-Text is enabled
        """
        vfour_ribbonobj.select_or_verify_top_banner(select=True)
        time.sleep(5)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'Image', 'Step 08:01:Verify that the content in this section are enabled.Image', item_property='disabled', property_value=False)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'ResourceTree', 'Step 08:02:Verify that the content in this section are enabled.Resource Tree', item_property='disabled', property_value=False)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'PortalList', 'Step 08:03:Verify that the content in this section are enabled.Resource Tree', item_property='disabled', property_value=False)
        vfour_ribbonobj.verify_ribbon_item_property('Insert', 'Text', 'Step 08:04:Verify that the content in this section are enabled.Resource Tree', item_property='disabled', property_value=False)
        """
            Step 10: Add a page then choose one column layout
        """
        vfour_portal_canvasobj.add_page('1 Column')
        
        """
            Step 11: Add the portal list container from the insert tab to the page canvas
        """
        vfour_ribbonobj.select_ribbon_item('Insert','Insert_PortalList')
        time.sleep(3)
        vfour_portal_canvasobj.verify_panel_portal_list('Panel 1', Portal_Name, "Step 11 :01 : Portal list is added in panel 1")
        
        """
            Step 12 : Save the portal
        """
        vfour_ribbonobj.select_tool_menu_item('menu_Save')
        
        """
            Step 13 : Press F5 to refresh the portal
        """
        resource_tree_css="#ResourcesPanelID #bipResourcesPanel"
        resource_tree_css_obj=self.driver.find_element_by_css_selector(resource_tree_css)
        vfour_ribbonobj.refresh_portal_page([resource_tree_css_obj], launch_point='keyboard')
        vfour_portal_canvasobj.verify_panel_portal_list('Panel 1', Portal_Name, "Step 13 :01 : Portal list is added in panel 1")
        
        """
            Verification : Step 13:01 :Verify refresh Portal Designer with F5 after saving does not goes to Run Mode
        """
        current_url = driver.current_url
        portal_url = "/portal/PortalDesigner?path=%252F"+proj_id+"%252F"+suite_id+"%252FBIP_V4_Portal%252FBIP_xxx_Portal123_V4"
        utillobj.asin(portal_url, current_url, "Step 13:01 :Verify refresh Portal Designer with F5 after saving does not goes to Run Mode")
        
        """
            Step 14 : Remove the page added
        """
        vfour_portal_canvasobj.manage_page_menu('1 Column', 'Remove')
        
        """
            Step 15 : Open the Domains from the tree
            Right click on Domains node and change the View to Display By Name
            Open the folder
            Verification :
            Step 15:01 :Verify that the portal is now listed as 'BIP_xxx_Portal123_V4.prtl'
        """
        vfour_miscelaneousobj.select_resource_menu(workspace, 'View->Display By Name')
        time.sleep(1)
        vfour_miscelaneousobj.verify_resource_item('{0}->{1}'.format(BIP_Portal_Path, Portal_Name1), Portal_Name1, '15:01', item_exit=True)
        vfour_miscelaneousobj.select_resource_menu(workspace, 'View->Display By Title') 
         
        """
            Step 16 : Use the scroll bar on the tree to go all the way to the right.
            Verify the white spaces.
        """
        parent_elem="#ResourcesPanelID #bipResourcesPanel"
        obj1=self.driver.find_element_by_css_selector(parent_elem)
        utillobj.click_on_screen(obj1, coordinate_type='bottom_middle', click_type=0, pause=2, x_offset=10, y_offset=-5)
        utillobj.click_on_screen(obj1, coordinate_type='bottom_middle', click_type=0, pause=2, x_offset=10, y_offset=-5)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 17 : Press F8 
            Verification :
            Step 17:01 : Verify that Resource Tree does not display.
        """
        vfour_ribbonobj.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=False)
        
        """
            Step 18 : Press F8 to bring back the resource tree.
            Verification:
            Step 19 : Verify that a resource folder was also created.
        """
        vfour_ribbonobj.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        vfour_miscelaneousobj.verify_resource_item('{0}->{1}'.format(BIP_Portal_Path, Portal_Resource_Name),Portal_Resource_Name, '19:', item_exit=True)
        
        """
            Step 20 : Publish the portal by checking the Publish check box located in the properties panel (Bottom of the portal).
        """
        vfour_portal_properties_obj.edit_input_control('page', 'Published', 'checkbox', checkbox_input='check', msg='Step 20')
        
        """
            Step 21 : Click on the Security Icon for the portal in Layout tab.
            Close the security window
            Verification : 
            Step 21:01 :Verify that security window opens and no errors. 
        """
        vfour_ribbonobj.select_ribbon_item('Layout','Layout_Security')
        parent_css="#dlgSecurityResource"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        css1 = parent_css+"[style*='inherit'] [class*='active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup(parent_css, "Step 21:02 : Verify that the Security dialog displayed.", popup_text_css=css1, popup_text='Security Rules - BIP_xxx_Portal123_V4')
        securityobj.select_security_rules_dialog_buttons('Cancel')
        time.sleep(5)
        
        """
            Step 22 : Click the BIP Icon and choose Exit.
            Click yes on the saving popup
            Verification : 
            Step 22:01 : Verify that you are back on the home portal and the portal was created and published
        """
        vfour_ribbonobj.bip_save_and_exit('Yes')
        core_utillobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        time.sleep(1)
        
        """
            Step 23 : Right click on the 'BIP_xxx_Portal123_V4' Resources folder and choose Properties.
            Verification :
            Step 23: 01: Verify that the name and title of the folder
            Step 23: 02: BIP_xxx_Portal123_V4 Resources --> title
            Step 23:03: BIP_xxx_Portal123_V4_Resources --> name
        """
        wf_mainobj.select_repository_menu(BIP_Portal_Path+'->'+Portal_Resource_Name, 'Properties')
        x=['Title', 'Step 23: title value as same as portal name', 'BIP_xxx_Portal123_V4 Resources']
        y=['Folder Name', 'Step 23:Folder name value is as same as portal name', 'BIP_xxx_Portal123_V4_Resources']
        for obj in (x,y):
            wf_mainobj.verify_properties_dialog('textbox', obj[0], obj[1], value=obj[2])
        
        """
            Step 24: Sign Out from WebFOCUS
        
        """
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
    
