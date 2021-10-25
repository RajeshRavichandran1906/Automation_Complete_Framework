'''
Created on June 28, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6390408
TestCase Name = API > BIP > Launch IA 
'''

import unittest, time
from common.pages import visualization_resultarea, wf_legacymainpage, vfour_miscelaneous, vfour_portal_ribbon, vfour_portal_canvas
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase

class C6390408_TestClass(BaseTestCase):

    def test_C6390408(self):
        
        Test_Case_ID = "C6390408"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        legacymainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfourmiscelaneousobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        vfourribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portalcanvasobj = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        
        """
        Step 01: Launch WebFOCUS using API,
        http://machine:port/{alias}/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        domain = "#bipTreePanel #treeView"
        utillobj.synchronize_with_number_of_element(domain,1,290)
          
        """
        Step 02: Right-click Domain folder (ex:P292_S10032_"P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)" > S10032_infoassist_5 folder) > New > URL
        """
        legacymainobj.select_repository_menu('P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->S10660_infoassist_2', 'New->URL')
        time.sleep(6)
           
        """
        Step 03: Type Title: Launch IA API from Portal
        Step 04: Type URL (with test environment) using API: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/S10032 > OK
        """
        parent_css="#createURLDialog"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
           
        title="Launch IA API from Portal"
        title_css = driver.find_element_by_css_selector("#createURLDialog input[id*='urlnewdesc']")
        utillobj.set_text_field_using_actionchains(title_css, title, keyboard_type=True)
           
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        project = utillobj.parseinitfile('project_id')
        suiteid = utillobj.parseinitfile('suite_id')
        folder = project + '/' + suiteid
        url = 'http://' + node + ':' + port + context + '/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/' + folder
        url_css = driver.find_element_by_css_selector("#createURLDialog input[id*='newurl']")
        utillobj.set_text_field_using_actionchains(url_css, url, keyboard_type=True)
        time.sleep(3)
        ok_btn=driver.find_element_by_css_selector("#createURLDialog div[id*='btnOK']")
        core_utilobj.python_move_to_element(ok_btn)
        ok_btn=driver.find_element_by_css_selector("#createURLDialog div[id*='btnOK']")
        core_utilobj.python_left_click(ok_btn)
        time.sleep(5)
        
        """
        Step 05: Create New > Collaborative Portal
        Step 06: Type Title: C2241561
        """
        legacymainobj.select_repository_menu('P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->S10660_infoassist_2', 'New->Collaborative Portal')
        time.sleep(6)
        elems=driver.find_elements_by_css_selector("div[id='dlgNewPortalDesigner'][style*='left'] input")
        utillobj.set_text_field_using_actionchains(elems[0], Test_Case_ID)
        utillobj.click_dialog_button("div[id='dlgNewPortalDesigner'][style*='left']", "Create")
        time.sleep(5)
        core_utilobj.switch_to_new_window()
        time.sleep(5)
        
        """Verify that Add Page dialog opens"""
        utillobj.verify_object_visible("#dlgTitleExplorer div[class^='bi-window active window window-active']", True, "Step 06: Verify that Add Page dialog opens")
        
        """
        Step 07: Select 'One Column' > Create 
        """
        vfourmiscelaneousobj.select_page_template(page_template="1 Column", btn_name="Create")
        time.sleep(5)
        
        """
        Step 08: Select Insert > WebFOCUS Resources
        """
        vfourribbonobj.select_ribbon_item('Insert', 'Insert_WebFOCUSResources')
        time.sleep(5)
        
        """Verify that WebFOCUS Resources added,"""
        
        utillobj.verify_object_visible("#BIPortalPanel #ResourcesPanelID", True, "Step 08: Verify that WebFOCUS Resources added")
        
        """
        Step 09: Expand the folder ""P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)" > S10660_infoassist_2 folder" > Drag "Launch IA API from Portal" into Portal
        """
        portalcanvasobj.dragdrop_repository_item_to_canvas('P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->S10660_infoassist_2->Launch IA API from Portal', 'column', 1)
        time.sleep(15)
        
        """Verify the Portal,"""
        portalcanvasobj.verify_panel_caption('Launch IA API from Portal','Step 09.1: Verify panel title')
        portalcanvasobj.verify_page_in_navigation_bar('1 Column', "Step 09.2: Verify 1 Column in Navigation Bar.")
        time.sleep(5)
        
        """
        Step 10: Select BIP > Exit > Yes to save prompt > OK
        """
        vfourribbonobj.select_tool_menu_item('menu_Exit')
        time.sleep(5)
        utillobj.verify_object_visible('#dlgSavepromptPortal', True, "Step 10: Verify save prompt appears")
        yes_btn=driver.find_element_by_css_selector("#dlgSavepromptPortal div[id*='yesDialogbtnAction']")
        core_utilobj.python_move_to_element(yes_btn)
        yes_btn=driver.find_element_by_css_selector("#dlgSavepromptPortal div[id*='yesDialogbtnAction']")
        core_utilobj.python_left_click(yes_btn)
        time.sleep(3)
        dialog_css="div[id='dlgPortalSaveDialog'][style*='left']"
        resultobj.wait_for_property(dialog_css, 1)
        ok_btn=driver.find_element_by_css_selector("#dlgPortalSaveDialog div[class*='bi-button button button-focus']")
        core_utilobj.python_move_to_element(ok_btn)
        ok_btn=driver.find_element_by_css_selector("#dlgPortalSaveDialog div[class*='bi-button button button-focus']")
        core_utilobj.python_left_click(ok_btn)

        time.sleep(3)
        core_utilobj.switch_to_previous_window(window_close=False)
        time.sleep(5)
        parent_css = "#topBannerMenuBox [id^='BiWelcomeBannerMenuButton']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        
        """
        Step 11: Right click on saved portal "C2241561" > Run
        """
        legacymainobj.select_repository_menu('P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->S10660_infoassist_2->C6390408', 'Run')
        time.sleep(6)
        
        """Verify IA is launched,"""
        parent_css="#BIPortalPanel"
        resultobj.wait_for_property(parent_css, 1)
        portalcanvasobj.verify_panel_caption('Launch IA API from Portal','Step 11.1: Verify panel title')
        portalcanvasobj.verify_page_in_navigation_bar('1 Column', "Step 11.2: Verify 1 Column in Navigation Bar.")
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#BIPortalPanel")
        utillobj.take_screenshot(ele,'C6390408_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        """
        Step 12: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()