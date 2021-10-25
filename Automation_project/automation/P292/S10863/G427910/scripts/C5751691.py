'''
Created on Apr 26, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5751691
TestCase Name = Verify report with Title Popup, Accordion, Repeat Sort Value, Stack Measures
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C5751691_TestClass(BaseTestCase):

    def test_C5751691(self):
        
        TestCase_ID = "C5751691"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        
        """
            Step 01: Launch IA Report mode:http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/GGSALES&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """         
        utillobj.invoke_infoassist_api_login('report','ibisamp/ggsales','P292_S10863/G427910', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
         
        """
            Step 02: Double click "Category", "Product", "Unit Sales", "Dollar Sales".
        """
        metaobj.datatree_field_click('Category', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='Category', with_regular_exprestion=True)
        metaobj.datatree_field_click('Product', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='Product', with_regular_exprestion=True)
        metaobj.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='UnitSales', with_regular_exprestion=True)
        metaobj.datatree_field_click('Dollar Sales', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='DollarSales', with_regular_exprestion=True)
         
        """
            Step 03: Verify the following report is displayed.
        """
#         ia_resultobj.create_report_data_set('TableChart_1', 2, 4, TestCase_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 4, TestCase_ID+"_Ds01.xlsx", msg="Step 03:Verify the following report is displayed.")
         
        """
            Step 04: Select "Format" > "Title Popup" (Features Group).
        """
        ribbonobj.select_ribbon_item('Format','title_popup')
         
        """
            Step 05: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
            Step 06:Verify the report is displayed.
        """
#         ia_runobj.create_table_data_set("table[summary='Summary']",TestCase_ID+'_Ds02.xlsx') 
        ia_runobj.verify_table_data_set("table[summary='Summary']",TestCase_ID+"_Ds02.xlsx", 'Step 06: Verify the report is displayed.')      
         
        """
            Step 07:Hover over the "Category" and verify the Title
        """
        expected_popup='Product category'
        ia_runobj.verify_report_title_popup("table[summary='Summary']",1, expected_popup, "Step 7:tooltip")
          
        """
            Step 08:Hover over the "Product" and verify the Title
        """
        expected_popup='Product name'
        ia_runobj.verify_report_title_popup("table[summary='Summary']",2, expected_popup, "Step 8:tooltip")
          
        """
            Step 09:Hover over the "Unit Sales" and verify the Title
        """
        expected_popup='Number of units sold'
        ia_runobj.verify_report_title_popup("table[summary='Summary']",3, expected_popup, "Step 9:tooltip")
          
        """
            Step 10:Hover over the "Dollar Sales" and verify the Title
        """
        expected_popup='Total dollar amount of reported sales'
        ia_runobj.verify_report_title_popup("table[summary='Summary']",4, expected_popup, "Step 10:tooltip")
         
        """
            Step 11:Click "IA" > "Save".
            Step 12:Enter Title = "C2227576".
            Step 13:Click "Save".
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(5)
         
        """
            Step 14:De-select "Title Popup" button.
        """
        ribbonobj.select_ribbon_item('Format','title_popup')
         
        """
            Step 15:Select "Format" > "Accordion" (Features Group).
        """
        ribbonobj.select_ribbon_item('Format','accordion')
         
        """
            Step 16:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
            Step 17:Verify the report is displayed.
        """
#         ia_runobj.create_table_data_set("table#treetable",TestCase_ID+'_Ds03.xlsx') 
        ia_runobj.verify_table_data_set("table#treetable",TestCase_ID+"_Ds03.xlsx", 'Step 17: Verify the report is displayed.')      
         
        """
            Step 18:Expand all the nodes on the Accordion.
            Step 19:Verify the following report is displayed.
        """
        elem=self.driver.find_element_by_css_selector("#divTreeTable tr[data-tt-id='1'] a[href]")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(3)
        elem=self.driver.find_element_by_css_selector("#divTreeTable tr[data-tt-id='2'] a[href]")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(3)
        elem=self.driver.find_element_by_css_selector("#divTreeTable tr[data-tt-id='3'] a[href]")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(3)
#         ia_runobj.create_table_data_set("table#treetable",TestCase_ID+'_Ds04.xlsx') 
        ia_runobj.verify_table_data_set("table#treetable",TestCase_ID+"_Ds04.xlsx", 'Step 20: Verify the report is displayed.')
         
        """
            Step 20:De-select "Accordion" button.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_ribbon_item('Format','accordion')
         
        """
            Step 21:Select "Format" > "Repeat Sort Value" (Features Group).
        """
        ribbonobj.select_ribbon_item('Format','repeat_sort_value')
         
        """
            Step 22:Verify the following report is displayed.
        """
#         ia_resultobj.create_report_data_set('TableChart_1', 2, 4, TestCase_ID+"_Ds05.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 4, TestCase_ID+"_Ds05.xlsx", msg="Step 22:Verify the following report is displayed.")
         
        """
            Step 23:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
            Step 24:Verify the report is displayed.
        """
#         ia_runobj.create_table_data_set("table[summary='Summary']",TestCase_ID+'_Ds06.xlsx')
        ia_runobj.verify_table_data_set("table[summary='Summary']",TestCase_ID+"_Ds06.xlsx", 'Step 24: Verify the report is displayed.')
         
        """
            Step 25:De-select "Repeat Sort Value" icon.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_ribbon_item('Format','repeat_sort_value')
         
        """
            Step 26:Select "Format" > "Stack Measures" (Features Group).
        """
        ribbonobj.select_ribbon_item('Format','stack_measures')
         
        """
            Step 27:Verify the following report is displayed.
        """
        resultobj.verify_report_titles_on_preview(2, 2, 'TableChart_1', ['Category','Product'],"Step 27:Verify the following report is displayed.")
         
        """
            Step 28:Click "Run".        
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
            Step 29:Verify the report is displayed.       
        """        
#         ia_runobj.create_table_data_set("table[summary='Summary']",TestCase_ID+'_Ds08.xlsx') 
        ia_runobj.verify_table_data_set("table[summary='Summary']",TestCase_ID+"_Ds07.xlsx", 'Step 29: Verify the report is displayed.')
         
        """
            Step 30:Select "Title Popup", "Accordion", and "Repeat Sort Value"    
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        ribbonobj.select_ribbon_item('Format','title_popup')
        ribbonobj.select_ribbon_item('Format','accordion')
        ribbonobj.select_ribbon_item('Format','repeat_sort_value')
         
        """
            Step 31:Click Save
        """
        ribbonobj.select_top_toolbar_item('infomini_save')
        parent_css="div[id^='BiDialog']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(5)
         
        """
            Step 32:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
         
        """
            Step 33:Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227576.fex&tool=Report
        """
        utillobj.infoassist_api_edit_(TestCase_ID,'Report','P292_S10863/G427910',mrid='mrid',mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 34:Verify "Title Popup", "Accordion", "Repeat Sort Value", and "Stack Measures" remain toggled ON
        """
        elem=self.driver.find_element_by_css_selector("#FormatTab_tabButton")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(5)        
        ele=driver.find_element_by_css_selector("#FormatTitlePopup")
        utillobj.verify_checked_class_property(ele, "Step 34.1:Verify Title Popup", check_property=True)        
        elem=driver.find_element_by_css_selector("#FormatAccordion")
        utillobj.verify_checked_class_property(elem, "Step 34.2:Verify Accordion", check_property=True)
        ele1=driver.find_element_by_css_selector("#FormatRepeatSort")
        utillobj.verify_checked_class_property(ele1, "Step 34.3:Verify Repeat Sort Value", check_property=True)
        ele2=driver.find_element_by_css_selector("#FormatStackMeasures")
        utillobj.verify_checked_class_property(ele2, "Step 34.4:Verify Stack Measures", check_property=True)       
        
        """
            Step 35:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()