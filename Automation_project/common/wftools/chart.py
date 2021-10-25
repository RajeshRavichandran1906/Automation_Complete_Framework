from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.core_utility import CoreUtillityMethods as coreutillobject
from common.pages.ia_metadata import IA_Metadata as metaobject
from common.pages.visualization_metadata import Visualization_Metadata as visual_metaobj
from common.pages.ia_miscelaneous import IA_Miscelaneous as miscelaneousobject
from common.pages.ia_ribbon import IA_Ribbon as ribbonobject
from common.pages.ia_resultarea import IA_Resultarea as ia_resultobject
from common.pages.define_compute import DefineCompute
from common.pages.visualization_ribbon import Visualization_Ribbon as visual_ribbonobj
from common.pages.visualization_resultarea import Visualization_Resultarea as visual_resobj
from common.pages.active_miscelaneous import Active_Miscelaneous as activemisc_obj
from common.pages.ia_run import IA_Run as iarun_obj
from common.pages.info_apps import Infoapps_Left_Panel as infoapps_obj
from common.pages.wf_map import Wf_Map as map_obj
from common.pages.insight_header import Insight_Header as insight_obj
from common.pages.core_metadata import CoreMetaData

class Chart(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    
    run_parent_css="#jschart_HOLD_0"
    preview_parent_css="#pfjTableChart_1"
    
    def __init__(self, driver):
        
        super(Chart, self).__init__(driver)

    """****************************************** This is for Common Section. ************************************"""
    
    def wait_for_number_of_element(self, element_css, expected_number=None, time_out=60):
        miscelaneousobject.wait_for_object(self, element_css, 'number', expected_number=expected_number, time_out=time_out)
    
    def wait_for_visible_text(self, element_css, visble_element_text=None, time_out=60):
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
            
#     def invoke_chart_tool_using_api(self, master, mrid=None, mrpass=None):
#         '''
#         Desc:- This function is used to switch to a new window.
#         '''
#         miscelaneousobject.invoke_ia_tool_using_api(self, tool='chart', master=master, mrid=mrid, mrpass=mrpass)
#         default_riser_css=".chartPanel rect[class^='riser!']"
#         miscelaneousobject.wait_for_object(self, default_riser_css, option='number', expected_number=25, time_out=60)

    def invoke_chart_tool_using_api(self, master, tool='chart',mrid=None, mrpass=None, folder_path=None):
        '''
        Desc:- This function is used to switch to a new window.
        '''
        miscelaneousobject.invoke_ia_tool_using_api_(self, tool=tool, master=master, mrid=mrid, mrpass=mrpass, folder_path=folder_path)
        default_riser_css=".chartPanel rect[class^='riser!']"
        miscelaneousobject.wait_for_object(self, default_riser_css, option='number', expected_number=25, time_out=60)
        
    def invoke_chart_in_edit_mode_using_api(self, fex, mrid=None, mrpass=None):
        '''
        Desc:- This function is used to switch to a new window.
        '''
        miscelaneousobject.invoke_ia_tool_in_edit_mode_using_api(self, fex, tool='chart', mrid=mrid, mrpass=mrpass)
    
    def invoke_chart_in_run_mode(self, webdriver_element):
        pass
    
    def run_fex_using_api_url(self, folder_name, fex_name=None, mrid=None, mrpass=None, home_page='New', run_chart_css="#jschart_HOLD_0", no_of_element=1,wait_time=0):
        '''
        Desc:- This function will run report/chart using api link and sign in as user defined in config file
        Usage: report_obj.run_fex_using_api(subfolder_name='Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass')
        '''
        wait_time=self.chart_long_timesleep if wait_time==0 else wait_time
        miscelaneousobject.run_fex_using_api(self, folder_name, fex_name=fex_name, mrid=mrid, mrpass=mrpass, home_page=home_page)
        Chart.wait_for_number_of_element(self, run_chart_css, no_of_element, wait_time)
        
    def run_htmlfex_using_api_url(self, folder_name, fex_name=None, mrid=None, mrpass=None, home_page='New', run_chart_css="#jschart_HOLD_0", no_of_element=1,wait_time=0):
        '''
        Desc:- This function will run report/chart using api link and sign in as user defined in config file
        Usage: report_obj.run_htmlfex_using_api(subfolder_name='Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass')
        '''
        wait_time=self.chart_long_timesleep if wait_time==0 else wait_time
        miscelaneousobject.run_htmlfex_using_api(self, folder_name, fex_name=fex_name, mrid=mrid, mrpass=mrpass, home_page=home_page)
        Chart.wait_for_number_of_element(self, run_chart_css, no_of_element, wait_time)
        
    def edit_fex_using_api_url(self, folder_name, tool='Chart', fex_name=None, mrid="mrid", mrpass="mrpass"):
        '''
        Desc:- This function will edit retail samples report using api link and sign in as user defined in config file
        Usage: report_obj.edit_retailsamples_using_api(subfolder_name='Auto_Link',fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass')
        '''
        miscelaneousobject.edit_fex_using_api(self, folder_name, tool=tool, fex_name=fex_name, mrid=mrid, mrpass=mrpass)
    
    def logout_chart_using_api(self):
        '''
        Desc:- This function is used to logout from visualization tool using api call
        '''
        miscelaneousobject.logout_ia_using_api(self)
        
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
    
    def verify_element_visiblty(self, element=None, element_css=None, visible=True, msg='Step X'):
        '''
        Desc:- This function is to verify whether the element is visible.
        '''
        custom_msg=msg+': Verify whether the object is visible.'
        utillobject.verify_element_visiblty(self, element=element, element_css=element_css, visible=visible, msg=custom_msg)
    
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
    
    def click_any_bibutton_in_dialog(self, dialog_css="[id^=BiDialog] .window.active", btn_name='OK'):
        '''
        Desc:- This function is to select any button in dialog
        ''' 
        utillobject.click_any_bibutton_in_dialog(self, dialog_css, btn_name)
    
    """ *** This is for RIBBON Section. *** """   
    
    def run_chart_from_toptoolbar(self):
        '''
        Desc: This is used to run visualization from the top toolbar.
        '''
        ribbonobject.select_ia_top_toolbar_item(self, 'run')
    
    def select_item_in_top_toolbar(self, top_toolbar_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        '''
        ribbonobject.select_ia_top_toolbar_item(self, top_toolbar_item_name)
    
    def save_as_chart_from_menubar(self, file_name, file_type=None, folder_location_to_save=None): #This function folder_location_to_save not working. 
        '''
        Desc: This is used to save visualization from menubar.
        :usage save_as_visualization_from_menubar('C2346054')
        '''
        ribbonobject.select_ia_application_menu_item(self, 'save_as')
        miscelaneousobject.ibfs_save_as(self, file_name, file_type=file_type, folder_location_to_save=folder_location_to_save)
        
    def save_as_from_application_menu_item(self, file_name, target_table_path='SmokeTest->My Content', application_menu_item_name='save_as', file_type=None):
        """
        Desc: This function will Click IA application button and click save as under SmokeTest MyContent folder
        """
        visual_ribbonobj.select_visualization_application_menu_item(self, application_menu_item_name)
        utillobject.expand_domain_folders_in_open_dialog(self, target_table_path=target_table_path)
        utillobject.ibfs_save_as(self, file_name, file_type=file_type)
    
    def select_chart_type(self, chart_name):
        '''
        Desc: This is used to select chart type.
        '''
        ribbonobject.select_ia_ribbon_item(self, 'Home', chart_name)
        
    def select_other_chart_type(self, chart_type, Chart_name, chart_index, starting_visibility_index=None, close_dialog='ok', verify_selection=True, verify_tooltip=None):
        '''
        Desc: This is used to select chart type
        Params: chart_type='bar','line','area','pie','x_y_plots','threed','stock','special','html5','map','html5_extension'.
        Params: Chart_name='vertical_clustered_bars', 'vertical_absolute_line'...(The name displayed when you hover over the chart image, with underscores, check the locator file)
        Params: chart_index=1, 2, 3...
        Params: starting_visibility_index=0, 1, 2, 3...(The index of the chart image which is visible)
        '''
        ribbonobject.select_other_chart_types(self, chart_type, Chart_name, chart_index, starting_visibility_index=starting_visibility_index, close_dialog=close_dialog, verify_selection=verify_selection, verify_tooltip=verify_tooltip)
    
    def select_ia_application_menu(self, menu_name):
        """
        Description : Click on application button and select menu
        """
        visual_ribbonobj.select_visualization_application_menu_item(self, menu_name)
        
    def verify_fexcode_syntax(self, expected_syntax_list, msg):
        """
        Desc : This function used to verify given syntax list available in fecode
        """
        pass   
                    
    def verify_chart_output_type(self):
        pass
    
    def verify_ribbon_item_enabled(self):
        pass
    
    def verify_ribbon_item_disabled(self):
        pass
    
    """ ****************************************** This is for METADATA Section. **************************************************** """
    
    def collapse_data_field_section(self, section_path):
        """
        This method used to collapse the data field. data_field_section_path should be in reverse order. for example if 'Product->Product->Model' already expanded then 
        we should pass data_field_section_path as 'Model->Product->Product' to close section
        Example : collapse_data_field_section('Model->Product->Product')
        """
        CoreMetaData.collapse_data_field_section(self, section_path)
    
    def expand_data_field_section(self, section_path):
        """
        This method used to expand the data field
        Example : expand_data_field_section('Product->Product->Model')
        """
        CoreMetaData.expand_data_field_section(self, section_path)
        
    def double_click_on_datetree_item(self, field_name, field_position):
        '''
        Desc:- This function is used to double click and select the field from data tree.
        :usage double_click_on_datetree_item('Revenue', 1)
        '''
        metaobject.select_datatree_field(self, field_name, 'double', field_position)
    
    def right_click_on_datetree_item(self, field_name, field_position, context_menu_path):
        '''
        Desc:- This function is used to right click on the field in data tree and select the item from the context menu.
        :usage right_click_on_datetree_item("Product,Category",1,'Add To Query->Horizontal Axis')
        '''
        metaobject.select_datatree_field(self, field_name, 'right', field_position, context_menu_path)
    
    def drag_field_from_data_tree_to_query_pane(self, field_name, field_position, bucket_name, bucket_position=1, bucket_loc='bottom_middle'):
        '''
        Desc:- This function is used to drag and drop data field to the specified bucket in query tree.
        :param - field_position: 1,2 .. (first match is 1)
        :param - bucket_position: 1,2 .. (first match is 1)
        :usage drag_field_from_data_tree_to_query_pane("PRICE_DOLLARS_BIN_1",1,"Model",1)
        '''
        metaobject.drag_and_drop_from_data_tree_to_query_tree(self, field_name, field_position, bucket_name,bucket_position, bucket_loc=bucket_loc)
        
    def drag_field_within_query_pane(self, source_item_name, target_item_name):
        '''
        Desc:- This function is used to drag and drop data field within query tree.
        :usage drag_field_within_query_pane('Discount','Color')
        '''
        metaobject.drag_and_drop_within_query_tree(self, source_item_name, target_item_name)
    
    def drag_multiple_data_fields_to_query_tree(self,  field_name_list, query_bucket_name, field_position_list=[], query_bucket_position=1, query_bucket_loc='bottom_middle', query_bucket_x=0, query_bucket_y=-1):
        """
        Description : Drag multiple data fields to query tree.
        Usage : drag_multiple_data_fields_to_query_tree(['Gross Profit', 'Revenue', 'Quantity,Sold'], 'Tooltip')
        """
        CoreMetaData.drag_multiple_data_fields_to_query_tree(self, field_name_list, query_bucket_name, field_position_list, query_bucket_position, query_bucket_loc, query_bucket_x, query_bucket_y)
    
    def verify_datatree_field_context_menu(self, field_name, field_position, context_menu_list, msg):
        '''
        Desc:- This function is used to verify the right click context menu of a data tree field item
        '''
        metaobject.verify_datatree_context_menu(self, field_name, field_position, context_menu_list, msg) 
    
    def verify_field_listed_under_datatree(self, field_type, field_name, position, msg='Step X'):
        '''
        Desc:- This function is used to verify whether the field is listed under Data tree
        '''
        metaobject.verify_field_in_data_pane(self,field_type, field_name, position, msg=msg)
        
    """***************************************************QUERY PANE**************************************************************************************************"""
        
    def verify_field_listed_under_querytree(self, bucket_type, field_name, position, msg='Step X', color_to_verify=None, font_to_verify=None):
        '''
        Desc:- This function is used to verify whether the field is listed under Query tree
                Here you can verify the color and the font of the query field.
        '''
        metaobject.verify_field_in_query_pane(self,bucket_type,field_name, position, msg=msg, color_to_verify=color_to_verify, font_to_verify=font_to_verify)
    
    def verify_field_availability_in_querytree(self, start_bucket_name, field_name, end_bucket_name, msg='Step X', availability=True):
        '''
        Desc:- This function is used to check the availability of a field under query bucket.
        '''
        metaobject.verify_field_available_in_query_pane(self,start_bucket_name, field_name, end_bucket_name, msg=msg, availability=availability)
        
    def verify_all_fields_in_query_pane(self, expected_fields, msg):
        """
        Desc: This function will verify all fields listed in querypane
        """
        visual_metaobj.verify_query_panel_all_field(self, expected_fields,msg)
        
    def select_field_under_query_tree(self, field_name, field_position):
        '''
        Desc:- This function is used to select the field is listed under query tree [uses only left click]
        '''
        metaobject.select_querytree_field(self, field_name, 'left', field_position)
    
    def right_click_on_field_under_query_tree(self, field_name, field_position, context_menu_path):
        '''
        Desc:- This function is used to right click on the field in query tree and select the item from the context menu
        '''
        metaobject.select_querytree_field(self, field_name, 'right', field_position, context_menu_path)
        
    """*******************************************************************FILTER BOX*********************************************************************************"""    
            
    def verify_field_in_filterbox(self, field_name, position=1, msg='Step X'):
        '''
        Desc:- This function is used to verify whether the field is listed under Filter box
        '''
        metaobject.verify_field_in_filter_pane(self,field_name=field_name, position=position, msg=msg)
        
    def verify_empty_filterbox(self, msg='Step X'):
        '''
        Desc:- This function is used to verify whether the field is listed under Filter box
        '''
        metaobject.verify_field_in_filter_pane(self, msg=msg)
    
    def select_field_in_filterbox(self, field_name, field_position):
        '''
        Desc:- This function is used to select the field is listed under Filter box [uses only left click]
        '''
        metaobject.select_filterbox_field(self, field_name, field_position, 'left')
    
    def right_click_on_field_in_filterbox(self, field_name, field_position, context_menu_path):
        '''
        Desc:- This function is used to right click on the field in filter box and select the item from the context menu
        '''
        metaobject.select_filterbox_field(self, field_name, field_position, 'right', context_menu_path)
    
    def select_filter_aggregation_combobox(self, field_type, aggregation_type):
        '''
        Desc:- This function is used to select the aggregation type - 'SUM'
        '''
        visual_metaobj.create_visualization_filters(self, field_type, ['Aggregation', aggregation_type], ok=False)
    
    def select_filter_by_combobox(self, field_type, by_type):
        '''
        Desc:- This function is used to select the BY type - '(None)'
        '''
        visual_metaobj.create_visualization_filters(self, field_type, ['By', by_type], ok=False)   
    
    def select_filter_operator_combobox(self, field_type, operator_type):
        '''
        Desc:- This function is used to select the operator type - 'Equal to' or 'Greater than equal to'
        '''
        visual_metaobj.create_visualization_filters(self, field_type, ['Operator', operator_type], ok=False)
    
    def filter_from_input_and_to_input(self, field_type, from_input=None, to_input=None):
        '''
        Desc:- This function is used to enter the input in From textbox and/or To textbox  - '1000', '25'
        '''
        if from_input!=None:
            visual_metaobj.create_visualization_filters(self, field_type, ['From', from_input], ok=False)
        if to_input!=None:
            visual_metaobj.create_visualization_filters(self, field_type, ['To', to_input], ok=False)
    
    def filter_search_value_input(self, field_type, search_value_input):
        '''
        Desc:- This function is used to search the entered value in search box inside filter dialog
        '''
        visual_metaobj.create_visualization_filters(self, field_type, ['SearchValues', search_value_input], ok=False)
    
    def select_filter_field_values(self, field_value_list):
        '''
        Desc:- This function is used to search the entered value in search box inside filter dialog
        '''
        visual_metaobj.select_or_verify_visualization_filter_values(self, field_value_list)
        
    def verify_filter_field_values(self, field_value_list, verify_type):
        '''
        Desc:- This function is used to verify the list of field value list in filter dialog
        Usage: field_value_list=['[All','EMEA']
        metaobj.verify_filter_field_values(field_value_list, verify='true')
        verify='true' -> To verify check box is checked
                OR
        metaobj.select_or_verify_visualization_filter_values(item_list, verify=None)
        verify=None -> To verify check box is Unchecked
        '''
        visual_metaobj.select_or_verify_visualization_filter_values(self, field_value_list,verify=verify_type)
    
    def enter_filter_starting_date_and_ending_date(self, field_type, start_date=None, end_date=None):
        '''
        Desc:- This function is used to verify the list of field value list in filter dialog
        Usage: l=['Jan','01','2008'] For 'Starting Date' Or 'Ending Date'
        '''
        if start_date!=None:
            visual_metaobj.create_visualization_filters(self, field_type, ['Starting Date',start_date])
        if end_date!=None:
            visual_metaobj.create_visualization_filters(self, field_type, ['Ending Date',end_date])
            
    def select_filter_sort_combobox(self, field_type, sort_type):
        '''
        Desc:- This function is used to select the sort_type - 'Ascending' or 'Decending'
        '''
        visual_metaobj.create_visualization_filters(self, field_type, ['Sort', sort_type], ok=False)
    
    def deselect_filter_show_prompt_checkbox(self, field_type, sort_type):
        '''
        Desc:- This function is used to select the deselect the 'Show Prompt' Checkbox
        '''
        visual_metaobj.create_visualization_filters(self, field_type, ['ShowPrompt', sort_type], ok=False)  
    
    def close_filter_dialog(self, btn_type):
        '''
        Desc:- This function is used to accept [OK] the changes or rejects [Cancel] the changes made in filter dialog
        '''
        if btn_type=='ok':
            self.driver.find_element_by_id("avFilterOkBtn").click()
        else:
            self.driver.find_element_by_id("avFilterCancelBtn").click()
            
    """********************************************************************RIBBON BAR*************************************************************************************"""
        
    def verify_checked_class_property_for_selected_object(self, web_element, msg, check_property=True):
        '''
        Desc :-Verify selected class property for the given webelement
        report_obj.verify_checked_class_property_for_selected_object(self, web_element, "Step x:Verify the selected object value")
        '''
        utillobject.verify_checked_class_property(self, web_element, msg, check_property=check_property)
        
    def select_visualization_application_menu_item(self, application_menu_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons -.
        param: item_name: 'save_as' OR 'run' OR 'exit' OR 'new'.
        '''
        visual_ribbonobj.select_visualization_application_menu_item(self, application_menu_item_name)
        
    def switch_ia_ribbon_tab(self, tab_name):
        '''
        Desc:-switch the ribbon tab like Home Format Data
        report_obj.switch_ia_ribbon_tab('Foramt')
        '''
        visual_ribbonobj.switch_ribbon_tab(self, tab_name)
        
    def select_ia_ribbon_item(self, tab_name, ribbon_button_name_path):
        ''''
        Desc :- Switching ia ribbon item : Format->AutoLink
        report_obj.switch_ia_ribbon_item(self, tab_name,ribbon_button_name_path)
        '''
        visual_ribbonobj.select_visualization_ribbon_item(self, tab_name, ribbon_button_name_path)
        
    def run_report_from_toptoolbar(self):
        '''
        Desc: This is used to run visualization from the top toolbar.
        '''
        ribbonobject.select_ia_top_toolbar_item(self, 'run')
        
    def save_file_in_save_dialog(self, file_name, file_type=None,**kwargs):
        '''
        Desc:-This function is used to save file in the save dialog
        '''
        utillobject.ibfs_save_as(self, file_name, file_type,**kwargs)
        
    def select_ia_toolbar_item(self, item_name, **kwargs):#need to remove
        '''
        Desc:- select toolbar item run, save
        visual_ribbonobj.select_ia_toolbar_item('Run')
        '''
        visual_ribbonobj.select_top_toolbar_item(self, item_name, **kwargs)
        
    def ia_exit_save(self, btn_name, parent_object=None):
        '''
        Desc:-This function is used to click on button like Yes, No and Cancel
        '''
        ia_resultobject.ia_exit_save(self, btn_name, parent_object)
    
    def change_output_format_type(self, output_format_type, location='Home'):
        '''
        Desc:- This function is used to change the output format
        '''
        visual_ribbonobj.change_output_format_type(self, output_format_type, location)
        
    def select_ia_exit_from_application_btn(self):
        '''
        This function will click on IA button and will select exit menu
        '''
        visual_ribbonobj.select_visualization_application_menu_item(self, 'exit')
    
    def select_output_format_from_ribbon(self, outpu_fromat_path):
        """
        Description : Click on format button in ribbon bar and select output format options
        :uage : select_output_format_from_ribbon("Excel->Excel (xlsx)")
        """
        ribbonobject.select_output_format(self, outpu_fromat_path)
        
    def select_output_format_from_status_bar(self, outpu_fromat_path):
        """
        Description : Click on format button in status bar and select output format options
        :uage : select_output_format_from_status_bar("Excel->Excel (xlsx)")
        """
        ribbonobject.select_output_format(self, outpu_fromat_path,  select_from="status_bar")
    
    def verify_ribbon_item_is_disabled(self, ribbon_button_name, step_num):
        """
        Description : This method will verify whether ribbon is disabled 
        :usage : verify_ribbon_item_is_disabled("format_auto_drill", "01.02")
        """
        ribbonobject.verify_ribbon_item_is_disabled_or_enabled(self, ribbon_button_name, step_num, enabled=False)
    
    def verify_ribbon_item_is_enabled(self, ribbon_button_name, step_num):
        """
        Description : This method will verify whether ribbon is disabled 
        :usage : verify_ribbon_item_is_enabled("format_auto_drill", "01.02")
        """
        ribbonobject.verify_ribbon_item_is_disabled_or_enabled(self, ribbon_button_name, step_num)
    
    def close_ia_without_save(self):
        """
        Description : This method click IA button and click on exit to close IA then click on No button.
        """
        ia_resultobject.close_ia_without_save(self)
    
    def verify_ribbon_item_selected(self, ribbon_button_name, step_num):
        """
        Description : Verify ribbon bar item is selected by using background color
        :usage : verify_ribbon_item_selected("format_auto_drill", "02.01")
        """
        ribbonobject.verify_ribbon_item_selected_or_not(self, ribbon_button_name, step_num)
        
    def verify_ribbon_item_not_selected(self, ribbon_button_name, step_num):
        """
        Description : Verify ribbon bar item is not selected by using background color
        :usage : verify_ribbon_item_not_selected("format_auto_drill", "02.01")
        """
        ribbonobject.verify_ribbon_item_selected_or_not(self, ribbon_button_name, step_num, selected=False)
            
    """ ************************************************* This is for Preview RESULTAREA Section. *******************************************"""
    
    def verify_x_axis_title_in_preview(self, expected_title_list, parent_css=preview_parent_css, x_or_y_axis_title_css="text[class^='xaxis'][class$='title']", x_or_y_axis_title_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify X-axis title.'
        ia_resultobject.verify_xy_axis_title(self, expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_y_axis_title_in_preview(self, expected_title_list, parent_css=preview_parent_css, x_or_y_axis_title_css="text[class='yaxis-title']", x_or_y_axis_title_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Y-axis title.'
        ia_resultobject.verify_xy_axis_title(self, expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_x_axis_label_in_preview(self, expected_label_list, parent_css=preview_parent_css, xyz_axis_label_css="svg > g text[class^='xaxis'][class*='labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify X-axis label.'
        ia_resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_y_axis_label_in_preview(self, expected_label_list, parent_css=preview_parent_css, xyz_axis_label_css="svg > g text[class^='yaxis-labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Y-axis label.'
        ia_resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_z_axis_label_in_preview(self, expected_label_list, parent_css=preview_parent_css, xyz_axis_label_css="svg > g text[class^='zaxis'][class*='labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Z-axis label.'
        ia_resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_rows_label_in_preview(self, expected_label_list, parent_css=preview_parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Rows label.'
        ia_resultobject.verify_ia_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='rows', label_length=label_length, msg=custom_msg)
    
    def verify_column_label_in_preview(self, expected_label_list, parent_css=preview_parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Columns label.'
        ia_resultobject.verify_ia_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='column', label_length=label_length, msg=custom_msg)
        
    def verify_rows_header_label_in_preview(self, expected_header, expected_label_list, parent_id=preview_parent_css, label_length=None, msg='Step X'):
        visual_resobj.verify_visualization_row_column_header_labels(self, parent_id, expected_header, expected_label=expected_label_list, matrix_type='Rows', label_length=label_length, msg=msg)
     
    def verify_column_header_label_in_preview(self, expected_header, expected_label, matrix_type='Column', parent_id=preview_parent_css, label_length=None, msg='Step X'):
        visual_resobj.verify_visualization_row_column_header_labels(self, parent_id, matrix_type, expected_header, expected_label, label_length=label_length, msg=msg)

    def verify_rows_label(self, expected_label_list, parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Rows label.'
        visual_resobj.verify_visualization_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='rows', label_length=label_length, msg=custom_msg)
    
    def verify_column_label(self, expected_label_list, parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Columns label.'
        visual_resobj.verify_visualization_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='column', label_length=label_length, msg=custom_msg)
    
    def verify_pie_label_in_single_group_in_preview(self, expected_label_list, parent_css=preview_parent_css, label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        custom_msg=msg + ": Verify Pie Label in a single Group."
        ia_resultobject.verify_pie_label_in_single_group(self, expected_label_list, parent_css, label_css, custom_msg)
    
    def verify_chart_title(self, expected_title, window, msg, run_index=0, preview_index=1):
        '''
        Desc: This function will verify chart title
        Usage: verify_chart_title(""Current Month - Daily Sales TrendFor All MODEL", 'run', "Step05: Verify chart title in run window")
        '''
        if window=='run':
            title_elem=self.driver.find_element_by_css_selector("#jschart_HOLD_"+str(run_index)+" .title")
        elif window=='preview':
            title_elem=self.driver.find_element_by_css_selector("#TableChart_"+str(preview_index)+" .title")
        act_title_elem=title_elem.text.replace('\n','')
        utillobject.asequal(self, expected_title, act_title_elem, msg)
        
    def verify_chart_title_text_align(self, expected_title_alignment, window, msg, css_property='text-anchor'):
        '''
        Desc: This function will verify chart title
        Usage: verify_chart_title(""Current Month - Daily Sales TrendFor All MODEL", 'run', "Step05: Verify chart title in run window")
        '''
        if window=='run':
            title_elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 svg g .title").value_of_css_property(css_property)
        elif window=='preview':
            title_elem=self.driver.find_element_by_css_selector("#TableChart_1 svg g .title").value_of_css_property(css_property)
        act_title_alignment=title_elem
        utillobject.asequal(self, expected_title_alignment, act_title_alignment, msg)
    
    def verify_chart_color(self, parent_id, riser_class, color, msg, **kwargs):
        '''Desc: This function will verify chart color
        Usage: utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mneedle", "cerulean_blue", "Step07:07: Verify needle color")
        utillobj.verify_chart_color('MAINTABLE_wbody0',None, 'green', 'Step07:08: Verify Gauge green color',custom_css=".chartPanel path[class='gaugeRange'][fill*='rgb(0,'][fill*='128,'][fill*='0)']")
        '''
        utillobject.verify_chart_color(self, parent_id, riser_class, color, msg, **kwargs)
    
    def verify_data_labels(self, parent_id, expected_datalabel, msg, **kwargs):
        '''
        Desc: Verify data labels
        Usage: gauge chart - verify_data_labels('jschart_HOLD_0',totalLabel,'Step 07:01: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        '''
        visual_resobj.verify_data_labels(self, parent_id, expected_datalabel, msg, **kwargs)
    
    def verify_number_of_chart_segment(self, parent_id, expected_number, msg, **kwargs):
        '''
        Desc: This function is used to verify number of chart segments
        Usage: verify_number_of_chart_segment('jschart_HOLD_0', 10, "Step 07:04: verify the Gauge range", custom_css=".chartPanel path[class*='gaugeRange']")
        '''
        ia_resultobject.verify_number_of_chart_segment(self, parent_id, expected_number, msg, **kwargs)
    
    def verify_legends_in_preview(self, expected_legend_list, parent_css=preview_parent_css, legend_length=None, msg='Step X'):
        '''
        Desc: This function is used to verify legend labels
        '''
        custom_msg= msg + " : Verify the legend labels."
        ia_resultobject.verify_legends(self, expected_legend_list, parent_css, legend_length=legend_length, msg=custom_msg)
        
    def verify_number_of_circles_in_preview(self, parent_css, minimum_number, maximum_number, msg):
        '''
        Desc: This function is used to verify the number of circles. As number of circles differs in a less margin from resolution to resolution
        user will have to pass a range.
        '''
        custom_msg= msg + ": to verify number of circles available."
        ia_resultobject.verify_number_of_circles(self, parent_css, minimum_number, maximum_number, custom_msg)
                        
    def verify_pie_label_and_value_in_multiple_groups_in_preview(self, expected_label_list, expected_total_label_list, parent_css=preview_parent_css, label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels and total labels in multiple groups.
        '''
        custom_msg1=msg + ": Verify Pie Labels in multiple Groups."
        custom_msg2=msg + ": Verify Pie Label total values in multiple Groups."
        ia_resultobject.verify_pie_label_and_value_in_multiple_groups(self, expected_label_list, expected_total_label_list, parent_css, label_css, custom_msg1, custom_msg2)
    
    def verify_chart_color_using_get_attribute_in_preview(self, riser_css, color_name, parent_css=preview_parent_css, attribute='fill', msg='Step X'):
        '''
        Desc: This function is used to verify chart color using the object attribute. attribute can be 'fill' OR 'stroke'.
        '''
        custom_msg=msg + ": Verify chart color."
        miscelaneousobject.verify_chart_color(self, parent_css, riser_css, color_name, 'get_attribute', attribute, custom_msg)
        
    def verify_chart_color_using_get_css_property_in_preview(self, riser_css, color_name, parent_css=preview_parent_css, attribute='fill', msg='Step X'):
        '''
        Desc: This function is used to verify chart color using css property. attribute can be 'fill' OR 'stroke'.
        '''
        custom_msg=msg + ": Verify chart color."
        miscelaneousobject.verify_chart_color(self, parent_css, riser_css, color_name, 'get_css_property', attribute, custom_msg)
        
    def verify_filter_pane_field(self, field_name, position, msg, **kwargs):
        """
        Desc: This function will verify fields in filter pane
        """
        visual_metaobj.verify_filter_pane_field(self, field_name, position, msg, **kwargs)
        
    def verify_slider_labels_in_preview(self, expected_label_list, msg, parent_css=preview_parent_css):
        '''
        Desc:-This function is used to verify slider labels in chart window
        '''
        iarun_obj.verify_slider_labels(self, parent_css, expected_label_list, msg)
        
    def move_chart_slider_in_preview(self, slider_value_to_select, parent_css=preview_parent_css):
        '''
        Desc:-This function is used to verify chart slider
        '''
        iarun_obj.move_chart_slider(self,slider_value_to_select,parent_css)
     
    def verify_color_scale_esri_maps_in_preview(self, expected_color_scale, msg, popup_id="pfjTableChart_1"):
        """
        Desc:-This function is used to verify color_scale_esri_maps_in_preview
        Usage : verify_color_scale_esri_maps(['RANDOM_NUMBER', '540', '553.5', '567', '580.5', '594'], "Step 9.1")
        """
        ia_resultobject.verify_color_scale_esri_maps(self, popup_id, expected_color_scale, msg)
    
    def close_run_preview_window(self):
        """
        Description : Left click on run preview window close button to close run window
        """
        ia_resultobject.close_run_preview_window(self)
        
    """ **********************************************This is for common functions. **************************************************************************************"""
        
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
        
    def api_logout(self):
        """
        Desc: This function uses new functionto pass the api logout url
        """
        utillobject.wf_logout(self)
        
    """ ********************************************This is for AUTO PROMPT***************************************************************"""
    
    def run_auto_prompt_chart(self, item_name='Run'):
        '''
        This function is to select run button in the auto prompt
        '''
        iarun_obj.select_amper_menu(self, item_name)  
        
    def run_auto_prompt_report(self):
        '''
        This function is to select run button in the auto prompt
        '''
        iarun_obj.select_amper_menu(self, 'Run')
        
    def select_field_filter_values_dropdown_in_auto_prompt(self, field_name):
        '''
        This function is used to select field dropdown
        select_field_filter_values_dropdown_in_auto_prompt('MODEL')
        '''
        iarun_obj.select_field_filter_values_dropdown_in_auto_prompt(self, field_name)
        
    def select_single_field_filter_value_in_auto_prompt(self, value_list):
        '''
        This function will select a single value in field autoprompt
        select_single_field_filter_value_in_auto_prompt(['BMW'])
        '''
        iarun_obj.select_field_filter_values_in_auto_prompt(self, value_list, 'list')
    
    def select_input_single_field_filter_value_in_auto_prompt(self, value_list):
        '''
        This function will select a single value in field autoprompt
        select_single_field_filter_value_in_auto_prompt(['BMW'])
        '''
        iarun_obj.select_field_filter_values_in_auto_prompt_(self, value_list, 'input')
        
    def select_single_field_filter_value_in_listbox_auto_prompt(self, value_list):
        '''
        This function will select a single value from list box auto prompt.(scroll bar will be in list of values)
        select_single_field_filter_value_in_auto_prompt(['BMW'])
        '''
        iarun_obj.select_field_filter_values_in_auto_prompt(self, value_list, 'listbox')
        
    def select_multiple_filter_values_from_field_auto_prompt(self,value_list, ):
        '''
        This function will select multiple values in field autoprompt
        select_multiple_filter_values_from_field_auto_prompt(['AUDI','BMW'])
        '''
        iarun_obj.select_field_filter_values_in_auto_prompt(self, value_list, 'check')
        
    def verify_input_type_field_filter_values_in_auto_prompt(self, expected_value_list, msg):
        '''
        This function will verify input type filter values in auto prompt
        verify_input_type_field_filter_values_in_auto_prompt(['AUDI','BMW'], "Step X: Verify CAR field filter values in auto prompt)
        '''
        iarun_obj.verify_field_filter_values_in_auto_prompt(self, expected_value_list, msg, 'input')
        
    def verify_field_filter_values_checked_property_in_auto_prompt(self, expected_value_list, msg, verify_type):
        '''
        This function will verify checked or unchecked property of the autoprompt list of values
        verify_field_filter_values_checked_property_in_auto_prompt(['AUDI','BMW'], "Step X: Verify CAR field filter values in auto prompt, 'checked')
        '''
        iarun_obj.verify_field_filter_values_checked_property_in_auto_prompt(self, expected_value_list, msg, verify_type)
        
    def verify_option_type_field_filter_values_in_auto_prompt(self, expected_value_list, msg):
        '''
        This function will verify input type filter values in auto prompt
        verify_option_type_field_filter_values_in_auto_prompt(['AUDI','BMW'], "Step X: Verify CAR field filter values in auto prompt)
        '''
        iarun_obj.verify_field_filter_values_in_auto_prompt(self, expected_value_list, msg, 'option')
        
    def get_autoprompt_field_object(self, field_name):
        '''
        This function will get field object in auto prompt
        get_autoprompt_field_object('CAR')
        '''
        iarun_obj.get_autoprompt_field_object(self, field_name)
        
    def verify_selected_field_dropdown_value_in_autoprompt(self, field_name, expected_selected_value, msg):
        '''
        This function will verify selected field dropdown value in auto prompt
        verify_selected_field_dropdown_value_in_autoprompt('CAR', 'BMW', "Step x: Verify selected drop down value")
        '''
        iarun_obj.verify_selected_field_dropdown_value_in_autoprompt(self, field_name, expected_selected_value, msg)
        
    def select_auto_prompt_value_back_button(self):
        '''
        This function will select back button in auto prompt
        select_auto_prompt_value_back_button()
        '''
        iarun_obj.select_auto_prompt_value_back_button(self)
        
    def verify_selected_field_dropdown_value_count_in_autoprompt(self, field_name, expected_selected_value, msg):
        '''
        This fucntion will verify the selected dropdown values count in auto prompt
        verify_selected_field_dropdown_value_count_in_autoprompt('MODEL','3 DOOR',"Step x: Verify selected field dropdown value count in auto prompt
        '''
        iarun_obj.verify_selected_field_dropdown_value_count_in_autoprompt(self, field_name, expected_selected_value, msg)
        
    def verify_autoprompt_field_labels_using_asin(self, expected_field_label_list, msg):
        '''
        This function will verify autoprompt field labels
        verify_autoprompt_field_labels(['CAR','COUNTRY','MODEL'], "Step x:Verify autoprompt field labels", 'asin') 
        '''
        iarun_obj.verify_autoprompt_field_labels(self, expected_field_label_list, msg, 'asin')
        
    def verify_autoprompt_field_labels_using_asequal(self, expected_field_label_list, msg):
        '''
        This function will verify autoprompt field labels
        verify_autoprompt_field_labels(['CAR','COUNTRY','MODEL'], "Step x:Verify autoprompt field labels", 'asin') 
        '''
        iarun_obj.verify_autoprompt_field_labels(self, expected_field_label_list, msg, 'asequal')
    
    def verify_field_textbox_value_in_autoprompt(self, field_name, expected_selected_value, msg):
        '''
        This function will verify field text box value in auto prompt
        '''
        iarun_obj.verify_field_textbox_value_in_autoprompt(self, field_name, expected_selected_value, msg)    
        
    def select_radio_button_in_auto_prompt_values(self, radio_button_name):
        '''
        This function will select radio button in auto prompt field filter values
        '''
        iarun_obj.select_radio_button_in_auto_prompt_values(self, radio_button_name)
    
    def select_value_button_in_auto_prompt(self, button_name):
        '''
        This function will select all or none value in auto prompt
        '''
        iarun_obj.select_value_button_in_auto_prompt(self, button_name)
            
    def select_close_button_in_field_filter_values_in_auto_prompt(self):
        '''
        This function will click close button which is in field filter values
        '''
        iarun_obj.select_close_button_in_field_filter_values_in_auto_prompt(self)
        
    def enter_value_field_textbox_in_auto_prompt(self, field_name, input_value):
        '''
        This function will enter value field in textbox in auto prompt
        '''
        iarun_obj.enter_value_field_textbox_in_auto_prompt(self, field_name, input_value)
    
    def enter_value_search_textbox_popup_in_auto_prompt(self, input_value):
        '''
        This function will enter value in search box in popup inside auto prompt
        '''
        iarun_obj.enter_value_search_textbox_popup_in_auto_prompt(self, input_value)
        
    def select_month_in_calendardatepicker_dialog_in_run_window(self, month_to_select):
        '''
        Desc:-This function is used to select month_in_calendardatepicker_dialog.
        '''
        iarun_obj.select_month_in_calendardatepicker_dialog(self, month_to_select)
        
    def select_year_in_calendardatepicker_dialog_in_run_window(self, year_to_select):
        '''
        Desc:-This function is used to select year_in_calendardatepicker_dialog.
        '''
        iarun_obj.select_year_in_calendardatepicker_dialog(self, year_to_select)
    
    def select_date_in_calendardatepicker_dialog_in_run_window(self, date_to_select):
        '''
        Desc:-This function is used to select date_in_calendardatepicker_dialog.
        '''
        iarun_obj.select_date_in_calendardatepicker_dialog(self, date_to_select)
    
    def verify_filter_chained_group_icon_is_visible_in_autoprompt(self, msg):
        '''
        Desc:-This function is used to verify filter chained group icon is displayed in auto prompt window
        '''
        iarun_obj.verify_filter_chained_group_icon_is_visible_in_autoprompt(self, msg)
         
    
    """ ************************************************* This is for RUN WINDOW  Section. *******************************************"""
    
    def verify_x_axis_title_in_run_window(self, expected_title_list, parent_css=run_parent_css, x_or_y_axis_title_css="text[class^='xaxis'][class$='title']", x_or_y_axis_title_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify X-axis title.'
        ia_resultobject.verify_xy_axis_title(self, expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_y_axis_title_in_run_window(self, expected_title_list, parent_css=run_parent_css, x_or_y_axis_title_css="text[class='yaxis-title']", x_or_y_axis_title_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Y-axis title.'
        ia_resultobject.verify_xy_axis_title(self, expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_x_axis_label_in_run_window(self, expected_label_list, parent_css=run_parent_css, xyz_axis_label_css="svg > g text[class^='xaxis'][class*='labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify X-axis label.'
        ia_resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_y_axis_label_in_run_window(self, expected_label_list, parent_css=run_parent_css, xyz_axis_label_css="svg > g text[class^='yaxis-labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Y-axis label.'
        ia_resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_z_axis_label_in_run_window(self, expected_label_list, parent_css=run_parent_css, xyz_axis_label_css="svg > g text[class^='zaxis'][class*='labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Z-axis label.'
        ia_resultobject.verify_xyz_labels(self, expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_rows_label_in_run_window(self, expected_label_list, parent_css=run_parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Rows label.'
        ia_resultobject.verify_ia_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='rows', label_length=label_length, msg=custom_msg)
    
    def verify_column_label_in_run_window(self, expected_label_list, parent_css=run_parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Columns label.'
        ia_resultobject.verify_ia_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='column', label_length=label_length, msg=custom_msg)
        
    def verify_rows_header_label_in_run_window(self, expected_header, expected_label_list, parent_id=run_parent_css, label_length=None, msg='Step X'):
        visual_resobj.verify_visualization_row_column_header_labels(self, parent_id, expected_header, expected_label=expected_label_list, matrix_type='Rows', label_length=label_length, msg=msg)
    
    def verify_column_header_label_in_run_window(self, expected_header, expected_label_list, parent_id=run_parent_css, label_length=None, msg='Step X'):
        visual_resobj.verify_visualization_row_column_header_labels(self, parent_id, expected_header, expected_label=expected_label_list, matrix_type='Column', label_length=label_length, msg=msg)
        
    def verify_riser_pie_labels_and_legends(self, parent_id, expected_label_list, msg, **kwargs):#need to remove
        '''
        Desc: This function will verify chart pie label
        pie_label_css="text[class*='pieLabel']"
        pie_totallabel_css= "text[class^='totalLabel!g']"
        Usage: verify_riser_pie_labels_and_legends('jschart_HOLD_0', pie_label, "Step02.1:",custom_css=pie_label_css)
        '''
        visual_resobj.verify_riser_pie_labels_and_legends(self, parent_id, expected_label_list, msg, **kwargs)
    
    def verify_pie_label_in_single_group_in_run_window(self, expected_label_list, parent_css=run_parent_css, label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        custom_msg=msg + ": Verify Pie Label in a single Group."
        ia_resultobject.verify_pie_label_in_single_group(self, expected_label_list, parent_css, label_css, custom_msg)
    
    def verify_legends_in_run_window(self, expected_legend_list, parent_css=run_parent_css, legend_length=None, msg='Step X'):
        '''
        Desc: This function is used to verify legend labels
        '''
        custom_msg= msg + " : Verify the legend labels."
        ia_resultobject.verify_legends(self, expected_legend_list, parent_css, legend_length=legend_length, msg=custom_msg)
        
    def verify_map_scale_in_run_window(self, parent_id, expected_labels, msg, custom_css=".esriScalebarLabel"):
        '''
        Desc: Verify map scale in run window
        '''
        labels=self.driver.find_elements_by_css_selector("#"+parent_id + " " + custom_css)
        actual_label_list= [title.text.strip() for title in labels]
        utillobject.asequal(self, expected_labels, actual_label_list, msg)
        
    def select_regionlabel_checkbox_in_run_window(self, labellist):
        map_obj.select_regionlabel_checkbox(self, labellist)
    
    def select_mainmenu_btn_in_esrimap(self, btn_name, mainmenu_css="#mainMenuemfobject1"):
        map_obj.select_mainmenu_btn(self, mainmenu_css=mainmenu_css, btn_name=btn_name)
        
    def close_basemap_dialog_in_esrimap(self):
        map_obj.close_basemap_dialog(self)
    
    def verify_pie_label_and_value_in_multiple_groups_in_run_window(self, expected_label_list, expected_total_label_list, parent_css=run_parent_css, label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels and total labels in multiple groups.
        '''
        custom_msg1=msg + ": Verify Pie Labels in multiple Groups."
        custom_msg2=msg + ": Verify Pie Label total values in multiple Groups."
        ia_resultobject.verify_pie_label_and_value_in_multiple_groups(self, expected_label_list, expected_total_label_list, parent_css, label_css, custom_msg1, custom_msg2)
        
    def verify_number_of_circles_in_run_window(self, minimum_number, maximum_number, msg, parent_css=run_parent_css):
        '''
        Desc: This function is used to verify the number of circles. As number of circles differs in a less margin from resolution to resolution
        user will have to pass a range.
        '''
        custom_msg= msg + ": to verify number of circles available."
        ia_resultobject.verify_number_of_circles(self, parent_css, minimum_number, maximum_number, custom_msg)
    
    def verify_chart_color_using_get_attribute_in_run_window(self, riser_css, color_name, parent_css=run_parent_css, attribute='fill', msg='Step X'):
        '''
        Desc: This function is used to verify chart color using the object attribute. attribute can be 'fill' OR 'stroke'.
        '''
        custom_msg=msg + ": Verify chart color."
        miscelaneousobject.verify_chart_color(self, parent_css, riser_css, color_name, 'get_attribute', attribute, custom_msg)
        
    def verify_chart_color_using_get_css_property_in_run_window(self, riser_css, color_name, parent_css=run_parent_css, attribute='fill', msg='Step X'):
        '''
        Desc: This function is used to verify chart color using css property. attribute can be 'fill' OR 'stroke'.
        '''
        custom_msg=msg + ": Verify chart color."
        miscelaneousobject.verify_chart_color(self, parent_css, riser_css, color_name, 'get_css_property', attribute, custom_msg)
    
    def select_tooltip_in_run_window(self, riser_css, menu_path, parent_css=run_parent_css, initial_move_xy_dict=None, element_location='middle', xoffset=0, yoffset=0, use_marker_enable=False, move_to_tooltip=False):
        '''
        Desc:- This function is used to select tooltip by hovering on the element, if required need to use javascript to enable the marker point.
        :param riser_css:- "riser!s0!g0!mbar"
        :param menu_path:- Filter chart, Exclude from Chart, Drill down
        :param use_marker_enable:- True or False
        :Param initial_move_xy_dict:- Before moving the mouse to the riser, we can move our mouse to any desired location. If it is None,
                by default mouse will move to the top left corner of the monitor.        
        :usage select_tooltip("riser!s0!g0!mbar", 'Drill down to->Store Business Sub Region')
        '''
        tooltip_elem=self.driver.find_element_by_css_selector(parent_css+" [class*='"+riser_css+"']")
        ia_resultobject.move_mouse_to_chart_component(self, tooltip_elem, initial_move_xy_dict=initial_move_xy_dict, element_location=element_location, xoffset=xoffset, yoffset=yoffset, use_marker_enable=use_marker_enable, move_to_tooltip=move_to_tooltip)
        tooltip_menu_list=menu_path.split('->')
        if len(tooltip_menu_list)==1:
            ia_resultobject.select_tooltip_item(self, tooltip_menu_list[0])
        elif len(tooltip_menu_list)==2:
            ia_resultobject.select_bilevel_tooltip_item(self, tooltip_menu_list[0], tooltip_menu_list[1])
            
    def verify_tooltip_in_run_window(self, riser_css, expected_tooltip_list, msg, parent_css=run_parent_css, initial_move_xy_dict=None, element_location='middle', xoffset=0, yoffset=0, use_marker_enable=False, move_to_tooltip=False):
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
        tooltip_elem=self.driver.find_element_by_css_selector(parent_css+" [class*='"+riser_css+"']")
        ia_resultobject.move_mouse_to_chart_component(self, tooltip_elem, initial_move_xy_dict=initial_move_xy_dict, element_location=element_location, xoffset=xoffset, yoffset=yoffset, use_marker_enable=use_marker_enable, move_to_tooltip=move_to_tooltip)
        ia_resultobject.verify_tooltip(self, expected_tooltip_list, msg=msg)
    
    def verify_active_chart_tooltip(self, parent_id, raiser_class, expected_tooltip_list, msg): 
        """
        activemisc_obj.verify_active_chart_tooltip('jschart_HOLD_0', "riser!s0!g0!mwedge", 'Category 37.9M', "Step X: Verify active tooltip") 
        """
        activemisc_obj.verify_active_chart_tooltip(self, parent_id, raiser_class, expected_tooltip_list, msg)
        
    def select_or_verify_marker_tooltip_in_run_window(self, marker_class, select_tooltip=None, verify_tooltip_list=None, msg=None, parent_css='#MAINTABLE_wbody0_f', **kwargs):
        """
        This function used to verify marker tooltip or select ,arker tooltip options
        example usage : select_or_verify_marker_tooltip("marker!s0!g0!mmarker!r0!c1!", select_tooltip='Exclude from Chart', verify_tooltip_list=expected_tooltip_list, msg='Step 05: Verify bar value')
        """
        activemisc_obj.select_or_verify_marker_tooltip(self, marker_class, select_tooltip=select_tooltip, verify_tooltip_list=verify_tooltip_list, msg=msg, parent_css=parent_css, **kwargs)
    
    def select_lasso_filter(self, select_item):
        """
        This function used to select lasso tooltip item
        example usage : select_lasso_filter(select_item='Exclude from Chart')
        """
        visual_resobj.select_or_verify_lasso_filter(self, select=select_item)
        
    def verify_lasso_filter(self, item_list, msg):
        """
        This function used to verify lasso tooltip items
        example usage : verify_lasso_filter(item_list=['1 point','Filter Chart','Exclude from Chart'],msg='Step 04: Expect to see the left-click options appear')
        """
        visual_resobj.select_or_verify_lasso_filter(self, verify=item_list, msg=msg)
        
    def select_default_tooltip_menu_in_run_window(self, parent_id, raiser_class, menu_path, wait_time=2, **kwargs):
        """
        This function used to select_default_tooltip_menu_in_run_window
        example usage : select_default_tooltip_menu_in_run_window("MAINTABLE_wbody0","riser!s0!g1!mbar!", 'Filter Chart')
        """
        visual_resobj.select_default_tooltip_menu(self, parent_id=parent_id, raiser_class=raiser_class, menu_path=menu_path, wait_time=wait_time, **kwargs)
    
    def create_drilldown_report(self, drilldown_type, **kwargs):
        """
        @params: browse_file_name
        @params: verify_left_pane
        @params: set_description
        @params: set_target
        @params: msg
        @params: verify_drilldown_type
        @params: verify_enabled_left_pane_icons =['create','duplicate','rename','remove','options]
        @params: create_new_drilldown
        @params: click_ok or delete_all_and_exit or click_cancel
        @params: set_ampersand='add' or 'edit' or 'remove'
        @params: verify_enabled_parameter_icons = ['add','edit','remove']
        create_drilldown_report("report",set_ampersend='add',name_select='DEPARTMENT', type_select='Constant', value_input="MIS", popup_close='ok')
        create_drilldown_report("webpage", url_value="http://www.yahoo.com", click_ok='yes')
        create_drilldown_report("report",set_ampersand='remove')
        create_drilldown_report("report", verify_input_text=[],verify_enabled_parameter_icons=['add'], click_cancel='yes')
        """
        ribbonobject.create_drilldown_report(self, drilldown_type,**kwargs)
     
    
    def select_autodrill_chart_tooltip_menu(self, raiser_class, menu_path, parent_id="jschart_HOLD_0", wait_time=2, **kwargs):
        """
        Description : This methods used to select auto drill chart tooltip menu.  
        :Usage - select_autodrill_chart_tooltip_menu("riser!s5!g4!mbar!r0!c1!", "Drill down to->Store Business Sub Region")
        """
        ia_resultobject.select_autolink_tooltip_menu(self, parent_id, raiser_class, menu_path, wait_time, **kwargs)
    
    def verify_chart_autodrill_breadcrumb_text(self, expected_breadcrumb, step_num, parent_css="#jschart_HOLD_0"):
        """
        Description : Verify auto drill chart bread crumb text as list
        :Usage : verify_chart_autodrill_breadcrumb_text(['Home->NorthAmerica->West->UnitedStates->California->SanDiego->92101'], "01.01")
        """
        iarun_obj.verify_chart_autodrill_breadcrumb_text(self, expected_breadcrumb, step_num, parent_css)
        
    def verify_slider_labels_in_run_window(self, expected_label_list, msg, parent_css=run_parent_css):
        '''
        Desc:-This function is used to verify slider labels in chart window
        '''
        iarun_obj.verify_slider_labels(self, parent_css, expected_label_list, msg)
        
    def move_chart_slider_in_run_window(self, slider_value_to_select, parent_css=run_parent_css):
        '''
        Desc:-This function is used to verify chart slider
        '''
        iarun_obj.move_chart_slider(self,slider_value_to_select, parent_css)
        
    def verify_chart_title_in_run_window(self, chart_title_keyname, expected_title, msg="Step X :", project_object=None):
        '''
        Desc:-This function is used to verify chart title, user need to add the title css in locators.
        '''
        custom_msg=msg+': Verify runtime chart title.'
        iarun_obj.verify_chart_title(self, chart_title_keyname, expected_title, msg=custom_msg, project_object=project_object)
    
    def verify_default_amper_value_in_run_window(self, field_name, expected_value, msg="Step X :"):
        '''
        Desc:-This function is used to verify default_amper_value_in_run_window.
        '''
        custom_msg=msg+': Verify default amper filter value: '+expected_value+' listed under '+field_name
        iarun_obj.verify_default_amper_value(self, field_name, expected_value, msg=custom_msg)   
        
    def select_amper_small_value_list_in_run_window(self, field_name, select_value_list):
        '''
        Desc:-This function is used to select amper_small_value_list_in_run_window.
        '''
        iarun_obj.select_amper_value(self, field_name, value_list=select_value_list, long_value_set=False) 
        
    def search_and_select_amper_large_value_list_in_run_window(self, field_name, select_value_list):
        '''
        Desc:-This function is used to search_and_select_amper_large_value_list_in_run_window.
        '''
        iarun_obj.select_amper_value(self, field_name, value_list=select_value_list, Search=True)
    
    def select_and_verify_amper_small_value_list_in_run_window(self, field_name, select_value_list, expected_small_value_list):
        '''
        Desc:-This function is used to select and verify amper_small_value_list_in_run_window.
        '''
        iarun_obj.select_amper_value(self, field_name, value_list=select_value_list, long_value_set=False, verify_small_value_list=expected_small_value_list)
        
    def select_amper_menu_in_run_window(self, item_name):
        '''
        Desc:-This function is used to select amper_menu_in_run_window.
        '''
        iarun_obj.select_amper_menu(self, item_name)
        
    def select_combo_item_in_infoapps_left_panel(self, label_name, item_name, top_panel=False):
        '''
        Desc:-This function is used to select combo_item_in_infoapps_left_panel.
        '''
        infoapps_obj.select_combo_item(self, label_name, item_name, top_panel=top_panel)
    
    def select_combo_item_in_infoapps_top_panel(self, label_name, item_name, top_panel=True):
        '''
        Desc:-This function is used to select combo_item_in_infoapps_left_panel.
        '''
        infoapps_obj.select_combo_item(self, label_name, item_name, top_panel=top_panel)
        
    def select_listbox_item_in_infoapps_left_panel(self, listbox_index, item_list):
        '''
        Desc:-This function is used to select_listbox_items_in_infoapps_left_panel.
        '''
        infoapps_obj.select_listbox_item(self, listbox_index, item_list)
        
    def click_run_option_button(self, button_name, top_panel=False):
        '''
        Desc:-This function is used to select run_option_button_in_infoapp_run_window.
        '''
        infoapps_obj.click_run_option_button(self, button_name, top_panel=top_panel)
    
    def click_run_option_button_in_infoapps_top_panel(self, button_name, top_panel=True):
        '''
        Desc:-This function is used to select run_option_button_in_infoapp_run_window.
        '''
        infoapps_obj.click_run_option_button(self, button_name, top_panel=top_panel)
        
    """**************************************************************************This is for Insight run window section***********************************************************************"""    
    
    def select_header_option_item_in_insight(self, header_option_item):
        '''
        Desc:-This function is used to select_header_option_item_in_insight.
        '''
        insight_obj.select_header_option_item(self, option_item_name=header_option_item)
        
    def change_chart_type_from_chart_picker_option_in_insight(self, chart_type):
        '''
        Desc:-This function is used to change_chart_type_from_chart_picker_option_in_insight.
        '''
        insight_obj.change_chart_type_from_chart_picker_option(self, chart_type)
        
    def search_and_add_field_to_query_bucket_in_insight(self, bucket_type, field_name):
        '''
        Desc:-This function is used to search_and_add_field_to_query_bucket_in_insight.
        '''
        insight_obj.search_and_add_field_to_query_bucket(self, bucket_type, field_name)
    
    def select_or_verify_more_option_menu_item_in_insight(self, menu_item, submenu_item=None, submenu=False, verify1=False, verify2=False, expected_menu_list=None, expected_submenu_list=None, msg1=None, msg2=None):
        '''
        Desc:-This function is used to select_or_verify_more_option_menu_item_in_insight.
        '''
        insight_obj.select_or_verify_more_option_menu_item(self, menu_item, submenu_item=submenu_item, submenu=submenu, verify1=verify1, verify2=verify2, expected_menu_list=expected_menu_list, expected_submenu_list=expected_submenu_list, msg1=msg1, msg2=msg2)
    
    def delete_field_in_query_bucket_container_in_insight(self, bucket_type, field_name):
        '''
        Desc:-This function is used to delete_field_in_query_bucket_container_in_insight.
        '''
        insight_obj.delete_field_in_query_bucket_container(self, bucket_type, field_name)
        
    def delete_field_in_filter_panel_container_in_insight(self, field_name):
        '''
        Desc:-This function is used to delete_field_in_filter_panel_container_in_insight.
        '''
        insight_obj.delete_field_in_filter_panel_container(self, field_name)
        
    def add_field_to_filter_container_in_insight(self, field_name, first_filter_selection=True):
        '''
        Desc:-This function is used to add_field_to_filter_container_in_insight.
        '''
        insight_obj.add_field_to_filter_container(self, field_name, first_filter_selection=first_filter_selection)
        
    def select_or_verify_filter_grid_values_in_insight(self, field_name, item_list, verify=False, expected_item_list=None, msg=None):
        '''
        Desc:-This function is used to select_or_verify_filter_grid_values_in_insight.
        '''
        insight_obj.select_or_verify_filter_grid_values(self, field_name, item_list, verify=verify, expected_item_list=expected_item_list, msg=msg)
        
    def verify_field_visible_in_query_bucket_container_in_insight(self, bucket_type, field_name, msg, visible=True):
        '''
        Desc:-This function is used to verify_field_in_query_bucket_container_in_insight.
        '''
        insight_obj.verify_field_visible_in_query_bucket_container(self, bucket_type, field_name, msg, visible=visible)  
        
    def verify_field_visible_in_filter_panel_container_in_insight(self, field_name, msg, visible=True):
        '''
        Desc:-This function is used to verify_field_in_filter_panel_container_in_insight.
        '''
        insight_obj.verify_field_visible_in_filter_panel_container(self, field_name, msg, visible=visible)
        
    def verify_add_filter_btn_visible_in_filter_panel_container_in_insight(self, msg, visible=True):
        '''
        Desc:-This function is used to verify_add_filter_btn_visible_in_filter_panel_container_in_insight.
        '''
        insight_obj.verify_add_filter_btn_visible_in_filter_panel_container(self, msg=msg, visible=visible)
        
    def click_on_blank_area_in_insight(self, insight_css='#runbox_id', coordinate_type='start'):
        '''
        Desc:-This function is used to verify_field_in_filter_panel_container_in_insight.
        '''
        insight_obj.click_on_blank_area_in_insight_chart(self, insight_css=insight_css, coordinate_type=coordinate_type)
        
    """ ************************************************* This is common for PREVIEW and RUN WINDOW Section. *******************************************"""
     
    def verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        custom_msg= msg + " : to verify number of risers available."
        ia_resultobject.verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, custom_msg)
    
    def verify_number_of_markers(self, parent_css, markers_per_segment, expected_number, msg='Step X'):
        '''
        Desc: This function is used to verify number of markers available in line chart.
        '''
        custom_msg= msg + " : to verify number of markers available in line chart."
        ia_resultobject.verify_number_of_markers(self, parent_css, markers_per_segment, expected_number, custom_msg)
    
    def verify_number_of_pie_segments(self, parent_css, risers_per_segment, expected_number, msg):
        '''
        Desc: This function is used to verify the number of pie segments.
        '''
        custom_msg= msg + ": to verify number of pie segments available."
        ia_resultobject.verify_number_of_pie_segment(self, parent_css, risers_per_segment, expected_number, custom_msg)
        
    def verify_number_of_connector_lines(self, parent_css, connector_lines_per_segment, expected_number, msg='Step X'):
        '''
        This function will verify number of connector lines in the chart. example waterfall charts
        '''
        custom_msg=msg+ " : to verify number of connector lines in the chart"
        ia_resultobject.verify_number_of_connector_lines(self, parent_css, connector_lines_per_segment, expected_number, custom_msg)
    
    def verify_arc_chart_group_label(self,run_parent_css,riser_css,Group_label_css,expected_group_label,text_alignment,msg,**kwargs):
        if 'default_move' in kwargs:
            pass
        else:
            css="#"+run_parent_css+" [class*='" + riser_css + "']"
            elem=self.driver.find_element_by_css_selector(css)
            coreutillobject.python_left_click(self, elem, 'middle')
        ia_resultobject.verify_arc_chart_group_labels(self, Group_label_css, expected_group_label,msg, text_alignment )
        
    
    def verify_tooltip_values(self,parent_id,raiser_class,expected_tooltip_list,msg,**kwargs):
        visual_resobj.verify_default_tooltip_values(self, parent_id, raiser_class, expected_tooltip_list,msg,**kwargs)
    
    def click_chart_animate_button(self,button_css="rect[class='animateButton']"):
        '''
        Desc: This function is used to verify the animate button
        '''
        ia_resultobject.click_animate_button(self, button_css)
        
    def verify_animate_start_position(self,slider_css="rect[class='sliderBody']", coordinate_type='top_left',msg="Step X: Verify animate button is in Start position."):
        '''
        Desc: This function is used to verify the animate button is in Starting position of the slider.
        '''
        ia_resultobject.verify_animate_button_position(self, slider_css, coordinate_type, msg)
    
    def verfiy_animate_end_position(self,slider_css="rect[class='sliderBody']",coordinate_type='bottom_right',msg="Step X: Verify animate button is in End position."):
        '''
        Desc: This function is used to verify the animate button is in end position of the slider
        '''
        ia_resultobject.verify_animate_button_position(self, slider_css, coordinate_type,msg)
    
    def verify_animate_slider(self,slider_css,handle_css,msg):
        ''' 
        Desc: This function used to verify the animate button is present in the chart
        usage:-verify_animate_slider("rect[class='sliderBody']", "rect[class='sliderHandle']","Step03:verify animate slider button")
        '''
        ia_resultobject.verify_chart_animate_slider(self, slider_css, handle_css, msg)
        
    def verify_autolink_tooltip_submenu(self, raiser_class, drill_menu_item, expected_tooltip_list, msg, parent_id="jschart_HOLD_0", wait_time=0):
        ''' 
        Desc: This function used to hover on chart riser and select tooltip menu to verify submenu of tooltip.
        usage:-verify_autolink_tooltip_submenu("riser!s4!g25!mbar!r0!c0!", "Drill down to", ['Store Business Sub Region', 'Sale Year/Quarter'], "Step 02.01 : Verify submenu tooltip")
        '''
        ia_resultobject.verify_autolink_tooltip_submenu(self, parent_id, raiser_class, drill_menu_item, expected_tooltip_list, msg, wait_time)
    
    def define_compute_dialog(self):
        """
        Description : This method returns DefineCompute class object. Using this object we can call all define and compute dialog dialog related methods 
        """
        return DefineCompute(self.driver)
    
    def click_on_marker(self,parent_css,risier_css):
        """Description:This used to click on marker in chart
        @requires: For drilldown functionality we will click on marker it navigates the new webpage
        @params: parent_css:#jschart_HOLD_0
        @params: riser_or_marker_element:marker!s0!g3!mmarker
        usage:click_on_marker("#jschart_HOLD_0","marker!s0!g3!mmarker")
        """
        visual_resobj.click_on_marker(self, parent_css, riser_or_marker_element=risier_css)
    
    def verify_sparkline_chart_tooltip(self, tooltip, step_num, parent_css="#jschart_HOLD_0", chart_location='middle', xoffset=0, yoffset=0):
        """
        Description : Verify Spark Line chart tooltip
        Usage : verify_sparkline_chart_tooltip('14.02', "01.02")
        """
        visual_resobj.verify_sparkline_chart_tooltip(self, tooltip, step_num, parent_css, chart_location, xoffset, yoffset)
        
    """ ********************************************** Verification points for different chart types pls (DONOT call this as fn call in the script)*************************************************************"""
    def __gauge_chart_run_window_verification_points(self):
        self.verify_chart_title("Gross Profit Year to YearLondon", 'run', "Step07.01: Verify chart title in run window")
        totalLabel=['$1M', '$1M']
        self.verify_data_labels('jschart_HOLD_0',totalLabel,'Step 07:02: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        groupLabel=['2015','2016']
        self.verify_data_labels('jschart_HOLD_0',groupLabel,'Step 07:03: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
        gaugelabels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '1.6M', '0', '0.4M', '0.8M', '1.2M', '1.6M', '1.6M']
        self.verify_data_labels('jschart_HOLD_0',gaugelabels,'Step 07:04: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
        self.verify_number_of_chart_segment('jschart_HOLD_0', 10, "Step 07:05: verify the Gauge range", custom_css=".chartPanel path[class*='gaugeRange']")
        self.verify_number_of_chart_segment('jschart_HOLD_0', 2, "Step 07:06: verify the needle", custom_css=".chartPanel path[class*='needle']")
        self.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mneedle", "cerulean_blue", "Step07:07: Verify needle blue color")
        color_css1="path.gaugeRange:nth-child(1)"
        color_css3="path.gaugeRange:nth-child(3)"
        color_css5="path.gaugeRange:nth-child(5)"
        self.verify_chart_color('jschart_HOLD_0',None, 'pink', 'Step07:08.1: Verify Gauge green color',custom_css=color_css1)
        self.verify_chart_color('jschart_HOLD_0',None, 'yellow1', 'Step07:08.2: Verify Gauge green color',custom_css=color_css3)
        self.verify_chart_color('jschart_HOLD_0',None, 'lime', 'Step07:08.3: Verify Gauge green color',custom_css=color_css5)
        
    def __gauge_chart_preview_window_verification_points(self):
        self.verify_data_labels('TableChart_1',['$0M'],'Step 06:06:: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        self.verify_data_labels('TableChart_1',['2015'],'Step 06:07: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
        labels=['0', '20', '40', '60', '80', '100', '120']
        self.verify_data_labels('TableChart_1',labels,'Step 06:08: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
        self.verify_number_of_chart_segment('TableChart_1', 5, "Step 06:05: verify the Gauge", custom_css=".chartPanel path[class*='gaugeRange']")
        self.verify_number_of_chart_segment('TableChart_1', 1, "Step 06:06: verify the Gauge", custom_css=".chartPanel path[class*='gaugeRange']")
        
    def __pie_ring_chart_run_window_verification_points(self):
        self.verify_riser_pie_labels_and_legends('jschart_HOLD_0',  ['Revenue'], "Step02.1:",custom_css="text[class*='pieLabel']") 
        self.verify_legends_in_run_window( ['Product Category', 'Accessories'], "#"+'jschart_HOLD_0', 5, 'Step02.2: Verify pie Legend List in run window')
        self.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['1.1B'], "Step02.3: Verify pie total label values in run window",custom_css="text[class^='totalLabel!g']",same_group=True)
        self.verify_chart_color('jschart_HOLD_0', "riser!s0!g0!mwedge", "bar_blue1", "Step02.4: Verify first pie segment color in run window")
        self.verify_number_of_chart_segment('jschart_HOLD_0', 7, "Step02.5: Verify number of pie segments in run window")
    
    def __pie_ring_chart_preview_window_verification_points(self):
        self.verify_riser_pie_labels_and_legends( 'pfjTableChart_1', ['Revenue'], "Step06.1:",custom_css="text[class*='pieLabel']") 
        self.verify_legends_in_run_window( ['Product Category', 'Accessories'], "#"+ 'pfjTableChart_1', 5, 'Step06.2: Verify pie Legend List in preview')
        self.verify_riser_pie_labels_and_legends( 'pfjTableChart_1', ['1.1B'], "Step06.3: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        self.verify_chart_color( 'pfjTableChart_1', "riser!s0!g0!mwedge", "bar_blue1", "Step06.4: Verify first pie segment color in preview")
        self.verify_number_of_chart_segment( 'pfjTableChart_1', 7, "Step06.5: Verify number of pie segments in preview", custom_css="[class*='riser!s']")
        
    def __line_chart_run_window_verification_points(self):
        self.verify_x_axis_title_in_run_window(['Sale Month'], msg='Step02:01a: Verify x-axis title')
        self.verify_y_axis_title_in_run_window(['Gross Profit'], msg="Step02:01b: Verify y-axis title")
        self.verify_legends_in_run_window(['Accessories'], msg='Step02:02: Verify Legend List in run window')
        self.verify_x_axis_label_in_run_window(['1','2'], msg="Step02:03: Verify x-axis label")
        self.verify_y_axis_label_in_run_window(['0', '10K'], msg="Step02:04: Verify y-axis label")
        self.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", attribute='stroke', msg="Step02:05: Verify line color")
        self.verify_number_of_chart_segment('jschart_HOLD_0', 91, "Step02:06: Verify number of segments in run window")
        self.verify_tooltip_in_run_window("marker!s4!g5!mmarker!", ['Sale Yer:2018'], "Step07:07: Verify tooltip values", use_marker_enable=True)
        
    def __line_chart_preview_window_verification_points(self):
        self.verify_x_axis_title_in_run_window(['Sale Month'], "#TableChart_2", msg='Step06.1a')
        self.verify_y_axis_title_in_run_window(['Gross Profit'], "#TableChart_2", msg='Step06.1b')
        self.verify_x_axis_label_in_preview(['1','2'], parent_css="#TableChart_2", msg="Step06:02a: Verify xaxis label")
        self.verify_y_axis_label_in_preview(['0', '10K'], parent_css="#TableChart_2", msg="Step06:02b: Verify yaxis label")
        self.verify_legends_in_preview(['Accessories'], "#TableChart_2", msg='Step06:03: Verify Legend List in run window')
        self.verify_chart_color_using_get_css_property_in_preview("[class='marker!s0!g0!mmarker!']", "white", "#TableChart_2", msg="Step06:04: Verify chart color")
        self.verify_number_of_chart_segment("TableChart_2", 7, "Step06:05: Verify number of pie segments in preview", custom_css= "[class*='riser!s']")
        self.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#TableChart_2", attribute='stroke', msg='Step06:06: Verify chart color in preview')
        
    def __bar_chart_run_window_verification_points(self):
        self.verify_x_axis_title_in_run_window(['Product Category'], msg='Step 02:00: Verify x-axis title')
        self.verify_y_axis_title_in_run_window(['Revenue'], msg="Step 02:01: Verify y-axis title")
        self.verify_legends_in_run_window(['Accessories'], msg='Step 02:02: Verify pie Legend List in run window')
        self.verify_x_axis_label_in_run_window(['Accessories','Camcorder'], msg="Step 02:03: Verify x-axis label")
        self.verify_y_axis_label_in_run_window(['0%', '20%'], msg="Step 02:04: Verify x-axis label")
        self.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mbar!']", "bar_blue", attribute='fill', msg="Step 02:05: Verify line color")
        self.verify_number_of_chart_segment('jschart_HOLD_0', 28, "Step 02:06: Verify number of chart segments in run window")
        self.verify_number_of_risers("#jschart_HOLD_0 rect", 28, 1, msg="Step 02:07: Verify number of risers")
        self.verify_tooltip_in_run_window("riser!s1!g2!mbar", ['Category:Accessories'], "Step 02:08: Verify tooltip")
    
    def __bar_chart_preview_window_verification_points(self):
        self.verify_x_axis_label_in_preview(['Accessories'], parent_css='#TableChart_2', msg="Step 05:02: Verify xaxis label")
        self.verify_y_axis_label_in_preview(['0%', '20%'], parent_css='#TableChart_2', msg="Step 05:03: Verify yaxis label")
        self.verify_chart_color_using_get_css_property_in_preview("riser!s1!g2!mbar", "bar_blue", parent_css='#TableChart_2', msg="Step 05:04: Verify chart color")
        self.verify_number_of_chart_segment('#TableChart_2', 7, "Step 05:05: Verify number of pie segments in preview", custom_css="[class*='riser!s']")
        self.verify_legends_in_preview(['Accessories'], parent_css='#TableChart_2', msg="Step 05:06:Verify legends in preview")
        self.verify_number_of_risers('#TableChart_2 rect', 7, 1, msg="Step 05:07:Verify number of risers in preview chart")
        
    def __heatmap_preview_window_verification_points(self):
        self.verify_x_axis_title_in_run_window(['Sale Quarter', 'Store Region'], "#jschart_HOLD_0", msg='Step03.1')
        self.verify_number_of_chart_segment("jschart_HOLD_0", 16, "Step03.2: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        self.verify_x_axis_label_in_run_window(['1', '2'], "#jschart_HOLD_0", msg='Step03.3')
        self.verify_z_axis_label_in_run_window(['EMEA'], "#jschart_HOLD_0", msg='Step03.4')
        self.verify_tooltip_in_run_window("riser!s1!g1!mbar",  ['AVE Discount:$19.70'], "Step03.5", "#jschart_HOLD_0", move_to_tooltip=True)
        self.verify_chart_color("jschart_HOLD_0",  "riser!s1!g1!mbar", 'reef1', "Step03.6: Verify chart color")
        
    def __heatmap_run_window_verification_points(self):
        self.verify_x_axis_title_in_run_window(['Sale Quarter', 'Store Region'], "#pfjTableChart_2", msg='Step07.1')
        self.verify_number_of_chart_segment('pfjTableChart_2', 1, "Step07.2: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        self.verify_x_axis_label_in_run_window(['1', '2'], "#pfjTableChart_2", msg='Step07.3')
        self.verify_z_axis_label_in_run_window(['EMEA'], "#pfjTableChart_2", msg='Step07.4')
        self.verify_chart_color("pfjTableChart_2", "riser!s1!g1!mbar", 'sandy_brown1', "Step07.5: Verify chart color")
    
    def __bubblemap_run_widow_verification_points(self):
        self.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['Store Business Region'], 'Step02.1. Verify Legend title', custom_css="[class*='legend-title']", same_group=True)
        self.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['EMEA', 'North America'], 'Step02.2: Verify Legend List', custom_css="[class*='legend-labels']", same_group=True)
        self.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['Revenue'], 'Step02.3: Verify Size Legend title', custom_css="[class*='sizeLegend-title']", same_group=True)
        self.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['327.8M', '164M'], 'Step02.4: Verify Size Legend List', custom_css="[class*='sizeLegend-labels']", same_group=True)
        self.verify_map_scale_in_run_window('jschart_HOLD_0', ['1000km', '600mi'], 'Step02.5: Verify map scale', custom_css=".esriScalebarLabel")
        self.verify_chart_color('jschart_HOLD_0', "riser!s1!g4!mmarker", 'pale_green', 'Step02.6: Verify map color')
        self.verify_number_of_circles_in_run_window(86,87,"Step02.7: Verify number of circles", '#jschart_HOLD_0')
        
    def __arc_chart_run_window_verification_points(self):
        self.verify_x_axis_label_in_run_window(['Oceania','South America','EMEA','North America'], xyz_axis_label_css=" g.group-labels text", msg="Step 03:01: Verify x-axis label")
        self.verify_y_axis_label_in_run_window(['0','50M','100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M', '500M', '550M','600M'], xyz_axis_label_css=" g text.label", msg="Step 03:02: Verify y-axis label")
        self.chart_obj.verify_chart_color_using_get_css_property_in_run_window(" .chartPanel .group-main path[class*='riser!s0!g0!mbar!']", "dark_green2", attribute='fill', msg="Step 03:03: Verify chart colour")
        self.verify_active_chart_tooltip("jschart_HOLD_0","riser!s0!g3!mbar!",["South America: 27.3M"],"Step04.01: Verify tooltip values")
        self.verify_arc_chart_group_label("jschart_HOLD_0","riser!s0!g3!mbar!","g.group-value>text",'27.3M',"middle","Step04.01: Verify arc chart group label values", default_move='true')
        
