'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327773
Test_Case Name : Paperclipping in Line Chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea
from common.lib import utillity

class C2327773_TestClass(BaseTestCase):

    def test_C2327773(self):
        
        """   
            TESTCASE VARIABLES 
        """
       
        utillobj = utillity.UtillityMethods(self.driver)
        metadata_obj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
     
        
        '''    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        '''  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite   '''
   
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
        
        '''    Step 02 : Double click "Revenue", "Product, Category"    '''
        
        metadata_obj.datatree_field_click('Revenue', 2, 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-title']", 1, 80, string_value='Revenue')
        
        metadata_obj.datatree_field_click('Product,Category', 2, 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Product Category')
        
        time.sleep(2)
        
        
        '''    Step 03 : Click on anyone riser (Accessories)    '''
        
        riser1_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        
        utillobj.click_on_screen(riser1_ele, coordinate_type='middle', click_type=0)
        time.sleep(3)
        
        '''   4. Verify "Group Product, Category Selection" option displaying in the tooltip    '''
        
        expected_tooltip_list=['1 item selected', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 4. Verify Group option displaying in the tooltip')

        
        '''    '5. Click "Group Product, Category Selection"    '''
        
        visul_result.select_or_verify_lasso_filter(select="Group Product,Category Selection", msg='Step 5. Click on the Group selection')
        
        '''    '6. Verify group created and updated in data pane,query pane and Horizontal axis "PRODUCT_CATEGORY_1"    '''
        '''    '7. Hover on any riser and verify tooltip    '''
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metadataobj.collapse_data_field_section('Product')
        time.sleep(5)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        utillobj.verify_object_visible("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", True, 'Step 6.1 Verify PRODUCT_CATEGORY_1 displays in Horizontal axis')
        
        query_ele=self.driver.find_element_by_css_selector("#queryTreeColumn tbody  tr:nth-child(9) td")
        utillobj.asequal(query_ele.text,"PRODUCT_CATEGORY_1",'Step 6.2 Verify PRODUCT_CATEGORY_1 is in query pane')
        
        data_ele=self.driver.find_element_by_css_selector("div[id^='QbMetaDataTree'] table tr:nth-child(11) td")
        utillobj.asequal(data_ele.text,"PRODUCT_CATEGORY_1",'Step 6.3 Verify PRODUCT_CATEGORY_1 is in data pane')
        
        xaxis_value="PRODUCT_CATEGORY_1"
        yaxis_value="Revenue"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 06:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 06:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        expected_yval_list=['0', '50M','100M', '150M', '200M','250M','300M', '350M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 06:c(iii):Verify XY labels")
        
        utillobj.click_on_screen(query_ele, coordinate_type='middle', click_type=3)
        time.sleep(10)
        
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values("MAINTABLE_wbody1_f", 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 7. Verify tooltip values')
        
        '''    8. Logout using API (without saving)    '''
        
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()