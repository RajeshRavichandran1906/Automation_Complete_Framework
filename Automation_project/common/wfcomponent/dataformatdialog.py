from common.lib.base import BasePage
from common.pages.dataformat_dialog import DataFormat_Dialog
from common.lib.utillity import UtillityMethods as utillobject

class DataFormatDialog(BasePage):
    
    def __init__(self, driver):
        super(DataFormatDialog, self).__init__(driver)
    
    def wait_for_number_of_element(self, element_css, expected_number, time_out=60):
        utillobject.synchronize_with_number_of_element(self, element_css, expected_number, time_out)
        
    def wait_for_visible_text(self, element_css, visble_text, time_out=60):
        utillobject.synchronize_with_visble_text(self, element_css, visble_text, time_out)
    
    def invoke_dataformattesterdlgonly_jsp(self):
        DataFormat_Dialog.invoke_dataformattesterdlgonly_jsp(self)
        
    def click_show_data_format_button(self):
        DataFormat_Dialog.click_show_data_format_button(self)
    
    def verify_selected_datatype(self, datatype_format, step_no, color_name='gray80'):
        msg = 'Step ' + str(step_no) + ': Verify if ' + datatype_format +' data format dialog is selected.'
        DataFormat_Dialog.verify_selected_datatype(self, datatype_format, msg, color_name=color_name)
    
    def select_datatype(self, datatype_format):
        '''
        This function will selected datatype field is either 'alpha', 'numeric', 'date' or 'custom'.
        
        @param datatype_format:'alpha', 'numeric', 'date' or 'custom'.
        :usage select_datatype('alpha')
        '''
        DataFormat_Dialog.select_datatype(self, datatype_format)
        
    def set_text_to_format_to_parse_input_box(self, input_value):
        DataFormat_Dialog.set_text_to_format_to_parse_input_box(self, input_value)  
        
    def verify_output_format_value(self, expected_output_value, step_no):
        msg = 'Step ' + str(step_no) + ': Verify output format value displays ' + expected_output_value + '.'
        DataFormat_Dialog.verify_output_format_value(self, expected_output_value, msg)
          
    def verify_data_format_dialog_is_visible(self, step_no):
        msg = 'Step ' + str(step_no) + ': Verify data format dialog appears.'
        DataFormat_Dialog.verify_data_format_dialog_is_visible(self, msg)
        
    def close_data_format_dialog_using_ok_button(self):
        DataFormat_Dialog.close_data_format_dialog_using_ok_cancel_button(self, 'ok')
    
    def close_data_format_dialog_using_cancel_button(self):
        DataFormat_Dialog.close_data_format_dialog_using_ok_cancel_button(self, 'cancel')
        
class AlphaType(BasePage):
    
    def __init__(self, driver):
        super(AlphaType, self).__init__(driver)
        
    def verify_datatype_fields(self):
        pass
    
    def verify_length_inside_dataformat_dialog(self, expected_lenght, step_no):
        msg = 'Step ' + str(step_no) + ': Verify if ' + expected_lenght +' is displaying inside data format dialog.'
        DataFormat_Dialog.verify_length(self, expected_lenght, msg)
    
    def modify_length_value_using_keybord_input_inside_dataformat_dialog(self, input_value):
        DataFormat_Dialog.modify_length_value_using_keybord_input(self, input_value)
        
    def verify_variable_length_checkbox_inside_dataformat_dialog(self, label_name, check_uncheck_toggle, step_num):
        DataFormat_Dialog.verify_checkbox_in_dataformat_popup(self, label_name, check_uncheck_toggle, step_num)
        
    def select_variable_length_checkbox_inside_dataformat_dialog(self, label_name, check_uncheck_toggle):
        '''
        This function will select or unselect checkbox under alpha section. 
        
        Note: 
            if need to check checkbox then pass 'check_uncheck_toggle' is False.
            if need to uncheck checkbox then pass 'check_uncheck_toggle' is True.
        
        @param label_name: 'Show 1000 separator' or 'Show leading zero'
        @param check_uncheck_toggle: True or False
        :Usage select_variable_length_checkbox_inside_dataformat_dialog('Show 1000 separator', True)
        '''
        DataFormat_Dialog.select_checkbox_in_dataformat_popup(self, label_name, check_uncheck_toggle)
        
    def select_max_value_in_alpha_max_length_dropdown(self, value_type='max'):
        '''
        This function will click on up arrow button in numeric max legnth dropdown
        :usage select_max_value_in_alpha_max_length_dropdown()
        '''
        DataFormat_Dialog.select_max_or_min_value_in_alpha_max_length_dropdown(self, value_type)
        
    def select_min_value_in_alpha_max_length_dropdown(self, value_type='min'):
        '''
        This function will click on down arrow button in numeric max legnth dropdown
        :usage select_min_value_in_alpha_max_length_dropdown()
        '''
        DataFormat_Dialog.select_max_or_min_value_in_alpha_max_length_dropdown(self, value_type)
    
    def select_value_in_alpha_max_length_dropdown(self, value):
        '''
        This function will click on down or up arrow button in numeric max legnth dropdown based on user value.
        current value is lesser than the given user value, it will click on up arrow else down arrow
        @param value=2
        :usage select_value_in_alpha_max_length_dropdown(2)
        '''    
        DataFormat_Dialog.select_value_in_alpha_max_length_dropdown(self, value)
    
