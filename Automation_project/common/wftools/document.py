
from common.lib.base import BasePage
from common.pages.visualization_ribbon import Visualization_Ribbon as visualribbon_obj
from common.pages.ia_miscelaneous import IA_Miscelaneous as miscelaneousobject
from common.pages.ia_resultarea import IA_Resultarea as iaresultarea_obj
from common.pages.visualization_resultarea import Visualization_Resultarea as visualresularea_obj
from common.pages.visualization_ribbon import Visualization_Ribbon as visual_ribbonobj
from common.lib.core_utility import CoreUtillityMethods as coreutillobject
from common.lib.utillity import UtillityMethods as utillobject
from common.pages.ia_run import IA_Run as iarunobject
from common.pages.ia_ribbon import IA_Ribbon as ia_ribbon_obj

class Document(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    listbox_css="#list_dPROMPT_1 table tr"

    def __init__(self, driver):
        super(Document, self).__init__(driver)

    """****************************************** This is for Common Section. ************************************"""
    
    def wait_for_number_of_element(self, element_css, expected_number=None, time_out=60):
        miscelaneousobject.wait_for_object(self, element_css, 'number', expected_number=expected_number, time_out=time_out)
    
    def wait_for_visible_text(self, element_css, visble_element_text=None, time_out=60):
        miscelaneousobject.wait_for_object(self, element_css, 'text', visble_element_text=visble_element_text, time_out=time_out)
        
    def invoke_ia_tool_using_api(self, tool='document', master='baseapp', mrid=None, mrpass=None, report_css="#resultArea", no_of_element=1, wait_time=0):
        '''
        Desc:-This function is used to invoke ia tool using the new folder structure
                '''
        wait_time= self.report_medium_timesleep if wait_time==0 else wait_time
        miscelaneousobject.invoke_ia_tool_using_api_(self, tool, master, mrid, mrpass)
        Document.wait_for_number_of_element(self, report_css, no_of_element, wait_time)
        
    def select_ia_ribbon_item(self, tab_name, ribbon_button_name, **kwargs):
        '''
        Syntax: select_ia_ribbon_item('Insert', 'Drop_Down')
        '''
        visualribbon_obj.select_ribbon_item(self, tab_name=tab_name, ribbon_button_name=ribbon_button_name, **kwargs)
    
    def repositioning_document_component_in_ia(self, horizontal_pos, vertical_pos, **kwargs):
        '''
        Syntax: repositioning_document_component_in_ia('8', '1')
        '''
        visualribbon_obj.repositioning_document_component(self, horizontal_pos=horizontal_pos, vertical_pos=vertical_pos, **kwargs)
        
    def resizing_document_component(self, size_height, size_width):
        '''
        This function will resize the document component such as textbox, dropdown etc..
        '''
        visualribbon_obj.resizing_document_component(self, size_height, size_width)
        
    def drag_drop_document_component(self,source_element_css, target_element_css, x, y, target_drop_point='top_right', mouse_speed=25):
        '''
        This function will drag and drop the components in results area.
        '''
        iaresultarea_obj.drag_drop_document_component(self, source_element_css, target_element_css, x, y, target_drop_point=target_drop_point, mouse_speed=mouse_speed)
    
    def choose_right_click_menu_item_for_prompt(self, prompt_css, item_name, **kwargs):
        '''
        This function will right click item in prompt
        '''
        visualresularea_obj.choose_right_click_menu_item_for_prompt(self, prompt_css, item_name, **kwargs)
        
    def customize_active_dashboard_properties(self, prompts=None, source=None, targets=None, msg="Step X", btn_type=None):
        '''
        This function will select fields add fields to target location.
        '''
        visualresularea_obj.customize_active_dashboard_properties(self, prompts=prompts, source=source, targets=targets, msg=msg, btn_type=btn_type)
        
    def add_and_verify_prompts_in_cascade(self, cascades=None, available_prompts=None, selected_prompts=None, msg="Step x"):
        '''
        This function will add and verify document components such list box, dropdown text box etc..
        '''
        visualresularea_obj.add_and_verify_prompts_in_cascade(self, cascades=cascades, available_prompts=available_prompts, selected_prompts=selected_prompts, msg=msg)
        
    def switch_to_new_window(self):
        '''
        Desc:- This function is used to switch to a new window.
        '''
        coreutillobject.switch_to_new_window(self)
        
    def switch_to_previous_window(self):
        '''
        Desc:- This function is used to switch to a previous window.
        '''
        coreutillobject.switch_to_previous_window(self)
        
    def switch_to_frame(self, frame_css="[id^='ReportIframe']"):
        '''
        Desc:- This function is used to switch to a Frame. Here you need to provide the css of the frame to be switched to.
        '''
        coreutillobject.switch_to_frame(self, frame_css=frame_css, timeout=60)
    
    def switch_to_default_content(self):
        '''
        Desc:- This function is used to switch back to default content from a frame.
        '''
        coreutillobject.switch_to_default_content(self)
        
    def api_logout(self):
        """
        Desc: This function uses new function to pass the api logout url
        """
        utillobject.wf_logout(self)
        
    def set_browser_window_size(self, x='998', y='768'):
        '''
        Desc:-This function is used to resize the browser based on the given width and height
        '''
        utillobject.set_browser_window_size(self, x, y)
        
    def maximize_browser(self):
        '''
        Desc:-This function is used to maximize the browser window
        '''
        self.driver.maximize_window()
        
    def verify_prompts(self, component, parent_css , verify_list, msg, selected_check=None):
        '''
        Desc:- This function is used to verify the items inside the radio button or dropdown
        '''
        iarunobject.verify_active_dashboard_prompts(self, component, parent_css,verify_list, msg, default_selected_check=selected_check)
    
    def verify_prompts_in_preview(self, component, parent_css, verify_list, msg):
        '''
        Desc:- This function is used to verify the items inside the radio button or dropdown or listbox in preview
        '''
        iaresultarea_obj.verify_active_dashboard_prompts(self, component_type=component, parent_css=parent_css, expected_value_list=verify_list, msg=msg)    
        
    def select_prompt(self, component, parent_css, select_list, scroll_down_times=0):
        '''
        Desc:- This function is used to select prompt 
        '''
        iarunobject.select_active_dashboard_prompts(self, component, parent_css, select_list, scroll_down_times=scroll_down_times)
    
    def select_active_document_page_layout_menu_run_window(self, value_to_select):
        '''
        Desc:- This function is used to select the mutipage document in run mode
        Usage:-select_active_document_page_layout_menu(self,'page1')
        '''
        iarunobject.select_active_document_page_layout_menu(self, value_to_select)
    
    def verify_active_document_page_layout_menu_run_window(self,table_css,expected_list,msg):
        
        '''
        Desc:- This function is used to verify the mutipage document in run mode
        Usage:-verify_document_page_layout_menu("table[id='iLayTB$']",['Layouts','Page 1','Page 2'], "Step02: Verify")
        '''
        
        iarunobject.verify_active_document_page_layout_menu(self,table_css,expected_list,msg)   
    
    def select_result_area_panel_caption_button(self, selection, custom_css="[class*='window-caption']"):
        '''
        Desc:- This function is used to select the panel button
        usage: select_result_area_panel_caption_button(self, 'close')
        '''
        visualresularea_obj.select_panel_caption_btn(self, 0, select_type=selection, custom_css=custom_css)
        
    def enter_text_in_document_Textbox(self, text_box, text_input, delete_count=20): 
        
        '''
        Desc:- This function is used to enter the text
        Usage:-enter_text_in_document_Textboxenter_text_in_TextBox('Text_1', "This is simple text input")
        '''
        iaresultarea_obj.enter_text_in_Textbox(self, text_box, text_input, delete_count)
        
    def verify_text_in_document_Textbox(self, text_box, exp_textbox_text, msg):
        '''
        Desc:- This function is used to verify the entered the text
        Usage:-enter_text_in_document_Textboxenter_text_in_TextBox('Text_1', "This is simple text input")
        '''
        iaresultarea_obj.verify_text_in_Textbox(self, text_box, exp_textbox_text, msg)

    def select_or_verify_document_page_menu(self, item_name,default_page_name='Page 1', **kwargs):
        '''
        Desc:- This function is used to verify the page menu in document
        Usage:-select_or_verify_document_page_menu("New Page")
        '''       
        iaresultarea_obj.select_or_verify_document_page_menu(self, item_name,default_page_name,**kwargs)  
        
    def verify_selected_value_in_active_dashboard_prompts(self, component, parent_css, expected_list, msg):
        '''
        Desc:- This function is used to select the panel button
        usage: verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['Coffee', 'Gifts'], 'Step 4.1: Verify the selected checkbox')
        '''
        iarunobject.verify_selected_value_in_active_dashboard_prompts(self, component, parent_css, expected_list, msg)
      
    def verify_default_selected_listbox_value(self, default_value, default_value_color, parent_css=listbox_css, msg="Step X"):
        '''
        Desc:- This function is used to verify the selected default value in the added listbox in document
        usage:-
        '''
        iarunobject.verify_default_selected_listbox_value(self, parent_css, default_value, default_value_color, msg=msg)
        
    def verify_output_format(self,expected_format,step="Step x"):
        '''
        Desc:- This function is used to select the panel button
        usage: document_obj.verify_output_format("Active PDF", step="Step 3")
        '''
        ia_ribbon_obj.verify_output_format(self, expected_format, msg=step) 
        
    def select_build_a_document_in_splash_options(self, **kwargs):
        '''
        This function will select new document from splash window
        '''
        visualribbon_obj.select_item_in_splash_options(self, 'Build a Document',**kwargs)
    
    def select_ia_application_menu(self, menu_name):
        """
        Description : Click on application button and select menu
        """
        visual_ribbonobj.select_visualization_application_menu_item(self, menu_name)
        
      
     
    
        
    
        
        
        
    
        
