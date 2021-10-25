from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.as_utility import AS_Utillity_Methods as as_utillobj
from common.lib.core_utility import CoreUtillityMethods as coreutillobject
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from common.pages import as_html_canvas_area
import pyautogui, time
import uiautomation as automation
from selenium.webdriver.support.ui import Select


class Document_Canvas(AS_BaseTestCase):
    """ Inherit attributes of the parent class = AS_BaseTestCase """
    

    def __init__(self, driver):
        #super(Document_Canvas, self).__init__(driver)
        self.driver=driver
        #self.se_driver=se_driver
        self.browser = utillobject.parseinitfile(self,'browser') 
        

    def run_item_using_right_click_menu(self, tree_path, item):
        '''
        Desc: This function will run an item using Right click menu
        '''
        as_utillobj.run_item_from_tree_pane_context_menu(self, tree_path, item)
        
    def select_UI_item_using_right_click_menu(self, tree_path, item, menu_item):
        '''
        Desc: This function will run an item using Right click menu
        '''
        as_utillobj.select_item_from_tree_pane_context_menu(self, tree_path, item, menu_item)
        
    
    def navigate_to_repository_item(self, tree_path):
        '''
        Desc: This function navigate to a repository item in AS
        '''
        as_utillobj.select_tree_view_pane_item(self, tree_path)
    
    def select_item_from_context_menu(self, item, menuoption, **kwargs):
        '''
        Desc: This function will right click on an item and click on menu option, 
        if kwargs: click_sub_menu is present it will click on submenu item too.
        '''
        as_utillobj.select_component_by_right_click(self,right_click_item=item,click=menuoption)
    
    def click_any_buton_on_canvas_page(self,btn_name):
        '''
        Desc: This function will click any button on the canvas page
        '''
        as_utillobj.click_any_canvas_button(self, btn_name)
    
    def select_html_dropdown_item(self,dropdown_css,option):
        '''
        Desc: This function will select the value from a combobox item in html canvas
        '''
        as_utillobj.select_or_verify_html_drop_down_option(self, dropdown_css, option)
        
    def run_canvas_item_in_browser(self,folderpath,file_name):
        '''
        Desc: This function will load the webdriver and run the item outside of AS.
        '''
        
        as_utillobj.run_item_in_browser(self, folderpath, file_name)
