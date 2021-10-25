'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327816
Test_Case Name : Bubble chart: Points info and paperclipping in tooltip on Lassoing
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.lib import utillity

class C2327816_TestClass(BaseTestCase):

    def test_C2327816(self):
        
        """   
            TESTCASE VARIABLES 
        """
       
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
     
        
        '''    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        '''  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite   '''
   
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
        
        '''    Step 02. Click Change drop down and Select Bubble chart    '''
        
        visul_ribbon.change_chart_type('bubble_chart')
        
        '''    Step 3. Double click "MODEL", "Revenue"    '''
        
        metadata.datatree_field_click('Model', 2, 1)
        parent_css="#queryTreeColumn  table tr:nth-child(11) > td"
        visul_result.wait_for_property(parent_css, expected_number=1, expire_time=30, string_value="Model")
        
        metadata.datatree_field_click('Revenue', 2, 1)
        parent_css="#queryTreeColumn table tr:nth-child(7) td"
        visul_result.wait_for_property(parent_css, expected_number=1, expire_time=30, string_value="Revenue")
        
        '''    Step 4. Drag and drop "Cost of Goods" to Horizontal axis and "Gross Profit" to Color bucket.    '''
        metadata.datatree_field_click('Cost of Goods', 1, 1, 'Add To Query', 'Horizontal Axis')
#         metadata.drag_and_drop_from_data_tree_to_query_tree('Cost of Goods', 1, 'Horizontal Axis')
        parent_css="#queryTreeColumn  table tr:nth-child(9) > td"
        visul_result.wait_for_property(parent_css, expected_number=1, expire_time=30, string_value="Cost of Goods")
        
        metadata.datatree_field_click('Gross Profit', 1, 1, 'Add To Query', 'Color')
#         metadata.drag_and_drop_from_data_tree_to_query_tree('Gross Profit', 1, 'Color')
        parent_css="#queryTreeColumn  table tr:nth-child(15) > td"
        visul_result.wait_for_property(parent_css, expected_number=1, expire_time=30, string_value="Gross Profit")
        
        '''    Step 5. Verify the bubble chart preview    '''
        
        xaxis_value="Cost of Goods"
        yaxis_value="Revenue"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['0', '3M','6M', '9M', '12M','15M']
        
        expected_yval_list=['0', '4M','8M', '12M', '16M']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 05:c(iii):Verify XY labels")
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g150!mmarker!", "punch1", "Step 05.e: Verify bubble color")
        utillobj.verify_chart_color(parentcss, "riser!s0!g126!mmarker!", "fern", "Step 05.f: Verify bubble color")
        utillobj.verify_chart_color(parentcss, "riser!s0!g13!mmarker!", "jaffa", "Step 05.g: Verify bubble color")
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '1.4M', '2.7M', '4M', '5.4M'], "Step 5.h Verify Legend Values")
        
        '''    Step 6. Lasso some points on Canvas (at top)    '''
        
        visul_result.create_lasso('MAINTABLE_wbody1', 'circle', 'riser!s0!g62!mmarker!',target_tag='circle', target_riser='riser!s0!g102!mmarker!')
        
        
        '''    Step 7. Verify the tooltip value. "Group Model selection" displayed in tooltip    '''
        
        expected_tooltip_list=['22 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Model Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 7. Verify Group Model selection displayed in tooltip')
        
        '''    Step 8. Click Run    '''
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_window(1, pause=3)
        
        parentcss="MAINTABLE_wbody1_f"
        visul_result.wait_for_property("#MAINTABLE_wbody1_f circle[class^='riser!s0!g62!mmarker!']", 1,expire_time=60)
        
        '''    Step 9. Lasso some points on Canvas (at top)    '''
        '''    Step 10. Verify the tooltip value. "Group Model selection" not displayed in tooltip    '''
        
        
        visul_result.create_lasso('MAINTABLE_wbody1', 'circle', 'riser!s0!g62!mmarker!',target_tag='circle', target_riser='riser!s0!g102!mmarker!')
        expected_tooltip_list=['22 items selected', 'Filter Chart', 'Exclude from Chart']
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 10. Verify Group Model selection displayed in tooltip')
        
        '''    Step 11. Dismiss run window    '''
        '''    Step 12. Logout using API (without saving)  '''
        
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()