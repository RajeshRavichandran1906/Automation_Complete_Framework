'''
Created on Jun 13, 2019

@author: Sudhan/Pearlson Joyal

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/7279918
TestCase Name : Auto Drill with Reporting Objects- Report component
'''

import unittest, time
from common.lib import utillity
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C7279918_TestClass(BaseTestCase):

    def test_C7279918(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver) 
        utils = utillity.UtillityMethods(self.driver)
        
        """
            TESTCASE VARIABLES 
        """
        querypane_css = "#queryBoxColumn"
        format_css = "#FormatTab"
        case_id = "C7279918"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        
        """
        STEP 1 : Launch MyReport (Report mode) using the below API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/RO-Shell.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url("RO-Shell")
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep) #firefox its required
        report_obj.wait_for_visible_text(querypane_css,"Product,Category")
          
        """
        STEP 2 : Click "Format tab" and Click "Auto Drill"option.
        """
        time.sleep(10) #firefox- giving time for different page elements locating
        self.driver.set_page_load_timeout(report_obj.home_page_long_timesleep)

        report_obj.select_ia_ribbon_item('Format','auto_drill')
        report_obj.wait_for_visible_text(format_css, "Features")
               
        """
        STEP 3 : Click "Run" in toolbar.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        report_obj.wait_for_number_of_element("iframe[src*='contentDrill']",1)
        report_obj.switch_to_frame("iframe[src*='contentDrill']")
         
        """
        STEP 4 : Click on "North America" and Click "Drill down to Store Business Sub Region".
        """   
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 10, 1, "Drill down to Store Business Sub Region")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "North America",120)
         
        """
        STEP 5 : Click on "Stereo Systems" under "East" and Click "Drill down to Product Subcategory".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 16, 2, "Drill down to Product Subcategory") 
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "Stereo Systems",120)
          
        """
        STEP 6 : Click on "2016" and Click "Drill down to Sale Year/Quarter".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 3, 2, "Drill down to Sale Year/Quarter") 
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "2016",120)
        
        """
        STEP 6.01 : Check the Breadcrumb and following Output.
        """
        #report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1,"Step 06.01 : verify report data")
        report_obj.switch_to_default_content()
        
        """
        STEP 7 : Click "IA" menu and Select "Save As" option.
        STEP 8 : Enter "C7279918" in Title textbox and Click "Save" button.
        """
        report_obj.save_as_from_application_menu_item(case_id)  
       
        """
        STEP 9 : Logout
                 http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()        
         
        """
        STEP 10 : Reopen the saved fex using API link
                  http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279918 .fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(case_id)
        report_obj.wait_for_visible_text(querypane_css,"Product,Category")       
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep) #firefox its required
        
        """
        STEP 11 : Click "Format tab".
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
        STEP 11.01 : Check" Auto Drill" is still selected.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "11.01")
        
        """
        STEP 12 : Logout - http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()     