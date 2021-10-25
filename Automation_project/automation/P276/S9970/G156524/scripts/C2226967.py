'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226967
TestCase Name = Test that AutoDrill works in a MultiDrill - HTML
'''

from common.pages import visualization_ribbon, visualization_metadata, ia_run, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity,core_utility
import unittest, time

class C2226967_TestClass(BaseTestCase):
    
    def test_C2226967(self):
        
        Test_ID="C2226967"
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID = Test_ID+"_"+browser_type
        
        """    
            STEP 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#resultArea div[class^='x']", 'Sale,Year', 150)
         
        """    
            STEP 02 : Click on Store,Business,Region on the canvas.    
        """
        metaobj.querytree_field_click("Store,Business,Region", 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn tr[class*='selected']", 'Store,Business,Region', 30)
         
        """    
            STEP 03 : Click on Drill Down on the ribbon.    
        """
        ribbonobj.select_ribbon_item("Field", "Drilldown")
        utillobj.synchronize_with_visble_text("[id^='QbDialog'] #ok", 'OK', 60)
         
        """    
            STEP 04 : Click on the Web Page radio button. Under URL, type "http://www.informationbuilders.com"
            Change the Description to say "Go to Information Builders Home Page" Press the Tab key.    
        """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.informationbuilders.com', set_description='Go to Information Builders Home Page', create_new_drilldown=True)
        utillobj.synchronize_with_visble_text("#drillDownBtn_2", 'Drill Down 2', 15)
         
        """    
            STEP 05 : Click on the "Create a new drill down" icon. On the Report line click on Browse and choose "Drilldown-Region". 
            In the Parameter section click on the Add Parameter icon.    
        """
        ia_ribbonobj.create_drilldown_report("report", browse_file_name="Drilldown-Region", set_ampersand='add')
        utillobj.synchronize_with_visble_text("#drillDownParmPopup #paramPopupOkBtn", 'OK', 15)
         
        """    
            STEP 06 : In the Name drop down pick BUSINESS_REGION. In the Value drop down pick Store,Business,Region. 
            Click OK twice to close the dialog.    
        """
        ia_ribbonobj.drilldown_parameter_popup(name_select='BUSINESS_REGION', value_select="Store,Business,Region",popup_close='ok')
        time.sleep(2)
        ok_btn_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        utillobj.synchronize_with_visble_text("#resultArea div[class^='x'] a", 'EMEA', 15)
         
        """    
            STEP 07 : Select Format tab > Auto Drill. Then select Enable Auto Linking.     
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
        utillobj.synchronize_with_number_of_element("[id='FormatEnableAutoLink'][class*='checked']", 1, 8)
         
        """    
            STEP 08 : Click Run    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_util_obj.switch_to_frame()
        utillobj.synchronize_with_number_of_element("iframe[src]", 1, 40)
        core_util_obj.switch_to_frame(frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(1)>td:nth-child(1)", 'Sale,Year', 40)
         
        """
            STEP 08.1 : Verify output
        """          
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 08a: verify Auto Drill, drill down data set", desired_no_of_rows=15)
         
        """    
            STEP 09 : Click on 2016 in Sales Year from ACROSS label and verify the drill down menu
        """
        expected_tooltip_list = ['Drill down to Sale Year/Quarter']
        iarun.verify_autolink_tooltip_values_usng_pyautogui("table[summary='Summary']",1,2, expected_tooltip_list, "Step 09: Verify that should only show an Auto Drill link")
        time.sleep(2)
         
        """    
            STEP 10 : Click on Accessories under North America and verify the drill down menu.    
        """
        expected_tooltip_list = ['Drill down to Product Subcategory']
        iarun.verify_autolink_tooltip_values_usng_pyautogui("table[summary='Summary']",12,2, expected_tooltip_list, "Step 10: Verify that should only show an Auto Drill link")
        time.sleep(2)
         
        """    
            STEP 11 : Click on North America and verify the drill down menu.    
        """
        expected_tooltip_list = ['Drill down to Store Business Sub Region', 'Go to Information Builders Home Page', 'Drilldown-Region', 'Auto Links']
        iarun.verify_autolink_tooltip_values_usng_pyautogui("table[summary='Summary']",12,1, expected_tooltip_list, "Step 11: Verify that should show an Auto Drill link, the two drill downs created above and an Auto Link tab ")
        time.sleep(2)
         
        """    
            STEP 12 : Hover over the Auto Link tab and verify that shows "Target-Region"    
        """
        expected_tooltip_list = ["Target-Region"]
        iarun.verify_report_autolink_tooltip_submenu("table[summary='Summary']",12,1, "Auto Links", expected_tooltip_list, "Step 12: Verify the autolink submenu", cord_type='top_middle', y_offset=5)
         
        """    
            STEP 13 : Click on "Go to Information Builders Home Page" from drill down menu and verify the page opens. Close the page.    
        """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 12,1, "Go to Information Builders Home Page")
        core_util_obj.switch_to_new_window()
         
        """
            STEP 13.1 : Verify that "http://www.informationbuilders.com/" opens on separate page
        """
        owebpage=self.driver.current_url
        utillobj.asin('informationbuilders', owebpage, "Step 13a: Verify Information Builder page is displayed")
        core_util_obj.switch_to_previous_window()
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_frame()
        core_util_obj.switch_to_frame(frame_css='iframe[src]')
         
        """    
            STEP 14 : Click on North America and select "Drilldown-Region" and verify the page opens. Close the page
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",12,1,'Drilldown-Region')
        core_util_obj.switch_to_new_window()
         
        """
            STEP 14.1 : Verify that "Drilldown-Region" report opens on separate page
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 14a: Verify that 'Drilldown-Region' report opens on separate page")
        core_util_obj.switch_to_previous_window()
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_frame()
        core_util_obj.switch_to_frame(frame_css='iframe[src]')
         
        """    
            STEP 15 : Click on North America and select "Auto Link tab" > "Target-Region" and verify the page opens. Close the page.    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",12,1,'Auto Links->Target-Region')
        core_util_obj.switch_to_new_window()
        core_util_obj.switch_to_frame(frame_css='iframe[src]')
         
        """
            STEP 15.1 : Verify that "Target-Region" report opens on separate page
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 15a: Verify that 'Target-Region' report opens on separate page")
        core_util_obj.switch_to_previous_window()
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_frame()
        core_util_obj.switch_to_frame(frame_css='iframe[src]')
         
        """    
            STEP 16 : Click on North America and Click on Drill down to Store Business Sub Region
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",12,1,'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:nth-child(1)", 'Sale,Year', 20)
         
        """
            STEP 16.1 : Verify that drilled down properly
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx", "Step 16a: Verify that drilled down properly", desired_no_of_rows=15)
        
        """    
            STEP 17 : Click on Canada and verify the drill menu    
        """
        expected_tooltip_list = ['Restore Original', 'Drill up to Store Business Region', 'Drill down to Store Country', 'Go to Information Builders Home Page']
        iarun.verify_autolink_tooltip_values_usng_pyautogui("table[summary='Summary']",5,1, expected_tooltip_list, "Step 17: Verify Canada tooltip menu")
        core_util_obj.switch_to_default_content()
         
        """    
            STEP 18 : Click IA > Save As> Type C2226967 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """    
            STEP 19 : Open saved fex. http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226967a.fex&tool=report    
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#resultArea div[class^='x']", 'Sale,Year', 150)
        
        """    
            STEP 20 : Click format tab and Verify that Auto Drill is still selected    
        """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 20a: Active_Report - Verify Autodrill button should be active")
        
        """    
            STEP 21 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    