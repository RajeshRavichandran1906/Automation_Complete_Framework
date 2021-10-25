'''
Created on DEC 29, 2017

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157431
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229119
TestCase Name = Verify Visualization with multiple components (Workflow)
'''
import unittest, time, os, pyautogui, pywinauto
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, wf_map
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from pathlib import Path
from pywinauto.application import Application
from pyautogui import linear

class C2229119_TestClass(BaseTestCase):

    def test_C2229119(self):
        
        driver = self.driver
        driver.implicitly_wait(60)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        wfmapobj=wf_map.Wf_Map(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        from selenium.webdriver.common.keys import Keys
        Test_Case_ID='C2229119'
        
        """        
            Step 01 : Launch Report Mode:
                    http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail','P292/S10032_leaflet_1', 'mrid', 'mrpass')
       
        """        
            Step 02 : Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type('choropleth_map')
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css,1,expire_time=50)
        
        """        
            Step 03 : Double click "Store,Country", "Revenue"
        """
        metaobj.datatree_field_click("Store,Country", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g5!mregion!', color='bar_blue', msg='Step 3.1 : Verify the bar_blue color')
        expected_list=['Store Country:United Kingdom']
        resobj.verify_chart_tooltip_values(1, 'riser!s0!g41!mregion!', expected_list, text='Step 3.2 : Verify tooltip values',parent_frame_num=1)
        expected_list=['Store Country:Brazil']
        resobj.verify_chart_tooltip_values(1, 'riser!s0!g4!mregion!', expected_list, text='Step 3.3 : Verify tooltip values',parent_frame_num=1)
        
        metaobj.datatree_field_click("Revenue", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('MAINTABLE_1', 'riser!s0!g3!mregion!', color='sorbus_2', msg='Step 3.4 : Verify the sorbus_2 color')
        utillobj.verify_chart_color('MAINTABLE_1', 'riser!s0!g33!mregion!', color='elf_green', msg='Step 3.5 : Verify the elf_green color')
        expected_legand_list=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resobj.verify_riser_legends('MAINTABLE_1', expected_legand_list, msg='Step 3.6 : Verify the legand list')
        
        """        
            Step 04 : Click "Add" in the Home tab
                        Click OK in the dialog
        """
        ribbonobj.select_ribbon_item('Home', 'add_storyboard')
        time.sleep(5)
        btn_click="div[class^='bi-button button button-focus ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        time.sleep(2)
        
        """        
            Step 05 : Click "Duplicate" in the Home tab
                        Verify the map component is duplicated
        """
        ribbonobj.select_ribbon_item('Home','duplicate')
        parent_css="div[id='MAINTABLE_2']"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('MAINTABLE_2', 'riser!s0!g3!mregion!', color='sorbus_2', msg='Step 5.1 : Verify the sorbus_2 color')
        utillobj.verify_chart_color('MAINTABLE_2', 'riser!s0!g33!mregion!', color='elf_green', msg='Step 5.2 : Verify the elf_green color')
        expected_legand_list=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resobj.verify_riser_legends('MAINTABLE_2', expected_legand_list, msg='Step 5.3 : Verify the legand list')
         
        """        
            Step 06 : Click "Change" dropdown > "ESRI Bubble"
                        Verify the map is converted to bubble map
        """
        ribbonobj.change_chart_type('bubble_map')
        parent_css="div[id='MAINTABLE_2'] circle[class='riser!s0!g33!mmarker!']"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('MAINTABLE_2', 'riser!s0!g33!mmarker!', color='bar_blue', msg='Step 6.1 : Verify the bar blue color')
        expected_title_list=['Revenue']
        expected_label_list=['Revenue']
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_title_list, 'Step 6.2 : Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_label_list, msg='Step 6.3 : ', custom_css="text[class^='legend-labels']", same_group=True)
         
        """        
            Step 07 : Click "Add" in the Home tab > OK
        """
        ribbonobj.select_ribbon_item('Home', 'add_storyboard')
        time.sleep(5)
        btn_click="div[class^='bi-button button button-focus ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        time.sleep(2)
        
        """        
            Step 08 : Click "Insert" dropdown > "Chart"
        """
        ribbonobj.select_ribbon_item('Home','insert',opt='Chart')
        parent_css="div[id='TableChart_3']"
        resobj.wait_for_property(parent_css, 1, expire_time=20)
        
        """        
            Step 09 : Drag "Bar Stacked1" component above the bubble map component
                        Verify the components are rearranged
        """
        source_element= self.driver.find_element_by_xpath(VisualizationResultareaLocators.chart_type.format('Bar Stacked1'))
        source_cord=utillobj.get_object_screen_coordinate(source_element,'middle')
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody2_f div[class^='TableOfContentsButton']")
        target_cord=utillobj.get_object_screen_coordinate(target_element,'left', x_offset=-80)
        utillobj.drag_drop_on_screen(sx_offset=source_cord['x'],sy_offset=source_cord['y'],tx_offset=target_cord['x'],ty_offset=target_cord['y'])
        
         
        """        
            Step 10 : Click "Change" dropdown > "Map"
                        Select "Leaflet Choropleth" > OK
        """
        ribbonobj.change_chart_type('map')
        time.sleep(5)
        ribbonobj.select_map('choropleth', teritory='United States of America',btn_click='ok') 
        parent_css="div[id='TableChart_1']"
        resobj.wait_for_property(parent_css,1,expire_time=50)
        """"        
            Step 11 : Double click "Gross Profit"
                        Double click "Store,State,Province"
        """
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, expire_time=20)
        """
            Step 12 : Select "state_name" as Geographic Role > OK
                        Verify the map
        """
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        time.sleep(2)
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_object_visible("a[class='leaflet-control-layers-toggle']", True, msg='Step 12.1 : Verify leaflet control toggle')
        utillobj.verify_object_visible("button[class='data-selection-button leaflet-control']", True, msg='Step 12.2 : Verify pan button')
         
        expected_tooltip_list=['Store State Province:Alaska', 'Gross Profit:$1,616,022.71', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resobj.verify_default_tooltip_values('TableChart_3', 'riser!s0!g1!mstate!', expected_tooltip_list, msg='Step 12.3: Verify tooltip values')
        expected_tooltip_list=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resobj.verify_default_tooltip_values('TableChart_3', 'riser!s0!g25!mstate!', expected_tooltip_list, msg='Step 12.4 : Verify tooltip values')
         
        utillobj.verify_chart_color('TableChart_3', 'riser!s0!g1!mstate!', color='punch', msg='Step 12.5 : Verify punch color')
        utillobj.verify_chart_color('TableChart_3', 'riser!s0!g25!mstate!', color='elf_green', msg='Step 12.6 : Verify green color')
        expected_legend_list=['Gross Profit', '0M', '23M', '46.1M', '69.2M', '92.2M']
        ia_resultobj.verify_color_scale_esri_maps('TableChart_3', expected_legend_list, "Step 12.7 : Verify the lables and legends")
        """        
            Step 13 : Click "Copy" in the Home tab
                        Click "Paste"
                        Verify the map components
        """ 
        ribbonobj.select_ribbon_item('Home', 'copy')
        time.sleep(2)
        ribbonobj.select_ribbon_item('Home', 'paste')
         
        utillobj.verify_chart_color('TableChart_4', 'riser!s0!g1!mstate!', color='punch', msg='Step 13.1 : Verify punch color')
        utillobj.verify_chart_color('TableChart_4', 'riser!s0!g25!mstate!', color='elf_green', msg='Step 13.2 : Verify green color')
        expected_tooltip_list=['Store State Province:Alaska', 'Gross Profit:$1,616,022.71', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resobj.verify_default_tooltip_values('TableChart_4', 'riser!s0!g1!mstate!', expected_tooltip_list, msg='Step 13.3 : Verify tooltip values')
        expected_legend_list=['Gross Profit', '0M', '23M', '46.1M', '69.2M', '92.2M']
        ia_resultobj.verify_color_scale_esri_maps('TableChart_4', expected_legend_list, "Step 13.4 : Verify the lables and legends")
        """        
            Step 14 : Drag "ChoroplethMap3" component above "ChoroplethMap1" component
                        Verify the maps are rearranged
        """
        source_element= self.driver.find_element_by_xpath(VisualizationResultareaLocators.chart_type.format('Choropleth Map3'))
        source_cord=utillobj.get_object_screen_coordinate(source_element,'middle')
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f div[class^='TableOfContentsButton']")
        target_cord=utillobj.get_object_screen_coordinate(target_element,'left', x_offset=-80)
        utillobj.drag_drop_on_screen(sx_offset=source_cord['x'],sy_offset=source_cord['y'],tx_offset=target_cord['x'],ty_offset=target_cord['y'])
         
        """        
            Step 15 : Click "Change" dropdown > "Map"
                        Select "Leaflet Bubble" > OK
                        Verify the map is converted
        """
        ribbonobj.change_chart_type('map')
        time.sleep(5)
        ribbonobj.select_map('bubble', teritory='United States of America',btn_click='ok')
        parent_css="div[id='TableChart_1'] div[class='riser!s0!g33!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('TableChart_4', 'riser!s0!g33!mstate!', color='bar_blue', msg='Step 15.1 : verify blue color')
        expected_title_list=['Gross Profit']
        expected_label_list=['Gross Profit']
        resobj.verify_riser_pie_labels_and_legends('TableChart_4', expected_title_list, 'Step 15.2 : Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_4', expected_label_list, msg='Step 15.3 : ', custom_css="text[class^='legend-labels']", same_group=True)
         
        """        
            Step 16 : Select "BubbleMap1" component
        """
        bubble_map1_elem=driver.find_element_by_css_selector("div[id='MAINTABLE_2']")
        utillobj.default_left_click(object_locator=bubble_map1_elem)
        """        
            Step 17 : Select Format tab
                        Click "Background" dropdown > "World Street Map"
                        Verify the basemap is changed
        """  
        ribbonobj.select_ribbon_item('Format','Background')
        time.sleep(2)
         
        chart_type_css="div[id^='Base'] img[src*='streets_map']"
        chart_elem=driver.find_element_by_css_selector(chart_type_css)
        utillobj.default_left_click(object_locator=chart_elem)
        utillobj.verify_chart_color('TableChart_2', 'riser!s0!g33!mmarker!', color='bar_blue', msg='Step 17.1 : Verify the bar blue color')
        """        
            Step 18 : Select "ChoroplethMap1" component
        """ 
        choropleth_map1_elem=driver.find_element_by_css_selector("div[id='MAINTABLE_1']")
        utillobj.default_left_click(object_locator=choropleth_map1_elem)
        """        
            Step 19 : Click "Reference Layers" in the Format tab
                        Check "World Countries" > OK
                        Verify the Reference layer is drawn
        """ 
        ribbonobj.select_ribbon_item('Format', 'referencelayers')
        time.sleep(2)
        layer_list=[('World Countries',0)]
        wfmapobj.select_reference_layer(layer_list, btn_click="Ok")
        parent_css="div[id='TableChart_1'] div[class='riser!s0!g33!mregion!']"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g3!mregion!', color='sorbus_2', msg='Step 19.1 : Verify sorbus_2 color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g33!mregion!', color='elf_green', msg='Step 19.2 : Verify green color')
        expected_tooltip_list=['Store Country:United Kingdom', 'Revenue:$51,494,193.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resobj.verify_default_tooltip_values('TableChart_1', 'riser!s0!g33!mregion!', expected_tooltip_list, msg='Step 19.3 : Verify tooltip values')
        """        
            Step 20 : Click "Add" in the Home tab > OK
        """
        ribbonobj.select_ribbon_item('Home', 'add_storyboard')
        time.sleep(5)
        btn_click="div[class^='bi-button button button-focus ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        time.sleep(2)
        """        
            Step 21 : Click "Run"
                        Verify the maps are displayed correctly
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1, pause=2)
        parent_css="#Resize_MAINTABLE_2"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('Resize_MAINTABLE_1', 'riser!s0!g3!mregion!', color='sorbus_2', msg='Step 21.1 : Verify sorbus_2 color')
        utillobj.verify_chart_color('Resize_MAINTABLE_2', 'riser!s0!g33!mmarker!', color='bar_blue', msg='Step 21.2 : Verify the bar blue color')
        utillobj.verify_chart_color('Resize_MAINTABLE_3', 'riser!s0!g1!mstate!', color='punch', msg='Step 21.3 : Verify punch color')
        expected_tooltip_list=['Store State Province:Alaska', 'Gross Profit:$1,616,022.71', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resobj.verify_default_tooltip_values('Resize_MAINTABLE_3', 'riser!s0!g1!mstate!', expected_tooltip_list, msg='Step 21.4 : Verify tooltip values')
        utillobj.verify_chart_color('Resize_MAINTABLE_4', 'riser!s0!g33!mstate!', color='bar_blue', msg='Step 21.5 : Verify bar_blue color')
        """        
            Step 22 : Dismiss the run window

        """
        driver.close()
        """        
            Step 23 : Click "Save" icon
                        Enter Title "C2229119"
                        Click "Save"
        """
        utillobj.switch_to_window(0,pause=2)
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        """        
            Step 24 : Click "Show" in the Home tab
        """ 
         
        ribbonobj.select_ribbon_item('Home', 'show_storyboard')
        time.sleep(2)
        """        
            Step 25 : Download and open the PowerPoint file
                        Verify the slide are displayed correctly
        """ 
        utillobj.save_file_from_browser(Test_Case_ID + '_actual_step46.pptx')
        time.sleep(8)
        try:
            my_file= Path(os.getcwd() + "\data\\" + Test_Case_ID + "_actual_step46.pptx")
            if my_file.is_file():
                filebool=True
                os.popen(os.getcwd() + "\data\\" + Test_Case_ID + "_actual_step46.pptx")
                time.sleep(5)
           
        except FileNotFoundError:
            filebool=False
        utillobj.asequal(filebool,True,'PPTX File to compare')
        try:
            time.sleep(2)
            pyautogui.hotkey('down')
            time.sleep(2)
            pyautogui.hotkey('down')
            pyautogui.click(800, 500, clicks=1, interval=0.03, button='left', duration=0.3, tween=linear, pause=None, _pause=True)
            utillobj.zoom_powerpoint_document(100)
            time.sleep(15)
            utillobj.verify_picture_using_sikuli(Test_Case_ID+'_actual_step46.png', 'Step 25.1 : Image verification')
            app = Application().Connect(class_name='PPTFrameClass')
            app.Kill_()
            filebool=True
        except pywinauto.findwindows.ElementNotFoundError:
            filebool=False
        utillobj.asequal(filebool,True,'Powerpoint File to compare')
        """        
            Step 26 : Click "IA" > "Exit"
        """
        utillobj.switch_to_window(0)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(2)
        """        
            Step 27 : Select "No" in the Save Storyboard dialog
        """
        btn_click="div[id^='BiOptionPan'] div[class='bi-button button ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        """        
            Step 28 : Dismiss IA
        """
        utillobj.infoassist_api_logout()
        """        
            Step 29 : Reopen fex using IA API:
                        http://machine:port/alias/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2229119.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_leaflet_1', mrid='mrid', mrpass='mrpass')
        parent_css="div[id='TableChart_4'] div[class='riser!s0!g33!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        """
        Step 30: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()     