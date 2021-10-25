'''
Created on June 27, 2016

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404 
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140684
'''
__author__ = "Gobinath Thiyagarajan"
__copyright__ = "IBI"

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,  visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.wftools.visualization import Visualization
from common.lib import utillity  

class C2140848_TestClass(BaseTestCase):
    
    def test_C2140848(self):
        
        #Test Variables 
        driver = self.driver #Driver reference object created  
        Test_Case_ID = 'C2140848'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual = Visualization(self.driver)
        
        
        '''Step 01: Launch the IA API with 
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F'''   
        
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        '''Step 02: Change to Grid..'''
        ribbonobj.change_chart_type('grid')
        time.sleep(6)
        
        '''Step 03: Double click "Product,Category" & "Revenue". '''
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text('#queryTreeWindow', 'Product,Category')
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text('#queryTreeWindow', 'Revenue')
        
        '''  Step 04: Verify grid title and data values '''
        visual.wait_for_visible_text(' .tablePanel .rowTitle text', 'Product Category')
        lit =['Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',lit, 'Step 04.01: Verify field titles')       
            
        '''Step 05:Verify query pane '''
        metaobj.verify_query_pane_field('Measure','Revenue',1, 'Step 05.01: Verify query pane') 
        
        '''Step 06: Verify grid data values'''
        time.sleep(4)
        row_val=['Accessories', '$129,608,338.53'] 
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 06.01: verify grid 1st row value')
        time.sleep(4)
        
        '''Step 07: Drag "Product Category" in to filter pane and Deselect "All" and select "Accessories", "Media Players" and "Video Production >OK.. '''
        
        metaobj.querytree_field_click('Product,Category', 1,1, 'Filter Values...')    
        time.sleep(10)
        l = ["[All]","Accessories", "Media Player", "Video Production"]
        metaobj.create_visualization_filters('alpha',['GridItems',l])        
        time.sleep(8)
        
        '''Step 08: Verify query added to filter pane '''
        metaobj.verify_filter_pane_field('Product,Category', 1,'Step 08.01: Verify Sale year query added to filter pane')
        
        
        '''Step 09:  Verify filtered grid values'''
        
        time.sleep(4)        
        row_val2=['Accessories', '$129,608,338.53']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val2,'Step 09.01: verify grid 1st row value')     
        
        
        '''Step 10:  Drag "Revenue" to Filter and Change the Aggregation to "Sum", Change "From" value to "80000000" (80,000,000) > OK. '''
        
        metaobj.querytree_field_click('Revenue', 1, 1,'Filter Values...')
        time.sleep(7)     
        print("IA-6203 issue is there in Creating Filter for Aggregation Sum")   
        metaobj.create_visualization_filters('numeric',['Aggregation','Sum'], ['From','80000000' ])        
        time.sleep(6)
        
        '''Step 11: Verify query added to filter pane'''
        time.sleep(8)
        _step11 = 'Step 11.01:  Verify query added to filter pan'
        metaobj.verify_filter_pane_field('SUM (Revenue)', 2, _step11)
        time.sleep(8)
        
        '''Step 12. Verify filtered grid values with two filters applied.'''
        time.sleep(10)
        row_val3=['Accessories', '$129,608,338.53']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val3,'Step 12.01: verify grid 1st row value')
        rows=len(driver.find_elements_by_css_selector("[class*='row'] rect[class*='riser!s0!']"))
        utillobj.asequal(rows,2,"Step 12.02: Verify 2 filtered rows in preview")
                        
        '''Step 13: Click Run in the toolbar'''
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        visual.switch_to_new_window()   
        
        
        '''Step 14 : Verify output'''
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#MAINTABLE_wbody1 g.rowLabels")
        resultobj._validate_page(elem1)    
        time.sleep(8)  
        row_val4=['Accessories', '$129,608,338.53']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val4,'Step 14.01: verify grid 1st row value')
        rows=len(driver.find_elements_by_css_selector("[class*='row'] rect[class*='riser!s0!']"))
        print("rows "+str(rows)+" present")
        utillobj.asequal(rows,2,"Step 14.02: Verify 2 filtered rows in output - Failure reported")
        time.sleep(10)
        
        '''Step 15: Close the output window'''
        visual.switch_to_previous_window()     
         
        '''Step 16: Click "Save" in the toolbar > Type C2140848 > Click "Save" in the Save As dialog'''
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                
if __name__ == '__main__':
    unittest.main()