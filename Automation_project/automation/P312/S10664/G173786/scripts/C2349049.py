'''
Created on Jan 10, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349049
Test_Case Name : Delete group from query pane
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity

class C2349049_TestClass(BaseTestCase):

    def test_C2349049(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349049'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
             
        """
            Note : Continue from C2349048 test case
            Step 01 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349048.fex
        """
        utillobj.infoassist_api_edit('C2349048', 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 120, string_value='BUSINESS_REGION_1')
        time.sleep(2)
        
        """
            Step 01.1 : Verify preview
        """ 
        visul_result.verify_xaxis_title('MAINTABLE_wbody1_f', 'BUSINESS_REGION_1', 'Step 01.1 : Verify X-Axis title')
        visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Gross Profit', 'Step 01.2 : Verify Y-Axis title')
        visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', ['EMEA and Oceania', 'North America', 'South America'], ['0', '40M', '80M', '120M', '160M', '200M'], 'Step 01.3 :')
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 3, 'Step 01.4 : Verify number of bar chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', 'lochmara', 'Step 01.5 : Verify bar chart riser color')
        
        """
            Step 02 : Right click "BUSINESS_REGION_1" group in query pane
            Step 03 : Click "Delete"
        """
        metadata.querytree_field_click('BUSINESS_REGION_1', 1, 1, 'Delete')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m7!']", 1, 30, string_value='350M')
        
        """
            Step 04 : Verify "BUSINESS_REGION_1" Group is deleted from query
            
        """
        expected_query_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Marker', 'Color', 'Size', 'Tooltip']
        expected_data_fields=['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'BUSINESS_REGION_1']
        metadata.verify_query_panel_all_field(expected_query_fields, 'Step 04.1 : Verify "BUSINESS_REGION_1" Group is deleted from query')
        metadata.verify_all_data_panel_fields(expected_data_fields, 'Step 04.2 : Verify "BUSINESS_REGION_1" Group is available in  data ')
        
        """
            Step 04.3 : Preview updates accordingly and Group still exists in data pane
        """
        visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Gross Profit', 'Step 04.3 : Verify Y-Axis title')
        visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', [], ['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], 'Step 04.3 :')
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 1, 'Step 04.5 : Verify number of bar chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', 'lochmara', 'Step 04.6 : Verify bar chart riser color')
         
        """
            Step 05 : Click View code to view foxexec
            Step 06 : Close foxexec window
        """
        expected_syntax_list=["-*COMPONENT=Define_wf_retail_lite", "DEFINE FILE baseapp/wf_retail_lite", "BUSINESS_REGION_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION ( 'EMEA' 'EMEA and Oceania' 'Oceania' 'EMEA and Oceania' ELSE 'Default');" ,"BUSINESS_REGION_1 = IF BUSINESS_REGION_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION ELSE BUSINESS_REGION_1;"]
        iaresult.verify_fexcode_syntax(expected_syntax_list, 'Step 05.1 : Verify Fex still contains following the group define')
        
        """
            Step 07 : Click IA > Save as "C2349049" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 08 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 09 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349049.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m7!']", 1, 30, string_value='350M')
        time.sleep(2)
        
        """
            Step 09.1 : Restored successfully - No "BUSINESS_REGION_1" Group in query
        """
        metadata.verify_query_panel_all_field(expected_query_fields, 'Step 09.1 : Verify Restored successfully - No "BUSINESS_REGION_1" Group in query')
        metadata.verify_all_data_panel_fields(expected_data_fields, 'Step 09.2 : Verify "BUSINESS_REGION_1" Group is available in  data ')
        
        """
            Step 09.3 : Verify preview
        """
        visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Gross Profit', 'Step 09.3 : Verify Y-Axis title')
        visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', [], ['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], 'Step 09.4 : ')
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 1, 'Step 09.5 : Verify number of bar chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', 'lochmara', 'Step 09.6 : Verify bar chart riser color')
        element=self.driver.find_element_by_id('resultAreaWindowManager')
        utillobj.take_screenshot(element, Test_Case_ID+'_Actual_Step_09')
        
        """
            Step 10 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()