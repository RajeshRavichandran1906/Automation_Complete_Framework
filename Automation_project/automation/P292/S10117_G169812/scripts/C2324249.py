'''
Created on 08-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324249
TestCase Name = Portal Designer_Design Content : Responsive_Magic_Filter
'''
import unittest, time, keyboard
from common.lib import utillity
from common.pages import visualization_resultarea, vfour_miscelaneous, wf_mainpage, vfour_portal_ribbon, vfour_portal_properties, vfour_portal_canvas, \
                         vfour_portal_run, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324249_TestClass(BaseTestCase):

    def test_C2324249(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324249'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 2: Expand P292 domain ->S10117 folder,
                    Right Click on 'BIP_Responsive' portal and choose Edit
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_Responsive', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
         
        """ Step 3: Maximize the portal designer window
        """
        utillobj.switch_to_window(1)
        time.sleep(2)
         
        """ Step 4: Click Insert then new page
                    Choose the 4 x 2 responsive template
        """
        """ Step 5: Change the title to 'Responsive Magic Filter testing page'
        """
        portal_canvas.add_page('Responsive 4-2',Page_title='Responsive Magic Filter testing page')
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('Responsive Magic Filter testing page', "Step 5: Verify 'Responsive Magic Filter testing page' added.")
        time.sleep(1)
        portal_canvas.select_panel('Add Content')
        time.sleep(1)
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Panel Title', 'textbox', textbox_input='Panel 2')
        time.sleep(1)
        portal_canvas.select_panel('Add Content')
        time.sleep(1)
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Panel Title', 'textbox', textbox_input='Panel 3')
        time.sleep(1)
        portal_canvas.select_panel('Add Content')
        time.sleep(1)
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Panel Title', 'textbox', textbox_input='Panel 4')
        time.sleep(1)
        portal_canvas.select_panel('Add Content')
        time.sleep(1)
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Panel Title', 'textbox', textbox_input='Panel 5')
        time.sleep(1)
        portal_canvas.select_panel('Add Content')
        time.sleep(1)
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Panel Title', 'textbox', textbox_input='Panel 6')
        time.sleep(1)
        portal_canvas.select_panel('Add Content')
        time.sleep(1)
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Panel Title', 'textbox', textbox_input='Panel 7')
          
        """ Step 6: Below the Designer Properties panel, click on Column 1 in the crumb trail.
                    Verify Top margin is set to 5px and then the Same for All box is checked.
        """
        portal_properties.select_breadcrumb_panel('Column 1')
        time.sleep(2)
        portal_properties.verify_input_control('column', 'Top', 'textbox', "Step 6: Verify Top is set to 5px.", textbox_value='5')
        portal_properties.verify_input_control('column', 'Same for All', 'checkbox', 'Step 6.1: Verify Same for All box is checked.', checkbox_input='check')
        portal_canvas.select_panel('Panel 6')
        time.sleep(1)
        portal_canvas.scroll_panel(0, 0, 'up', option='autohotkey', number_of_times=70)
          
        """ Step 7: Multi select four content panels in the first row then click on Responsive Properties button
                    Verify that bip-container bip-responsive-4-2-1 is set
        """
        portal_canvas.select_panel_in_responsive('Panel 2')
        keyboard.press('ctrl')
        portal_canvas.select_panel_in_responsive('Panel 3')
        portal_canvas.select_panel_in_responsive('Panel 4')
        portal_canvas.select_panel_in_responsive('Panel 5')
        keyboard.release('ctrl')
        time.sleep(2)
        portal_properties.select_property_tab('Properties')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Responsive Properties', 'button')
        time.sleep(1)
        portal_properties.manage_responsive_properties_popup('Custom CSS Classes', 'textbox', textbox_value='bip-container bip-responsive-4-2-1 ', 
                                                             msg="Step 7: Verify that 'bip-container bip-responsive-4-2-1' is set")
        portal_properties.manage_responsive_properties_popup('Cancel', 'button', verification=False)
          
        """ Step 8: Multi select two content panels in the second row
                    Click responsive properties button
                    Verify that bip-container bip-responsive-2-1 is set
        """
        portal_canvas.select_panel_in_responsive('Panel 6')
        keyboard.press('ctrl')
        portal_canvas.select_panel_in_responsive('Panel 7')
        keyboard.release('ctrl')
        time.sleep(2)
        portal_properties.edit_input_control('panel', 'Responsive Properties', 'button')
        time.sleep(1)
        portal_properties.manage_responsive_properties_popup('Custom CSS Classes', 'textbox', textbox_value='bip-container bip-responsive-2-1 ', 
                                                             msg="Step 8: Verify that 'bip-container bip-responsive-2-1' is set")
        portal_properties.manage_responsive_properties_popup('Cancel', 'button', verification=False)
          
        """ Step 9: Select BIP_Responsive > Pages > Responsive Magic Filter testing page > Column 1 > Panel 1 under breadcrumbs
                    Verify height is Dynamic.
        """
        time.sleep(1)
        portal_properties.select_breadcrumb_panel('BIP_Responsive')
        time.sleep(1)
        portal_properties.select_breadcrumb_panel('BIP_Responsive', next='Pages')
        time.sleep(1)
        portal_properties.select_breadcrumb_panel('Pages', next='Responsive Magic Filter testing page')
        time.sleep(1)
        portal_properties.select_breadcrumb_panel('Responsive Magic Filter testing page', next='Column 1')
        time.sleep(1)
        portal_properties.select_breadcrumb_panel('Column 1', next='Panel 1')
        time.sleep(1)
        portal_properties.verify_input_control('panel', 'Height', 'textbox', 'Step 9: Verify height is Dynamic.', textbox_value='Dynamic')
          
        """ Step 10: Verify that the title bar is not there for panel 1
        """
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.verify_input_control('panel', 'Hide Title Bar', 'checkbox', 'Step 10: Verify that the hide title bar is checked.', checkbox_input='check')
        time.sleep(1)
        portal_canvas.select_panel_in_responsive('Panel 6')
        time.sleep(1)
        portal_canvas.scroll_panel(0, 0, 'up', option='autohotkey', number_of_times=70)
          
        """ Step 11: Press F8 to bring up the Resource Tree
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
          
        """ Step 12: Open Retail Samples domain
                     Open the portals folder
        """
        """ Step 13: Drag 6 reports (Caterory Sales, Regional Sales Trend, Stores Sales by region, Units profit treemap, accordion datatable,
                     freeze data table) into that responsive container; as you drag them there you will see a blue outline that will let you know 
                     this is a good place to drop.
                     Drag Standard autofit off over accordion data table to add another tab
                     Drag Standard autofit on over freeze data table to add another tab
        """
        item_path="Retail Samples->Portal->Small Widgets->Category Sales"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Panel 2")
        time.sleep(2)
        item_path="Retail Samples->Portal->Small Widgets->Regional Sales Trend"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Panel 3")
        time.sleep(2)
        item_path="Retail Samples->Portal->Large Widgets->Store Sales by Region"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Panel 4")
        time.sleep(2)
        item_path="Retail Samples->Portal->Large Widgets->Units Profit Treemap"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Panel 5")
        time.sleep(2)
        portal_canvas.select_panel_in_responsive('Panel 6')
        item_path="Retail Samples->Portal->Responsive Tables->Accordion DataTable"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Panel 6")
        time.sleep(2)
        portal_canvas.select_panel_in_responsive('Panel 7')
        item_path="Retail Samples->Portal->Responsive Tables->Freeze DataTable"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Panel 7")
        time.sleep(2)
        item_path="Retail Samples->Portal->Responsive Tables->Standard Autofit Off"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Accordion DataTable")
        utillobj.select_or_verify_bipop_menu('Add As Tab', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden'])")
        time.sleep(9)
        portal_canvas.verify_tabbed_panel_in_responsive('Accordion DataTable', ['Accordion DataTable', 'Standard Autofit Off', 'New Tab'], "Step 13: Verify Standard Autofit Off added on another tab.")
        item_path="Retail Samples->Portal->Responsive Tables->Standard Autofit On"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Freeze DataTable")
        utillobj.select_or_verify_bipop_menu('Add As Tab', custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden'])")
        time.sleep(9)
        portal_canvas.verify_tabbed_panel_in_responsive('Freeze DataTable', ['Freeze DataTable', 'Standard Autofit On', 'New Tab'], "Step 13.1: Verify Standard Autofit Off added on another tab.")
        time.sleep(1)
        portal_canvas.select_panel_in_responsive('Accordion DataTable')
        time.sleep(1)
        portal_canvas.scroll_panel(0, 0, 'up', option='autohotkey', number_of_times=70)
        
        """ Step 14: Drag Retail Sales Filter panel to the left of Category sales panel
        """
        item_path="Retail Samples->Portal->Retail Sales Filter Panel"
        portal_canvas.dragdrop_repository_item_to_responsive(item_path, "Panel", "Category Sales", drop_point='left', tx_offset=5)
        time.sleep(5)
         
        """ Step 15: Click on responsive properties button
                     Add bip-responsive-1 and change the height to 64px then click OK
        """
        portal_properties.edit_input_control('panel', 'Responsive Properties', 'button')
        time.sleep(1)
        portal_properties.manage_responsive_properties_popup('Custom CSS Classes', 'textbox', verification=False, textbox_input='bip-container bip-responsive-1')
        portal_properties.manage_responsive_properties_popup('Height', 'textbox', verification=False, textbox_input='64px')
        time.sleep(1)
        portal_properties.manage_responsive_properties_popup('OK', 'button', verification=False)
         
        """ Step 16: Hide the title bar of that panel
        """
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Hide Title Bar', 'checkbox', checkbox_input='check', msg='Step 16')
         
        """ Step 17: Click the save button.
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord',display_status=False)
        time.sleep(2)
        portal_ribbon.select_tool_menu_item('menu_Save')
         
        """ Step 18: Shrink the portal window to make sure that the container is being resized and you can see the content. 
                     there will be a point where they will stop moving and its ok.
                     Verify that the top 4 will only be displayed as 4 in a row or 2 in a row.
                     the bottom 2 as 2 in a row or 1 on top of the other.
        """
        panel_bef=portal_canvas.get_column_obj(1)
        panel_width_bef = panel_bef.size['width']
        driver.set_window_size(642, 990)
        time.sleep(10)
        panel_aft = portal_canvas.get_column_obj(1)
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 700, 1072, 'less_than' , "Step 18: Verify container is being resized and you can see the content.")
        elem=portal_canvas.get_column_obj(1)
        actual_list=[el.strip().replace(' ','').replace(':','') for el in elem.text.strip().split('\n')]
        expected_list=['To', 'From', 'BusinessRegion', 'ALL', 'EMEA', 'NorthAmerica', 'Oceania', 'SouthAmerica', 'ProductCategory', 'ALL', 'StoreType', 'Store', 'Web', 'ALL', 'CategorySales', 'RegionalSalesTrend', 'StoreSalesbyRegion', 'UnitsProfitTreemap', 'AccordionDataTable', 'AccordionDataTable', 'StandardAutofitOff', 'NewTab', 'FreezeDataTable']
        status_=False
        for text in expected_list:
            if text in actual_list:
                status_=True
            else:
                status_=False
                break
        utillobj.asequal(status_, True, "Step 18.1: Verify container is being resized and you can see the content.")
        elem=portal_canvas.get_column_obj(1)
        utillobj.click_on_screen(elem, 'right')
        portal_canvas.scroll_panel(-10000, 0, 'down', option='autohotkey', number_of_times=110)
        elem=driver.find_element_by_css_selector("[class*='bip-page']:not([style*='hidden'])")
        utillobj.take_screenshot(elem, Test_Case_ID+"_Actual_step_18")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(15)
          
        """ Step 19: Exit the designer
        """
        portal_ribbon.select_tool_menu_item('menu_Exit')
        utillobj.switch_to_window(0, pause=5)
        time.sleep(5)
         
        """ Step 20: Run the portal
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_Responsive', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
         
        """ Step 21: Shrink the portal window to make sure that the container is being resized and you can see the content. there will be a point where they will stop moving and its ok.
                     Verify that the top 4 will only be displayed as 4 in a row or 2 in a row.
                     the bottom 2 as 2 in a row or 1 on top of the other.
        """
        panel_bef=portal_canvas.get_column_obj(1)
        panel_width_bef = panel_bef.size['width']
        driver.set_window_size(642, 990)
        time.sleep(10)
        panel_aft = portal_canvas.get_column_obj(1)
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 700, 1072, 'less_than' , "Step 21: Verify container is being resized and you can see the content.")
        elem=portal_canvas.get_column_obj(1)
        actual_list=elem.text.strip().split('\n')
        expected_list=['To:', 'From:', 'Business Region:', 'ALL', 'EMEA', 'North America', 'Oceania', 'South America', 'Product Category:', 'ALL', 'Store Type:', 'Store', 'Web', 'ALL', 'Category Sales', ' Regional Sales Trend', ' Store Sales by Region', ' Units Profit Treemap', ' Accordion DataTable', ' Accordion DataTable', ' Standard Autofit Off', ' Freeze DataTable', ' Freeze DataTable', ' Standard Autofit On']
        utillobj.as_List_equal(actual_list, expected_list, "Step 21.1: Verify container is being resized and you can see the content.")
        elem=portal_canvas.get_column_obj(1)
        utillobj.click_on_screen(elem, 'right')
        portal_canvas.scroll_panel(-10000, 0, 'down', option='autohotkey', number_of_times=110)
        elem=driver.find_element_by_css_selector("[class*='bip-page']:not([style*='hidden'])")
        utillobj.take_screenshot(elem, Test_Case_ID+"_Actual_step_21")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(9)
        elem=portal_canvas.get_column_obj(1)
        utillobj.click_on_screen(elem, 'right')
        portal_canvas.scroll_panel(-10000, 0, 'up', option='autohotkey', number_of_times=110)
         
        """ Step 22: In the filter panel
                     Chose EMEA in the business region section
                     Verify that all the panels have change their outputs
        """
        elem=driver.find_element_by_css_selector("[id*='hc_panel1'] [id*='hc_combobox1']")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        driver.find_element_by_xpath("//select/option[@value='EMEA']").click()
        time.sleep(15)
        ''' Verify Category Sales panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_2_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 .chartPanel text[class^='totalLabel!g0!mtotalLabel!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        resultobj.verify_data_labels('jschart_HOLD_0', ['422.7M'], "Step 22: Verify Data label in Category Sales.", custom_css=".chartPanel text[class^='totalLabel!g0!mtotalLabel!']")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Regional Sales Trend panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_3_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 g.chartPanel text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        expected_xlist = ['1','2','3','4','5','6','7','8','9','10','11','12']
        expected_ylist = ['0','10M','20M','30M','40M','50M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xlist, expected_ylist, "Step 22.1: Verify Regional Sales Trend. xy labels")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Store Sales by Region panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_4_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 svg rect[class*='legend-background']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        legend=['Store Business Region', 'EMEA', 'Revenue', '31.8M', '0M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 22.2: Verify Store Sales by Region legends")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Units Profit Treemap '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_5_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 svg text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        legend=['Gross Profit', '0.2M', '5.3M', '10.5M', '15.6M', '20.8M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 22.3: Verify  Units Profit Treemap legends")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Accordion DataTable panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_6_1']",frame_height_value=0)
        parent_css="#DataTables_Table_0"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
#         portal_run.create_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds01.xlsx')
        portal_run.verify_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds01.xlsx', "Step 22.4: Accordion DataTable verification ")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Freeze DataTable panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_7_1']",frame_height_value=0)
        parent_css="#DataTables_Table_0"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
#         portal_run.create_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds02.xlsx')
        portal_run.verify_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds02.xlsx', "Step 22.5: Freeze DataTable verification ")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
         
        """ Step 23: Choose Accessories in the product category area
                     Verify that all the panels have change their outputs
        """
        elem=driver.find_element_by_css_selector("[id*='hc_panel3'] [id*='hc_combobox2']")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        driver.find_element_by_css_selector("[class*='ui-dialog'][id*='hc_combobox2'] label input[id*='hc_combobox2_1']").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div[class*='ui-dialog'] button[class*='ui-dialog-titlebar']").click()
        time.sleep(15)
         
        ''' Verify Category Sales panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_2_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 .chartPanel text[class^='totalLabel!g0!mtotalLabel!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        resultobj.verify_data_labels('jschart_HOLD_0', ['51.8M'], "Step 23: Verify Data label in Category Sales.", custom_css=".chartPanel text[class^='totalLabel!g0!mtotalLabel!']")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Regional Sales Trend panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_3_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 g.chartPanel text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        expected_xlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_ylist = ['0', '1M', '2M', '3M', '4M', '5M', '6M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xlist, expected_ylist, "Step 23.1: Verify Regional Sales Trend. xy labels")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Store Sales by Region panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_4_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 svg rect[class*='legend-background']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        legend=['Store Business Region', 'EMEA', 'Revenue', '3.8M', '0M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 23.2: Verify Store Sales by Region legends")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Units Profit Treemap '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_5_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 svg text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        legend=['Gross Profit', '0.8M', '3M', '5.3M', '7.5M', '9.8M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 23.3: Verify  Units Profit Treemap legends")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Accordion DataTable panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_6_1']",frame_height_value=0)
        parent_css="#DataTables_Table_0"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
#         portal_run.create_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds03.xlsx')
        portal_run.verify_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds03.xlsx', "Step 23.4: Accordion DataTable verification ")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Freeze DataTable panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_7_1']",frame_height_value=0)
        parent_css="#DataTables_Table_0"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
#         portal_run.create_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds04.xlsx')
        portal_run.verify_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds04.xlsx', "Step 23.5: Freeze DataTable verification ")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
         
        """ Step 24: Close the portal and rerun it.
                     Verify that no customizations have been saved and all the reports go back to their default settings.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(5)
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_Responsive', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(9)
         
        ''' Verify Category Sales panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_2_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 .chartPanel text[class^='totalLabel!g0!mtotalLabel!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        resultobj.verify_data_labels('jschart_HOLD_0', ['1.1B'], "Step 24: Verify Data label in Category Sales.", custom_css=".chartPanel text[class^='totalLabel!g0!mtotalLabel!']")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Regional Sales Trend panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_3_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 g.chartPanel text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        expected_xlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_ylist = ['0', '14M', '28M', '42M', '56M', '70M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xlist, expected_ylist, "Step 24.1: Verify Regional Sales Trend. xy labels")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Store Sales by Region panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_4_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 svg rect[class*='legend-background']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        legend=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America', 'Revenue', '327.8M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 24.2: Verify Store Sales by Region legends")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Units Profit Treemap '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_5_1']",frame_height_value=0)
        parent_css="#jschart_HOLD_0 svg text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        legend=['Gross Profit', '0.3M', '13.1M', '26M', '38.9M', '51.8M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 24.3: Verify  Units Profit Treemap legends")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Accordion DataTable panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_6_1']",frame_height_value=0)
        parent_css="#DataTables_Table_0"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
#         portal_run.create_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds05.xlsx')
        portal_run.verify_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds05.xlsx', "Step 24.4: Accordion DataTable verification ")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ''' Verify Freeze DataTable panel '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bi-iframe iframe'][name^='Panel_7_1']",frame_height_value=0)
        parent_css="#DataTables_Table_0"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
