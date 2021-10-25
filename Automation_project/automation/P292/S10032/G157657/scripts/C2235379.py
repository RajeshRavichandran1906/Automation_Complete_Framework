'''
Created on Dec 6, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235379
TestCase Name = Verify Report with Header&Footer
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
import datetime
from common.lib.global_variables import Global_variables
from common.wftools.report import Report

class C2235379_TestClass(BaseTestCase):

    def test_C2235379(self):
        
        Test_Case_ID = "C2235379"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        browser = Global_variables()
        currentDT = datetime.datetime.now()
        current_date = currentDT.strftime("%B %d,%Y")
        report = Report(self.driver)
        
        """
            TESTCASE CSS
        """
        query_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, report.home_page_long_timesleep)
           
        """
        Step 02: Double click fields "Product,Category" and "Cost of Goods"
        """
        report.double_click_on_datetree_item("Product,Category", 1)
        report.wait_for_visible_text(query_tree_css, "Product,Category")
        
        report.double_click_on_datetree_item("Cost of Goods", 1)
        report.wait_for_visible_text(query_tree_css, "Cost of Goods")
          
        """
        Step 03: Click "Header & Footer" in the Home Tab ribbon
        Step 04: Type "Report Header for test case C2235379"
        """
        ia_stylingobj.create_header_footer('ribbon','Report Header', 'Report Header for test case C2235379')
        time.sleep(2)
           
        """
        Step 05: Click "Page Header" in the toolbar > Type "Cost of Goods by Product"
        """
        ia_stylingobj.create_header_footer('frame','Page Header', 'Cost of Goods by Product')
        time.sleep(2)
          
        """
        Step 06: Click "Page Footer" in the toolbar > Then click last button to access preformatted text options
        Step 07: Select current date, formatted as > "January 18, 2007"
        """
        ia_stylingobj.create_header_footer('frame','Page Footer','')
        time.sleep(2)
        option=driver.find_element_by_css_selector("#QuickText div[class^='bi-component tool-bar-menu-button-drop-down-arrow']")
        utillobj.click_on_screen(option, 'middle')
        utillobj.click_on_screen(option, 'middle', click_type=0)
        time.sleep(1)
        currentDT = datetime.datetime.now()
        current_date1 = currentDT.strftime("%B %d,%Y")
        print (current_date1)
        utillobj.select_or_verify_bipop_menu('Date')
        utillobj.select_or_verify_bipop_menu(current_date1)
          
        """
        Step 08: Verify syntax displayed in the dialog
        """
        if browser == 'ie':
            time.sleep(8)
            ele=driver.find_element_by_css_selector("#subheaderDlg")
            utillobj.take_screenshot(ele,'C2235379_Actual_step08_IE', image_type='actual',x=1, y=1, w=-1, h=-1)
        else:    
            syntax = "&DATEtrM&DATED,&DATEYY"
            time.sleep(5)
            self.driver.switch_to.frame(self.driver.find_element_by_id("Editor"))
            time.sleep(15)
            el = self.driver.find_element_by_css_selector('html>body')
            text_value=el.text.strip()
            print(text_value)
            utillobj.asequal(text_value,syntax,"Step 08.00: Verify syntax displayed in the dialog")
            time.sleep(1)
            self.driver.switch_to_default_content()
              
        """
        Step 09: Click "Report Footer" in the toolbar > Type "Report Footer for test case C2235379"
        Step 10: Click OK
        """
        ia_stylingobj.create_header_footer('frame', 'Report Footer', 'Report Footer for test case C2235379', btn_ok=True)
        time.sleep(10)
         
        """
        Step 11: Verify Preview
        """
        cur_date = current_date.replace(' ' ,'')
        print (type(current_date))
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 11.01: Verify report titles")
        #ia_resultobj.create_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", no_of_cells=4)
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 11.02: Verify report dataset', no_of_cells=4)
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='matterhorn1', text_value='Report Header for test case C2235379', font_name='Arial',font_size='14pt', bold=True, msg='Step 11.03:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='matterhorn1', text_value='Cost of Goods by Product', font_name='Arial', font_size='12pt',bold=True,msg='Step 11.04:')
        if browser == 'firefox':
            font_size='10pt'
        elif browser == 'ie':
            font_size='13px'
        else:
            font_size='12pt'
         
        if browser == 'ie':
            ia_resultobj.verify_report_header_footer_property('TableChart_1', 3, font_color='matterhorn1', font_name='Arial',font_size=font_size, font_size_pixel=True, msg='Step 11.05:')
        else:
            ia_resultobj.verify_report_header_footer_property('TableChart_1', 3, font_color='matterhorn1', font_name='Arial',font_size=font_size, msg='Step 11.06:')    
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 4, font_color='matterhorn1', text_value='Report Footer for test case C2235379', font_name='Arial',font_size='10pt', msg='Step 11.07:')
        total_elems=self.driver.find_elements_by_css_selector("#TableChart_1"  + " div[style*='solid'] span")
        header_footer_elems=[el.text.replace(' ', '') for el in total_elems]
        utillobj.asin(cur_date, header_footer_elems, 'Step 11.08: Verify Date')
        
        """
        Step 12: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
     
        """
        Step 13: Verify output
        """
        time.sleep(10)
        #ia_runobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx" )
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx" , 'Step 13.00: Verify report dataset', desired_no_of_rows=12)
         
        """
        Step 14: Click "IA" > "Save As" > "C2235379" > click "Save"
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """
        Step 15: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """
        Step 16: Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235379.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_5',mrid='mrid',mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 18, expire_time=resultobj.home_page_long_timesleep) 
        
        """
        Step 17: Verify Preview
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 17.01: Verify report titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 7, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 17.02: Verify report dataset', no_of_cells=4)
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='matterhorn1', text_value='Report Header for test case C2235379', font_name='Arial',font_size='14pt', bold=True,msg='Step 17.03:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='matterhorn1', text_value='Cost of Goods by Product', font_name='Arial', font_size='12pt',bold=True,msg='Step 17.04:')
        if browser == 'ie':
            ia_resultobj.verify_report_header_footer_property('TableChart_1', 3, font_color='matterhorn1',  font_name='Arial', font_size=font_size, font_size_pixel=True, msg='Step 17.05:')
        else:
            ia_resultobj.verify_report_header_footer_property('TableChart_1', 3, font_color='matterhorn1', font_name='Arial', font_size=font_size, msg='Step 17.06:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 4, font_color='matterhorn1', text_value='Report Footer for test case C2235379', font_name='Arial',font_size='10pt', msg='Step 17.07:')
        total_elems=self.driver.find_elements_by_css_selector("#TableChart_1"  + " div[style*='solid'] span")
        header_footer_elems=[el.text.replace(' ', '') for el in total_elems]
        utillobj.asin(cur_date, header_footer_elems, 'Step 17.08: Verify Date')
        """
        Step 18: Logout and do not save changes: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()