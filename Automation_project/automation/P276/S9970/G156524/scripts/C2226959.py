'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226959
TestCase Name = Test if Heading formatting impacts look and/or positioning of breadcrumbs
'''
import unittest, time
from common.pages import visualization_ribbon, ia_run, active_miscelaneous, ia_styling
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2226959_TestClass(BaseTestCase):
    
    def test_C2226959(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226959"
        Test_Case_ID = Test_ID+"_"+browser_type
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """   
            Step 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'Revenue', expire_time=40)
        time.sleep(8)
        
        """    
            Step 02 : Click on Header & Footer in the Ribbon    
        """
        ribbonobj.select_ribbon_item('Home', 'Header_footer', opt='Page Header')
        utillobj.synchronize_with_visble_text("#okBtn>div", 'OK', expire_time=10)
        
        """    
            Step 03 : Select "Page Header" > Change the font to Comic Sans MS > Change the size to 18 > Italic > Center > Change Font Color to Red (255 0 0) > Change Background Color to Green (0 255 0).     
        """
        ia_stylingobj.set_header_footer_style(font_name='COMIC SANS MS', font_size='18', italic=True, center_justify=True, text_color='red',background_color='lime')
         
        """    
            Step 04 : Type "This is Line 1" as First Line of Heading > Enter 
            Step 05 : Type "This is Line 2" as 2nd line of Heading > Click OK
        """   
        ia_stylingobj.type_text_in_editor(['This is Line 1', 'This is Line 2'])
        ok_btn=self.driver.find_element_by_id("okBtn")
        utillobj.default_click(ok_btn)
        time.sleep(10)
#         
        """   
            Step 6 : Click Format tab > Autodrill button 
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=5)
        
        """    
            Step 07 : Click RUN    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'EMEA', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=10)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 07.1 : verify Auto Drill, drill down data set", desired_no_of_rows=10)
        
        """    
            Step 08 : Click on Stereo Systems within North America and select "Drill down to Product Subcategory"   
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",18,2,'Drill down to Product Subcategory')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'NorthAmerica', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 08.1 : Verify Drill down to Sale Year/Quarter Report")
        iarun.verify_header_footer_report_cell("table[summary='Summary']", 1, font_color='red', bg_color='lime', msg='Step 08.2 : This is Line 1: ')
        
        """    
            Step 09 : Click on North America and select "Drill down to Store Business Sub region"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'Canada', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", desired_no_of_rows=6)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 09.1 : Verify Drill down to Sale Year/Month Report", desired_no_of_rows=6)
        iarun.verify_header_footer_report_cell("table[summary='Summary']", 1, font_color='red', bg_color='lime', msg='Step 09.2 - This is Line 1: ')
        iarun.verify_header_footer_report_cell("table[summary='Summary']", 2, font_color='red', bg_color='lime', msg='Step 09.3 - This is Line 2: ')
        
        utillobj.switch_to_default_content(2)
        
        """    
            Step 10 : Click IA > Save As> Type C2226959a > click Save  
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
      
        """    
            Step 11 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226959a.fex&tool=report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'Revenue', expire_time=40)

        """    
            Step 12 : Click on the Format tab. Verify that Auto Drill is still selected. 
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=5)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 12a: Active_Report - Verify Autodrill button is still selected")
       
        """    
            Step 13 : Click on HTML output format in status bar and select Active format 
        """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        utillobj.synchronize_with_visble_text("#sbpOutputFormat>div[class*='label']", 'ActiveReport', expire_time=20)
        
        """    
            Step 14 : Click Run   
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("tr[id^='I0r0']>td[id^='I0r0.0C0']", 'EMEA', expire_time=30)
         
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 14c: Verify the report data ')
        iarun.verify_header_footer_doc_cell("ITableData0", 1, font_color='red', bg_color='lime', msg='Step 14d - This is Line 1: ')
        iarun.verify_header_footer_doc_cell("ITableData0", 2, font_color='red', bg_color='lime', msg='Step 14e - This is Line 2: ')
        
        """    
            Step 15 : Click on Stereo Systems within North America and select "drill down to Product Subcategory" 
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 11, 1, 'Drill down to Product Subcategory')
        utillobj.synchronize_with_visble_text("tr[id^='I0r0']>td[id^='I0r0.0C0']", 'NorthAmerica', expire_time=10)
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 15a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Subcategory', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 15c: Verify the report data ')
        iarun.verify_header_footer_doc_cell("ITableData0", 1, font_color='red', bg_color='lime', msg='Step 15d - This is Line 1: ')
        iarun.verify_header_footer_doc_cell("ITableData0", 2, font_color='red', bg_color='lime', msg='Step 15e - This is Line 2: ')
        
        """    
            Step 16 : Click on North America and select "Drill down to Store Business Sub Region"    
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0, 0, 'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("tr[id^='I0r0']>td[id^='I0r0.0C0']", 'Canada', expire_time=10)
        miscelanousobj.verify_page_summary(0, '35of35records,Page1of1', 'Step 16a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Subcategory', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 16b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx', 'Step 16c: Verify the report data ')
        iarun.verify_header_footer_doc_cell("ITableData0", 1, font_color='red', bg_color='lime', msg='Step 16d - This is Line 1: ')
        iarun.verify_header_footer_doc_cell("ITableData0", 2, font_color='red', bg_color='lime', msg='Step 16e - This is Line 2: ')
        
        utillobj.switch_to_default_content(3)
        
        """    
            Step 17 Click IA > Save As > Type C2226959b > click Save  
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
       
        """    
            Step 18 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226959b.fex&tool=Report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'Revenue', expire_time=40)
        
        """    
            Step 19 : Click on the Format tab. Verify that Auto Drill is still selected.    
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=5)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 19a: Active_Report - Verify Autodrill button is still selected")
    
        """   
            Step 20 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    