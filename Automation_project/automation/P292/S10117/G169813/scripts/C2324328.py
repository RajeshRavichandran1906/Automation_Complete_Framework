'''
Created on 31-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324328
TestCase Name = Global Resources Testing : Create_New_Page_GlobalResources
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_ribbon, vfour_miscelaneous, vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324328_TestClass(BaseTestCase):

    def test_C2324328(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal'
        
        def verify_panel_data(panel_name, expected_panel_text, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_text = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.asin(expected_panel_text, actual_panel_text, "Step " + str(step_num) + ": Verify 'Resource Tree' added in '" + str(panel_name) + "'.")
        
        def verify_droped_panel_title(panel_name, expected_panel_list, step_num):
            panel_text = portal_canvas.get_panel_obj(panel_name)
            actual_panel_list = [elem.strip() for elem in panel_text.text.strip().split('\n') if elem != '']
            utillobj.as_List_equal(expected_panel_list, actual_panel_list, "Step " + str(step_num) + ": Verify panel dropped in page.")
           
        def verify_panel_frame_data(chart_type, panel_name, expected_value, step_num, custom_css=None):
            utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe'][name*='" + panel_name + "']",frame_height_value=0)
            if chart_type == 'legend':
                resultobj.verify_riser_legends("jschart_HOLD_0", expected_value, "Step "+str(step_num)+": Verify legend Title in '" + str(panel_name) + "'.")
            elif chart_type == 'text':
                actual_text = self.driver.find_element_by_css_selector(custom_css).text.strip()
                utillobj.asequal(actual_text, expected_value, "Step "+str(step_num)+": Verify table data displayed in '" + str(panel_name) + "'.")
            utillobj.switch_to_default_content(pause=3)
        
        """ Step 1: Sign into WebFOCUS home page as Administrator
                    Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        time.sleep(1)
         
        """ Step 2: Open the Global Resources node
        """
        """ Step 3: Open the Page Templates folder
        """
        """ Step 4: Right Click on Standard
                    Verify that there is NO new menu option
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Standard', expected_menu_list=['Refresh', 'Security', 'Properties'], item_exit=True, msg='Step 4')
        wf_mainpageobj.select_menu(project_id, 'Refresh')
         
        """ Step 5: Right Click on Custom
        """
        """ Step 6: Click New then Portal Page
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', 'New->Portal Page')
         
        """ Step 7: Enter 'Global_Resources_page' then Click Create
                    Leave as 1 column
        """
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
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(1)
        portal_misobj.select_page_template(page_template="1 Column", Page_title='Global_Resources_page', btn_name='Create')
        time.sleep(2)
        portal_properties.verify_breadcrumb_panel('Global_Resources_page', ['Global_Resources_page'], "Step 7: Verify that the breads-crumbs have the correct terminology 'Global_Resources_page'.")
         
        """ Step 8: Check the page icon and choose honda_integra image
        """
        portal_properties.edit_input_control('page', 'Page Icon', 'checkbox', checkbox_input='check', msg='Step 8:')
        portal_properties.edit_input_control('page', 'Change Image', 'button')
        portal_canvas.open_files_from_repository_window(BIP_Portal_Path, ['honda_integra'], msg="Step 8.1: ")
        portal_properties.verify_input_control('page', 'Page Icon', 'image', "Step 8.2: Verify Page icon changed to 'honda_integra'", page_icon_image_name='honda_integra')
         
        """ Step 9: Click Insert Tab
        """
        """ Step 10: Choose Resource Tree
                     Verify that the Resource Tree panel appears.
        """
        portal_ribbon.select_ribbon_item('Insert', 'Insert_ResourceTree')
        time.sleep(1)
        verify_panel_data('Panel 1', project_id, '10')
         
        """ Step 11: Click on BIP-->Exit then Yes to save
                     Verify that the Page appears under the Custom folder
        """
        portal_ribbon.bip_save_and_exit('Yes')
        time.sleep(3)
        core_utilobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        time.sleep(1)
        wf_mainpageobj.verify_repositery_item('Global Resources->Page Templates->Custom', 'Global_Resources_page', msg="11")
        wf_mainpageobj.select_menu(project_id, 'Refresh')
        image_index = wf_mainpageobj.expand_tree('Global Resources->Page Templates->Custom->Global_Resources_page')
        tree_rows="#bipTreePanel #treeView table>tbody>tr"
        repository_items = self.driver.find_elements_by_css_selector(tree_rows)
        td_img = repository_items[image_index].find_element_by_css_selector("img.icon")
        image_elem_src = utillity.UtillityMethods.get_attribute_value(self, td_img, 'src')
        utillobj.asin('honda_integra', image_elem_src['src'], "Step 11: Verify that the Page appears under the Custom folder.")
        
        """ Step 12: Click New then Portal Page from Global Resources > Custom folder
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom', 'New->Portal Page')
        
        """ Step 13: Enter 'Global_42Responsive_filter' then Click Create
                     Choose Responsive 4-2
        """
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
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90)
        time.sleep(1)
        portal_misobj.select_page_template(page_template="Responsive 4-2", Page_title='Global_42Responsive_filter', btn_name='Create')
        time.sleep(2)
        portal_properties.verify_breadcrumb_panel('Global_42Responsive_filter', ['Global_42Responsive_filter'], "Step 13: Verify that the breads-crumbs have the correct terminology 'Global_Resources_page'.")
        
        """ Step 14: Check the page icon and choose babydeer image
        """
        portal_properties.edit_input_control('page', 'Page Icon', 'checkbox', checkbox_input='check', msg='Step 14:')
        portal_properties.edit_input_control('page', 'Change Image', 'button')
        portal_canvas.open_files_from_repository_window(BIP_Portal_Path, ['babydeer'], msg="Step 14.1: ")
        portal_properties.verify_input_control('page', 'Page Icon', 'image', "Step 14.2: Verify Page icon changed to 'babydeer'", page_icon_image_name='babydeer')
         
        """ Step 15: Below the Designer Properties panel, click on Column 1 in the crumb trail.
                     Verify the Top margin is set to '5' px and then Same for All box checkbox is checked.
        """
        portal_properties.select_breadcrumb_panel('Global_42Responsive_filter', next='Column 1')
        time.sleep(1)
        portal_properties.verify_input_control('column', 'Top', 'textbox', "Step 15: Verify the Top margin is set to '5px'.", textbox_value='5')
        portal_properties.verify_input_control('column', 'Bottom', 'textbox', "Step 15.1: Verify the Bottom margin is set to '5px'.", textbox_value='5')
        portal_properties.verify_input_control('column', 'Left', 'textbox', "Step 15.2: Verify the Left margin is set to '5px'.", textbox_value='5')
        portal_properties.verify_input_control('column', 'Right', 'textbox', "Step 15.3: Verify the Right margin is set to '5px'.", textbox_value='5')
        portal_properties.verify_input_control('column', 'Same for All', 'checkbox', "Step 15.4: Verify the Right margin is set to '5px'.", checkbox_input='check')
        
        """ Step 16: Open Retail samples domain
                     Open the portals folder
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(2)
        
        """ Step 17: Drag 6 reports (Caterory Sales, Regional Sales Trend, Stores Sales by Region, Units Profit Treemap, Accordion DataTable, Freeze DataTable) into that responsive container; as you drag them there you will see a blue outline that will let you know this is a good place to drop.
                     Drag Standard Autofit Off over Accordion DataTable to add another tab
                     Drag Standard Autofit On over Freeze DataTable to add another tab
        """
        
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Add Content")
        time.sleep(2)
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Add Content")
        time.sleep(2)
        item_path="Retail Samples->Portal->Large Widgets->Store Sales by Region"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Add Content")
        time.sleep(2)
        item_path="Retail Samples->Portal->Large Widgets->Units Profit Treemap"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Add Content")
        time.sleep(2)
        item_path="Retail Samples->Portal->Responsive Tables->Accordion DataTable"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Add Content")
        time.sleep(2)
        item_path="Retail Samples->Portal->Responsive Tables->Freeze DataTable"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Add Content")
        time.sleep(2)
        item_path="Retail Samples->Portal->Responsive Tables->Standard Autofit Off"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Accordion DataTable")
        utillobj.select_or_verify_bipop_menu('Add As Tab', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden'])")
        time.sleep(2)
        portal_canvas.verify_tabbed_panel_in_responsive('Accordion DataTable', ['Accordion DataTable', 'Standard Autofit Off', 'New Tab'], "Step 17: Verify Standard Autofit Off added on another tab.")
        item_path="Retail Samples->Portal->Responsive Tables->Standard Autofit On"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Freeze DataTable")
        utillobj.select_or_verify_bipop_menu('Add As Tab', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden'])")
        time.sleep(2)
        portal_canvas.verify_tabbed_panel_in_responsive('Freeze DataTable', ['Freeze DataTable', 'Standard Autofit On', 'New Tab'], "Step 17.1: Verify Standard Autofit Off added on another tab.")
        expected_panel_text=['Category Sales', 'Regional Sales Trend', 'Store Sales by Region', 'Units Profit Treemap', 'Accordion DataTable', 'Accordion DataTable', 
                             'Standard Autofit Off', 'New Tab', 'Freeze DataTable', 'Freeze DataTable', 'Standard Autofit On', 'New Tab']
        verify_droped_panel_title('Category Sales', expected_panel_text, '17.2')
        
        verify_panel_frame_data('legend', 'Panel_2', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '17.3')
        verify_panel_frame_data('legend', 'Panel_3', ['EMEA', 'North America', 'Oceania', 'South America'], '17.4')
        verify_panel_frame_data('legend', 'Panel_4', ['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America', 'Revenue', '327.8M'], '17.5')
        verify_panel_frame_data('legend', 'Panel_5', ['Gross Profit', '0.3M', '13.1M', '26M', '38.9M', '51.8M'], '17.6')
        verify_panel_frame_data('text', 'Accordion_DataTable', 'Blu Ray', '17.7', custom_css="table[summary*='Standard'] tr:nth-child(2) td:nth-child(1)")
        verify_panel_frame_data('text', 'Freeze_DataTable', 'Blu Ray', '17.8', custom_css="table[summary*='Standard'] tr:nth-child(2) td:nth-child(1)")
        
        """ Step 18: Drag Retail Sales Filter panel to the left of Category sales panel
        """
        item_path="Retail Samples->Portal->Retail Sales Filter Panel"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Category Sales", drop_point='left', tx_offset=5)
        time.sleep(5)
        
        """ Step 19: Click on responsive properties button
                     Add bip-responsive-1 and change the height to 64px then click OK
        """
        portal_properties.edit_input_control('panel', 'Responsive Properties', 'button')
        time.sleep(1)
        portal_properties.manage_responsive_properties_popup('Custom CSS Classes', 'textbox', verification=False, textbox_input='bip-container bip-responsive-1')
        portal_properties.manage_responsive_properties_popup('Height', 'textbox', verification=False, textbox_input='64px')
        time.sleep(1)
        portal_properties.manage_responsive_properties_popup('OK', 'button', verification=False)
        
        """ Step 20: Click the Save button.
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        
        """ Step 21: Exit designer
                     Verify that the pages show up properly with their page icons correct.
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 90)
        time.sleep(1)
        wf_mainpageobj.verify_repositery_item('Global Resources->Page Templates->Custom', 'Global_42Responsive_filter', msg="21")
        wf_mainpageobj.select_menu(project_id, 'Refresh')
        image_index = wf_mainpageobj.expand_tree('Global Resources->Page Templates->Custom->Global_42Responsive_filter')
        tree_rows="#bipTreePanel #treeView table>tbody>tr"
        repository_items = self.driver.find_elements_by_css_selector(tree_rows)
        td_img = repository_items[image_index].find_element_by_css_selector("img.icon")
        image_elem_src = utillity.UtillityMethods.get_attribute_value(self, td_img, 'src')
        utillobj.asin('babydeer', image_elem_src['src'], "Step 22: Verify that the Page appears under the Custom folder.")
        
        """ Step 22: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()