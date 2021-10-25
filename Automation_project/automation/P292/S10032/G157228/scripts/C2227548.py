'''
Created on 03-Nov-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227548
TestCase Name = Verify Chart with Auto Link, Auto Drill, and Multi Drill using wf_retail_lite 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227548_TestClass(BaseTestCase):
    
    def test_C2227548(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """    1. Reopen fex using IA API:Chart_Source01a.fex using tool=chart    """
        utillobj.infoassist_api_edit("Chart_Source01", "chart", "S7385")
        parent_css="input[id=SignonUserName]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        parent_css="#TableChart_1 rect[class^='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    2. Select "Format" > "Auto Drill" (from Navigation group)    """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        
        """    3. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=15)
        utillobj.switch_to_frame(frame_css='iframe[src]')
        time.sleep(3)
        parent_css="rect[class*='riser!s0!g1!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 03.00: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 03.01: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 03.02: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 03.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 03.04: Verify Y-Axis Title")
        
        """    4. Hover over on Chart riser "Stereo systems"    """
        """    5. Verify the Autolink,Autodrill and Multidrill menus are displayed    """
        expected_tooltip=['Product Category:Stereo Systems', 'Revenue:$291,294,933.52', 'Drill down to Product Subcategory', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g4!mbar",expected_tooltip, "Step 05.00: verify the default tooltip values")
        
        """    6.Hover over on Chart riser "Media Player > Select "Drilldown to Product Subcategory"   """
        time.sleep(4)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g3!mbar", "Drill down to Product Subcategory", wait_time=1)
        
        """    7. Verify the following "Chart"    """
        time.sleep(1)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.switch_to_frame()
        utillobj.switch_to_frame(frame_css='iframe[src]')
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 4, 'Step 07.00: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 07.01: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 07.02: Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 07.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 07.04: Verify Y-Axis Title")
        
        """    8. Hover over on Chart riser "Blu Ray" > Select "Drill down to Model"    """
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g0!mbar", "Drill down to Model", wait_time=2)
        
        """    9. Verify the following "Chart"    """
        utillobj.switch_to_default_content()
        time.sleep(8)
        utillobj.switch_to_frame()
        utillobj.switch_to_frame(frame_css='iframe[src]')
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 21, 'Step 09.00: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['JVC XV-BP1', 'JVC XV-BP10', 'JVC XV-BP11', 'Panasonic DMP-BD30', 'Panasonic DMP-BD60', 'Panasonic DMP-BD70V', 'Panasonic DMP-BD80', 'Pioneer BDP-120', 'Pioneer BDP-320', 'Pioneer BDP-330', 'Pioneer BDP-51', 'SAMSUNG BD-C6500', 'SHARP BD-HP70U', 'Samsung BD-C5500', 'Samsung BD-P1600', 'Samsung BD-P3600', 'Sharp BD-HP24U', 'Sony BDP-S360', 'Sony BDP-S370', 'Sony BDP-S470', 'Sony BDP-S570']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 09.01: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 09.02: Verify first bar color")
        xaxis_value="Model"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 09.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 09.04: Verify Y-Axis Title")
        
        """    10. Hover over on Chart riser "JVCXV-BP11" > Select "Drill up to Product Subcategory"    """
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g2!mbar", "Drill up to Product Subcategory", wait_time=2)
        utillobj.synchronize_with_number_of_element('#jschart_HOLD_0  svg g.risers >g>rect[class^="riser"]', 4, 30)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 4, 'Step 10.00: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 10.01: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 10.02: Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 10.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 10.04: Verify Y-Axis Title")
        
        """    11. Hover over on Chart riser "DVD Players" > Select "Restore Original"    """
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g1!mbar", "Restore Original", wait_time=2)
        
        """    12. Verify the "Chart" is reverted back to Original stage    """
        utillobj.synchronize_with_number_of_element('#jschart_HOLD_0  svg g.risers >g>rect[class^="riser"]', 7, 30)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 12.00: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 12.01: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 12.02: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 12.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 12.04: Verify Y-Axis Title")
        utillobj.switch_to_default_content()
        time.sleep(2)
        
        """    13. Click IA > "Save"    """
        """    14. Verify the message "Report Saved Successfully" > Click OK    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("Chart_Source01b")
        time.sleep(5)
        
        """    15. Click "Run"    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(4)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(frame_css='iframe[src]')
        
        """    16. Verify the Chart and hover on any chart riser verify the menus    """
        parent_css="rect[class*='riser!s0!g1!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 16.00: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 16.01: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 16.02: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 16.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 16.04: Verify Y-Axis Title")
        utillobj.switch_to_default_content()
        
        """    17. Close the Chart window    """
        """    18. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()