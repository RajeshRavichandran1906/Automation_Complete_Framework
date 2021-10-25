'''@author: Adithyaa

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6467916'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_report_canvas_locators
import keyboard as keys
from common.pages import as_environment_tree
from common.wftools import html_canvas
import uiautomation as automation

class C6467916_TestClass(AS_BaseTestCase):
    def test_C6467916(self):
        
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
        base_folder="P292_S10032_G156801"
        ibisamp="ibisamp"
        fields_to_select=['FIRST_NAME','LAST_NAME','CURR_SAL']
        select_report_header=['down','enter']
        select_borders=['down','enter']
        heading_area="1234"
        select_header_area="100"
        first="FIRST"
        second="SECOND"
        third="THIRD"
        border_width_dropdown="1007"
        medium_width="Medium"
        color_chooser="1015"
        color_pane="Color"
        employee_master_file="employee.mas"
        C6467916_file="C6467916"
        save_fex_C6467916="C6467916.fex"
        
        '''Testcase verification'''

        verify_report_presentation_canvas="step9_C6467916.png"
        verify_output_in_chrome="step10_C6467916_cr.png"
        verify_output_in_firefox="step10_C6467916_ff.png"
        verify_output_in_ie="step10_C6467916_ie.png"
        verify_msg_1="Step 09: Verify correct Report Canvas presentation" 
        verify_msg_2= browser + " - Step 10: Verify correct STYLING in report output" 
        verify_msg_3="Step 14: Created report is deleted"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()

        '''Step 01: Right click on P292_S10032_G156801-> New-> Report
                    Click ibisamp
                    Click on employee.mas
                    Click Ok.
                    Double click on FIRST_NAME, LAST_NAME, CURR_SAL'''
                    
        as_utilobj.logout_conf_env(envpath=True)
        time.sleep(4)
                                                            
        as_utilobj.select_tree_view_pane_item(webfocus_env) 
        time.sleep(3)
                   
        as_env_tree_obj.ui_double_click_tree_view_item(folder_path)
        time.sleep(2)
                 
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(2)
        
        dsource_win=automation.WindowControl(Name="Select Data Source")
        hcanvas.wait_for_object_exist(dsource_win, 20)
                  
        as_utilobj.select_file_in_dialogs(component_locators.ok_button,tree_path=ibisamp,select_file=employee_master_file)
        time.sleep(2)
                 
        for fields in fields_to_select: 
            as_utilobj.click_element_using_ui(tree_item=fields)
                     
        '''Step 02: Click Format tab 
                    Click PDF-> click OK in Output Format Options dialog box'''
                      
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.format_tab)
        time.sleep(1)
                  
        as_utilobj.click_element_using_ui(button_item=True,name=report_canvas_locators.pdf)
        time.sleep(1)
                  
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
               
        '''Step 03: Add Report Heading in Report. Right click on Heading Area -> select context menu Alignment Grid...'''
                
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.report_tab)
        time.sleep(1)
                   
        as_utilobj.click_element_using_ui(split_button=report_canvas_locators.header_footer,send_keys=select_report_header)
        time.sleep(1)
                   
        #as_utilobj.click_element_using_ui(edit_element=True,id=heading_area)
        automation.DocumentControl(AutomationId="1234").Click()
        time.sleep(1)
                  
        as_utilobj.select_component_by_right_click(click=report_canvas_locators.alignment_grid)
        time.sleep(2)
                 
        '''Step 04: In Insert Alignment Grid dialog box check Align with Data-> click OK'''
                 
        as_utilobj.click_element_using_ui(check_box=True,name=report_canvas_locators.align_with_data_check_box)
        time.sleep(2)
                 
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
               
        '''Step 05: In Report Heading grid type FIRST, SECOND and THIRD in correspondent cells'''
               
        as_utilobj.click_element_using_ui(pane_control=select_header_area,x=40,y=10)
        time.sleep(2)
               
        keys.write(first)
        time.sleep(2)
               
        as_utilobj.click_element_using_ui(pane_control=select_header_area,x=150,y=40)
        time.sleep(2)
               
        keys.write(second)
        time.sleep(2)
              
        as_utilobj.click_element_using_ui(pane_control=select_header_area,x=270,y=60)
        time.sleep(2)
               
        keys.write(third)
        time.sleep(2)
              
        '''Step 06: Click the cell with the FIRST text
                    On tab Report select Borders from Borders/Grid'''
                  
        as_utilobj.click_element_using_ui(pane_control=select_header_area,x=40,y=10)
        time.sleep(2)
                  
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.report_tab)
        time.sleep(1)
                  
        as_utilobj.click_element_using_ui(split_button=report_canvas_locators.borders_grid,send_keys=select_borders)
        time.sleep(2)
        
        '''Step 07: Create borders '''
                
        as_utilobj.click_element_using_ui(combo_box_with_offset=border_width_dropdown,x=120,y=10,combo_box_list_item=medium_width)
        time.sleep(2)
                
        as_utilobj.click_element_using_ui(button_item=True,id=color_chooser)
        time.sleep(1)
               
        as_utilobj.click_element_using_ui(window_click_with_offset=color_pane,x=40,y=85)
        time.sleep(1)
               
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(2)
              
        '''Step 08: Click on cell Second-> click on Border-> create another border'''
                 
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.report_tab)
        time.sleep(1)
               
        as_utilobj.click_element_using_ui(pane_control=select_header_area,x=130,y=40)
        time.sleep(2)
                   
        as_utilobj.click_element_using_ui(split_button=report_canvas_locators.borders_grid,send_keys=select_borders)
        time.sleep(2)
               
        as_utilobj.click_element_using_ui(combo_box_with_offset=border_width_dropdown,x=120,y=10,combo_box_list_item=medium_width)
        time.sleep(2)
       
        as_utilobj.click_element_using_ui(button_item=True,id=color_chooser)
        time.sleep(1)
                
        as_utilobj.click_element_using_ui(window_click_with_offset=color_pane,x=70,y=85)
        time.sleep(1)
                
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(2)
             
        '''Step 09: Click on cell Third -> click on Border-> create another border.'''
              
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.report_tab)
        time.sleep(1)
             
        as_utilobj.click_element_using_ui(pane_control=select_header_area,x=220,y=70)
        time.sleep(2)
                  
        as_utilobj.click_element_using_ui(split_button=report_canvas_locators.borders_grid,send_keys=select_borders)
        time.sleep(2)
              
        as_utilobj.click_element_using_ui(combo_box_with_offset=border_width_dropdown,x=120,y=10,combo_box_list_item=medium_width)
        time.sleep(2)
      
        as_utilobj.click_element_using_ui(button_item=True,id=color_chooser)
        time.sleep(1)
               
        as_utilobj.click_element_using_ui(window_click_with_offset=color_pane,x=90,y=85)
        time.sleep(1)
               
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(2)
     
        as_utilobj.verify_picture_using_sikuli(verify_report_presentation_canvas,verify_msg_1)
        time.sleep(2)
          
        '''Step 10: Click Run & Close report output, 
           Step 11: close Report canvas and save Report1'''
           
        as_utilobj.close_canvas_item()
        time.sleep(3)
           
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
           
        as_utilobj.save_as_UI_dialog(C6467916_file)
        time.sleep(6)
          
        ''''Step 12: Right click on Report1 and select Open
            Step 13: Click Run'''

        hcanvas.run_canvas_item_in_browser(base_folder,save_fex_C6467916)
        time.sleep(6)

        if browser=="Firefox":
            as_utilobj.verify_picture_using_sikuli(verify_output_in_firefox,verify_msg_2)
        elif browser=="Chrome":
            as_utilobj.verify_picture_using_sikuli(verify_output_in_chrome,verify_msg_2)
        else:
            automation.SendKeys('{Ctrl}0')
            time.sleep(10)
            as_utilobj.verify_picture_using_sikuli(verify_output_in_ie,verify_msg_2)
        
        hcanvas.close_browser_session()
        time.sleep(3)
        
        '''Step 14: Close report output
                    Close Report Canvas
                    Right click on Report1 and select Delete'''
        
        as_utilobj.select_component_by_right_click(right_click_item=C6467916_file,click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item=C6467916_file,unavailable=True)
        time.sleep(1)
             
if __name__=='__main__' :
    unittest.main()     