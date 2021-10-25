'''
Created on Jan 11, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349051
Test_Case Name : Delete group from data pane
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity


class C2349051_TestClass(BaseTestCase):

    def test_C2349051(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349051'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        def verify_bar_chart(step_num):
            visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Gross Profit', 'Step ' + step_num + '.1 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', [], ['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M'], 'Step ' + step_num + '.2 :')
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 1, 'Step ' + step_num + '.3 : Verify number of bar chart risers')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', 'lochmara', 'Step ' + step_num + '.4 : Verify bar chart riser color')
            
        """
            Note : Continue from C2349049 test case
            Step 01 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349049.fex
        """
        utillobj.infoassist_api_edit('C2349049', 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-labels!m7!']", 1, 120, string_value='350M')
        time.sleep(2)
            
        """
            Step 01.1 : Verify preview
        """ 
        verify_bar_chart('01')
        
        """
            Step 02 : Right click "BUSINESS_REGION_1" group in Data pane
            Step 03 : Click "Delete"
        """
        metadata.datatree_field_click('Dimensions->BUSINESS_REGION_1', 1, 1, 'Delete')
        visul_result.wait_for_property("#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']", 10, 30)
        
        """
            Step 04 : Verify "BUSINESS_REGION_1" Group is deleted from Data pane
        """
        verify_bar_chart('04')
        metadata.verify_all_data_panel_fields(['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer'], 'Step 04.5 : Verify "BUSINESS_REGION_1" Group is deleted from Data pane')
        metadata.verify_query_panel_all_field(['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Marker', 'Color', 'Size', 'Tooltip'], 'Step 04.6 : Verify query panel')
        
        """
            Step 05 : Verify following Group define is not in fex
        """
        expected_syntax_list=["BUSINESS_REGION_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION ( 'EMEA' 'EMEA and Oceania' 'Oceania' 'EMEA and Oceania' ELSE 'Default');" ,"BUSINESS_REGION_1 = IF BUSINESS_REGION_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION ELSE BUSINESS_REGION_1;"]
        iaresult.verify_syntax_not_in_fexcode(expected_syntax_list, 'Step 05.1 : Verify following Group define is not in fex')
        
        """
            Step 06 : Click IA > Save as "C2349051" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 07 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 08 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349051.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-labels!m7!']", 1, 120, string_value='350M')
        time.sleep(2)
        
        """
            Step 08.1 : Restored successfully - No "BUSINESS_REGION_1" Group in data pane 
        """
        verify_bar_chart('08')
        metadata.verify_all_data_panel_fields(['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer'], 'Step 08.5 : Verify No "BUSINESS_REGION_1" Group in data pane ')
        metadata.verify_query_panel_all_field(['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Marker', 'Color', 'Size', 'Tooltip'], 'Step 08.6 : Verify query panel')
        visul_result.verify_default_tooltip_values("MAINTABLE_wbody1_f", "riser!s0!g0!mbar!", ['Gross Profit:$299,753,396.20'], 'Step 08.7 : Verify tooltip')
        element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(element, Test_Case_ID+'_Actual_Step_08')
        
        """
            Step 09 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()