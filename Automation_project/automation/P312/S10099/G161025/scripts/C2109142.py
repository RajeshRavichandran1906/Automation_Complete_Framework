'''
Created on June 21, 2016

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404 
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109128
'''
__author__ = "Gobinath Thiyagarajan"
__copyright__ = "IBI"

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, core_metadata
from common.lib import utillity
from common.wftools.visualization import Visualization

class C2109142_TestClass(BaseTestCase):
    
    def test_C2109142(self):
        
        """
        TESTCASE VARIABLES
        """ 
        Test_Case_ID = 'C2109142'
        driver = self.driver 
        element_css = '#queryTreeWindow'
        
        """
        CLASS OBJECTS
        """
        visual = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        core_metaobj = core_metadata.CoreMetaData(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        '''Step 01: Launch the IA API  
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F'''
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        '''Step 02: Change to chart type Heatmap.'''
        visual.change_chart_type('heatmap')
        
        '''Step 03: Add Dimensions/Product/Product/Product,Category to Vertical axis '''
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Vertical Axis', 0)
        visual.wait_for_visible_text(element_css, 'Product,Category')
        
        '''  Step 04: Add Dimensions/Store/Store/Attributes/Store Type to Horizontal axis '''
        core_metaobj.collapse_data_field_section('Filters and Variables')
        time.sleep(3)
        core_metaobj.expand_data_field_section('Dimensions->Store->Store->Store Name->Attributes')
        time.sleep(1)
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_script_syntax='document.querySelector("{0}").scrollTop=0'.format(scrollable_element_css)
        driver.execute_script(scroll_script_syntax)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store Type', 1, 'Horizontal Axis', 0)
        time.sleep(6)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Store Type",'Step 04.01: Verify X title Store Type')
        title=driver.find_elements_by_css_selector(".xaxisOrdinal-title")
        utillobj.asequal("Product Category",title[1].text,"Step 04.02: Verify X title Product Category")
        
        '''Step 05:Add Measures/Gross Profit to Color '''
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit', 1, 'Color', 0)
        time.sleep(4)
        
        '''Step 06: Add Dimensions/Shipments_Related/Transaction Date.Simple/Sale,Year to Row'''
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Year', 1, 'Rows', 0)
        
        time.sleep(4)
        
        '''Step 07: Add Dimensions/Shipments_Related/Transaction Date.Simple/Sale,Quarter to Column  '''
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Columns', 0)
        time.sleep(6)
        
        '''Step 08: Verify Label values '''
        tooltip_val=['Sale Year:2011', 'Sale Quarter:1', 'Gross Profit:$347,865.02', 'Product Category:Accessories', 'Store Type:Store Front', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1',"riser!s0!g0!mbar!r0!c0",tooltip_val,"Step 08.01: Verify output value", x_offset=0, y_offset=-7)
         
        '''Step 09:  verify query pane'''
        metaobj.verify_query_pane_field('Vertical Axis', 'Product,Category', 1, 'Step 09.01:  verify query pane')
         
        '''Step 10:  Add Sale,Year to Filter '''
        metaobj.datatree_field_click('Sale,Year',1,1,'Filter')
        metaobj.create_visualization_filters('numeric')
        time.sleep(15)
          
        '''Step 11: Verify query added to filter pane'''
        metaobj.verify_filter_pane_field('Sale,Year',1,'Step 11.01: Verify Sale year query added to filter pane')
         
        '''  Step 12. Drill down on sale,quarter for any product category'''
        utillobj.synchronize_until_element_is_visible("rect[class*='riser!s0!g0!mbar!r0!c0']", 190)
        time.sleep(6)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s5!g0!mbar!r0!c0', 'Drill down to->Sale Month')
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        utillobj.synchronize_with_number_of_element(elem, 3, 190)
         
        '''Step 13: Verify query added to filter pane'''
        time.sleep(5)
        metaobj.verify_filter_pane_field('TIME_YEAR and TIME_QTR and STORE_TYPE and PRODUCT_CATEGORY', 2,  'Step 13.01: Verify query added to filter pane')
         
         
        '''Step 14 : Verify filtered values'''
        tooltip_val=['Sale Year:2011', 'Sale Month:1', 'Gross Profit:$147,867.96', 'Product Category:Televisions', 'Store Type:Store Front', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Quarter', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar!r0!c0',tooltip_val,"Step 14.01: Verify output value")
         
        expected_xval_list=['Store Front', 'Store Front', 'Store Front']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 14.02: X annd Y axis Scales Values has changed or NOT')
         
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "mantis2", "Step 14.03: Verify first bar color")
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 14.04: Verify X-Axis Title")
        time.sleep(8)
         
         
        '''Step 15: Click Run in the toolbar'''
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
         
        '''Step 16: Verify output '''
        time.sleep(5)
        expected_xval_list=['Store Front', 'Store Front', 'Store Front']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 16.01: X annd Y axis Scales Values has changed or NOT')
         
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "mantis2", "Step 16.02: Verify first bar color")
        xaxis_value= "Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16.03: Verify X-Axis Title")
         
        '''Step 17: Close the output window'''
        visual.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", 90)
         
        ''' Step 18: Click "Save" in the toolbar > Type C2109142 > Click "Save" in the Save As dialog'''
        visual.save_visualization_from_top_toolbar(Test_Case_ID)

if __name__ == '__main__':
    unittest.main()