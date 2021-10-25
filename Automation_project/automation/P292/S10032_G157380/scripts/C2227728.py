'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227728
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227728_TestClass(BaseTestCase):
    def test_C2227728(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227728'
        bar1=['Product Category:Camcorder', 'MSRP:161,574,103.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar2=['Product Category:Televisions', 'Revenue:$78,381,132.81', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar3=['Product Category:Accessories', 'MSRP:135,623,183.37', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar4=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar5=['Product Category:Televisions', 'MSRP:82,016,823.33', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        bar6=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        expected_legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_xval_list=['0', '300', '600', '900', '1,200', '1,500']
        expected_yval_list=['0', '40','80', '120', '160', '200', '240', '280']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult_obj = ia_resultarea.IA_Resultarea(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Select "Home" > "Visual" > "Change" (dropdown) > "Bubble".    """
        ribbonobj.change_chart_type('bubble_chart')
        
        """    3. Drag "Discount" to Vertical Axis.    """
        metaobj.datatree_field_click("Discount", 2, 1)
        time.sleep(8)
        
        """    4. Highlight "Discount" (in Query pane) > Right mouse click > "More" > "Aggregation Functions" > "Average".    """
        metaobj.querytree_field_click('Discount', 1, 1,'More', 'Aggregation Functions', 'Average')
        
        """    5. Verify the following Query pane is displayed.    """
        metaobj.verify_query_pane_field('Vertical Axis', 'AVE.Discount', 1, "Step 05: Verify Aggregation function - Average has been applied for Discount field")
        
        """    6. Drag "Gross Profit" to Horizontal Axis.    """
        metaobj.datatree_field_click("Gross Profit", 1, 1, 'Add To Query', 'Horizontal Axis')
        time.sleep(8)
        
        """    7. Highlight "Gross Profit" (in Query pane) > Right mouse click > "More" > "Aggregation Functions" > "Average".    """
        metaobj.querytree_field_click('Gross Profit', 1, 1,'More', 'Aggregation Functions', 'Average')
        
        """    8. Verify the following Query pane is displayed.    """
        metaobj.verify_query_pane_field('Horizontal Axis', 'AVE.Gross Profit', 1, "Step 08: Verify Aggregation function - Average has been applied for Gross Profit field")
        
        """    9.Drag "Product,Category" to "Marker - Color".    """
        metaobj.datatree_field_click("Product,Category", 1, 1, 'Add To Query', 'Color')
        time.sleep(8) 
        
        """    10. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'AVE Gross Profit', "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'AVE Discount', "Step 10a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend, "Step 10:a(iii) Verify Y-Axis Title")
        expected_xval=['0', '40','80', '120', '160', '200', '240']
        expected_yval=['0', '10','20', '30', '40', '50', '60']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval, expected_yval, "Step 10:a(iv):Verify XY labels")
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody1', 7, 'Step 10:a(v): Verify number of circles in Bubble chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g0!mmarker", "dark_green", "Step 10.b(i): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step 10.b(ii): Verify any circle color")
        
        """    11.Drag "Model" to "Marker - Detail".    """
        metaobj.datatree_field_click("Model", 1, 1, 'Add To Query', 'Detail')
        time.sleep(8)
        
        """    12. Verify the following chart is displayed.    """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'AVE Gross Profit', "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'AVE Discount', "Step 12a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend, "Step 12:a(iii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iv):Verify XY labels")
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody1', 157, 'Step 12:a(v): Verify number of circles in Bubble chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g0!mmarker", "dark_green", "Step 12.b(i): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step 12.b(ii): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g37!mmarker", "pale_yellow", "Step 12.b(iii): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g1!mmarker", "brick_red", "Step 12.b(iv): Verify any circle color")
        
        """    13. Select "Series" tab > "Trendline" (dropdown) > "Linear".    """
        ribbonobj.select_ribbon_item('Series','Trendline',opt='Linear')
        time.sleep(8)
        
        """    14. Verify the following chart is displayed.    """
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody1', 7, 'Step 14(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s1!g0!mtrendline!", "pale_green", "Step 14(ii): Verify any trendline color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s5!g0!mtrendline!", "orange", "Step 14(iii): Verify any trendline color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s6!g0!mtrendline!", "periwinkle_gray", "Step 14(iv): Verify any trendline color", attribute_type='stroke')
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'AVE Gross Profit', "Step 14:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'AVE Discount', "Step 14a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend, "Step 14:a(iii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14:a(iv):Verify XY labels")
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody1', 157, 'Step 14:a(v): Verify number of circles in Bubble chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g0!mmarker", "dark_green", "Step 14.b(i): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step 14.b(ii): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g37!mmarker", "pale_yellow", "Step 14.b(iii): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g1!mmarker", "brick_red", "Step 14.b(iv): Verify any circle color")
                
        """    15. Click "IA" > "Save" > "C2160065" > "Save".    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    16. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    17. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2227728.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    18. Verify the following chart is displayed.    """
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody1', 7, 'Step 18(i): Verify number of Trendline displayed in bubble chart', custom_css="svg>g path[class^='series']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s0!g0!mtrendline!", "bar_blue", "Step 18(ii): Verify first trendline color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s1!g0!mtrendline!", "pale_green", "Step 18(iii): Verify second trendline color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s2!g0!mtrendline!", "dark_green", "Step 18(iv): Verify third trendline color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s3!g0!mtrendline!", "pale_yellow", "Step 18(v): Verify fourth trendline color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s4!g0!mtrendline!", "brick_red", "Step 18(vi): Verify fifth trendline color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s5!g0!mtrendline!", "orange", "Step 18(vii): Verify sixth trendline color", attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "series!s6!g0!mtrendline!", "periwinkle_gray", "Step 18(viii): Verify seventh trendline color", attribute_type='stroke')
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'AVE Gross Profit', "Step 18:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'AVE Discount', "Step 18a(ii): Verify Y-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend, "Step 18:a(iii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18:a(iv):Verify XY labels")
        iaresult_obj.verify_number_of_chart_segment('MAINTABLE_wbody1', 157, 'Step 18:a(v): Verify number of circles in Bubble chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g0!mmarker", "dark_green", "Step 18.b(i): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step 18.b(ii): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g37!mmarker", "pale_yellow", "Step 18.b(iii): Verify any circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g1!mmarker", "brick_red", "Step 18.b(iv): Verify any circle color")
        time.sleep(1)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step18', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        
        """    19. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
                
if __name__ == '__main__':
    unittest.main()

