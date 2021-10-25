from common.locators.page_designer_locators import PageDesigner as PD_LOCATORS
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as pd_miscelaneous
from common.lib.core_utility import CoreUtillityMethods as coreutils
from common.lib.utillity import UtillityMethods as utils
from common.lib.javascript import JavaScript as javascript
from selenium.webdriver.support.ui import Select
from common.lib.base import BasePage
from time import strptime
import time
import pyautogui
import sys

if sys.platform == 'linux':
    from pymouse import PyMouse
    mouse_=PyMouse()
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    from uisoup import uisoup
    import keyboard as virtual_keyboard

FILTER_DROPDOWN_ICON_CSS=PD_LOCATORS.FILTER_DROPDOWN_PARENT_CSS + " div[class^='ibx-select-open-btn']"

class PageDesignerPreview(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(PageDesignerPreview, self).__init__(driver)

    
    def enter_input_value_for_filter_control(self, condition_name, input_value_to_enter, control_position=1):
        """
        Descriptions : This method used to enter value to filter condition
        example usage : enter_input_value_for_filter_control('Business Region:', 'Car')
        """
        condtion_obj=pd_miscelaneous.get_pd_filter_control_object(self, condition_name, control_position)
        inpubox=condtion_obj.find_element_by_css_selector("div[data-ibx-type='ibxTextField']>input")
        coreutils.left_click(self, inpubox)
        inpubox.clear()
        time.sleep(1)
        inpubox.send_keys(input_value_to_enter)
        pyautogui.press('enter')
        time.sleep(5)
    
    def verify_preview_is_displayed(self, msg):
        """
        Descriptions : This method used to verify whether preview page is displayed or not after click on preview button
        example usage : verify_preview_is_displayed('Step 01.1 : Verify page preview window display')
        """
        left_pane_css="div[class^='pd-left-pane']"
        right_pane_css="div[class^='pd-right-pane']"
        bottom_pane_css="div[data-ibx-type='ibxHTabGroup'][class*='ibx-tab-position-bottom'][style*='none']"
        toolbar_pane_css="div[class^='pd-toolbar'][data-ibx-type='ibxHBox']"
        page_canvas_css="div[data-ibx-type='pdPageTab']"
        innerwidth=int(self.driver.execute_script('return window.innerWidth'))
        innerheight=int(self.driver.execute_script('return window.innerHeight'))
        page_canvas_obj=self.driver.find_element_by_css_selector(page_canvas_css)
        bottom_pane_visibility=self.driver.find_element_by_css_selector(bottom_pane_css).is_displayed()
        page_canvas_visibility=page_canvas_obj.is_displayed()
        toolbar_Y=int(self.driver.find_element_by_css_selector(toolbar_pane_css).location['y'])
        left_pane_X=int(self.driver.find_element_by_css_selector(left_pane_css).location['x'])
        right_pane_X=int(self.driver.find_element_by_css_selector(right_pane_css).location['x'])
        page_canvas_W=int(page_canvas_obj.size['width'])
        page_canvas_H=int(page_canvas_obj.size['height'])
        page_canvas_X=int(page_canvas_obj.location['x'])
        page_canvas_Y=int(page_canvas_obj.location['y'])    
        if page_canvas_visibility==True and page_canvas_W in range(innerwidth-1, innerwidth+1) and page_canvas_H in range(innerheight-1, innerheight+1) and page_canvas_X==0 and page_canvas_Y==0 and toolbar_Y<0 and left_pane_X<0 and right_pane_X>=innerwidth and bottom_pane_visibility==False:
            status=True
        else :
            status=False
        utils.asequal(self, True, status, msg)
    
    def go_back_to_design_from_preview(self, wait_time=3):
        """
        Descriptions : This method used to back to design page from preview window 
        example usage : go_back_to_design_from_preview()
        """
        back_design_obj=self.driver.find_element(*PD_LOCATORS.GO_BACK_DESIGN)
        coreutils.python_move_to_element(self, back_design_obj, element_location='bottom_middle', yoffset=-5)
        time.sleep(1)
        coreutils.left_click(self, back_design_obj)
        time.sleep(wait_time)
    
    def verify_filter_dropdown_options(self, filter_control_name, expected_options, msg, filter_control_position=1, verify_selected_options=False):
        """
        Descriptions : This method used to verify filter drop down options
        example usage : verify_filter_dropdown_options('Select North America', ['South America', 'EMEA'], 'Step 01.1 : Verify ['South America', 'EMEA'] options are display in filter drop down')
        """
        options_parent_css="div[data-ibx-type*='Popup'][class*='pop-top']"
        if verify_selected_options == True :
            options_css="div[class*='sel-selected'][data-ibx-type^='ibxSelect']"
        else :
            options_css="div[class^='ibx-page'][data-ibx-type^='ibxSelect']"
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        dropdown_icon_obj=filter_control_obj.find_element_by_css_selector(FILTER_DROPDOWN_ICON_CSS)
        coreutils.python_left_click(self, dropdown_icon_obj)
        utils.synchronize_with_number_of_element(self, options_parent_css, 1, 10)
        dropdown_options_css=options_parent_css + " " + options_css
        dropdown_options_obj=self.driver.find_elements_by_css_selector(dropdown_options_css)
        actaul_options=[option.text.strip() for option in dropdown_options_obj]
        utils.asequal(self, expected_options, actaul_options, msg)
        dropdown_icon_obj=filter_control_obj.find_element_by_css_selector(FILTER_DROPDOWN_ICON_CSS)
        coreutils.left_click(self, dropdown_icon_obj)
        
    def __select_filter_dropdown_options(self, filter_control_name, option_list_to_select, filter_control_position=1, use_ctrl=False, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to select one or more drop down options
        example usage : __select_filter_dropdown_options('Select North America', ['South America', 'EMEA'])
        if you want select multiple options bu pressing ctrl then pass use_ctrl=True
        """
        if type(option_list_to_select) is not list:
            select_option_list=[option_list_to_select]
        else:
            select_option_list=option_list_to_select
        options_parent_css="div[data-ibx-type*='Popup'][class*='pop-top']"
        options_css="div[class^='ibx-page'][data-ibx-type^='ibxSelect']"
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        dropdown_icon_obj=filter_control_obj.find_element_by_css_selector(FILTER_DROPDOWN_ICON_CSS)
        coreutils.python_left_click(self, dropdown_icon_obj)
        utils.synchronize_with_number_of_element(self, options_parent_css, 1, 10)
        dropdown_options_css=options_parent_css + " " + options_css
        if use_ctrl == True :
            if sys.platform == 'linux':
                pykeyboard.press_key(pykeyboard.control_key)
            else:
                virtual_keyboard.press('ctrl')
        for option in select_option_list:
            dropdown_options_obj=self.driver.find_elements_by_css_selector(dropdown_options_css)
            try :
                option_index=javascript.find_element_index_by_text(self, dropdown_options_obj, option)
            except :
                if sys.platform == 'linux':
                    pykeyboard.release_key(pykeyboard.control_key)
                else:
                    virtual_keyboard.release('ctrl')
                option_index=None
            if option_index != None :
                dropdown_option_obj=dropdown_options_obj[option_index]
                coreutils.python_left_click(self, dropdown_option_obj)
            else :
                if use_ctrl == True :
                    if sys.platform == 'linux':
                        pykeyboard.release_key(pykeyboard.control_key)
                    else:
                        virtual_keyboard.release('ctrl')
                error_msg = "[{0}] option not found in filter drop down".format(option)
                raise KeyError(error_msg)
        if use_ctrl == True :
            if sys.platform == 'linux':
                pykeyboard.release_key(pykeyboard.control_key)
            else:
                virtual_keyboard.release('ctrl')
            
    def select_filter_dropdown_option(self, filter_control_name, option_list_to_select, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to select single drop down option
        example usage : select_filter_dropdown_option('Select North America', 'EMEA')
        """
        PageDesignerPreview.__select_filter_dropdown_options(self, filter_control_name, option_list_to_select, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def select_multiple_options_from_filter_dropdown(self, filter_control_name, option_list_to_select, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to select multiple options from drop down control
        example usage : select_multiple_options_from_filter_dropdown('Select North America', ['South America', 'EMEA'])
        """
        PageDesignerPreview.__select_filter_dropdown_options(self, filter_control_name, option_list_to_select, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        dropdown_icon_obj=filter_control_obj.find_element_by_css_selector(FILTER_DROPDOWN_ICON_CSS)
        coreutils.left_click(self, dropdown_icon_obj)
        time.sleep(8)
    
    def select_multiple_options_from_filter_dropdown_using_ctrl(self, filter_control_name, option_list_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select multiple options from drop down control by pressing ctrl
        example usage : select_multiple_options_from_filter_dropdown('Select North America', ['South America', 'EMEA'])
        """
        PageDesignerPreview.__select_filter_dropdown_options(self, filter_control_name, option_list_to_select, filter_control_position, use_ctrl=True)
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        dropdown_icon_obj=filter_control_obj.find_element_by_css_selector(FILTER_DROPDOWN_ICON_CSS)
        coreutils.left_click(self, dropdown_icon_obj)
        time.sleep(8)
    
    def select_filter_buttonset_options(self, filter_control_name, options_list_to_select, filter_control_position=1, use_ctrl=False):
        """
        Descriptions : This method used to select button set options.You can select more than one options at same time.
        :arg = use_ctrl : if you want select multiple options using ctrl then pass use_ctrl=True
        example usage : select_filter_buttonset_options('Select North America', ['EMEA', 'South America'])
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        buttonset_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_BUTTONSET_OPTIONS_CSS)
        if use_ctrl == True :
            if sys.platform == 'linux':
                pykeyboard.press_key(pykeyboard.control_key)
            else:
                virtual_keyboard.press('ctrl')
        for option in options_list_to_select :
            try :
                option_index=javascript.find_element_index_by_text(self, buttonset_options_list, option)
            except :
                if sys.platform == 'linux':
                    pykeyboard.release_key(pykeyboard.control_key)
                else:
                    virtual_keyboard.release('ctrl')
                option_index=None
            if option_index != None :
                option_obj = buttonset_options_list[option_index]
                coreutils.python_left_click(self, option_obj)
            else :
                error = "[{0}] option not found in filter button set control".format(option)
                if use_ctrl == True :
                    if sys.platform == 'linux':
                        pykeyboard.release_key(pykeyboard.control_key)
                    else:
                        virtual_keyboard.release('ctrl')
                raise KeyError(error)
        if use_ctrl == True :
            if sys.platform == 'linux':
                pykeyboard.release_key(pykeyboard.control_key)
            else:
                virtual_keyboard.release('ctrl')
        time.sleep(8)
    
    def select_filter_radio_group_options(self, filter_control_name, options_list_to_select, filter_control_position=1, use_ctrl=False):
        """
        Descriptions : This method used to select radio group options.
        :arg = use_ctrl : if you want select multiple options using ctrl then pass use_ctrl=True
        example usage : select_filter_radio_group_options('Select North America', ['EMEA'])
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        radio_group_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_RADIOGROUP_OPTIONS_CSS)
        if use_ctrl == True :
            if sys.platform == 'linux':
                pykeyboard.press_key(pykeyboard.control_key)
            else:
                virtual_keyboard.press('ctrl')
        for option in options_list_to_select :
            try :
                option_index=javascript.find_element_index_by_text(self, radio_group_options_list, option)
            except :
                if sys.platform == 'linux':
                    pykeyboard.release_key(pykeyboard.control_key)
                else:
                    virtual_keyboard.release('ctrl')
                option_index=None
            if option_index != None :
                option_obj = radio_group_options_list[option_index]
                radio_button_icon = option_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_RADIOGROUP_BUTTON_ICON_CSS)
                coreutils.python_left_click(self, radio_button_icon)
            else :
                error = "[{0}] option not found in filter button set control".format(option)
                if use_ctrl == True :
                    if sys.platform == 'linux':
                        pykeyboard.release_key(pykeyboard.control_key)
                    else:
                        virtual_keyboard.release('ctrl')
                raise KeyError(error)
        if use_ctrl == True :
            if sys.platform == 'linux':
                pykeyboard.release_key(pykeyboard.control_key)
            else:
                virtual_keyboard.release('ctrl')
        time.sleep(8)
    
    def clear_filter_date_value(self, filter_control_name, filter_control_position=1):
        """
        Descriptions : This method used to click on clear icon to clear  filer date value.
        example usage : select_date_from_single_date_picker('Select 2016/03/17')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        clear_icon = filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_DATE_CLEAR_ICON_CSS)
        coreutils.left_click(self, clear_icon)
        time.sleep(8)
        
    def select_date_from_single_date_picker(self, filter_control_name, month=None, year=None, day=None, filter_control_position=1):
        """
        Descriptions : This method used select month, year and day from single date picker.
        example usage : select_date_from_single_date_picker('Select 2016/03/17', month='Apr', year='1991', day='9')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        calendar_icon_obj = filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_DATE_PICKER_ICON_CSS)
        coreutils.python_left_click(self, calendar_icon_obj)
        utils.synchronize_with_visble_text(self, PD_LOCATORS.FILTER_DATE_PICKER_POPUP_PARENT_CSS + " span[title='Sunday']", 'Su', 10)
        if year != None :
            utils.select_dropdown(self, PD_LOCATORS.FILTER_DATE_PICKER_YEAR_SELECT_CSS, 'visible_text', year)
        if month != None :
            utils.select_dropdown(self, PD_LOCATORS.FILTER_DATE_PICKER_MONTH_SELECT_CSS, 'visible_text', month)
        if day != None :
            day_objs = self.driver.find_elements_by_css_selector(PD_LOCATORS.FILTER_DATE_PICKER_DATE_SELECT_CSS)
            day_index = javascript.find_element_index_by_text(self, day_objs, day)
            if day_index != None :
                coreutils.left_click(self, day_objs[day_index])
            else :
                error_msg ="Unable to find [{0}] in single date picker calendar".format(day)
                raise KeyError(error_msg)
            time.sleep(1)
        time.sleep(8)
    
    def select_date_from_date_range_picker(self, filter_control_name, start_date, end_date, filter_control_position=1):
        """
        Descriptions : This method used select starting and ending state from date range picker control.
        example usage : select_date_from_date_range_picker('Select 2016/03/10 and 2016/03/17', 'Mar-10-2016', 'Mar-17-2016')
        Note : start_date and end_date format should be like this 'Mar-10-2016'
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        calendar_icon_obj = filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_DATE_PICKER_ICON_CSS)
        coreutils.left_click(self, calendar_icon_obj)
        utils.synchronize_with_visble_text(self, PD_LOCATORS.FILTER_DATE_PICKER_POPUP_PARENT_CSS + " span[title='Sunday']", 'Su', 10)
        for count, date in enumerate([start_date, end_date]) :
            date_list = date.split('-')
            month = date_list[0]
            day = date_list[1]
            year = date_list[2]
            selected_year=Select(self.driver.find_element_by_css_selector(PD_LOCATORS.FILTER_DATE_PICKER_YEAR_SELECT_CSS)).first_selected_option.text
            start_month = Select(self.driver.find_element_by_css_selector(PD_LOCATORS.FILTER_DATE_PICKER_MONTH_SELECT_CSS)).first_selected_option.text
            end_month = self.driver.find_element_by_css_selector(PD_LOCATORS.FILTER_DATE_PICKER_POPUP_PARENT_CSS + " span[class='ui-datepicker-month']").text.strip()[:3]
            if selected_year != year :
                utils.select_dropdown(self, PD_LOCATORS.FILTER_DATE_PICKER_YEAR_SELECT_CSS, 'visible_text', year)
            if count == 0 and month != start_month :
                utils.select_dropdown(self, PD_LOCATORS.FILTER_DATE_PICKER_MONTH_SELECT_CSS, 'visible_text', month)
            if month not in [start_month, end_month] :
                utils.select_dropdown(self, PD_LOCATORS.FILTER_DATE_PICKER_MONTH_SELECT_CSS, 'visible_text', month)
            month_index = strptime(month,'%b').tm_mon - 1
            day_css = PD_LOCATORS.FILTER_DATE_PICKER_POPUP_PARENT_CSS + " table[class='ui-datepicker-calendar'] td[data-month='{0}'][data-year='{1}']".format(month_index, year)
            day_obj = self.driver.find_elements_by_css_selector(day_css)[int(day)-1]
            coreutils.left_click(self, day_obj)
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        coreutils.python_left_click(self, filter_control_obj, element_location='top_middle')
        time.sleep(8)
        
    def select_filter_checkbox_options(self, filter_control_name, options_list_to_select, filter_control_position=1):
        """
        Descriptions : This method used to select checkbox options.
        example usage : select_filter_checkbox_options('Select North America', ['EMEA'])
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        checkbox_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_CHECKBOX_OPTIONS_CSS)
        for option in options_list_to_select :
            option_index = javascript.find_element_index_by_text(self, checkbox_options_list, option)
            if option_index != None :
                option_obj = checkbox_options_list[option_index]
                radio_button_icon = option_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_CHECKBOX_OPTION_CHECK_ICON_CSS)
                coreutils.python_left_click(self, radio_button_icon)
            else :
                error = "[{0}] option not found in filter button set control".format(option)
                raise KeyError(error)
        time.sleep(8)
    
    def move_filter_slider(self, filter_control_name, slider_value_to_select, slider_marker=1, filter_control_position=1):
        """
        Descriptions : This method used to move slider to specific value by drag and drop slider marker. 
        :arg - slider_marker : If you want to select slider value by using slider marker 1 (left side) then pass slider_marker=1 else slider_marker=2 (right side)
        example usage : move_filter_slider('Move Slider to 5011', 5020, 2)
        """
        slider_marker_css = PD_LOCATORS.FILTER_SLIDER_MARKER1_CSS if slider_marker==1 else PD_LOCATORS.FILTER_SLIDER_MARKER2_CSS
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        slider_min_val = int(filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_SLIDER_MIN_VAL_CSS).text.strip())
        slider_max_val = int(filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_SLIDER_MAX_VAL_CSS).text.strip())
        if slider_value_to_select in range(slider_min_val, slider_max_val+1) :
            slider_line = filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_SLIDER_LINE_CSS)
            slider_line_width = slider_line.size['width']
            slider_line_xoffset = coreutils.get_web_element_coordinate(self, slider_line, element_location='middle_left')['x']
            slider_range = slider_max_val - slider_min_val
            slider_value_distance = slider_line_width / slider_range
            slider_value_range = slider_value_to_select - slider_min_val
            slider_value_xoffset = slider_value_distance * slider_value_range
            slider_marker = filter_control_obj.find_element_by_css_selector(slider_marker_css)
            slider_marker_mid_loc = coreutils.get_web_element_coordinate(self, slider_marker)
            source_x = slider_marker_mid_loc['x']
            source_y = slider_marker_mid_loc['y']
            target_x = slider_line_xoffset + slider_value_xoffset
            target_y = source_y
            if sys.platform == 'linux':
                mouse_.move(int(source_x), int(source_y))
                time.sleep(1)
                mouse_.press(int(source_x), int(source_y))
                time.sleep(1)
                pyautogui.moveTo(int(target_x), int(target_y), duration=3)
                time.sleep(1)
                mouse_.release(int(target_x), int(target_y))
                
            else:
                uisoup.mouse.move(source_x,source_y)
                time.sleep(1)
                uisoup.mouse.drag(source_x,source_y, target_x, target_y)
        else :
            error_msg = "Slider select value {0} is not in range({1}, {2})".format(slider_value_to_select, slider_min_val, slider_max_val)
            raise ValueError(error_msg)
        time.sleep(8)
        
    def move_filter_slider_range(self,  filter_control_name, range_value1=None, range_value2=None, filter_control_position=1):
        """
        Descriptions : This method used to move sliders to specific value by drag and drop slider markers. 
        example usage : move_filter_slider_range('Move Slider to 5011', slider_value1=5010, slider_value2=5015)
        """
        if range_value1 != None :
            PageDesignerPreview.move_filter_slider(self, filter_control_name, range_value1, 1, filter_control_position)
        if range_value2 != None :
            PageDesignerPreview.move_filter_slider(self, filter_control_name, range_value2, 2, filter_control_position)
        time.sleep(8)
