from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.designer.chart import SetColorRangesDialog
from common.pages.designer.chart import ControlsMenuDialog
from common.pages.ia_miscelaneous import IA_Miscelaneous
from common.pages.ia_resultarea import IA_Resultarea
from common.pages.designer_metadata import Designer_Metadata
from common.pages.designer_metadata import Designer_Insight_Metadata
from common.pages.wf_reporting_object import Wf_Reporting_Object
from common.pages.page_designer_design import PageDesignerDesign as pd_design
from common.pages.page_designer_preview import PageDesignerPreview as pd_preview
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.pages.wf_mainpage import Wf_Mainpage
from common.lib.webfocus.resource_dialog import Resource_Dialog as resc_obj
from common.wfcomponent import dataformatdialog
from common.pages import dataformat_dialog

class Designer_Chart(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    run_parent_css = "#jschart_HOLD_0"
    preview_parent_css = "div.wfc-bc-output-div"
    
    def __init__(self, driver):
        super(Designer_Chart, self).__init__(driver)
        self._utillity = UtillityMethods(self.driver)
        self._miscelaneousobject = IA_Miscelaneous(self.driver)
        self._ia_resultobject = IA_Resultarea(self.driver)
        self._designer_metadataobj = Designer_Metadata(self.driver)
        self._reporting_obj = Wf_Reporting_Object(self.driver)
        self._pd_previewobj = pd_preview(self.driver)
        self._pd_designobj = pd_design(self.driver)
        self._wf_main_page_obj = Wf_Mainpage(self.driver)
        self._resc_obj = resc_obj(self.driver)
        self._data_format_dialog = dataformatdialog.DataFormatDialog(self.driver)
        self._alpha_type = dataformatdialog.AlphaType(self.driver)
        self._numeric_type = dataformatdialog.NumericType(self.driver)
        self._data_type = dataformatdialog.DateType(self.driver)
        self._custom_type = dataformatdialog.CustomType(self.driver)
        self._core_utils = CoreUtillityMethods(self.driver)
        
    """************************************************************* This is for Common Section. ***************************************************************************************"""
    
    def wait_for_number_of_element(self, element_css, expected_number=None, time_out=60):
        self._miscelaneousobject.wait_for_object(element_css, 'number', expected_number=expected_number, time_out=time_out)
        
    def wait_for_visible_text(self, element_css, visble_element_text=None, time_out=60):
        self._miscelaneousobject.wait_for_object(element_css, 'text', visble_element_text=visble_element_text, time_out=time_out)
    
    def invoke_designer_chart_using_api(self, master, tool='chart', mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.invoke_designer_tool_using_api(tool=tool, master=master, mrid=mrid, mrpass=mrpass, folder_path=folder_path)
    
    def invoke_designer_using_api(self, master_file, mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.invoke_designer_using_api(master_file, mrid, mrpass, folder_path)
    
    def edit_chart_with_designer_using_api(self, fex_file, mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.edit_fex_with_designer_using_api(fex_file, mrid, mrpass, folder_path)
    
    def edit_page_with_designer_using_api(self, fex_file, mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.edit_page_with_designer_using_api(fex_file, mrid, mrpass, folder_path)
                                                    
    def invoke_designer_chart_in_edit_mode_using_api(self, fex, tool='chart', mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.invoke_designer_tool_in_edit_mode_using_api(fex=fex, tool=tool, mrid=mrid, mrpass=mrpass, folder_path=folder_path)
        
    def invoke_ia_using_api(self, master, tool='chart', mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.invoke_ia_tool_using_api(tool=tool, master=master, mrid=mrid, mrpass=mrpass, folder_path=folder_path)
        
    def run_designer_chart_using_api(self,fex,mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.run_designer_tool_using_api(fex=fex,mrid=mrid, mrpass=mrpass, folder_path=folder_path)
    
    def run_designer_workbook_using_api(self,fex,mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.run_designer_tool_using_api(fex=fex,mrid=mrid, mrpass=mrpass, folder_path=folder_path, tool='workbook')
    
    def invoke_ia_in_edit_mode_using_api(self, fex, tool='chart', mrid=None, mrpass=None, folder_path=None):
        self._designer_metadataobj.invoke_ia_tool_in_edit_mode_using_api(fex=fex, tool=tool, mrid=mrid, mrpass=mrpass, folder_path=folder_path)
        
    def api_logout(self):
        self._utillity.wf_logout()
        
        
    """******************************************************************** This is common for Metadata Section*************************************************************************************"""
    def drag_measure_field_to_query_bucket(self, data_field_path, bucket_name, bucket_location='bottom_middle'):
        """
        Description : Drag the measure data field and drop into specified query bucket
        :Usage - drag_measure_field_to_query_bucket('CAR', 'Vertical')
        """
        self._designer_metadataobj.drag_data_field_to_query_bucket('measure', data_field_path, bucket_name, bucket_location)
    
    def drag_measure_field_to_canvas(self,data_field_path,location="middle"):
        """
        Description : Drag the measure data field and drop into Live preview canvas
        :Usage - drag_measure_field_to_canvas('CAR')
        """
        self._designer_metadataobj.drag_data_field_to_canvas('measure', data_field_path, location=location)
    
    def drag_measure_field_to_query_bucket_field(self, data_field_path, bucket_name, bucket_field, bucket_field_pos=1, bucket_field_loc='bottom_middle'):
        """
        Description : Drag measure field and drop into specified query bucket filed
        :Usage - drag_measure_field_to_query_bucket_field('SEATS', 'Vertical', 'SALES')
        """
        self._designer_metadataobj.drag_data_field_to_query_bucket_field('measure', data_field_path, bucket_name, bucket_field, bucket_field_pos, bucket_field_loc)
    
    def drag_dimension_field_to_query_bucket(self, data_field_path, bucket_name, bucket_location='bottom_middle'):
        """
        Description : Drag the dimension data field and drop into specified query bucket
        :Usage - drag_dimension_field_to_query_bucket('SALES', 'Vertical')
        """
        self._designer_metadataobj.drag_data_field_to_query_bucket('dimension', data_field_path, bucket_name, bucket_location)
    
    def drag_dimension_field_to_canvas(self,data_field_path,location="middle"):
        """
        Description : Drag the measure data field and drop into Live preview canvas
        :Usage - drag_dimension_field_to_canvas('CAR')
        """
        self._designer_metadataobj.drag_data_field_to_canvas('dimension', data_field_path, location=location)
    
    def drag_dimension_field_to_query_bucket_field(self, data_field_path, bucket_name, bucket_field, bucket_field_pos=1, bucket_field_loc='bottom_middle'):
        """
        Description : Drag dimension field and drop into specified query bucket filed
        :Usage - drag_dimension_field_to_query_bucket_field('CAR', 'Vertical', 'MODEL')
        """
        self._designer_metadataobj.drag_data_field_to_query_bucket_field('dimension', data_field_path, bucket_name, bucket_field, bucket_field_pos, bucket_field_loc)
    
    def drag_query_bucket_field_to_another_query_bucket(self, source_bucket, source_field, target_bucket, source_field_pos=1, target_bucket_loc='bottom_middle'):
        """
        Description : Drag the query bucket field to another query bucket
        :Usage - drag_query_bucket_field_to_another_query_bucket('Vertical', 'SALES', 'Color')
        """
        self._designer_metadataobj.drag_query_bucket_field_to_another_query_bucket(source_bucket, source_field, target_bucket, source_field_pos, target_bucket_loc)
        
    def drag_query_bucket_field_to_another_query_bucket_field(self, source_bucket, source_field, target_bucket, target_field, source_field_pos=1, target_field_pos=1, target_field_loc='bottom_middle'):
        """
        Description : Drag the query bucket field to another query bucket field
        :Usage - drag_query_bucket_field_to_another_query_bucket_field('Vertical', 'SALES', 'Horizontal', 'CAR')
        """
        self._designer_metadataobj.drag_query_bucket_field_to_another_query_bucket_field(source_bucket, source_field, target_bucket, target_field, source_field_pos, target_field_pos, target_field_loc)
            
    def double_click_on_dimension_field(self, field_name):
        """
        Descriptions : This method will double click on dimension field.
        :usage : double_click_on_dimension_field('CAR')
        """
        self._designer_metadataobj.double_click_dimension_field_in_metadata_tree(field_name)
    
    def double_click_on_measures_field(self, field_name):
        """
        Descriptions : This method will double click on measures field.
        :usage : double_click_on_dimension_field('CAR')
        """
        self._designer_metadataobj.double_click_measures_field_in_metadata_tree(field_name) 
    
    def right_click_on_measures_field(self, field_name, context_menu_item_path=None):
        """
        Description : This method will right click the value in the measures section
        :usage : right_click_on_measures_field('CAR', 'Vertical')
        """
        self._designer_metadataobj.right_click_on_datapane(field_name, context_menu_item_path, datapane='measures')
        
    def right_click_on_dimensions_field(self, field_name, context_menu_item_path=None):
        """
        Description : This method will right click the value in the measures section
        :usage : right_click_on_measures_field('CAR', 'Vertical')
        """
        self._designer_metadataobj.right_click_on_datapane(field_name, context_menu_item_path, datapane='dimensions')
    
    def enter_text_in_search_fields(self, text_to_search=None, send_keys=None):
        """
        Description: This method is used to enter the text in the search input field
        :usage : enter_text_in_search_fields('Product')
        """
        self._designer_metadataobj.search_fields_in_search_box(text_to_enter=text_to_search, send_keys=send_keys)
    
    def verify_dimensions_field_is_empty(self,msg):
        """
        Description: This method is used to verify the dimensions field is empty
        :usage : verify_dimensions_field_is_empty("Step 4.1")
        """
        self._designer_metadataobj.verify_dimensions_field_is_empty(msg)
    
    def verify_measures_field_is_empty(self,msg):
        """
        Description: This method is used to verify the measures field is empty
        :usage : verify_measures_field_is_empty("Step 4.1")
        """   
        self._designer_metadataobj.verify_measures_field_is_empty(msg)
    
    def verify_fields_in_dimensions(self, field_list, msg, compare_type='asequal',field_path=None):
        """
        Description: This method is used to verify the fiels in dimensions section
        :usage : verify_fields_in_dimensions(['Product'])
        """
        self._designer_metadataobj.verify_dimensions_fields(field_list, msg,compare_type=compare_type,field_path=field_path)
        
    def verify_fields_in_measures(self, field_list, msg, compare_type='asequal',field_path=None):
        """
        Description: This method is used to verify the fiels in measures section
        :usage : verify_fields_in_measures(['Product'])
        """
        self._designer_metadataobj.verify_measures_fields(field_list, msg, compare_type=compare_type,field_path=field_path)
    
    def verify_variables_list(self, variable_list, msg, compare_type='asequal'):
        """
        Description: This method is used to verify the variables list
        :usage : verify_variables_list(['Product'])
        """
        self._designer_metadataobj.verify_variables_list(variable_list, msg, compare_type=compare_type)
    
    def select_layout_option(self, option_to_select):
        """
        Description : This method select the layout option from the layout menu bar
        :Usage select_layout_option('Heading')
        """
        self._designer_metadataobj.select_layout_options(option_to_select)
       
    def verify_checked_layout_options(self, checked_item_list, msg):
        """
        Description : This method is used to verify the checked layout option
        :Usage verify_checked_layout_options(['Heading'])
        """
        self._designer_metadataobj.verify_layout_options_if_checked(checked_item_list, msg)
    
    def verify_all_options_in_layout(self, item_list, msg, compare_type='asequal'):
        """
        Description : This method is used to verify all the layout options
        :Usage verify_all_options_in_layout(['Heading'])
        """
        self._designer_metadataobj.verify_all_layout_options(item_list, msg, compare_type=compare_type)
        
    def select_fields_or_variables_in_datapane(self, option_to_select):
        """
        Description: This method is used to select the fields or variables
        :Usage select_fields_or_variables_in_datapane('Fields')
        """
        self._designer_metadataobj.select_field_or_variables(option_to_select)
    
    def drag_variables_to_header(self, variable_path, text_to_enter=None):
        """
        Description: This method is enter spaces in the header and drag variables item to the header
        :Usage drag_variables_to_header('Query Variables->Filters and Variables->Store Name, space_to_enter=' ')
        """
        self._designer_metadataobj.drag_and_drop_variables_to_heading_or_footing(variable_path, 'Heading', text_to_enter=text_to_enter)
        
    def drag_variables_to_footer(self, variable_path, text_to_enter=None):
        """
        Description: This method is enter spaces in the footer and drag variables item to the footer
        :Usage drag_variables_to_footer('Query Variables->Filters and Variables->Store Name, space_to_enter=' ')
        """
        self._designer_metadataobj.drag_and_drop_variables_to_heading_or_footing(variable_path, 'Footing', text_to_enter=text_to_enter)
    
    def drag_variables_to_filter_bar(self, item_path):
        """
        Description: This method is used todrag variables to filter pane
        :Usage : drag_variables_to_filter_bar('Query Variables->Filters and Variables->Store Name')
        """
        self._designer_metadataobj.drag_variables_to_filter_pane(item_path)
    
    def click_on_heading(self, text_to_enter=None):
        """
        Description: This method is used to click on the heading and enter some text
        :Usage : click_on_heading()
        """
        self._designer_metadataobj.click_heading_or_footing('Heading', text_to_enter=text_to_enter)
    
    def click_on_footing(self, text_to_enter=None):
        """
        Description: This method is used to click onfooting and enter some text
        :Usage : click_on_footing()
        """
        self._designer_metadataobj.click_heading_or_footing('Footing', text_to_enter=text_to_enter)
    
    def verify_text_in_heading(self, text_list, msg, compare_type='asequal'):
        """
        Description: This method is used to verify the text in the heading
        :Usage : verify_text_in_heading(['Product'], "Step 4.1: Verify the list")
        """
        self._designer_metadataobj.verify_text_in_heading_or_footing(text_list, msg, 'Heading', compare_type=compare_type)

    def verify_text_in_footing(self, text_list, msg, compare_type='asequal'):
        """
        Description: This method is used to verify the text in the footing
        :Usage : verify_text_in_footing(['Product'], "Step 4.1: Verify the list")
        """
        self._designer_metadataobj.verify_text_in_heading_or_footing(text_list, msg, 'Footing', compare_type=compare_type)
    
    def verify_date_time_format_in_heading(self, index, msg, date_time_format='mm/dd/yy'):
        """
        Description: This method is used to verify the date time format in heading
        :Usage : verify_date_time_format_in_heading(1, 'Step 4.1: Verify', date_time_format='mm/dd/yy')
        """
        self._designer_metadataobj.verify_date_time_in_header_or_footer(index, msg, date_time_format=date_time_format, layout_option='Heading')
        
    def verify_date_time_format_in_footing(self, index, msg, date_time_format='mm/dd/yy'):
        """
        Description: This method is used to verify the date time format in footing
        :Usage : verify_date_time_format_in_footing(1, 'Step 4.1: Verify', date_time_format='mm/dd/yy')
        """
        self._designer_metadataobj.verify_date_time_in_header_or_footer(index, msg, date_time_format=date_time_format, layout_option='Footing')
    
    def close_heading_or_footing_toolbar(self):
        """
        Description: This method is used to close both heading and footing toolbar
        :Usage : close_heading_or_footin_toolbar()
        """
        self._designer_metadataobj.close_heading_or_footing_toolbar()
    
    def drag_data_field_from_measures_to_filter_pane(self, field_path):
        """
        Description: This method is used to drag data from measuresto filter bar
        :Usage : drag_data_field_from_measures_to_filter_pane('Product->Profit')
        """
        self._designer_metadataobj.drag_data_fields_to_filter_bar(field_path, field_type='Measures')
        
    def drag_data_field_from_dimensions_to_filter_pane(self, field_path):
        """
        Description: This method is used to drag data from dimensions to filter bar
        :Usage : drag_data_field_from_measures_to_filter_pane('Product->Profit')
        """
        self._designer_metadataobj.drag_data_fields_to_filter_bar(field_path, field_type='Dimensions')
    
    def click_toolbar_item(self, item_name):
        """
        Description: This method is used to click all items from toolbar
        @params : save, undo, redo, preview, layout, more, help, settings
        :Usage : click_toolbar_item('preview')
        """
        self._designer_metadataobj.click_an_item_on_toolbar(item_name)
        
    def verify_toolbar_item_enabled_disabled(self, item_name, msg, disabled='true'):
        """
        Description: This method is used to verify if the object in toolbar is enabled or disabled
        @params : save, undo, redo, preview, layout, more, help, settings
        :Usage : verify_toolbar_item_enabled_disabled(item_name, msg)
        """
        self._designer_metadataobj.verify_toolbar_item_enabled_or_disabled(item_name, msg, disabled=disabled)
        
    def go_back_to_design_from_preview(self, wait_time=3):
        """
        Description : This method used to back to design page from preview window 
        :Usage : go_back_to_design_from_preview()
        """
        pd_preview.go_back_to_design_from_preview(self, wait_time)
        
    def verify_drag_drop_with_warning_logo(self, source_x, source_y, target_x, target_y, target_obj, msg):
        """
        Description: This method is used to verify the warning logo in drag drop
        :Usage : verify_drag_drop_with_warning_logo(100, 615, 853, 404, target_obj, "Step 3")
        """
        self._designer_metadataobj.verify_drag_and_verify_warning_logo_on_the_cursor(source_x, source_y, target_x, target_y, target_obj, msg)
        
    def select_more_option(self, option_to_select):
        """
        Description : This method select the more option from the toolbar
        :Usage select_more_option('Run with Insight')
        """
        self._designer_metadataobj.select_more_options(option_to_select)
        
    def select_format_access_option(self, access_option):
        """
        Description: This method is used to select the access type in format
        :Usage : select_format_access_option('Axis')
        """
        self._designer_metadataobj.change_format_access(access_option)
        
    def select_theme_in_format_tab(self, theme_name, msg=None, verify_list=None, compare_type='asequal'):
        """
        Description: This method is used to change the theme name 
        :Usage : select_theme_in_format_tab('Light')
        """
        self._designer_metadataobj.change_theme_in_format_tab(theme_name, msg=msg, verify_list=verify_list, compare_type=compare_type)
    
    def select_line_style_options_series_format(self,line_style_option):
        """
        Description: This method is used to select line_style in series format option
        :Usage: select_line_style_options('Short_Dash_Dot_Dot')
        @params: line_style_option: use any one from the below
        ['Solid','Dash','Dash_dot','Dash_dot_dot','Dot','Long_dash','Long_Dash_Dot','Short_Dash','Short_Dash_Dot','Short_Dash_Dot_Dot','Short_Dot']
        """
        self._designer_metadataobj.select_line_style_options(line_style=line_style_option)
    
    def verify_theme_in_format_tab(self,theme_name,msg):
        """
        Description: This method is used to verify the default theme selected under format tab
        :Usage : verify_default_theme_in_format_tab('Designer 2018',"verify the default theme selected")
        """
        self._designer_metadataobj.verify_default_theme_in_format_tab(theme_name,msg)
    
    def change_labels_options(self, option_type, item_name):
        """
        Description: This method is used to change the items inside the label
        :Usage : change_labels_options(option_type, item_name)
        """
        self._designer_metadataobj.change_format_labels(option_type, item_name)
    
    def verify_values_in_querybucket(self, bucket_name, expected_list, msg, compare_type='asequal'):
        """
        Description: This method is used to verify the values under the bucket
        :Usage : verify_values_in_querybucket('Size', ['Sales'], "Step 2.1")
        """
        self._designer_metadataobj.verify_query_bucket_values(bucket_name, expected_list, msg, compare_type=compare_type)
    
    def select_font_name_in_labels(self, fontname, expand=False):
        """
        Description: This method is used to select the font name in labels 
        :Usage : select_font_name_in_labels('TIMES')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LABELS_CSS, font_name=fontname, expand=expand)
    
    def select_font_style_in_labels(self, fontstyle, expand=False):
        """
        Description: This method is used to select the font style
        :Usage : select_font_style_in_labels('bold')
        :params: bold or italic
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LABELS_CSS, format_style=fontstyle, expand=expand)
        
    def select_font_size_in_labels(self, size, expand=False):
        """
        Description: This method is used to select font size 
        :Usage : select_font_size_in_labels('24')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LABELS_CSS, size=size, expand=expand)
        
    def select_font_unit_in_labels(self, unit, expand=False):
        """
        Description: this method is used to select font units
        :Usage : select_font_unit_in_labels('pt')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LABELS_CSS, unit=unit, expand=expand)
        
    def select_font_color_in_labels(self, color, color_option='palette', expand=False):
        """
        Description: This method is used to select font color in labels
        :Usage: select_font_color_in_labels('#b97a57')
        :params: used hex code for the colors from the dom, and color option based on the palette or more
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LABELS_CSS, color=color, color_option=color_option, expand=expand)
    
    def select_font_name_in_title(self, font_name, expand=False):
        """
        Description: This method is used to select the font name in labels 
        :Usage : select_font_name_in_title('TIMES')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.TITLE_CSS, font_name=font_name, expand=expand)
        
    def select_font_style_in_title(self, font_style, expand=False):
        """
        Description: This method is used to select the font style
        :Usage : select_font_style_in_title('bold')
        :params: bold or italic
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.TITLE_CSS, format_style=font_style, expand=expand)
    
    def select_font_size_in_title(self, size, expand=False):
        """
        Description: This method is used to select font size 
        :Usage : select_font_size_in_title('24')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.TITLE_CSS, size=size, expand=expand)
        
    def select_font_unit_in_title(self, unit, expand=False):
        """
        Description: this method is used to select font units
        :Usage : select_font_unit_in_title('pt')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.TITLE_CSS, unit=unit, expand=expand)
        
    def select_font_color_in_title(self, color, color_option='palette', expand=False):
        """
        Description: This method is used to select font color in labels
        :Usage: select_font_color_in_labels('#b97a57')
        :params: used hex code for the colors from the dom, and color option based on the palette or more
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.TITLE_CSS, color=color, color_option=color_option, expand=expand)
        
    def verify_font_name_in_labels(self, fontname, msg, expand=False):
        """
        Description: This method is used to verify the font name in labels 
        :Usage : verify_font_name_in_labels('TIMES', 'Step 4.1')
        """
        self._designer_metadataobj.verify_font_options(msg, parent_css=dc_locators.LABELS_CSS, verify_font_name=fontname, expand=expand)
    
    def verify_font_size_in_labels(self, size, msg, expand=False):
        """
        Description: This method is used to verify font size unser labels
        :Usage : verify_font_size_in_title('24', 'Step 3.1: Verify')
        :Params: pass the size as a string
        """
        self._designer_metadataobj.verify_font_options(msg, parent_css=dc_locators.LABELS_CSS, verify_size=size, expand=expand)
        
    def verify_axis_style_in_chart_canvas(self, attribute, verify_text, msg, axis='x'):
        """
        Description: This method is used to verify the fontstyle in the chart axis canvas page
        :Usage : verify_axis_style_in_chart_canva('font-family', 'TIMES NEW ROMAN', 'Step 4.1')
        :Params:  attribute can be transform, fill, font-style, font-weight, font-size, font-family
        """
        self._designer_metadataobj.verify_style_in_chart_preview(attribute, verify_text, msg, axis=axis)
    
    def verify_axis_style_in_chart_preview_window(self, attribute, verify_text, msg, axis='x'):
        """
        Description: This method is used to verify the fontstyle in the chart axis preview window
        :Usage : verify_axis_style_in_chart_preview_window('font-family', 'TIMES NEW ROMAN', 'Step 4.1')
        :Params:  attribute can be transform, fill, font-style, font-weight, font-size, font-family
        """
        self._designer_metadataobj.verify_style_in_chart_preview(attribute, verify_text, msg, parent_css='#jschart_HOLD_0', axis=axis)
        
    def verify_title_style_in_chart_canvas(self, attribute, verify_text, msg, axis='x'):
        """
        Description: This method is used to verify the fontstyle in the chart axis canvas page
        :Usage : verify_title_style_in_chart_canvas('font-family', 'TIMES NEW ROMAN', 'Step 4.1')
        :Params:  attribute can be transform, fill, font-style, font-weight, font-size, font-family
        """
        self._designer_metadataobj.verify_style_in_chart_preview(attribute, verify_text, msg, child_css=" text[class^='xaxis'][class$='title']", axis=axis)
    
    def verify_title_style_in_chart_preview_window(self, attribute, verify_text, msg, axis='x'):
        """
        Description: This method is used to verify the fontstyle in the chart axis preview window
        :Usage : verify_title_style_in_chart_preview_window('font-family', 'TIMES NEW ROMAN', 'Step 4.1')
        :Params:  attribute can be transform, fill, font-style, font-weight, font-size, font-family
        """
        self._designer_metadataobj.verify_style_in_chart_preview(attribute, verify_text, msg, parent_css='#jschart_HOLD_0', child_css=" text[class^='xaxis'][class$='title']", axis=axis)
        
    def verify_axis_rotation_in_chart_canvas(self, verify_text, msg, compare_type='asin', axis='x'):
        """
        Description: This method is used to verify the rotation of the text element in the axis in canvas
        :Usage : verify_axis_rotation_in_chart_canvas('rotate(-45)', 'Step 6.1')
        """
        self._designer_metadataobj.verify_axis_rotation_in_chart(verify_text, msg, axis=axis, compare_type=compare_type)
        
    def verify_axis_rotation_in_chart_preview(self, verify_text, msg, compare_type='asin', axis='x'): 
        """
        Description: This method is used to verify the rotation of the text element in the axis in preview window
        :Usage : verify_axis_rotation_in_chart_preview('rotate(-45)', 'Step 6.1')
        """
        self._designer_metadataobj.verify_axis_rotation_in_chart(verify_text, msg, parent_css='#jschart_HOLD_0', axis=axis, compare_type=compare_type)
    
    def select_new_calculation_from_dimensions_or_measures(self, field_to_select):
        """
        Description: This method is used to select new calculation from the measures or dimensions
        :Usage : select_new_calculation_from_dimensions_or_measures('measures')
        :Params : 'measures' or 'dimensions'
        """
        self._designer_metadataobj.select_new_calculation(field=field_to_select)
        
    def click_operator_from_new_calculation(self, operator_name):
        """
        Description: This method is used to select the operator in new calculation
        :Usage: click_operator_from_new_calculation('x')
        :Params : use * for multiplication and / for division (for others use the same as given in the new calculation table)
        """
        self._designer_metadataobj.click_calculation_operator_button(operator_name)
        
    def double_click_on_calculation_fields(self, field_path):
        """
        Description : This method will double click on the calculations
        :usage : double_click_on_calculation_fields('COUNTRY')
        """
        self._designer_metadataobj.double_click_on_calculation_dimensions(field_path)
        
    def verify_dialog_box_in_calculation(self, text_to_verify, msg, compare_type='asequal'):
        """
        Description : This method will verify the text box in teh calcultions
        :Usage : verify_dialog_box_in_calculation(('CAR.ORIGIN.COUNTRY', 'Step 5: Verify the text box')
        """
        self._designer_metadataobj.verify_calculation_dialog(text_to_verify, msg, compare_type=compare_type)
    
    def edit_calculation_dialog_name(self, name_to_change):
        """
        Description: This function is used to change the nae of new calculation
        :Usage : edit_calculation_dialog_name('Profit')
        """
        self._designer_metadataobj.edit_calculation_dialog_name(name_to_change)
    
    def edit_calculation_dialog_editor(self, value_to_change):
        """
        Description : This method will change the value inside textbox on the calculations
        :usage : edit_calculation_dialog_editor('DISCOUNT_US *250')
        """
        self._designer_metadataobj.edit_calculation_dialog_editor(value_to_change)
    
    def click_button_on_calculation(self, button_name):
        """
        Description: This method is used to click the ok or cancel button in a popup dialog
        :Usage : click_button_on_calculation('OK')
        """
        self._wf_main_page_obj.button_in_popup_dialog_from_action_bar(button_name, 'click')
        
    def select_font_name_in_legend_labels(self, fontname, expand=False):
        """
        Description: This method is used to select the font name in labels 
        :Usage : select_font_name_in_legend_labels('TIMES')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LEGEND_LABELS_CSS, font_name=fontname, expand=expand)
    
    def select_font_style_in_legend_labels(self, fontstyle, expand=False):
        """
        Description: This method is used to select the font style
        :Usage : select_font_style_in_legend_labels('bold')
        :params: bold or italic
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LEGEND_LABELS_CSS, format_style=fontstyle, expand=expand)
        
    def select_font_size_in_legend_labels(self, size, expand=False):
        """
        Description: This method is used to select font size 
        :Usage : select_font_size_in_legend_labels('24')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LEGEND_LABELS_CSS, size=size, expand=expand)
        
    def select_font_unit_in_legend_labels(self, unit, expand=False):
        """
        Description: this method is used to select font units
        :Usage : select_font_unit_in_legend_labels('pt')
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LEGEND_LABELS_CSS, unit=unit, expand=expand)
        
    def select_font_color_in_legend_labels(self, color, color_option='palette', expand=False):
        """
        Description: This method is used to select font color in labels
        :Usage: select_font_color_in_labels('#b97a57')
        :params: used hex code for the colors from the dom, and color option based on the palette or more
        """
        self._designer_metadataobj.edit_font_options(parent_css=dc_locators.LEGEND_LABELS_CSS, color=color, color_option=color_option, expand=expand) 
        
    def verify_font_name_in_legend_labels(self, fontname, msg, expand=False):
        """
        Description: This method is used to verify the font name in labels 
        :Usage : verify_font_name_in_legend_labels('TIMES', 'Step 4.1')
        """
        self._designer_metadataobj.verify_font_options(msg, parent_css=dc_locators.LEGEND_LABELS_CSS, verify_font_name=fontname, expand=expand)
    
    def verify_font_size_in_legend_labels(self, size, msg, expand=False):
        """
        Description: This method is used to verify font size unser labels
        :Usage : verify_font_size_in_legend_labels('24', 'Step 3.1: Verify')
        :Params: pass the size as a string
        """
        self._designer_metadataobj.verify_font_options(msg, parent_css=dc_locators.LEGEND_LABELS_CSS, verify_size=size, expand=expand)
        
    def verify_legend_style_in_canvas(self, attribute, verify_text, msg):
        """
        Description: This method is used to verify legend style in the canvas
        :Usage : verify_legend_style_in_canvas('font-weight', 'BOOKMAN', 'Step 2.1')
        """
        self._designer_metadataobj.verify_legend_style(attribute, verify_text, msg)
        
    def verify_legend_style_in_preview(self, attribute, verify_text, msg):
        """
        Description: This method is used to verify legend style in preview
        :Usage : verify_legend_style_in_preview('font-weight', 'BOOKMAN', 'Step 2.1')
        """
        self._designer_metadataobj.verify_legend_style(attribute, verify_text, msg, parent_css='#jschart_HOLD_0')
    
    def verify_show_title_in_legend_labels(self, msg, present=False, verify_text=None):
        """
        Description: This method is used to verify the show title under the font stylying section
        :Usage : verify_show_title_in_legens_labels('Step 4.5: Verify the label is not present', present=False)
        """
        self._designer_metadataobj.verify_show_title_in_font_styling(msg, present=present, verify_text=verify_text, parent_css=dc_locators.LEGEND_LABELS_CSS)
    
    def edit_bin_values_in_measures(self, bin_width_text=None, show_as=None, click_type='Ok'):
        """
        Description: This method is used to edit the bin values
        :Usage : edit_bin_values_in_measures (bin_width_text=1000, show_as=Value)
        :Params : use ok or cancel for click_type
        """
        self._designer_metadataobj.edit_bin_values(bin_width_text=bin_width_text, show_as=show_as, click_type=click_type)
    
    def verify_element_added_in_dimensions(self, msg, field_path=None, verify_value=None):
        """
        Description: This method is used to verify the value added in the data pane
        :Usage : verify_element_added_in_dimensions('Step 4.1', field_path='CAR->COMP', verify_value='COMP')
        """
        self._designer_metadataobj.verify_element_added_in_datapane(msg, field_path, verify_value)
        
    def verify_element_added_in_measures(self, msg, field_path=None, verify_value=None):
        """
        Description: This method is used to verify the value added in the data pane
        :Usage : verify_element_added_in_measures('Step 4.1', field_path='CAR->COMP', verify_value='COMP')
        """
        self._designer_metadataobj.verify_element_added_in_datapane(msg, field_path, verify_value, datapane='measures')
        
    def select_item_from_query_menu_widget(self, bucket_name, content_path):
        """
        Description: This method is used to click the menu widget and select items
        :Usage : select_item_from_query_menu_widget('Size', 'Split axis')
        """
        self._designer_metadataobj.click_menu_widget_on_query_buckets(bucket_name, content_path)
        
    def verify_x_axis_title_color_in_chart_canvas(self, color, msg, attribute='fill'):
        """
        Description: This method is used to verify the x axis title color in chart
        :Usage : verify_x_axis_title_color_in_chart_preview(blue, 'Step 4.1: Verify blue is in x axis')
        """
        self._designer_metadataobj.verify_color_in_chart_axis(color, msg, attribute=attribute)
        
    def verify_x_axis_title_color_in_chart_preview(self, color, msg, attribute='fill'):
        """
        Description: This method is used to verify the x axis title color in chart
        :Usage : verify_x_axis_title_color_in_chart_preview(blue, 'Step 4.1: Verify blue is in x axis')
        """
        self._designer_metadataobj.verify_color_in_chart_axis(color, msg, attribute=attribute, parent_css='#jschart_HOLD_0')
    
    def select_datatype_in_format_data_tab(self, type_name):
        """
        Description: This method is used to select datatype in format data tab
        :usage select_datatype_in_format_data('alpha')
        @param datatype_format:'alpha', 'numeric', 'date' or 'custom'.
        """
        self._designer_metadataobj.select_datatype_in_format_data(type_name)
    
    def select_checkbox_in_format_data_tab(self, checkbox_name, toggle):
        """
        Description: This function will select or un_select check box under data format popup for any one of the section 'alpha', 'numeric', 'date' or 'custom'.
        @param label_name:'Variable length'.
        @param check_uncheck_toggle: True or False
        :usage select_checkbox_in_format_data_tab('Variable length', True)
        """
        self._designer_metadataobj.select_checkbox_in_format_data(checkbox_name, toggle)
        
    def select_grid_item_from_open_dialog(self, item_to_click, click_type='double'):
        """
        Description: This method is used to select the item in the open dialog
        :Usage : select_grid_item_from_open_dialog('ENDark.sty')
        """
        self._resc_obj.select_resource_from_gridview(item_to_click, selection_type=click_type)
        
    def verify_background_color_in_chart_canvas(self, color, msg, attribute='fill'):
        """
        Description: This method is used to verify background color in the chart canvas
        :Usage : verify_background_color_in_chart_canvas('nero', 'Step 4.1: Verify')
        """
        self._utillity.verify_element_color_using_css_property(".wfc-bc-output-div [class='background']", color, msg, attribute=attribute)
    
    def verify_background_color_in_chart_preview(self, color, msg, attribute='fill'):
        """
        Description: This method is used to verify background color in the chart canvas
        :Usage : verify_background_color_in_chart_preview('nero', 'Step 4.1: Verify')
        """
        self._utillity.verify_element_color_using_css_property("#jschart_HOLD_0 [class='background']", color, msg, attribute=attribute)
        
    def select_chart_from_chart_picker(self, chart_name, expand=False):
        """
        Description: This method is used to select the chart item
        :Usage: select_chart_picker_element('range_chart')
        @params: chart_name: use any one from the below
        ['vertical_stacked_bar', 'horizontal_bar', 'vertical_side_by_side_bar', 'ring_pie', 'absolute_line', 'vertical_stacked_area', 
        'scatter_bubble', 'circle_plot', 'tree_map', 'datagrid', 'matrix_marker', 'proportional_symbol_map', 'choropleth_map', 'waterfall', 
        'gauge', 'funnel_chart', 'mekko_chart', 'tagcloud', 'streamgraph', 'arc_chart', 'calendar_heat_map_chart', 'usa_state_cartogram', 
        'chord_diagram', 'cluster_diagram', 'compare_2_bars', 'datatables_grid', 'force_directed_chart', 'hexagon_bin_scatter_chart', 
        'histogram_chart', 'sparkline_kpi', 'kpi_with_sparkline_large', 'liquid_gauge_chart', 'choropleth_usa_map_chart', 'world_choropleth_&_bubble_map', 
        'marker_chart', 'organization_chart', 'pack_chart', 'population_pyramid', 'range_chart', 'ratio_chart', 'sankey_flow_chart', 'simple_bar_chart', 
        'sunburst_chart', 'timeline_chart', 'us_map_chart', 'what_if_assist']
        """
        self._designer_metadataobj.select_chart_picker_element(chart_name, expand=expand)
        
    def verify_chart_index_on_chart_picker(self, chart_name, chart_index, msg):
        """
        Description: This method is used to verify the chart index
        :Usage: verify_chart_index_on_chart_picker('vertical_stacked_bar', 0 , 'Step 4.1')
        @params: chart_name: use any one from the below
        ['vertical_stacked_bar', 'horizontal_bar', 'vertical_side_by_side_bar', 'ring_pie', 'absolute_line', 'vertical_stacked_area', 
        'scatter_bubble', 'circle_plot', 'tree_map', 'datagrid', 'matrix_marker', 'proportional_symbol_map', 'choropleth_map', 'waterfall', 
        'gauge', 'funnel_chart', 'mekko_chart', 'tagcloud', 'streamgraph', 'arc_chart', 'calendar_heat_map_chart', 'usa_state_cartogram', 
        'chord_diagram', 'cluster_diagram', 'compare_2_bars', 'datatables_grid', 'force_directed_chart', 'hexagon_bin_scatter_chart', 
        'histogram_chart', 'sparkline_kpi', 'kpi_with_sparkline_large', 'liquid_gauge_chart', 'choropleth_usa_map_chart', 'world_choropleth_&_bubble_map', 
        'marker_chart', 'organization_chart', 'pack_chart', 'population_pyramid', 'range_chart', 'ratio_chart', 'sankey_flow_chart', 'simple_bar_chart', 
        'sunburst_chart', 'timeline_chart', 'us_map_chart', 'what_if_assist']
        """
        self._designer_metadataobj.verify_chart_index(chart_name, chart_index, msg)
        
    """******************************************************************** This is common for query Section*************************************************************************************"""
    
    def select_query_or_format_tab(self, select_option='format'):
        """
        Description: This method is used to select the query or format
        :Usage select_query_or_format_tab(select_option='format')
        :Params  query or format
        """
        self._designer_metadataobj.select_query_or_format_tab_option(select_option=select_option)
    
    def remove_query_bucket_field(self, bucket_name, filed_name):
        """
        Descriptions : This method will remove field's(hover over field and click 'x') in query bucket.
        :Usage remove_query_bucket_field('Vertical', 'Customers')
        """
        self._designer_metadataobj.remove_query_bucket_field(bucket_name, filed_name)
    
    def select_display_toolbar_in_query_bucket(self, display_toolbar):
        """
        Descriptions : This method will select display tool_bar options in query bucket.
        :Usage select_display_toolbar_in_query_bucket('Stacked)
        """
        self._designer_metadataobj.select_display_toolbar_in_query_bucket(display_toolbar)
        
    def verify_display_toolbar_in_query_bucket(self, display_toolbar_list, display_message, comparison_type='asequal'):
        """
        Descriptions : This method will verify display tool_bar options as list in query bucket.
        :Usage verify_display_toolbar_in_query_bucket(['Stacked'], 'Step 09.00: verify', comparison_type='asin')
        """
        self._designer_metadataobj.verify_display_toolbar_in_query_bucket(display_toolbar_list, display_message, assert_type=comparison_type)
    
    def verify_selected_display_toolbar_in_query_bucket(self, display_toolbar, display_message):
        """
        Descriptions : This method will verify selected display tool_bar options in query bucket.
        :Usage verify_selected_display_toolbar_in_query_bucket('Stacked', 'Step 09.00: verify')
        """
        self._designer_metadataobj.verify_selected_display_toolbar_in_query_bucket(display_toolbar, display_message)
    
    def select_quick_marker_option(self, option_name):
        """
        Description: This function is used to select marker option from its drop down under quick->Marker.
        usage : select_quick_marker_option('Tick')
        """
        self._designer_metadataobj.change_marker_option(option_name)
        
    
    """******************************************************************** This is filter Section*************************************************************************************"""
    
    def verify_filter_shelf(self, list_values, msg):
        """
        Description: This method is used to verify the filter shelf
        :Usage : verify_filter_shelf([['Product Category','All'],['Product','All']], "Step 4.5: Verify the filter shelf)
        """
        self._designer_metadataobj.verify_filter_shelf_fields_and_values(list_values, msg)
        
    def click_filter_shelf_field(self, field_name, xoffset=0, yoffset=0):
        """
        Description: This function will left click on field from filter shelf.
        :Usage : click_filter_shelf_field('Product Category')
        """
        self._designer_metadataobj.select_filter_shelf_field(field_name, left_click=True, xoffset=xoffset, yoffset=yoffset)
    
    def right_click_filter_shelf_field(self, field_name, context_menu_path=None, xoffset=0, yoffset=0):
        """
        Description: This function will right click on field from filter shelf.
        :Usage : right_click_filter_shelf_field('Product Category', context_menu_path='Single')
        """
        self._designer_metadataobj.select_filter_shelf_field(field_name, context_menu_path=context_menu_path, right_click=True, xoffset=xoffset, yoffset=yoffset)
    
    def verify_filter_shelf_field_right_click_options(self, field_name, expected_list, step_num, context_menu_path=None, comparision_type='asequal', xoffset=0, yoffset=0):
        """
        Description: This function verify right click option from field from filter shelf.
        :Usage : select_filter_shelf_field('Product Category', ['Edit'], '09.00', context_menu_path='Single')
        """
        self._designer_metadataobj.verify_filter_shelf_field_right_click_options(field_name, expected_list, step_num, context_menu_path=context_menu_path, comparision_type=comparision_type, xoffset=xoffset, yoffset=yoffset)
    
    def verify_slider_label_in_filter_shelf_fields_popup(self, label_value, msg):
        """
        Description: This function will verify slider label value in filter shelf field popup.
        :Usage : verify_slider_label_in_filter_shelf_fields_popup('17:19', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_slider_in_filter_shelf_fields_popup(msg, label_value=label_value)
    
    def verify_slider_minimum_value_in_filter_shelf_fields_popup(self, min_label_value, msg):
        """
        Description: This function will verify slider minimum value in filter shelf field popup.
        :Usage : verify_slider_minimum_value_in_filter_shelf_fields_popup('17', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_slider_in_filter_shelf_fields_popup(msg, min_label_value=min_label_value)
    
    def verify_slider_maximum_value_in_filter_shelf_fields_popup(self, max_label_value, msg):
        """
        Description: This function will verify slider maximum value in filter shelf field popup.
        :Usage : verify_slider_maximum_value_in_filter_shelf_fields_popup('19', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_slider_in_filter_shelf_fields_popup(msg, max_label_value=max_label_value)
    
    def verify_slider_marker_in_filter_shelf_fields_popup(self, marker_value, marker_status, msg):
        """
        Description: This function will verify slider marker is displayed in filter shelf field popup.
        :Usage : verify_slider_maximum_value_in_filter_shelf_fields_popup('19', 'Visible', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_slider_in_filter_shelf_fields_popup(msg, marker_value=marker_value, marker_status=marker_status)
    
    def select_slider_marker_in_filter_shelf_fields_popup(self, marker_value, move_left_times=None, move_right_times=None, pause_=0.5):
        """
        Description: This function will select slider in filter shelf field popup.
        :Usage : select_slider_marker_in_filter_shelf_fields_popup('19', move_left_times=19, move_right_times=19)
        """
        self._designer_metadataobj.select_slider_marker_in_filter_shelf_fields_popup(marker_value=marker_value, move_left_times=move_left_times, move_right_times=move_right_times, pause_=pause_)
    
    def verify_textbox_in_filter_shelf_fields_popup(self, text_box_title, text_box_input, msg, comparision_type='asequal'):
        """
        Description: This function will verify textbox in filter shelf field popup.
        :Usage : verify_textbox_in_filter_shelf_fields_popup('Enter search string', 'Japan', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_filter_shelf_fields_popup('text_box', msg, text_box_title=text_box_title, text_box_input=text_box_input, assert_type=comparision_type)
    
    def verify_button_in_filter_shelf_fields_popup(self, button, msg, comparision_type='asequal'):
        """
        Description: This function will verify button in filter shelf field popup.
        :Usage : verify_button_in_filter_shelf_fields_popup(Japan', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_filter_shelf_fields_popup('button', msg, button_name=button, assert_type=comparision_type)
    
    def verify_checkbox_in_filter_shelf_fields_popup(self, checkbox_name, msg, comparision_type='asequal'):
        """
        Description: This function will verify checkbox in filter shelf field popup.
        :Usage : verify_checkbox_in_filter_shelf_fields_popup('Japan', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_filter_shelf_fields_popup('checkbox', msg, checkbox_name=checkbox_name, assert_type=comparision_type)
    
    def verify_radio_in_filter_shelf_fields_popup(self, radio_name, msg, comparision_type='asequal'):
        """
        Description: This function will verify radio in filter shelf field popup.
        :Usage : verify_radio_in_filter_shelf_fields_popup('Japan', 'Step 09.00: Verify')
        """
        self._designer_metadataobj.verify_filter_shelf_fields_popup('radio', msg, radio_name=radio_name, assert_type=comparision_type)
    
    def enter_text_in_textbox_filter_shelf_fields_popup(self, text_box_title, text_box_input):
        """
        Description: This function will enter text in filter shelf field popup.
        :Usage : enter_text_in_textbox_filter_shelf_fields_popup('Japan', 'Japan')
        """
        self._designer_metadataobj.select_filter_shelf_fields_popup('text_box', text_box_title, text_box_input)
    
    def select_button_in_filter_shelf_fields_popup(self, button_name):
        """
        Description: This function will select button in filter shelf field popup.
        :Usage : select_button_in_filter_shelf_fields_popup('Japan')
        """
        self._designer_metadataobj.select_filter_shelf_fields_popup('button', button_name=button_name)
    
    def select_checkbox_in_filter_shelf_fields_popup(self, checkbox_name):
        """
        Description: This function will select checkbox in filter shelf field popup.
        :Usage : select_checkbox_in_filter_shelf_fields_popup('Japan')
        """
        self._designer_metadataobj.select_filter_shelf_fields_popup('checkbox', checkbox_name=checkbox_name)
    
    def select_radio_button_in_filter_shelf_fields_popup(self, radio_button_name):
        """
        Description: This function will select radio button in filter shelf field popup.
        :Usage : select_radio_button_in_filter_shelf_fields_popup('Japan')
        """
        self._designer_metadataobj.select_filter_shelf_fields_popup('checkbox', radio_name=radio_button_name)
    
    """******************************************************************** This is common for RIBBON Section*************************************************************************************"""
        
    def save_designer_chart_from_toolbar(self, title_to_save, wait_time=3):
        """
        Descriptions : This method will save file from ribbon tool_bar.
        :Usage save_designer_chart_from_toolbar('Chart')
        """
        self._designer_metadataobj.save_chart_from_toolbar(title_to_save=title_to_save, wait_time=wait_time)  
        
    def close_designer_chart_from_application_menu(self, select_confirm_dialog_button='No'):
        """
        Descriptions : This method will click on close option from application button menu in ribbon tool_bar.
        :Usage close_designer_chart_from_application_menu(select_confirm_dialog_button='Yes')
        """
        self._designer_metadataobj.close_chart_from_application_menu(confirm_dialog=select_confirm_dialog_button)
    
    def save_ro_from_toolbar(self, file_name):
        """
        Descriptions : This method will click on application button in ribbon tool_bar.
        :Usage click_application_button()
        """
        self._reporting_obj.select_top_toolbar_item(item_name='toptoolbar_save')
        self._utillity.ibfs_save_as(file_name, file_type=None)
    
    def click_application_button(self):
        """
        Descriptions : This method will click on application button in ribbon tool_bar.
        :Usage click_application_button()
        """
        self._designer_metadataobj.click_application_button()
    
    def select_option_from_application_menu(self, option_name):
        """
        Descriptions : This method will click on application button and select option from menu.
        :Usage select_option_from_application_menu('Save as...')
        """
        self._designer_metadataobj.select_option_from_application_menu(option_name)
        
    def verify_application_menu_options(self, expected_options_list, step_num, comparision_type='asequal', menu_item_path=None):
        """
        Descriptions : This method will click on application button and verify options listed in menu.
        :Usage verify_application_menu_options(['Chart'], '09.00', comparision_type='asin', menu_item_path='New')
        """
        self._designer_metadataobj.verify_application_menu_options(expected_options_list, step_num, comparision_type=comparision_type, menu_item_path=menu_item_path)
        
    def save_as_from_application_menu(self, title=None, name=None):
        """
        Descriptions : This method will handle save as dialog.
        :Usage save_as_from_application_menu(title='Chart', name='chart')
        """
        self._designer_metadataobj.save_as_from_application_menu(title=title, name=name)
        
    """ ************************************************************** This is common for PREVIEW and RUN WINDOW Section. *********************************************************************"""
    def verify_x_axis_title_in_preview(self, expected_title_list, parent_css=preview_parent_css, x_or_y_axis_title_css="text[class^='xaxis'][class$='title']", x_or_y_axis_title_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify X-axis title.'
        self._ia_resultobject.verify_xy_axis_title(expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_y_axis_title_in_preview(self, expected_title_list, parent_css=preview_parent_css, x_or_y_axis_title_css="text[class='yaxis-title']", x_or_y_axis_title_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Y-axis title.'
        self._ia_resultobject.verify_xy_axis_title(expected_title_list, parent_css=parent_css, x_or_y_axis_title_css=x_or_y_axis_title_css, x_or_y_axis_title_length=x_or_y_axis_title_length, msg=custom_msg)
    
    def verify_x_axis_label_in_preview(self, expected_label_list, parent_css=preview_parent_css, xyz_axis_label_css="svg > g text[class^='xaxis'][class*='labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify X-axis label.'
        self._ia_resultobject.verify_xyz_labels(expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
    def verify_y_axis_label_in_preview(self, expected_label_list, parent_css=preview_parent_css, xyz_axis_label_css="svg > g text[class^='yaxis-labels']", xyz_axis_label_length=None, msg='Step X'):
        custom_msg=msg + ' : Verify Y-axis label.'
        self._ia_resultobject.verify_xyz_labels(expected_label_list, parent_css, xyz_axis_label_css, xyz_axis_label_length=xyz_axis_label_length, msg=custom_msg)
    
        
    def verify_chart_color_using_get_css_property_in_preview(self, riser_css, color_name, parent_css=preview_parent_css, attribute='fill', msg='Step X'):
        '''
        Descriptions: This function is used to verify chart color using css property. attribute can be 'fill' OR 'stroke'.
        '''
        custom_msg=msg + ": Verify chart color."
        self._miscelaneousobject.verify_chart_color(parent_css, riser_css, color_name, 'get_css_property', attribute, custom_msg)
        
    def verify_number_of_risers(self, parent_css_with_tagname, risers_per_segment, expected_number, msg='Step X'):
        '''
        Descriptions: This function is used to verify pie labels within a single group.
        '''
        custom_msg= msg + " : Verify number of risers available."
        self._ia_resultobject.verify_number_of_risers(parent_css_with_tagname, risers_per_segment, expected_number, custom_msg)
        
    def verify_legends_in_preview(self, expected_legend_list, parent_css=preview_parent_css, legend_length=None, msg='Step X'):
        '''
        Descriptions: This function is used to verify legend labels
        '''
        custom_msg= msg + " : Verify the legend labels."
        self._ia_resultobject.verify_legends(expected_legend_list, parent_css, legend_length=legend_length, msg=custom_msg)
        
    def verify_ro_tree_item_list(self, expected_ro_tree_item_list, msg='Step X'):
        custom_msg= msg + ": To verify ro tree item list."
        self._reporting_obj.verify_ro_tree_item(ro_tool_name=expected_ro_tree_item_list, msg=custom_msg)   
        
    
    def create_data_grid_set(self, file_name):
        """
        Description: Read the all data from Data grid and write data in workbook
        :Usage : create_data_grid_set('test')
        """
        self._designer_metadataobj.create_data_set(file_name)
    
    def verify_data_grid_set(self, file_name, step_num):
        """
        Description: Read the all data from Data grid and compare with exists data
        :Usage : verify_data_grid_set('test', '09.00')
        """
        self._designer_metadataobj.verify_data_grid_set(file_name, step_num)
    
    def verify_data_grid_tooltip(self, cell_data, expected_tooltip_list, msg, row_index=None, col_index=None):
        """
        Description: Read the all data from Data grid and compare with exists data
        :Usage : verify_data_grid_tooltip('$49,598,845.24', 'Step 09.00: Verify tool-tip value.')
        """
        self._designer_metadataobj.verify_data_grid_tooltip('#jschart_HOLD_0', cell_data, expected_tooltip_list, msg, row_index=row_index, col_index=col_index)
         
    """ ************************************************************** Status bar tab section. *********************************************************************"""
    
    def select_tab_button(self, button_name):
        """
        Descriptions : This method will select tab button(bottom left hand corner) from designer.
        :Usage select_tab_button('Data')
        """
        self._designer_metadataobj.select_tab_button(button_name)
    
    """******************************************************************** This is common for Data page Section*************************************************************************************"""
    
    def click_data_node_folder(self, node_path):
        """
        Descriptions : This method will click on node path based on hierarchy.
        :usage : click_data_node_folder('baseapp/facts/wf_retail_sales')
        """
        self._designer_metadataobj.click_data_node_folder(node_path)
        
    def right_data_node_folder(self, join_node_name, option_name):
        """
        Descriptions : This method will click['left', 'right'] join node on canvas.
        :Usage click_join_object_node_on_canvas('Join 1')
        """
        self._designer_metadataobj.click_join_object_node_on_canvas(join_node_name, click_type='right', click_options=option_name)
    
    def drag_and_drop_node_folder_to_join_obj(self, node_path, join_node_name):
        """
        Descriptions : This method will click on node path based on hierarchy then get data tree node and drop on join node canvas.
        :Usage drag_and_drop_node_folder_to_join_obj('baseapp/facts/wf_retail_sales', 'join 1')
        """
        self._designer_metadataobj.drag_and_drop_node_folder_to_join_obj(node_path, join_node_name)
        
    def select_query_bucket_field_context_menu(self,bucket_name,field_name,context_menu_item_path,field_position=1, click_type='left',element_location='middle',xoffset=0):
        """
        Descriptions : This function will right click on query bucket and select bucket
        :Usage select_query_bucket_field_context_menu('Vertical', 'SALARY', 'Shape->Line')
        """
        self._designer_metadataobj.right_click_and_select_option_from_query_pane(bucket_name, field_name, context_menu_item_path, field_position, click_type=click_type,element_location=element_location,xoffset=xoffset)
    
    def verify_query_bucket_field_context_menu(self, expected_context_menu_item_list, msg, comparision_type='asequal', context_menu_item_path=None):
        """
        Descriptions : This function will right click on query bucket and verify options
        :Usage verify_query_bucket_field_context_menu(['Line'], 'Step 09.00: Verify option', comparision_type='asin', context_menu_item_path='Shape')
        """
        self._designer_metadataobj.verify_right_click_and_option_from_query_pane(expected_context_menu_item_list, msg, comparision_type=comparision_type, context_menu_item_path=context_menu_item_path)
        
    def verify_query_bucket_field_option_in_context_menu_checked(self, expected_context_menu_item_list, msg, comparision_type='asequal', context_menu_item_path=None):
        """
        Descriptions : This function will right click on query bucket and verify option is checked.
        :Usage verify_query_bucket_field_option_in_context_menu_checked(['Line'], 'Step 09.00: Verify option', comparision_type='asin', context_menu_item_path='Shape')
        """
        self._designer_metadataobj.verify_right_click_and_option_is_checked_unchecked_from_query_pane(expected_context_menu_item_list, 'check', msg, comparision_type=comparision_type, context_menu_item_path=context_menu_item_path)
        
    def verify_query_bucket_field_option_in_context_menu_unchecked(self, expected_context_menu_item_list, msg, comparision_type='asequal', context_menu_item_path=None):
        """
        Descriptions : This function will right click on query bucket and verify option is unchecked.
        :Usage verify_query_bucket_field_option_in_context_menu_unchecked(['Line'], 'Step 09.00: Verify option', comparision_type='asin', context_menu_item_path='Shape')
        """
        self._designer_metadataobj.verify_right_click_and_option_is_checked_unchecked_from_query_pane(expected_context_menu_item_list, 'uncheck', msg, comparision_type=comparision_type, context_menu_item_path=context_menu_item_path)
        
    def set_color_ranges_dialog(self):
        """
        Description : This method will return common.locators.designer.chart.SetColorRangesDialog class object.
        Using this object we can perform all "Set Color Ranges" dialog action.
        :Usage - set_color_ranges_dialog().select_color("Green")
        """
        return SetColorRangesDialog(self.driver)
    
    def switch_to_run_preview_frame(self):
        """
        Description : Will switch to run preview iframe
        """
        self._core_utils.switch_to_frame(".ides-tool-preview-frame iframe")
    
    def switch_to_default_content(self):
        """
        Description : Seitch to default content from ifrmae
        """
        self._core_utils.switch_to_default_content()
    
    def controls_menu_dialog(self):
        """
        Description : This method will return common.locators.designer.chart.ControlsMenuDialog class object.
        Using this object we can perform all "Controls Menu" dialog action.
        :Usage - controls_menu_dialog().select_combobox_option("Aggregation", "Sum")
        """
        return ControlsMenuDialog(self.driver)
    
    def click_new_embedded_page(self):
        """
        Description : Left click on "New Embedded Page" option at bottom of the workbook
        """
        button = self._utillity.validate_and_get_webdriver_object("div[title='New embedded page']", "Workbook New embedded page")
        self._core_utils.left_click(button)
        self._utillity.synchronize_with_visble_text(".pop-top", "template", 120)
        
class Designer_Insight(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    
    def __init__(self, driver):
        super(Designer_Insight, self).__init__(driver)
        self._utillity = UtillityMethods(self.driver)
        self._miscelaneousobject = IA_Miscelaneous(self.driver)
        self._ia_resultobject = IA_Resultarea(self.driver)
        self._designer_insightobj = Designer_Insight_Metadata(self.driver)
        self._reporting_obj = Wf_Reporting_Object(self.driver)
        self._pd_previewobj = pd_preview(self.driver)
        self._pd_designobj = pd_design(self.driver)
        
    def select_more_options_in_preview(self, item_path):
        """
        Description : This method will click on more options and select item
        :Usage select_more_options_in_preview('Export Data')
        """
        self._designer_insightobj.select_more_options(item_path)
        
    def verify_insight_querybox_text_options(self, query_list, msg, compare_type='asequal'):
        """
        Description: This method is used to verify the query list in insight
        :Usage : verify_insight_querybox_text_options(['Size'], "Step 4.3")
        """
        self._designer_insightobj.verify_insight_querybox(query_list, msg, compare_type=compare_type)
    
    def verify_insight_optionsbox_text(self, options_list, msg, compare_type='asequal'):
        """
        Description: This method is used to verify the options list in insight
        :Usage : verify_insight_optionsbox_tex(['More Options'], "Step 4.3")
        """
        self._designer_insightobj.verify_insight_optionsbox(options_list, msg, compare_type=compare_type)
        
    def select_chart_from_chartpicker(self, chart_option=None):
        """
        Description: This function is used to select the chart
        :Usage : select_chart_from_chartpicker(chart_option='Horizontal Bar')
        :Params : Use the following parameters are arguments
        Horizontal Bar
        Vertical Bar
        Vertical Stacked Bar
        Ring Pie
        Vertical Line
        Area
        Scatter
        Circle Plot
        Treemap
        Histogram
        Table
        Matrix
        Point Map
        Choropleth Map
        """
        self._designer_insightobj.select_chart_from_grid(chart_option=chart_option)
    
    def verify_insight_query_bucket_sort(self, bucket_name, sorted_value, msg, sorted_by='ascending'):
        """
        Description: This function is verify the query bucket
        :Usage : verify_query_bucket_sort('Horizontal Axis', 'Product Category', 'Step 4', sorted_by='ascending')
        :Params : sorted_by = 'ascending' or 'descending'
        """
        self._designer_insightobj.verify_query_bucket_sort(bucket_name, sorted_value, msg, sorted_by=sorted_by)
    
    def select_insight_optionsbox_in_preview(self, option):
        """
        Description: This function is used to select the options
        :Usage : select_insight_optionsbox_in_preview('Save')
        """
        self._designer_insightobj.select_insight_optionsbox(option)

class Designer_calculation_edit_format(BasePage):
    def __init__(self, driver):
        super(Designer_calculation_edit_format, self).__init__(driver)
        self._designer_metadataobj = Designer_Metadata(self.driver)
        self._data_format_dialog = dataformatdialog.DataFormatDialog(self.driver)
        self._alpha_type = dataformatdialog.AlphaType(self.driver)
        self._numeric_type = dataformatdialog.NumericType(self.driver)
        self._date_type = dataformatdialog.DateType(self.driver)
        self._custom_type = dataformatdialog.CustomType(self.driver)
        self._data_format = dataformat_dialog.DataFormat_Dialog(self.driver)
    
    def click_edit_format_on_calculation_dialog(self):   
        '''
        Description: This function is used click edit format button and perform some operation.
        :Usage : click_edit_format_on_calculation_dialog()
        '''
        self._designer_metadataobj.click_edit_format_on_calculation_dialog()
        
    def verify_dialog_visible(self, step_no):
        '''
        Description: This function verify edit format dialog visible.
        :Usage : verify_edit_format_dialog_visble('09.00')
        '''
        self._data_format_dialog.verify_data_format_dialog_is_visible(step_no)
            
    def close_dialog(self, button_name):
        '''
        Description: This function is used click edit format button and close it.
        :Usage : close_edit_format_dialog('OK')
        '''
        self._data_format.close_data_format_dialog_using_ok_cancel_button(button_name, synch=False)
    
    def select_datatype_in_dialog(self, datatype_format):
        '''
        Description: This function is used click datatype format in edit format dialog.
        @param datatype_format:'alpha', 'numeric', 'date' or 'custom'
        :Usage : select_datatype_in_edit_format('alpha')
        '''
        self._data_format_dialog.select_datatype(datatype_format)
        
    def verify_selected_datatype_in_dialog(self, datatype_format, step_no, color_name='whisper'):
        '''
        Description: This function is used verify selected datatype format in edit format dialog.
        @param datatype_format:'alpha', 'numeric', 'date' or 'custom'
        :Usage : verify_selected_datatype_in_edit_format_dialog('alpha', '09.00')
        '''
        self._data_format_dialog.verify_selected_datatype(datatype_format, step_no, color_name)
        
    def verify_length_value_in_alpha(self, expected_lenght, step_no):
        '''
        Description: This function is used verify length value in alpha section.
        :Usage : verify_length_value_in_alpha('9', '09.00')
        '''
        self._alpha_type.verify_length_inside_dataformat_dialog(expected_lenght, step_no)
        
    def modify_length_value_in_alpha(self, input_value):
        '''
        Description: This function is used modigy length value in alpha section.
        :Usage : verify_length_value_in_alpha('9')
        '''
        self._alpha_type.modify_length_value_using_keybord_input_inside_dataformat_dialog(input_value)
    
    def select_lenght_max_min_arrow_button_in_alpha(self, button_name):
        '''
        Description: This function will click on up/down arrow button in alpha section.
        @param check_uncheck_toggle:'max' or 'min'
        :Usage select_lenght_max_min_arrow_button_in_alpha('max')
        '''
        self._alpha_type.select_max_value_in_alpha_max_length_dropdown(button_name)
    
    def verify_variable_length_check_uncheck_in_alpha(self, check_uncheck_toggle, step_num):
        '''
        Description: This function is used verify variable length check_box status check/uncheck in alpha section.
        @param check_uncheck_toggle:'check' or 'uncheck'
        :Usage : verify_variable_length_check_uncheck_in_alpha('check')
        '''
        status_ = True if check_uncheck_toggle == 'check' else False
        self._alpha_type.verify_variable_length_checkbox_inside_dataformat_dialog('Variable length', status_, step_num)
        
    def select_variable_length_check_uncheck_in_alpha(self, check_uncheck_toggle):
        '''
        Description: This function is used select variable length check_box for toggle check/uncheck in alpha section.
        @param check_uncheck_toggle:'check' or 'uncheck'
        :Usage : select_variable_length_check_uncheck_in_alpha('check')
        '''
        status_ = False if check_uncheck_toggle == 'check' else True
        self._alpha_type.select_variable_length_checkbox_inside_dataformat_dialog('Variable length', status_)
    
    def verify_selected_datatype_in_numeric(self, numeric_datatype, step_no, color_name='whisper'):
        '''
        Description: This function is used verify selected numeric data_type format in numeric section.
        @param numeric_datatype:'integer', 'decimal', 'currency', 'percentage'
        :Usage : verify_selected_datatype_in_numeric('integer', '09.00')
        '''
        self._numeric_type.verify_selected_numeric_datatype(numeric_datatype, step_no, color_name=color_name)
        
    def select_datatype_in_numeric(self, numeric_datatype):
        '''
        Description: This function is used select numeric data_type format in numeric section.
        @param numeric_datatype:'integer', 'decimal', 'currency', 'percentage'
        :Usage : select_datatype_in_numeric('integer')
        '''
        self._numeric_type.select_numeric_type(numeric_datatype)
    
    def verify_max_length_in_numeric(self, expected_lenght, step_no):
        '''
        Description: This function is used verify maximum length value in numeric section.
        :Usage : verify_max_length_in_numeric('9', '09.00')
        '''
        self._numeric_type.verify_max_length(expected_lenght, step_no)
    
    def verify_decimal_place_in_numeric(self, expected_lenght, step_no):
        '''
        Description: This function is used verify decimal place value in numeric section.
        :Usage : verify_decimal_place_in_numeric('9.0', '09.00')
        '''
        self._numeric_type.verify_decimal_place(expected_lenght, step_no)
    
    def modify_max_length_value_in_numeric(self, input_value):
        '''
        Description: This function is used change maximum length value in numeric section.
        :Usage : modify_max_length_value_in_numeric('9')
        '''
        self._numeric_type.modify_max_length_value(input_value)
    
    def modify_decimal_place_value_in_numeric(self, input_value):
        '''
        Description: This function is used change decimal place value in numeric section.
        :Usage : modify_decimal_place_value_in_numeric('9.0')
        '''
        self._numeric_type.modify_decimal_place_value(input_value)
    
    def select_negative_numbers_in_numeric(self, negative_number_type):
        '''
        Description: This function will select negative numbers  in numeric section.
        @param negative_number_type:'-123' or '(123)'
        :Usage select_negative_numbers_in_numeric('(123)')
        '''
        self._numeric_type.select_negative_numbers(negative_number_type)
    
    def verify_negative_numbers_in_numeric(self, step_no, expected_selected_value=None, expected_nonselected_value=None, color_name='whisper'):
        '''
        Description: This function will verify selected negative numbers in numeric section.
        :Usage verify_negative_numbers_in_numeric('09.00', expected_selected_value='(123)', expected_nonselected_value='-123')
        '''
        self._numeric_type.verify_negative_numbers(step_no, expected_selected_value, expected_nonselected_value, color_name)
    
    def select_checkbox_in_numeric(self, checkbox_label_name, command_value):
        '''
        Description: This function will select or unselect checkbox under numeric section. 
        :Usage select_checkbox_inside_numeric_dataformat_dialog('Show 1000 separator', check)
        '''
        check_uncheck_toggle = False if command_value == 'check' else True
        self._numeric_type.select_checkbox_inside_numeric_dataformat_dialog(checkbox_label_name, check_uncheck_toggle)
    
    def verify_checkbox_in_numeric(self, checkbox_label_name, command_value, step_num):
        '''
        Description: This function will verify checkbox under numeric section. 
        :Usage verify_checkbox_inside_dataformat_dialog('Show 1000 separator', check, '09.00')
        '''
        check_uncheck_toggle = True if command_value == 'check' else False
        self._numeric_type.verify_checkbox_inside_numeric__dataformat_dialog(checkbox_label_name, check_uncheck_toggle, step_num)
    
    def verify_checkbox_is_disable_in_numeric(self, label_name, checkbox_state, step_num):
        '''
        This function will verify the check box section is disabled.
        '''
        self._numeric_type.verify_checkbox_disable_in_dataformat_popup(label_name, checkbox_state, step_num)
    
    def verify_symbol_position_disabled_in_numeric(self, step_number, checkbox_state='enable'):
        '''
        Description: This function will verify the symbol position section is disabled.
        :Usage verify_symbol_position_disabled_in_numeric('09.00')
        '''
        self._numeric_type.verify_symbol_position_disabled(step_number, checkbox_state=checkbox_state)
        
    def select_currency_symbol_in_numeric(self, currency_symbol_name):
        '''
        Description: This function will verify currency symbol.
        @param currency_symbol_name: 'Base on locale' or 'Dollar' or 'Euro' or 'Pound sterling' or 'Japanese yen'
        :usage select_currency_symbol_in_numeric('Euro')
        '''
        self._numeric_type.select_currency_symbol(currency_symbol_name)
    
    def verify_currency_symbol_in_numeric(self, expected_currency_symbol_name, step_no):
        '''
        Description: This function will verify currency symbol value 'Base on locale'.
        @param expected_currency_symbol_name: 'Base on locale' or 'Dollar' or 'Euro' or 'Pound sterling' or 'Japanese yen'
        :usage verify_currency_symbol_in_numeric('Euro', '09.00')
        '''
        self._numeric_type.verify_currency_symbol(expected_currency_symbol_name, step_no)
    
    def select_symbol_position_in_numeric(self, symbol_position_type):
        '''
        Description:  This function will select symbol position either 'Fixed' or 'Floating'.
        @param symbol_position_type:'Fixed', 'Floating'.
        :usage select_symbol_position('Fixed')
        '''
        self._numeric_type.select_symbol_position(symbol_position_type)
    
    def verify_symbol_position_in_numeric(self, step_no, expected_selected_value=None, expected_nonselected_value=None, color_name='whisper'):
        '''
        Description: This function will verify symbol position 'Fixed', 'Floating'.
        :usage verify_symbol_position_in_numeric('09.00', expected_selected_value='Fixed', expected_nonselected_value='Floating')
        '''
        self._numeric_type.verify_symbol_position(step_no, expected_selected_value=expected_selected_value, expected_nonselected_value=expected_nonselected_value, color_name=color_name)
    
    def select_date_format_in_date(self, format_name):
        '''
        Description:  This function will select date format value from drop_down under date section.
        :Usage select_date_format_in_date('2019/12/31')
        '''
        self._date_type.select_date_format(format_name)
    
    def select_date_separator_in_date(self, separator_name):
        '''
        Description:  This function will select date separator value from drop_down under date section.
        :Usage select_date_separator_in_date('2019/12/31')
        '''
        self._date_type.select_date_separator(separator_name)
    
    def verify_date_format_in_date(self, format_name, step_no):
        '''
        Description:  This function will verify date format value under date section.
        :Usage verify_date_format_in_date('2019/12/31', '09.00')
        '''
        self._date_type.verify_date_format(format_name, step_no)
    
    def verify_date_separator_in_date(self, separator_name, step_no):
        '''
        Description:  This function will verify date separator value under date section.
        :Usage verify_date_separator_in_date('2019/12/31', '09.00')
        '''
        self._date_type.verify_date_separator(separator_name, step_no)

    def modify_format_in_custom(self, input_value):
        '''
        Description:  This function will modify format value under custom section.
        :Usage modify_format_in_custom('20')
        '''
        self._custom_type.modify_format_using_keybord_input(input_value)
      
    def verify_format_in_custom(self, expected_format, step_no):
        '''
        Description: This function will verify format value under custom section.
        :Usage verify_format_in_custom('20', '09.00')
        '''
        self._custom_type.verify_format(expected_format, step_no)
    