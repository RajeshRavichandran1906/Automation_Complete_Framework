'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6467910'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_report_canvas_locators
from common.pages import as_environment_tree
from common.wftools import html_canvas

class C6467910_TestClass(AS_BaseTestCase):
    def test_C6467910(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        report_canvas_locators=as_report_canvas_locators.ASReportCanvasLocators()
        as_env_tree_obj=as_environment_tree.AS_Environment_Tree_And_Detail(driver)
        hcanvas=html_canvas.Html_Canvas(self.driver)
    
        '''Testcase property variables'''
        
        webfocus_env=as_utilobj.parseinitfile("envpath")
        browser=as_utilobj.parseinitfile("browser")
        folder_path="Domains->P292_S10032_G156801"
        base_folder='P292_S10032_G156801'
        ibisamp="ibisamp"
        foccache="foccache"
        car_master_file="car.mas"
        fields_to_select=['COUNTRY','CAR','DEALER_COST','RETAIL_COST','SALES']
        fields_in_myhold_report=['COUNTRY','CAR','SALES']
        select_focus_database=['down','down','down','right','enter']
        select_push_button="37040"
        file_name_edit_button="37043"
        application_dropdown="37042"
        edit_control_id="37039"
        type_my_hold="myhold"
        report_in_procedure_panel="Report"
        procedure_view_panel=['-52','170']
        file_atest="C6467910"
        file_atest_fex="C6467910.fex"
        
        '''Testcase verification'''

        verify_value="'foccache/myhold'"
        verify_myhold_report="App Studio - Report1*"
        verify_atest_report="App Studio - C6467910"
        verify_output_report="step16_C6467910_Ds01.xlsx"
        verify_msg_1="Step 07: Verify that 2part name has been created in Output Destination dialog box" 
        verify_msg_2="Step 10: Verify that myhold.mas open in second report tab of Procedure"
        verify_msg_3= browser + " - Step 12: Verify correct report output"
        verify_msg_4="Step 15: Verify no parsing error and correct presentation of Procedure View and Report Canvas"
        verify_msg_5= browser + " - Step 16: Verify correct atest report output"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()

        '''Step 01: Right click on folder P292_S10032_G156801-> New-> Report''' 
                     
        as_utilobj.logout_conf_env(envpath=True)
        time.sleep(4)
                                                               
        as_utilobj.select_tree_view_pane_item(webfocus_env) 
        time.sleep(3)
                      
        as_env_tree_obj.ui_double_click_tree_view_item(folder_path)
        time.sleep(2)
                  
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(2)
             
        '''Step 02: In Report Wizard select foccache/car.mas -> Click Ok.'''
                      
        as_utilobj.select_file_in_dialogs(component_locators.ok_button,tree_path=ibisamp,select_file=car_master_file)
        time.sleep(2)
            
        '''Step 03: In Object Inspector double click on fields COUNTRY, CAR, DEALER_COST, RETAIL_COST, SALES'''
                     
        for fields in fields_to_select: 
            as_utilobj.click_element_using_ui(tree_item=fields)
                
        '''Step 04: Click on tab Format. Select FOCUS Database (FOCUS) from Database Formats/Output formats drop down
                    Click Ok in Output formats Options'''
                 
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.format_tab)
        time.sleep(1)
                         
        as_utilobj.click_element_using_ui(split_button=report_canvas_locators.output_format_dropdown,send_keys=select_focus_database)
        time.sleep(1)
           
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
  
        '''Step 05: Click on Destination(HOLD).'''
                
        as_utilobj.click_element_using_ui(button_item=True,name=report_canvas_locators.destination_pchold)
        time.sleep(1)
           
        '''Step 06: In dialog box Output Destination dialog box click on pushbutton ...'''
           
        as_utilobj.click_element_using_ui(button_item=True,id=select_push_button)
        time.sleep(2)
          
        as_utilobj.click_element_using_ui(combo_box=application_dropdown)
        time.sleep(1)
          
        as_utilobj.select_file(list_item=foccache)
        time.sleep(1)
          
        '''Step 07: Type MYHOLD for File Name -> Click OK'''
          
        as_utilobj.click_element_using_ui(edit_element=True,id=file_name_edit_button,write=type_my_hold)
        time.sleep(1)
          
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
          
        as_utilobj.verify_edit_control_value(edit_control_id,verify_value,verify_msg_1)
        time.sleep(2)
          
        '''Step 08: Click Ok in Output Destination dialog box'''
          
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
          
        '''Step 09: Open procedure view-> right click on Report-> New...-> Report'''
          
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(1)
          
        as_utilobj.select_component_by_right_click(right_click_item=report_in_procedure_panel,click=component_locators.comments_new,click_sub_menu=component_locators.new_report)
        time.sleep(8)
  
        '''Step 10: In Report wizard dialog box select foccache/myhold-> Ok'''
          
        as_utilobj.select_file_in_dialogs(component_locators.ok_button,tree_path=base_folder,select_file=type_my_hold)
        time.sleep(2)
             
        as_utilobj.verify_active_tool(verify_myhold_report,verify_msg_2)
        time.sleep(1)
  
        '''Step 11: In Object Inspector double click on fields COUNTRY, CAR, SALES'''
          
        for fields_1 in fields_in_myhold_report: 
            as_utilobj.click_element_using_ui(tree_item=fields_1)
              
        '''Step 12: Execute report request.   
           Step 13: Close report output.
           Step 14: Close Report Canvas , save report as ATEST'''
              
        as_utilobj.close_canvas_item()
        time.sleep(3)
          
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
                  
        as_utilobj.save_as_UI_dialog(file_atest)
        time.sleep(3)
              
        hcanvas.run_canvas_item_in_browser(base_folder,file_atest_fex)
        time.sleep(6)
            
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
            
        hcanvas.create_web_table_data("html body table tbody tr",verify_output_report)
            
        hcanvas.verify_web_table_data("html body table tbody tr",verify_output_report,verify_msg_3)
             
        hcanvas.close_browser_session()
        time.sleep(3)
        
        '''Step 15:  Right click on ATEST-> select context menu Open'''
        
        as_utilobj.select_component_by_right_click(right_click_item=file_atest,click=component_locators.open_button)
        time.sleep(7)
        
        as_utilobj.verify_active_tool(verify_atest_report,verify_msg_4)
        time.sleep(2)
        
        '''Step 16: Execute report request.'''
        
        hcanvas.run_canvas_item_in_browser(base_folder,file_atest_fex)
        time.sleep(6)
            
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
            
        hcanvas.create_web_table_data("html body table tbody tr",verify_output_report)
            
        hcanvas.verify_web_table_data("html body table tbody tr",verify_output_report,verify_msg_5)
             
        hcanvas.close_browser_session()
        time.sleep(3)
        
        '''Step 17: Close report output, close Report Canvas'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3) 
        
        '''Step 18: Right click on ATEST-> select context menu Delete
                    Delete ATEST.fex'''
        
        as_utilobj.select_component_by_right_click(right_click_item=file_atest,click=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 