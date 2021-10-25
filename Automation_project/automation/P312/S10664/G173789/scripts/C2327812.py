'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327812
Test_Case Name : Paperclipping in Line Chart
'''

from common.pages import visualization_metadata, visualization_resultarea
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest

class C2327812_TestClass(BaseTestCase):

    def test_C2327812(self):
        
        """   
            TESTCASE VARIABLES 
        """
       
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """    
            STEP 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite   
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 svg text", 'DropMeasuresorSortsintotheQueryPane', 200)
        
        """    
            Step 02 : Add "Sale, Year" field to Horizontal axis. (Under Sales_Related > Transaction Data, Simple)    
        """
        metadata.datatree_field_click('Sale,Year', 1, 1, 'Add To Query', 'Horizontal Axis')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'Sale Year', 250)
        
        """   
            Step 03 : Click on any riser    
        """
        riser1_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(riser1_ele, coordinate_type='middle', click_type=0)
        
        """    
            Step 04 : Verify the following tooltip info displayed without any error, Group Sale,Year selection" paper clipping option not showing 
        """
        expected_tooltip_list=['1 item selected', 'Filter Chart', 'Exclude from Chart']
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 4. Verify "Group Sale,Year selection" paper clipping option not showing')
        
        """   
            STEP 05 : Logout using API (without saving)   
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()