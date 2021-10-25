'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227699
'''
import unittest
import time, pyautogui
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227699_TestClass(BaseTestCase):
    def test_C2227699(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227699'
        bar1=['Vendor:Sony', 'ID Product:134012', 'Filter Chart', 'Exclude from Chart']
        bar2=['Vendor:LG', 'ID Geography:1098929', 'Filter Chart', 'Exclude from Chart']
        expected_xval_list=['Audio Technica', 'Audiovox', 'BOSE', 'Canon', 'Denon', 'GPX', 'Grado', 'Harman Kardon', 'JVC', 'LG', 'Logitech', 'Magnavox', 'Niles Audio', 'Onkyo', 'Panasonic', 'Philips', 'Pioneer', 'Polaroid', 'Polk Audio', 'Roku', 'Samsung', 'Sanyo', 'Sennheiser', 'Sharp', 'Sony', 'SuperSonic', 'Thomson Grass Valley', 'Tivax', 'Toshiba', 'Yamaha']
        expected_yval_list=['0', '0.5M', '1M', '1.5M','2M', '2.5M', '3M', '3.5M']
        
        """    01: Launch the IA API with wf_retail_product (from dimensions sub app folder), Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
      
        utillobj.infoassist_api_login('idis','baseapp/dimensions/wf_retail_product','P292/S10032_visual_3', 'mrid', 'mrpass')
                
        element_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 190)
        
        """    2. Click 'Join'    """
        ribbonobj.select_ribbon_item('Home','Join')
        time.sleep(4)
        
        parent_css="#dlgJoin #dlgJoin_btnAddMaster img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        
        """    3. Click 'Add New'    """
        """    4. Select wf_retail_vendor (under baseapp\dimensions)    """
        ia_ribbonobj.create_join("baseapp->dimensions","wf_retail_vendor", new_join=False)
         
        """    5. Drag and drop field "ID_VENDOR" from wf_retail_product to "ID_VENDOR" in wf_retail_vendor to create Join link    """
        ia_ribbonobj.create_join_link(0, "ID_VENDOR", 1, "ID_VENDOR", source_scroll_down=5)
        utillobj.synchronize_with_number_of_element("#dlgJoin line[marker-start]", 1, 120)
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 05a: verify Join link created successfully")
         
        """    6. Click 'Blend' in the toolbar    """
        ia_ribbonobj.select_join_menu_buttons("blend")
         
        """    7. Click OK    """
        ia_ribbonobj.select_join_menu_buttons("ok")
        time.sleep(4)
         
        """    8. Verify Fields in Data pane    """
        metaobj.verify_data_pane_field("Dimensions", "Model", 3, "Step 8a: Verify 'Model' is displayed in the Query pane")
        metaobj.verify_data_pane_field("Dimensions", "Vendor Name", 11, "Step 8b: Verify 'Vendor Name' is displayed in the Query pane")
        metaobj.verify_data_pane_field("Measures/Properties", "ID Vendor", 2, "Step 8c: Verify 'ID Vendor' is displayed in the Query pane")
        metaobj.verify_data_pane_field("Measures/Properties", "ID Geography", 9, "Step 8d: Verify 'ID Geography' is displayed in the Query pane")
         
        """    9. Select Calculation -> Detail(Define)    """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        time.sleep(5)
         
        """    10. Double-click "Vendor Name", type Field name "Vendor", change Format to "A30V" Click OK    """
        calculate_obj.enter_define_compute_parameter("Vendor", "A30V", "Dimensions->Vendor Name", 1)
        time.sleep(1)
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(8)
         
        """    11. Double-click fields "Vendor", "ID_Product", "ID_Geography"    """
        metaobj.datatree_field_click("Dimensions->Vendor", 2, 1)
        
        parent_css="#MAINTABLE_wbody1 rect[class*='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 30, 120)
         
        metaobj.datatree_field_click("Measures/Properties->ID Product", 2, 1)
        parent_css="#MAINTABLE_wbody1 rect[class*='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 30, 120)
         
        metaobj.datatree_field_click("Measures/Properties->ID Geography", 2, 1)
        parent_css="#MAINTABLE_wbody1 rect[class*='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 60, 120)
         
        """    12. Click "Save", save as "C2166441", click Save    """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """    13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
         
        """    14. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2166441.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        utillobj.synchronize_with_number_of_element('#applicationButton img', 1, 120)
        time.sleep(10)
         
        """    15. Verify "Vendor" appears in the Data Pane    """
        metaobj.verify_data_pane_field('Dimensions', "Vendor", 12, "Step 15a: Verify 'Vendor' is listed in the Metadata pane")
         
        """    16. Verify Canvas    """
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g24!mbar!", bar1, "Step 16(i): Verify PROFITS bar value")
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g9!mbar!", bar2, "Step 16(ii): Verify Profits bar value")
#         time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Vendor', "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['ID Product','ID Geography'], "Step 16:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 30, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g20!mbar!", "lochmara", "Step 16.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g25!mbar!", "pale_green", "Step 16.c(ii): Verify first bar color")
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    17. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()

