'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197847
TestCase Name = Run with autodrill on map with GIS Point field crashes
'''
import unittest, time
from common.lib import utillity  
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, metadata

class C2197847_TestClass(BaseTestCase):
    
    def test_C2197847(self):
        
        """
        Class & Objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """
        Testcase Variables
        """
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2197847_"+browser_type
        
        """    1.  Open a new chart with wf_retail_lite using the API,    """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P276/S9976', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        utillobj.wait_for_page_loads(ribbonobj.home_page_long_timesleep)
        
        """    2. Select Format > ESRI Proportional Symbol    """
        ribbonobj.select_ribbon_item("Format", "Proportional_symbol")
        time.sleep(4)
        
        """    3. Double click Quantity,Sold to add it to Size, Drag Store,Country,Capital,GIS,Point to Layer  """
        metaobj.datatree_field_click('Quantity,Sold', 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'Quantity,Sold', 30)
        metadataobj.collapse_data_field_section('Measure Groups')
        time.sleep(2) 
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Country,Capital,GIS Point',1,'Layer',0)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'Store,Country,Capital,GIS Point', 30)
        
        metaobj.verify_query_pane_field("Size", "Quantity,Sold", 1, "Step 03.01: Verify Quantity,Sold added in Size")
        metaobj.verify_query_pane_field("Layer", "Store,Country,Capital,GIS Point", 1, "Step 03.02: Verify Store,Country,Capital,GIS,Point added in Layer")
        time.sleep(4)
        parentcss="pfjTableChart_1"
        element_css="#pfjTableChart_1 text[class^='legend-labels']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 60, 1)
        expected_label_list=['Quantity Sold']
        msg="Step 03.03: Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Quantity Sold']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 03.04: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        element_css="#pfjTableChart_1 circle[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(element_css, 34, 20, 1)
        utillobj.verify_chart_color(parentcss, "riser!s0!g8!mregion!", 'bar_blue', 'Step 03.05: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g11!mregion!", 'bar_blue', 'Step 03.06: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g14!mregion!", 'bar_blue', 'Step 03.07: Verify map color')
        
        """    4. Click Format tab > Autodrill button   """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(8)
        
        """    5. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        chart_type_css="circle[class*='riser!s0!g8!mregion!"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parentcss1="jschart_HOLD_0"
        msg="Step 05.01: Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_title_list, 'Step 05.02: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        time.sleep(5)
        element_css="#jschart_HOLD_0 circle[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(element_css, 34, 20, 1)
        utillobj.verify_chart_color(parentcss1, "riser!s0!g8!mregion!", 'bar_blue', 'Step 05.03: Verify map color')
        utillobj.verify_chart_color(parentcss1, "riser!s0!g11!mregion!", 'bar_blue', 'Step 05.04: Verify map color')
        utillobj.verify_chart_color(parentcss1, "riser!s0!g14!mregion!", 'bar_blue', 'Step 05.05: Verify map color')        
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        time.sleep(4)
        
        """    6. Click "Save" in the toolbar > Type C2197847 > Click "Save" in the Save As dialog    """
        ribbonobj.select_top_toolbar_item("toolbar_save")
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
          
        """    7. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()