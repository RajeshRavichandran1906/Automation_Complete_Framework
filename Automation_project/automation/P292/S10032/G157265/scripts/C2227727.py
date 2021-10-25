'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227727
'''
import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,active_miscelaneous

class C2227727_TestClass(BaseTestCase):
    
    def test_C2227727(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227727'
        bar1=['Product Category:Accessories', 'MSRP:135,623,183.37', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M','100M', '150M', '200M', '250M', '300M', '350M']
        
        """
            CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        misc_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        
        """    
            STEP 01 : Launch the IA API with wf_retail_lite, Visualization mode:
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", 'Drop Measures', 120)
        
        """    
            STEP 02 : Select "Home" > "Visual" > "Change" (dropdown) > "Line".    
        """
        ribbonobj.change_chart_type('line')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1 path[class*='riser!s0!g0!mline!']", 15)
        
        """    
            STEP 03 : Double click Product,Category".    
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1 text.xaxisOrdinal-title", 'Product Category', 20)
        
        """    
            STEP 04 : Double click "MSRP" and "Revenue".    
        """
        metaobj.datatree_field_click("MSRP", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1 text.yaxis-title", 'MSRP', 20)
        
        metaobj.datatree_field_click("Revenue", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='legend-labels!s1!']", 'Revenue', 20)
        
        """    
            STEP 05 : Verify the following chart is displayed.    
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 05.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 05.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 05.03: Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mline!", "lochmara", "Step 05.04: Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mline!", "pale_green", "Step 05.05: Verify first bar color", attribute_type='stroke')
        
        """    
            STEP 06 : Verify hover (tooltip) is working properly.    
        """
        misc_obj.select_or_verify_marker_tooltip(marker_class='marker!s0!g0!mmarker!',verify_tooltip_list=bar1, msg='Step 06.01: Verify MSRP line value',parent_css='#MAINTABLE_wbody1')
        
        """    
            STEP 07 : Click "Run".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1 text.xaxisOrdinal-title", 'Product Category', 120)
        
        """    
            STEP 08 : Verify the following chart is displayed.    
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 08.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 08.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08.03: Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mline!", "lochmara", "Step 08.04: Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mline!", "pale_green", "Step 08.05: Verify first bar color", attribute_type='stroke')
       
        self.driver.close()
        utillobj.switch_to_window(0)
    
        """    
            STEP 09 : Click Save in the toolbar > Save as "C2227727" > Click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
            STEP 10 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        utillobj.infoassist_api_logout()
        
        """    
            STEP 11 : Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227727.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1 text.xaxisOrdinal-title", 'Product Category', 160)
        
        """     
            STEP 12 : Verify the following chart is displayed.    
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 12.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 12.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.03: Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mline!", "lochmara", "Step 12.04: Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mline!", "pale_green", "Step 12.05: Verify first bar color", attribute_type='stroke')
        
        """    
            STEP 13 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
                
if __name__ == '__main__':
    unittest.main()