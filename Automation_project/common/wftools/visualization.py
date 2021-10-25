from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.core_utility import CoreUtillityMethods as coreutillobject
from common.pages.visualization_properties import Visualization_Properties as propertyobject
from common.pages.visualization_metadata import Visualization_Metadata as metadataobject
from common.pages.visualization_resultarea import Visualization_Resultarea as resultobject
from common.pages.visualization_ribbon import Visualization_Ribbon as ribbonobject
from common.pages.visualization_run import Visualization_Run as runobject
from common.pages.visualization_miscelaneous import Visualization_Miscelaneous as miscelaneousobject
from common.pages.ia_miscelaneous import IA_Miscelaneous as iamiscelaneousobject
from selenium.common.exceptions import NoSuchElementException
from common.pages.wf_map import Wf_Map as mapobject
from common.pages.define_compute import Define_Compute as definecomputeobject

class Visualization(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Visualization, self).__init__(driver)

    
    """*** This is for Common Section. *** """
    def wait_for_number_of_element(self, element_css, expected_number=None, time_out=60):
        """
        :usage wait_for_number_of_element(total_no_of_riser_css, 28, wait_time_in_sec)
        """
        miscelaneousobject.wait_for_object(self, element_css, 'number', expected_number=expected_number, time_out=time_out)
    
    def wait_for_visible_text(self, element_css, visble_element_text=None, time_out=60):
        """
        :usage wait_for_visible_text(x_title_element_css, 'Product Category', wait_time_in_sec)
        """
        miscelaneousobject.wait_for_object(self, element_css, 'text', visble_element_text=visble_element_text, time_out=time_out)
    
    def take_preview_snapshot(self, file_name, step_num):
        '''
        Desc:- This function will take screenshot only for preview area
        :param file_name:- 'C123435'
        :param step_num:- '05'
        :usage take_preview_snapshot('C123435' ,'05')
        '''
        element=self.driver.find_element_by_id('resultArea')
        file_name=file_name + '_Actual_Step_' + str(step_num)
        utillobject.take_snapshot(self, element, file_name)
        
    def take_run_window_snapshot(self, file_name, step_num):
        '''
        Desc:- This function will take screenshot only for run window
        :param file_name:- 'C123435'
        :param step_num:- '05'
        :usage take_preview_snapshot('C123435' ,'05')
        '''
        file_name=file_name + '_Actual_Step_' + str(step_num)
        utillobject.take_browser_snapshot(self,file_name)
        
    def invoke_visualization_using_api(self, master, mrid=None, mrpass=None):
        '''
        Desc:- This function will invoke visualization using api call
        :param master:- 'new_retail/wf_retail_lite'
        :param mrid
        :param mrpass
        :usage invoke_visualization_using_api('new_retail/wf_retail_lite')
        '''
        miscelaneousobject.invoke_visualization_tool_using_api(self, tool='idis', master=master, mrid=mrid, mrpass=mrpass)
        default_riser_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        miscelaneousobject.wait_for_object(self, default_riser_css, option='number', expected_number=12)
        
    def edit_visualization_using_api(self, fex, mrid=None, mrpass=None):
        '''
        Desc:- This function will invoke saved visualization file in edit mode using api call
        :param fex:- 'C2346054'
        :param mrid
        :param mrpass
        :usage edit_visualization_using_api('C2346054')
        '''
        miscelaneousobject.invoke_visualization_tool_in_edit_mode_using_api(self, fex, 'idis', mrid=mrid, mrpass=mrpass)
    
    def edit_fex_using_api_url(self, folder_name, tool='idis', fex_name=None, mrid=None, mrpass=None):
        '''
        Desc:- This function will edit retail samples report using api link and sign in as user defined in config file
        Usage: report_obj.edit_retailsamples_using_api(subfolder_name='Auto_Link',fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass')
        '''
        iamiscelaneousobject.edit_fex_using_api(self, folder_name, tool=tool, fex_name=fex_name, mrid=mrid, mrpass=mrpass)
        
    def run_visualization_using_api(self, fex, mrid=None, mrpass=None, run_visual_css="#MAINTABLE_wbody1", no_of_element=1,wait_time=10):
        '''
        Desc:- This function is used to run the fex in visualization tool using api call
        '''
        miscelaneousobject.invoke_visualization_tool_in_run_mode_using_api(self, fex, mrid=mrid, mrpass=mrpass)
        Visualization.wait_for_number_of_element(self, run_visual_css, no_of_element, wait_time)
    
    def logout_visualization_using_api(self):
        '''
        Desc:- This function is used to logout from visualization tool using api call
        '''
        miscelaneousobject.logout_visualization_using_api(self)
            
    def switch_to_new_window(self):
        '''
        Desc:- This function is used to switch to a new window.
        Eg: It will switch from Infoassist edit to run window
        '''
        coreutillobject.switch_to_new_window(self)
    
    def switch_to_previous_window(self):
        '''
        Desc:- This function is used to switch to a previous window.
        Eg: It will switch from run to Infoassist edit window
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
        
    def verify_element_visiblty(self, element=None, element_css=None, visible=True, msg='Step X'):
        '''
        Desc:- This function is to verify whether the element is visible.
        '''
        custom_msg=msg+': Verify whether the object is visible.'
        utillobject.verify_element_visiblty(self, element=element, element_css=element_css, visible=visible, msg=custom_msg)
    
    def verify_element_disable(self, element=None, element_css=None, expected_element_status=True, msg='Step X', attribute_='class'):
        '''
        Desc:- This function is to verify whether the element is disabled.
        '''
        custom_msg=msg+': Verify whether the object is visible.'
        if element is not None:
            elem=element
        elif element_css is not None:
            try:
                elem = self.driver.find_element_by_css_selector(element_css)
            except NoSuchElementException:
                raise ValueError("NoSuchElementException of '"+str(element_css)+"' css value.")
        status = utillobject.verify_element_disable(self, element=elem, attribute_=attribute_)
        utillobject.asequal(self, expected_element_status, status, custom_msg)
    
    def verify_popup_or_dialog_caption_text(self, caption_css, text_to_verify, msg='Step X'):    
        '''
        Desc:- This function is to verify the text written inside the caption.
        ''' 
        custom_msg=msg+': Verify text written inside the caption.'
        utillobject.verify_dialogs_and_popups_caption(self, caption_css, text_to_verify, msg=custom_msg)       
        
    def verify_dialogs_and_popups_text(self, text_css, text_to_verify, msg='Step X'):
        '''
        Desc:- This function is to verify the text written inside the popup.
        '''        
        custom_msg=msg+': Verify text written inside the popup.'
        utillobject.verify_dialogs_and_popups_text(self, text_css, text_to_verify, msg=custom_msg)
            
    def verify_dialogs_and_popups_text_in_element(self, popup_element, text_to_verify, msg='Step X'):
        '''
        Desc:- This function is to verify the text written inside any element within the popup.
        '''        
        custom_msg=msg+': Verify text written inside the provided element within the popup.'
        utillobject.verify_dialogs_and_popups_text_in_element(self, popup_element, text_to_verify, msg=custom_msg)
    
    def click_any_bibutton_in_dialog(self, dialog_css="[id^='BiDialog'][style*='inherit']", btn_name='OK'):
        '''
        Desc:- This function is to select any button in dialog
        ''' 
        utillobject.click_any_bibutton_in_dialog(self, dialog_css, btn_name)
    
    def find_my_coordinate(self, element, element_location='middle', xoffset=0, yoffset=0):
        '''
        Desc:- This function will return your desired location of the element.
        '''
        location_dict=coreutillobject.get_web_element_coordinate(self, element, element_location=element_location, xoffset=xoffset, yoffset=yoffset)
        return(location_dict)
    """**************************************************** This is for RIBBON Section. ************************************** """   
    def run_visualization_from_toptoolbar(self):
        '''
        Desc: This is used to run visualization from the top toolbar.
        '''
        ribbonobject.select_visualization_top_toolbar_item(self, 'run')
    
    def save_as_visualization_from_menubar(self, file_name, file_type=None, folder_location_to_save=None):
        '''
        Desc: This is used to save visualization from menubar.
        :usage save_as_visualization_from_menubar('C2346054')
        '''
        ribbonobject.select_visualization_application_menu_item(self, 'save_as')
        miscelaneousobject.ibfs_save_as_visualization(self, file_name, file_type=file_type, folder_location_to_save=folder_location_to_save)
        
    def save_visualization_from_top_toolbar(self, file_name, file_type=None, folder_location_to_save=None):
        '''
        Desc: This is used to save visualization from toolbar.
        :usage save_visualization_from_top_toolbar('C2346054')
        '''
        ribbonobject.select_visualization_top_toolbar_item(self, 'save')
        miscelaneousobject.ibfs_save_visualization(self, file_name, file_type=file_type, folder_location_to_save=folder_location_to_save)
        
    def save_as_from_application_menu_item(self, file_name, target_table_path='SmokeTest->My Content', application_menu_item_name='save_as', file_type=None):
        """
        Desc: This function will Click IA application button and click save as under SmokeTest MyContent folder
        """
        ribbonobject.select_visualization_application_menu_item(self, application_menu_item_name)
        utillobject.expand_domain_folders_in_open_dialog(self, target_table_path=target_table_path)
        utillobject.ibfs_save_as(self, file_name, file_type=file_type)
    
    def select_item_in_top_toolbar(self, top_toolbar_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        '''
        ribbonobject.select_visualization_top_toolbar_item(self, top_toolbar_item_name)
        
    def change_chart_type(self, chart_name):
        '''
        Desc: This is used to select chart type.
        '''
        ribbonobject.select_visualization_ribbon_item(self, 'Home', 'change')
        ribbonobject.select_visualization_chart_type(self, chart_name)
    
    def select_ribbon_item(self, tab_name, ribbon_button_name_path):
        '''
        Desc: This is used to select ribbon item
        :usage visualobj.select_visualization_ribbon_item('Home', 'insert->Grid')
        '''
        ribbonobject.select_visualization_ribbon_item(self, tab_name, ribbon_button_name_path)
        
    def verify_fexcode_syntax(self, expected_syntax_list, msg):
        """
        Desc : This function used to verify given syntax list available in fecode
        """
        ribbonobject.verify_fexcode_syntax(self, expected_syntax_list, msg)   
         
    """ *** This is for METADATA Section. *** """
    
    def double_click_on_datetree_item(self, field_name, field_position):
        '''
        Desc:- This function is used to double click and select the field from data tree.
        :usage double_click_on_datetree_item('Revenue', 1)
        '''
        metadataobject.select_datatree_field(self, field_name, 'double', field_position)
    
    def right_click_on_datetree_item(self, field_name, field_position, context_menu_path):
        '''
        Desc:- This function is used to right click on the field in data tree and select the item from the context menu.
        :usage right_click_on_datetree_item("Product,Category",1,'Add To Query->Horizontal Axis')
        '''
        metadataobject.select_datatree_field(self, field_name, 'right', field_position, context_menu_path)
    
    def drag_field_from_data_tree_to_query_pane(self, field_name, field_position, bucket_name, bucket_position=1):
        '''
        Desc:- This function is used to drag and drop data field to the specified bucket in query tree.
        :param - field_position: 1,2 .. (first match is 1)
        :param - bucket_position: 1,2 .. (first match is 1)
        :usage drag_field_from_data_tree_to_query_pane("PRICE_DOLLARS_BIN_1",1,"Model",1)
        '''
        metadataobject.drag_and_drop_from_data_tree_to_query_tree(self, field_name, field_position, bucket_name,bucket_position)
    
    def drag_field_within_query_pane(self, source_item_name, target_item_name):
        '''
        Desc:- This function is used to drag and drop data field within query tree.
        :usage drag_field_within_query_pane('Discount','Color')
        '''
        metadataobject.drag_and_drop_within_query_tree(self, source_item_name, target_item_name)  
    
    def drag_and_drop_from_data_tree_to_filter(self, field_name, field_position):
        '''
        Desc:- This function is used to drag from data tree and drop in filter.
        :usage drag_and_drop_from_data_tree_to_filter('Discount','Color')
        '''
        metadataobject.drag_and_drop_from_data_tree_to_filter(self, field_name, field_position)
    
    def verify_datatree_field_context_menu(self, field_name, field_position, context_menu_list, msg):
        '''
        Desc:- This function is used to verify the right click context menu of a data tree field item
        '''
        metadataobject.verify_datatree_context_menu(self, field_name, field_position, context_menu_list, msg) 
    
    def verify_query_field_context_menu(self, field_name, field_position, context_menu_list, msg):
        '''
        Desc:- This function is used to verify the right click context menu of a Query field item
        '''
        metadataobject.verify_querytree_context_menu(self, field_name, field_position, context_menu_list, msg)
    
    def verify_field_listed_under_datatree(self, field_type, field_name, position, msg='Step X'):
        '''
        Desc:- This function is used to verify whether the field is listed under Data tree
        '''
        metadataobject.verify_field_in_data_pane(self,field_type, field_name, position, msg=msg)
        
    def verify_field_listed_under_querytree(self, bucket_type, field_name, position, msg='Step X', color_to_verify=None, font_to_verify=None):
        '''
        Desc:- This function is used to verify whether the field is listed under Query tree
                Here you can verify the color and the font of the query field.
        '''
        metadataobject.verify_field_in_query_pane(self,bucket_type,field_name, position, msg=msg, color_to_verify=color_to_verify, font_to_verify=font_to_verify)
    
    def verify_all_fields_in_query_pane(self, expected_fields, msg):
        """
        Desc: This function will verify all fields listed in querypane
        """
        metadataobject.verify_query_panel_all_field(self, expected_fields,msg)
        
    def verify_field_availability_in_querytree(self, start_bucket_name, field_name, end_bucket_name, msg='Step X', availability=True):
        '''
        Desc:- This function is used to check the availability of a field under query bucket.
        '''
        metadataobject.verify_field_available_in_query_pane(self,start_bucket_name, field_name, end_bucket_name, msg=msg, availability=availability)
            
    def verify_field_in_filterbox(self, field_name, position=1, msg='Step X'):
        '''
        Desc:- This function is used to verify whether the field is listed under Filter box
        :usage verify_field_in_filterbox('PRODUCT_CATEGORY and BUSINESS_REGION', 1, msg="Step09: Verify  Query added to filter pane")
        '''
        metadataobject.verify_field_in_filter_pane(self,field_name=field_name, position=position, msg=msg)
        
    def verify_empty_filterbox(self, msg='Step X'):
        '''
        Desc:- This function is used to verify whether the field is listed under Filter box
        '''
        metadataobject.verify_field_in_filter_pane(self, msg=msg)
         
    def select_field_in_filterbox(self, field_name, field_position):
        '''
        Desc:- This function is used to select the field is listed under Filter box [uses only left click]
        '''
        metadataobject.select_filterbox_field(self, field_name, field_position, 'left')
    
    def right_click_on_field_in_filterbox(self, field_name, field_position, context_menu_path):
        '''
        Desc:- This function is used to right click on the field in filter box and select the item from the context menu
        '''
        metadataobject.select_filterbox_field(self, field_name, field_position, 'right', context_menu_path)
    
    def select_field_under_query_tree(self, field_name, field_position):
        '''
        Desc:- This function is used to select the field is listed under query tree [uses only left click]
        '''
        metadataobject.select_querytree_field(self, field_name, 'left', field_position)
        
    def multiselect_querytree_field(self, field_name_list, context_menu_path):
        '''
        Desc:- This function is used to select the field is listed under query tree [uses only left click]
        Usage: multiselect_querytree_field(['PRODUCT_CATEGORY_1','PRODUCT_SUBCATEG_1'], 'Delete')
        '''
        metadataobject.multiselect_querytree_field(self, field_name_list, context_menu_path)
    
    def right_click_on_field_under_query_tree(self, field_name, field_position, context_menu_path):
        '''
        Desc:- This function is used to right click on the field in query tree and select the item from the context menu
        '''
        metadataobject.select_querytree_field(self, field_name, 'right', field_position, context_menu_path)
    
    def select_filter_aggregation_combobox(self, field_type, aggregation_type, close_dialog_button=None):
        '''
        Desc:- This function is used to select the aggregation type - 'SUM'
        '''
        metadataobject.create_visualization_filters_(self, field_type, ['Aggregation', aggregation_type], close_dialog_button=close_dialog_button)
    
    def select_filter_by_combobox(self, field_type, by_type, close_dialog_button=None):
        '''
        Desc:- This function is used to select the BY type - '(None)'
        '''
        metadataobject.create_visualization_filters_(self, field_type, ['By', by_type], close_dialog_button=close_dialog_button)   
    
    def select_filter_operator_combobox(self, field_type, operator_type, close_dialog_button=None):
        '''
        Desc:- This function is used to select the operator type - 'Equal to' or 'Greater than equal to'
        '''
        metadataobject.create_visualization_filters_(self, field_type, ['Operator', operator_type], close_dialog_button=close_dialog_button)
    
    def filter_from_input_and_to_input(self, field_type, from_input=None, to_input=None, close_dialog_button=None):
        '''
        Desc:- This function is used to enter the input in From textbox and/or To textbox  - '1000', '25'
        '''
        if from_input!=None:
            metadataobject.create_visualization_filters_(self, field_type, ['From', from_input], close_dialog_button=close_dialog_button)
        if to_input!=None:
            metadataobject.create_visualization_filters_(self, field_type, ['To', to_input], close_dialog_button=close_dialog_button)
    
    def filter_search_value_input(self, field_type, search_value_input, close_dialog_button=None):
        '''
        Desc:- This function is used to search the entered value in search box inside filter dialog
        '''
        metadataobject.create_visualization_filters_(self, field_type, ['SearchValues', search_value_input], close_dialog_button=close_dialog_button)
    
    def select_filter_field_values(self, field_value_list, Ok_button=False):
        '''
        Desc:- This function is used to select values inside filter dialog
        '''
        metadataobject.select_or_verify_visualization_filter_values(self, field_value_list, Ok_button=Ok_button)
        
    def verify_filter_field_values(self, field_value_list, verify_type, ):
        '''
        Desc:- This function is used to verify the list of field value list in filter dialog
        Usage: field_value_list=['[All','EMEA']
        metaobj.verify_filter_field_values(field_value_list, verify='true')
        verify='true' -> To verify check box is checked
                OR
        metaobj.select_or_verify_visualization_filter_values(item_list, verify=None)
        verify=None -> To verify check box is Unchecked
        '''
        metadataobject.select_or_verify_visualization_filter_values(self, field_value_list,verify=verify_type)
    
    def enter_filter_starting_date_and_ending_date(self, field_type, start_date=None, end_date=None):
        '''
        Desc:- This function is used to verify the list of field value list in filter dialog
        Usage: l=['Jan','01','2008'] For 'Starting Date' Or 'Ending Date'
        '''
        if start_date!=None:
            metadataobject.create_visualization_filters_(self, field_type, ['Starting Date',start_date])
        if end_date!=None:
            metadataobject.create_visualization_filters_(self, field_type, ['Ending Date',end_date])
            
    def select_filter_sort_combobox(self, field_type, sort_type, close_dialog_button=None):
        '''
        Desc:- This function is used to select the sort_type - 'Ascending' or 'Decending'
        '''
        metadataobject.create_visualization_filters_(self, field_type, ['Sort', sort_type], close_dialog_button=close_dialog_button)
    
    def deselect_filter_show_prompt_checkbox(self, field_type, sort_type, close_dialog_button=None):
        '''
        Desc:- This function is used to select the deselect the 'Show Prompt' Checkbox
        '''
        metadataobject.create_visualization_filters_(self, field_type, ['ShowPrompt', sort_type], close_dialog_button=close_dialog_button)  
    
    def close_filter_dialog(self, btn_type):
        '''
        Desc:- This function is used to accept [OK] the changes or rejects [Cancel] the changes made in filter dialog
        '''
        from selenium.webdriver import ActionChains
        if btn_type=='ok':
            action1 = ActionChains(self.driver)
            action1.move_to_element(self.driver.find_element_by_id("avFilterOkBtn")).click(self.driver.find_element_by_id("avFilterOkBtn")).perform()
            del action1
        else:
            action1 = ActionChains(self.driver)
            action1.move_to_element(self.driver.find_element_by_id("avFilterCancelBtn")).click(self.driver.find_element_by_id("avFilterCancelBtn")).perform()
            del action1
        
    def enter_field_text_group(self, field_text):
        '''
        Desc:- This function is used to enter the name of the field in create group dialog
        '''
        metadataobject.change_text_field_for_group(self, field_text)
    
    def slect_group_grid_values(self, value_list_for_group):
        '''
        Desc:- This function is used to multi select the grid values of field in create group dialog
        '''
        metadataobject.choose_value_list_for_group(self, value_list_for_group)
    
    def rename_group(self, field_text):
        '''
        Desc:- This function is used to enter the name of the field in create group dialog
        Usage: rename_group("new name")
        '''
        metadataobject.rename_group(self, field_text)
    
    def create_group_options(self, group_option):
        '''
        Desc:- This function is used to click to button -group, rename, ungroup in Create group dialog
        '''
        metadataobject.select_options_for_group(self, group_option)
    
    def extend_existing_group(self, value_list_to_extend, extend_group_name):
        '''
        Desc:- This function is used to extend the existing group with additional values
        '''
        metadataobject.extend_values_in_group(self, value_list_to_extend, extend_group_name)
    
    def exit_group_dialog(self, btn_type):
        '''
        Desc:- This function is used to exit the group dialog by clicking on Ok/Cancel
        '''
        metadataobject.close_group_dialog(self, btn_type)
    
    def verify_group_grid_values(self, expected_grid_value_list, msg):
        '''
        Desc:- This function is used to verify the grid field values
        '''
        metadataobject.verify_fields_in_groupdialog(self, expected_grid_value_list, msg)
    
    def create_bins(self, field_name, name_textbox_value=None, format_textbox_value=None, format_button_dict=None, bin_width=None, btn_click='OK'):
        '''
        :Description: This function is used to set the values in create a bins dialog.
        '''
        metadataobject.create_bins(self, field_name, name_textbox_value=name_textbox_value, format_textbox_value=format_textbox_value, format_button_dict=format_button_dict, bin_width=bin_width, btn_click=btn_click)  
    
    def verify_bins_dialog(self, bin_dialog_title=None, name_textbox_value=None, format_textbox_value=None, format_button_visible=True, bin_width_value=None, ok_btn_status='Enabled', btn_click='OK', msg='Step X'):
        '''
        :Description: This function is used to verify different controls in create a bins dialog.
        '''
        custom_msg=msg + ": Verify the Create Bins Dialog."
        metadataobject.verify_bins_dialog(self, bin_dialog_title=bin_dialog_title, name_textbox_value=name_textbox_value, format_textbox_value=format_textbox_value, format_button_visible=format_button_visible, bin_width_value=bin_width_value, ok_btn_status=ok_btn_status, btn_click=btn_click, msg=custom_msg)
    
    """ ************************************************* This is for RESULTAREA Section. *******************************************"""
    def verify_x_axis_title(self, expected_title_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css="text[class^='xaxis'][class$='title']", x_or_y_axis_title_length=None, msg='Step X'):
        """
        :usage verify_x_axis_title(['Product Category'], msg='Step01:' )
        """
        custom_msg=msg + ' : Verify X-axis title.'
        resultobject.verify_xy_axis_title(self, expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_y_axis_title(self, expected_title_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css="text[class='yaxis-title']", x_or_y_axis_title_length=None, msg='Step X'):
        """
        :usage verify_y_axis_title(['Cost of Goods'], msg='Step01:' )
        """
        custom_msg=msg + ' : Verify Y-axis title.'
        resultobject.verify_xy_axis_title(self, expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_x_axis_label(self, expected_label_list, parent_css='#MAINTABLE_wbody1_f', xyz_axis_label_css="svg > g text[class^='xaxis'][class*='labels']", xyz_axis_label_length=None, msg='Step X'):
        """
        :usage verify_x_axis_label(['Accessories','Camcorder'], msg='Step01: Verify x-axis label'
        """
        custom_msg=msg + ' : Verify X-axis label.'
        resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_y_axis_label(self, expected_label_list, parent_css='#MAINTABLE_wbody1_f', xyz_axis_label_css="svg > g text[class^='yaxis-labels']", xyz_axis_label_length=None, msg='Step X'):
        """
        :usage verify_y_axis_label(['0','30M','60M'], msg='Step01: Verify y-axis label'
        """
        custom_msg=msg + ' : Verify Y-axis label.'
        resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_z_axis_label(self, expected_label_list, parent_css='#MAINTABLE_wbody1_f', xyz_axis_label_css="svg > g text[class^='zaxis'][class*='labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Z-axis label.'
        resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_rows_label(self, expected_label_list, parent_css='#MAINTABLE_wbody1_f', label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Rows label.'
        resultobject.verify_visualization_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='rows', label_length=label_length, msg=custom_msg)
    
    def verify_column_label(self, expected_label_list, parent_css='#MAINTABLE_wbody1_f', label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Columns label.'
        resultobject.verify_visualization_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='column', label_length=label_length, msg=custom_msg)
    
    def verify_pie_label_in_single_group(self, expected_label_list, parent_css='#MAINTABLE_wbody1 svg > g', label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        custom_msg=msg + ": Verify Pie Label in a single Group."
        resultobject.verify_pie_label_in_single_group(self, expected_label_list, parent_css, label_css, custom_msg)
    
    def verify_legends(self, expected_legend_list, parent_css="#MAINTABLE_wbody1_f", legend_length=None, msg='Step X'):
        '''
        Desc: This function is used to verify legend labels
        '''
        custom_msg= msg + " : Verify the legend labels."
        resultobject.verify_legends(self, expected_legend_list, parent_css, legend_length=legend_length, msg=custom_msg)
    
    def verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        :usage verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 28, msg='Step.5: Verify number of risers')
        '''
        custom_msg= msg + " : to verify number of risers available."
        resultobject.verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, custom_msg)
    
    def verify_number_of_pie_segments(self, parent_css, risers_per_segment, expected_number, msg):
        '''
        Desc: This function is used to verify the number of pie segments.
        '''
        custom_msg= msg + ": to verify number of pie segments available."
        resultobject.verify_number_of_pie_segment(self, parent_css, risers_per_segment, expected_number, custom_msg)
    
    def verify_number_of_circles(self, parent_css, minimum_number, maximum_number, msg):
        '''
        Desc: This function is used to verify the number of circles. As number of circles differs in a less margin from resolution to resolution
        user will have to pass a range.
        '''
        custom_msg= msg + ": to verify number of circles available."
        resultobject.verify_number_of_circles(self, parent_css, minimum_number, maximum_number, custom_msg)
                        
    def verify_pie_label_and_value_in_multiple_groups(self, expected_label_list, expected_total_label_list, parent_css='MAINTABLE_wbody0 svg > g', label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels and total labels in multiple groups.
        '''
        custom_msg1=msg + ": Verify Pie Labels in multiple Groups."
        custom_msg2=msg + ": Verify Pie Label total values in multiple Groups."
        resultobject.verify_pie_label_and_value_in_multiple_groups(self, expected_label_list, expected_total_label_list, parent_css, label_css, custom_msg1, custom_msg2)
    
    def verify_chart_color_using_get_attribute(self, riser_css, color_name, parent_css='#MAINTABLE_wbody1_f', attribute='fill', msg='Step X'):
        '''
        Desc: This function is used to verify chart color using the object attribute. attribute can be 'fill' OR 'stroke'.
        '''
        custom_msg=msg + ": Verify chart color."
        miscelaneousobject.verify_chart_color(self, parent_css, riser_css, color_name, 'get_attribute', attribute, custom_msg)
        
    def verify_chart_color_using_get_css_property(self, riser_css, color_name, parent_css='#MAINTABLE_wbody1_f', attribute='fill', msg='Step X'):
        '''
        Desc: This function is used to verify chart color using css property. attribute can be 'fill' OR 'stroke'.
        :usage verify_chart_color_using_get_css_property("rect[class*='riser!s0!g0!mbar']", 'lochmara',  msg='Step.6: Verify riser color')
        '''
        custom_msg=msg + ": Verify chart color."
        miscelaneousobject.verify_chart_color(self, parent_css, riser_css, color_name, 'get_css_property', attribute, custom_msg)
         
    def select_tooltip(self, riser_css, menu_path, parent_css='MAINTABLE_wbody1', initial_move_xy_dict=None, element_location='middle', xoffset=0, yoffset=0, use_marker_enable=False, move_to_tooltip=False):
        '''
        Desc:- This function is used to select tooltip by hovering on the element, if required need to use javascript to enable the marker point.
        :param riser_css:- "riser!s0!g0!mbar"
        :param menu_path:- Filter chart, Exclude from Chart, Drill down
        :param use_marker_enable:- True or False
        :Param initial_move_xy_dict:- Before moving the mouse to the riser, we can move our mouse to any desired location. If it is None,
                by default mouse will move to the top left corner of the monitor.        
        :usage select_tooltip("riser!s0!g0!mbar", 'Drill down to->Store Business Sub Region')
        '''
        tooltip_elem=self.driver.find_element_by_css_selector("#"+parent_css+" [class*='"+riser_css+"']")
#         resultobject.move_mouse_to_chart_component(self, tooltip_elem, initial_move_xy_dict=initial_move_xy_dict, element_location='top_left', xoffset=2, yoffset=2, use_marker_enable=use_marker_enable, move_to_tooltip=move_to_tooltip)
        resultobject.move_mouse_to_chart_component(self, tooltip_elem, initial_move_xy_dict=initial_move_xy_dict, element_location=element_location, xoffset=xoffset, yoffset=yoffset, use_marker_enable=use_marker_enable, move_to_tooltip=move_to_tooltip)
        tooltip_menu_list=menu_path.split('->')
        if len(tooltip_menu_list)==1:
            resultobject.select_tooltip_item(self, tooltip_menu_list[0])
        elif len(tooltip_menu_list)==2:
            resultobject.select_bilevel_tooltip_item(self, tooltip_menu_list[0], tooltip_menu_list[1])
    
        
    def verify_tooltip(self, riser_css, expected_tooltip_list, msg, parent_css='MAINTABLE_wbody1', initial_move_xy_dict=None, element_location='middle', xoffset=0, yoffset=0, use_marker_enable=False, move_to_tooltip=False):
        '''
        Desc:- This function is used to verify tooltip by hovering on the element, if required need to use javascript to enable the marker point.
        :param absolute_css_path:- This is the absolute css path to the marker point.
        :param riser_css:- "riser!s0!g0!mbar"
        :Param initial_move_xy_dict:- Before moving the mouse to the riser, we can move our mouse to any desired location. If it is None,
                by default mouse will move to the top left corner of the monitor.
        :Param parent_css='MAINTABLE_wbody1'   
        :param expected_tooltip_list:- The tooltip list which is expected. ex: ['Discount:$6,014,845.52', 'Filter Chart']
        :usage verify_tooltip("marker!s0!g1!mmarker!r0!c0",q12013_tooltip,msg='Step09: Verify q12013_riser_ tooltip'
        '''
        tooltip_elem=self.driver.find_element_by_css_selector("#"+parent_css+" [class*='"+riser_css+"']")
        resultobject.move_mouse_to_chart_component(self, tooltip_elem, initial_move_xy_dict=initial_move_xy_dict, element_location=element_location, xoffset=xoffset, yoffset=yoffset, use_marker_enable=use_marker_enable, move_to_tooltip=move_to_tooltip)
        resultobject.verify_tooltip(self, expected_tooltip_list, msg=msg)
    
    def select_tooltip_with_limited_search(self, parent_css, riser_css, tooltip_css, item_name, element_location='bottom_middle', javascript_marker_enable=None, mouse_duration=2.5):
            '''
            Desc: limit tooltip css to specific li, so that calculation time will be saved. and webelement click used, coreutility left click for ff not working in this case
            tooltip_css: limit tooltip css to specific li, so that calculation time will be saved. Here i limited to last li for drill up
            tooltip_css="#MAINTABLE_wbody1 span[id*='tdgchart-tooltip']:not([style*='hidden']) li.tdgchart-tooltip-pad:last-child span[style]"
            item_name='Drill up to Product Subcategory'
            parent_css="#MAINTABLE_wbody1"
            element_location='top_middle'
            riser_css='marker!s0!g5!mmarker'
            visual.select_tooltip_with_limited_search(parent_css, riser_css, tooltip_css, item_name, element_location, javascript_marker_enable=True)
            '''
            parent_elem=self.driver.find_element_by_css_selector(parent_css)
            utillobject.click_on_screen(self, parent_elem, element_location)
            tooltip_elem=self.driver.find_element_by_css_selector(parent_css+" [class*='"+riser_css+"']")
            if javascript_marker_enable!=None:
                utillobject.click_on_screen(self, tooltip_elem, element_location, javascript_marker_enable=javascript_marker_enable, mouse_duration=mouse_duration)
            else:
                utillobject.click_on_screen(self, tooltip_elem, element_location, mouse_duration=mouse_duration)
            utillobject.synchronize_with_number_of_element(self, tooltip_css, 1, 30)
            elems=self.driver.find_elements_by_css_selector(tooltip_css)
            tooltip_item_to_be_selected=elems[[elem.text.strip() for elem in elems].index(item_name)]
            tooltip_item_to_be_selected.click()
    
    def select_lasso_tooltip(self, item_name):
        resultobject.select_lasso_tooltip_item(self, item_name)
        
    def create_lasso(self, source_element, target_element, source_xoffset=0, source_yoffset=0, target_xoffset=0, target_yoffset=0, source_element_location='middle', target_element_location='middle'):
        '''
        Desc:- This function is used to create a lasso by dragging from source to target element. The default behavior is it will drag from the middle.
                If your want to provide some offset, then you can.
        '''
        resultobject.create_laso(self, source_element, target_element, source_element_location, source_xoffset, source_yoffset, target_element_location, target_xoffset, target_yoffset)
    
    def create_lasso_using_action_chain(self, source_riser_css, target_riser_css, parent_css="#MAINTABLE_wbody1"):
        """
        Description : Drag mouse from one riser to another riser to create lasso in chart
        :param - source_riser_css : Css value of source riser. Example : rect[class='riser!s0!g1!mbar']
        :param - target_riser_css : Css value of target riser. Example : rect[class='riser!s0!g4!mbar']
        :Usage - create_lasso_using_action_chain("rect[class*='riser!s0!g0!mbar']", "rect[class*='riser!s1!g1!mbar")
        """
        resultobject.create_lasso_using_action_chain(self, source_riser_css, target_riser_css, parent_css)
        
    def create_marker_lasso(self, source_element, target_element, source_xoffset=0, source_yoffset=0, target_xoffset=0, target_yoffset=0, source_element_location='middle', target_element_location='middle', enable_marker=True):
        '''
        Desc:- This function is used to create a lasso by dragging from source to target element. The default behavior is it will drag from the middle.
                If your want to provide some offset, then you can.
        '''
        resultobject.create_laso(self, source_element, target_element, source_element_location, source_xoffset, source_yoffset, target_element_location, target_xoffset, target_yoffset, enable_marker=enable_marker)
            
    def verify_lasso_tooltip(self, expected_tooltip_list, msg):
        resultobject.verify_lasso_tooltip(self, expected_tooltip_list, msg=msg)
                                        
    def select_chart_component(self, riser_or_marker_element, use_marker_enable=False):
        resultobject.select_chart_component(self, riser_or_marker_element, use_marker_enable=use_marker_enable)
        
    def multi_select_chart_component(self, riser_or_marker_element_list, use_marker_enable=False):
        resultobject.multiselect_chart_component(self, riser_or_marker_element_list, use_marker_enable=use_marker_enable)  
    
    def rename_grouped_riser_name(self, old_name, new_name, close_button_name=None):
        '''
        Desc: This is to rename the Rename-Dialog for Group riser name.
        '''
        resultobject.rename_or_verify_grouped_riser_name(self, default_verify_name=old_name, new_name=new_name, close_button_name=close_button_name)
    
    def verify_grouped_riser_name(self, expected_name, msg='Step X', close_button_name=None):
        '''
        Desc: This is to verify the Rename-Dialog for Group riser name.
        '''
        resultobject.rename_or_verify_grouped_riser_name(self, default_verify_name=expected_name, close_button_name=close_button_name, msg=msg)
        
    def verify_header_footer_property(self, parent_id, header_footer_index, verify_style, step_num='X'):
        '''
        Desc: This function is used to verify header footer styling properties
        verify_style={'font_color':'red','bold':True, 'text_value':'100.00','text_align':'754','bg_color':'yellow'}
        Usage:verify_header_footer_property('MAINTABLE_1', 1, verify_style,"11")
        '''
        resultobject.verify_header_footer_property(self, parent_id, header_footer_index, verify_style, step_num=step_num)
    
    def select_resultarea_panel_caption_btn(self, position=0, parent_css="div[id^='BoxLayoutMiniWindow']", select_button_name='maximize', drop_down_menu_item_name=None):
        '''
        Desc: This function is used to click on the right corner panel buttons. And also we can select the items from the drop down arrow.
        param: position: 0, 1, 2, ... This is the Chart/Grid panel position number starts/scans from top-left to bottom-right.
        param :parent_css = This is the css of the panel.(to selecet IA or Visualization css area)
        select_button_name: 'menu' OR 'maximize' OR 'restore' OR 'close'
        Usage: select_panel_caption_btn(0, 'maximize')
        Usage: select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        '''
        resultobject.select_resultarea_panel_caption_btn(self, position, parent_css, select_button_name, drop_down_menu_item_name=drop_down_menu_item_name)
        
    """********************************This is for PROPERTY Section. *****************************************"""
    
    def select_single_item_from_show_prompt_table(self, item_name, parent_prompt_css='#Prompt_1', javascript_scroll_down=False): 
        '''
        Desc: This function will select a single item from the frompt table. If the item is not visible, then use javascript to make it visible.
        '''   
        propertyobject.select_single_item_from_show_prompt_table(self, item_name, parent_prompt_css, javascript_scroll_down)
    
    def verify_show_prompt_table_list(self, expected_items_list, parent_prompt_css='#Prompt_1', msg='Step X'):
        '''
        Desc: This function will verify all items in the table.
        '''
        custom_msg=msg+' Verify all the items in the provided prompt table.'
        propertyobject.verify_show_prompt_table_list(self, expected_items_list, parent_prompt_css, custom_msg)
        
    def verify_item_checked_status_in_show_prompt_table(self, item_name, parent_prompt_css='#Prompt_1', javascript_scroll_down=False, checked_status=True, msg='Step X'):
        '''
        Desc: This function will verify if the requested item is checked or not. If the item is not visible, then use javascript to make it visible.
        '''
        select_status='Checked' if checked_status==True else 'Unchecked'
        custom_msg=msg+' Verify if ' + item_name + ' is ' + select_status + '.'
        propertyobject.verify_item_checked_status_in_show_prompt_table(self, item_name, parent_prompt_css, javascript_scroll_down, checked_status, custom_msg)
    
    def verify_prompt_title(self, title_name, parent_prompt_css='#ar_Prompt_1'):
        '''
        Desc: This is to verify the title of the prompt window.
        '''
        propertyobject.verify_prompt_title(self, parent_prompt_css, title_name)
        
    def select_prompt_menu(self, prompt_menu_item, parent_prompt_css='#ar_Prompt_1'):
        '''
        Desc: This function will select the prompt menu item.
        '''
        propertyobject.select_prompt_menu(self, parent_prompt_css, prompt_menu_item)  
    
    def verify_prompt_menu(self, expected_prompt_menu_list, parent_prompt_css='ar_Prompt_1', msg='Step X'):
        '''
        Desc: This function will select the prompt menu item.
        '''
        custom_msg=msg+' Verify all the items available in the prompt menu.'
        propertyobject.verify_prompt_menu(self, parent_prompt_css, expected_prompt_menu_list, custom_msg)   
    
    def edit_prompt_title(self, parent_prompt_css, old_title, new_title, close_button_type='OK'):
        '''
        Desc: This function is used to edit the prompt title. Close button can be OK OR Cancel
        '''
        propertyobject.edit_prompt_title(self, parent_prompt_css, old_title, new_title, close_button_type)
    
    def move_slider_using_page_up_or_down_key(self, page_up_down_times, parent_css='#ar_Prompt_1', drag_button='min', move_type='left', comparison_type='integer'):
        '''
        Desc: This function is used to verify either minimum or maximum value of the slider.
        Comparison_type can be'integer' OR 'floating'
        '''
        propertyobject.move_slider_using_page_up_or_down_key(self, parent_css, drag_button, move_type, page_up_down_times, comparison_type=comparison_type)
    
    def drag_minimum_value_slider_in_filter_prompt(self, target_value, prompt_css="#Prompt_1"): 
        """
        Description : Drag the minimum value slider in filter prompt
        :Usage : drag_minimum_value_slider_in_filter_prompt(14810)
        """
        propertyobject.drag_minimum_value_slider_in_filter_prompt(self, target_value, prompt_css)
        
    def verify_slider_min_max_value_in_live_preview(self, expected_val, parent_css = '#ar_Prompt_1', msg = 'Step X', drag_button='min', comparison_type='integer'):
        '''
        Desc: This function is used to verify either minimum or maximum value of the slider. comparison_type can be'integer' OR 'floating' 
        '''
        value_type = 'minimum' if drag_button == 'min' else 'maximum'
        custom_msg = msg+' Verify slider value for ' + value_type + ' value in Live Preview.'
        propertyobject.verify_slider_min_max_value(self, parent_css, expected_val, custom_msg, drag_button=drag_button, comparison_type=comparison_type)
    
    def verify_slider_min_max_value_in_run_window(self, expected_val, parent_css = '#sliderPROMPT_1', msg = 'Step X', drag_button='min', comparison_type='integer'):
        '''
        Desc: This function is used to verify either minimum or maximum value of the slider. comparison_type can be'integer' OR 'floating' 
        '''
        value_type = 'minimum' if drag_button == 'min' else 'maximum'
        custom_msg = msg+' Verify slider value for ' + value_type + ' value in Run window.'
        propertyobject.verify_slider_min_max_value(self, parent_css, expected_val, custom_msg, drag_button=drag_button, comparison_type=comparison_type)
            
    """********************************This is for RUN Section. *****************************************"""
    
    def select_bottom_right_run_menu_options(self, menu_option_button_name=None, parent_css='#MAINTABLE_menuContainer1', toggle_button_click='yes'):
        '''
        Desc: This function is used to click the run menu options buttons. If toggle_button_click is 'yes' then it will click that toggle button,
        means the option menu will open. If it is 'no' means the option menu is already opened.
        '''
        runobject.select_run_menu_options(self, menu_option_button_name=menu_option_button_name, parent_css=parent_css, toggle_button_click=toggle_button_click)
   
    def create_visualization_tabular_report(self, file_name, table_css="#MAINTABLE_wbody2 .arPivot table > tbody > tr"):
        '''
        Desc:-This function is used to create visualization report in run time.
        '''
        runobject.create_visualization_tabular_report(self, file_name=file_name, table_css=table_css)
    
    def verify_visualization_tabular_report(self, file_name, table_css="#MAINTABLE_wbody2 .arPivot table > tbody > tr", msg='Step X'):
        '''
        Desc:-This function is used to verify visualization report in run time.
        '''
        custom_msg = msg+' Verify visualization tabular report. '
        runobject.verify_visualization_tabular_report(self, file_name=file_name, table_css=table_css, msg=custom_msg)
    

    def create_table_data_set(self,table_css,file_name):
        ''' 
        Desc: This is used to create table data set of a standard html table. 
        Need to provide the full parent path. means till: table > tbody > tr
        '''
        runobject.create_table_data_set(self, table_css, file_name)
         
    
    def verify_table_data_set(self,table_css,file_name,msg):
        '''
        Desc: This is used to verify table data set of a standard html table.
        Need to provide the full parent path. means till: table > tbody > tr
        '''
        runobject.verify_table_data_set(self, table_css, file_name, msg)
        
    """********************************This is for MAP Section. *****************************************"""
    
    def select_map_dialog (self, map_type, teritory_name, close_dialog):
        """
        Desc:-This function is used to select the map type. Here all parameters are not mandatory. 
        Default value for map_type is None,
        Default value for teritory_name is None,
        Default value for close_dialog is ok.
        Usage : select_map_dialog(map_type='choropleth', teritory_name='US-all', close_dialog='ok')
        """
        ribbonobject.select_map_dialog(self, map_type=map_type, teritory_name=teritory_name, close_dialog=close_dialog)
        
    def set_geo_role_location(self, role_name, btn_click):
        """
        Desc:-This function is used to select geo_role_location
        Usage : set_geo_role_location(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        """
        mapobject.set_geo_role_location(self, role_name=role_name, btn_click=btn_click)
        
    def select_pan_or_selection_in_map(self, parent_css='#MAINTABLE_wbody1', btn_name='Pan'):
        """
        Desc:-This function is used to select pan_or_selection in map
        btn_name='Pan' or 'Selection'
        Usage: select_pan_or_selection_in_map('#MAINTABLE_wbody2',btn_name='Pan')
        """
        mapobject.select_pan_or_selection(self, parent_css=parent_css, btn_name=btn_name)
        
    """********************************This is for define_compute Section. *****************************************"""

    def enter_define_compute_parameter(self, type_name, type_format, data_field, position):   
        """
        Desc:-This function is used to enter parameter define compute dialog
        @Usage : enter_define_compute_parameter('Compute_1', '14.5','Cost of Goods', 1)
        """
        definecomputeobject.enter_define_compute_parameter(self, type_name, type_format, data_field, position)
        
    def close_define_compute_dialog(self, click_type):   
        """
        Desc:-This function is used to close define compute dialog
        @Usage : close_define_compute_dialog('ok')
        """
        definecomputeobject.close_define_compute_dialog(self, click_type)
        
    def select_calculation_btns(self, btn_series):   
        """
        Desc:-This function is used to close define compute dialog
        @Usage : select_calculation_btns("mult->minus->one")
        """
        definecomputeobject.select_calculation_btns(self, btn_series=btn_series)    
        