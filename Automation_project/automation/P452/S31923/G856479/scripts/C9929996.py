#for local testing
import sys
sys.path.append('../../')
#*************************

import unittest,time
from utility.selenium_utility import Selenium_Utility, ParisHomeUtility, DesignerUtility, PortalRuntimeUtility
from utility.locators import ParisHomeLocators, DesignerLocators, PortalRuntimeLocators
from utility.basetestcasedocker import BaseTestCaseDocker

class C9929996_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9929996_TestClass, self).__init__(driver)
    
    def test_C9929996(self):        
        case_id = 'C9929996'
        folder_name = "Retail Samples"
        portal_folder = "Portal"
        widget_folder_1 = "Test Widgets"
        widget_folder_2 = "Small Widgets"
        widget_folder_3 = "Large Widgets"
        eda_folder_name = "ibisamp"
        page_name_1 = "Unified_1" 
        page_name_2 = "Unified_2" 
        portal_name = "test portal2" 
        my_pages = "My Pages"
        my_content = "My Content"
        my_workspace = "My Workspace"
        output_name = "Assemble"
        output_path = "IBFS:/WFC/Repository/My_Workspace/~admin/Assemble"
         
        sel_util = Selenium_Utility(self.driver)
        
        #Log into WF
        sel_util.login_wf()
      
        home_util = ParisHomeUtility(self.driver)
        home_util.select_workspace()
        home_util.switch_to_workspace_iframe()
        home_util.navigate_to_workspace_folder(folder_name)
  
        home_util.navigate_path([portal_name, my_pages, my_content])
              
        home_util.edit_content(page_name_1)
              
        sel_util.switch_to_window(2)
              
        df_util = DesignerUtility(self.driver)
              
        df_util.delete_container(3, wait_time=75)   
                  
        #Save chart
        df_util.press_save_button() 
                  
        #Close Designer
        #Why so slow??
        df_util.open_logo_menu()
        df_util.select_close()
                 
        sel_util.switch_to_window(1)
        home_util.switch_to_workspace_iframe()
              
        home_util.edit_content(page_name_2)
              
        sel_util.switch_to_window(2)
              
        df_util.delete_container(2, wait_time=75)   
                  
        #Save chart
        df_util.press_save_button() 
                  
        #Close Designer
        #Why so slow??
        df_util.open_logo_menu()
        df_util.select_close()
      
        #Navigate back to Retail Samples folder
        sel_util.switch_to_window(1)
        home_util.switch_to_workspace_iframe()   
         
        home_util.navigate_to_workspace_folder(folder_name)
        home_util.run_content_from_tree(portal_name)
        sel_util.switch_to_window(2)
           
        #to workaround HOME-3052
        time.sleep(25) 
              
        page_runtime_util = PortalRuntimeUtility(self.driver)
              
        page_runtime_util.click_page(page_name_1)
              
        sel_util.assert_equal(2, page_runtime_util.get_chart_container_count(), "Verify number of charts", str(case_id), '9')
              
        page_runtime_util.click_page(page_name_2)
              
        sel_util.assert_equal(4, page_runtime_util.get_chart_container_count(4), "Verify number of charts", str(case_id), '9')
         
        sel_util.close_window()
        sel_util.switch_to_window(1)        
 
        home_util.create_content('assemble')
        sel_util.switch_to_window(2)
           
        df_util.choose_template_by_name('Grid 4-2-1')
           
        #df_util.navigate_content_folders_up([my_content, my_workspace])
        df_util.navigate_content_folders_up([folder_name]) #changing from the line above to this due to a product change
        df_util.navigate_content_folders_down([folder_name, portal_folder, widget_folder_1])
        df_util.add_content_to_container('Blue', 'Panel 1')
        df_util.add_content_to_container('Gray', 'Panel 2')
        df_util.add_content_to_container('Green', 'Panel 3')
        df_util.add_content_to_container('Red', 'Panel 4')
           
        df_util.navigate_content_folders_up([widget_folder_1])
        df_util.navigate_content_folders_down([widget_folder_2])
        df_util.add_content_to_container('Category Sales', 'Panel 5')
        df_util.add_content_to_container('Regional Sales Trend', 'Panel 6')
   
        df_util.navigate_content_folders_up([widget_folder_2])
        df_util.navigate_content_folders_down([widget_folder_3])    
        df_util.add_content_to_container('Store Sales by Region', 'Panel 7')    
           
        df_util.auto_create_filters()
           
        sel_util.assert_equal(6, df_util.get_filter_dropdown_count(), "Verify number of filters", str(case_id), '15')
              
        container_orig_color = df_util.find_element_attribute_value(DesignerLocators.designer_page_box, "background-image")
        print(str(container_orig_color))
          
        #change page theme          
        df_util.select_page_container()        
        df_util.select_format_tab()
        df_util.change_page_theme("Midnight")
          
        container_color = df_util.find_element_attribute_value(DesignerLocators.designer_page_box, "background-image")
        print(str(container_color))   
        sel_util.assert_true("linear-gradient" in container_color, "Verify background image changed", case_id, '16')
  
        #change container 3 style
        df_util.change_container_style('Category Sales', 'Style 6')                
   
        #Save chart
        df_util.press_save_button()   
        df_util.save_chart(output_name)      
   
        #Close Designer
        df_util.open_logo_menu()
        df_util.select_close()  
           
        sel_util.switch_to_window(1)
          
        home_util.select_workspace()
        home_util.switch_to_workspace_iframe()
        home_util.navigate_to_workspace_folder(folder_name)       
        
        home_util.run_content_from_tree(portal_name)
        sel_util.switch_to_window(2)       
         
        page_runtime_util = PortalRuntimeUtility(self.driver)
        
        page_runtime_util.add_portal_page(output_name, [folder_name]) 
        
        page_runtime_util.click_page(output_name)   
        
        container_color = df_util.find_element_attribute_value(DesignerLocators.designer_page_box, "background-image")
        print(container_color)

        sel_util.assert_true(container_color == container_orig_color, "Verify background image is removed", case_id, '23')  
        
              
if __name__ == "__main__":   
    unittest.main()