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
from common.pages import visualization_resultarea, wf_legacymainpage, vfour_miscelaneous, wf_mainpage, vfour_portal_canvas, vfour_portal_ribbon, vfour_portal_run,ia_resultarea
from common.lib import utillity



class C2324220_TestClass(BaseTestCase):

    def test_C2324220(self):
        
        Test_Case_ID='C2324220'
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iaresultobj= ia_resultarea.IA_Resultarea(self.driver)
        vfour_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        
        """
            Step 01:Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#topBannerMenuBox [id^='SignonBannerPanelToolsMenuBtn']"
        resobj.wait_for_property(parent_css, 1, expire_time=20, string_value="Tools", with_regular_exprestion=True)
         
        """
            Step 02:Edit 'BIP_xxx_Portal123_V4' portal
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
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
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(5)
        """
            Step 03:Press F8 if the resource tree is not present
                    Right Click on Domains then View > Display by Title
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(5)
        vfour_misobj.select_resource_menu('Domains', 'View->Display By Title')
           
        """
            Step 04:Select Column1 Layout area in canvas and Click insert tab; Add a simple panel ;Panel1;
                    Verify that Panel 1 appears on the page canvas with no content
        """
        portal_canvas.select_column(1)   
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
        time.sleep(3)
        portal_canvas.verify_column_panel_caption(1, 'Panel 1', "Step 04 : Verify first panel title")
           
        """
            Step 05: Click on Resource tree icon in the content group
                     Verify that the tree now appears in Panel 1
        """
               
        portal_ribbon.select_ribbon_item("Insert", 'Insert_ResourceTree')  
        vfour_misobj.verify_resource_item('Domains', 'P292', "Step 05:", item_exit=True, tree_rows="div[id^='BipContentArea'] div[class*='bi-tree-view-body-content'] td")
                
        """
            Step 06:Select Column2 Layout area in canvas and Click insert tab; Add a simple panel;
        """
        time.sleep(2)
        portal_canvas.select_column(2)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_Panel')
        time.sleep(3)
        portal_canvas.verify_panel_caption("Panel 1", "Step 06.1: Verify first panel title'")
        portal_canvas.verify_panel_caption("Panel 2", "Step 06.2: Verify first panel title'")
           
        """
            Step 07:From F8 Resource tree-> Retail Samples --> Portal --> Small widget, Drag and Drop the Category Sales content into panel2.
                Verify that the area name changes to the report name
        """
            
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 2", tx_offset=-126)
        time.sleep(5)
        portal_canvas.verify_column_panel_caption(2, 'Category Sales', "Step 07 : Verify first panel title")        
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel']",frame_height_value=0)
        time.sleep(8)
                
        parent_css="#jschart_HOLD_0 path[class*='riser!']"
        resobj.wait_for_property(parent_css, 7, expire_time=50)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0",7, 'Step 07.1: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
                
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Revenue',"Step 07.2: Verify X-axis label")
                
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='totalLabel!g0!mtotalLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'1.1B',"Step 07.3: Verify total label")
                
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 07.4: Verify legend Title")
                
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue1", "Step 07.5 Verify first bar color")
                
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
               
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
        utillobj.select_or_verify_bipop_menu('Replace Area Content', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        portal_canvas.verify_accordian_panel_title('Panel 3', ['Regional Sales Trend', 'New Area'], "Step 08: Verify accordian title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Area_1']",frame_height_value=0)
        time.sleep(8)
             
        parent_css="#jschart_HOLD_0 path[class*='riser!']"
        resobj.wait_for_property(parent_css, 4, expire_time=50)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 4, 'Step 08.1: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
             
        legend=['EMEA', 'North America', 'Oceania', 'South America']
        resobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 08.2: Verify legend Title")
             
        resobj.verify_xaxis_title("jschart_HOLD_0", "Month", "Step 08.3: Verify -xAxis Title")
        resobj.verify_yaxis_title("jschart_HOLD_0", "Revenue", "Step 08.4: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['1','2','3','4','5','6','7','8','9','10','11','12']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        resobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 08.5: Verify XY labels")
             
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mline!", "bar_blue1", "Step 08.6: Verify first bar color", attribute_type='stroke')
             
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
             
        """
            Step 09:Click New Area in the Accordion panel(panel3); 
                    Drag and Drop Accordion report content from F8 Resource tree -> P292->S10117 -> BIP_V4_Portal to Area2 by choosing replace area content
                Verify that the area name changes to the report name
        """
        portal_canvas.select_accordian_panel_title('Panel 3', 'New Area') 
            
        item_path="P292->S10117->BIP_V4_Portal->Accordion_report"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3", tx_offset=-126)
        utillobj.select_or_verify_bipop_menu('Replace Area Content',custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        accordian_title=['Regional Sales Trend','Accordion_report','New Area']
        portal_canvas.verify_accordian_panel_title('Panel 3', accordian_title, "Step : Verify accordian title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe '][name^='Area_2']",frame_height_value=0)
        time.sleep(8)
        parent_css="[ibiattr='table1']"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(3)
#         vfour_runobj.create_table_data_set("table[ibiattr='table1']", Test_Case_ID+'_Ds01.xlsx')
        vfour_runobj.verify_table_data_set("table[ibiattr='table1']", Test_Case_ID+'_Ds01.xlsx', "Step 09:Accordion_report verification ")
        utillobj.switch_to_default_content(pause=3)
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
        utillobj.select_or_verify_bipop_menu('Replace Tab Content', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden'])")
        Tabbed_title=['Demo Videos', 'New Tab']
        portal_canvas.verify_tabbed_panel('Panel 4', Tabbed_title,  "Step 10.1: Verify Tabbed_title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Tab_1']",frame_height_value=0)
        time.sleep(5)
        parent_css="a[class^='navbar-brand'] img"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(2)
        utillobj.verify_object_visible("a[class^='navbar-brand'] img", True, 'Step 10.2:Info builders icon is Visible')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
            
        """
            Step 11:Drag and Drop an Image content (ie babydeer) 
            from F8 Resource tree -> P292 -> S10117 -> BIP_V4_Portal into Tab2 by choosing Add As tab
            Verify that the tab name changes to the report name
                
        """
        panel_0bj = portal_canvas.get_column_obj(4)
        utillobj.click_on_screen(panel_0bj, 'top_middle')
        item_path="P292->S10117->BIP_V4_Portal->babydeer"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", tx_offset=-126)
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Add As Tab', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden'])")
        Tabbed_title=['Demo Videos','babydeer','New Tab']
        portal_canvas.verify_tabbed_panel('Panel 4', Tabbed_title,  "Step 11.1: Verify Tabbed_title")
        utillobj.verify_object_visible("[id^='ID_'] div[id^='BipContentArea'] img[id^='BiImage']", True, 'Step 11.2: babydeer icon is Visible')
        """
            Step 12:Drag and Drop an Discount by Region from F8 Resource tree > Retail Samples > Portal > Small Widgets into Tab3 by choosing Add as tab
        """
        panel_0bj = portal_canvas.get_panel_obj('Panel 4')
        utillobj.click_on_screen(panel_0bj, 'right')
        item_path="Retail Samples->Portal->Small Widgets->Discount by Region"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", tx_offset=-126)
        time.sleep(5)
        utillobj.select_or_verify_bipop_menu('Add As Tab' , custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        Tabbed_title=['Demo Videos','babydeer','Discount by Region','New Tab']
        portal_canvas.verify_tabbed_panel('Panel 4', Tabbed_title,  "Step 12.1: Verify Tabbed_title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel_4_9']",frame_height_value=0)
        time.sleep(8)
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        resobj.wait_for_property(parent_css, 16, expire_time=50)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 16, 'Step 12.1: Verify number of risers displayed', custom_css="svg g>rect[class^='riser!s']")   
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g3!mbar!", "yellow_green", "Step 12.2: Verify first bar color")
        utillobj.switch_to_default_content(pause=3)
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
        item_path="P292"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 4", tx_offset=-126)
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Replace Tab Content', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item ']:not([style*='hidden'])")
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=False)
        time.sleep(5)
        if bool(driver.find_element_by_css_selector("[id^='BipTabBar'] :not([style*='hidden']) [id^='BiRepeatButton'][class*='scroll-left']")):
            portal_canvas.scroll_tabbed_panel("Panel 4", 'left', 3)
        Tabbed_title=['Demo Videos','babydeer','Discount by Region','Tab 4']
        portal_canvas.verify_tabbed_panel('Panel 4', Tabbed_title,  "Step 13.1: Verify Tabbed_title")
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=True)
        time.sleep(5)
        vfour_misobj.verify_resource_item('P292', 'S10117', "Step 13.2", item_exit=True, tree_rows="div[id^='BipContentArea'] div[id^='BidFolderBlockTree'] [class*='bi-tree-view-body-content'] td")
         
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
        portal_canvas.verify_page_in_navigation_bar('AHTML_page', "Step 16:", verify=True)
          
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
        time.sleep(15)
        portal_canvas.verify_column_panel_caption(1, 'Regional Analysis', "Step 18 : Verify first panel title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel_1_2']",frame_height_value=0)
        parent_css="#plugin"
        resobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(35)
        utillobj.switch_to_default_content(pause=5)
        element = portal_canvas.get_panel_obj('Regional Analysis')
        utillobj.take_screenshot(element, Test_Case_ID+"_Actual_step_18")
         
        """
            Step 19:Drag and Drop the Sales by Region Dashboard content into panel 2.
        """
        #Panel 2
        portal_canvas.select_panel("Panel 2")    
        item_path="Retail Samples->Documents->Sales by Region Dashboard"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 2", tx_offset=-126)
        time.sleep(2)
        portal_canvas.verify_column_panel_caption(2, 'Sales by Region Dashboard', "Step 19.1: Verify first panel title")
        utillobj.switch_to_frame(frame_css="[class*='bi-iframe'][class*='iframe'][name^='Panel_2_2']",frame_height_value=0)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody0 path[class*='riser!']"
        resobj.wait_for_property(parent_css, 7, expire_time=50)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody0",7, 'Step 19.2: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        """
            Step 20:Drag and Drop the tagCloud chart content into panel 3 .
                    Verify the report content ran inside the panel;
        """
        #Panel 3
        portal_canvas.select_panel("Panel 3")
        item_path="P292->S10117->BIP_V4_Portal->tagCloud_chart"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 3", tx_offset=-126)
        time.sleep(2)
        portal_canvas.verify_column_panel_caption(3, 'tagCloud_chart', "Step 20: Verify first panel title")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel_3_1']",frame_height_value=0)
        time.sleep(8)
        parent_css="#jschart_HOLD_0 text[class*='riser!']"
        resobj.wait_for_property(parent_css, 5, expire_time=50)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 5, 'Step 20.1: Verify number of risers displayed', custom_css="svg g>text[class^='riser!s']")   
        utillobj.switch_to_default_content(pause=3)
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
        portal_ribbon.select_tool_menu_item('menu_Save')
        
        portal_ribbon.select_tool_menu_item('menu_Exit')
        """
            Step 24:Sign Out from WebFOCUS
        """
        utillobj.switch_to_window(0)
        time.sleep(3)

        
if __name__ == '__main__':
    unittest.main()
