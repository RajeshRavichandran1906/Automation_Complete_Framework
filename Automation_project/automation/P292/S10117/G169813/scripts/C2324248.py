'''
Created on 28-Aug-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324248
TestCase Name = Portal Designer_Design Content : Responsive Container Percentage
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import visualization_resultarea, vfour_miscelaneous, vfour_portal_ribbon, vfour_portal_properties, vfour_portal_canvas, \
                         active_miscelaneous, vfour_portal_run, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class C2324248_TestClass(BaseTestCase):

    def test_C2324248(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        Test_Case_ID = 'C2324248'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        Portal_Name = 'BIP_Responsive'
        BIP_Portal_Path = project_id+'->'+suite_id+'->BIP_V4_Portal'
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
         
        """ Step 2: Right click on the P292 domain -> S10117 folder and choose New > Collaborative Portal
            Step 3: Enter 'BIP_Responsive' as page title
                    Maximize the portal designer window
                    Verify when Portal Designer loads you are on the Layout tab.
        """
        wf_mainpageobj.create_portal(BIP_Portal_Path, Portal_Name)
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
         
        """ Step 4: Click 1 Column template
                    Enter 'Page 1' for title and 'Page_1' for name
        """
        portal_misobj.select_page_template(page_template="1 Column", Page_title='Page 1', Page_name='Page_1', btn_name='Create')
         
        """ Step 5: Click the Theme button.
                    Verify that Neutral is the default theme. if not please choose it.
                    Verify that Neutral is the default theme.
        """
        portal_ribbon.select_or_verify_layout_base_theme(default_theme_name='Neutral', msg='Step 5.1:Verify the Neutral theme is set as default', theme_name='Neutral')
         
        """ Step 6: In the Designer Properties panel, change Width from 100% to 'Responsive'. Do not change Page Height Mode
        """
        portal_properties.select_breadcrumb_panel('BIP_Responsive')
        time.sleep(5)
        portal_properties.edit_input_control('pageview', 'Width %', 'combobox', combobox_input='Responsive')
        time.sleep(3) 
        
        """ Step 7: Click Page 1
                    Click the Insert tab and then click Responsive in the Containers group.
                    Verify that a new Responsive container called Panel 1 is inserted into the page and it takes the full screen width because 
                    it was placed on a One Column layout.
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Responsive')
        time.sleep(2)
        portal_canvas.verify_panel_caption('Panel 1', 'Step 7.1: Verify that a new Responsive container called Panel 1 is inserted into the page.')
        time.sleep(2)
        panel_width = portal_canvas.get_panel_obj('Panel 1')
        page_width = driver.find_element_by_css_selector("#BIPortalPanel [class*='bip-canvas']").size['width']
        status_h=True if int(page_width)-int(panel_width.size['width']) in range(0, 30) else False
        utillobj.asequal(True, status_h, "Step 7.2: Verify that a new Responsive container called Panel 1 it takes the full screen width.")
         
        """ Step 8: In the Designer Properties panel, change Height from 400 to 'Dynamic'.
                    Verify that the page now takes over the whole column
                    Verify that all the checkboxes are now correct based on the image
                    8200 image
        """
        portal_properties.verify_input_control('panel', 'Height', 'textbox', "Step 8: Verify Panel Height Dispalyed '400'.", textbox_value='400')
        time.sleep(2)
        portal_properties.edit_input_control('panel', 'Height', 'combobox', combobox_input='Dynamic')
        time.sleep(3)
        panel_height = portal_canvas.get_panel_obj('Panel 1')
        status_h=True if int(panel_height.size['height']) in range(0, 97) else False
        utillobj.asequal(True, status_h, "Step 8.1: Verify that a new Responsive container called Panel 1 takes Dynamic height.")
        page_width = driver.find_element_by_css_selector("#BIPortalPanel [class*='bip-canvas']").size['width']
        utillobj.asequal(page_width, 1300, 'Step 8.2: Verify that the panel now takes over the whole column.')
         
        ''' Verification of panel properties section '''
        combobox_option = {'Height':'Dynamic', 'Height Unit':'px'}
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 3
        for combo in combobox_option:
            portal_properties.verify_input_control('panel', combo, 'combobox', 
                                "Step 8."+str(count)+": Verify 'Panel 1' main Properties tab "+combo+" value "+combobox_option[combo]+".", combobox_value=combobox_option[combo])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 8."+str(count)+": Verify 'Panel 1' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 8."+str(count)+": Verify 'Panel 1' main Properties tab "+box+" value "+checkbox_option[box]+".", 
                                enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('panel', 'Responsive Properties', 'button', 
                                "Step 8."+str(count+1)+": Verify 'Panel 1' Responsive Properties  Buttons.", elem_visible=True)
         
         
        """ Step 9: Below the Designer Properties panel, click on Column 1 in the crumb trail.
                    Change the Top margin to '0' px and then click the Same for All box.
                    Verify that the panel moved yet again to remove the padding.
        """
        portal_properties.select_breadcrumb_panel('Column 1')
        time.sleep(1)
        panel_location_x = portal_canvas.get_panel_obj('Panel 1').location['x']
        portal_properties.edit_input_control('column', 'Same for All', 'checkbox', checkbox_input='Uncheck', msg="Step 9:")
        time.sleep(1)
        portal_properties.edit_input_control('column', 'Top', 'textbox', textbox_input='0')
        time.sleep(1)
        portal_properties.edit_input_control('column', 'Same for All', 'checkbox', checkbox_input='check', msg="Step 9.1")
        panel_location_x1 = portal_canvas.get_panel_obj('Panel 1').location['x']
        status_x = True if int(panel_location_x)-int(panel_location_x1) in range(0, 15) else False
        utillobj.asequal(True, status_x, "Step 9.2: Verify that the panel moved yet again to remove the padding.")
         
        """ Step 10: Press F8 to bring up the Resource Tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
         
        """ Step 11: Drag 6 reports (Sales Metrics YTD, Arc - Sales by Region, Choropleth Map - Sales by State], 
                    Stacked Bar - Units Sold by Stores vs Web (Animation), Analytical Dashboard, Regional Analysis) into that responsive container;
                    as you drag them there you will see a red outline that will let you know this is a good place to drop.
        """
        portal_canvas.select_panel('Panel 1')
        item_path="Retail Samples->Reports->Sales Metrics YTD"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Panel 1")
        time.sleep(5)
        script ='document.querySelector("#treeContainer").scrollLeft=0'
        self.driver.execute_script(script)
        item_path="Retail Samples->Charts->Arc - Sales by Region"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Sales Metrics YTD", drop_point='right')
        time.sleep(5)
        script ='document.querySelector("#treeContainer").scrollLeft=0'
        self.driver.execute_script(script)
        item_path="Retail Samples->Charts->Choropleth Map - Sales by State"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Arc - Sales by Region", drop_point='right')
        time.sleep(5)
        script ='document.querySelector("#treeContainer").scrollLeft=0'
        self.driver.execute_script(script)
        item_path="Retail Samples->Charts->Stacked Bar - Units Sold by Stores vs Web (Animation)"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Choropleth Map - Sales by State", drop_point='right')
        time.sleep(8)
        script ='document.querySelector("#treeContainer").scrollLeft=0'
        self.driver.execute_script(script)
        visualization_folder_obj=driver.find_element_by_xpath('//*[@id="treeView"]/div[2]/table/tbody/tr[39]/td/img[1]')
        visualization_folder_obj.click()
        # to expand Retail Samples->Visualizations
        item_path="Retail Samples->Visualizations->Analytical Dashboard"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Stacked Bar - Units Sold by Stores vs Web (Animation)", drop_point='right')
        time.sleep(8)
        script ='document.querySelector("#treeContainer").scrollLeft=0'
        self.driver.execute_script(script)
        item_path="Retail Samples->Documents->Regional Analysis"
        portal_canvas.dragdrop_repository_item_to_canvas(item_path, "Panel", "Analytical Dashboard", drop_point='right')
        time.sleep(15)
         
        portal_canvas.verify_panel_caption_in_responsive('Sales Metrics YTD', "Step 11: Verify 'Sales Metrics YTD' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_1']",frame_height_value=0)
        miscelanousobj.verify_page_summary('0','139of139records,Page1of6', "Step 11.1: Verify 'Sales Metrics YTD' Drag and Droped in Responsive panel.")
        utillobj.switch_to_default_content(pause=5)
         
        portal_canvas.verify_panel_caption_in_responsive('Arc - Sales by Region', "Step 11.2: Verify 'Arc - Sales by Region' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_2']",frame_height_value=0)
        resultobj.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['Oceania', 'South America', 'EMEA', 'North America'], "Step 11.3: Verify 'Arc - Sales by Region' chart label.", 
                                                      custom_css=".group-label text",same_group=True)
        utillobj.switch_to_default_content(pause=5)
         
        portal_canvas.verify_panel_caption_in_responsive('Choropleth Map - Sales by State', "Step 11.4: Verify 'Choropleth Map - Sales by State' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_3']",frame_height_value=0)
        resultobj.verify_riser_legends('jschart_HOLD_0', ['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M'], 
                                       "Step 11.5: Verify 'Choropleth Map - Sales by State' chart legends.")
        utillobj.switch_to_default_content(pause=5)
         
        portal_canvas.verify_panel_caption_in_responsive('Stacked Bar - Units Sold by Stores vs Web (Animation)', "Step 11.6: Verify 'Stacked Bar - Units Sold by Stores vs Web (Animation)' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_4']",frame_height_value=0)
        resultobj.verify_riser_legends('jschart_HOLD_0', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', '', ''], 
                                       "Step 11.7: Verify 'Stacked Bar - Units Sold by Stores vs Web (Animation)' chart legends.")
        utillobj.switch_to_default_content(pause=5)
        
        portal_canvas.verify_panel_caption_in_responsive('Analytical Dashboard', "Step 11.8: Verify 'Analytical Dashboard' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_5']",frame_height_value=0)
        resultobj.verify_riser_legends('MAINTABLE_wbody4', ['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M'], 
                                       "Step 11.9: Verify 'Analytical Dashboard' chart legends.")
        utillobj.switch_to_default_content(pause=5)
        
        element = portal_canvas.get_panel_obj_in_responsive('Regional Analysis')
        utillobj.take_screenshot(element, Test_Case_ID+"_Actual_step_11.10")
        
        element = portal_canvas.get_panel_obj('Panel 1')
        utillobj.take_screenshot(element, Test_Case_ID+"_Actual_step_11.11")
        
        
        """ Step 12: Save and exit the designer
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        time.sleep(5)
        
        """ Step 13: Run the Portal
                     Verify that all changes are present.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_Responsive', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep, string_value="Page 1", with_regular_exprestion=True)
        time.sleep(15)
        portal_run.verify_panel_caption_in_responsive('Sales Metrics YTD', "Step 13: Verify 'Sales Metrics YTD' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_1']",frame_height_value=0)
        miscelanousobj.verify_page_summary('0','139of139records,Page1of6', "Step 13.1: Verify 'Sales Metrics YTD' Drag and Droped in Responsive panel.")
        utillobj.switch_to_default_content(pause=5)
        
        portal_run.verify_panel_caption_in_responsive('Arc - Sales by Region', "Step 13.2: Verify 'Arc - Sales by Region' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_2']",frame_height_value=0)
        resultobj.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['Oceania', 'South America', 'EMEA', 'North America'], "Step 13.3: Verify 'Arc - Sales by Region' chart label.", 
                                                      custom_css=".group-label text",same_group=True)
        utillobj.switch_to_default_content(pause=5)
        
        portal_run.verify_panel_caption_in_responsive('Choropleth Map - Sales by State', "Step 13.4: Verify 'Choropleth Map - Sales by State' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_3']",frame_height_value=0)
        resultobj.verify_riser_legends('jschart_HOLD_0', ['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M'], 
                                       "Step 13.5: Verify 'Choropleth Map - Sales by State' chart legends.")
        utillobj.switch_to_default_content(pause=5)
        
        portal_run.verify_panel_caption_in_responsive('Stacked Bar - Units Sold by Stores vs Web (Animation)', "Step 13.6: Verify 'Stacked Bar - Units Sold by Stores vs Web (Animation)' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_4']",frame_height_value=0)
        resultobj.verify_riser_legends('jschart_HOLD_0', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', ''], 
                                       "Step 13.7: Verify 'Stacked Bar - Units Sold by Stores vs Web (Animation)' chart legends.")
        utillobj.switch_to_default_content(pause=5)
        
        portal_run.verify_panel_caption_in_responsive('Analytical Dashboard', "Step 13.8: Verify 'Analytical Dashboard' Drag and Droped in Responsive panel.")
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name^='Panel_1_5']",frame_height_value=0)
        resultobj.verify_riser_legends('MAINTABLE_wbody4', ['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M'], 
                                       "Step 13.9: Verify 'Analytical Dashboard' chart legends.")
        utillobj.switch_to_default_content(pause=5)
        
        analytical_panel = portal_run.get_panel_obj_in_responsive('Analytical Dashboard')
        analytical_panel_width = analytical_panel.size['width']
        
        regional_panel = portal_run.get_panel_obj_in_responsive('Regional Analysis')
        regional_panel_width = regional_panel.size['width']
        utillobj.take_screenshot(regional_panel, Test_Case_ID+"_Actual_step_13.10")
        
        element = portal_canvas.get_panel_obj('Panel 1')
        utillobj.take_screenshot(element, Test_Case_ID+"_Actual_step_13.11")
        
        """ Step 14: Shrink the portal window to make sure that the container is being resized and you can see the content. there will be a point where they will stop moving and its ok.
        """
        panel_bef = portal_canvas.get_panel_obj('Panel 1')
        panel_width_bef = panel_bef.size['width']
        driver.set_window_size(642, 990)
        time.sleep(10)
        panel_aft = portal_canvas.get_panel_obj('Panel 1')
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 500, 875, 'less_than' , "Step 14: Verify container is being resized and you can see the content.")
        elem=portal_canvas.get_panel_obj('Panel 1')
        actual_list=[el.strip().replace(' ','') for el in elem.text.strip().split('\n')]
        expected_list=['Panel1', 'SalesMetricsYTD', 'Arc-SalesbyRegion', 'ChoroplethMap-SalesbyState', 'StackedBar-UnitsSoldbyStoresvsWeb(Animation)', 'RegionalAnalysis', 'AnalyticalDashboard']
        utillobj.as_List_equal(actual_list, expected_list, "Step 14.1: Verify container is being resized and you can see the content.")
        elem=portal_canvas.get_panel_obj('Panel 1')
        utillobj.click_on_screen(elem, 'right')
        portal_canvas.scroll_panel(-10000, 0, 'down', option='autohotkey', number_of_times=100)
        elem=driver.find_element_by_css_selector("[class*='bip-page']:not([style*='hidden'])")
        utillobj.take_screenshot(elem, Test_Case_ID+"_Actual_step_14")
        driver.maximize_window()
        time.sleep(15)
        
        """ Step 15: Click Close link
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 16: Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.navigate_to_legacyhomepage()
        utillobj.synchronize_with_visble_text("#PortalResourcevBOX table tr td", workspace, resultobj.home_page_long_timesleep)
        
        """ Step 17: Edit the portal
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_Responsive', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utilobj.switch_to_new_window()
        time.sleep(25)
        
        """ Step 18: Multi select Analytical Dashboard and Regional Analysis panels
        """
        panel_temp = portal_canvas.get_panel_obj_in_responsive('Analytical Dashboard')
        panel_temp_w = panel_temp.size['width']
        panel_temp1 = portal_canvas.get_panel_obj_in_responsive('Regional Analysis')
        panel_temp_w1 = panel_temp1.size['width']
        portal_canvas.select_panel_in_responsive('Analytical Dashboard')
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
        else:
            keyboard.press('ctrl')
        portal_canvas.select_panel_in_responsive('Regional Analysis')
        if sys.platform == 'linux':
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            keyboard.release('ctrl')
        
        """ Step 19: Click on responsive Item properties button in the properties section
        """
        portal_properties.edit_input_control('panel', 'Responsive Properties', 'button')
        
        """ Step 20: Set width 300px to 440px, height from 220 to 440, max width from 350 to 620px click apply then OK
        """
        textbox_option = {'Minimum Width':'300px', 'Minimum Height':'220px', 'Maximum Width':'350px'}
        textbox_option_change = {'Minimum Width':'440px', 'Minimum Height':'440px', 'Maximum Width':'620px'}
        count = 1
        for text in textbox_option:
            portal_properties.manage_responsive_properties_popup(text, 'textbox', textbox_value=textbox_option[text], 
                                                                 msg="Step 20."+str(count)+": Verify Responsive Properties PopUp "+text+" Value is "+textbox_option[text]+" Displayed.")
            count += 1
        for opt in textbox_option_change:
            portal_properties.manage_responsive_properties_popup(opt, 'textbox', verification=False, textbox_input=textbox_option_change[opt])
            count += 1
        time.sleep(2)
        portal_properties.manage_responsive_properties_popup('Apply', 'button', verification=False)
        time.sleep(1)
        portal_properties.manage_responsive_properties_popup('OK', 'button', verification=False)
        
        time.sleep(5)
        panel_temp2 = portal_canvas.get_panel_obj_in_responsive('Analytical Dashboard')
        panel_temp_w2 = panel_temp2.size['width']
        panel_temp3 = portal_canvas.get_panel_obj_in_responsive('Regional Analysis')
        panel_temp_w3 = panel_temp3.size['width']
        portal_misobj.verify_difference(panel_temp_w, panel_temp_w2, 125, 272, 'Greater_than' , "Step 20.1: Verify 'Analytical Dashboard' is Changes took place.")
        portal_misobj.verify_difference(panel_temp_w1, panel_temp_w3, 125, 272, 'Greater_than' , "Step 20.2: Verify 'Regional Analysis' is Changes took place.")
        
        
        """ Step 21: Save and exit
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text("#PortalResourcevBOX table tr td", workspace, resultobj.home_page_long_timesleep)
        
        """ Step 22: Run the portal
                     Verify the changes took place
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->BIP_Responsive', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep, string_value="Page 1", with_regular_exprestion=True)
        time.sleep(15)
        analytical_panel = portal_run.get_panel_obj_in_responsive('Analytical Dashboard')
        analytical_panel_width1 = analytical_panel.size['width']
        
        regional_panel = portal_run.get_panel_obj_in_responsive('Regional Analysis')
        regional_panel_width1 = regional_panel.size['width']
        portal_misobj.verify_difference(analytical_panel_width, analytical_panel_width1, 125, 272, 'Greater_than' , "Step 22: Verify 'Analytical Dashboard' is Changes took place.")
        portal_misobj.verify_difference(regional_panel_width, regional_panel_width1, 125, 272, 'Greater_than' , "Step 22.1: Verify Regional Analysis' is Changes took place.")
        
        element = portal_canvas.get_panel_obj('Panel 1')
        utillobj.take_screenshot(element, Test_Case_ID+"_Actual_step_21")
        
        
        """ Step 23: Click Close link
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 24: In the banner link, click on the top right username > Click Sign Out.
        """
        time.sleep(2)
                

if __name__ == '__main__':
    unittest.main()