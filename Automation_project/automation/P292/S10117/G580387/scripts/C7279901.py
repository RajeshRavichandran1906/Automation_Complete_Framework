'''
Created on Jun 13, 2019

@author: Sudhan/Pearlson Joyal

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/7279901
TestCase Name : Drilling all the way down and up a long hierarchy path in report
'''
import time
import unittest
from common.lib import utillity
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C7279901_TestClass(BaseTestCase):

    def test_C7279901(self):
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        querypane_css = "#queryBoxColumn"
        format_css = "#FormatTab"
        case_id = "C7279901"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        
        """
        STEP 1 : Reopen the saved fex using API link:
                 http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/IA-Shell.fex&tool=Report
        """ 
        report_obj.edit_fex_using_api_url("IA-Shell")
        report_obj.wait_for_visible_text(querypane_css,"Product,Category")
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep) #firefox its required
        
        """
        STEP 2 : Click "Format tab" and Click "Auto Drill"option.
        """
        report_obj.select_ia_ribbon_item('Format','auto_drill')
        report_obj.wait_for_visible_text(format_css, "Features")    
         
        """
        STEP 3 : Click "Run" in toolbar.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.wait_for_number_of_element("[id^='ReportIframe']",1)
        report_obj.switch_to_frame()
        report_obj.wait_for_number_of_element("iframe[src*='contentDrill']",1)
        report_obj.switch_to_frame("iframe[src*='contentDrill']")
         
        """
        STEP 4 : Click on "North America" under "Store_Business,Region"and Click "Drill down to Store Business Sub Region".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(12, 1, "Drill down to Store Business Sub Region")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "North America",120)         
         
        """
        STEP 5 : Click on "West" and Click "Drill down to Store Country".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(66, 1, "Drill down to Store Country")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "West",120)           
         
        """
        STEP 6 : Click on "United States" and Click "Drill down to Store State Province".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(5, 1, "Drill down to Store State Province")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "United States",120)    
         
        """
        STEP 7 : Click on "California" and Click "Drill down to Store City".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(13, 1, "Drill down to Store City")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "California",120)  
         
        """
        STEP 8 : Click on "Sandiego" and Click "Drill down to Store Postal Code".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(13, 1, "Drill down to Store Postal Code")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "San Diego",120)  
         
        """
        STEP 9 : Click on "92101" and Click "Drill down to Store Name".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(5, 1, "Drill down to Store Name")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "92101",120)  
        
        """
        STEP 9.01 : Check the Breadcrumb and following Output.
        """
#         report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1,"Step 9.01 : verify report data")
        
        """
        STEP 10 : Click on "Sandiego" and Click "Drill up to Store Postal Code".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(5, 1, "Go up to Store Postal Code")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "San Diego",120)  
         
        """
        STEP 11 : Click on "92101" and Click "Drill up to Store City"
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(5, 1, "Go up to Store City")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "California",120)  
               
        """
        STEP 12 : Click on "Sandiego" and Click "Drill up to Store State Province".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(13, 1, "Go up to Store State Province")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "United States",120)
        time.sleep(5) 
                 
        """
        STEP 13 : Click on "California" and Click "Drill up to Store Country".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(13, 1, "Go up to Store Country")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "West",120)   
        time.sleep(5)
         
        """
        STEP 14 : Click on "United States" and Click "Drill up to Store Business Sub Region".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(5, 1, "Go up to Store Business Sub Region")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "North America",120)   
        time.sleep(5)
        
        """
        STEP 15 : Click on "West" and Click "Drill up to Store Business Region".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(66, 1, "Go up to Store Business Region")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "Sale,Year",120)   
         
        """
        STEP 15.01 : Check the following output.
        """
        #report_obj.create_html_report_dataset(DATA_SET_NAME2)
        report_obj.verify_html_report_dataset(DATA_SET_NAME2,"Step 15.01 : verify report data")
        report_obj.switch_to_default_content()
        
        """
        STEP 16 : Click "IA" menu and Select "Save As" option.
        STEP 17 : Enter "C7279901" in Title textbox and Click "Save" button.
        """      
        report_obj.save_as_from_application_menu_item(case_id)
         
        """
        STEP 18 : Logout
                  http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
                
        """
        STEP 19 : Reopen the saved fex using API link    
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279901 .fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(case_id)
        report_obj.wait_for_visible_text(querypane_css,"Product,Category")       
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep) #firefox its required
        
        """
        STEP 20 : Click "Format tab".
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
        STEP 20.01 : Check" Auto Drill" is still selected.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "20.01")
        
        """
        STEP 21 : Logout
                  http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()