#         as_utillobj.get_se_driver(self,file_name)
        
    def verify_msg_dialog_text(self, dialogtitle,text_verify, msg, **kwargs):
        '''
        Desc: This function will verify the given text in a msg dialog
        '''
        as_utillobj.verify_current_active_tool(self, dialogtitle, msg, text_to_verify=text_verify)
        
    def wait_for_object_exist(self, object,wait_time):
        '''
        Desc: This function will wait for object exists
        '''
        as_utillobj.wait_for_UI_object(self, object, wait_time)
        
    def wait_for_web_object_exist(self, object_css, expected_number, expire_time,pause_time):
        '''
        Desc: This function will wait for object exists
        '''
        as_utillobj.synchronize_with_number_of_element(self, object_css, expected_number, expire_time, pause_time)
        
    def wait_for_object_not_exist(self, object,wait_time):
        '''
        Desc: This function will wait for object to disappear
        '''
        as_utillobj.wait_for_UI_object_close(self, object, wait_time)
    
    def verify_object_exist(self,css, visible, msg, **kwargs):
        '''
        Desc: This function will verify if object exists
        '''
        as_utillobj.verify_object_visible(self, css, visible, msg)
    
    def verify_total_no_of_child_objects(self,ui_object, count,msg, **kwargs):
        '''
        Desc: This function will verify no of child objects
        '''
        as_utillobj.verify_child_count(self, ui_object, count, msg)    
    
    def select_combobox_option_item(self, select_css, select_type, value):
        '''
        Desc: This function will select item from a  dropdown
        '''
        as_utillobj.select_dropdown(self, select_css, select_type, value)
    
    def click_on_web_element(self, select_css):
        '''
        Desc: This function will click on a web element
        '''
        element_obj = self.se_driver.find_element_by_css_selector(select_css)
        coreutillobject.left_click(self, element_obj,mouse_move_duration=1)   
    def click_on_UI_element(self, ui_object):
        '''
        Desc: This function will click on UI element
        '''
        ui_object.MoveCursor()
        time.sleep(3)
        ui_object.Click()
    
    def verify_web_element_attribute(self, elem_css,attribute, value, msg):
        '''
        Desc: This function will verify web element attributes
        '''
        elem=self.se_driver.find_element_by_css_selector(elem_css)
        attribvalue=utillobject.get_element_attribute(self, elem, attribute)
        utillobject.asequal(self, attribvalue,value, msg)

    def verify_web_element_css(self, elem_css,css_property, value, msg):
        '''
        Desc: This function will verify web element css property
        '''
        elem=self.se_driver.find_element_by_css_selector(elem_css)
        attribvalue=utillobject.get_element_css_propery(self, elem, css_property)
        utillobject.asequal(self, attribvalue,value, msg)
    
    def create_web_table_data(self, table_css, file_name): 
        '''
        Desc: This function will create a table
        ''' 
        as_utillobj.create_table_data(self, table_css, file_name)
    
    def verify_web_table_data(self, table_css, file_name,msg):
        '''
        Desc: This function will verify a web table
        '''
        as_utillobj.verify_table_data(self, table_css, file_name, msg)
        
    def switch_to_web_frame(self, frame_css):
        '''
        Desc: This function will switch to a specified iframe
        '''
        as_utillobj.switch_to_frame(self, frame_css)
        
    def switch_to_window(self,wndnum, pause=15, **kwargs):
        '''
        Desc: This function will switch to a given window number
        '''
        as_utillobj.switch_to_window(self, wndnum, pause)
    
    def switch_to_main_window(self):
        '''
        Desc: This function will close child windows and switch to main window
        '''
        as_utillobj.switch_to_main_window(self)
        
    def switch_to_default_content(self):
        '''
        Desc: This function will switch back to main content from a iframe
        '''
        as_utillobj.switch_to_default_content(self)
    
    def verify_web_object_visible(self, css, visible, msg):
        '''
        Desc: This function will verify web object is visible
        '''
        as_utillobj.verify_web_object_visible(self, css, visible, msg)
    
    def verify_web_object_no_of_elements(self, css, count, msg):
        '''
        Desc: This function will verify web object no of elements
        '''
        as_utillobj.verify_web_object_count(self, css, count, msg)
    
    def close_browser_session(self):
        '''
        Desc: This function will close a browser session
        '''
        as_utillobj.close_web_window(self)
        
    def select_item_from_tree_view(self,tree_item,list_item,button_name):
        '''
        Desc: This function will select tree item using UIA
        '''
        as_utillobj.select_UI_tree_view_item(self, tree_item, list_item, button_name)
    
    def wait_for_web_object_text(self, element_css, visble_element_text, expire_time, pause_time, text_option):
        '''
        Desc: This function will wait for a web object text to be visible
        '''
        as_utillobj.synchronize_with_visble_text(self, element_css, visble_element_text, expire_time, pause_time, text_option)
    
    def verify_color_web_object_chart(self, parent_id, riser_class, color, msg):
        '''
        Desc: This function will verify color of a web object
        '''
        as_utillobj.verify_chart_color(self, parent_id, riser_class, color, msg)
    
    def verify_labels_for_web_object_chart(self, parent_id, expected_datalabel, msg, **kwargs):
        '''
        Desc: This function will verify labels of a web object
        '''
        as_utillobj.verify_data_labels(self, parent_id, expected_datalabel, msg, **kwargs)
    
    def verify_no_of_risers_for_web_object_chart(self, parent_css_with_tagname, risers_per_segment, expected_number, msg):
        '''
        Desc: This function will verify no of risers in a webobject chart
        '''
        as_utillobj.verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, msg)
    
    def verify_xy_axis_title_for_web_object_chart(self,popup_id,expected_xaxis_title,expected_yaxis_title,msg):
        '''
        Desc: This function will verify x and y axis of a web object chart
        ''' 
        as_utillobj.verify_xy_axis_title(self,popup_id,expected_xaxis_title,expected_yaxis_title,msg)
        
    def verify_web_object_text_visible(self,web_object_css,text_verify,msg,**kwargs):
        '''
        Desc: This function will verify web object text exists
        '''
        as_utillobj.verify_web_object_text(self, web_object_css, text_verify, msg)  
    
    def select_new_item_from_requests_datasource_menu(self,menu_path):
        '''
        Desc: This function will select new item from requests datasource menu
        '''
        as_utillobj.select_new_request_datasource_menu(self, menu_path)
        
    def select_dropdown_item_from_run_requests_menu(self,menu_path):
        '''
        Desc: This function will select dropdown item from run requests menu
        '''
        as_utillobj.select_run_request_actions_menu(self, menu_path)
    
    def verify_current_web_url(self,expected_url,msg):
        '''
        Desc: This function will verify current web url
        '''
        as_utillobj.verify_web_url(self, expected_url,msg)
    
    def click_web_button_exists(self,select_xpath):
        '''
        Desc: This function will click on a web button using xpath
        '''
        try:
            
            if (self.se_driver.find_element_by_xpath(select_xpath)):
                element_obj=self.se_driver.find_element_by_xpath(select_xpath)
                coreutillobject.left_click(self, element_obj,mouse_move_duration=1)
        
        except:
            print ("No prompt to close")
        
    def select_listbox_item(self, select_css, index):
        '''
        Desc: This function will click on a web element
        '''
        
        element_obj = self.se_driver.find_element_by_css_selector(select_css)
        element_obj.click()

        
    def select_report_autolink_tooltip_value(self, parent_table_css, row, col, tooltip_path, verify_tooltip=None, msg=None, **kwargs):
        as_utillobj.select_report_autolink_tooltip(self, parent_table_css, row, col, tooltip_path, verify_tooltip, msg)
      
    def move_to_chart_component(self, riser_or_marker_element, use_marker_enable=False, move_to_tooltip=True):
        as_utillobj.move_mouse_to_chart_component(self, riser_or_marker_element, use_marker_enable, move_to_tooltip)
    
    def create_new_Document_Canvas_document(self,tree_path,item):
        automation.TabItemControl(Name="Home").Click()
        time.sleep(4)
        automation.MenuItemControl(Name="All Files").Click()
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
         
          
        if stat==True:
            automation.TreeItemControl(Name=item).ScrollIntoView()
            time.sleep(8)
            automation.TreeItemControl(Name=item).RightClick()
            time.sleep(3)
            automation.MenuItemControl(Name="New").Click()
            time.sleep(3)
            automation.MenuItemControl(Name="HTML/Document").DoubleClick()
        else:
            Document_Canvas.select_UI_item_using_right_click_menu(self,tree_path, item, "New->HTML/Document")
            
         
        button_control=automation.ButtonControl(Name='Next >')
        Document_Canvas.click_on_UI_element(self,button_control)
         
        button_control=automation.ButtonControl(Name='Finish')
        Document_Canvas.wait_for_object_exist(self,button_control, 30)
        Document_Canvas.click_on_UI_element(self,button_control)
         
        pane_control=automation.PaneControl(Name="HtmlPage")
        Document_Canvas.wait_for_object_exist(self,pane_control, 30)
            
    def create_new_document_canvas_with_options(self,tree_path,item, **kwargs):
        automation.TabItemControl(Name="Home").Click()
        time.sleep(4)
        automation.MenuItemControl(Name="All Files").Click()
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
          
        if stat==True:
            automation.TreeItemControl(Name=item).ScrollIntoView()
            time.sleep(8)
            automation.TreeItemControl(Name=item).RightClick()
            time.sleep(3)
            automation.MenuItemControl(Name="New").Click()
            time.sleep(3)
            automation.MenuItemControl(Name="HTML/Document").DoubleClick()
        else:
            
            Document_Canvas.select_UI_item_using_right_click_menu(self,tree_path, item, "New->HTML/Document")
        automation.RadioButtonControl(Name="Document (PDF, Excel...)").Click()
        
        button_control=automation.ButtonControl(Name='Next >')
        Document_Canvas.click_on_UI_element(self,button_control)
        
        if 'output' in kwargs:
            automation.ComboBoxControl(AutomationId="23453").ButtonControl(Name="Open").Click()
            time.sleep(3)
            automation.ListItemControl(Name=kwargs['output']).Click()
            time.sleep(3)
        
        if 'coordinate' in kwargs:
            automation.ComboBoxControl(Name="Units").ButtonControl(Name="Open").Click()
            time.sleep(3)
            automation.ListItemControl(Name=kwargs['coordinate']).Click()
            time.sleep(3)
        
        if 'page_size' in kwargs:
            automation.ComboBoxControl(Name="Additional Pages").ButtonControl(Name="Open").Click()
            time.sleep(3)
            automation.ListItemControl(Name=kwargs['page_size']).Click()
            time.sleep(3)
            
        if 'page_orientation' in kwargs:
            automation.ComboBoxControl(Name="Chart Engine").ButtonControl(Name="Open").Click()
            time.sleep(3)
            automation.ListItemControl(Name=kwargs['page_orientation']).Click()
            time.sleep(3)
            
        
        if 'units' in kwargs:
            automation.ComboBoxControl(Name="Page Orientation").ButtonControl(Name="Open").Click()
            time.sleep(3)
            automation.ListItemControl(Name=kwargs['units']).Click()
            time.sleep(3)
        
        if 'add_toc' in kwargs:
            automation.CheckBoxControl(Name="Add Table of Contents").Toggle(waitTime=2)
            time.sleep(3)

        if 'add_master_page' in kwargs:
            automation.CheckBoxControl(Name="Add Master Page").Toggle(waitTime=2)
            time.sleep(3)
            
             
        button_control=automation.ButtonControl(Name='Finish')
        Document_Canvas.wait_for_object_exist(self,button_control, 30)
        Document_Canvas.click_on_UI_element(self,button_control)
         
        pane_control=automation.WindowControl(Name="Document1")
        Document_Canvas.wait_for_object_exist(self,pane_control, 45)

    def draw_item_on_canvas(self,tab_name,ribbon_button_name,start_x,start_y,end_x,end_y,elem_name="Document1"):
        as_html_canvas_area.AS_Html_Canvas.drag_drop_on_canvas(self,tab_name,ribbon_button_name,start_x,start_y,end_x,end_y,elem_name=elem_name)
    
    def draw_item_on_canvas_no_select(self,start_x,start_y,end_x,end_y):
        as_html_canvas_area.AS_Html_Canvas.drag_drop_on_canvas_no_select(self,start_x,start_y,end_x,end_y)
    
    def verify_button_enabled(self, msg, button_name, enabled=True):
        '''
        Verify a button object is enabled on UI
        '''
        as_utillobj.verify_element_using_ui(self, msg, button_item=button_name, enabled=True) 
    
    def verify_menu_item_enabled(self, msg, menu_item, enabled=True):
        '''
        Verify a button object is enabled on UI
        '''
        as_utillobj.verify_element_using_ui(self, msg, menu_item_enabled=menu_item, enabled=True)
    
    def verify_button_disabled(self, msg, button_name, disabled=True):
        '''
        Verify a button object is enabled on UI
        '''
        as_utillobj.verify_element_using_ui(self, msg, button_item=button_name, disabled=True)
            
    def open_Document_Canvas_document(self,tree_path,item):
        automation.TabItemControl(Name="Home").Click()
        time.sleep(4)
        automation.MenuItemControl(Name="All Files").Click()
        
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
         
        if stat==True:
            automation.TreeItemControl(Name=item).ScrollIntoView()
            time.sleep(8)
            automation.TreeItemControl(Name=item).RightClick()
            time.sleep(3)
            automation.MenuItemControl(Name="Open").Click()
        else:
            
            Document_Canvas.select_UI_item_using_right_click_menu(self,tree_path, item, "Open")
 
       
    def create_new_report_chart_from_canvas_component_by_context_menu(self, comp_type,appdir,master_file,comp_x,comp_y): 
        if comp_type.lower()=="report":
            item="New report"
        elif comp_type.lower()=="chart":
            item="New chart"
        else:
            print ("wrong type ", comp_type.lower())
        
        automation.PaneControl(AutomationId="59648").RightClick(comp_x,comp_y)
          
        menu_item=automation.MenuItemControl(Name=item)
        Document_Canvas.wait_for_object_exist(self,menu_item, 20)
        menu_item.DoubleClick(20,4)
          
        win_control=automation.WindowControl(Name="Select Data Source")
  
        Document_Canvas.wait_for_object_exist(self,win_control, 30)
          
        Document_Canvas.select_item_from_tree_view(self,appdir, master_file, 'OK') 
        
    def add_fields_in_report_painter(self,field_name_list):
        text_control=automation.WindowControl(Name="Project View")
        Document_Canvas.wait_for_object_exist(self,text_control, 30)
        automation.TabItemControl(Name='Fields').Click(waitTime=1)
        time.sleep(9)
        f_list=field_name_list
        for item in f_list:
            tree_item=automation.TreeItemControl(Name=item)
            tree_item.DoubleClick()
            time.sleep(5)
    
    def add_fields_in_ia(self,field_name_list):
        text_control=automation.PaneControl(Name="- WebFOCUS InfoAssist+")
        Document_Canvas.wait_for_object_exist(self,text_control, 30)
        
        f_list=field_name_list
        for item in f_list:
            tree_item=automation.TextControl(Name=item)
            tree_item.DoubleClick(20,4)
            time.sleep(5)
    def refresh_tree(self,item):
        automation.TreeItemControl(Name=item).ScrollIntoView()
        time.sleep(3)
        automation.TreeItemControl(Name=item).RightClick()
        time.sleep(3)
        automation.MenuItemControl(Name="Refresh Descendants").MoveCursor()
        time.sleep(3)
        automation.MenuItemControl(Name="Refresh Descendants").Click()
        time.sleep(3)
            
    def refresh_tree_and_close_canvas_item(self, item):  
        Document_Canvas.refresh_tree(self, item)
        as_utillobj.close_canvas_item(self)
        time.sleep(6)
        stat=automation.ButtonControl(Name="Yes").Exists()
        if stat==True:
            btn_control=automation.ButtonControl(Name="Yes")
            Document_Canvas.wait_for_object_exist(self,btn_control, 30)
            btn_control.SetFocus()
            btn_control.Click()  
    def click_change_item_properties_tab_using_sikuli(self, image_name, x_val,y_val,click_type,text_to_add):
        time.sleep(4)
         
        #as_utillobj.click_picture_using_sikuli(self,image_name, x_val,y_val,click_type)
        as_utillobj.click_picture_from_region_using_sikuli(self,image_name, x_val,y_val,click_type, 'right')
         
        time.sleep(60)
        print ("60 seconds done")
        
        automation.SendKey(automation.Keys.VK_END)
  
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_HOME)
 
        time.sleep(3)
        automation.SendKeys('{Ctrl}a')
        time.sleep(3)
        automation.SendKeys('{Delete}')
      
        time.sleep(3)
        css=text_to_add
        automation.SendKeys(css)
       
        time.sleep(3) 
        automation.SendKeys('{Enter}')
        
    def use_existing_fex_on_canvas_component_by_context_menu(self, comp_type,appdir,master_file,comp_x,comp_y): 
        if comp_type.lower()=="reference":
            item="Reference existing procedure"
        elif comp_type.lower()=="import":
            item="Import existing report"
        elif comp_type.lower()=="import_chart":
            item="Import existing chart"
        else:
            print ("wrong type ", comp_type.lower())
        
        automation.PaneControl(AutomationId="59648").RightClick(comp_x,comp_y)
          
        menu_item=automation.MenuItemControl(Name=item)
        Document_Canvas.wait_for_object_exist(self,menu_item, 20)
        menu_item.DoubleClick(20,4)
          
        win_control=automation.WindowControl(Name="Open File")
  
        Document_Canvas.wait_for_object_exist(self,win_control, 30)
          
        Document_Canvas.select_item_from_tree_view(self,appdir, master_file, 'OK') 
    def get_element_obj(self,element_css, pos):
        a1=as_utillobj.get_elem_obj(self,element_css, pos)
        return(a1)
    def click_elem(self,element, x_offset, y_offset):
        as_utillobj.click_on_elem(self, element, x_offset, y_offset)
        
    def select_tooltip_option(self, parent, item_name):
        as_utillobj.select_tooltip_item(self, parent, item_name)
    
    def click_on_web_element_default(self, select_css):
        '''
        Desc: This function will click on a web element
        '''
        element_obj = self.se_driver.find_element_by_css_selector(select_css)
        element_obj.click()
        #coreutillobject.left_click(self, element_obj,element_location='middle',xoffset=xoffset,yoffset=yoffset,mouse_move_duration=5)
        
    def double_click_web_element_default(self, element_css):
        as_utillobj.double_click_web_element(self, element_css)
        
    def create_new_report_options(self,tree_path,item, method, folder, masterfile,**kwargs):
        automation.TabItemControl(Name="Home").Click()
        time.sleep(4)
        automation.MenuItemControl(Name="All Files").Click()
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
        
        if method=="toolbar_button":
            automation.ButtonControl(Name="Report").Click()
            time.sleep(4)
            win_control=automation.WindowControl(Name="Report Wizard")
            as_utillobj.wait_for_UI_object(self,win_control,30)
            automation.ButtonControl(Name="  Create Report").Click()
            time.sleep(8)
            automation.WindowControl(ClassName="#32770").TreeItemControl(Name=item).ScrollIntoView()
            time.sleep(8)
            automation.TreeItemControl(Name=item).Click()
            time.sleep(4)
            automation.WindowControl(ClassName="#32770").ButtonControl(AutomationId="12324").Click()
            time.sleep(4)
            win_control=automation.WindowControl(Name="Select Data Source")
            as_utillobj.wait_for_UI_object(self,win_control,30)
            as_utillobj.select_UI_tree_view_item(self,folder, masterfile, 'Finish')
        elif method=="context_menu":
            if stat==True:
                automation.TreeItemControl(Name=item).ScrollIntoView()
                time.sleep(8)
                automation.TreeItemControl(Name=item).RightClick()
                time.sleep(3)
                automation.MenuItemControl(Name="New").Click()
                time.sleep(3)
                automation.MenuItemControl(Name="Report").DoubleClick()
            else:
                Document_Canvas.select_UI_item_using_right_click_menu(self,tree_path, item, "New->Report")
            win_control=automation.WindowControl(Name="Select Data Source")
            as_utillobj.wait_for_UI_object(self,win_control,30)
            time.sleep(8)
            automation.WindowControl(Name="Select Data Source").TreeItemControl(Name="Domains").Click()
            time.sleep(3)
            as_utillobj.select_UI_tree_view_item(self,folder, masterfile, 'OK')
        
        win_control=automation.WindowControl(Name="Report1")
        as_utillobj.wait_for_UI_object(self,win_control,45)
        
    def scroll_to_environment_tree_item(self,tree_path, item):
        as_utillobj.navigate_to_env_tree_item(self, tree_path, item)    
        
    def run_canvas_item_from_toolbar(self):    
        automation.SplitButtonControl(Name="Run").Click()
    
    def run_canvas_item_from_asmenu(self,refresh_folder):    
        Document_Canvas.refresh_tree(self,refresh_folder)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_R, waitTime=3)
        time.sleep(2)
        
    def refresh_save_as_canvas_item(self,refresh_folder,save_name):
        Document_Canvas.refresh_tree(self,refresh_folder)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
         
        as_utillobj.save_as_UI_dialog(self,save_name)
        
    def select_new_report_chart_canvas_by_context_menu(self,option,comp_x,comp_y):
        
        automation.PaneControl(AutomationId="59648").RightClick(comp_x,comp_y)
        time.sleep(4)
        automation.MenuItemControl(Name=option).Click()
    def click_tab_button(self,tab_name,button_name):
        tab_item=automation.TabItemControl(Name=tab_name)
        refresh_btn=automation.ButtonControl(Name=button_name)
         
        Document_Canvas.click_on_UI_element(self,tab_item)
        time.sleep(3)
        Document_Canvas.click_on_UI_element(self,refresh_btn)
        time.sleep(40)
    def procedure_view_select_context_menu(self,tree_item,menu_path):
        automation.PaneControl(AutomationId="1").Click()
        time.sleep(2)
        automation.TreeItemControl(Name=tree_item).Click()
        time.sleep(2)
        automation.TreeItemControl(Name=tree_item).RightClick(15,3)
        time.sleep(5)
        menu_list=menu_path.split("->")
        for each_item in menu_list:
            automation.MenuItemControl(Name=each_item).DoubleClick(36,5)
            time.sleep(2)
    def select_layout_properties_dropdown(self,layout_name):
        as_utillobj.change_page_layout_from_properties(self, layout_name)
    



