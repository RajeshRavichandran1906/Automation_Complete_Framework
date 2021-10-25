'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226961
TestCase Name = Test that AS name overrides fieldname/title in AutoDrill menu
'''
import unittest, time
from common.pages import visualization_ribbon, ia_run, active_miscelaneous, visualization_metadata
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2226961_TestClass(BaseTestCase):
    
    def test_C2226961(self):
        
        Test_ID="C2226961"
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = Test_ID+"_"+browser_type
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        """    
            Step 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'Revenue', expire_time=40)
        time.sleep(8)
        
        """    
            Step 02 : Right click on "Store Business Region" on the report canvas. Choose Change Title. Enter 'World,Market' > OK    
        """
        metaobj.querytree_field_click("Store,Business,Region", 1, 1, "Change Title...")
        utillobj.synchronize_with_visble_text("[id^='BiDialog'] div[class*='window-caption']>div[class='bi-label']", 'EditTitle', expire_time=10)
        
        edit_title_css="div[id^='BiDialog'][tabindex='0']"
        edit_title_obj=self.driver.find_element_by_css_selector(edit_title_css)
       
        utillobj.set_text_field_using_actionchains(edit_title_obj.find_element_by_css_selector("input"), 'World Market')
        utillobj.click_dialog_button(edit_title_css,"OK")
        utillobj.synchronize_with_visble_text("#TableChart_1 div[class^='x']:nth-of-type(26)", 'WorldMarket', expire_time=10)
        
        """    
                Step 03 : Right click on "Sale,Year" in the Across query panel and choose Change Title. Enter 'Fiscal Year' > Ok    
        """
        metaobj.querytree_field_click("Sale,Year", 1, 1, "Change Title...")
        utillobj.synchronize_with_visble_text("[id^='BiDialog'] div[class*='window-caption']>div[class='bi-label']", 'EditTitle', expire_time=10)
    
        edit_title_obj=self.driver.find_element_by_css_selector(edit_title_css)
        
        utillobj.set_text_field_using_actionchains(edit_title_obj.find_element_by_css_selector("input"), 'Fiscal Year')
        utillobj.click_dialog_button(edit_title_css,"OK")
        utillobj.synchronize_with_visble_text("#TableChart_1 div[class^='x']", 'FiscalYear', expire_time=10)
        
        """   
            Step 4 : Click Format tab > Autodrill button    
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=5)
        
        """    
            Step 05 : Click RUN    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'Fiscal Year', expire_time=20)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 05.1 : verify Auto Drill, drill down data set", desired_no_of_rows=15)
                
        """    
            Step 06 : Click on "North America" and select "Drill down to Store Business Sub Region"    
        """    
        iarun.select_report_autolink_tooltip("table[summary='Summary']", 12 , 1,'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'Canada', expire_time=20)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 06.1 : Verify this breadcrumb (North America) should appear above the previous one (Stereo Systems) Since this is a higher level sort .", desired_no_of_rows=15)
        
        """    
            Step 7 : Click on Canada.    
        """
        expected_tooltip_list = ['Restore Original', 'Drill up to World Market', 'Drill down to Store Country']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",5,1, expected_tooltip_list, "Step 07.1 : Verify the menu shows 'Drill up to World Market' instead of Store Business Region")
       
        """    
            Step 08 : Click on 2016 in the ACROSS labels. Select Drill down to Sale Year/Quarter    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,2,'Drill down to Sale Year/Quarter')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(3)>td:nth-child(2)", '2016Q4', expire_time=20)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 08.1 : verify Auto Drill, drill down data set", desired_no_of_rows=15)
        
        """    
            Step 09 : Click on 2016 Q4.    
        """
        expected_tooltip_list = ['Restore Original', 'Drill up to Fiscal Year', 'Drill down to Sale Year/Month']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",3,2, expected_tooltip_list, "Step 09.1 : Verify the menu shows 'Drill up to Fiscal Year' instead of Sale Year")
        utillobj.switch_to_default_content(pause=3)
        
        """    
            Step 10 : Click IA > Save As > Type C2226961a > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"_a")
        utillobj.infoassist_api_logout()
              
        """    
            Step 11 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226961a.fex&tool=Report    
        """
        utillobj.infoassist_api_edit(Test_Case_ID+"_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'Revenue', expire_time=40) 
        
        """    
            Step 12 : Click on the Format tab. Verify that Auto Drill is still selected.    
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=8)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 10a: Active_Report - Verify Autodrill button should be active")
       
        """    
            Step 13 : Click on HTML output format in status bar and select Active format    
        """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        utillobj.synchronize_with_visble_text("#sbpOutputFormat>div[class*='label']", 'ActiveReport', expire_time=20)
        
        """    
            Step 14 : Click Run    
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("td[id='I0r0.0C0'] div", 'EMEA', expire_time=20)
        
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['World Market', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 14c: Verify the report data ')
        
        """    
            Step 15 : Click on North America and select Drill down to Store Business Sub Region  
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("td[id='I0r0.0C0'] div", 'Canada', expire_time=20)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 15a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 15c: Verify the report data ')
        
        """    
            Step 16 : Click on Canada.  
        """
        values=['Restore Original', 'Drill up to World Market', 'Drill down to Store Country', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 0, values, "Step 16: Verify the menu shows 'Drill up to World Market' instead of Store Business Region")
        
        """    
            Step 17  : Click on 2016 in the ACROSS labels. Select Drill down to Sale Year/Quarter 
            Step 18. Click on 2016 Q4
        """
        utillobj.asequal(False,True, "Step 18: ACT-618 already exist for not able to click on across cells, once the case is fixed, scripts will be updated")
        utillobj.switch_to_default_content(pause=3)
      
        """    
            Step 19 : Click IA > Save As > Type C2226961b > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"b")
       
        """    
            Step 20. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226961b.fex&tool=Report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID+"b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'Revenue', expire_time=40)
        
        """    
            Step 21 : Click on the Format tab. Verify that Auto Drill is still selected.   
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=8)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 21a: Active_Report - Verify Autodrill button should be active")
      
        """    
            Step 22 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp  
        """
        
if __name__ == '__main__':
    unittest.main()
    