'''@author: Adithyaa

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6467906'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_report_canvas_locators
from common.pages import as_environment_tree
from common.wftools import html_canvas
import uiautomation as automation

class C6467906_TestClass(AS_BaseTestCase):
    def test_C6467906(self):
        
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
        car_master_file="car.mas"
        fields_to_select=['COUNTRY','CAR','SALES']
        select_excel_xlsx=['down','enter']
        C6467906_file="C6467906"
        saved_fex_C6467906="C6467906.fex"
        
        '''Testcase verification'''
        
        verify_new_report="App Studio - Report1*"
        verify_push_buttons=['HTML','Active Report','PDF','Active PDF','Output Format Options','Destination (PCHOLD)']
        verify_push_button_1=['Excel','PowerPoint','Output Format']
        verify_output_format_dialog="Output Format Options"
        verify_default_stylesheet="step3_C6467906.png"
        verify_html_table="step5_C6467906_Ds01.xlsx"
        verify_output_in_chrome="step8_C6467906_cr.png"
        verify_output_in_firefox="step8_C6467906_ff.png"
        verify_output_in_ie="step8_C6467906_ie.png"
        verify_active_report_in_firefox="step14_C6467906_ff.png"
        verify_active_report_in_chrome="step14_C6467906_cr.png"
        verify_active_report_in_ie="step14_C6467906_ie.png"
        
        '''Testcase Msgs'''
        
        verify_msg_1="Step 02: Verify new report is invoked" 
        verify_msg_2= "Step 03: Verify default stylesheet is presented on Report"
        verify_msg_3="Step 04: Verify pushbuttons for Formats - "
        verify_msg_4="Step 05: Verify correct data in HTML Format report output"
        verify_msg_5="Step 08: Verify correct Output Format Options dialog box"
        verify_msg_6= browser + " - Step 08: Verify correct data and styling in PDF report output"
        verify_msg_7="Step 10: Verify correct Output Format Options dialog box"
        verify_msg_8="Step 11: Verify correct data and styling in Excel report output"
        verify_msg_9= browser + " - Step 14: Verify correct report output in Active report format"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()

        '''Step 01: Right click on P292_S10032_G156801- > New-> Report'''
            
        as_utilobj.logout_conf_env(envpath=True)
        time.sleep(4)
                                                               
        as_utilobj.select_tree_view_pane_item(webfocus_env) 
        time.sleep(3)
                      
        as_env_tree_obj.ui_double_click_tree_view_item(folder_path)
        time.sleep(2)
                   
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(2)
            
        '''Step 02: In Select Data Source select master file car.mas->Click Ok.'''
                     
        as_utilobj.select_file_in_dialogs(component_locators.ok_button,tree_path=ibisamp,select_file=car_master_file)
        time.sleep(8)
           
        as_utilobj.verify_active_tool(verify_new_report,verify_msg_1)
        time.sleep(2)
            
        '''Step 03: In Object Inspector double click on COUNTRY, CAR, SALES'''
            
        for fields in fields_to_select: 
            as_utilobj.click_element_using_ui(tree_item=fields)
            time.sleep(2)
                
        as_utilobj.verify_picture_using_sikuli(verify_default_stylesheet,verify_msg_2)
        time.sleep(2)
           
        '''Step 04: Click on Format tab'''
               
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.format_tab)
        time.sleep(1)
           
        for push_buttons in verify_push_buttons: 
            as_utilobj.verify_element_using_ui(verify_msg_3 + push_buttons,button_item=push_buttons,enabled=True)
           
        for push_buttons_1 in verify_push_button_1: 
            as_utilobj.verify_element_using_ui(verify_msg_3 + push_buttons_1,split_button_item=push_buttons_1,enabled=True)
           
        '''Step 05: Execute report request (HTML is Default format output)
           Step 06: Close report output'''
                
        as_utilobj.close_canvas_item()
        time.sleep(3)
               
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
               
        as_utilobj.save_as_UI_dialog(C6467906_file)
        time.sleep(6)
             
        hcanvas.run_canvas_item_in_browser(base_folder,saved_fex_C6467906)
        time.sleep(6)
           
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
           
        hcanvas.create_web_table_data("html body table tbody tr",verify_html_table)
           
        hcanvas.verify_web_table_data("html body table tbody tr",verify_html_table,verify_msg_4)
            
        hcanvas.close_browser_session()
        time.sleep(3)
          
        '''Step 07: Click on pushbutton PDF'''
           
        as_env_tree_obj.ui_double_click_tree_view_item(C6467906_file)
        time.sleep(2)
           
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.format_tab)
        time.sleep(1)
                    
        as_utilobj.click_element_using_ui(button_item=True,name=report_canvas_locators.pdf)
        time.sleep(1)
           
        as_utilobj.Verify_Current_Dialog_Opens(verify_output_format_dialog,verify_msg_5)
        time.sleep(1)
          
        '''Step 08: Click OK in Output Format Options. Execute report request
           Step 09: Close report output'''
                    
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
           
        as_utilobj.close_canvas_item()
        time.sleep(3)
            
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
            
        hcanvas.run_canvas_item_in_browser(base_folder,saved_fex_C6467906)
        time.sleep(10)
   
        if browser=="Firefox":
            as_utilobj.verify_picture_using_sikuli(verify_output_in_firefox,verify_msg_6)
        elif browser=="Chrome":
            as_utilobj.verify_picture_using_sikuli(verify_output_in_chrome,verify_msg_6)
        else:
            automation.SendKeys('{Ctrl}0')
            time.sleep(5)
            as_utilobj.verify_picture_using_sikuli(verify_output_in_ie,verify_msg_6)
            time.sleep(3)
           
        hcanvas.close_browser_session()
        time.sleep(3)
         
        '''Step 10: Select Excel 2007 from drop down for Excel formats'''
            
        as_env_tree_obj.ui_double_click_tree_view_item(C6467906_file)
        time.sleep(2)
            
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.format_tab)
        time.sleep(1)
                      
        as_utilobj.click_element_using_ui(split_button=report_canvas_locators.excel,send_keys=select_excel_xlsx)
        time.sleep(1)
             
        as_utilobj.Verify_Current_Dialog_Opens(verify_output_format_dialog,verify_msg_7)
        time.sleep(1)
   
        '''Step 11: Click OK in Output Format Options and execute
           Step 12: Close report output'''
           
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
             
        as_utilobj.close_canvas_item()
        time.sleep(3)
              
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
             
        hcanvas.run_canvas_item_in_browser(base_folder,saved_fex_C6467906)
        time.sleep(10)
           
        as_utilobj.save_file_from_browser('C6467906_actual_1')
        time.sleep(5)
           
        as_utilobj.verify_xml_xls('C6467906_base_1.xlsx','C6467906_actual_1.xlsx',verify_msg_8)
        time.sleep(2)
           
        hcanvas.close_browser_session()
        time.sleep(3)
         
        '''Step 13: Click on pushbutton Active Report'''
           
        as_env_tree_obj.ui_double_click_tree_view_item(C6467906_file)
        time.sleep(2)
            
        as_utilobj.click_element_using_ui(tab_item=report_canvas_locators.format_tab)
        time.sleep(1)
                      
        as_utilobj.click_element_using_ui(button_item=True,name=report_canvas_locators.active_report)
        time.sleep(1)
             
        as_utilobj.close_canvas_item()
        time.sleep(3)
               
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
         
        '''Step 14: Execute report request'''
         
        hcanvas.run_canvas_item_in_browser(base_folder,saved_fex_C6467906)
        time.sleep(10)
         
        if browser=="Firefox":
            as_utilobj.verify_picture_using_sikuli(verify_active_report_in_firefox,verify_msg_9)
        elif browser=="Chrome":
            as_utilobj.verify_picture_using_sikuli(verify_active_report_in_chrome,verify_msg_9)
        else:
            as_utilobj.verify_picture_using_sikuli(verify_active_report_in_ie,verify_msg_9)
            time.sleep(3)
            
        '''Step 15: Close report output.
                    Close Report Canvas'''

        hcanvas.close_browser_session()
        time.sleep(3)
                    
if __name__=='__main__' :
    unittest.main()    