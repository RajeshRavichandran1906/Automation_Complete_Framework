'''
Created on Oct 23, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6417167&group_by=cases:section_id&group_order=asc&group_id=542381
Testcase Name : Verify to Run and Edit "Store Product Quantity Sold by Year"
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C6417167_TestClass(BaseTestCase):

    def test_C6417167(self):
        
        driver = self.driver
        report_obj = report.Report(driver)
        utillobj=utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables-----------------------------------------------------------------------------------"
        
        LONG_WAIT= 240
        SHORT_TIME=20
        
        TESTCASE_ID="C6417167"
        USERNAME= 'mradvid'
        PASSWORD= 'mradvpass'
        FEX_NAME='Store_Product_Quantity_Sold_by_Year'
        FOLDER_NAME='Retail_Samples/Reports/Auto_Link'
        QUERY_FIELD_LIST=['Report (wf_retail_lite)', 'Sum', 'Quantity,Sold', 'By', 'Product,Subcategory', 'Model', 'Across', 'Sale,Year']
        FILTER_FIELD1='Store Name Equal to Simple Parameter (Name: STORE_NAME)'
        FILTER_FIELD2='Model Equal to Optional Simple Parameter (Name: MODEL)'
        REPORT_PREVIEW_TITLE=['STORE_NAME Product Quantity Sold']
        
        "----------------------------------------------------------------------------CSS-----------------------------------------------------------------------------------------"
        AUTO_PROMPT_CSS="#mainPage #promptPanel .autop-title"
        REPORT_TABLE_CSS="TableChart_1"
        TOTAL_NO_OF_VALUES="#"+REPORT_TABLE_CSS+" div[class^='x']"
        
        "---------------------------------------------------------------------------Test Steps--------------------------------------------------------------------------------"
                        
        """ 
        Step 1 :Sign to Webfocus using "rsadv" user
        http://machine:port/ibi_apps
        Step 2:Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Reports/Auto_Link&BIP_item=Store_Product_Quantity_Sold_by_Year.fex
        Verify the Autoprompt window is displayed
        """
        report_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USERNAME, mrpass=PASSWORD, run_table_css=AUTO_PROMPT_CSS, no_of_element=1)
        utillobj.verify_object_visible(AUTO_PROMPT_CSS, True, "Step 02:01: Verify AutoPrompt window is displayed")
        
        """ Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/{alias}/service/wf_security_logout.jsp """
        report_obj.api_logout()
        
        """Step 4:Edit the Report using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Reports/Auto_Link/Store_Product_Quantity_Sold_by_Year.fex&tool=Report"""
        
        report_obj.edit_fex_using_api_url(fex_name=FEX_NAME, folder_name = FOLDER_NAME, mrid=USERNAME, mrpass=PASSWORD)
        report_obj.wait_for_number_of_element(TOTAL_NO_OF_VALUES, 227, LONG_WAIT)
        
        """
        Verify the background color for Product Subcategory.
        Verify the first row value of Report output
        Verify Query Pane,Filter Pane.
        """
        report_obj.verify_report_cell_property(REPORT_TABLE_CSS, 3, bg_color='dim_gray', bg_cell_no=3, text_value="Product", msg="Step 04:01: Verify background color of the table cell")
#         report_obj.create_acrossreport_data_set_in_preview(REPORT_TABLE_CSS, 4, 2, 20, 2, TESTCASE_ID+"_Ds01.xlsx")
        report_obj.verify_across_report_data_set_in_preview(REPORT_TABLE_CSS, 4, 2, 20, 2, TESTCASE_ID+"_Ds01.xlsx", "Step 04:02: Verify preview report data")
        report_obj.verify_report_header_footer_title_in_preview(REPORT_PREVIEW_TITLE, msg="Step 04:03: Verify report title")
        report_obj.verify_all_fields_in_query_pane(QUERY_FIELD_LIST, "Step 04:04: Verify Query panel in preview")
        report_obj.verify_filter_pane_field(FILTER_FIELD1, 1, 'Step 04:05: Verify filter pane field ['+FILTER_FIELD1+'] is available in filterbox')
        report_obj.verify_filter_pane_field(FILTER_FIELD2, 2, 'Step 04:06: Verify filter pane field ['+FILTER_FIELD2+'] is available in filterbox')
        
        
        """Step 5:Click Format tab
        Verify "Auto Link Target" is enabled"""
        
        report_obj.switch_ia_ribbon_tab('Format')
        FORMAT_AUTOLINK_CSS="#FormatAutoLinkCluster #FormatTargetAutoLink"
        report_obj.wait_for_number_of_element(FORMAT_AUTOLINK_CSS, 1, SHORT_TIME)
        web_element=utillobj.validate_and_get_webdriver_object(FORMAT_AUTOLINK_CSS, 'Format Autolink Target Menu')
        report_obj.verify_checked_class_property_for_selected_object(web_element, "Step 04: Verify Auto Link Target is enabled ")
        
        
        """Step 6:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/{alias}/service/wf_security_logout.jsp"""
            
        
if __name__ == "__main__":
    unittest.main()