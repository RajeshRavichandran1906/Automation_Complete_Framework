'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227726
'''
import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon

class C2227726_TestClass(BaseTestCase):
    
    def test_C2227726(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227726'
        bar1=['Product Category:Camcorder', 'MSRP:161,574,103.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar2=['Product Category:Televisions', 'Revenue:$78,381,132.81', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar3=['Product Category:Accessories', 'MSRP:135,623,183.37', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar4=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '100M','200M', '300M', '400M', '500M', '600M', '700M']
        
        """
            CLASS OBJEECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
      
        """    
            STEP 01 : Launch the IA API with wf_retail_lite, Visualization mode:
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", 'Drop Measures', 120)
        
        """    
            STEP 02 : Select "Home" > "Visual" > "Change" (dropdown) > "Bar".    
        """
        ribbonobj.change_chart_type('stacked_bar')
        
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
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 5:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 5:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 5:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 5.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "lochmara", "Step 5.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 5.c(ii): Verify first bar color")
        
        """    
            STEP 6 : Verify hover (tooltip) is working properly.    
        """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", bar1, "Step 6(i): Verify MSRP bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar2, "Step 6(ii): Verify Revenue bar value")
               
        """    
            STEP 7 : Click "Run".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1 text.xaxisOrdinal-title", 'Product Category', 120)
        
        """    
            STEP 08 : Verify the following chart is displayed.    
        """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar3, "Step 8(i): Verify MSRP bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g3!mbar!", bar4, "Step 8(ii): Verify Revenue bar value")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 8:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 8:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 8:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 8.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 8.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g5!mbar!", "pale_green", "Step 8.c(ii): Verify first bar color")
        
        """    
            STEP 0 9 : Dismiss the "Run" window.    
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """    
            STEP 10 : Click "IA" > "Save" > "C2160065" > "Save".   
        """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
            STEP 11 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        utillobj.infoassist_api_logout()
        
        """    
            STEP 12 : Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160065.fex&tool=idis    
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1 text.xaxisOrdinal-title", 'Product Category', 160)
        
        """    
            STEP 12.01 : Verify the following chart is displayed.    
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['MSRP','Revenue'], "Step 12:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!", "lochmara", "Step 12.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g6!mbar!", "pale_green", "Step 12.c(ii): Verify first bar color")
                
        """    
            STEP 13 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
                
if __name__ == '__main__':
    unittest.main()