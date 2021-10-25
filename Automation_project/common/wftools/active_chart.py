from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.core_utility import CoreUtillityMethods as coreutillobject
from common.pages.ia_metadata import IA_Metadata as metaobject
from common.pages.visualization_metadata import Visualization_Metadata as visual_metaobj
from common.pages.ia_miscelaneous import IA_Miscelaneous as miscelaneousobject
from common.pages.active_miscelaneous import Active_Miscelaneous as activemiscelaneousobject
from common.pages.ia_ribbon import IA_Ribbon as ribbonobject
from common.pages.ia_resultarea import IA_Resultarea as ia_resultobject
from common.pages.active_tools import Active_Tools as active_toolobj
from common.pages.active_chart_rollup import Active_Chart_Rollup as active_chart_rollupobj
from common.pages.visualization_ribbon import Visualization_Ribbon as visual_ribbonobj

        
class Active_Chart(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    run_parent_css="#MAINTABLE_wbodyMain0"
    preview_parent_css="#TableChart_1"
    
    def __init__(self, driver):
        super(Active_Chart, self).__init__(driver)
        
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
            
    def invoke_ia_chart_tool_using_api(self, master, mrid=None, mrpass=None):
        '''
        Desc:- This function is used to switch to a new window.
        '''
        miscelaneousobject.invoke_ia_tool_using_api(self, tool='chart', master=master, mrid=mrid, mrpass=mrpass)
        default_riser_css=".chartPanel rect[class^='riser!']"
        miscelaneousobject.wait_for_object(self, default_riser_css, option='number', expected_number=25, time_out=60)
        
    def invoke_chart_tool_using_api(self, master, tool='chart', mrid=None, mrpass=None):
        '''
        Desc:- This function is used to switch to a new window.
        '''
        miscelaneousobject.invoke_ia_tool_using_api_(self, tool=tool, master=master, mrid=mrid, mrpass=mrpass)
        default_riser_css=".chartPanel rect[class^='riser!']"
        miscelaneousobject.wait_for_object(self, default_riser_css, option='number', expected_number=25, time_out=60)
        
    def invoke_chart_in_edit_mode_using_api(self, fex, mrid=None, mrpass=None):
        '''
        Desc:- This function is used to switch to a new window.
        '''
        miscelaneousobject.invoke_ia_tool_in_edit_mode_using_api(self, fex, tool='chart', mrid=mrid, mrpass=mrpass)
    
    def invoke_chart_in_run_mode(self, webdriver_element):
        pass
    
    def run_fex_using_api_url(self, folder_name, fex_name=None, mrid=None, mrpass=None, home_page='New', run_chart_css="#MAINTABLE_wbody0", no_of_element=1,wait_time=0):
        '''
        Desc:- This function will run report/chart using api link and sign in as user defined in config file
        Usage: report_obj.run_fex_using_api(subfolder_name='Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass')
        '''
        wait_time=self.chart_long_timesleep if wait_time==0 else wait_time
        miscelaneousobject.run_fex_using_api(self, folder_name, fex_name=fex_name, mrid=mrid, mrpass=mrpass, home_page=home_page)
        Active_Chart.wait_for_number_of_element(self, run_chart_css, no_of_element, wait_time)
    
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
    
    def click_any_bibutton_in_dialog(self, dialog_css="[id^='BiDialog'][style*='inherit']", btn_name='OK'):
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
    
    def save_as_chart_from_menubar(self, file_name, file_type=None, folder_location_to_save=None):
        '''
        Desc: This is used to save visualization from menubar.
        :usage save_as_visualization_from_menubar('C2346054')
        '''
        ribbonobject.select_ia_application_menu_item(self, 'save_as')
        miscelaneousobject.ibfs_save_as(self, file_name, file_type=file_type, folder_location_to_save=folder_location_to_save)
    
    def select_chart_type(self, chart_name):
        '''
        Desc: This is used to select chart type.
        '''
        ribbonobject.select_ia_ribbon_item(self, 'Format', chart_name)
        
    def select_other_chart_type(self, chart_type, Chart_name, chart_index, starting_visibility_index=None, close_dialog='ok'):
        '''
        Desc: This is used to select chart type
        Params: chart_type='bar','line','area','pie','x_y_plots','threed','stock','special','html5','map','html5_extension'.
        Params: Chart_name='vertical_clustered_bars', 'vertical_absolute_line'...(The name displayed when you hover over the chart image, with underscores, check the locator file)
        Params: chart_index=1, 2, 3...
        Params: starting_visibility_index=0, 1, 2, 3...(The index of the chart image which is visible)
        '''
        ribbonobject.select_other_chart_types(self, chart_type, Chart_name, chart_index, starting_visibility_index=starting_visibility_index, close_dialog=close_dialog)
        
    def change_output_format_type(self, output_format_type, location='Home'):
        '''
        Desc:- This function is used to change the output format
        '''
        visual_ribbonobj.change_output_format_type(self, output_format_type, location)
        
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
    
    def drag_field_from_data_tree_to_query_pane(self, field_name, field_position, bucket_name, bucket_position=1):
        '''
        Desc:- This function is used to drag and drop data field to the specified bucket in query tree.
        :param - field_position: 1,2 .. (first match is 1)
        :param - bucket_position: 1,2 .. (first match is 1)
        :usage drag_field_from_data_tree_to_query_pane("PRICE_DOLLARS_BIN_1",1,"Model",1)
        '''
        metaobject.drag_and_drop_from_data_tree_to_query_tree(self, field_name, field_position, bucket_name,bucket_position)
    
    def drag_field_within_query_pane(self, source_item_name, target_item_name):
        '''
        Desc:- This function is used to drag and drop data field within query tree.
        :usage drag_field_within_query_pane('Discount','Color')
        '''
        metaobject.drag_and_drop_within_query_tree(self, source_item_name, target_item_name)  
    
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
        
    def verify_query_field_context_menu(self, field_name, field_position, context_menu_list, msg):
        '''
        Desc:- This function is used to verify the right click context menu of a Query field item
        '''
        metaobject.verify_querytree_context_menu(self, field_name, field_position, context_menu_list, msg)
    
    def verify_query_field_checked_context_menu(self, field_name, field_position, context_menu_list, msg):
        '''
        Desc:-This fucntion is used to verify the checked context menu
        '''
        metaobject.verify_querytree_context_menu(self, field_name, field_position, context_menu_list, msg, verify_type='ticked')
    
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
            
    def chart_rollup_tool_drag_drop_items(self, table_id, from_column, item_name, item_position, to_column, to_row_num, **kwargs):
        '''
        Desc:-This function is used to drag and drop items in chart rollup tool
        active_chartobj.chart_rollup_tool_drag_drop_items('charttoolt2', 'Columns', 'Product', 1, 'Group By', 1)
        '''
        active_toolobj.chart_rollup_tool_drag_drop_items(self, table_id, from_column, item_name, item_position, to_column, to_row_num, **kwargs)
        
    def select_advance_chart(self, popup_id, chart_name, index=0):
        '''
        Desc:-This function is used to select chart from charts tab:
        active_chart_obj.select_advance_chart('wall1', 'bar')
        '''
        active_chart_rollupobj.select_advance_chart(self, popup_id, chart_name, chart_index=index)
    
    def create_new_item(self, popup_id, select_path, index=0):
        '''
        Desc:-This function is used to select menu item from active chart toolbar using more options dropdown)
        active_chart_obj.create_new_item_(self, 'MAINTABLE_0', 'Restore Original')
        '''
        active_chart_rollupobj.create_new_item_(self, popup_id, select_path, parent_popup_index=index)
        
    def close_active_chart_popup_dialog(self, popup_index):
        '''
        Desc:- This function is used to close the popup dialog
        activemiscelaneousobject.close_popup_dialog(1)
        '''
        activemiscelaneousobject.close_popup_dialog(self, popup_index)
    
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
    
    def verify_pie_label_in_single_group_in_preview(self, expected_label_list, parent_css=preview_parent_css, label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        custom_msg=msg + ": Verify Pie Label in a single Group."
        ia_resultobject.verify_pie_label_in_single_group(self, expected_label_list, parent_css, label_css, custom_msg)
    
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
    
    def right_click_on_chart_bar_perview_and_select_context_menu(self, riser_css, context_menu_path, parent_css=run_parent_css):
        '''
        Desc:-This function is used to right click on the bar in preview and select context menu.
        '''
        ia_resultobject.right_click_on_chart_bar_or_line_in_perview_and_select_context_menu(self, parent_css, riser_css, context_menu_path)
    
    def right_click_on_chart_bar_perview_and_verify_context_menu(self, riser_css, expected_list, step_number, parent_css=run_parent_css, context_menu_path=None, compare_type='asequal'):
        '''
        Desc:-This function is used to right click on the bar/line in chart preview and verify context menu.
        '''
        ia_resultobject.right_click_on_chart_bar_or_line_in_perview_and_verify_context_menu(self, parent_css, riser_css, expected_list, step_number, context_menu_path=context_menu_path, compare_type=compare_type)
        
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
    
    def verify_x_axis_label_and_length_in_run_window(self, expected_label_list, parent_css=run_parent_css, xyz_axis_label_css="svg > g text[class^='xaxis'][class*='labels']", msg='Step X'):
        custom_msg=msg + ' : Verify X-axis label.'
        ia_resultobject.verify_xyz_labels_and_length(self, expected_label_list, parent_css, xyz_axis_label_css, msg=custom_msg)
    
    def verify_y_axis_label_and_length_in_run_window(self, expected_label_list, parent_css=run_parent_css, xyz_axis_label_css="svg > g text[class^='yaxis-labels']", msg='Step X'):
        custom_msg=msg + ' : Verify Y-axis label.'
        ia_resultobject.verify_xyz_labels_and_length(self, expected_label_list, parent_css, xyz_axis_label_css, msg=custom_msg)
    
    def verify_z_axis_label_and_length_in_run_window(self, expected_label_list, parent_css=run_parent_css, xyz_axis_label_css="svg > g text[class^='zaxis'][class*='labels']",  msg='Step X'):
        custom_msg=msg + ' : Verify Z-axis label.'
        ia_resultobject.verify_xyz_labels_and_length(self, expected_label_list, parent_css, xyz_axis_label_css, msg=custom_msg)
    
    def verify_rows_label_in_run_window(self, expected_label_list, parent_css=run_parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Rows label.'
        ia_resultobject.verify_ia_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='rows', label_length=label_length, msg=custom_msg)
    
    def verify_column_label_in_run_window(self, expected_label_list, parent_css=run_parent_css, label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Columns label.'
        ia_resultobject.verify_ia_row_and_column_labels(self, expected_label_list, parent_css, matrix_type='column', label_length=label_length, msg=custom_msg)
    
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
                        
    def verify_pie_label_and_value_in_multiple_groups_in_run_window(self, expected_label_list, expected_total_label_list, parent_css=run_parent_css, label_css="text[class^='pieLabel!g']", msg='Step X'):
        '''
        Desc: This function is used to verify pie labels and total labels in multiple groups.
        '''
        custom_msg1=msg + ": Verify Pie Labels in multiple Groups."
        custom_msg2=msg + ": Verify Pie Label total values in multiple Groups."
        ia_resultobject.verify_pie_label_and_value_in_multiple_groups(self, expected_label_list, expected_total_label_list, parent_css, label_css, custom_msg1, custom_msg2)
    
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
    
    """ ************************************************* This is common for PREVIEW and RUN WINDOW Section. *******************************************"""
     
    def verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        custom_msg= msg + " : to verify number of risers available."
        ia_resultobject.verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, custom_msg)
        
    def verify_number_of_risers_in_preview(self, tag_name, risers_per_segment, expected_number, parent_css=preview_parent_css, msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        riser_css=parent_css+" .chartPanel "+ tag_name +"[class^='riser']"
        total_risers=len(self.driver.find_elements_by_css_selector(riser_css))
        actual_number=int(total_risers/risers_per_segment)
        utillobject.asequal(self, expected_number, actual_number, msg)
    
    def verify_number_of_risers_in_run_window(self, tag_name, risers_per_segment, expected_number, parent_css=run_parent_css, msg='Step X'):
        '''
        Desc: This function is used to verify pie labels within a single group.
        '''
        riser_css=parent_css+" .chartPanel "+ tag_name +"[class^='riser']"
        total_risers=len(self.driver.find_elements_by_css_selector(riser_css))
        actual_number=int(total_risers/risers_per_segment)
        utillobject.asequal(self, expected_number, actual_number, msg)
    
    def verify_number_of_pie_segments(self, parent_css, risers_per_segment, expected_number, msg):
        '''
        Desc: This function is used to verify the number of pie segments.
        '''
        custom_msg= msg + ": to verify number of pie segments available."
        ia_resultobject.verify_number_of_pie_segment(self, parent_css, risers_per_segment, expected_number, custom_msg)

    """ **********************This is specific to RESULTAREA Section for Active Chart*************************"""
    
    def verify_chart_title(self, expected_chart_title, msg='Step X', parent_css=preview_parent_css, title_css=None):
        '''
        Desc:- Verify chart title during run time.
        '''
        custom_msg=msg + ": Verify chart Title."
        activemiscelaneousobject.verify_chart_title_(self, parent_css, expected_chart_title, custom_msg, title_css=title_css)
        
    """****************************************ACTIVE CHART TOOLBAR ITEMS******************************************************************************"""
    
    def verify_active_chart_toolbar(self, expected_toolbar_menu_list, msg='Step X', parent_css=run_parent_css, verify_toolbar_title=True, verify_toolbar_text=True, toolbar_title_css="[title]", toolbar_text_css="[id*='SUM']"):
        '''
        Desc:- Verify Active tool-bar menu title and text name.
        '''
        custom_msg=msg + ": Verify chart Title."
        activemiscelaneousobject.verify_acitive_chart_toolbar(self, parent_css, expected_toolbar_menu_list, custom_msg, verify_toolbar_title=verify_toolbar_title, verify_toolbar_text=verify_toolbar_text, toolbar_title_css=toolbar_title_css, toolbar_text_css=toolbar_text_css)
        
    def click_chart_menu_bar_items(self, window_id, item_index):
        '''
        Desc:- This function is used to select active chart toolbar items
        '''
        active_chart_rollupobj.click_chart_menu_bar_items(self, window_id, item_index)
    
    def verify_items_in_advanced_chart_menu(self, expected_list, comparison_type, msg):
        '''
        Description : Verify all the items in the advanced chart menu
        usage: verify_items_in_advanced_chart_menu(['Bar'], 'asin', 'Step 3.1: Verify bar under the advanced chart menu') 
        '''
        active_chart_rollupobj.verify_advanced_chart_items(self, expected_list, comparison_type, msg)
        
    def verify_menu_bar_popup_values(self,window_id, menu_item_index, expected_list, msg, popup_path=''):
        '''
        Description: Verify the popup values under the menu bar
        usage: verify_menu_bar_popup_values('MAINTABLE_wmenu0', 0, ['Chart/Rollup Tool', 'Restore Original'],"step 6: Verify the popup")
        '''
        active_chart_rollupobj.select_chartmenubar_option(self, window_id, 0, popup_path , elem_index=menu_item_index, custom_css='cpop', verify=True, expected_list=expected_list, msg=msg)
        
    def select_chart_rollup_tab(self, tab_name):
        '''
        Description: Used to click the item in chart/Rollup tool
        usage: click_chart_rollup_items('Charts')
        '''
        active_chart_rollupobj.click_chart_rollup_tool_items(self,tab_name)
    
    def move_active_popup_window(self, index, xoffset, yoffset, **kwargs):
        activemiscelaneousobject.move_active_popup(self, index=index, x=xoffset, y=yoffset, **kwargs)
        