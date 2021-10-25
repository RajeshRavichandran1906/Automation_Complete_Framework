'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327798
Test_Case Name : Paperclipping in Line Chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2327798_TestClass(BaseTestCase):

    def test_C2327798(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2327798'
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
        
        
        '''    Step 02. Double Click "Cost of Goods" and "Product,Category" to add fields    '''
        metadata_obj.datatree_field_click('Cost of Goods', 2, 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-title']", 1, 80, string_value='Cost of Goods')
        metadata_obj.datatree_field_click('Product,Category', 2, 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Product Category')
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 7, 'Step 2. Verify no of risers')
        time.sleep(2)
        
        '''    Step 03. Lasso over "Accessories", "Camcorder" riser    '''
        visul_result.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g0!mbar!',target_tag='rect', target_riser='riser!s0!g1!mbar!')
        
        '''    Step 04. Click Group Product,Category Selection.    '''
        time.sleep(5)
        visul_result.select_or_verify_lasso_filter(select="Group Product,Category Selection", msg='Step 4. Click on the Group selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metadataobj.collapse_data_field_section('Product')
        time.sleep(5)
        query_ele=self.driver.find_element_by_css_selector("#queryTreeColumn tbody  tr:nth-child(9) td")
        utillobj.asequal(query_ele.text,"PRODUCT_CATEGORY_1",'Step 4.2 Verify PRODUCT_CATEGORY_1 is in query pane')
        data_ele=self.driver.find_element_by_css_selector("div[id^='QbMetaDataTree'] table tr:nth-child(11) td")
        utillobj.asequal(data_ele.text,"PRODUCT_CATEGORY_1",'Step 4.3 Verify PRODUCT_CATEGORY_1 is in data pane')
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M','200M','240M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 04:c(iii):Verify XY labels")
        utillobj.click_on_screen(query_ele, coordinate_type='middle', click_type=3)
        time.sleep(10)
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Cost of Goods:$194,620,755.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values("MAINTABLE_wbody1_f", 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 5. Verify tooltip values')
        
        '''    '5. Lasso over "Televisions", "Video Production"    '''
        '''    '6. Click Group PRODUCT_CATEGORY_1 Selection.    '''
        visul_result.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g4!mbar!',target_tag='rect', target_riser='riser!s0!g5!mbar!')
        time.sleep(3)
        visul_result.select_or_verify_lasso_filter(select="Group PRODUCT_CATEGORY_1 Selection", msg='Step 6. Click on the Group selection')
        time.sleep(5)
        
        
        
        '''    '7. Click on "Televisions and Video Production" riser    '''
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class^='xaxisOrdinal-labels!g4!mgroupLabel!']", 1, 80, string_value='Televisions and Video Production')
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 5, 'Step 7. Verify no of risers')
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Cost of Goods"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 7:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 7:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M','200M','240M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 07:c(iii):Verify XY labels")
        query_ele=self.driver.find_element_by_css_selector("#queryTreeColumn tbody  tr:nth-child(9) td")
        utillobj.click_on_screen(query_ele, coordinate_type='middle', click_type=3)
        time.sleep(10)
        riser1_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g4!mbar!']")
        utillobj.click_on_screen(riser1_ele, coordinate_type='bottom_middle',click_type=0)
        time.sleep(4)
        utillobj.click_on_screen(riser1_ele, coordinate_type='middle', click_type=0)
        time.sleep(3)
        
        '''    '8. Verify the tooltip displayed .    '''
        '''    '8.1. Rename Televisions and Video...    '''
        '''    '8.2. Ungroup Televisions and Video...    '''
        '''    '8.3. Ungroup All    '''
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Televisions and Video...', 'Ungroup Televisions and Video...', 'Ungroup All']
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 8. Verify "Group Sale,Year selection" paper clipping option not showing')
        
        '''    9. Logout using API (without saving)    '''
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()