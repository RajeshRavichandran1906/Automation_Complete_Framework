'''
Created on 04-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324322
TestCase Name = Portal Designer_Design Properties : Lock Width
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, ia_resultarea, wf_mainpage, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_portal_properties, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
import keyboard as local_keyboard

class C2324322_TestClass(BaseTestCase):

    def test_C2324322(self):
        """
        TESTCASE VARIABLES
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02', 'wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        BIP_Portal_Path = 'P292->S10117->BIP_V4_Portal'
        portal_name = 'lock column portal'
        
        def verify_coumn_panel_title(column_no, expected_column_text_list, step_num):
            elem = portal_canvas.get_column_obj(column_no)
            panel_titles = elem.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
            actual_column_text_list = [elem.strip() for elem in [elem.text.strip() for elem in panel_titles] if elem != '']
            utillobj.as_List_equal(expected_column_text_list, actual_column_text_list, "Step " + str(step_num) + ": Verify 'column " + str(column_no) + "' panel.")
            
        def verify_panel_frame_data(chart_type, panel_name, expected_legend, step_num):
            vfour_miscelaneous.Vfour_Miscelaneous.switch_to_frame_in_bip_page(self, frame_panel_name=panel_name)
            resultobj.wait_for_property('#jschart_HOLD_0', 1, expire_time=15)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'riser':
                ia_resultobj.verify_number_of_chart_segment("jschart_HOLD_0", expected_legend, "Step "+str(step_num)+": Verify number of risers displayed in '" + str(panel_name) + "'.")   
            utillobj.switch_to_default_content(pause=3)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 2: Right click on the 'lock column' portal under P292->S10117 in domains tree and choose Edit
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
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 3: Add another 3 Column page titled lock width testing page
        """
        portal_canvas.add_page('3 Column',Page_title='lock width testing page')
        time.sleep(1)
        portal_canvas.select_page_in_navigation_bar('lock width testing page')
        time.sleep(2)
        
        """ Step 4: Add some panels and content from the retail samples domain in each column
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(1)
        portal_canvas.select_column(1)
        time.sleep(0.5)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(0.5)
        portal_canvas.select_column(2)
        time.sleep(0.5)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(0.5)
        portal_canvas.select_column(3)
        time.sleep(0.5)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 1")
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 2")
        item_path="Retail Samples->Portal->Small Widgets->Discount by Region"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3")
        time.sleep(3)
        verify_panel_frame_data('legend', 'Panel_1', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '4')
        verify_panel_frame_data('legend', 'Panel_2', ['EMEA', 'North America', 'Oceania', 'South America'], '4.1')
        verify_panel_frame_data('riser', 'Panel_3', 16, '4.2')
        
        """ Step 5: Click Column 2 and change the width to 850
                    Verify that the column got bigger.
        """
        portal_canvas.select_column(2)
        time.sleep(2)
        portal_properties.edit_input_control('column', 'Width', 'combobox', combobox_input='{Value}')
        time.sleep(1)
        portal_properties.edit_input_control('column', 'Width', 'textbox', textbox_input='850')
        time.sleep(1)
        local_keyboard.send('enter')
        time.sleep(1)
        portal_canvas.select_column(2)
        current_page = portal_canvas.get_current_page()
        column2_widht=current_page.find_element_by_css_selector("[class*='selection-marquee']").size['width']
        utillobj.asequal('850', str(int(column2_widht)), "Step 5: Verify Column 2 width change to 850 and that column got bigger.")
        
        """ Step 6: Check the Lock Width box
        """
        portal_properties.edit_input_control('column', 'Lock Width', 'checkbox', checkbox_input='check', msg='Step 5.1')
        
        """ Step 7: Save and run the portal
        """
        portal_ribbon.bip_save_and_exit('Yes')
        utillobj.switch_to_window(0)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->'+portal_name, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        verify_coumn_panel_title(1, ['Category Sales'], '7')
        verify_coumn_panel_title(2, ['Regional Sales Trend'], '7.1')
        verify_coumn_panel_title(3, ['Discount by Region'], '7.2')
        
        """ Step 8: Change the browser size to small enough to just see the panel in column 2
                    Verify that the panel in column 2 is the one being shown
                    Verify that you see a horizontal scroll bar at the bottom of the browser
        """
        verify_panel_frame_data('legend', 'Panel_1', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '8')
        verify_panel_frame_data('legend', 'Panel_2', ['EMEA', 'North America', 'Oceania', 'South America'], '8.1')
        verify_panel_frame_data('riser', 'Panel_3', 16, '8.2')
        time.sleep(1)
        driver.set_window_size(860, 560)
        elem = portal_canvas.get_current_page()
        utillobj.take_screenshot(elem, 'C2324321_Actual_Step_8')
        driver.maximize_window()
        time.sleep(5)
        verify_panel_frame_data('legend', 'Panel_2', ['EMEA', 'North America', 'Oceania', 'South America'], '8.3')
        time.sleep(1)
        
        """ Step 9: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 10: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()