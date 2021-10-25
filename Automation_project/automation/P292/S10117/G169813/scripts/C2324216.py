'''
Created on 21-Sep-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324216
TestCase Name = Defaults : Defaults : Check_container_properties
'''
import unittest, time
from common.lib import utillity, core_utility
from common.pages import vfour_portal_canvas, vfour_portal_ribbon, wf_legacymainpage
from common.pages import vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324216_TestClass(BaseTestCase):

    def test_C2324216(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        proj_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        root_path = proj_id+'->'+suite_id
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
         
         
        """ Step 2: Edit 'BIP_xxx_Portal123_V4' portal from P292 domain->S10117 folder
        """
        wf_mainpageobj.select_repository_menu(root_path+'->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
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
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
         
        """ Step 3: Click the new page icon
                    Add a 4 column page to the portal
        """
        portal_canvas.add_page('4 Column')
        time.sleep(5)
         
         
        """ Step 4: In col 1 add a panel and an easy selector container (choose Retail Samples --> Portal --> Test Widget folder)
                    in col2 add an accordion container
                    in col3 add a tabbed container
                    in col4 at a responsive container.
        """
        portal_canvas.select_column(1)
        time.sleep(3)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(2)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Test Widgets', launch_point='bip_ribbon_bar', button='OK', x_scroll=10000, scroll='down')
        time.sleep(3)
        portal_canvas.select_column(2)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Accordion')
        time.sleep(3)
        portal_canvas.select_column(3)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Tabbed')
        time.sleep(3)
        portal_canvas.select_column(4)
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Responsive')
         
        """ Step 5: Add a panel, accordion, tabbed, easy selector (choose Retail Samples --> Portal --> Test Widget folder) in the responsive container.
        """
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Panel')
        time.sleep(2)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Accordion')
        time.sleep(3)
        portal_ribbon.select_ribbon_item('Insert', 'Insert_Tabbed')
        time.sleep(2)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Test Widgets', launch_point='bip_ribbon_bar', button='OK')
         
        """ Step 6: Click Col 2 and check the easy selector box in the properties section then choose test widget folder.
        """
        portal_canvas.select_column(2)
        time.sleep(2)
        portal_canvas.select_easy_selector_path('Retail Samples->Portal->Test Widgets', launch_point='property_tab', button='OK', 
                                                section='column', item_name='Show Easy Selector', control='checkbox', checkbox_input='check', msg='Step 6:')
        time.sleep(3)
        """ Step 7: Click Panel 1
                    Verify the main properties tab (bip-3372)
        """
        portal_canvas.select_panel('Panel 1')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        textbox_option = {'Height':'400'}
        combobox_option = {'Height unit':'px'}
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 7."+str(count)+": Verify 'Panel 1' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for combo in combobox_option:
            portal_properties.verify_input_control('panel', combo, 'combobox', 
                                "Step 7."+str(count)+": Verify 'Panel 1' main Properties tab "+combo+" value "+combobox_option[combo]+".", combobox_value=combobox_option[combo])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 7."+str(count)+": Verify 'Panel 1' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 7."+str(count)+": Verify 'Panel 1' main Properties tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 8: Click the title tab
        """
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        textbox_option = {'Panel Title':'Panel 1'}
        checkbox_option = {'Panel Icons':'uncheck', 'Hide Title Bar':'uncheck', 'Show Menu Icons':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 8."+str(count)+": Verify 'Panel 1' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 8."+str(count)+": Verify 'Panel 1' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Change Image', 'button', 
                                "Step 8."+str(count)+": Verify 'Panel 1' Title tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 9: Enter panel 1 testing in the Panel title entry box
                    Verify that the panel title has changed.
        """
        portal_properties.edit_input_control('panel', 'Panel Title', 'textbox', textbox_input='Panel 1 testing')
        time.sleep(2)
        portal_canvas.verify_column_panel_caption(1, 'Panel 1 testing', "Step 9: Verify that the 'Panel 1' title has changed 'panel 1 testing'.")
        time.sleep(1)
         
        """ Step 10: Click the content tab
        """
        portal_properties.select_property_tab('Content')
        time.sleep(2)
        textbox_option = {'Content Area':'Panel_1_1', 'Auto Refresh':'30'}
        checkbox_option = {'Auto Refresh':'uncheck', 'Dynamic Report Styling':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 10."+str(count)+": Verify 'Panel 1' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 10."+str(count)+": Verify 'Panel 1' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
         
         
        """ Step 11: Click Panel 2 --> properties tab
        """
        portal_canvas.select_panel('Panel 2')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        textbox_option = {'Height':'400'}
        combobox_option = {'Height Unit':'px'}
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 11."+str(count)+": Verify 'Panel 2' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for combo in combobox_option:
            portal_properties.verify_input_control('panel', combo, 'combobox', 
                                "Step 11."+str(count)+": Verify 'Panel 2' main Properties tab "+combo+" value "+combobox_option[combo]+".", combobox_value=combobox_option[combo])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 11."+str(count)+": Verify 'Panel 2' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 11."+str(count)+": Verify 'Panel 2' main Properties tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
         
        """ Step 12: Click the title tab
        """ 
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        textbox_option = {'Easy Selector Title':'Panel 2'}
        checkbox_option = {'Panel Icons':'uncheck', 'Hide Title Bar':'uncheck', 'Show Menu Icons':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 12."+str(count)+": Verify 'Panel 2' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 12."+str(count)+": Verify 'Panel 2' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Change Image', 'button', 
                                "Step 12."+str(count)+": Verify 'Panel 2' Title tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
         
         
        """ Step 13: Enter Panel 2 testing in the Panel title entry box
                     Verify that the panel title has changed.
        """
        portal_properties.edit_input_control('panel', 'Easy Selector Title', 'textbox', textbox_input='Panel 2 testing')
        time.sleep(2)
        portal_canvas.verify_column_panel_caption(1, 'Panel 2 testing', "Step 13: Verify that the 'Panel 2' title has changed 'Panel 2 testing'.")
        time.sleep(1)
         
         
         
        """ Step 14: Click the content tab
        """
        portal_properties.select_property_tab('Content')
        time.sleep(2)
        textbox_option = {'Easy Selector':'Panel_2_1', 'Easy Selector Auto Refresh':'30'}
        checkbox_option = {'Auto Refresh':'uncheck', 'Dynamic Report Styling':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 14."+str(count)+": Verify 'Panel 2' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 14."+str(count)+": Verify 'Panel 2' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
         
         
        """ Step 15: Click panel 3 --> Properties tab
        """
        portal_canvas.select_panel('Panel 2 testing')
        time.sleep(3)
        portal_canvas.scroll_panel(0, 0, 'up', option='uiautomation', number_of_times=90)
        portal_canvas.select_panel('Panel 3')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        textbox_option = {'Height':'400'}
        combobox_option = {'Height Unit':'px'}
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 15."+str(count)+": Verify 'Panel 3' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for combo in combobox_option:
            portal_properties.verify_input_control('panel', combo, 'combobox', 
                                "Step 15."+str(count)+": Verify 'Panel 3' main Properties tab "+combo+" value "+combobox_option[combo]+".", combobox_value=combobox_option[combo])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 15."+str(count)+": Verify 'Panel 3' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 15."+str(count)+": Verify 'Panel 3' main Properties tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 16: Click the title tab
        """
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        textbox_option = {'Accordion Title':'Panel 3'}
        checkbox_option = {'Panel Icons':'uncheck', 'Hide Title Bar':'uncheck', 'Show Menu Icons':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 16."+str(count)+": Verify 'Panel 3' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 16."+str(count)+": Verify 'Panel 3' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Change Image', 'button', 
                                "Step 16."+str(count)+": Verify 'Panel 2' Title tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 17: Enter panel 3 testing in the Panel title entry box
                     Verify that the panel title has changed.
        """
        portal_properties.edit_input_control('panel', 'Accordion Title', 'textbox', textbox_input='Panel 3 testing')
        time.sleep(2)
        portal_canvas.verify_column_panel_caption(2, 'Panel 3 testing', "Step 17: Verify that the 'Panel 3' title has changed 'Panel 3 testing'.")
        time.sleep(1)
         
        """ Step 18: Click the content tab
        """
        portal_properties.select_property_tab('Content')
        time.sleep(2)
        textbox_option = {'Content Area':'Area_1_1', 'Auto Refresh':'30'}
        checkbox_option = {'Auto Refresh':'uncheck', 'Dynamic Report Styling':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 18."+str(count)+": Verify 'Panel 3' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 18."+str(count)+": Verify 'Panel 3' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
         
        """ Step 19: Click the areas tab
        """
        portal_properties.select_property_tab('Areas')
        time.sleep(2)
        portal_properties.verify_input_control('panel', 'Hide New Area', 'checkbox', 
                                "Step 19: Verify 'Panel 3' Title tab Hide New Area value Uncheck.", checkbox_input='uncheck')
        portal_properties.verify_input_control('panel', 'Area:', 'panel_area', 
                                "Step 19.1: Verify 'Panel 3' Areas value Area 1.", area_list=['Area 1'])
             
        """ Step 20: Click panel 4 -->properties tab
        """
        portal_canvas.select_panel('Panel 4')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        textbox_option = {'Height':'400'}
        combobox_option = {'Height Unit':'px'}
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 20."+str(count)+": Verify 'Panel 4' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for combo in combobox_option:
            portal_properties.verify_input_control('panel', combo, 'combobox', 
                                "Step 20."+str(count)+": Verify 'Panel 4' main Properties tab "+combo+" value "+combobox_option[combo]+".", combobox_value=combobox_option[combo])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 20."+str(count)+": Verify 'Panel 4' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 20."+str(count)+": Verify 'Panel 4' main Properties tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 21: Click the title tab
        """
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        textbox_option = {'Tab Title':'Panel 4'}
        checkbox_option = {'Panel Icons':'uncheck', 'Hide Title Bar':'uncheck', 'Show Menu Icons':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 21."+str(count)+": Verify 'Panel 4' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 21."+str(count)+": Verify 'Panel 4' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Change Image', 'button', 
                                "Step 21."+str(count)+": Verify 'Panel 4' Title tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 22: Enter panel 4 testing in the Panel title entry box
                     Verify that the panel title has changed.
        """
        portal_properties.edit_input_control('panel', 'Tab Title', 'textbox', textbox_input='Panel 4 testing')
        time.sleep(2)
        portal_canvas.verify_column_panel_caption(3, 'Panel 4 testing', "Step 17: Verify that the 'Panel 4' title has changed 'Panel 4 testing'.")
        time.sleep(1)
         
        """ Step 23: Click the content tab
        """
        portal_properties.select_property_tab('Content')
        time.sleep(2)
        textbox_option = {'Content Area':'Tab_1_1', 'Auto Refresh':'30'}
        checkbox_option = {'Auto Refresh':'uncheck', 'Dynamic Report Styling':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 23."+str(count)+": Verify 'Panel 4' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 23."+str(count)+": Verify 'Panel 4' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
         
        """ Step 24: Click the tabs tab
        """
        portal_properties.select_property_tab('Tabs')
        time.sleep(2)
        portal_properties.verify_input_control('panel', 'Buttons', 'button', 
                                "Step 24: Verify 'Panel 4' tabs tab Buttons.", elem_visible=True)
        portal_properties.verify_input_control('panel', 'Hide New Tab', 'checkbox', 
                                "Step 24.1: Verify 'Panel 4' Title tab Hide New Tab value Uncheck.", checkbox_input='uncheck')
        portal_properties.verify_input_control('panel', 'Area:', 'panel_area', 
                                "Step 24.2: Verify 'Panel 4' Areas value Area 1.", area_list=['Tab 1'])
        
        time.sleep(1)
         
        """ Step 25: Click panel 5 -->properties tab
        """
        portal_canvas.select_panel('Panel 5')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        textbox_option = {'Height':'400'}
        combobox_option = {'Height Unit':'px'}
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 25."+str(count)+": Verify 'Panel 5' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for combo in combobox_option:
            portal_properties.verify_input_control('panel', combo, 'combobox', 
                                "Step 25."+str(count)+": Verify 'Panel 5' main Properties tab "+combo+" value "+combobox_option[combo]+".", combobox_value=combobox_option[combo])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 25."+str(count)+": Verify 'Panel 5' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 25."+str(count)+": Verify 'Panel 5' main Properties tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('panel', 'Responsive Properties', 'button', 
                                "Step 24."+str(count+1)+": Verify 'Panel 5' Responsive Properties  Buttons.", elem_visible=True)
        
        """ Step 26: Click the title tab
        """
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        textbox_option = {'Responsive title':'Panel 5'}
        checkbox_option = {'Panel Icons':'uncheck', 'Hide Title Bar':'uncheck', 'Show Menu Icons':'check'}
        count = 1
        for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 26."+str(count)+": Verify 'Panel 5' Title tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 26."+str(count)+": Verify 'Panel 5' Title tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Change Image', 'button', 
                                "Step 26."+str(count)+": Verify 'Panel 5' Title tab "+box+" value "+checkbox_option[box]+".", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 27: Enter panel 5 testing in the Panel title entry box
                     Verify that the panel title has changed.
        """
        portal_properties.edit_input_control('panel', 'Responsive title', 'textbox', textbox_input='Panel 5 testing')
        time.sleep(2)
        portal_canvas.verify_column_panel_caption(4, 'Panel 5 testing', "Step 27: Verify that the 'Panel 5' title has changed 'Panel 5 testing'.")
        time.sleep(1)
         
        """ Step 28: Click the content tab
        """
        portal_properties.select_property_tab('Content')
        time.sleep(2)
        portal_properties.verify_input_control('panel', 'Responsive Panel', 'text', 
                                "Step 28: Verify 'Panel 5' Responsive Panel.", text_list=['Responsive Panel'])
        
         
        """ Step 29: Click on all the panels inside the responsive container
                     Verify that the properties are all the same as the ones in this test other then the main section of the properties tab will have
                      a Responsive Properties button.
        """
        portal_canvas.select_panel('Panel 6')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        '''for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 29."+str(count)+": Verify 'Panel 6' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1'''
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 29."+str(count)+": Verify 'Panel 6' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 29."+str(count)+": Verify 'Panel 6' main Properties tab Freeze Container value uncheck.", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control_enable_or_disable('panel', 'Hide', 'checkbox', 
                                "Step 29."+str(count+1)+": Verify 'Panel 6' main Properties tab Hide value Uncheck.", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('panel', 'Responsive Properties', 'button', 
                                "Step 29."+str(count+1)+": Verify 'Panel 6' Responsive Properties  Buttons.", elem_visible=True)
       
        """ Step 30: Verify panel 7 properties 
        """
        portal_canvas.select_panel('Panel 6')
        time.sleep(0.5)
        portal_canvas.scroll_panel(1388, 0, 'down')
        time.sleep(2)
        portal_canvas.select_panel('Panel 7')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        '''for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 30."+str(count)+": Verify 'Panel 7' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1'''
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 30."+str(count)+": Verify 'Panel 7' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 30."+str(count)+": Verify 'Panel 7' main Properties tab Freeze Container value uncheck.", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control_enable_or_disable('panel', 'Hide', 'checkbox', 
                                "Step 30."+str(count+1)+": Verify 'Panel 7' main Properties tab Hide value Uncheck.", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('panel', 'Responsive Properties', 'button', 
                                "Step 30."+str(count+1)+": Verify 'Panel 7' Responsive Properties  Buttons.", elem_visible=True)
        
        """ Step 31: Verify Panel 8 properites
        """
        portal_canvas.select_panel('Panel 7')
        time.sleep(0.5)
        portal_canvas.scroll_panel(1388, 0, 'down')
        time.sleep(2)
        portal_canvas.select_panel('Panel 8')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        '''for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 31."+str(count)+": Verify 'Panel 8' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1'''
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 31."+str(count)+": Verify 'Panel 8' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 31."+str(count)+": Verify 'Panel 8' main Properties tab Freeze Container value uncheck.", enable_status='disabled', enable_value=True,color_name='silver')
        portal_properties.verify_input_control_enable_or_disable('panel', 'Hide', 'checkbox', 
                                "Step 31."+str(count+1)+": Verify 'Panel 8' main Properties tab Hide value Uncheck.", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('panel', 'Responsive Properties', 'button', 
                                "Step 31."+str(count+1)+": Verify 'Panel 8' Responsive Properties  Buttons.", elem_visible=True)
        
        """ Step 32: Verify Panel 9 properites
        """
        portal_canvas.select_panel('Panel 8')
        time.sleep(0.5)
        portal_canvas.scroll_panel(1388, 0, 'down')
        time.sleep(2)
        portal_canvas.select_panel('Panel 9')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(2)
        checkbox_option = {'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check', 'Refresh':'check', 'Hide':'uncheck', 
                           'Delete':'check', 'Show Comments':'uncheck', 'Freeze Container':'uncheck', 'Hide Panel':'uncheck'}
        count = 1
        '''for text in textbox_option:
            portal_properties.verify_input_control('panel', text, 'textbox', 
                                "Step 32."+str(count)+": Verify 'Panel 9' main Properties tab "+text+" value "+textbox_option[text]+".", textbox_value=textbox_option[text])
            count += 1'''
        for box in checkbox_option:
            portal_properties.verify_input_control('panel', box, 'checkbox', 
                                "Step 32."+str(count)+": Verify 'Panel 9' main Properties tab "+box+" value "+checkbox_option[box]+".", checkbox_input=checkbox_option[box])
            count += 1
        portal_properties.verify_input_control_enable_or_disable('panel', 'Freeze Container', 'checkbox', 
                                "Step 32."+str(count)+": Verify 'Panel 9' main Properties tab Freeze Container value uncheck.", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control_enable_or_disable('panel', 'Hide', 'checkbox', 
                                "Step 32."+str(count+1)+": Verify 'Panel 9' main Properties tab Hide value Uncheck.", enable_status='disabled', enable_value=True, color_name='silver')
        portal_properties.verify_input_control('panel', 'Responsive Properties', 'button', 
                                "Step 32."+str(count+1)+": Verify 'Panel 9' Responsive Properties  Buttons.", elem_visible=True)
               
        """ Step 33: Right click and delete the page.
                     Verify that the page is gone
        """
        portal_canvas.manage_page_menu('4 Column', 'Remove')
        
        """ Step 34: Exit portal without saving
        """
        portal_ribbon.bip_save_and_exit('No')
        time.sleep(3)
        core_utilobj.switch_to_previous_window(window_close=False)
        
        """ Step 35: Sign Out from WebFOCUS
        """
        time.sleep(5)
        

if __name__ == '__main__':
    unittest.main()