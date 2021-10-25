'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327807
Test_Case Name : Paperclipping in Line Chart
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.wftools import visualization

class C2327807_TestClass(BaseTestCase):

    def test_C2327807(self):
        
        """   
            TESTCASE VARIABLES 
        """
        visual_obj = visualization.Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
     
        
        '''    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        '''  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite   '''
   
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 svg text", 'DropMeasuresorSortsintotheQueryPane', 190)
        
        '''    Step 02. Click Change drop down and select "Grid"    '''
        
        visul_ribbon.change_chart_type('grid')
        
        '''    Step 03. Add "Product, Category" to ROWS.    '''
        
        metadata.datatree_field_click('Product,Category', 1, 1, 'Add To Query', 'Rows')
        parent_css="#queryTreeColumn table tr:nth-child(3) td"
        utillobj.synchronize_with_visble_text(parent_css, "Product,Category", 190)
        
        '''    Step 04. lasso on the "Product, Category" values. (Accessories, Camcorder, Computers)    '''
        source_element = utillobj.validate_and_get_webdriver_object("rect[class='rowHeader!mcellFill!r0!c0!']", 'source')
        target_element = utillobj.validate_and_get_webdriver_object("rect[class='rowHeader!mcellFill!r2!c0!']", 'target')
        visual_obj.create_lasso(source_element, target_element,target_xoffset=150)
        
        
        ''' Step 05. Verify the following tooltip values displayed, "Group Product, Category selection" option displayed at last    '''
        expected_tooltip_list=['1 item selected', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 4. Verify Group option displaying in the tooltip')
        
        
        '''    '6. Logout using API (without saving)    '''
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()