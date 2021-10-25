'''
Created on 13-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324250
TestCase Name = Portal Designer_Design Content : Add Easy Selector
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run, wf_legacymainpage, vfour_portal_properties, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class C2324250_TestClass(BaseTestCase):

    def test_C2324250(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        BIP_Portal_Path = project_id+'->'+suite_id+'->BIP_V4_Portal'
        portal_name = 'Easy_Selector'
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep, string_value=workspace, with_regular_exprestion=True)
        
        """ Step 2: Expand P292 domain, right click on S10117 folder and choose New -> Collaborative Portal
        """
        """ Step 3: Enter 'Easy_Selector' and click Ok button
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, portal_name)
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
        utillobj.synchronize_with_number_of_element(parent_css, 1, resultobj.home_page_long_timesleep)
        portal_misobj.verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
          
        """ Step 4: Choose Page Layout and 2 Columns
        """
        portal_misobj.select_page_template(page_template="2 Column", Page_title='Page 1', Page_name='Page_1', btn_name='Create')
         
        """ Step 5: Maximize the portal
                    Check the Publish checkbox
        """
        portal_properties.select_breadcrumb_panel(portal_name)
        time.sleep(1)
        portal_properties.edit_input_control('pageview', 'Published', 'checkbox', checkbox_input='check', msg='Step 5: ')
        time.sleep(1)
         
        """ Step 6: Click on Column 1
                    Verify the properties section
        """
        portal_canvas.select_column(1)
        portal_properties.verify_input_control('column', 'Column 1', 'text', "Step 6: Verify Column 1 shown in properties section", text_list=['Column 1'])
        portal_properties.verify_input_control('column', 'Width', 'combobox', "Step 6.1: Verify width Auto shown in properties section", combobox_value='Auto')
        portal_properties.verify_input_control('column', 'Width unit', 'combobox', "Step 6.2: Verify width unit px shown in properties section", combobox_value='px')
        portal_properties.verify_input_control_enable_or_disable('column', 'Lock Width', 'checkbox', 'Step 6.3: Verify Lock Width is uncheck and disabled.',
                                                                 enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('column', 'Same for All', 'checkbox', "Step 6.4: Verify Same for All is checked in properties section", checkbox_input='uncheck')
        portal_properties.verify_input_control('column', 'Top', 'textbox', "Step 6.5: Verify Top value is 10 in properties section", textbox_value='10')
        portal_properties.verify_input_control('column', 'Bottom', 'textbox', "Step 6.6: Verify Bottom value is 10 in properties section", textbox_value='10')
        portal_properties.verify_input_control('column', 'Left', 'textbox', "Step 6.7: Verify Left value is 10 in properties section", textbox_value='10')
        portal_properties.verify_input_control('column', 'Right', 'textbox', "Step 6.8: Verify Right value is 5 in properties section", textbox_value='5')
        portal_properties.verify_input_control_enable_or_disable('column', 'Freeze Column', 'checkbox', 'Step 6.9: Verify Freeze Column is uncheck and disabled.',
                                                                 enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('column', 'Show Easy Selector', 'checkbox', "Step 6.10: Verify Show Easy Selector is uncheck in properties section", checkbox_input='uncheck')
        portal_properties.verify_input_control('column', 'Select Folder', 'button', "Step 6.11: Verify Select Folder  button in properties section", elem_visible=True)
         
        """ Step 7: Check the Easy Selector box
                    Verify an explorer window will pop up
        """
        portal_properties.edit_input_control('column', 'Show Easy Selector', 'checkbox', checkbox_input='check', msg='Step 7: ')
        parent_css = "#dlgIbfsBrowseForFile [class*='active'] [class*='window-caption']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep)
        time.sleep(1)
        actual_elem = driver.find_element_by_css_selector(parent_css).text.strip().replace(' ','')
        utillobj.asequal(actual_elem, 'BrowseForFolder', 'Step 7.1: Verify an explorer window will pop up.')
         
        """ Step 8: Click cancel w/o choosing a folder
        """
        close_popup = driver.find_element_by_css_selector("#dlgIbfsBrowseForFile [class*='active'] #IbfsBrowseForFolderDlg_btnCancel")
        utillobj.click_on_screen(close_popup, 'middle', click_type=0)
         
        """ Step 9: Click on Exit --> Save --> Run the portal
        """
        portal_ribbon.bip_save_and_exit('Yes')
        time.sleep(1)
        core_utilobj.switch_to_previous_window(window_close=False)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep)
         
        """ Step 10: Verify that no + sign appears as no folder was selected
        """
        status_=False
        try:
            driver.find_element_by_css_selector("[id*='EasyInsertMarker'] [class*='bip'][class*='easy'][class*='selector'][class*='image']")
            status_=False
        except NoSuchElementException:
            status_=True
        utillobj.asequal(status_, True, "Step 10: Verify that no + sign appears as no folder was selected")
         
        """ Step 11: Close and Navigate URL to http://environment_name:port/alias/legacyhome
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep, string_value=workspace, with_regular_exprestion=True)
        time.sleep(5)
        
        """ Step 12: Edit 'Easy_Selector' portal
                     Check the easy selector box
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utilobj.switch_to_new_window()
        time.sleep(2)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep)
        
        """ Step 13: Choose Retail Samples--> Portal--> Small Widgets folder
        """
        portal_canvas.select_column(1)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', launch_point='property_tab', button='OK', 
                                                section='column', item_name='Show Easy Selector', control='checkbox', checkbox_input='check', msg='Step 13:')
        
        """ Step 14: Click Column2 and check the easy selector box and choose Retail Samples--> Portal--> Small Widgets folder
                     Verify that the folder was already highlighted
        """
        portal_canvas.select_column(2)
        time.sleep(1)
        portal_properties.edit_input_control('column', 'Show Easy Selector', 'checkbox', checkbox_input='check', msg='Step 14: ')
        popup_elem=driver.find_element_by_css_selector("#dlgIbfsBrowseForFile [class*='active'] table>tbody>tr[class*='selected']").text.strip().replace(' ','')
        utillobj.asequal('SmallWidgets', popup_elem, "Step 14.1: Verify that the folder was already highlighted")
        close_popup = driver.find_element_by_css_selector("#dlgIbfsBrowseForFile [class*='active'] #IbfsBrowseForFolderDlg_btnCancel")
        utillobj.click_on_screen(close_popup, 'middle', click_type=0)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Small Widgets', launch_point='property_tab', button='OK', 
                                                section='column', item_name='Show Easy Selector', control='checkbox', checkbox_input='check', msg='Step 14.2:')
        
        """ Step 15: Click the + sign and click on any report
        """
        panel_elem = portal_canvas.get_column_obj(2)
        elem = panel_elem.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']")
        core_utilobj.left_click(elem)
        
        """ Step 16: Click the delete key on the keyboard
                     Verify that the key does NOTHING.
        """
        selector_items = self.driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        elem = selector_items[[elem.text.strip() for elem in selector_items].index('Category Sales')]
        core_utilobj.left_click(elem.find_element_by_css_selector("img"))
        time.sleep(1)
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.delete_key)
        else:
            keyboard.send('del')
        time.sleep(2)
        selector_items = driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        status_=False
        try:
            elem = selector_items[[elem.text.strip() for elem in selector_items].index('Category Sales')]
            status_=True
        except ValueError:
            print('Category Sales Not in list and its deleted.')
            status_=False
        utillobj.asequal(True, status_, "Verify 16: Verify that the del key does NOTHING after pressed.")
        core_utilobj.left_click(driver.find_element_by_css_selector("[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnCancel']"))
        
        """ Step 17: Click Add.
        """
        portal_canvas.select_easy_selector_item(1, 'Category Sales', option='column', button='Add')
        
        """ Step 18: Click the title bar menu arrow.
                     Verify that minimize, maximize, replace, refresh, delete show.
        """
        portal_canvas.manage_panel_title_menubar('Category Sales', expected_opt=['Minimize', 'Maximize', 'Replace', 'Refresh', 'Delete'], msg="Step 18: Verify that minimize, maximize, replace, refresh, delete show.")
        
        """ Step 19: Click Delete option
                     Verify that the panel disappears
        """
        portal_canvas.manage_panel_title_menubar('Category Sales', verify=False, select_menu_opt='Delete')
        elem = portal_canvas.get_column_obj(2).text
        status_ = True if elem == '' else False
        utillobj.asequal(True, status_, "Step 19: Verify that the panel disappears.")
        
        """ Step 20: Add another page
                     Change the layout to 1 column
        """
        portal_canvas.add_page('1 Column',Page_title='Page 2')
        
        """ Step 21: Add a responsive container
        """
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Responsive')
        
        """ Step 22: Select responsive container.
                     Verify no Show Easy Selector check box is available in Properties.
        """
        portal_canvas.select_panel('Panel 1')
        time.sleep(1)
        parent_css="[id^='idProperties']:not([style*='hidden'])"
        vbox_css=parent_css + " [id^='BIPTab']:not([style*='hidden']) div[id^='PropertiesCluster']  > div[id^='BiHBox']  > div[id*='Box']:not([style*='hidden'])"
        elems=driver.find_elements_by_css_selector(vbox_css)
        status_=False
        try:
            elems[['Show Easy Selector' in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
            status_=False
        except ValueError:
            status_= True
        utillobj.asequal(True, status_, "Step 22: Verify Show Easy Selector checkbox option is not available in Responsive panel Properties section.")
        
        """ Step 23: Click the BIP icon and exit then save
        """
        portal_ribbon.bip_save_and_exit('Yes')
        
        """ Step 24: Sign Out from WebFOCUS
        """
        core_utilobj.switch_to_previous_window(window_close=False)
        time.sleep(2)
                

if __name__ == '__main__':
    unittest.main()