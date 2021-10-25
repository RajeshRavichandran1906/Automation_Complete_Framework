'''
Created on Sep 23, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10117&group_by=cases:section_id&group_id=169813&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2324220
TestCase Name = Portal Designer_Layout : Adding_Panel_and_contents_to_Columns
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, wf_legacymainpage, vfour_miscelaneous, vfour_portal_canvas, vfour_portal_ribbon
# from common.pages import ia_resultarea
from common.lib import utillity, core_utility



class C2324220_TestClass(BaseTestCase):

    def test_C2324220(self):
        
        Test_Case_ID='C2324220'
        
        """
            TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
#         iaresultobj= ia_resultarea.IA_Resultarea(self.driver)
        vfour_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+'->'+suite_id
        
        """
            Step 01: Sign into WebFOCUS home page as Developer User
                     Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
         
        """
            Step 02:Edit 'BIP_xxx_Portal123_V4' portal
        """
        wf_mainpageobj.select_repository_menu(folder_path+'->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        core_utilobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        time.sleep(5)
        """
            Step 03:Press F8 if the resource tree is not present
                    Right Click on Domains then View > Display by Title
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(5)
        vfour_misobj.select_resource_menu(workspace, 'View->Display By Title')
             
        """
            Step 04:Select Column1 Layout area in canvas and Click insert tab; Add a simple panel ;Panel1;
                    Verify that Panel 1 appears on the page canvas with no content
        """
        portal_canvas.select_column(1)   
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
        time.sleep(3)
        portal_canvas.verify_column_panel_caption(1, 'Panel 1', "Step 04.00: Verify first panel title")
             
        """
            Step 05: Click on Resource tree icon in the content group
                     Verify that the tree now appears in Panel 1
        """
                 
        portal_ribbon.select_ribbon_item("Insert", 'Insert_ResourceTree')  
        vfour_misobj.verify_resource_item(workspace, project_id, "Step 05.00 :", item_exit=True, tree_rows="div[id^='BipContentArea'] div[class*='bi-tree-view-body-content'] td")
                  
        """
            Step 06:Select Column2 Layout area in canvas and Click insert tab; Add a simple panel;
        """
        time.sleep(2)
        portal_canvas.select_column(2)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
        time.sleep(3)
             
        """
            Step 07:From F8 Resource tree-> Retail Samples --> Portal --> Small widget, Drag and Drop the Category Sales content into panel2.
                Verify that the area name changes to the report name
        """
              
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 2", tx_offset=-126)
        time.sleep(5)
        portal_canvas.verify_column_panel_caption(2, 'Category Sales', "Step 07.00 : Verify first panel title")        
                 
        """
            Step 08:Select Column3 layout area in canvas and Add an Accordion panel from insert tab; 
                    Drag and Drop Regional Sales trend content from F8 Resource tree > Retail Samples > Portal > Small Widgets to Accordion panel Area1 
                    then choose replace area content
            Verify that the area name changes to the report name
        """
        portal_canvas.select_column(3)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Accordion')
        time.sleep(5)
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3", tx_offset=-126)
        vfour_misobj.select_bipop_menu('Replace Area Content')
        portal_canvas.verify_accordian_panel_title('Panel 3', ['Regional Sales Trend', 'New Area'], "Step 08.00: Verify accordian title")
        time.sleep(3)
               
        """
            Step 09:Click New Area in the Accordion panel(panel3); 
                    Drag and Drop Accordion report content from F8 Resource tree -> P292->S10117 -> BIP_V4_Portal to Area2 by choosing replace area content
                Verify that the area name changes to the report name
        """
        portal_canvas.select_accordian_panel_title('Panel 3', 'New Area') 
              
        item_path=folder_path+"->BIP_V4_Portal->Accordion report"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3")
        vfour_misobj.select_bipop_menu('Replace Area Content')
        accordian_title=['Regional Sales Trend','Accordion report','New Area']
        portal_canvas.verify_accordian_panel_title('Panel 3', accordian_title, "Step 09.00: Verify accordian title")
        time.sleep(3)
     
        """
            Step 10:Select Column4 layout area in canvas and Add a Tabbed panel from insert tab;
            Drag and Drop Demo Videos (url) content from F8(Resource tree) -> Retail Samples to Tabbed panel area Tab1 by choosing replace tab content
            Verify that the tab name changes to the report name
        """
        portal_canvas.select_column(4)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Tabbed')
        time.sleep(2)
        item_path="Retail Samples->Demo Videos"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", tx_offset=-126)
        vfour_misobj.select_bipop_menu('Replace Tab Content')
        Tabbed_title=['Demo Videos', 'New Tab']
        portal_canvas.verify_tabbed_panel('Panel 4', Tabbed_title,  "Step 10.01: Verify Tabbed_title")
        time.sleep(3)
              
        """
            Step 11:Drag and Drop an Image content (ie babydeer) 
            from F8 Resource tree -> P292 -> S10117 -> BIP_V4_Portal into Tab2 by choosing Add As tab
            Verify that the tab name changes to the report name
                  
        """
        panel_0bj = portal_canvas.get_column_obj(4)
        utillobj.click_on_screen(panel_0bj, 'top_middle')
        item_path=folder_path+"->BIP_V4_Portal->babydeer"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", tx_offset=-126)
        time.sleep(3)
        vfour_misobj.select_bipop_menu('Add As Tab')
        Tabbed_title=['Demo Videos','babydeer','New Tab']
        portal_canvas.verify_tabbed_panel('Panel 4', Tabbed_title,  "Step 11.01: Verify Tabbed_title")
        utillobj.verify_object_visible("[id^='ID_'] div[id^='BipContentArea'] img[id^='BiImage']", True, 'Step 11.02: babydeer icon is Visible')
        """
            Step 12:Drag and Drop an Discount by Region from F8 Resource tree > Retail Samples > Portal > Small Widgets into Tab3 by choosing Add as tab
        """
        panel_0bj = portal_canvas.get_panel_obj('Panel 4')
        utillobj.click_on_screen(panel_0bj, 'right')
        item_path="Retail Samples->Portal->Small Widgets->Discount by Region"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", tx_offset=-126)
        time.sleep(5)
        vfour_misobj.select_bipop_menu('Add As Tab')
        Tabbed_title=['Demo Videos','babydeer','Discount by Region','New Tab']
        portal_canvas.verify_tabbed_panel('Panel 4', Tabbed_title,  "Step 12.01: Verify Tabbed_title")
        time.sleep(3)

        """
            Step 13:Click New Tab in tabbed panel; Drag and drop P292 domain into Tab 4 by choosing replace tab content
                    Verify that the folder is there with its contents
        """
        time.sleep(2)
        if bool(driver.find_element_by_css_selector("[id^='BipTabBar'] :not([style*='hidden']) [id^='BiRepeatButton'][class*='scroll-right']")):
            portal_canvas.scroll_tabbed_panel("Panel 4", 'right', 5)
        portal_canvas.select_tabbed_panel("Panel 4", "New Tab")
        panel_0bj = portal_canvas.get_panel_obj('Panel 4')
        utillobj.click_on_screen(panel_0bj, 'bottom_middle')
        item_path=project_id
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", tx_offset=-126)
        time.sleep(3)
        vfour_misobj.select_bipop_menu('Replace Tab Content')
        time.sleep(5)
        panel_4_obj = portal_canvas.get_panel_obj('Panel 4')
        panel_4_text_list = panel_4_obj.find_element_by_css_selector("table").text.strip().split('\n')
        utillobj.asin(item_path, panel_4_text_list, "Step 13.01: Verify that the folder is there with its contents")
          
        """
            Step 14:Open 'P292_S10117' domain in the tree blockTry to drag a portal onto the page canvas
                    Verify that you get the no drop icon
        """
        ''' Step done by manual team '''
            
        """
            Step 15:Save the portal
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
    
        """ Step16: Click insert tab; and click on new page icon under page group; choose a 3 column layout and enter AHTML_page
                    Verify all the above changes are available in the design mode. 
                    Verify that as you are typing the title of the page is changing.
        """
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Page')
        vfour_misobj.select_page_template(page_template="3 Column", Page_title="AHTML_page", btn_name="Create")
        portal_canvas.verify_page_in_navigation_bar('AHTML_page', "Step 16.00:", verify=True)
           
        """
            Step 17:Add a simple panel to column1; add a simple panel to column2; Again add a simple panel to Column3;
        """
        #column 1
        portal_canvas.select_column(1)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
        #column 2
        portal_canvas.select_column(2)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
        #column 3
        portal_canvas.select_column(3)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
        """
            Step 18:Drag and Drop the Regional Analysis from F8(Resource tree) -> Retail Samples -> Documents content into panel1..
            Verify the report content ran in the panel.
        """
           
        # Panel 1
        portal_canvas.select_panel("Panel 1")
        item_path="Retail Samples->Documents->Regional Analysis"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 1", tx_offset=-126)
        resobj.wait_for_property('Regional Analysis Panel', 1, expire_time=190, string_value='Regional Analysis', parent_object=portal_canvas.get_current_page())
        portal_canvas.verify_column_panel_caption(1, 'Regional Analysis', "Step 18.00: Verify first panel title")
        element = portal_canvas.get_panel_obj('Regional Analysis')
        utillobj.take_screenshot(element, Test_Case_ID+"_Actual_step_18")
          
        """
            Step 19:Drag and Drop the Sales by Region Dashboard content into panel 2.
        """
        #Panel 2
        portal_canvas.select_panel("Panel 2")    
        item_path="Retail Samples->Documents->Sales by Region Dashboard"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 2", tx_offset=-126)
        resobj.wait_for_property('Sales by Region Dashboard Panel', 1, expire_time=190, string_value='Sales by Region Dashboard', parent_object=portal_canvas.get_current_page())
        portal_canvas.verify_column_panel_caption(2, 'Sales by Region Dashboard', "Step 19.01: Verify first panel title")
        time.sleep(3)
        
        """
            Step 20:Drag and Drop the tagCloud chart content into panel 3 .
                    Verify the report content ran inside the panel;
        """
        #Panel 3
        portal_canvas.select_panel("Panel 3")
        item_path=folder_path+"->BIP_V4_Portal->tagCloud chart"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3", tx_offset=-126)
        resobj.wait_for_property('tagCloud chart Panel', 1, expire_time=190, string_value='tagCloud chart', parent_object=portal_canvas.get_current_page())
        portal_canvas.verify_column_panel_caption(3, 'tagCloud chart', "Step 20.00: Verify first panel title")
        time.sleep(3)
          
        """
            Step 21 :Right click on AHTML_page and remove
                    Verify that the page is now gone
        """
        portal_canvas.manage_page_menu('AHTML_page', "Remove")
        time.sleep(5)
        """
            Step 22:Close the F8 tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=False)
        time.sleep(3)
         
        """
            Step 23:Save and Exit the portal
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        """
            Step 24:Sign Out from WebFOCUS
        """
        core_utilobj.switch_to_previous_window(window_close=False)
        time.sleep(3)

        
if __name__ == '__main__':
    unittest.main()