class NumericType(BasePage):
    
    def __init__(self, driver):
        super(NumericType, self).__init__(driver)
    
    def verify_selected_numeric_datatype(self, numeric_datatype, step_no, color_name='gray80'):
        msg = 'Step {0}: Verify if {1} data format dialog is selected.'.format(str(step_no), str(numeric_datatype))
        DataFormat_Dialog.verify_selected_numeric_datatype(self, numeric_datatype, msg, color_name=color_name)
    
    def verify_max_length(self, expected_lenght, step_no):
        msg = 'Step {0}: Verify if {1} is displaying inside data format dialog.'.format(str(step_no), str(expected_lenght))
        DataFormat_Dialog.verify_max_length(self, expected_lenght, msg)
    
    def verify_decimal_place(self, expected_lenght, step_no):
        msg = 'Step {0}: Verify if {1} is displaying inside data format dialog.'.format(str(step_no), str(expected_lenght))
        DataFormat_Dialog.verify_decimal_place(self, expected_lenght, msg)
    
    def modify_max_length_value(self, input_value):
        DataFormat_Dialog.modify_max_length_value_using_keybord_input(self, input_value)
    
    def modify_decimal_place_value(self, input_value):
        DataFormat_Dialog.modify_decimal_place_value_using_keybord_input(self, input_value)
    
    def select_negative_numbers(self, negative_number_type):
        '''
        This function will select negative numbers label.
        
        @param negative_number_type:'-123' or '(123)'
        :Usage select_negative_numbers('(123)')
        '''
        DataFormat_Dialog.select_negative_numbers(self, negative_number_type)
    
    def verify_negative_numbers(self, step_no, expected_selected_value=None, expected_nonselected_value=None, color_name='gray80'):
        if expected_selected_value != None:
            msg = 'Step {0}: Verify if {1} is displaying inside data format dialog.'.format(str(step_no), str(expected_selected_value))
        if expected_nonselected_value != None:
            msg = 'Step {0}: Verify if {1} is displaying inside data format dialog.'.format(str(step_no), str(expected_nonselected_value))
        DataFormat_Dialog.verify_negative_numbers(self, expected_selected_value=expected_selected_value, expected_nonselected_value=expected_nonselected_value, msg=msg, color_name=color_name)
    
    def select_checkbox_inside_numeric_dataformat_dialog(self, label_name, check_uncheck_toggle):
        '''
        This function will select or unselect checkbox under numeric section. 
        
        Note: 
            if need to check checkbox then pass 'check_uncheck_toggle' is False.
            if need to uncheck checkbox then pass 'check_uncheck_toggle' is True.
        
        @param label_name: 'Show 1000 separator' or 'Show leading zero'
        @param check_uncheck_toggle: True or False
        :Usage select_checkbox_inside_numeric_dataformat_dialog('Show 1000 separator', True)
        '''
        DataFormat_Dialog.select_checkbox_in_dataformat_popup(self, label_name, check_uncheck_toggle)
    
    def verify_checkbox_inside_numeric__dataformat_dialog(self, label_name, check_uncheck_toggle, step_num):
        '''
        This function will verify checkbox under numeric section. 
        
        @param label_name: 'Show 1000 separator' or 'Show leading zero'
        @param check_uncheck_toggle: True or False
        @param step_num: '9'
        :Usage verify_checkbox_inside_dataformat_dialog('Show 1000 separator', True, '9')
        '''
        DataFormat_Dialog.verify_checkbox_in_dataformat_popup(self, label_name, check_uncheck_toggle, step_num)
    
    def verify_checkbox_disable_in_dataformat_popup(self, label_name, checkbox_state, step_num):
        '''
        This function will verify the check box section is disabled.
        '''
        DataFormat_Dialog.verify_checkbox_disable_in_dataformat_popup(self, label_name, checkbox_state, step_num)
    
    def select_numeric_type(self, numeric_datatype):
        '''
        This function will select numeric type.
        
        @param numeric_datatype:'integer' or 'decimal' or 'currency' or 'percentage'
        :Usage select_numeric_type('percentage')
        '''
        DataFormat_Dialog.select_numeric_type(self, numeric_datatype)
    
    def select_symbol_position(self, symbol_position_type):
        '''
        This function will select symbol position either 'Fixed' or 'Floating'.
        
        @param symbol_position_type:'Fixed', 'Floating'.
        :usage select_symbol_position('Fixed')
        '''
        DataFormat_Dialog.select_symbol_position(self, symbol_position_type)
    
    def verify_symbol_position(self, step_no, expected_selected_value=None, expected_nonselected_value=None, color_name='gray80'):
        '''
        This function will verify symbol position 'Fixed', 'Floating'.
        '''
        if expected_selected_value != None:
            msg = 'Step {0}: Verify if {1} is displaying inside data format dialog.'.format(str(step_no), str(expected_selected_value))
        if expected_nonselected_value != None:
            msg = 'Step {0}: Verify if {1} is displaying inside data format dialog.'.format(str(step_no), str(expected_nonselected_value))
        DataFormat_Dialog.verify_symbol_position(self, expected_selected_value=expected_selected_value, expected_nonselected_value=expected_nonselected_value, msg=msg, color_name=color_name)
    
    def verify_symbol_position_disabled(self, step_number, checkbox_state='enable'):
        '''
        This function will verify the symbol position section is disabled.
        '''
        DataFormat_Dialog.verify_symbol_position_disabled(self, step_number, checkbox_state=checkbox_state)
        
    def select_currency_symbol(self, currency_symbol_name):
        '''
        This function will verify currency symbol.
        User need to provide either 'Base on locale', 'Dollar', 'Euro', 'Pound sterling', 'Japanese yen'
        
        @param expected_currency_symbol_name: 'Base on locale' or 'Dollar' or 'Euro' or 'Pound sterling' or 'Japanese yen'
        @param step_no: '9'
        :usage verify_currency_symbol('Euro', '9')
        '''
        DataFormat_Dialog.select_currency_symbol(self, currency_symbol_name)
    
    def verify_currency_symbol(self, expected_currency_symbol_name, step_no):
        '''
        This function will verify currency symbol value 'Base on locale'.
        
        @param expected_currency_symbol_name:'Base on locale'.
        @param step_no:'9'.
        :usage verify_currency_symbol('Base on locale', '9')
        '''
        DataFormat_Dialog.verify_currency_symbol(self, expected_currency_symbol_name, step_no)
        
    def select_max_value_in_numeric_max_length_dropdown(self, value_type='max'):
        '''
        This function will click on up arrow button in numeric max legnth dropdown
        :usage select_max_value_in_numeric_max_length_dropdown()
        '''
        DataFormat_Dialog.select_max_or_min_value_in_numeric_max_length_dropdown(self, value_type)
        
    def select_min_value_in_numeric_max_length_dropdown(self, value_type='min'):
        '''
        This function will click on down arrow button in numeric max legnth dropdown
        :usage select_min_value_in_numeric_max_length_dropdown()
        '''
        DataFormat_Dialog.select_max_or_min_value_in_numeric_max_length_dropdown(self, value_type)
    
    def select_value_in_numeric_max_length_dropdown(self, value):
        '''
        This function will click on down or up arrow button in numeric max legnth dropdown based on user value.
        current value is lesser than the given user value, it will click on up arrow else down arrow
        @param value=2
        :usage select_value_in_numeric_max_length_dropdown(2)
        '''    
        DataFormat_Dialog.select_value_in_numeric_max_length_dropdown(self, value)
        
class DateType(BasePage):
    
    def __init__(self, driver):
        super(DateType, self).__init__(driver)
    
    def select_date_format(self, format_name):
        DataFormat_Dialog.select_date_format(self, format_name)
    
    def select_date_separator(self, separator_name):
        DataFormat_Dialog.select_date_separator(self, separator_name)
    
    def verify_date_format(self, format_name, step_no):
        DataFormat_Dialog.verify_date_format(self, format_name, step_no)
    
    def verify_date_separator(self, separator_name, step_no):
        DataFormat_Dialog.verify_date_separator(self, separator_name, step_no)

class CustomType(BasePage):
    
    def __init__(self, driver):
        super(CustomType, self).__init__(driver)
        
    def verify_format(self, expected_format, step_no):
        '''
        This function will verify format value under custom section.
        @param expected_format: '20'
        @param step_no: '9' 
        :Usage verify_format('20', '9')
        '''
        DataFormat_Dialog.verify_format(self, expected_format, step_no)
    
    def modify_format_using_keybord_input(self, input_value):
        '''
        This function will modify format value under custom section.
        @param input_value: '20'
        :Usage modify_format_using_keybord_input('20')
        '''
        DataFormat_Dialog.modify_format_using_keybord_input(self, input_value)
    