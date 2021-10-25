#for local testing
import sys
sys.path.append('../../')
#*************************

import unittest
from utility.selenium_utility import Selenium_Utility, ParisHomeUtility, DesignerUtility
from utility.locators import ParisHomeLocators, DesignerLocators
from utility.basetestcasedocker import BaseTestCaseDocker

class C9336692_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9336692_TestClass, self).__init__(driver)
    
    def test_C9336692(self):        
        case_id = 'C9336692'
        master_name = "wf_retail_lite"
        folder_name = "Retail Samples"
        eda_folder_name = "retail_samples"
        portal_name = "test portal2"  
        chart_1 = "CHART1"    
        chart_2 = "Unified_1"  
        sel_util = Selenium_Utility(self.driver)
        
        #Log into WF
        sel_util.login_wf()
      
        home_util = ParisHomeUtility(self.driver)
         
        #Navigate to work space folder
        home_util.select_workspace()
        home_util.switch_to_workspace_iframe()
        home_util.navigate_to_workspace_folder(folder_name)
        home_util.select_application_button()
          
        #Create portal - if portal exists, it will be deleted 
        home_util.create_new_portal(portal_name)
        
        #To workaround a product issue where auto-refresh does not occur after content creation
        home_util.refresh_workspace()
          
        #Publish portal
        home_util.publish_portal_folder(portal_name)
          
        self.driver.switch_to.default_content()
          
        #Launch Designer by clicking 'Visualize Data'
        home_util.launch_designer()
        sel_util.switch_to_window(2)
        
        df_util = DesignerUtility(self.driver)
                
        #Select a master file
        df_util.select_data_source(master_name, folder_name, eda_folder_name)
        
        #Verify master file is selected in the tool
        master_title = df_util.get_data_source_title()
        sel_util.assert_equal(master_name, master_title, "Verify correct master is selected", case_id, '10')
          
        #Change Chart type
        df_util.change_chart_type("Data Grid (Chart)")
           
        #Add fields
        product_category = df_util.search_for_field('Product,Category')
        df_util.add_field(product_category)
           
        quantity_sold = df_util.search_for_field('Quantity,Sold')
        df_util.add_field(quantity_sold)
           
        column_bucket_locator = ParisHomeLocators.create_xpath_locator_with_text(DesignerLocators.designer_bucket_xpath_template, 'Column')
        store_biz_region = df_util.search_for_field('Store,Business,Region')
        df_util.add_field(store_biz_region, column_bucket_locator, drag=True)      
           
        df_util.add_visualization()
           
        #Change Chart type
        df_util.change_chart_type("Tagcloud")
   
        product_sub_category = df_util.search_for_field('Product,Subcategory')
        df_util.add_field(product_sub_category)
           
        color_bucket_locator = ParisHomeLocators.create_xpath_locator_with_text(DesignerLocators.designer_bucket_xpath_template, 'Color')
        gross_profit = df_util.search_for_field('Gross Profit')
        df_util.add_field(gross_profit, color_bucket_locator, drag=True, index=1)           
           
        df_util.add_visualization()
            
        #Change Chart type
        df_util.change_chart_type("Arc Chart")
    
        product_category = df_util.search_for_field('Product,Category')
        df_util.add_field(product_category)
            
        cost_goods = df_util.search_for_field('Cost of Goods')
        df_util.add_field(cost_goods, index=1)             
           
        #Move and resize charts
        container3 = df_util.locate_container(0, 7)
        df_util.resize_container(container3, width=6)
        container2 = df_util.locate_container(6, 0)
        df_util.move_container(container2, x=6, y=7)
        df_util.move_container(container3, x=6, y=0)
        df_util.move_container(container2, x=0, y=7)
        df_util.resize_container(container2, width=12)
        
        #Save chart
        df_util.press_save_button()   
        df_util.save_chart(chart_1)   
             
        #change page theme     
        df_util.select_page_container()        
        df_util.select_format_tab()
        df_util.change_page_theme("Midnight")
        
        #change container 3 style
        container_num = 3
        df_util.change_container_style(container_num, 'Style 6')
        
        #change container 2 theme
        container_num = 2
        text_color = df_util.find_element_attribute_value(DesignerLocators.designer_cloud_chart_first_text, "fill")
        df_util.change_container_theme(container_num, 'Light')
        new_text_color = df_util.find_element_attribute_value(DesignerLocators.designer_cloud_chart_first_text, "fill")
        
        #Verify text color change after theme change
        sel_util.assert_true(text_color != new_text_color, "Verify text color changed in CloudTag Chart", case_id, "30")
        
        #Save as Unified_1
        df_util.open_logo_menu()
        df_util.select_save_as_menu_item()
        df_util.save_chart(chart_2) 
        
        #Close Designer
        df_util.open_logo_menu()
        df_util.select_close()
        
        #Navigate back to Retail Samples folder
        sel_util.switch_to_window(1)
        home_util.switch_to_workspace_iframe()
        home_util.navigate_to_workspace_folder(folder_name)
        
        #Verify charts have been created
        chart1 = home_util.locate_fex(chart_1)
        sel_util.assert_true(chart1, "Verify chart fex is saved", case_id, '32')
        unify1 = home_util.locate_fex(chart_2)
        sel_util.assert_true(unify1, "Verify final version of chart is saved", case_id, '32')

              
if __name__ == "__main__":   
    unittest.main()