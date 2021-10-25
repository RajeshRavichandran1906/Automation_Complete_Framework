'''
Created on 03-Nov-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227547
TestCase Name = Verify Chart with Auto Link and Multi Drill using wf_retail_lite
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity
from common.lib import core_utility   
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
import time
        
class C2227547_TestClass(BaseTestCase):
    
    def test_C2227547(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Testcase css
        """
        querytree_css = "#queryTreeWindow"
        
        """    1. Launch the IA API with WF_RETAIL_LITE, Chart mode:
                    http://machine:port/ibi_apps/ia?tool=chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F    """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        parent_css1="#TableChart_1 rect[class^='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css1, 1, 190)
          
        """    2. Double click "Product,Category","Revenue"    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        visual_obj.wait_for_visible_text(querytree_css, "Product,Category")
        
        metaobj.datatree_field_click("Revenue", 2, 1)
        visual_obj.wait_for_visible_text(querytree_css, "Revenue")
          
        """    3. Verify the following Chart in Live Preview    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 03.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 03.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03.05: Verify Y-Axis Title")
          
        """    4. Select "Format" > "Enable Auto Linking".    """
        ribbonobj.switch_ia_tab("Format")
        if utillobj.validate_and_get_webdriver_object("#FormatAutoLinkCluster", 'autolink').value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=utillobj.validate_and_get_webdriver_object("#FormatAutoLinkCluster_altButton img", 'cluster-button')
            core_utillobj.left_click(autolink_altbtn)
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
          
        """    5. Click "IA" > "Save" > Enter "Title:" = "Chart_Source01", click "Save".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("Chart_Source01")
          
        """    6. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
          
        """    7. Launch the IA API with WF_RETAIL_LITE, Chart mode:
                    http://machine:port/ibi_apps/ia?tool=chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        parent_css1="#TableChart_1 rect[class^='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css1, 1, 190)
          
        """    8. Double click "Product,Category","Gross_Profit"    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        visual_obj.wait_for_visible_text(querytree_css, "Product,Category")
        
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        visual_obj.wait_for_visible_text(querytree_css, "Gross Profit")
          
        """    9. Drag and drop "Product,Category" into Filter panel    """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        visual_obj.wait_for_visible_text("#dlgWhere_btnCancel", "Cancel")
          
        """    10. Double click "<Value>", set "Type:" = "Parameter", click "OK" (2x).    """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
        visual_obj.wait_for_visible_text("#qbFilterBox", "Product")
        
        """    11. Verify "Filter" is created    """
        metaobj.verify_filter_pane_field('Product,Category Equal to Simple Parameter (Name: PRODUCT_CATEGORY)', 1, "Step 11a")
          
        """    12. Select "Format" > "Auto Link Target".    """
        ribbonobj.switch_ia_tab("Format")
        if utillobj.validate_and_get_webdriver_object("#FormatAutoLinkCluster", 'cluster').value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=utillobj.validate_and_get_webdriver_object("#FormatAutoLinkCluster_altButton img", 'cluster img')
            core_utillobj.left_click(autolink_altbtn)
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
          
        """    13. Click "IA" > "Save As" > Enter "Title:" = "Chart_Target01", click "Save"    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("Chart_Target01")
          
        """    14. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
         
        """    15. Reopen fex using IA API:    """        
        utillobj.infoassist_api_edit("Chart_Source01", "chart", "S7385", mrid='mrid', mrpass='mrpass')
        parent_css1="#TableChart_1 rect[class^='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css1, 1, 190)
         
        """    16. Click field "Revenue", click "Drill Down" on the Ribbon    """
        metaobj.querytree_field_click("Revenue", 1)
        utillobj.synchronize_with_number_of_element("#FieldDrillDown img", 1, metaobj.chart_medium_timesleep)
        drilldown_btn = utillobj.validate_and_get_webdriver_object("#FieldDrillDown img", 'drilldownimage')
        core_utillobj.left_click(drilldown_btn)
         
        """    17. Click "Web Page" radio button    """
        """    18. Click URL input box -> Type "http://www.ibi.com"    """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.ibi.com')
         
        """    19. Click "Create a new drill down" button    """
        new_btn=utillobj.validate_and_get_webdriver_object("#drillDownNew img", 'image')
        core_utillobj.left_click(new_btn)
         
        """    20. Click "Web Page" radio button    """
        """    21. Click URL input box -> Type "http://www.bbc.com"    """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.bbc.com')
          
        """    22. Verify the following drilldown window    """
        ia_ribbonobj.create_drilldown_report('webpage', verify_left_pane=['1', 'Drill Down 1'], msg="Step 22.01: Verify Drill Down 1 displayed on left side")
        ia_ribbonobj.create_drilldown_report('webpage', verify_left_pane=['2', 'Drill Down 2'], msg="Step 22.02: Verify Drill Down 1 displayed on left side")
         
        """    23. Click OK    """
        ia_ribbonobj.create_drilldown_report('webpage', click_ok="yes")
         
        """    24. Click "IA" > Click Save > Click OK to message    """
        ribbonobj.select_tool_menu_item('menu_save')
        ok_css = "div[id^='BiDialog'] div[id^='BiOption'] .bi-button-label"
        ok_button = utillobj.validate_and_get_webdriver_object(ok_css, 'ok')
        core_utillobj.left_click(ok_button)
        
        """    25. Click "IA" > click "Run"    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utillobj.switch_to_frame()
        parent_css1="rect[class*='riser!s0!g1!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css1, 1, 30)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 25.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 25.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 25.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 25.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 25.05: Verify Y-Axis Title")
        
        """    26. Hover over on Chart riser "Computers "    """
        """    27. Verify the Autolink and Multidrill menus are displayed    """
        expected_tooltip=['Product Category:Computers', 'Revenue:$103,316,482.12', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g2!mbar",expected_tooltip, "Step 27.01: verify the default tooltip values")
        time.sleep(10)
        
        """    28. Hover over "Autolink" > Select "Chart_Target01"    """
        
        visual_obj.select_tooltip("riser!s0!g2!mbar", "Auto Links->Chart_Target01", "jschart_HOLD_0", move_to_tooltip = True)
        
        """    29. Verify "Chart_Target01" is displayed in a new window    """
        core_utillobj.switch_to_default_content()
        core_utillobj.switch_to_new_window()
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 1, 'Step 29.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Computers']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 29.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 29.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 29.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 29.05: Verify Y-Axis Title")
        
        """    30. Close the window    """
        core_utillobj.switch_to_previous_window()
        
        """    31. Select "Camcorder" > Click "Drill down1"    """
        core_utillobj.switch_to_frame()
        visual_obj.select_tooltip("riser!s0!g1!mbar", "Drill Down 1", "jschart_HOLD_0")
        
        """    32. Verify it displays a new window going to IBI site    """
        core_utillobj.switch_to_default_content()
        core_utillobj.switch_to_new_window()
        drill1=driver.current_url
        utillobj.asin('ibi', drill1, "Step 32.01: Verify IBI page is displayed")
        
        """    33. Close the IBI window    """
        core_utillobj.switch_to_previous_window()
        
        """    34. Select "Stereo Systems" > Click "Drill down2"    """
        core_utillobj.switch_to_frame()
        visual_obj.select_tooltip("riser!s0!g1!mbar", "Drill Down 2", "jschart_HOLD_0")
        
        """    35. Verify it displays a new window going to "BBC" site.    """
        core_utillobj.switch_to_default_content()
        core_utillobj.switch_to_new_window()
        drill2=driver.current_url
        utillobj.asin('bbc', drill2, "Step 35.01: Verify BBC page is displayed")
        
        """    36. Close the BBC window    """
        core_utillobj.switch_to_previous_window()
        
        """    37. Close the "Chart" window    """
        """    38. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()