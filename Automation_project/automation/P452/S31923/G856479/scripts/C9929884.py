#for local testing
import sys
sys.path.append('../../')
#*************************

import unittest
from utility.selenium_utility import Selenium_Utility, ParisHomeUtility, DesignerUtility, PortalRuntimeUtility
from utility.locators import ParisHomeLocators, DesignerLocators, PortalRuntimeLocators
from utility.basetestcasedocker import BaseTestCaseDocker

class C9929884_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9929884_TestClass, self).__init__(driver)
    
    def test_C9929884(self):        
        case_id = 'C9929884'
        master_name = "car"
        folder_name = "Responsive Demo"
        eda_folder_name = "ibisamp"
        page_name = "Unified_2" 
        chart_2 = "Unified_1" 
        portal_name = "test portal2" 
        my_pages = "My Pages"
        my_content = "My Content"
         
        sel_util = Selenium_Utility(self.driver)
        
        #Log into WF
        sel_util.login_wf()
      
        home_util = ParisHomeUtility(self.driver)
      
        home_util.create_content('create')
             
        sel_util.switch_to_window(2)
             
        df_util = DesignerUtility(self.driver)
                     
        #Select a master file
        df_util.select_data_source(master_name, folder_name, eda_folder_name)
             
        country = df_util.search_for_field('COUNTRY')
        df_util.add_field(country)
             
        sales = df_util.search_for_field('SALES')
        df_util.add_field(sales)
             
        df_util.convert_to_page()
             
        df_util.add_visualization()
             
        #Change Chart type
        df_util.change_chart_type("Ring Pie")
     
        car = df_util.search_for_field('CAR')
        df_util.add_field(car) 
     
        d_cost = df_util.search_for_field('DEALER_COST')
        df_util.add_field(d_cost)
     
        df_util.add_visualization()    
             
        #Change Chart type
        df_util.change_chart_type("Absolute Line")    
             
        car = df_util.search_for_field('CAR')
        df_util.add_field(car) 
     
        d_cost = df_util.search_for_field('DEALER_COST')
        df_util.add_field(d_cost)        
            
        r_cost = df_util.search_for_field('RETAIL_COST')
        df_util.add_field(r_cost)   
             
        car = df_util.search_for_field('CAR')
        df_util.add_field(car, DesignerLocators.designer_filter_bar, drag=True) 
             
        folder_name = "Retail Samples" #delete this line when starting folder is Retail Samples
             
        #Save chart
        df_util.press_save_button() 
        df_util.save_with_navigation(page_name, [folder_name, portal_name, my_pages, my_content]) 
             
        #Close Designer
        #Why so slow??
        df_util.open_logo_menu()
        df_util.select_close()
            
        #Navigate back to Retail Samples folder
        sel_util.switch_to_window(1)
 
        home_util.select_workspace()
        home_util.switch_to_workspace_iframe()
        home_util.navigate_to_workspace_folder(folder_name)
            
        home_util.copy_content(chart_2)
            
        home_util.navigate_path([portal_name, my_pages, my_content])
            
        home_util.paste_content(chart_2)

        home_util.run_content_from_tree(portal_name)
        sel_util.switch_to_window(2)
        
        page_runtime_util = PortalRuntimeUtility(self.driver)
        
        page_runtime_util.click_page(chart_2)
        
        sel_util.assert_equal(3, page_runtime_util.get_chart_container_count(), "Verify number of charts", str(case_id), '26')
        
        page_runtime_util.click_page(page_name)
        
        sel_util.assert_equal(6, page_runtime_util.get_chart_container_count(4), "Verify number of charts", str(case_id), '26')
              
if __name__ == "__main__":   
    unittest.main()