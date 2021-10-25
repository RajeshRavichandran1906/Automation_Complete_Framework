'''
Created on 13-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324251
TestCase Name = Run Mode_Run Content : Run Easy Selector
'''
import unittest, time, keyboard
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_ribbon, vfour_portal_canvas, vfour_portal_run, wf_legacymainpage, vfour_portal_properties, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException

class C2324251_TestClass(BaseTestCase):

    def test_C2324251(self):
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        portal_name = 'Easy_Selector'
        BIP_Portal_Path = 'P292->S10117->BIP_V4_Portal'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 2: Right Click 'Easy_Selector' and choose Run
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
         
        """ Step 3: Click the Plus sign in column 1
                    Verify that the Retail Samples -> Portal -> Small Widgets is expanded with all the reports
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        panel_elem = portal_canvas.get_column_obj(1)
        elem = panel_elem.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']")
        elem.click()
        avialable_items = driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        actual = [elem.replace(' ','') for elem in [elem.text.strip() for elem in avialable_items] if elem not in '']
        expected = ['CategorySales', 'RegionalSalesTrend', 'DiscountbyRegion', 'RegionalProfitbyCategory', 'AverageCostvSales', 'AverageCostvsRevenueScatter', 'ProductProfitLineByMonth', 'RevenueProductBar', 'RevenueRegionBar']
        utillobj.as_List_equal(actual, expected, "Step 3: Verify that the Retail Samples -> Portal -> Small Widgets is expanded with all the reports.")
        driver.find_element_by_css_selector("[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnCancel']").click()
         
        """ Step 4: Choose 'Average Cost Vs Sales' report
                    Verify that the report is now shown in the container
        """
        portal_canvas.select_easy_selector_item(1, 'Average Cost v Sales', option='column', button='Add')
        portal_canvas.verify_panel_caption('Average Cost v Sales', "Step 4: Verify that the Average Cost v Sales report is now shown in the container")
        panel_elem = portal_canvas.get_column_obj(1)
        elem = panel_elem.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']")
        elem.click()
        avialable_items = driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        actual = [elem.replace(' ','') for elem in [elem.text.strip() for elem in avialable_items] if elem not in '']
        expected = ['CategorySales', 'RegionalSalesTrend', 'DiscountbyRegion', 'RegionalProfitbyCategory', 'AverageCostvsRevenueScatter', 'ProductProfitLineByMonth', 'RevenueProductBar', 'RevenueRegionBar']
        utillobj.as_List_equal(actual, expected, "Step 3: Verify that the Retail Samples -> Portal -> Small Widgets is expanded with all the reports.")
        driver.find_element_by_css_selector("[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnCancel']").click()
        portal_canvas.select_easy_selector_item(1, 'Category Sales', option='column', button='Add')
        time.sleep(2)
        panel_bef=portal_canvas.get_panel_obj('Category Sales')
        panel_width_bef = panel_bef.size['height']
         
        """ Step 5: Add another 2 column page
        """
        portal_canvas.add_page('2 Column',Page_title='Page 3')
         
        """ Step 6: Add 'tagCloud chart' into col 1 and col 2
        """
        status_ = False
        res = False
        try:
            res = driver.find_element_by_css_selector("#ResourcesPanelID #bipResourcesPanel").is_displayed()
            status_=True
        except NoSuchElementException:
            res = False
            status_ = False
        if status_ == True and res == True:
            pass
        else:
            portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
        item_path = BIP_Portal_Path + "->tagCloud_chart"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 1)
        time.sleep(2)
        item_path = BIP_Portal_Path + "->tagCloud_chart"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "column", 2)
        time.sleep(2)
        ''' Verify tagCloud_chart panel in column 1'''
        portal_canvas.verify_column_panel_caption(1, 'tagCloud_chart', "Step 6: Verify tagCloud_chart added in column 1")
        column1 = portal_canvas.get_column_obj(1)
        driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        parent_css="#jschart_HOLD_0 g.groupPanel"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        actual_elems = driver.find_elements_by_css_selector(parent_css+" text")
        actual_text = [elem.text.strip() for elem in actual_elems]
        expected_text = ['W GERMANY', 'ENGLAND', 'ITALY', 'JAPAN', 'FRANCE']
        utillobj.as_List_equal(actual_text, expected_text, "Step 6.1: Verify tagCloud_chart is loaded.")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify tagCloud_chart panel in column 2'''
        portal_canvas.verify_column_panel_caption(2, 'tagCloud_chart', "Step 6.2: Verify tagCloud_chart added in column 2")
        column1 = portal_canvas.get_column_obj(2)
        driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        parent_css="#jschart_HOLD_0 g.groupPanel"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        actual_elems = driver.find_elements_by_css_selector(parent_css+" text")
        actual_text = [elem.text.strip() for elem in actual_elems]
        expected_text = ['W GERMANY', 'ENGLAND', 'ITALY', 'JAPAN', 'FRANCE']
        utillobj.as_List_equal(actual_text, expected_text, "Step 6.3: Verify tagCloud_chart is loaded.")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
         
        """ Step 7: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(5)
         
        """ Step 8: Run the portal again
                    Switch between pages then click Close
                    Verify that there are no issues with the tagCloud report
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        portal_canvas.select_page_in_navigation_bar('Page 2')
        time.sleep(2)
        portal_canvas.select_page_in_navigation_bar('Page 3')
        time.sleep(2)
        ''' Verify tagCloud_chart panel in column 1'''
        portal_canvas.verify_column_panel_caption(1, 'tagCloud_chart', "Step 8: Verify tagCloud_chart added in column 1")
        column1 = portal_canvas.get_column_obj(1)
        driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        parent_css="#jschart_HOLD_0 g.groupPanel"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        actual_elems = driver.find_elements_by_css_selector(parent_css+" text")
        actual_text = [elem.text.strip() for elem in actual_elems]
        expected_text = ['W GERMANY', 'ENGLAND', 'ITALY', 'JAPAN', 'FRANCE']
        utillobj.as_List_equal(actual_text, expected_text, "Step 8.1: Verify tagCloud_chart is loaded.")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify tagCloud_chart panel in column 2'''
        portal_canvas.verify_column_panel_caption(2, 'tagCloud_chart', "Step 8.2: Verify tagCloud_chart added in column 2")
        column1 = portal_canvas.get_column_obj(2)
        driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        parent_css="#jschart_HOLD_0 g.groupPanel"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        actual_elems = driver.find_elements_by_css_selector(parent_css+" text")
        actual_text = [elem.text.strip() for elem in actual_elems]
        expected_text = ['W GERMANY', 'ENGLAND', 'ITALY', 'JAPAN', 'FRANCE']
        utillobj.as_List_equal(actual_text, expected_text, "Step 8.3: Verify tagCloud_chart is loaded.")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(5)
         
        """ Step 9: Edit the portal then click on page1
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
        utillobj.switch_to_window(1)
        time.sleep(2)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
         
        """ Step 10: Uncheck the Lock page checkbox
                     Exit and save
        """
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg="Step 10: ")
        time.sleep(2)
        portal_ribbon.select_tool_menu_item('menu_Save')
        time.sleep(2)
        portal_ribbon.select_tool_menu_item('menu_Exit')
        utillobj.switch_to_window(0, pause=5)
         
        """ Step 11: Run the portal,
                     Press F8 to bring up the tree,
                     Expand P292 domain -> S10117 folder.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
         
        """ Step 12: Right Click on Folders, pages and portals and choose Properties menu option
                     Verify that the Advanced Tab does not show for these objects. It should show only for reports.
        """
        portal_misobj.select_resource_menu(BIP_Portal_Path, 'Properties')
        parent_css="#dlgProperties [class*='active']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        properties_tab_css="#dlgProperties [class*='active'] #propTabPane [id*='BiTabBar'] [id*='BiTabButton']"
        tab_elems = driver.find_elements_by_css_selector(properties_tab_css)
        actual_tab_text = [elem.text.strip() for elem in tab_elems]
        utillobj.as_List_equal(actual_tab_text, ['Main Properties'], "Step 12: Verify that the Advanced Tab does not show for these objects. It should show only for reports.")
        time.sleep(1)
        portal_misobj.edit_properties_dialog('Main Properties', 'button', 'Cancel')
        """ Step 13: Open Retail Samples -> Portal -> Small Widgets
                     Right click on Category Sales and choose Properties
        """
        """ Step 14: Click the Advanced tab
        """
        """ Step 15: Change the defaultheight to 90
        """
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_misobj.select_resource_menu(item_path, 'Properties')
        portal_misobj.edit_properties_dialog('Advanced', 'textbox', 'Default Height', text_input='90')
        time.sleep(1)
        portal_misobj.edit_properties_dialog('Advanced', 'button', 'OK')
        
        """ Step 16: Click the Plus sign in column1
                     Verify that the Retail Samples -> Portal -> Small Widgets is expanded with all the reports
        """
        panel_elem = portal_canvas.get_column_obj(1)
        elem = panel_elem.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']")
        elem.click()
        parent_css = "[id^='dlgIbfsOpenFile'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        avialable_items = driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        actual = [elem.replace(' ','') for elem in [elem.text.strip() for elem in avialable_items] if elem not in '']
        expected = ['CategorySales', 'RegionalSalesTrend', 'DiscountbyRegion', 'RegionalProfitbyCategory', 'AverageCostvSales', 'AverageCostvsRevenueScatter', 'ProductProfitLineByMonth', 'RevenueProductBar', 'RevenueRegionBar']
        utillobj.as_List_equal(actual, expected, "Step 16: Verify that the Retail Samples -> Portal -> Small Widgets is expanded with all the reports.")
        driver.find_element_by_css_selector("[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnCancel']").click()
         
        """ Step 17: Choose Category Sales report
                     Before height change
                     Verify that the report is now shown in the container
                     After height change
                     verify that the panel height has changed to what it was before
        """
        portal_canvas.select_easy_selector_item(1, 'Category Sales', option='column', button='Add')
        time.sleep(2)
        panel_aft = portal_canvas.get_panel_obj('Category Sales')
        panel_width_aft = panel_aft.size['height']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 250, 315, 'less_than' , "Step 17: Verify Category Sales is being resized to widht 90.")
        panel_elem = portal_canvas.get_column_obj(1)
        elem = panel_elem.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']")
        elem.click()
        parent_css = "[id^='dlgIbfsOpenFile'] [class*='active']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        avialable_items = driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        actual = [elem.replace(' ','') for elem in [elem.text.strip() for elem in avialable_items] if elem not in '']
        expected = ['RegionalSalesTrend', 'DiscountbyRegion', 'RegionalProfitbyCategory', 'AverageCostvSales', 'AverageCostvsRevenueScatter', 'ProductProfitLineByMonth', 'RevenueProductBar', 'RevenueRegionBar']
        utillobj.as_List_equal(actual, expected, "Step 17: Verify that the Retail Samples -> Portal -> Small Widgets is expanded with all the reports.")
         
        """ Step 18: Keep alternating between column1 and 2 and add all the reports or you can multi select the reports to add them.
                     Once all reports are added
                     Verify that the Plus signs no longer show
        """
        click_first_elem = driver.find_element_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td img")
        click_first_elem.click()
        keyboard.send('ctrl+a')
        time.sleep(1)
        driver.find_element_by_css_selector("[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btnOK']").click()
        status_=False
        try:
            driver.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']")
            status_=False
        except NoSuchElementException:
            status_=True
        utillobj.asequal(True, status_, "Step 18: Verify that the Plus signs no longer show")
         
        """ Step 19: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(2)
        
        """ Step 20: Remove defaultHeight for Category Sales 
                     Click OK and close.
        """
        wf_mainpageobj.select_repository_menu(item_path, 'Properties')
        wf_mainpageobj.edit_properties_dialog('Advanced', 'textbox', 'Default Height', text_input='')
        time.sleep(1)
        portal_misobj.edit_properties_dialog('Advanced', 'button', 'OK')
        time.sleep(2)
        driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 21: Check Properties > Advanced tab for the Category Sales
                     Make sure the changes are still present
        """
        wf_mainpageobj.select_repository_menu(item_path, 'Properties')
        wf_mainpageobj.verify_properties_dialog('textbox', 'Default Height', "Step 21: Verify Default Height value is null.", tab_name='Advanced', textbox_value='')
        
        """ Step 22: Click Close button
        """
        time.sleep(1)
        wf_mainpageobj.edit_properties_dialog('Advanced', 'button', 'Cancel')
        
        """ Step 23: Sign Out from WebFOCUS
        """
        time.sleep(5)
                

if __name__ == '__main__':
    unittest.main()