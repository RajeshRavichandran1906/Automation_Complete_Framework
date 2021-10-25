'''
Created on Jun 12, 2019

@author: Sudhan/Pearlson Joyal

Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7279890
TestCase Name : Drill down eligibility for a hierarchy field as a verb object
'''

import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C7279890_TestClass(BaseTestCase):

    def test_C7279890(self):
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        case_id = "C7279890"
        querypane_css = " #queryBoxColumn"
        format_css = "#FormatTab"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        table_css="table[summary='Summary']"
        
        """
        STEP 1 : Reopen the saved fex using API link:
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/IA-Shell.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name="IA-Shell")
        report_obj.wait_for_visible_text(querypane_css,"Product,Category")
         
        """
        STEP 2 : Drag and drop "Product,Category" in to "Sum" in Query pane.
        """
        report_obj.drag_field_from_data_tree_to_query_pane(field_name="Product,Category",field_position=1, bucket_name="Sum")
        report_obj.wait_for_visible_text(querypane_css,"MAX.Product,Category")
        
        """
        STEP 2.01 : Check MAX prefix has been added to "Product,Category" in Query pane.
        """
        report_obj.verify_field_in_querypane("Sum", "MAX.Product,Category", 1, "Step 02.01 ")
        
        """
        STEP 3 : Right click "MAX.Product,Category" in Sum and Select "More" > Select "Aggregation Functions" > Click "None".
        """
        report_obj.right_click_on_field_under_query_tree("MAX.Product,Category", 1, "More->Aggregation Functions->(None)")
         
        """
        STEP 4 : Click "Format tab" and Click "Auto Drill"option.
        """       
        report_obj.select_ia_ribbon_item('Format','auto_drill')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
        STEP 5 : Click "Run" in toolbar.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.wait_for_number_of_element("[id^='ReportIframe']",1)
        
        """
        STEP 5.01 : Check the following output.
        """
        report_obj.switch_to_frame()
        report_obj.wait_for_number_of_element("iframe[src^='/ibi_apps/contentDrill']",1)
         
        report_obj.switch_to_frame("iframe[src^='/ibi_apps/contentDrill']") 
        report_obj.wait_for_visible_text(table_css, "Quantity")
        #report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1,"Step 5.01 : verify report data")
        report_obj.switch_to_default_content()
        
        """
        STEP 6 : Click "IA" menu and Select "Save As" option.
        STEP 7 : Enter "C7279890" in Title textbox and Click "Save" button.
        """
        report_obj.save_as_from_application_menu_item(case_id)       
         
        """
        STEP 8 : Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
        """
        STEP 9 : Reopen the saved fex using API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279890.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name=case_id)
        report_obj.wait_for_visible_text(querypane_css,"Product,Category")       
         
        """
        STEP 10 : Click "Format tab".
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
        STEP 10.01 : Check" Auto Drill" is still selected.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "10.01")
        
        """
        STEP 11 : Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()