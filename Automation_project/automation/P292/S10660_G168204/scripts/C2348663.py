'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348663
Test case Name =  Verify Map with Define and Compute
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, define_compute, ia_run, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2348663_TestClass(BaseTestCase):

    def test_C2348663(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        driver.implicitly_wait(15)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2348663"
        Test_fex_name="C2348663"

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/10660', 'mrid', 'mrpass')
        #time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        #time.sleep(6)
          
          
        """    2. Go to Format tab    """
        """    3. Click "Proportional Symbol" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
#         ribbonobj.switch_ia_tab('Format')
#         
        ribbonobj.switch_ia_tab('Home')
        time.sleep(6)
        
        
        
        
        """    "4. Go to Data tab > "Detail (Define)"    """
        """     5. Enter "Countries" in Field; Set "Format" = A40V; Double click "Store,Country"    """
        """    "6. Click OK    """
        
        
        defcomp.invoke_define_compute_dialog('define')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        defcomp.enter_define_compute_parameter("Countries", 'A40V', 'Store,Country', 1)
        defcomp.close_define_compute_dialog('ok')
        
        """    "7. Double click "Countries" in the Data pane    """
        """    "8. Set "Geographic Role" = "Country";Set "Stored As" = "Name"    """
        """    "9. Click OK    """
        
        metaobj.datatree_field_click("Countries", 2, 1)
        time.sleep(5)
        wfmapobj.set_geo_role(role_name='Country', store_as='Name', btn_click='Ok')
      

        """    10. Verify the map is updated    """
        
        parentcss="pfjTableChart_1"
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g4!mmarker!", 'bar_blue', 'Step 10.1a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mmarker!", 'bar_blue', 'Step 10.1b Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step10'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    11. Click "Summary (Compute)" in the Data tab    """
        """    12. Enter "Store_Revenue" in Field Double click "Revenue"; Set "Format" = D20.2    """
        """    13. Click OK    """
        defcomp.invoke_define_compute_dialog('compute')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        defcomp.enter_define_compute_parameter("Store_Revenue", 'D20.2', 'Revenue', 1)
        defcomp.close_define_compute_dialog('ok')
        
        """    14. Verify the map is updated    """

        parentcss="pfjTableChart_1"
        expected_label_list=['Store_Revenue']
        msg="Step 12.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Store_Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.1. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 14.2a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 14.2b Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step14'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    15. Click "Run"    """
        """    16. Hover over United States bubble    """
        """    17. Verify the map and tooltip are displayed correctly    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1)
        
        
        expected_label_list=['Store_Revenue']
        msg="Step 17.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Store_Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 17.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 17.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 17.3b Verify map color')
        
        expected_tooltip=['Countries:United States', 'Store_Revenue:545,792,166.41']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g33!mmarker!",expected_tooltip, "Step 17.4: Verify Tooltip is displayed correctly")
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step17'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)


        
        """    18. Click "Save" icon    """
        """    19. Enter Title "C2229085"    """
        """    20. Click "Save" and dismiss IA window    """
        utillobj.switch_to_default_content(pause=3)

        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_fex_name)
        time.sleep(5)
        
        
        """    21. Reopen the fex using API code:    """
        """    22. Verify IA is launched, preserving the map    """
        """    23. Dismiss IA window    """
        """    24. Log out :    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_fex_name, 'chart', 'P292/S10660', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#pfjTableChart_1', 1)
        time.sleep(10)
        parentcss="pfjTableChart_1"
        expected_label_list=['Store_Revenue']
        msg="Step 22.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Store_Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 22.1. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 22.2a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 22.2b Verify map color')        
        

        
if __name__ == '__main__':
    unittest.main()
    
        