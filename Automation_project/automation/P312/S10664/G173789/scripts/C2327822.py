'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327822
Test_Case Name : Paperclipping in Line Chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2327822_TestClass(BaseTestCase):

    def test_C2327822(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2327822'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata_obj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
     
        
        '''    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        '''  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite   '''
   
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
        
        '''    Step 02. Double click "Cost of Goods" and "Product,Category" to add fields to query    '''
        
        metadata_obj.datatree_field_click('Cost of Goods', 2, 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-title']", 1, 80, string_value='Cost of Goods')
        
        metadata_obj.datatree_field_click('Product,Category', 2, 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Product Category')
        
        time.sleep(2)
        
        
        '''    Step 03. Lasso far right risers "Televisions & Video production" riser    '''
        visul_result.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g5!mbar!',target_tag='rect', target_riser='riser!s0!g6!mbar!')
                
        
        '''    Step 04. Click "Group Product, Category selection"    '''
        
        visul_result.select_or_verify_lasso_filter(select="Group Product,Category Selection", msg='Step 4. Click on the Group selection')
        
        '''    5. Verify following preview displayed. Expected to see Grouped "Televisions and Video production" one riser and other risers    '''
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metadataobj.collapse_data_field_section('Product')
        time.sleep(5)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        utillobj.verify_object_visible("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", True, 'Step 5.1 Verify PRODUCT_CATEGORY_1 displays in Horizontal axis')
        
        query_ele=self.driver.find_element_by_css_selector("#queryTreeColumn tbody  tr:nth-child(9) td")
        utillobj.asequal(query_ele.text,"PRODUCT_CATEGORY_1",'Step 5.2 Verify PRODUCT_CATEGORY_1 is in query pane')
        
        data_ele=self.driver.find_element_by_css_selector("div[id^='QbMetaDataTree'] table tr:nth-child(11) td")
        utillobj.asequal(data_ele.text,"PRODUCT_CATEGORY_1",'Step 5.3 Verify PRODUCT_CATEGORY_1 is in data pane')
        
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        
        expected_yval_list=['0', '40M', '80M', '120M', '160M','200M','240M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 06:c(iii):Verify XY labels")
        
        utillobj.click_on_screen(query_ele, coordinate_type='middle', click_type=3)
        time.sleep(10)
        
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Televisions and Video Production', 'Cost of Goods:$101,656,766.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values("MAINTABLE_wbody1_f", 'riser!s0!g5!mbar!', expected_tooltip_list, 'Step 5. Verify tooltip values')
        
        '''    '6. Click Run    '''
        '''    '7. Verify run time chart    '''
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_window(1, pause=3)
        
        parentcss="MAINTABLE_wbody1_f"
        visul_result.wait_for_property("#MAINTABLE_wbody1_f circle[class^='riser!s0!g5!mbar!']", 1,expire_time=60)
        
        utillobj.verify_object_visible("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", True, 'Step 7.1 Verify PRODUCT_CATEGORY_1 displays in Horizontal axis')
        
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        
        expected_yval_list=['0', '40M', '80M', '120M', '160M','200M','240M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 07:c(iii):Verify XY labels")
        
#         utillobj.click_on_screen(query_ele, coordinate_type='middle', click_type=3)
#         time.sleep(10)
        
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Televisions and Video Production', 'Cost of Goods:$101,656,766.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values("MAINTABLE_wbody1_f", 'riser!s0!g5!mbar!', expected_tooltip_list, 'Step 7.2 Verify tooltip values')
        
        '''    8. Dismiss run window    '''
        '''    9. Click Save in the toolbar > Save as "C2327822" > Click Save    '''
        '''    10. Logout using API. http://machine:port/ibi_apps/service/wf_security_logout.jsp   '''
        
        self.driver.close()
        
        utillobj.switch_to_window(0, pause=3)
        
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        utillobj.infoassist_api_logout()
        
        '''    11. Reopen the saved fex. http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2327822.fex    '''
        '''    12. Verify successfully restored    '''
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        
        utillobj.verify_object_visible("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", True, 'Step 12.1 Verify PRODUCT_CATEGORY_1 displays in Horizontal axis')
        
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        
        expected_yval_list=['0', '40M', '80M', '120M', '160M','200M','240M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 12:c(iii):Verify XY labels")
        
        query_ele=self.driver.find_element_by_css_selector("#queryTreeColumn tbody  tr:nth-child(9) td")
        utillobj.asequal(query_ele.text,"PRODUCT_CATEGORY_1",'Step 12.3 Verify PRODUCT_CATEGORY_1 is in query pane')
        
        data_ele=self.driver.find_element_by_css_selector("div[id^='QbMetaDataTree'] table tr:nth-child(11) td")
        utillobj.asequal(data_ele.text,"PRODUCT_CATEGORY_1",'Step 12.4 Verify PRODUCT_CATEGORY_1 is in data pane')
        
        utillobj.click_on_screen(query_ele, coordinate_type='middle', click_type=3)
        time.sleep(10)
        
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Televisions and Video Production', 'Cost of Goods:$101,656,766.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values("MAINTABLE_wbody1_f", 'riser!s0!g5!mbar!', expected_tooltip_list, 'Step 12.2 Verify tooltip values')
        
        '''    8. Logout using API (without saving)    '''
        
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()