#         portal_run.create_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds06.xlsx')
        portal_run.verify_table_data_set("#DataTables_Table_0", Test_Case_ID+'_Ds06.xlsx', "Step 24.5: Freeze DataTable verification ")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
         
        """ Step 25: Maximize all the panels and restore them
                     Verify that the panel is maximized and no issues.
        """
        def get_maximize_panel(panel_name):
            elem = portal_run.get_current_page()
            panel_elems = elem.find_elements_by_css_selector("[class*='bip-responsive']")
            return(panel_elems[[panel_name in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)])
        
        def handle_maximize_panel(panel_name, select_menu_option):
            elem = get_maximize_panel(panel_name)
            elem.find_element_by_css_selector("[id^='BipTitleBarMenuButton'][class*='button']").click()
            utillity.UtillityMethods.select_or_verify_bipop_menu(self, select_menu_option)
        
        ''' verification Category Sales ''' 
        time.sleep(10)
        panel_bef=portal_run.get_panel_obj_in_responsive('Category Sales')
        panel_width_bef = panel_bef.size['width']
        time.sleep(2)
        portal_run.manage_panel_title_menubar_button('Category Sales', verify=False, select_menu_opt='Maximize')
        time.sleep(2)
        panel_aft = get_maximize_panel('Category Sales')
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 900, 1085, 'Greater_than' , "Step 25: Verify Category Sales is being Maximize and Restore.")
        handle_maximize_panel('Category Sales', 'Restore')
        time.sleep(5)
        ''' verify Regional Sales Trend '''
        panel_bef=portal_run.get_panel_obj_in_responsive('Regional Sales Trend')
        panel_width_bef = panel_bef.size['width']
        time.sleep(2)
        portal_run.manage_panel_title_menubar_button('Regional Sales Trend', verify=False, select_menu_opt='Maximize')
        time.sleep(2)
        panel_aft = get_maximize_panel('Regional Sales Trend')
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 900, 1085, 'Greater_than' , "Step 25.1: Verify Regional Sales Trend is being Maximize and Restore.")
        handle_maximize_panel('Regional Sales Trend', 'Restore')
        time.sleep(5)
        ''' verify Store Sales by Region '''
        panel_bef=portal_run.get_panel_obj_in_responsive('Store Sales by Region')
        panel_width_bef = panel_bef.size['width']
        time.sleep(2)
        portal_run.manage_panel_title_menubar_button('Store Sales by Region', verify=False, select_menu_opt='Maximize')
        time.sleep(2)
        panel_aft = get_maximize_panel('Store Sales by Region')
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 900, 1085, 'Greater_than' , "Step 25.2: Verify Store Sales by Region is being Maximize and Restore.")
        handle_maximize_panel('Store Sales by Region', 'Restore')
        time.sleep(5)
        ''' verify Units Profit Treemap '''
        panel_bef=portal_run.get_panel_obj_in_responsive('Units Profit Treemap')
        panel_width_bef = panel_bef.size['width']
        time.sleep(2)
        portal_run.manage_panel_title_menubar_button('Units Profit Treemap', verify=False, select_menu_opt='Maximize')
        time.sleep(2)
        panel_aft = get_maximize_panel('Units Profit Treemap')
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 900, 1085, 'Greater_than' , "Step 25.3: Verify Units Profit Treemap is being Maximize and Restore.")
        handle_maximize_panel('Units Profit Treemap', 'Restore')
        time.sleep(5)
        ''' verify Accordion DataTable panel '''
        panel_bef=portal_run.get_panel_obj_in_responsive('Accordion DataTable')
        panel_width_bef = panel_bef.size['width']
        time.sleep(2)
        portal_run.manage_panel_title_menubar_button('Accordion DataTable', verify=False, select_menu_opt='Maximize')
        time.sleep(2)
        panel_aft = get_maximize_panel('Accordion DataTable')
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 650, 1085, 'Greater_than' , "Step 25.4: Verify Accordion DataTable panel is being Maximize and Restore.")
        handle_maximize_panel('Accordion DataTable', 'Restore')
        time.sleep(5)
        ''' verify Freeze DataTable panel '''
        panel_bef=portal_run.get_panel_obj_in_responsive('Freeze DataTable')
        panel_width_bef = panel_bef.size['width']
        time.sleep(2)
        portal_run.manage_panel_title_menubar_button('Freeze DataTable', verify=False, select_menu_opt='Maximize')
        time.sleep(2)
        panel_aft = get_maximize_panel('Freeze DataTable')
        panel_width_aft = panel_aft.size['width']
        portal_misobj.verify_difference(panel_width_bef, panel_width_aft, 650, 1085, 'Greater_than' , "Step 25.5: Verify Freeze DataTable panel is being Maximize and Restore.")
        handle_maximize_panel('Freeze DataTable', 'Restore')
        time.sleep(5)
        
        """ Step 26: Close the portal
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(5)
        
        
        """ Step 27: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
        
if __name__ == '__main__':
    unittest.main()