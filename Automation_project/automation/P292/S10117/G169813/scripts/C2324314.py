'''
Created on 11-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324314
TestCase Name = Portal Designer_Design Content : Create_Portal_within_portal
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2324314_TestClass(BaseTestCase):

    def test_C2324314(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+'->'+suite_id
        BIP_Portal_Path = folder_path+'->BIP_V4_Portal'
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
         
        """ Step 2: Open P292 -> S10117 from domains tree,
                    Right Click on 'testing change title' portal and choose Edit
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->testing change title', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utilobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep)
         
        """ Step 3: Click the BIP icon and choose New Portal
                    Verify that the New portal title/name dialog appears
        """
        portal_ribbon.select_tool_menu_item('menu_NewPortal')
         
        """ Step 4: Enter 'Portal_within' as title then click on Create button
                    Verify that the new portal takes over the original window
        """
        wf_mainpageobj.set_field_new_portal_dialog('Portal_within')
        wf_mainpageobj.close_new_portal_dialog()
        panel_css="#BreadCrumbPanelID > [id^='Bi'][id*='MenuButton']"
        utillobj.synchronize_with_visble_text(panel_css, 'Portal_within', resultobj.home_page_long_timesleep)
        elems=self.driver.find_elements_by_css_selector(panel_css) 
        elem_list=[el.text.strip() for el in elems]
        utillobj.asin('Portal_within', elem_list, "Step 04.00: Verify that the new portal takes over the original window.")
         
        """ Step 5: Add page 1 with any layout
                    Add any content
        """
        portal_misobj.select_page_template(page_template="2 Column", Page_title='Page 1', btn_name='Create')
        time.sleep(2)
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 1)
        time.sleep(5)
        portal_canvas.verify_column_panel_caption(1, 'Category Sales', "Step 05.00: Verify Category Sales panel title")        
         
        """ Step 6: Exit and save
                    Verify that Portal_within is there
        """
        portal_ribbon.bip_save_and_exit('Yes')
        time.sleep(1)
        core_utilobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
         
        """ Step 7: Run that portal
                    Verify that all are present
        """
        driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->Portal_within', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep)
        portal_canvas.verify_column_panel_caption(1, 'Category Sales', "Step 07.00: Verify Category Sales panel title")        
         
        """ Step 8: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
         
        """ Step 9: Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        
        """ Step 10: Edit the 'Portal_within'
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->Portal_within', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utilobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep)
         
        """ Step 11: Click the BIP icon and choose New Portal
        """
        portal_ribbon.select_tool_menu_item('menu_NewPortal')
         
        """ Step 12: Enter 'Portal_within'
                     Verify that you can get an error message
        """
        time.sleep(2)
        wf_mainpageobj.set_field_new_portal_dialog('Portal_within')
        wf_mainpageobj.close_new_portal_dialog()
        time.sleep(1)
        css = "div[id='dlgNewPortalDesigner'] [class*='window'][class*='active']"
        cap_css = css + " [class*='caption']"
        cap_txt = 'New Collaborative Portal'
        pop_css = css + " [id*='BiDockPanel'] [id*='BiHBo'][style*='visibility']"
        pop_txt='Portal with this name already exists.\nPlease specify a unique name.'
        utillobj.verify_popup(css,'Step 12.00: Verify that you can get an error message.',caption_css=cap_css,caption_text=cap_txt,popup_text_css=pop_css,popup_text=pop_txt)
         
        """ Step 13: Click Cancel
        """
        wf_mainpageobj.close_new_portal_dialog(option='Cancel')
        time.sleep(2)
         
        """ Step 14: Add another content into an page
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 2)
        time.sleep(5)
        portal_canvas.verify_column_panel_caption(2, 'Regional Sales Trend', "Step 14.00: Verify Regional Sales Trend panel title")        
        time.sleep(2)
         
        """ Step 15: Click the BIP icon and choose New Portal
                     Verify that you are asked to save
        """
        portal_ribbon.select_tool_menu_item('menu_NewPortal')
        time.sleep(1)
        css="#dlgSavepromptPortal [class*='active'][class*='window']"
        cap_css = css + " [class*='caption']"
        cap_txt = 'Portal Designer'
        pop_css = css + " [id*='BiComponent'][class*='content']"
        pop_txt="Do you want to save the changes you made to\n'Portal_within'?\nYes\nNo\nCancel"
        utillobj.verify_popup(css,'Step 15.00: Verify that you can get an error message.',caption_css=cap_css,caption_text=cap_txt,popup_text_css=pop_css,popup_text=pop_txt)
         
        """ Step 16: Click Yes
        """
        click_yes = driver.find_element_by_css_selector(css + " #yesDialogbtnAction")
        utillobj.click_on_screen(click_yes, 'middle', click_type=0)
        time.sleep(2)
        utillobj.click_dialog_button('#dlgPortalSaveDialog', 'OK')
         
        """ Step 17: Enter 'Portal_within'
                     Verify that you can get an error message
        """
        wf_mainpageobj.set_field_new_portal_dialog('Portal_within')
        wf_mainpageobj.close_new_portal_dialog()
        time.sleep(1)
        css = "div[id='dlgNewPortalDesigner'] [class*='window-active']"
        cap_css = css + " [class*='caption']"
        cap_txt = 'New Collaborative Portal'
        pop_css = css + " [id*='BiDockPanel'] [id*='BiHBo'][style*='visibility']"
        pop_txt='Portal with this name already exists.\nPlease specify a unique name.'
        utillobj.verify_popup(css,'Step 17.00: Verify that you can get an error message.',caption_css=cap_css,caption_text=cap_txt,popup_text_css=pop_css,popup_text=pop_txt)
         
        """ Step 18: Add any naming convention as Portal_within_1 then click Create
        """
        wf_mainpageobj.set_field_new_portal_dialog('Portal_within_1')
        wf_mainpageobj.close_new_portal_dialog()
        panel_css="#BreadCrumbPanelID > [id^='Bi'][id*='MenuButton']"
        utillobj.synchronize_with_visble_text(panel_css, 'Portal_within_1', resultobj.home_page_long_timesleep)
        portal_misobj.select_page_template(page_template="2 Column", Page_title='Page 1', btn_name='Create')
        time.sleep(2)
         
        """ Step 19: BIP icon and exit
                     Verify that the Portal_within_1 is there on the list
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        time.sleep(1)
        try:
            pop_css = "div[id='dlgSavepromptPortal'] [class*='window-active'] #yesDialogbtnAction"
            utillobj.synchronize_until_element_is_visible(pop_css, 19)
            click_yes = utillobj.validate_and_get_webdriver_object(pop_css, 'save popup') 
            utillobj.click_on_screen(click_yes, 'middle', click_type=0)
            time.sleep(2)
            utillobj.click_dialog_button('#dlgPortalSaveDialog', 'OK')
        except:
            pass
        core_utilobj.switch_to_previous_window(window_close=False)
        time.sleep(1)
        driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path+'->BIP_xxx_Portal123_V4','Portal_within_1', msg='18.00')
         
        """ Step 20: Right Click on the new portal and choose Publish menu
                     Verify now the portal is published
        """
        wf_mainpageobj.verify_folder_status(BIP_Portal_Path+'->Portal_within_1', status='unpublished', msg='20.00')
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->Portal_within_1','Publish')
        time.sleep(4)
        wf_mainpageobj.verify_folder_status(BIP_Portal_Path+'->Portal_within_1', status='published', msg='20.01')
        
        """ Step 21: Sign Out from WebFOCUS
        """
        time.sleep(5)
                

if __name__ == '__main__':
    unittest.main()