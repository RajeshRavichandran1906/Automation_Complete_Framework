'''
Created on Sep 22, 2017

@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage, wf_legacymainpage, vfour_miscelaneous, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run
from common.lib import utillity

class C2324239_TestClass(BaseTestCase):
    
    def test_C2324239(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the testpass
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324239'
        utill_obj = utillity.UtillityMethods(self.driver)
        if utill_obj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_main_obj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_main_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_ribbon_obj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_portal_canvas_obj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        vfour_miscelaneous_obj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        vfour_portal_run_obj=vfour_portal_run.Vfour_Portal_Run(self.driver)
        proj_id = utill_obj.parseinitfile('project_id')
        suite_id = utill_obj.parseinitfile('suite_id')
        user_id = utill_obj.parseinitfile('mrid03')
        browser=utill_obj.parseinitfile('browser')
        parent_folder_name='BIP_V4_Portal'
        BIP_Portal_Path = str(proj_id)+'->'+str(suite_id)+'->'+parent_folder_name
        Portal_Name = 'BIP_xxx_Portal123_V4'
        Page_Name = 'Test_Page'
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        run_page_parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        
        """ Step 1: Sign in as WF Developer
        """
        utill_obj.invoke_webfocu('mrid03', 'mrpass03')
        utill_obj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        
        """ Step 2: Right click on 'BIP_xxx_Portal123_V4' portal
                    Verify the right click menu options.
        """
        menu_list = ['Run', 'RuninNewWindow', 'Edit', 'Customizations', 'CutCtrl+X', 'CopyCtrl+C', 'DeleteDEL', 'ChangeTitleF2', 'AddToFavorites', 'AddToMobileFavorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        wf_main_obj.select_menu(BIP_Portal_Path+'->'+Portal_Name,  item_exit=True, expected_menu_list=menu_list, msg="Step 2: Verify the right click menu options.")
        wf_main_obj.select_menu(str(proj_id), 'Refresh')
        
        """ Step 3: Choose Edit menu option
        """
        utill_obj.synchronize_with_visble_text(welcome_page_parent_css, str(suite_id), 50)
        wf_main_obj.select_menu(BIP_Portal_Path+'->'+Portal_Name, 'Edit')
        time.sleep(5)
        utill_obj.switch_to_window(1)
        utill_obj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
        
        """
            Step 4 : Click on theme button and change it to the Neutral theme
        """
        vfour_ribbon_obj.select_or_verify_layout_base_theme(button_click='OK', theme_name='Neutral', msg='Step 4:Click on theme button and change it to the Neutral theme' )
        vfour_ribbon_obj.select_or_verify_top_banner(select=True, bg_color='Zambezi_grey', msg="Step 4.1: Verify the portal canvas color has changed to the default theme as Neutral.")
        
        """
            Step 5: Add a new page by clicking on the new page icon in the page tab;
                    Choose 4 Columns;
            Step 6: Enter Test_Page as page title
                    Click Create
                    Verify that the Test_Page is also in the Name: entry box.
                    Verify that Test_Page is created.
        """
        vfour_portal_canvas_obj.add_page('4 Column', Page_title='Test_Page')
        time.sleep(2)
        vfour_portal_canvas_obj.verify_page_in_navigation_bar(Page_Name, "Step 6:Verify that the Test_Page is also in the Name: entry box", verify=True)
         
        """
           Step 7: Select Column1 area in canvas and Add a simple panel from insert tab; Insert a Resource tree into the panel by clicking the Resource tree icon in the content
        """
        vfour_portal_canvas_obj.select_column(1)
        vfour_portal_canvas_obj.verify_column_selected(1, 'top', 'Step 07: verify column area is selected')
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_Panel')
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_ResourceTree')
        vfour_portal_canvas_obj.verify_panel_caption('Panel 1', "Step 7.1:Verify Panel1 is displayed")
        vfour_miscelaneous_obj.verify_resource_item('Domains', 'P292', "Step 7.2:", item_exit=True, tree_rows="div[class*='bip-page'][style*='inherit'] div[id^='BipContentArea'] div[class*='bi-tree-view-body-content'] td")
        
        """
            Step 8 : Select Column2 area in canvas and insert portal tree into the panel by clicking the portal list icon in the Content area on top
        """
        vfour_portal_canvas_obj.select_column(2)
        vfour_portal_canvas_obj.verify_column_selected(2, 'top', 'Step 8: verify column area is selected')
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_Panel')
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_PortalList')
        vfour_portal_canvas_obj.verify_panel_caption('Panel 2', "Step 8.1 :Verify Panel2 is displayed")
        vfour_portal_canvas_obj.verify_panel_portal_list('Panel 2', Portal_Name, "Step 8.2 : Portal list is added in panel 2")
        
        """
            Step 9 : Select Column3 area in canvas and Add a simple panel; insert Text area from insert tab into the panel; 
        """
        vfour_portal_canvas_obj.select_column(3)
        vfour_portal_canvas_obj.verify_column_selected(3, 'top', 'Step 9: verify column area is selected')
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_Panel')
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_Text')
        vfour_portal_canvas_obj.verify_panel_caption('Panel 3', "Step 9.1 :Verify Panel2 is displayed")
        
        """
            Step 10 : Enter "testing text panel area" inside the text panel
        """
        vfour_portal_canvas_obj.select_panel('Panel 3')
        panel3_textarea_obj=driver.find_element_by_css_selector("div[id^='BipContentArea'] [class*='bip-panel-pane pd-internal']")
        utill_obj.click_on_screen(panel3_textarea_obj, 'middle', click_type=0)
        time.sleep(1)
        text_area_msg="testing text panel area"
        vfour_portal_canvas_obj.add_text_into_panel('Panel 3', text_area_msg)
        vfour_portal_canvas_obj.verify_panel_text('Panel 3', text_area_msg, "Step 10: The added text message is available in the added panel 3")
        
        """
            Step 11 : Select Column4 area in canvas and Add an image by clicking on Image from Ribbon;
            navigate to an image and add babydeer
        """
        vfour_portal_canvas_obj.select_column(4)
        vfour_portal_canvas_obj.verify_column_selected(4, 'top', 'Step 11: Select Column4 area in canvas and Add an image by clicking on Image from Ribbon')
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_Panel')
        time.sleep(1)
        vfour_ribbon_obj.select_ribbon_item('Insert','Insert_Image')
        vfour_miscelaneous_obj.insert_image_or_file_from_bip_canvas(BIP_Portal_Path+'->'+'babydeer', 'JPEG (*.jpg;*.jpeg;*.jpe)')
        portal_canvas_obj=driver.find_element_by_css_selector("div[class*='bi-component bip-canvas pd']")
        utill_obj.take_screenshot(portal_canvas_obj,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 12: Click the BIP icon then exit.
            Click Yes to save
        """
        vfour_ribbon_obj.bip_save_and_exit('Yes')
        utill_obj.switch_to_window(0, pause=9)
        utill_obj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        time.sleep(1)
        
        """
            Step 13 : Run the portal by double clicking
                      Verify the changes
        """
        wf_main_obj.select_repository_menu(BIP_Portal_Path+'->'+Portal_Name, 'Run')
        utill_obj.synchronize_with_number_of_element(run_page_parent_css, 1, 50)
        
        """ Verification""" 
        vfour_portal_canvas_obj.verify_page_in_navigation_bar(Page_Name, "Step 13: Verify the created page Page_New is available.", verify=True)
        vfour_portal_run_obj.verify_number_of_portal_panel(4, "Step 13.1: Verify the created panels in the created portal at runtime")
        vfour_portal_run_obj.verify_portal_panel_label(['Panel 1','Panel 2','Panel 3','Panel 4'], "Step 13.2 : Verify Panel Labels")
        if browser=='IE':
            vfour_portal_run_obj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Enable Accessibility', 'Hidden Content'], msg='Step 13.3 : Verify portal banner menu bar')    
        else:
            vfour_portal_run_obj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Hidden Content'], msg='Step 13.3 : Verify portal banner menu bar')
         
        """
            Verify Panel1 contents
        """
        vfour_portal_canvas_obj.verify_panel_caption('Panel 1', "Step 13.4 :Verify Panel1 is displayed")
        utill_obj.verify_object_visible("#treeView tbody>tr>td>img[src*='discovery_domain']", True, 'Step 13.5 : Domain tree Visible')
        
        """
            Verify : Panel2 contents
        """
        
        vfour_portal_canvas_obj.verify_panel_caption('Panel 2', "Step 13.6 : Verify Panel2 is displayed")
        vfour_portal_canvas_obj.verify_panel_portal_list('Panel 2', Portal_Name, "Step 13.7 : Portal list is added in panel 2")
        
        """
            Verify : Panel3 contents
        """
        
        text_area_msg="testing text panel area"
        vfour_portal_canvas_obj.verify_panel_text('Panel 3', text_area_msg, "Step 13.8 : The added text message is available in the added panel 3")
        
        """
            Verify Panel4 contents
        """
        vfour_portal_canvas_obj.verify_panel_image('Panel 4', 'babydeer', "Step 13.9 : Babydeer image is present in the added panel 4")

        """
            Step 13 : Close the portal run mode using close menu bar link
        """
        vfour_portal_run_obj.select_or_verify_portal_menu_bar_item(select='Close', msg='Step 13.10: Close the portal run mode by clicking on the Close Menubar link.')
        
        """
            Step 14 : Sign Out from WebFOCUS
        """
        time.sleep(3)
        

if __name__ == "__main__":
    unittest.main()