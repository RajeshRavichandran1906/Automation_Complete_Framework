from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utils
from common.lib.webfocus.resource_dialog import ResourceDialog
from common.lib.core_utility import CoreUtillityMethods as core_utils
from common.pages.page_designer_design import PageDesignerDesign as pd_design
from common.pages.page_designer_preview import PageDesignerPreview as pd_preview
from common.pages.page_designer_design import AddFilterControlsDialog, TabContainer, AccordionContainer
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as pd_miscelaneous
from common.pages.portal_canvas import Portal_canvas

class Design(BasePage):
        
    def __init__(self, driver):
        super(Design, self).__init__(driver)
        self._portal_canvas = Portal_canvas(self.driver)
        
    def wait_for_number_of_element(self, element_css, expected_number=None, time_out=30, pause_time=1):
        """
        :usage wait_for_number_of_element(total_no_of_riser_css, 28, wait_time_in_sec)
        """
        utils.synchronize_with_number_of_element(self, element_css, expected_number, time_out, pause_time)
    
    def wait_for_visible_text(self, element_css, visble_element_text=None, time_out=30,  pause_time=1):
        """
        :usage wait_for_visible_text(x_title_element_css, 'Product Category', wait_time_in_sec)
        """
        utils.synchronize_with_visble_text(self, element_css, visble_element_text, time_out,  pause_time)
    
    def invoke_page_designer(self, mrid=None, mrpass=None, folder_path=None):
        """
        Descriptions : This method used to invoke page designer page from given folder path
        example usage : invoke_page_designer()
        """
        pd_design.invoke_page_designer(self, mrid, mrpass, folder_path)
    
    def expand_content_folder(self, folder_path):
        """
        Description : This method will expand content 
        """
        pd_miscelaneous.expand_pd_content_folder(self, folder_path)
    
    def expand_content_folder_by_double_click(self, folder_path, left_click=False):
        """
        Description : This method will expand content by double click
        """
        pd_miscelaneous.expand_pd_content_folder(self, folder_path, left_click=left_click)
    
    def collapse_content_folder(self, folder_path):
        """
        Description : This method will collapse content 
        """
        pd_design.collapse_content_folder(self, folder_path)
        
    def collapse_content_folder_by_double_click(self, folder_path, left_click=False):
        """
        Description : This method will collapse content by double click
        """
        pd_design.collapse_content_folder(self, folder_path, left_click=left_click)
        
    def invoke_page_designer_and_select_template(self, template_name, mrid=None, mrpass=None, folder_path=None, from_designer_group=False):
        """
        Descriptions : This method used to invoke page designer page and select template
        example usage : invoke_page_designer_and_select_template('Blank')
        template names : 'Blank', 'Grid 2-1', 'Grid 4-2-1', 'Grid 3-3-3'
        from_designer_group - True if click on page icon from designer group other it will click on page in common group in home page
        """
        pd_design.invoke_page_designer_and_select_template(self, template_name, mrid, mrpass, folder_path, from_designer_group)
    
    def select_page_designer_template(self, template_name):
        """
        Descriptions : This method used to select the page designer template
        template names : 'Blank', 'Grid 2-1', 'Grid 4-2-1', 'Grid 3-3-3'
        example usage : select_page_designer_template('Blank')
        """
        pd_miscelaneous.select_page_designer_template(self, template_name)
        
    def drag_content_item_to_blank_canvas(self, content_item_to_drog, blank_grid_index_to_drop, content_folder_path=None):
        """
        Descriptions : This method used to drag content item to bank grid canvas
        :arg- content_item_drog = Which content item drag to canvas
        :arg- blank_grid_index_to_drop = Position of bank grid to drop item ( blank_grid_index start from 1)
        :arg- content_folder_path = Content folder path to select item 
        example usage : drag_content_item_to_blank_canvas('01 - Simple Input Required', 2)
        """
        pd_design.drag_content_item_to_blank_canvas(self, content_item_to_drog, blank_grid_index_to_drop, content_folder_path)
    
    def drag_canvas_container_to_section_cell(self, canvas_container_title, section_cell_num, canvas_container_position=1, section_num=1):
        """
        Descriptions : This method will drag canvas container to blank section cell
        :Usage - drag_canvas_container_to_section_cell("Panel1", 4)'
        """
        pd_design.drag_canvas_container_to_section_cell(self, canvas_container_title, section_cell_num, canvas_container_position, section_num)
        
    def drag_content_item_to_container(self, content_item_to_drog, container_title_to_drop, container_position=1, content_folder_path=None):
        """
        Descriptions : This method used to drag content item to container
        :arg- content_item_drog = Which content item drag to container
        :arg- container_title_to_drop = Which container to drop content item
        :arg- container_position = Position of container. Some times two or more containers have same title that time we can pass container_position. container_position start form 1
        example usage : drag_content_item_to_container('01 - Simple Input Required', 'Panel 1')
        """
        pd_design.drag_content_item_to_container(self, content_item_to_drog, container_title_to_drop, container_position, content_folder_path)
    
    def drag_container_item_to_blank_canvas(self, container_name_to_drag, blank_grid_index_to_drop, section_num=1, element_location='middle', xoffset=0, yoffset=0):
        """
        Descriptions : This method used to drag container item to blank canvas
        :arg- container_name_to_drag : 'Panel' or 'Tab' or 'Carousel' or 'Accordion' or 'Grid'
        :arg- blank_grid_index_to_drop = Position of bank grid to drop item ( blank_grid_index start from 1)
        example usage : drag_container_item_to_blank_canvas('Panel', 1)
        """
        pd_design.drag_container_item_to_blank_canvas(self, container_name_to_drag, blank_grid_index_to_drop, section_num, element_location, xoffset, yoffset)
    
    def drag_basic_container_to_canvas_container(self, basic_container_name, canvas_container_title, location='middle',canvas_container_position=1):
        """
        Descriptions : This method will drag container to canvas container
        :Usage - drag_container_to_canvas_container("Grid", "Panel1")'
        """
        pd_design.drag_basic_container_to_canvas_container(self, basic_container_name, canvas_container_title,location,canvas_container_position)
    
    def drag_content_item_to_container_and_verify_drop_color(self, content_item, container_title, step_num, container_position=1):
        """
        Description : Drag content item and drop to canvas container and verify drop background color
        :Usage - drag_content_item_to_container_and_verify_drop_color("report", "Panel1", "02.02")
        """
        pd_design.drag_content_item_to_container_and_verify_drop_color(self, content_item, container_title, step_num, container_position)
        
    def drag_content_item_to_section_cell_and_verify_drop_color(self, content_item, section_cell_num, step_num, section_num=1):
        """
        Description : Drag content item and drop to bank section grid-cell canvas and verify drop target highlighted background color
        :Usage - drag_content_item_to_section_cell_and_verify_drop_color("report", 1, "02.02", section_num=1)
        """
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color(self, content_item, section_cell_num, step_num, section_num=section_num)
        
    def select_option_from_carousel_items(self, option_name):
        """
        Descriptions : This method used to select carousel items
        :arg-option_name : 'Containers' or 'Content' or 'Controls'
        example usage : select_option_from_carousel_items('Containers')
        """
        pd_design.select_option_from_carousel_items(self, option_name)
           
    def click_quick_filter(self):
        """
        Descriptions : This method used to click on quick filter option
        """
        pd_design.click_quick_filter(self)
    
    def click_preview(self):
        """
        Descriptions : This method used to click on preview button 
        """
        pd_design.click_preview(self)
    
    def click_toolbar_save(self):
        """
        Descriptions : This method used to click on toolbar save button 
        """
        pd_design.click_toolbar_save(self)
        
    def click_property(self):
        """
        Descriptions : This method used to click on property save button
        """
        pd_design.click_property(self)
    
    def click_filter_configuration(self):
        """
        Descriptions: This method is used to click on the filter configurations
        """
        pd_design.click_configuration(self)
        
    def select_filter_configurations_property(self, text_to_select):
        """
        Descriptions: This method is used to select the button in the filter configurations
        """
        pd_design.select_filter_configuration(self, text_to_select)
    
    def select_property_tab(self, tab_name):
        """
        Descriptions : This method will select property tab style
        example usage : select_property_tab()
        """
        pd_design.select_property_tab(self, tab_name)
        
    def select_property_tab_style_option(self, tab_name, property_type, property_name, property_value):
        """
        Descriptions : This method used to select specific property tab style content properties
        example usage : select_property_tab_content_properties('Page Style', 'Margin', 'text_box', '50%')
        """
        pd_design.select_property_tab_content_properties(self, 'style', tab_name, property_type, property_name, property_value)
    
    def select_property_tab_settings_option(self, tab_name, property_type, property_name, property_value=None):
        """
        Descriptions : This method used to select specific property tab style content properties
        example usage : select_property_tab_settings_option('Container Settings', 'Classes', 'text_box', 'Test')
        """
        pd_design.select_property_tab_content_properties(self, 'settings', tab_name, property_type, property_name, property_value)
    
    def verify_property_tab_style_option(self, tab_name, property_type, property_value_list, msg, comparision_type='asequal'):
        """
        Descriptions : This method used to verify specific property tab style content properties
        example usage : verify_property_tab_style_option('style', 'Page Style', 'text_box', ['Light'], 'Step 9: verify')
        """
        pd_design.verify_property_tab_content_properties(self, 'style', tab_name, property_type, property_value_list, msg, comparision_type=comparision_type)
        
    def close_page_designer_from_application_menu(self):
        """
        Descriptions : This method used to close the page desginer from application 
        """
        pd_design.close_page_designer_from_application_menu(self)
    
    def save_page_from_toolbar_with_default_name(self, wait_time=3):
        """
        Descriptions : This method used to click on save button on tool bar and save current page with default name  
        """
        pd_design.save_page_from_toolbar(self, None, wait_time)
    
    def save_page_from_toolbar(self, page_name_to_save, wait_time=3):
        """
        Descriptions : This method used to click on save button on tool bar and save current page with default name  
        """
        pd_design.save_page_from_toolbar(self, page_name_to_save, wait_time)
    
    def click_dialog_box_button(self, button_name):
        """
        Description : Click on button in dialog box.
        :Usage : click_dialog_box_button('Yes')
        """
        pd_design.click_dialog_box_button(self, button_name)
        
    def save_as_page_from_application_menu(self,page_name_to_save):
        """
        Descriptions : This method used to click on save as button from application menu and save the page. 
        """
        pd_miscelaneous.select_page_designer_application_menu(self,'Save as...')
        pd_miscelaneous.page_designer_open_dialog_resources(self, title=page_name_to_save, ok_button=True)
    
    def save_page_from_application_menu(self,page_name_to_save):
        """
        Descriptions : This method used to click on save button from application menu and save the page. 
        """
        pd_miscelaneous.select_page_designer_application_menu(self,'Save')
        pd_miscelaneous.page_designer_open_dialog_resources(self, title=page_name_to_save, ok_button=True)
        
    def select_option_from_application_menu(self, option_name):
        """
        Descriptions : This method used to option from application menu  like 'Open...', 'Save', 'New', etc... 
        @Usage select_option_from_application_menu('New')
        """
        pd_miscelaneous.select_page_designer_application_menu(self, option_name)
    
    def close_and_save_page_with_default_name(self, wait_time=2):
        """
        Descriptions : This method used to click on close button from application menu and save page
        """
        pd_design.close_and_save_page(self, None, wait_time)
    
    def close_page_designer_without_save_page(self):
        """
        Descriptions : This method used to click on close button from application menu and click on No button to leave  current page
        """
        pd_design.close_page_designer_from_application_menu(self)
        utils.synchronize_with_visble_text(self, "div[data-ibx-type='ibxDialog'][class*='pop-top']", "No", 15)
        pd_miscelaneous.dialog_box(self, button_name_to_click='No')
        
    def delete_saved_page_designer(self, page_name_to_delete='Page 1', folder_path=None):
        """
        Descriptions : This method used to delete the saved or already existed page designer
        example usage : run_page_designer('Page 1')
        """
        pd_design.delete_saved_page_designer(self, page_name_to_delete, folder_path)
        
    def switch_to_container_frame(self, container_title, container_position=1, timeout=30, wait_time=1, frame_index=1):
        """
        Descriptions : This method used to switch to iframe in specific pd container   
        """
        pd_design.switch_to_container_frame(self, container_title, container_position, timeout, wait_time, frame_index)
        
    def switch_to_default_page(self):
        """
        Descriptions : This method used to switch to default page from container iframe  
        """
        core_utils.switch_to_default_content(self)
    
    def switch_to_previous_window(self, driver_close=True):
        """
        Descriptions : This function will switch the control back to previous window by closing the current window.
        :arg - driver_close= If already target window closed then pass driver_close=False
        """
        pd_miscelaneous.switch_to_previous_window(self, driver_close)
        
    def run_page_designer(self, page_name_to_run='Page 1', folder_path=None):
        """
        Descriptions : This method used to run the saved or already existed page designer
        example usage : run_page_designer('Page 1')
        """
        pd_design.run_page_designer(self, page_name_to_run, folder_path)
    
    def edit_page_designer(self, page_name_to_edit, folder_path=None):
        """
        Descriptions : This method used to edit the saved or already existed page designer
        example usage : edit_page_designer('Page 1')
        """
        pd_design.edit_page_designer(self, page_name_to_edit, folder_path)
        
    def run_page_designer_by_double_click(self, page_name_to_run='Page 1', folder_path=None):
        """
        Descriptions : This method used to run the saved or already existed page designer by double click
        example usage : run_page_designer_by_double_click('Page 1')
        """
        pd_miscelaneous.run_page_designer_by_double_click(self, folder_path, page_name_to_run)
    
    def run_page_designer_in_new_window(self, page_name_to_run='Page 1', folder_path=None):
        """
        Descriptions : This method used to run the saved or already existed page designer in new window by right click on pd fex and select Run in new window
        example usage : run_page_designer_in_new_window('Page 1')
        """
        pd_design.run_page_designer_in_new_window(self, page_name_to_run, folder_path)
        
    def select_filter_control_context_menu(self, filter_control_name, context_menu, control_position=1):
        """
        Descriptions : This method used to select filter control context menu
        example usage : select_filter_control_context_menu('Business Region:', 'Settings')
        """
        pd_design.select_filter_control_context_menu(self, filter_control_name, context_menu, control_position)
    
    def select_container_context_menu(self, container_title, context_menu, container_position=1):
        """
        Descriptions : This method used to right click on container and select context menu
        example usage : select_container_context_menu('Panel1', 'Settings')
        """
        pd_design.select_container_context_menu(self, container_title, context_menu, container_position)
        
    def verify_container_context_menu(self, container_title, expected_context_menu_list, step_no, container_position=1, comparision_type='asequal'):
        """
        Descriptions : This method used to right click on container and verify context menu
        @param container_position: ordered position of container 
        @param comparision_type: comparision type like 'asequal', 'asnotin' or 'asin'
        example usage : verify_container_context_menu('Panel1', ['Settings'], '09.00')
        """
        pd_design.verify_container_context_menu(self, container_title, expected_context_menu_list, step_no, container_position=container_position, comparision_type=comparision_type)
        
    def convert_filter_control(self, filter_control_name, control_name_to_convert, filter_control_position=1):
        """
        Descriptions : This method used to convert filter control to some other filter controls. For example convert  drop down control to button set control. 
        example usage : convert_filter_control('Select North America', 'Button set')
        control_name_to_converts : 'Button set' , 'Checkbox', 'Dropdown'
        """
        pd_design.convert_filter_control(self, filter_control_name, control_name_to_convert, filter_control_position)
    
    def expand_and_collapse_content_tab(self, option):
        """
        Description: This method is used to expand or collapse the content tab in the page designer window
        usage: expand_and_collapse_content_tab('expand')
        """
        pd_design.expand_and_collapse_content_and_repository_widgets_tab(self, content=option)
    
    def expand_and_collapse_repository_widgets_tab(self, option):
        """
        Description: This method is used to expand or collapse the repository widgets tab in the page designer window
        usage: expand_and_collapse_repository_widgets_tab('expand')
        """
        pd_design.expand_and_collapse_content_and_repository_widgets_tab(self, repository_widgets=option)
    
    def drag_repository_widgets_item_to_blank_canvas(self, repository_widgets_name_to_drag, blank_grid_index_to_drop, section_num=1):
        """
        Description: THis methos is used to drag and drop the items under the repository widgets to blank canvas
        usage: drag_repository_widgets_item_to_blank_canvas('Explorer',1)
        """
        pd_design.drag_repository_widgets_item_to_blank_canvas(self, repository_widgets_name_to_drag, blank_grid_index_to_drop, section_num)
    
    def verify_repository_widgets_item(self,items_list,custom_msg):
        """
        Descriptions : This method use to verify the items in repository widgets:-
        @param: ['explorer','link_title']
        example usage:-verify_repository_widgets_items(['explorer','link_title'],"step 4")
        """
        pd_design.verify_repository_widgets_items(self, expected_widgets_list=items_list, msg=custom_msg)
    
    def select_section_style(self, style_name):
        """
        Descriptions : This method used to select section style by left click
        example usage : select_section_style("Style 2")
        """
        pd_design.select_style(self, 'Section Style', style_name)
    
    def select_grid_style(self, style_name):
        """
        Descriptions : This method used to select grid style by left click
        example usage : select_section_style("Style 2")
        """
        pd_design.select_style(self, 'Grid Style', style_name)
        
    def select_container_style(self, style_name):
        """
        Descriptions : This method used to select container style by left click
        example usage : select_section_style("Style 2")
        """
        pd_design.select_style(self, 'Container Style', style_name)
        
    def select_page_section_context_menu(self, section_num, context_menu):
        """
        Descriptions : Right click on page section at top left and click context menu
        example usage : select_page_section_context_menu(1, "Style") 
        """
        pd_design.select_page_section_context_menu(self, section_num, context_menu)
        
    "--------------------------------- Verification Method -------------------------------------------------"
    def verify_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Description : This method will verify whether add content button is displayed in panel container in canvas 
        example usage : verify_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_displayed_in_container(container_obj, 'panel', msg)
    
    def verify_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will verify content button color in container 
        example usage : verify_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_color_in_container(container_obj, 'panel', expected_color, msg)
    
    def verify_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will mouse move on add content button and verify color on container in canvas 
        example usage : verify_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.mouse_move_on_add_content_button_and_verify_color_in_container(container_obj, 'panel', expected_color, msg)
    
    def verify_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Description : This method will verify add content button tool-tip in container
        example usage : verify_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_tooltip_in_container(container_obj, 'panel', expected_tooltip, msg)
    
    def verify_tab_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Description : This method will verify whether add content button is displayed in tab panel container. 
        example usage : verify_tab_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_displayed_in_container(container_obj, 'tab', msg)
    
    def verify_tab_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will verify content button color in tab panel container. 
        example usage : verify_tab_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_color_in_container(container_obj, 'tab', expected_color, msg)
    
    def verify_tab_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will mouse move on add content button and verify color on container in tab panel container. 
        example usage : verify_tab_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.mouse_move_on_add_content_button_and_verify_color_in_container(container_obj, 'tab', expected_color, msg)
    
    def verify_tab_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Description : This method will verify add content button tool-tip in tab panel container.
        example usage : verify_tab_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_tooltip_in_container(container_obj, 'tab', expected_tooltip, msg)
    
    def verify_carousel_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Description : This method will verify whether add content button is displayed in tab panel container. 
        example usage : verify_carousel_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_displayed_in_container(container_obj, 'carousel', msg)
    
    def verify_carousel_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will verify content button color in tab panel container. 
        example usage : verify_carousel_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_color_in_container(container_obj, 'carousel', expected_color, msg)
    
    def verify_carousel_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will mouse move on add content button and verify color on container in tab panel container. 
        example usage : verify_carousel_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.mouse_move_on_add_content_button_and_verify_color_in_container(container_obj, 'carousel', expected_color, msg)
    
    def verify_carousel_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Description : This method will verify add content button tool-tip in tab panel container.
        example usage : verify_carousel_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_tooltip_in_container(container_obj, 'carousel', expected_tooltip, msg)
        
    def verify_accordion_panel_add_content_displayed_in_container(self, panel_name, msg, panel_index=1):
        """
        Description : This method will verify whether add content button is displayed in tab panel container. 
        example usage : verify_accordion_panel_add_content_displayed_in_container('Panel 1', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_displayed_in_container(container_obj, 'accordion', msg)
    
    def verify_accordion_panel_add_content_color_in_container(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will verify content button color in tab panel container. 
        example usage : verify_accordion_panel_add_content_color_in_container('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_color_in_container(container_obj, 'accordion', expected_color, msg)
    
    def verify_accordion_panel_add_content_color_in_container_after_mouse_move(self, panel_name, expected_color, msg, panel_index=1):
        """
        Description : This method will mouse move on add content button and verify color on container in tab panel container. 
        example usage : verify_accordion_panel_add_content_color_in_container_after_mouse_move('Panel 1', 'grey', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.mouse_move_on_add_content_button_and_verify_color_in_container(container_obj, 'accordion', expected_color, msg)
    
    def verify_accordion_panel_add_content_tooltip_in_container(self, panel_name, expected_tooltip, msg, panel_index=1):
        """
        Description : This method will verify add content button tool-tip in tab panel container.
        example usage : verify_accordion_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', 'Step 9: Verify')
        """
        container_obj = pd_design.get_container_object(self, panel_name, container_title_index=panel_index)
        self._portal_canvas.verify_add_content_button_tooltip_in_container(container_obj, 'accordion', expected_tooltip, msg)
        
    def verify_number_of_filter_grid_cells(self, expected_total_grid_cells, msg):
        """
        Descriptions : This method used to verify total filter grid cells in page designer
        example usage : verify_number_of_filter_grid_cells(6, 'Step 01.1 : Verify 6 filter grid cells are display')
        """
        pd_design.verify_number_of_filter_grid_cells(self, expected_total_grid_cells, msg)
    
    def verify_filter_control_labels(self, expected_label_list, msg, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to filter panel heading labels
        example usage : verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], 'Step 01.1 : Verify filter panel heading labels)
        :arg - grid_container_title = 'Panel1'. If you want to verify filter labels inside grid container then pass grid container title. 
        """
        pd_design.verify_filter_control_labels(self, expected_label_list, msg, grid_container_title=grid_container_title, model_window=model_window)
        
    def verify_number_of_page_sections(self, expected_total_sections, msg):
        """
        Descriptions : This method used to verify total number of page sections displaying in canvas
        example usage : verify_number_of_page_sections(5, 'Step 01.1 : Verify 5 page sections are displaying in page canvas') 
        """
        pd_design.verify_number_of_page_sections(self, expected_total_sections, msg)
    
    def verify_number_of_panels(self, expected_total_panels, msg):
        """
        Descriptions : This method used to verify total number of panels displaying on canvas
        example usage : verify_number_of_panels(5, 'Step 01.1 : Verify 5 panels are displaying in page canvas') 
        """
        pd_design.verify_number_of_panels(self, expected_total_panels, msg)
    
    def verify_containers_title(self, expected_title_list, msg):
        """
        Descriptions : This method used to verify pd container titles
        example usage: verify_containers_title(["Panel 1", "Panel 2", "Panel 3", "Category Sales"], 'Step 01.1 : Verify container titles') 
        """
        pd_design.verify_containers_title(self, expected_title_list, msg)
    
    def verify_container_title_bar_visible_buttons(self, container_title, expected_buttons, msg, container_position=1):
        """
        Descriptions : This method used to verify visible container title bar button such as 'Maximize', 'Options' and 'Restore'
        example usage : verify_container_title_bar_button_options('Panel 6', ['Maximize', 'Options'], 'Step 01.1 : Verify ['Maximize', 'Options'] buttons display on container tool bar')
        """
        pd_design.verify_container_title_bar_visible_buttons(self, container_title, expected_buttons, msg, container_position)
    
    def verify_quick_filter_value(self, expected_value, step_no):
        """
        Descriptions : This method used to verify quick filter value.
        example usage : verify_quick_filter_value('3', 'Step 01.1' 
        """
        pd_design.verify_quick_filter_value(self, expected_value, step_no)
    
    def verify_quick_filter_properties(self,properties_as_dic, msg):
        """
        Descriptions : This method used to quick filter properties such as filter count value, backgroud_color, font size and etc..
        :arg- properties_as_dic = Should be paass as dictionary
        example usage : verify_quick_filter_properties({'text':'1', 'background_color':'mandy', 'font_size':'12px', 'position':'absolute', 'text_align':'center'}, 'Step01.1')
        """
        pd_design.verify_quick_filter_properties(self, properties_as_dic, msg)
    
    def verify_page_heading_title(self, expected_title_list, msg):
        """
        Descriptions : This method used to verify page header title. expected title should be pass as list
        example usage : verify_page_heading_title(['Page Heading'], 'Step 01.1 : Verify page title')
        """
        pd_design.verify_page_heading_title(self, expected_title_list, msg)
        
    def verify_page_header_visible_buttons(self, expected_visible_buttons, msg):
        """
        Descriptions : This method used to verify page header visible buttons such as 'Refresh', 'Filter'
        example usage : verify_page_header_visible_buttons('['Refresh', 'Filter'], 'Step 01.1 : Verify Refresh and Filter button are display on page header')
        """
        pd_design.verify_page_header_visible_buttons(self, expected_visible_buttons, msg)
        
    def verify_page_tab_groups(self, expected_groups, msg):
        """
        Descriptions : This method used to verify page page tab group name. Page tab group appear on bottom of the page
        example usage : verify_page_tab_groups(['Page 1'], 'Step 01.1 : Verify page tab groups')
        """
        pd_design.verify_page_tab_groups(self, expected_groups, msg)
        
    def verify_filter_control_panel_is_selected(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether specific filter condition panel is selected
        example usage : verify_filter_control_panel_is_selected('Business Region:', 'Step 01.1 : Verify Business Region condition is selected')
        """
        pd_design.verify_filter_control_panel_is_selected(self, filter_control_name, msg, filter_control_position, grid_container_title, model_window)
    
    def verify_filter_control_panel_is_not_selected(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether specific filter control panel is not selected
        verify_filter_control_panel_is_not_selected('Business Region:', 'Step 01.1 : Verify Business Region filter control is not selected')
        """
        pd_design.verify_filter_control_panel_is_not_selected(self, filter_control_name, msg, filter_control_position, grid_container_title, model_window)
        
    def verify_filter_inputbox_is_not_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is not optional. If not optional means drop down control bounded with red solid border around it.
        example usage : verify_filter_inputbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region control input box is selected')
        """
        pd_design.verify_filter_inputbox_is_not_optional(self, filter_control_name, msg,  border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_inputbox_is_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If optional means drop down control not bounded with red solid border around it.
        example usage : verify_filter_inputbox_is_optional('Business Region:', 'Step 01.1 : Verify Business Region control input box is not selected')
        """
        pd_design.verify_filter_inputbox_is_optional(self, filter_control_name, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_default_output_for_input_required_container(self, container_title, msg, expected_output='A required parameter is missing', container_position=1) :
        """
        Descriptions : This method used to verify default output for input required fex contains container text
        example usage : verify_default_output_for_input_required_container('01 - Simple Input Required', 'Step 01.1 : Verify report added to the page successfully.')
        """
        pd_design.verify_default_output_for_input_required_container(self, container_title, msg, expected_output, container_position)
        
    def verify_property_tabs(self, expected_tabs, msg):
        """
        Descriptions : This method used to verify property widow tabs
        example usage : verify_property_tabs(['Settings', 'Style'], 'Step 06.1 : Verify Property_tabs')
        """
        pd_design.verify_property_tabs(self, expected_tabs, msg)
    
    def verify_setting_tabs(self, expected_tabs, msg):
        """
        Descriptions : This method used to verify setting tabs
        example usage : verify_setting_tabs(['General Settings', 'Control Settings', 'Data Settings', 'Parameters'], 'Step 01.1 : Step 06.2 : Verify ['General Settings', 'Control Settings', 'Data Settings', 'Parameters'] tabs are display in setting tab - PASSED.')
        """
        pd_design.verify_setting_tabs(self, expected_tabs, msg)
        
    def verify_setting_tab_properties(self,tab_name, expected_properties, msg, property_tab_name='settings'):
        """
        Descriptions : This method used to verify specific setting tab properties
        example usage1 : verify_setting_tab_properties('General Settings', ['Type=Input', 'Tooltip=', 'Global name='], 'Step 06.3 : Verify General Settings properties')
        example usage2 : verify_setting_tab_properties('Control Settings', ['Optional=off', 'Placeholder text='], 'Step 06.3 : Verify Control Settings properties') 
        """
        pd_design.verify_setting_tab_properties(self, tab_name, expected_properties, msg, property_tab_name=property_tab_name)
        
    def verify_setting_parameter_tab_properties(self, expected_values, msg):
        """
        Descriptions : This method used to verify parameter tab properties in setting tab
        example usage : verify_setting_parameter_tab_properties(['BUSINESS_REGION (A15V)'], 'Step 06.5 : Verify parameter properties')
        """
        pd_design.verify_setting_parameter_tab_properties(self, expected_values, msg)
    
    def create_html_report_data_set(self, file_name_to_save, table_css="table[summary]"):
        """
        Descriptions : This method used to verify parameter tab properties in setting tab
        example usage : create_html_report_data_set('C2345_DataSet_01')
        """
        pd_miscelaneous.create_report_data_set_using_bs4(self, file_name_to_save, table_css)
        
    def verify_html_report_data_set(self, saved_file_name, msg, table_css="table[summary]"):
        """
        Descriptions : This method used to verify parameter tab properties in setting tab
        example usage : verify_html_report_data_set('C2345_DataSet_01', 'Step 01.1 : Verify report data')
        """
        pd_miscelaneous.verify_report_table_data_using_bs4(self, saved_file_name, msg, table_css)
    
    def verify_filter_inputbox_value(self, filter_control_name, expected_value_list, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter input box values
        example usage : verify_filter_inputbox_value('Business Region:', ['EMP'], 'Step 01.1 : Verify Business Region condition inbutbox is selected')
        """
        pd_design.verify_filter_inputbox_value(self, filter_control_name, expected_value_list, msg, filter_control_position)
    
    def verify_blank_container_output(self, container_title, msg, container_position=1):
        """
        Descriptions : This method used to verify blank containers output which means blank container should be blank
        example usage : verify_blank_container_output('Panel 2', 'Step 01.1 : Verify Panel 1 is blank')
        """
        pd_design.verify_blank_container_output(self, container_title, msg, container_position)
    
    def verify_html_report_has_vertical_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container html report has vertical scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because html report placed inside the container iframe
        """
        pd_design.verify_report_has_vertical_scrollbar(self, "html", msg)
        
    def verify_html_report_has_horizontal_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container html report has horizontal scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        pd_design.verify_report_has_horizontal_scrollbar(self, "html", msg)
    
    def verify_html_report_does_not_have_vertical_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container report does not have vertical scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because html report placed inside the container iframe
        """
        pd_design.verify_report_does_not_have_vertical_scrollbar(self, "html", msg)
    
    def verify_html_report_does_not_have_horizontal_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container report does not have horizontal scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        pd_design.verify_report_does_not_have_horizontal_scrollbar(self, "html", msg)
    
    def verify_html_report_vertical_scrollbar_reached_bottom(self, msg):
        """
        Descriptions : This method used to verify whether specific container report vertical scroll bar reached bottom
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        pd_design.verify_report_vertical_scrollbar_reached_bottom(self, "html", msg)

    def verify_filter_dropdown_is_not_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is not optional. If not optional means drop down control bounded with red solid border around it.
        example usage : verify_filter_dropdown_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter drop down control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_dropdown_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_dropdown_is_optional(self, filter_control_name, msg,  filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If optional means drop down control not bounded with red solid border around it.
        example usage : verify_filter_dropdown_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter drop down control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_dropdown_is_optional(self, filter_control_name, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_buttonset_is_not_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If not optional means button set control bounded with red solid border around it.
        example usage : verify_filter_buttonset_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter button set control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_buttonset_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position)
    
    def verify_filter_buttonset_is_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If optional means button set control not bounded with red solid border around it.
        example usage : verify_filter_buttonset_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter button set control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_buttonset_is_optional(self, filter_control_name, msg, filter_control_position)
    
    def verify_selected_value_of_filter_dropdown(self, filter_control_name, expected_value_list, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter drop down selected value or default value
        example usage : verify_selected_value_of_filter_dropdown('Business Region:', ['EMP'], 'Step 01.1 : Verify Business Region drop down selected EMP value')
        """
        pd_design.verify_selected_value_of_filter_dropdown(self, filter_control_name, expected_value_list, msg, filter_control_position)

    def verify_filter_buttonset_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter buttonset options
        example usage : verify_filter_buttonset_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter button set control')
        """
        pd_design.verify_filter_buttonset_options(self, filter_control_name, expected_options, msg, filter_control_position)
        
    def verify_selected_options_in_filter_buttonset(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter button set control.It will verify selected options based on backgroud color of option
        example usage : verify_filter_buttonset_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter button set control')
        """
        pd_design.verify_selected_options_in_filter_buttonset(self, filter_control_name, expected_selected_options, msg, filter_control_position)
        
    def verify_filter_control_converter_window(self, filter_control_name, msg_step_no, expected_controls_list=None, verify_window_display_position=False, window_title='Convert Control To', filter_control_position=1):
        """
        Descriptions : This method used to verify filter control converter window.
        example usage : verify_filter_control_converter_window('Select North America', '01.1', expected_controls_list=['Button set', 'Checkbox'], verify_window_display_position=True]
        """    
        pd_design.verify_filter_control_converter_window(self, filter_control_name, msg_step_no, expected_controls_list, verify_window_display_position, window_title, filter_control_position)
    
    def verify_filter_radio_group_is_not_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter radio button group control is not optional. If not optional means button set control bounded with red solid border around it.
        example usage : verify_filter_radio_group_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_radio_group_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position)
    
    def verify_filter_radio_group_is_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If optional means button set control not bounded with red solid border around it.
        example usage : verify_filter_radio_group_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_radio_group_is_optional(self, filter_control_name, msg, filter_control_position)
    
    def verify_filter_radio_group_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter radio group options
        example usage : verify_filter_radio_group_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter radio group control')
        """
        pd_design.verify_filter_radio_group_options(self, filter_control_name, expected_options, msg, filter_control_position)
    
    def verify_selected_options_in_filter_radio_group(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter radio group control.
        example usage : verify_selected_options_in_filter_radio_group('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter radio group control')
        """
        pd_design.verify_selected_options_in_filter_radio_group(self, filter_control_name, expected_selected_options, msg, filter_control_position)
    
    def verify_filter_date_picker_is_not_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter date picker control is not optional. If not optional means date picker control bounded with red solid border around it.
        example usage : verify_filter_date_picker_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter date picker control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_date_picker_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_date_picker_is_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter date picker is optional. If optional means date picker control not bounded with red solid border around it.
        example usage : verify_filter_date_picker_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter date picker control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_date_picker_is_optional(self, filter_control_name, msg, filter_control_position=filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_selected_date_in_filter_date_picker(self, filter_control_name, expected_selected_date, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify selected date value in filter data picker control
        example usage : verify_selected_date_in_filter_date_picker('Select 2016/03/17', ['Jun 19, 2018'], 'Step 01.1 : Verify Jun 19, 2018 date selected in data picker control')
        """
        pd_design.verify_selected_date_in_filter_date_picker(self, filter_control_name, expected_selected_date, msg, filter_control_position)
        
    def verify_filter_checkbox_is_not_optional(self, filter_control_name, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify whether filter checkbox group control is not optional. If not optional means checkbox control bounded with red solid border around it.
        example usage : verify_filter_checkbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_checkbox_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position)
    
    def verify_filter_checkbox_is_optional(self, filter_control_name, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify whether filter checkbox control is optional. If optional means checkbox control not bounded with red solid border around it.
        example usage : verify_filter_checkbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_checkbox_is_optional(self, filter_control_name, msg, filter_control_position)
    
    def verify_filter_checkbox_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter checkbox options
        example usage : verify_filter_checkbox_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter radio group control')
        """
        pd_design.verify_filter_checkbox_options(self, filter_control_name, expected_options, msg, filter_control_position)
    
    def verify_selected_options_in_filter_checkbox(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter checkbox control.
        example usage : verify_selected_options_in_filter_checkbox('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter radio group control')
        """
        pd_design.verify_selected_options_in_filter_checkbox(self, filter_control_name, expected_selected_options, msg, filter_control_position)
    
    def verify_filter_slider_values(self, filter_control_name, expected_values, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter slider control range values. Range value means slider minimum value, selected value and maximum value. 
        example usage : verify_filter_slider_values('Move Slider to 5011', ['MIN=5000', 'SELECTED=5008', 'MAX=5020'], 'Step 01.1 : Verify slider range values')
        """
        pd_design.verify_filter_slider_values(self, filter_control_name, expected_values, msg, filter_control_position)
    
    def verify_filter_slider_range_line_color(self, filter_control_name, msg , color_name='bar_blue1', filter_control_position=1):
        """
        Descriptions : This method used to verify slider range line color 
        example usage : verify_filter_slider_range_line_color('Move Slider to 5011', 'Step 01.1 : Verify slider range line color is blue')
        """
        pd_design.verify_filter_slider_range_line_color(self, filter_control_name, msg, color_name=color_name, filter_control_position=filter_control_position)
    
    def verify_grid_style_options(self, step_num):
        """
        Descriptions : This method used to verify grid style options
        example usage : verify_grid_style_options("04.1")
        """
        pd_design.verify_style_options(self, "Grid Style", step_num)
        
    def verify_container_style_options(self, step_num):
        """
        Descriptions : This method used to verify container style options
        example usage : verify_container_style_options("04.1")
        """
        pd_design.verify_style_options(self, "Container Style", step_num)
        
    def verify_section_style_options(self, step_num):
        """
        Descriptions : This method used to verify section style options
        example usage : verify_section_style_options("04.1")
        """
        pd_design.verify_style_options(self, "Section Style", step_num)
    
    def verify_container_style_color(self, container_title, color_name, step_num, container_position=1):
        """
        Descriptions : This method will verify the container style color
        :Usage - verify_container_style_color("Panel1", 'blue')
        """
        pd_design.verify_container_style_color(self, container_title, color_name, step_num, container_position)
        
    def verify_filter_grid_style_color(self, expected_color, step_num, grid_container_title=None, model_window=False):
        """
        Descriptions : This method will verify the filter grid style color
        :arg - grid_container_title = 'Panel1'. If you want to verify filter grid style color inside the grid container then pass grid container title. 
        :Usage - verify_filter_grid_style_color("01.02", 'blue')
        """
        pd_design.verify_filter_grid_style_color(self, expected_color, step_num, grid_container_title, model_window=model_window)
    
    def add_filter_controls_dialog(self, parameter=None):
        """
        Description : This method will return object of AddFilterControlsDialog class from common.pages
        Using this method we can perform all actions related to  Add Filter Controls Dialog.
        Note : If you want perform any action by parameter value then you should pass parameter value.
        :Usage1 = add_filter_controls_dialog("MODEL").check()
        :Usage2 = add_filter_controls_dialog("MODEL").uncheck()
        :Usage3 = add_filter_controls_dialog().click_add_filter_controls_button()
        :Usage4 = add_filter_controls_dialog().verify_title()
        """
        return AddFilterControlsDialog(self.driver, parameter)
    
    def select_filter_grid_cell(self, cell_num, grid_container_title=None, model_window=False, click_on_location='top_left', click_type='left'):
        """
        Descriptions : This method used to click on filter grid cell at top left corner
        example usage : select_filter_grid_cell(1, grid_container_title='Panel 2', click_on_location='middle', click_type='right')
        """
        pd_design.select_filter_grid_cell(self, cell_num, grid_container_title, model_window, click_on_location, click_type)
    
    def select_filter_control_panel(self,cell_num,click_on_location='top_left', click_type='left'):
        """
        Descriptions : This method used to click on filter grid cell at top left corner
        example usage : select_filter_grid_cell(1, grid_container_title='Panel 2', click_on_location='middle', click_type='right')
        """
        pd_design.select_filter_grid_panel(self, cell_num, click_on_location, click_type)
    
    def verify_page_domain_tree_node(self, expected_domain_tree_list, msg, tree_node_css=None, assert_type='asin'):
        """
        Descriptions : This method used to verify_page_domain_tree_node
        example usage : verify_page_domain_tree_node(['Domains', 'P292_S19901', 'P398_S10799', 'Public', 'S9100', 'Retail Samples'], msg='Step 01.1 : Verify slider range line color is blue')
        """
        pd_design.verify_page_domain_tree_node(self, expected_domain_tree_list, msg, tree_node_css=tree_node_css, assert_type=assert_type)  
    
    def select_page_section(self, section_num, location='top_left', xoffset=0, yoffset=0):
        """
        Descriptions : Click on page section at top left to select
        example usage : select_page_section(1) 
        """
        pd_design.select_page_section(self, section_num, location, xoffset, yoffset)
    
    def select_container(self, container_title, container_position=1, xoffset=2, yoffset=2):
        """
        Descriptions : This method used to left click on container at top left to select
        example usage : select_container_context_menu('Panel1')
        """
        pd_design.select_container(self, container_title, container_position, xoffset=xoffset, yoffset=yoffset)
        
    def verify_page_section_style_color(self, section_num, color_name, step_num):
        """
        Descriptions : This method used to verify page section style color
        example usage : verify_page_section_style_color(1, 'blue', '04.01') 
        """
        pd_design.verify_page_section_style_color(self, section_num, color_name, step_num)
    
    def select_page_from_bottom_tab(self, page_name):
        """
        Descriptions : This method used to click on tab in bottom page tab.
        example usage : select_page_from_bottom_tab("Page 1")
        """
        pd_design.select_page_from_bottom_tab(self, page_name)
    
    def change_page_heading(self, new_heading):
        """
        Description : Double click on page heading and clear old heading and enter the new page heading and enter the key
        :Usage - change_page_heading("Test Heading")
        """
        pd_design.change_page_heading(self, new_heading)
        
    def close_filter_model_window(self):
        """
        Description : Click on close icon button to close filter model window
        """
        pd_design.close_filter_model_window(self)
    
    def tab_container(self, title, position=1):
        """
        Description : This method will return object of TabContainer class from common.pages
        Using this method we can perform all actions related to Tabcontainer
        :Usage1 = tab_container("Panel 1").click_new_tab_plus_icon()
        :Usage2 = tab_container("Panel 1").click_tab_overflow_icon()
        :Usage3 = tab_container("Panel 1").verify_add_content_button_displayed("01.01)
        """
        return TabContainer(self.driver, title, position)
    
    def accordion_container(self, title, position=1):
        """
        Description : This method will return object of AccordionContainer class from common.pages
        Using this method we can perform all actions related to Accordion Container
        :Usage = accordion_container("Panel 1").verify_area_title(['Area 1], "01.01")
        """
        return AccordionContainer(self.driver, title, position)
    
    def search_content(self, text, enter=False, click_search_icon=False):
        """
        Descriptions : Click on content search textbox and type text to search contents
        :arg1 - enter - Press enter key if enter = True.
        :arg2 - click_search - click on search icon button if click_search = True.
        :Usage - search_content("Category", enter=True)
        """
        pd_design.search_content(self, text, enter=enter, click_search_icon=click_search_icon)
    
    def click_clear_content_search(self):
        """
        Descriptions : Click on content search clear icon button to clear 
        Usage : click_clear_content_search("Category", "01.01")
        """
        pd_design.click_clear_content_search(self)
        
    def verify_content_items_contain_specific_text(self, specific_text, step_num):
        """
        Descriptions : Verify content item contain specific text value.
        Usage : verify_content_items_contain_specific_text("Category", "01.01")
        """
        pd_design.verify_content_items_contain_specific_text(self, specific_text, step_num)
    
    def find_content_item_and_scroll_into_view(self, content_item):
        """
        Descriptions : Find and scroll content item to bring into visible area.
        :Usage : find_content_item_and_scroll_into_view("Category_Sales")
        """
        pd_design.find_content_item_and_scroll_into_view(self, content_item)
    
    def verify_content_item_tooltip(self, content_item, expected_tooltip, step_num):
        """
        Descriptions : Hover mouse of content item and verify tooltip value
        :Usage : verify_content_item_tooltip("Category Sales", expcted_tooltip, "07.01")
        """
        pd_design.verify_content_item_tooltip(self, content_item, expected_tooltip, step_num)
        
    def verify_published_content_items(self, expected_contents, step_num, assert_type="asin"):
        """
        Descriptions : Verify published domain content items
        :Usage : verify_published_content_items(["Category Sales"], "07.01")
        """
        pd_design.verify_published_or_unpublished_content_items(self, "published", expected_contents, step_num, assert_type)
        
    def verify_unpublished_content_items(self, expected_contents, step_num, assert_type="asin"):
        """
        Descriptions : Verify unpublished domain content items
        :Usage : verify_unpublished_content_items(["Category Sales"], "07.01")
        """
        pd_design.verify_published_or_unpublished_content_items(self, "unpublished", expected_contents, step_num, assert_type)
    
    def resource_dialog(self):
        """
        Description : This method will return object of ResourceDialog class
        Using this method we can perform all actions related to resource dialog
        """
        return ResourceDialog(self.driver)
    
    def verify_resource_label_value(self, panel_index, expected_label_value_list, step_num, assert_type="asequal"):
        """
        Descriptions : verify_resource__label_value
        :arg1 - panel_index = '1' or 2 or 3
        :arg2 - label_type = 'resource'
        :arg3 - expected_label_value_list = ['Resource', 'Not set']
        :arg4 - step_num = '01.01'
        :Usage - verify_resource_or_parameters_label_value(1, ['Resource', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Category_Sales.fex'], "01.01")
        """
        pd_design.verify_resource_or_parameters_label_value(self, panel_index=panel_index, label_type="resource", expected_label_value_list=expected_label_value_list, step_num=step_num, assert_type=assert_type)
        
    def verify_parameters_label_value(self, panel_index, expected_label_value_list, step_num, assert_type="asequal"):
        """
        Descriptions : verify_resource__label_value
        :arg1 - panel_index = '1' or 2 or 3
        :arg2 - label_type = 'resource'
        :arg3 - expected_label_value_list = ['Parameters', 'None']
        :arg4 - step_num = '01.01'
        :Usage - verify_resource_or_parameters_label_value(1, ['Parameters', 'None'], "01.02")
        """
        pd_design.verify_resource_or_parameters_label_value(self, panel_index=panel_index, label_type="parameters", expected_label_value_list=expected_label_value_list, step_num=step_num, assert_type=assert_type)
     
    def verify_filter_modal_window_buttons(self, expected_buttons, msg, assert_type="asequal"):
        """
        Description : Verify filter modal window visible buttons text.
        :Usage - verify_filter_modal_window_buttons(["Submit", "Reset"], "Step 01.01 : Verify ["Submit", "Reset"] button are displayed")
        """
        pd_design.verify_filter_modal_window_buttons(self, expected_buttons, msg, assert_type)
    
    def verify_repository_widgets_items_text(self, expected_items_list, msg, assert_type="asequal"):
        """
        Description : Verify Repository Widgets tab items text 
        :Usage : verify_repository_widgets_items_text(["Explorer", "Link tile"], "Step 05.01 : Verify ["Explorer", "Link tile"] items displayed in Repository Widgets tab)
        """
        pd_design.verify_repository_widgets_items_text(self, expected_items_list, msg, assert_type)
    
    def select_link_tile_widget_in_canvas(self, widget_position):
        """
        Description : Left click on link tile widget in canvas to select.
        :usage - select_link_tile_widget_in_canvas(1)
        """
        pd_design.select_link_tile_widget_in_canvas(self, widget_position)
    
    def select_container_in_canvas(self, container_title, container_title_index=1):
        """
        Description : Left click on link tile widget in canvas to select.
        :usage - select_container_in_canvas("Panel 1")
        """
        pd_design.select_container_in_canvas(self, container_title, container_title_index)
    
    def drag_repository_widget_to_canvas_container(self, widget_name, canvas_container_title, canvas_container_position=1):
        """
        Descriptions : This method will drag container to canvas container
        :Usage - drag_container_to_canvas_container("Grid", "Panel1")'
        """
        pd_design.drag_repository_widget_to_canvas_container(self, widget_name, canvas_container_title, canvas_container_position)
    
    def verify_add_content_panel_dialog(self,expected_content_options,msg):
        """
        Descriptions:This method is used to verify the add content dialog.
        Scenario: add content dialog appears while drag drop the content item to existing item it throws add_content_dialog
        Example usage:verify_add_content_panel_dialog(['Replace content','Add content as new tab','Cancel'], msg="Step 4.1")
        """
        pd_design.verify_add_content_dialog(self, expected_content_options, msg)
        
    def select_options_add_content_dialog(self,options_to_select):
        """
        Descriptions:This method is used to select options from the add content dialog.
        Scenario: add content appears while drag drop the content item to existing item it throws add_content_dialog
        Example usage:select_options_add_content_dialog(self,"Add content as new tab")
        """
        pd_design.select_options_add_content_dialog(self, item_to_select=options_to_select)
        
    def select_options_from_add_content_dropdown(self,menu_options):
        """
        Descriptions:This method is used to select options from the add content dialog dilog dropdown values.
        Scenario: add content appears while drag drop the content item to existing item in blank canvas it throws add_content_dialog in this select options from dropdown
        Example usage:select_options_from_add_content_dropdown(self,"Add content as new slide")
        """
        pd_design.select_options_from_add_content_dropdown(self, dropdown_option=menu_options)
    
    def verify_tooltip_carousel_items(self,expected_tooltip,msg):
        """
        Description: This method is uesd to verify the tooltip option is avialable in carousel items
        @param: ['Containers','Content','Controls']
        """
        pd_design.verify_tooltip_of_carousel_item(self, expected_tooltip, msg)
        
    def verify_tooltip_for_container_options(self,container_title,expected_title,msg):
        """
        Description: This method is used to verify the tooltip options for panel
        @param:coantainer_title= "Panel 1","Panel 2"
        Scenario: add container need to verify the the tooltip of panel option eg: maximize and options so on
        """
        pd_design.verify_tooltip_for_container_options(self, container_title,expected_title, msg)
    
    def click_options_verify_message(self,container_title,expected_message,msg):
        """
        Description:This method is used to verify the click options in panel and verify the message
        Usage:-click_options_verify_message("Panel 1","This feature is enable only techinal preview is enable","Step 6.1")
        """
        pd_design.click_options_verify_message(self, container_title, expected_message, msg)
    
    def verify_notification_popup_message(self, expected_msg, step_num):
        """
        Description : Verify any notification popup message
        :Usage : verify_notification_popup_message("Sample notification", "01.02")
        """
        pd_design.verify_notification_popup_message(self, expected_msg, step_num)
    
    def drag_embedded_content_to_canvas_section(self, content, canvas_section_cell, section_num=1):
        """
        Descriptions : This method used to drag Embedded content to page container section
        :Usage - drag_embedded_content_to_canvas_section('Chart 1', 1)
        """
        pd_design.drag_embedded_content_to_canvas_section(self, content, canvas_section_cell, section_num)
        
"======================================================================== PREVIEW METHODS ========================================================================"

class Preview(BasePage):
    
    def __init__(self, driver):
        super(Preview, self).__init__(driver)
    
    def wait_for_number_of_element(self, element_css, expected_number=None, time_out=30, pause_time=1):
        """
        :usage wait_for_number_of_element(total_no_of_riser_css, 28, wait_time_in_sec)
        """
        utils.synchronize_with_number_of_element(self, element_css, expected_number, time_out, pause_time)
    
    def wait_for_visible_text(self, element_css, visble_element_text=None, time_out=30,  pause_time=1):
        """
        :usage wait_for_visible_text(x_title_element_css, 'Product Category', wait_time_in_sec)
        """
        utils.synchronize_with_visble_text(self, element_css, visble_element_text, time_out,  pause_time)
        
    def switch_to_container_frame(self, container_title, container_position=1, timeout=30, wait_time=1, frame_index=1):
        """
        Descriptions : This method used to switch to iframe in specific pd container   
        """
        pd_design.switch_to_container_frame(self, container_title, container_position, timeout, wait_time, frame_index)
        
    def switch_to_default_page(self):
        """
        Descriptions : This method used to switch to default page from container iframe  
        """
        core_utils.switch_to_default_content(self)
        
    def switch_to_previous_window(self, driver_close=True):
        """
        Descriptions : This function will switch the control back to previous window by closing the current window.
        :arg - driver_close= If already target window closed then pass driver_close=False
        """
        pd_miscelaneous.switch_to_previous_window(self, driver_close)
        
    def enter_input_value_for_filter_control(self, control_name, input_value_to_enter, control_position=1):
        """
        Descriptions : This method used to enter value to filter control
        example usage : enter_input_value_for_filter_control('Business Region:', 'Car')
        """
        pd_preview.enter_input_value_for_filter_control(self, control_name, input_value_to_enter, control_position)
    
    def go_back_to_design_from_preview(self, wait_time=3):
        """
        Descriptions : This method used to back to design page from preview window 
        example usage : go_back_to_design_from_preview()
        """
        pd_preview.go_back_to_design_from_preview(self, wait_time)
    
    def verify_filter_control_labels(self, expected_label_list, msg, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to filter panel heading labels
        example usage : verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], 'Step 01.1 : Verify filter panel heading labels)
        :arg - grid_container_title = 'Panel1'. If you want to verify filter labels inside grid container then pass grid container title. 
        """
        pd_design.verify_filter_control_labels(self, expected_label_list, msg, grid_container_title=grid_container_title, model_window=model_window)
        
    def verify_number_of_page_sections(self, expected_total_sections, msg):
        """
        Descriptions : This method used to verify total number of page sections displaying in canvas
        example usage : verify_number_of_page_sections(5, 'Step 01.1 : Verify 5 page sections are displaying in page canvas') 
        """
        pd_design.verify_number_of_page_sections(self, expected_total_sections, msg)
    
    def verify_number_of_panels(self, expected_total_panels, msg):
        """
        Descriptions : This method used to verify total number of panels displaying on canvas
        example usage : verify_number_of_panels(5, 'Step 01.1 : Verify 5 panels are displaying in page canvas') 
        """
        pd_design.verify_number_of_panels(self, expected_total_panels, msg)
    
    def verify_containers_title(self, expected_title_list, msg):
        """
        Descriptions : This method used to verify pd container titles
        example usage: verify_containers_title(["Panel 1", "Panel 2", "Panel 3", "Category Sales"], 'Step 01.1 : Verify container titles') 
        """
        pd_design.verify_containers_title(self, expected_title_list, msg)
    
    def verify_container_title_bar_visible_buttons(self, container_title, expected_buttons, msg, container_position=1):
        """
        Descriptions : This method used to verify visible container title bar button such as 'Maximize', 'Options' and 'Restore'
        example usage : verify_container_title_bar_button_options('Panel 6', ['Maximize', 'Options'], 'Step 01.1 : Verify ['Maximize', 'Options'] buttons display on container tool bar')
        """
        pd_design.verify_container_title_bar_visible_buttons(self, container_title, expected_buttons, msg, container_position)
    
    def verify_filter_inputbox_is_not_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is not optional. If not optional means drop down control bounded with red solid border around it.
        example usage : verify_filter_inputbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region control input box is selected')
        """
        pd_design.verify_filter_inputbox_is_not_optional(self, filter_control_name, msg,  border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_inputbox_is_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If optional means drop down control not bounded with red solid border around it.
        example usage : verify_filter_inputbox_is_optional('Business Region:', 'Step 01.1 : Verify Business Region control input box is not selected')
        """
        pd_design.verify_filter_inputbox_is_optional(self, filter_control_name, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_control_panel_is_not_selected(self, filter_control_name, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify whether specific filter control panel is not selected
        verify_filter_control_panel_is_not_selected('Business Region:', 'Step 01.1 : Verify Business Region filter control is not selected')
        """
        pd_design.verify_filter_control_panel_is_not_selected(self, filter_control_name, msg, filter_control_position)
        
    def verify_page_heading_title(self, expected_title_list, msg):
        """
        Descriptions : This method used to verify page header title. expected title should be pass as list
        example usage : verify_page_heading_title(['Page Heading'], 'Step 01.1 : Verify page title')
        """
        pd_design.verify_page_heading_title(self, expected_title_list, msg)
    
    def verify_page_header_visible_buttons(self, expected_visible_buttons, msg):
        """
        Descriptions : This method used to verify page header visible buttons such as 'Refresh', 'Filter'
        example usage : verify_page_header_visible_buttons('['Refresh', 'Filter'], 'Step 01.1 : Verify Refresh and Filter button are display on page header')
        """
        pd_design.verify_page_header_visible_buttons(self, expected_visible_buttons, msg)
    
    def verify_default_output_for_input_required_container(self, container_title, msg, expected_output='A required parameter is missing', container_position=1) :
        """
        Descriptions : This method used to verify default output for input required fex contains container text
        example usage : verify_default_output_for_input_required_container('01 - Simple Input Required', 'Step 01.1 : Verify report added to the page successfully.')
        """
        pd_design.verify_default_output_for_input_required_container(self, container_title, msg, expected_output, container_position)
        
    def verify_preview_is_displayed(self, msg):
        """
        Descriptions : This method used to verify whether preview page is displayed or not after click on preview button
        example usage : verify_preview_is_displayed('Step 01.1 : Verify page preview window display')
        """
        pd_preview.verify_preview_is_displayed(self, msg)
    
    def create_html_report_data_set(self, file_name_to_save, table_css="table[summary]"):
        """
        Descriptions : This method used to verify parameter tab properties in setting tab
        example usage : create_html_report_data_set('C2345_DataSet_01')
        """
        pd_miscelaneous.create_report_data_set_using_bs4(self, file_name_to_save, table_css)
        
    def verify_html_report_data_set(self, saved_file_name, msg, table_css="table[summary]"):
        """
        Descriptions : This method used to verify parameter tab properties in setting tab
        example usage : verify_html_report_data_set('C2345_DataSet_01', 'Step 01.1 : Verify report data')
        """
        pd_miscelaneous.verify_report_table_data_using_bs4(self, saved_file_name, msg, table_css)
    
    def verify_filter_inputbox_value(self, filter_control_name, expected_value_list, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter input box values
        example usage : verify_filter_inputbox_value('Business Region:', ['EMP'], 'Step 01.1 : Verify Business Region condition inbutbox is selected')
        """
        pd_design.verify_filter_inputbox_value(self, filter_control_name, expected_value_list, msg, filter_control_position)
    
    def verify_blank_container_output(self, container_title, msg, container_position=1):
        """
        Descriptions : This method used to verify blank containers output which means blank container should be blank
        example usage : verify_blank_container_output('Panel 2', 'Step 01.1 : Verify Panel 1 is blank')
        """
        pd_design.verify_blank_container_output(self, container_title, msg, container_position)
    
    def scroll_down_html_report(self, number_of_scroll=None):
        """
        Descriptions : This method used get to scroll down on scrollable element
        :arg - number_of_scroll = we can pass number to how many times to scroll down. 
        It will keep on scroll down until scroll bar reach bottom of the given scrollable_element if number_of_scroll==None
        """
        report_scrollable_obj = self.driver.find_element_by_css_selector("html")
        utils.scroll_down_on_element(self, report_scrollable_obj, number_of_scroll)
    
    def verify_html_report_has_vertical_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container html report has vertical scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because html report placed inside the container iframe
        """
        pd_design.verify_report_has_vertical_scrollbar(self, "html", msg)
        
    def verify_html_report_has_horizontal_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container html report has horizontal scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        pd_design.verify_report_has_horizontal_scrollbar(self, "html", msg)
    
    def verify_html_report_does_not_have_vertical_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container report does not have vertical scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because html report placed inside the container iframe
        """
        pd_design.verify_report_does_not_have_vertical_scrollbar(self, "html", msg)
    
    def verify_html_report_does_not_have_horizontal_scrollbar(self, msg):
        """
        Descriptions : This method used to verify whether specific container report does not have horizontal scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        pd_design.verify_report_does_not_have_horizontal_scrollbar(self, "html", msg)
    
    def verify_html_report_vertical_scrollbar_reached_bottom(self, msg):
        """
        Descriptions : This method used to verify whether specific container report vertical scroll bar reached bottom
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        pd_design.verify_report_vertical_scrollbar_reached_bottom(self, "html", msg)
    
    def verify_filter_dropdown_is_not_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is not optional. If not optional means drop down control bounded with red solid border around it.
        example usage : verify_filter_dropdown_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter drop down control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_dropdown_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_dropdown_is_optional(self, filter_control_name, msg,  filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If optional means drop down control not bounded with red solid border around it.
        example usage : verify_filter_dropdown_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter drop down control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_dropdown_is_optional(self, filter_control_name, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        
    def verify_filter_buttonset_is_not_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If not optional means button set control bounded with red solid border around it.
        example usage : verify_filter_buttonset_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter button set control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_buttonset_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position)
    
    def verify_filter_buttonset_is_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If optional means button set control not bounded with red solid border around it.
        example usage : verify_filter_buttonset_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter button set control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_buttonset_is_optional(self, filter_control_name, msg, filter_control_position)
    
    def verify_selected_value_of_filter_dropdown(self, filter_control_name, expected_value_list, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify filter drop down selected value or default value
        example usage : verify_selected_value_of_filter_dropdown('Business Region:', ['EMP'], 'Step 01.1 : Verify Business Region drop down selected EMP value')
        """
        pd_design.verify_selected_value_of_filter_dropdown(self, filter_control_name, expected_value_list, msg, filter_control_position=filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        
    def verify_filter_dropdown_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter drop down options
        example usage : verify_filter_dropdown_options('Select North America', ['South America', 'EMEA'], 'Step 01.1 : Verify ['South America', 'EMEA'] options are display in filter drop down')
        """
        pd_preview.verify_filter_dropdown_options(self, filter_control_name, expected_options, msg, filter_control_position)
    
    def verify_selected_filter_dropdown_options(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected filter drop down options
        example usage : verify_selected_filter_dropdown_options('Select North America', ['South America', 'EMEA'], 'Step 01.1 : Verify ['South America', 'EMEA'] options are selected in filter drop down control')
        """
        pd_preview.verify_filter_dropdown_options(self, filter_control_name, expected_selected_options, msg, filter_control_position, verify_selected_options=True)
        
    def select_filter_dropdown_option(self, filter_control_name, option_list_to_select, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to select single drop down option
        example usage : select_filter_dropdown_option('Select North America', 'EMEA')
        """
        pd_preview.select_filter_dropdown_option(self, filter_control_name, option_list_to_select, filter_control_position, grid_container_title, model_window)
    
    def select_multiple_options_from_filter_dropdown(self, filter_control_name, option_list_to_select, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to select multiple options from drop down control
        example usage : select_multiple_options_from_filter_dropdown('Select North America', ['South America', 'EMEA'])
        """
        pd_preview.select_multiple_options_from_filter_dropdown(self, filter_control_name, option_list_to_select, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def select_multiple_options_from_filter_dropdown_using_ctrl(self, filter_control_name, option_list_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select multiple options from drop down control by pressing ctrl
        example usage : select_multiple_options_from_filter_dropdown('Select North America', ['South America', 'EMEA'])
        """    
        pd_preview.select_multiple_options_from_filter_dropdown_using_ctrl(self, filter_control_name, option_list_to_select, filter_control_position)
    
    def select_multiple_options_in_filter_buttonset(self, filter_control_name, options_list_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select multiple options in button set control.
        example usage : select_multiple_options_in_filter_buttonset('Select North America', ['EMEA', 'South America'])
        """
        pd_preview.select_filter_buttonset_options(self, filter_control_name, options_list_to_select, filter_control_position)
    
    def select_multiple_options_in_filter_buttonset_using_ctrl(self, filter_control_name, options_list_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select multiple options in button set control using ctrl
        example usage : select_multiple_options_in_filter_buttonset_using_ctrl('Select North America', ['EMEA', 'South America'])
        """
        pd_preview.select_filter_buttonset_options(self, filter_control_name, options_list_to_select, filter_control_position, use_ctrl=True)

    def select_filter_buttonset_option(self, filter_control_name, options_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select button set options
        example usage : select_filter_buttonset_option('Select North America', 'EMEA')
        """
        pd_preview.select_filter_buttonset_options(self, filter_control_name, [options_to_select], filter_control_position)
    
    def verify_filter_buttonset_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter buttonset options
        example usage : verify_filter_buttonset_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter button set control')
        """
        pd_design.verify_filter_buttonset_options(self, filter_control_name, expected_options, msg, filter_control_position)
        
    def verify_selected_options_in_filter_buttonset(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter button set control.It will verify selected options based on backgroud color of option
        example usage : verify_filter_buttonset_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter button set control')
        """
        pd_design.verify_selected_options_in_filter_buttonset(self, filter_control_name, expected_selected_options, msg, filter_control_position)
    
    def verify_filter_radio_group_is_not_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter radio button group control is not optional. If not optional means button set control bounded with red solid border around it.
        example usage : verify_filter_radio_group_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_radio_group_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position)
    
    def verify_filter_radio_group_is_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If optional means button set control not bounded with red solid border around it.
        example usage : verify_filter_radio_group_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_radio_group_is_optional(self, filter_control_name, msg, filter_control_position)
    
    def verify_filter_radio_group_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter radio group options
        example usage : verify_filter_radio_group_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter radio group control')
        """
        pd_design.verify_filter_radio_group_options(self, filter_control_name, expected_options, msg, filter_control_position)
    
    def verify_selected_options_in_filter_radio_group(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter radio group control.
        example usage : verify_selected_options_in_filter_radio_group('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter radio group control')
        """
        pd_design.verify_selected_options_in_filter_radio_group(self, filter_control_name, expected_selected_options, msg, filter_control_position)
        
    def select_filter_radio_group_option(self, filter_control_name, option_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select filter radio group option
        example usage : select_filter_radio_group_option('Select North America', 'EMEA')
        """
        pd_preview.select_filter_radio_group_options(self, filter_control_name, [option_to_select], filter_control_position)
    
    def verify_filter_date_picker_is_not_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter date picker control is not optional. If not optional means date picker control bounded with red solid border around it.
        example usage : verify_filter_date_picker_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter date picker control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_date_picker_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position)
    
    def verify_filter_date_picker_is_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter date picker is optional. If optional means date picker control not bounded with red solid border around it.
        example usage : verify_filter_date_picker_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter date picker control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_date_picker_is_optional(self, filter_control_name, msg, filter_control_position)
    
    def verify_selected_date_in_filter_date_picker(self, filter_control_name, expected_selected_date, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify selected date value in filter data picker control
        example usage : verify_selected_date_in_filter_date_picker('Select 2016/03/17', ['Jun 19, 2018'], 'Step 01.1 : Verify Jun 19, 2018 date selected in data picker control')
        """
        pd_design.verify_selected_date_in_filter_date_picker(self, filter_control_name, expected_selected_date, msg, filter_control_position)
    
    def select_date_from_single_date_picker(self, filter_control_name, month=None, year=None, day=None, filter_control_position=1):
        """
        Descriptions : This method used select month, year and day from single date picker.
        example usage : select_date_from_single_date_picker('Select 2016/03/17', month='Apr', year='1991', day='9')
        """
        pd_preview.select_date_from_single_date_picker(self, filter_control_name, month=month, year=year, day=day, filter_control_position=filter_control_position)
    
    def verify_filter_checkbox_is_not_optional(self, filter_control_name, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify whether filter checkbox group control is not optional. If not optional means checkbox control bounded with red solid border around it.
        example usage : verify_filter_checkbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_checkbox_is_not_optional(self, filter_control_name, msg, border_width='1px', border_rgb_value='rgb(240, 80, 80)', border_style='solid', position='absolute', filter_control_position=filter_control_position)
    
    def verify_filter_checkbox_is_optional(self, filter_control_name, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify whether filter checkbox control is optional. If optional means checkbox control not bounded with red solid border around it.
        example usage : verify_filter_checkbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        pd_design.verify_filter_checkbox_is_optional(self, filter_control_name, msg, filter_control_position)
    
    def verify_filter_checkbox_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter checkbox options
        example usage : verify_filter_checkbox_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter radio group control')
        """
        pd_design.verify_filter_checkbox_options(self, filter_control_name, expected_options, msg, filter_control_position)
    
    def verify_selected_options_in_filter_checkbox(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter checkbox control.
        example usage : verify_selected_options_in_filter_checkbox('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter radio group control')
        """
        pd_design.verify_selected_options_in_filter_checkbox(self, filter_control_name, expected_selected_options, msg, filter_control_position)
        
    def select_filter_checkbox_options(self, filter_control_name, options_list_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select checkbox options.
        example usage : select_filter_checkbox_options('Select North America', ['EMEA'])
        """
        pd_preview.select_filter_checkbox_options(self, filter_control_name, options_list_to_select, filter_control_position)
    
    def verify_filter_slider_values(self, filter_control_name, expected_values, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter slider control range values. Range value means slider minimum value, selected value and maximum value. 
        example usage : verify_filter_slider_values('Move Slider to 5011', ['MIN=5000', 'SELECTED=5008', 'MAX=5020'], 'Step 01.1 : Verify slider range values')
        """
        pd_design.verify_filter_slider_values(self, filter_control_name, expected_values, msg, filter_control_position)
        
    def move_filter_slider(self, filter_control_name, slider_value_to_select, filter_control_position=1):
        """
        Descriptions : This method used to move slider to specific value by drag and drop slider marker. 
        example usage : move_filter_slider('Move Slider to 5011', 5020)
        """
        pd_preview.move_filter_slider(self, filter_control_name, slider_value_to_select, 1, filter_control_position)
    
    def move_filter_slider_range(self,  filter_control_name, range_value1=None, range_value2=None, filter_control_position=1):
        """
        Descriptions : This method used to move sliders to specific value by drag and drop slider markers. 
        example usage : move_filter_slider_range('Move Slider to 5011', slider_value1=5010, slider_value2=5015)
        """
        pd_preview.move_filter_slider_range(self, filter_control_name, range_value1=range_value1, range_value2=range_value2, filter_control_position=filter_control_position)
    
    def verify_filter_slider_range_line_color(self, filter_control_name, msg , color_name='bar_blue1', filter_control_position=1):
        """
        Descriptions : This method used to verify slider range line color 
        example usage : verify_filter_slider_range_line_color('Move Slider to 5011', 'Step 01.1 : Verify slider range line color is blue')
        """
        pd_design.verify_filter_slider_range_line_color(self, filter_control_name, msg, color_name=color_name, filter_control_position=filter_control_position)
    
    def select_date_from_date_range_picker(self, filter_control_name, start_date, end_date, filter_control_position=1):
        """
        Descriptions : This method used select starting and ending state from date range picker control.
        example usage : select_date_from_date_range_picker('Select 2016/03/10 and 2016/03/17', 'Mar-10-2016', 'Mar-17-2016')
        Note : start_date and end_date format should be like this 'Mar-10-2016'
        """
        pd_preview.select_date_from_date_range_picker(self, filter_control_name, start_date, end_date, filter_control_position)
    
    def clear_filter_date_value(self, filter_control_name, filter_control_position=1):
        """
        Descriptions : This method used to click on clear icon to clear  filer date value.
        example usage : select_date_from_single_date_picker('Select 2016/03/17')
        """
        pd_preview.clear_filter_date_value(self, filter_control_name, filter_control_position)
    
    def verify_container_style_color(self, container_title, color_name, step_num, container_position=1):
        """
        Descriptions : This method will verify the container style color
        :Usage - verify_container_style_color("Panel1", 'blue')
        """
        pd_design.verify_container_style_color(self, container_title, color_name, step_num, container_position)
    
    def click_show_filters(self):
        """
        Descriptions : This method used to click on show filters option
        """
        pd_design.click_show_filters(self)
    
    def close_selections_filter_dialog(self):
        """
        Descriptions : This method used to click on close button in selections_filter_dialog
        """
        pd_design.close_selections_filter_dialog(self)
    
    def verify_filter_grid_style_color(self, expected_color, step_num, grid_container_title=None, model_window=False):
        """
        Descriptions : This method will verify the filter grid style color
        :arg - grid_container_title = 'Panel1'. If you want to verify filter grid style color inside the grid container then pass grid container title. 
        :Usage - verify_filter_grid_style_color("01.02", 'blue')
        """
        pd_design.verify_filter_grid_style_color(self, expected_color, step_num, grid_container_title, model_window=model_window)
    
    def verify_page_domain_tree_node(self, expected_domain_tree_list, msg, tree_node_css=None, assert_type='asin'):
        """
        Descriptions : This method used to verify_page_domain_tree_node
        example usage : verify_page_domain_tree_node(['Domains', 'P292_S19901', 'P398_S10799', 'Public', 'S9100', 'Retail Samples'], msg='Step 01.1 : Verify slider range line color is blue')
        """
        pd_design.verify_page_domain_tree_node(self, expected_domain_tree_list, msg, tree_node_css=tree_node_css, assert_type=assert_type) 
    
    def verify_page_section_style_color(self, section_num, color_name, step_num):
        """
        Descriptions : This method used to verify page section style color
        example usage : verify_page_section_style_color(1, 'blue', '04.01') 
        """
        pd_design.verify_page_section_style_color(self, section_num, color_name, step_num)
    
    def close_filter_model_window(self):
        """
        Description : Click on close icon button to close filter model window
        """
        pd_design.close_filter_model_window(self)
    
    def tab_container(self, title, position=1):
        """
        Description : This method will return object of TabContainer class from common.pages
        Using this method we can perform all actions related to Tabcontainer
        :Usage1 = tab_container("Panel 1").click_new_tab_plus_icon()
        :Usage2 = tab_container("Panel 1").click_tab_overflow_icon()
        :Usage3 = tab_container("Panel 1").verify_add_content_button_displayed("01.01)
        """
        return TabContainer(self.driver, title, position)
        
    def select_container_option(self, container_title, option, container_position=1):
        """
        Descriptions : click on container options icon and select option
        example usage : select_container_option("Panel 1", "Refresh")
        """
        pd_design.select_container_option(self, container_title, option, container_position)
        
"======================================================================== RUN METHODS ========================================================================"

class Run(Preview):
    
    def __init__(self, driver):
        super(Run, self).__init__(driver)
    
    def swtich_to_homepage_runwindow_frame(self, wait_time=40):
        """
        Descriptions : This method used to switch home page run window frame.
        """
        frame_css="div[class^='output-area-frame']>iframe[class='ibx-iframe-frame']"
        utils.synchronize_until_element_is_visible(self, frame_css, 60)
        core_utils.switch_to_frame(self, frame_css, wait_time)
    
    def close_homepage_run_window(self):
        """
        Descriptions : This method used to close run window dialog box in main home page
        """
        Run.switch_to_default_page(self)
        close_obj=self.driver.find_element_by_css_selector("div[class^='output-area-close-button'")
        core_utils.left_click(self, close_obj)
    
    def verify_default_output_for_input_required_container(self, container_title, msg, expected_output='', container_position=1) :
        """
        Descriptions : This method used to verify default output for input required fex contains container text
        example usage : verify_default_output_for_input_required_container('01 - Simple Input Required', 'Step 01.1 : Verify report added to the page successfully.')
        """
        pd_design.verify_default_output_for_input_required_container(self, container_title, msg, expected_output, container_position)
    
    def run_page_using_api(self, page_name, mrid=None, mrpass=None, folder=None, login=True) :
        """
        Description : Run the saved page using API url
        :Usage - run_page_using_api("C1234567")
        """
        pd_miscelaneous.run_page_using_api(self, page_name, mrid, mrpass, folder, login)