from common.lib import utillity
from common.lib.base import BasePage
from common.pages import visualization_ribbon
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.global_variables import Global_variables
import re, time, os, pyautogui
from selenium.webdriver.support.color import Color
import sys
from common.lib.core_utility import CoreUtillityMethods
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as virtual_keyboard

class IA_Style(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(IA_Style, self).__init__(driver)
         
        
    def _validate_page(self, locator, **kwargs):
        if 'wait_time' in kwargs:
            custom_wait = WebDriverWait(self.driver, kwargs['wait_time'])
            custom_wait.until(EC.visibility_of_element_located(locator))
        else:
            self.longwait.until(EC.visibility_of_element_located(locator))
    
    def set_color(self, color):
        color_dialog_popup_css="div[id*='ColorPicker'] div[class*='window-active']"
        color_picker_box_css = color_dialog_popup_css + " [class*='color-picker-box']"
        ok_btn_css=color_dialog_popup_css+" #BiColorPickerOkBtn"
        utillity.UtillityMethods.synchronize_with_visble_text(self, ok_btn_css, 'OK', 30, 2)
        rgb_color=utillity.UtillityMethods.color_picker(self, color)
        color_icons=self.driver.find_elements_by_css_selector(color_picker_box_css)
        for color_icon in color_icons:
            if rgb_color == Color.from_string(color_icon.value_of_css_property("background-color")).rgb:
                utillity.UtillityMethods.default_click(self, color_icon)
                time.sleep(2)
                break
        ok_elems=self.driver.find_element_by_css_selector(ok_btn_css)
        ok_elems.click()
        time.sleep(2)
    
    def set_color_(self, color):
        color_dialog_popup_css="div[id*='ColorPicker'] div[class*='window-active']"
        ok_btn_css=color_dialog_popup_css+" #BiColorPickerOkBtn"
        ok_elems=self.driver.find_element_by_css_selector(ok_btn_css)
        utillity.UtillityMethods.synchronize_with_number_of_element(self, ok_btn_css, 1, 25)
        rgb_color=utillity.UtillityMethods.color_picker(self, color)
        color_obj=re.match(r'rgb\((\d+)\,\s(\d+)\,\s(\d+)\)', rgb_color)
        red=self.driver.find_element_by_css_selector(color_dialog_popup_css+" input#RedTextField")
        green=self.driver.find_element_by_css_selector(color_dialog_popup_css+" input#GreenTextField")
        blue=self.driver.find_element_by_css_selector(color_dialog_popup_css+" input#BlueTextField")
        red.click()
        red.clear()
        red.send_keys(color_obj.group(1))
        time.sleep(1)
        green.click()
        green.clear()
        green.send_keys(color_obj.group(2))
        time.sleep(1)
        blue.click()
        blue.clear()
        blue.send_keys(color_obj.group(3))
        time.sleep(1)
        ok_elems.click()
        time.sleep(2)
   
    def set_field_style(self, **kwargs):
        '''
        params: font_name='Ariel'
        params: font_size=12
        params: bold=True
        params: italic=True
        params: underline=True
        params: left_justify=True
        params: center_justify=True
        params: right_justify=True
        params: text_color='red'
        params: background_color='yellow'
        '''
        if 'font_name' in kwargs:
            utillity.UtillityMethods.select_combobox_item(self, "FieldFont", kwargs["font_name"])
        if 'font_size' in kwargs:
            utillity.UtillityMethods.select_combobox_item(self, "FieldFontSize", kwargs["font_size"])
        if 'bold' in kwargs:
            bold_obj=self.driver.find_element_by_css_selector("#FieldFontBold img")
            utillity.UtillityMethods.default_left_click(self, object_locator=bold_obj, **kwargs)
            time.sleep(1)
        if 'italic' in kwargs:
            italic_obj=self.driver.find_element_by_css_selector("#FieldFontItalic img")
            utillity.UtillityMethods.default_left_click(self, object_locator=italic_obj, **kwargs)
            time.sleep(1)
        if 'underline' in kwargs:
            underline_obj=self.driver.find_element_by_css_selector("#FieldFontUnderline img")
            utillity.UtillityMethods.default_left_click(self, object_locator=underline_obj, **kwargs)
            time.sleep(1)
        if 'left_justify' in kwargs:
            left_justify_obj=self.driver.find_element_by_css_selector("#FieldFontLeft img")
            utillity.UtillityMethods.default_left_click(self, object_locator=left_justify_obj, **kwargs)
            time.sleep(1)
        if 'center_justify' in kwargs:
            center_justify_obj=self.driver.find_element_by_css_selector("#FieldFontCentre img")
            utillity.UtillityMethods.default_left_click(self, object_locator=center_justify_obj, **kwargs)
            time.sleep(1)
        if 'right_justify' in kwargs:
            right_justify_obj=self.driver.find_element_by_css_selector("#FieldFontRight img")
            utillity.UtillityMethods.default_left_click(self, object_locator=right_justify_obj, **kwargs)
            time.sleep(1)
        if 'text_color' in kwargs:
            text_color_obj=self.driver.find_element_by_css_selector("#FieldFontColour img")
            utillity.UtillityMethods.default_left_click(self, object_locator=text_color_obj, **kwargs)
            self.set_color(kwargs['text_color'])
        if 'background_color' in kwargs:
            background_color_obj=self.driver.find_element_by_css_selector("#FieldFontBackColour img")
            utillity.UtillityMethods.default_left_click(self, object_locator=background_color_obj, **kwargs)
            self.set_color(kwargs['background_color'])
    
    def set_report_style(self, **kwargs):
        '''
        :params font_name='Ariel'
        :params font_size='12'  (pass value what view in font size dropdown)
        :params bold=True
        :params italic=True
        :params underline=True
        :params left_justify=True
        :params center_justify=True
        :params right_justify=True
        :params text_color='red'
        :params background_color='yellow'
        ==================================
        currency_type={'USD':'dollar','GBP':'britishpound', 'JPY':'japanyen', 'EUR':'euro', 'NIS':'shekel'}
        :params currency='USD'    
        ==================================
        :params btn_reset=True
        :params btn_apply=True
        :params btn_ok=True
        :params btn_cancel=True
        :Usage  set_report_style(font_name='Arial',font_size='12', bold=True, italic=True, underline=True, left_justify=True, background_color='yellow', currency='USD', btn_reset=True, btn_apply=True, btn_ok=True)
        '''
        elem=(By.CSS_SELECTOR,'#styleOKBtn img')
        self._validate_page(elem)
        time.sleep(3)
        if 'font_name' in kwargs:
            font_name_elem=self.driver.find_element_by_css_selector("#styleDlg  div[id*=FontNameCombo] div[id^='BiButton']")
            utillity.UtillityMethods.select_any_combobox_item(self, font_name_elem, kwargs["font_name"])
            time.sleep(2)
            self.verify_report_style_popup_property(font_name=kwargs['font_name'], preview_font_name=kwargs['font_name'])
            time.sleep(1)
        if 'font_size' in kwargs:
            font_name_elem=self.driver.find_element_by_css_selector("#styleDlg  div[id*=FontSizeCombo] div[id^='BiButton']")
            utillity.UtillityMethods.select_any_combobox_item(self, font_name_elem, kwargs["font_size"])
            time.sleep(2)
            self.verify_report_style_popup_property(font_size=kwargs["font_size"], preview_font_size=kwargs["font_size"])
            time.sleep(1)
        if 'bold' in kwargs:
            if kwargs['bold'] == False:
                bold_obj=self.driver.find_element_by_css_selector("#styleDlg #Bold img")
                utillity.UtillityMethods.default_left_click(self, object_locator=bold_obj, **kwargs)
            self.verify_report_style_popup_property(bold_btn=kwargs['bold'], preview_bold=kwargs['bold'])
            time.sleep(1)
        if 'italic' in kwargs:
            italic_obj=self.driver.find_element_by_css_selector("#styleDlg #Italic img")
            utillity.UtillityMethods.default_left_click(self, object_locator=italic_obj, **kwargs)
            self.verify_report_style_popup_property(italic_btn=kwargs['italic'], preview_italic=kwargs['italic'])
            time.sleep(1)
        if 'underline' in kwargs:
            underline_obj=self.driver.find_element_by_css_selector("#styleDlg #Underline img")
            utillity.UtillityMethods.default_left_click(self, object_locator=underline_obj, **kwargs)
            self.verify_report_style_popup_property(underline_btn=kwargs['underline'], preview_underline=kwargs['underline'])
            time.sleep(1)
        if 'left_justify' in kwargs:
            left_justify_obj=self.driver.find_element_by_css_selector("#styleDlg #Left img")
            utillity.UtillityMethods.default_left_click(self, object_locator=left_justify_obj, **kwargs)
            self.verify_report_style_popup_property(left_btn=kwargs['left_justify'], preview_left=kwargs['left_justify'])
            time.sleep(1)
        if 'center_justify' in kwargs:
            center_justify_obj=self.driver.find_element_by_css_selector("#styleDlg #Center img")
            utillity.UtillityMethods.default_left_click(self, object_locator=center_justify_obj, **kwargs)
            self.verify_report_style_popup_property(center_btn=kwargs['center_justify'], preview_center=kwargs['center_justify'])
            time.sleep(1)
        if 'right_justify' in kwargs:
            right_justify_obj=self.driver.find_element_by_css_selector("#styleDlg #Right img")
            utillity.UtillityMethods.default_left_click(self, object_locator=right_justify_obj, **kwargs)
            self.verify_report_style_popup_property(right_btn=kwargs['right_justify'], preview_right=kwargs['right_justify'])
            time.sleep(1)
        if 'text_color' in kwargs:
            text_color_obj=self.driver.find_element_by_css_selector("#styleDlg #FontColor img")
            utillity.UtillityMethods.default_left_click(self, object_locator=text_color_obj, **kwargs)
            self.set_color(kwargs['text_color'])
            self.verify_report_style_popup_property(preview_text_color=kwargs['text_color'])
        if 'background_color' in kwargs:
            background_color_obj=self.driver.find_element_by_css_selector("#styleDlg #FontBackColor img")
            utillity.UtillityMethods.default_left_click(self, object_locator=background_color_obj, **kwargs)
            self.set_color(kwargs['background_color'])
            self.verify_report_style_popup_property(preview_background_color=kwargs['background_color'])
        if 'currency' in kwargs:
            currency_menu_item_css="#CurrencySymbolMenu #" + kwargs['currency'] + "MenuItem img"
            currency_symbol_obj=self.driver.find_element_by_css_selector("#CurrencySymbol img")
            utillity.UtillityMethods.default_left_click(self, object_locator=currency_symbol_obj, **kwargs)
            time.sleep(2)
            currency_menu_obj=self.driver.find_element_by_css_selector(currency_menu_item_css)
            utillity.UtillityMethods.default_left_click(self, object_locator=currency_menu_obj, **kwargs)
            self.verify_report_style_popup_property(currency_symbol=kwargs['currency'])
        if 'btn_reset' in kwargs:
            btn_reset_obj=self.driver.find_element_by_css_selector("#styleDlg #Reset img")
            utillity.UtillityMethods.default_left_click(self, object_locator=btn_reset_obj, **kwargs)
            self.verify_report_style_popup_property(font_name='Arial', font_size='9', bold_btn=True, italic_btn=False, underline_btn=False,
                                                    left_btn=False, center_btn=False, right_btn=False, currency_symbol='USD', 
                                                    preview_font_name='Arial', preview_font_size=9, preview_bold=True, preview_italic=False, 
                                                    preview_underline=False, preview_left=True, preview_center=False, preview_right=False, 
                                                    preview_text_color='gray8', preview_background_color='white', preview_default_text='Arial 9')
            time.sleep(1)
        if 'btn_apply' in kwargs:
            btn_apply_obj=self.driver.find_element_by_css_selector("#styleDlg #styleApplyBtn img")
            utillity.UtillityMethods.default_left_click(self, object_locator=btn_apply_obj, **kwargs)
            time.sleep(1)
        if 'btn_ok' in kwargs:
            btn_ok_obj=self.driver.find_element_by_css_selector("#styleDlg #styleOKBtn img")
            utillity.UtillityMethods.default_left_click(self, object_locator=btn_ok_obj, **kwargs)
            time.sleep(1)
        if 'btn_cancel' in kwargs:
            btn_cancel_obj=self.driver.find_element_by_css_selector("#styleDlg #styleCancelBtn img")
            utillity.UtillityMethods.default_left_click(self, object_locator=btn_cancel_obj, **kwargs)
            time.sleep(1)
    
    
    def verify_report_style_popup_property(self, **kwargs):
        '''
        :params font_name='Arial'
        :params font_size=9 (pass value what view in font size dropdown)
        :params bold_btn=True
        :params italic_btn=True
        :params underline_btn=True
        :params left_btn=True
        :params center_btn=True
        :params right_btn=True
        :params currency_symbol='USD'
        :params preview_font_name='Arial'
        :params preview_font_size=9 (pass value what view in font size dropdown)
        :params preview_bold=True
        :params preview_italic=True
        :params preview_underline=True
        :params preview_left=True
        :params preview_center=True
        ;params preview_right=True
        :params preview_text_color='blue'
        :params preview_background_color='cyan'
        :params preview_default_text='Arail 9'
        :Usage  verify_report_style_popup_property(font_name='Arial',font_size=12, bold=True, italic=True, underline=True, 
                                                    left_btn=True, currency_symbol='USD', preview_font_name='Arial',
                                                     preview_font_size=12, preview_bold=True, preview_italic=True, 
                                                     preview_underline=True, preview_left=True, preview_text_color='blue',
                                                     preview_background_color='cyan', preview_default_text='Arial 9')
        '''
        time.sleep(3)
        if 'font_name' in kwargs:
            actual_font_name=self.driver.find_element_by_css_selector("[class*='active'] #FontNameCombo > div[class*='combo-box-label']").text.strip().lower()
            expected_font_name=kwargs["font_name"].lower()
            utillity.UtillityMethods.asequal(self, expected_font_name, actual_font_name , "Step X: Verify " + kwargs["font_name"] + " font name within the style within style window.")
        if 'font_size' in kwargs:
            actual_font_size=str(self.driver.find_element_by_css_selector("[class*='active'] #FontSizeCombo > div[class*='combo-box-label']").text.strip())
            expected_font_size=str(kwargs["font_size"])
            utillity.UtillityMethods.asequal(self, expected_font_size, actual_font_size, "Step X: Verify " + str(kwargs["font_size"]) + " font size within the style within style window.")
        if 'bold_btn' in kwargs:
            actual_bold_btn_status=bool(re.match('.*checked\s*', self.driver.find_element_by_css_selector("#styleDlg #Bold").get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['bold_btn'], actual_bold_btn_status , "Step X: Verify bold within the style within style window "+str(kwargs['bold_btn'])+".")
        if 'italic_btn' in kwargs: 
            actual_italic_btn_status=bool(re.match('.*checked\s*', self.driver.find_element_by_css_selector("#styleDlg #Italic").get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['italic_btn'], actual_italic_btn_status, "Step X: Verify italic within the style within style window "+str(kwargs['italic_btn'])+".")
        if 'underline_btn' in kwargs:
            actual_underline_btn_status=bool(re.match('.*checked\s*', self.driver.find_element_by_css_selector("#styleDlg #Underline").get_attribute("class"))) 
            utillity.UtillityMethods.asequal(self, kwargs['underline_btn'], actual_underline_btn_status, "Step X: Verify Underline within the style within style window "+str(kwargs['underline_btn'])+".")
        if 'left_btn' in kwargs:
            actual_left_btn_status=bool(re.match('.*checked\s*', self.driver.find_element_by_css_selector("#styleDlg #Left").get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['left_btn'], actual_left_btn_status, "Step X: Verify left justify within the style within style window "+str(kwargs['left_btn'])+".")
        if 'center_btn' in kwargs:
            actual_center_btn_status=bool(re.match('.*checked\s*', self.driver.find_element_by_css_selector("#styleDlg #Center").get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['center_btn'], actual_center_btn_status, "Step X: Verify center justify within the style within style window "+str(kwargs['center_btn'])+".")
        if 'right_btn' in kwargs:
            actual_right_btn_status=bool(re.match('.*checked\s*', self.driver.find_element_by_css_selector("#styleDlg #Right").get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['right_btn'], actual_right_btn_status, "Step X: Verify right justify within the style within style window "+str(kwargs['right_btn'])+".")
        if 'currency_symbol' in kwargs:
            currency_type={'USD':'dollar','GBP':'britishpound', 'JPY':'japanyen', 'EUR':'euro', 'NIS':'shekel'}
            actual_currency=self.driver.find_element_by_css_selector("#CurrencySymbol img").get_attribute("src").split("/")[-1]
            expected_currency=currency_type[kwargs['currency_symbol']] + "_16.png" 
            utillity.UtillityMethods.asequal(self, expected_currency, actual_currency , "Step X: Verify " + str(kwargs['currency_symbol']) + " Currency is selected.")
        if 'preview_font_name' in kwargs:
            expected_font_name=kwargs["preview_font_name"].lower()
            applied_font_name=self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").value_of_css_property("font-family").strip('"').lower()
            utillity.UtillityMethods.asequal(self, expected_font_name, applied_font_name, "Step X: Verify font name "+str(kwargs["preview_font_name"])+" within the style within style Preview window.")
        if 'preview_font_size' in kwargs:
            expected_font_size=(round(1.333333*int(kwargs["preview_font_size"])))
            applied_font_size=self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").value_of_css_property("font-size")
            utillity.UtillityMethods.asequal(self, str(expected_font_size)+"px", applied_font_size , "Step X: Verify font size "+str(kwargs["preview_font_size"])+" within the style within style Preview window.")
        if 'preview_bold' in kwargs:
            try:
                if self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel[style*='bold']").is_displayed():
                    status_bold=True
            except:
                status_bold=False
            utillity.UtillityMethods.asequal(self, kwargs['preview_bold'], status_bold, "Step X: Verify bold within the style within style preview window "+str(kwargs['preview_bold'])+".")
        if 'preview_italic' in kwargs: 
            try:
                if self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel[style*='italic']").is_displayed():
                    status_italic=True
            except:
                status_italic=False
            utillity.UtillityMethods.asequal(self, kwargs['preview_italic'], status_italic, "Step X: Verify italic within the style within style preview window "+str(kwargs['preview_italic'])+".")
        if 'preview_underline' in kwargs:
            try:
                if self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel[style*='underline']").is_displayed():
                    status_underline=True
            except:
                status_underline=False
            utillity.UtillityMethods.asequal(self, kwargs['preview_underline'], status_underline, "Step X: Verify Underline within the style within style preview window "+str(kwargs['preview_underline'])+".")
        if 'preview_left' in kwargs:
            val=self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").value_of_css_property('text-align')
            status_left=True if val == 'left' else False
            utillity.UtillityMethods.asequal(self, kwargs['preview_left'], status_left, "Step X: Verify left justify within the style within style preview window "+str(kwargs['preview_left'])+".")
        if 'preview_center' in kwargs:
            val=self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").value_of_css_property('text-align')
            status_center=True if val == 'center' else False
            utillity.UtillityMethods.asequal(self, kwargs['preview_center'], status_center, "Step X: Verify center justify within the style within style preview window "+str(kwargs['preview_center'])+".")
        if 'preview_right' in kwargs:
            val=self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").value_of_css_property('text-align')
            status_right=True if val == 'right' else False
            utillity.UtillityMethods.asequal(self, kwargs['preview_right'], status_right, "Step X: Verify right justify within the style within style preview window "+str(kwargs['preview_right'])+".")
        if 'preview_text_color' in kwargs:
            expected_text_color=utillity.UtillityMethods.color_picker(self, kwargs['preview_text_color'], 'rgba')
            actual_text_color=Color.from_string(self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").value_of_css_property("color")).rgba
            utillity.UtillityMethods.asequal(self, expected_text_color, actual_text_color , "Step X: Verify text color within the style within style preview window.")
        if 'preview_background_color' in kwargs:
            expected_bg_color=utillity.UtillityMethods.color_picker(self, kwargs['preview_background_color'], 'rgba')
            actual_bg_color=Color.from_string(self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").value_of_css_property("background-color")).rgba
            utillity.UtillityMethods.asequal(self, expected_bg_color, actual_bg_color , "Step X: Verify  background color within the style within style preview window.")
        if 'preview_default_text' in kwargs:
            expected_text = kwargs['preview_default_text'].lower()
            actual_text=self.driver.find_element_by_css_selector("#styleDlg #stylePreviewLabel").text.strip().lower()
            utillity.UtillityMethods.asequal(self, expected_text, actual_text , "Step X: Verify  preview default text 'Arail 9' within the style within style preview window.")
    
    
    def set_header_footer_style(self, **kwargs):
        '''
        params: font_name='Arial'
        params: font_size=12
        params: bold=True
        params: italic=True
        params: underline=True
        params: left_justify=True
        params: center_justify=True
        params: right_justify=True
        params: text_color='red'
        params: background_color='yellow'
        '''
        time.sleep(5)
        if 'font_name' in kwargs:
            font_name_ele=self.driver.find_element_by_css_selector("#subheaderDlg  div[id*=FontName] div[id^='BiButton']")
            utillity.UtillityMethods.select_any_combobox_item(self, font_name_ele, kwargs["font_name"])
        if 'font_size' in kwargs:
            font_size_ele=self.driver.find_element_by_css_selector("#subheaderDlg  div[id*=FontSize] div[id^='BiButton']")
            utillity.UtillityMethods.select_any_combobox_item(self, font_size_ele, kwargs["font_size"])
        if 'bold' in kwargs:
            bold_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Bold img")
            CoreUtillityMethods.left_click(self, web_element = bold_obj)
        if 'italic' in kwargs:
            italic_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Italic img")
            CoreUtillityMethods.left_click(self, web_element = italic_obj)
        if 'underline' in kwargs:
            underline_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Underline img")
            CoreUtillityMethods.left_click(self, web_element = underline_obj)
            time.sleep(1)
        if 'left_justify' in kwargs:
            left_justify_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Left img")
            CoreUtillityMethods.left_click(self, web_element = left_justify_obj)
        if 'center_justify' in kwargs:
            center_justify_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Center img")
            CoreUtillityMethods.left_click(self, web_element = center_justify_obj)
        if 'right_justify' in kwargs:
            right_justify_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Right img")
            CoreUtillityMethods.left_click(self, web_element = right_justify_obj)
        if 'text_color' in kwargs:
            (Global_variables.browser_name in ['firefox']) and IA_Style.click_on_header_footer_editor(self)
            text_color_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Color img")
            CoreUtillityMethods.left_click(self, web_element = text_color_obj)
            color_dialog_popup_css="div[id*='ColorPicker'] div[class*='window-active']"
            ok_btn_css=color_dialog_popup_css+" #BiColorPickerOkBtn"
            utillity.UtillityMethods.synchronize_with_number_of_element(self, ok_btn_css, 1, 25)
            self.set_color(kwargs['text_color'])
        if 'background_color' in kwargs:
            (Global_variables.browser_name in ['firefox']) and IA_Style.click_on_header_footer_editor(self)
            background_color_obj=self.driver.find_element_by_css_selector("#subheaderDlg #BackColor img")
            CoreUtillityMethods.left_click(self, web_element = background_color_obj)
            color_dialog_popup_css="div[id*='ColorPicker'] div[class*='window-active']"
            ok_btn_css=color_dialog_popup_css+" #BiColorPickerOkBtn"
            utillity.UtillityMethods.synchronize_with_number_of_element(self, ok_btn_css, 1, 25)
            self.set_color(kwargs['background_color']) 
    
    
    def create_sub_header_footer(self, heading_type, input_text, **kwargs): 
        """
        :Params: heading_type= Sub_Header or Sub_Footer
        :Params: Input_text = provide the text to be added for sub-header/subfooter
        Usage: create_sub_header_footer("Sub_Header", "This is simple text test")
        Enhancement to apply styling for SUB - Header/Footer text will be updated later
        """
        visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual_ribbonobj.select_ribbon_item('Field', heading_type)
        utillity.UtillityMethods.synchronize_until_element_is_visible(self, '#subheaderDlg', 90)
        if Global_variables.browser_name in ['ie', 'edge']:     
            action=ActionChains(self.driver)
            time.sleep(1)
            action.send_keys(input_text).perform()
            time.sleep(1)
            del action
        else:
            CoreUtillityMethods.switch_to_frame(self, frame_css='#Editor')
            time.sleep(15)
            el = self.driver.find_element_by_css_selector('html>body').click()
            time.sleep(1)
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('a')
            pyautogui.keyUp('a')
            pyautogui.keyUp('ctrl')
            time.sleep(1)
            pyautogui.press('delete')

            time.sleep(1)
            el = self.driver.find_element_by_css_selector('html>body')
            el.send_keys(input_text)
            time.sleep(1)
            CoreUtillityMethods.switch_to_default_content(self)
        time.sleep(5)
        
        self.set_header_footer_style(**kwargs)
        if 'btn_apply' in kwargs:
            self.driver.find_element_by_id("applyBtn").click()
            time.sleep(1)
        elif 'btn_ok' in kwargs:
            self.driver.find_element_by_id("okBtn").click()
            time.sleep(1)
        elif 'btn_cancle' in kwargs:
            self.driver.find_element_by_id("cancelBtn").click()
            time.sleep(1)
        elif 'btn_reset' in kwargs:
            self.driver.find_element_by_id("resetBtn").click()
            time.sleep(1)
        else:
            self.driver.find_element_by_id("okBtn").click()
            time.sleep(1)
    
    def create_header_footer(self, launch_point, heading_type, input_text,**kwargs): 
        """
        :params: launch_point=ribbon(when you call this function first time)
        :params: launch_point=frame(when you want to use this function again)
        :Params: heading_type= Report_Header or Page_Header or Page_Footer or Report_Footer
        :Params: Input_text = provide the text to be added
        :Params: **kwargs = provide keyword for style section and Internal functionality too.
        :Usage:  create_header_footer('ribbon', 'Report Footer', 'Report Footer', font_name='COMIC SANS MS', text_color='blue',background_color='yellow', btn_apply='btn_apply', btn_ok='btn_ok')
                                                    OR
        :Usage:  create_header_footer('frame', 'Report Footer', 'Report Footer', font_name='COMIC SANS MS', text_color='blue',background_color='yellow', btn_apply='btn_apply', btn_ok='btn_ok')
        Enhancement to apply styling for SUB - Header/Footer text will be updated later
        """
        self.driver.implicitly_wait=5
        if launch_point =='ribbon':
            visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
            visual_ribbonobj.select_ribbon_item('Home', 'header_footer', opt=heading_type)
        else:
            ids={'Report Header':'rptHding','Page Header':'pgHding','Page Footer':'pgFting','Report Footer':'rptFting'}
            btn_css="#" + ids[heading_type] + " img"
            btn_css_obj=self.driver.find_element_by_css_selector(btn_css)
            CoreUtillityMethods.left_click(self, web_element= btn_css_obj)
#             utillity.UtillityMethods.default_left_click(self, object_locator=btn_css_obj, **kwargs)
            time.sleep(2)
        utillity.UtillityMethods.synchronize_until_element_is_visible(self, '#subheaderDlg #okBtn', 90)
        """ Browser specific """
        if Global_variables.browser_name in ['ie', 'edge']:
            utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, input_text, text_box_css='#subheaderDlg .window-active')     
#             action=ActionChains(self.driver)
#             time.sleep(1)
#             action.send_keys(input_text).perform()
#             time.sleep(1)
#             del action
        elif Global_variables.browser_name in ['firefox', 'chrome']:
            self.driver.switch_to.frame(self.driver.find_element_by_id("Editor"))
            time.sleep(15)
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.type_string(str(input_text), interval=int(1))
            else:
                el = self.driver.find_element_by_css_selector('html>body').click()
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('del')
#                 virtual_keyboard.send('backspace')
                time.sleep(1)
                virtual_keyboard.write(input_text)
            time.sleep(5)
            self.driver.switch_to_default_content()
        else:
            self.driver.switch_to.frame(self.driver.find_element_by_id("Editor"))
            time.sleep(15)
            el = self.driver.find_element_by_css_selector('html>body').click()
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
#             el.send_keys(keys.Keys.CONTROL, 'a')
            time.sleep(1)
            pyautogui.press('del')
#             el.send_keys(keys.Keys.DELETE)
            time.sleep(1)
            el = self.driver.find_element_by_css_selector('html>body')
            el.send_keys(input_text)
            time.sleep(1)
            self.driver.switch_to_default_content()
        time.sleep(2)
        self.set_header_footer_style(**kwargs)
        if 'btn_apply' in kwargs:
            self.driver.find_element_by_id("applyBtn").click()
            time.sleep(1)
        if 'btn_ok' in kwargs:
            self.driver.find_element_by_id("okBtn").click()
            time.sleep(1)
        if 'btn_cancle' in kwargs:
            self.driver.find_element_by_id("cancelBtn").click()
            time.sleep(1)
        if 'btn_reset' in kwargs:
            self.driver.find_element_by_id("resetBtn").click()
            time.sleep(1)
    
    
    def traffic_light_verify_condition_row(self, rownum, **kwargs):
        """
        :params : rownum=1,2,3..
        :params : kwargs['field_name']='DEALER_COST' or 'RETAIL_COST'
        :params : kwargs['relation_name']='Equal to' or ' Greater than'
        :params : kwargs['Field_Value_txt']='0' or value shown in traffic light Field Value text (default is 0)
        :params : kwargs['total_row']=1, 2, 3...
        :Usage  : traffic_light_create_new(1, field_name='DEALER_COST', relation_name='Equal to', Field_Value_txt='0', total_row=1)
        """
        row_elems=self.driver.find_elements_by_css_selector("#trafficLightsDlg #cstyMainPane [id^='condGridRowBox']")
        if 'field_name' in kwargs:
            field_elem_data=row_elems[rownum-1].find_element_by_css_selector("[id^='cstyFieldTxt'] [class^='bi-label']")
            expected_field_name=kwargs['field_name'].lower()
            actual_field_name=field_elem_data.text.lower()
            utillity.UtillityMethods.asequal(self, expected_field_name, actual_field_name, "Step X: Verify " + str(kwargs["field_name"]) + " field name within the traffic light style window.")
        if 'relation_name' in kwargs:
            relation_elem_data=row_elems[rownum-1].find_element_by_css_selector("[id^='cstyRelationsCmb'] [class^='bi-label']")
            expected_relation_name=kwargs['relation_name'].lower()
            actual_relation_name=relation_elem_data.text.lower()
            utillity.UtillityMethods.asequal(self, expected_relation_name, actual_relation_name, "Step X: Verify " + str(kwargs["relation_name"]) + " relation field name within the traffic light style window.")
        if 'Field_Value_txt' in kwargs:
            value_elem_data=row_elems[rownum-1].find_element_by_css_selector("[id^='cstyFieldValuetxt'] [class^='bi-label']")
            expected_filter_type=kwargs['Field_Value_txt'].lower().strip()
            actual_filter_type=value_elem_data.text.lower().strip()
            utillity.UtillityMethods.asequal(self, expected_filter_type, actual_filter_type, "Step X: Verify '" + str(kwargs["Field_Value_txt"]) + "' field Value text within the traffic light style window.")
        if 'total_row' in kwargs:
            expected_total_row=kwargs['total_row']
            actual_total_row=len(row_elems)
            utillity.UtillityMethods.asequal(self, expected_total_row, actual_total_row, "Step X: Verify total "+str(expected_total_row)+"-row number within the traffic light style window.")
            
    
    def traffic_light_create_new(self, rownum, **kwargs):
        """
        :params : rownum=1,2,3..
        :params : kwargs['field_name']='DEALER_COST' or 'RETAIL_COST'
        :params : kwargs['relation_name']='Equal to' or ' Greater than'
        :params : kwargs['filter_type']='Constant' or 'Field'
        :Usage  : traffic_light_create_new(1, field_name='DEALER_COST', relation_name='Equal to', filter_type='Constant', value_box_input='ENGLAND')
                        or
        :Usage  : traffic_light_create_new(1, field_name='DEALER_COST', relation_name='Equal to', filter_type='Constant', getvalue_params='All', value='6,000 (6000)')
                        or
        :Usage  : traffic_light_create_new(1, filter_type='Constant', getvalue_params='All', value='6,000 (6000)')
                        or
        :Usage traffic_light_create_new(1, filter_type='Constant', getvalue_params='From File', flat_file='Flat_file.txt', browse_okBtn=True, value='4444')
        """
        row_elems=self.driver.find_elements_by_css_selector("#trafficLightsDlg #cstyMainPane [id^='condGridRowBox']")
        field_elem=row_elems[rownum-1].find_element_by_css_selector("[id^='cstyFieldTxt'] [id^='BiButton']")
        relation_elem=row_elems[rownum-1].find_element_by_css_selector("[id^='cstyRelationsCmb'] [id^='BiButton']")
        value_elem=row_elems[rownum-1].find_element_by_css_selector("[id^='cstyFieldValuetxt'] [id^='BiButton']")
        if 'field_name' in kwargs:
            utillity.UtillityMethods.select_any_combobox_item(self, field_elem, kwargs['field_name'])
        if 'relation_name' in kwargs:
            utillity.UtillityMethods.select_any_combobox_item(self, relation_elem, kwargs['relation_name'])
        if 'filter_type' in kwargs:
            value_elem.click()
            self.traffic_light_value_select(**kwargs)

        
    def traffic_light_value_select(self, **kwargs):
        """
        :params: kwargs['filter_type']='Constant' or 'Field'
        :params: kwargs['value_box_input']='ENGLAND' or 'ITALY' OR any value
        :params: kwargs['getvalue_params']='All' OR 'First', OR 'Last'....
        :params: kwargs['value']='5,610 (5610)'
        :Usage: traffic_light_value_select('All', '13000')
        """
        ok_btn_elem=(By.CSS_SELECTOR,'#wndWhereValuePopup_btnOK img')
        self._validate_page(ok_btn_elem)
        utillity.UtillityMethods.select_any_combobox_item(self,self.driver.find_element_by_css_selector("#id_wv_combo_type [id^='BiButton']"), kwargs['filter_type'])
        if kwargs['filter_type']=='Constant':
            get_value_btn_css="#dlgWhereValue_tbuttonGetValue"
            value_item_css="#dlgWhereValue_listValues span"
            if 'value_box_input' in kwargs:
                value_box_css="[class*='active'] #dlgWhereValue #id_wv_text_value"
                value_box_find=self.driver.find_element_by_css_selector(value_box_css)
                value_box_find.click()
                time.sleep(2)
                value_box_find.clear()
                time.sleep(2)
                value_box_find.send_keys(kwargs['value_box_input'])
                time.sleep(2)
            else:
                self.driver.find_element_by_css_selector(get_value_btn_css).click()
                time.sleep(3)
                utillity.UtillityMethods.select_or_verify_bipop_menu(self, kwargs['getvalue_params'])
                if 'verify' in kwargs:
                    IA_Style.traffic_light_select_value_verify(self,value_item_css=value_item_css,**kwargs)
                if 'flat_file' in kwargs:
                    IA_Style.traffic_light_select_browse_file(self,**kwargs)
                if 'excelSpread_sheet' in kwargs:
                    IA_Style.traffic_light_select_browse_file(self,**kwargs)
                if 'value' in kwargs:
                    input_val = self.driver.find_element_by_css_selector("#wndWhereValuePopup #dlgWhereGetValueBox input")
                    input_val.click()
                    time.sleep(3)
                    input_val.send_keys(kwargs['value'])
                    time.sleep(3)
                    values=self.driver.find_elements_by_css_selector(value_item_css)
                    values[0].click()        
                    time.sleep(2)
        if kwargs['filter_type']=='Field':
            fields=self.driver.find_elements_by_css_selector("#dlgWhereValue div[id^='BiListItem']")
            fields[[el.text.strip() for el in fields].index(kwargs['value'])].click()
        time.sleep(3)
        ok_btn_obj=self.driver.find_element(*ok_btn_elem)
        utillity.UtillityMethods.default_left_click(self, object_locator=ok_btn_obj, **kwargs)
        time.sleep(2)
        
        
    def traffic_light_select_value_verify(self, **kwargs):
        """
        :params : kwargs['value_item_css']="#dlgWhereValue_listValues span"
        :params : kwargs['verify']=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN']
        :Usage  : traffic_light_select_value_verify(value_item_css=""#dlgWhereValue_listValues span", verify=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN'])
        """
        values=self.driver.find_elements_by_css_selector(kwargs['value_item_css'])
        actual_text_name=[]
        if 'verify' in kwargs:
            expected_text_name=kwargs['verify']
            for actual in values:
                actual_text_name.append(actual.text)
            utillity.UtillityMethods.as_List_equal(self, expected_text_name, actual_text_name, "Step X: Verify " + str(kwargs["verify"]) + " text name within the traffic light style window.")
            
    
    def traffic_light_select_browse_file(self, **kwargs):
        """
        :Params flat_file='Flat_file.txt'
        :Params excelSpread_sheet='Excel-Data-for-0027.xls'
        :Params browse_okBtn=True
        :Params browse_cancleBtn=True
        :Usage  traffic_light_select_browse_file(flat_file='Flat_file.txt', browse_okBtn=True)
        """
        okbtn_css = (By.CSS_SELECTOR, "form table tr td input[id='okBtn']")
        time.sleep(5)
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "[id^='IBIDialog'] iframe[class*='iframe-focus']")))
        time.sleep(15)
        IA_Style._validate_page(self, okbtn_css)
        time.sleep(15)
        flat_file_or_cvs_css="form table tr td input[id='flatFileFormatRadio']"
        excel_spreadsheet_css="form table tr td input[id='excelSpreadsheetFormatRadio']"
        select_file_css="form table tr td input[id='datasourceField']"
        select_file_obj=self.driver.find_element_by_css_selector(select_file_css)
        if 'flat_file' in kwargs:
            flat_file=self.driver.find_element_by_css_selector(flat_file_or_cvs_css)
            flat_file.click()
            time.sleep(1)
            if Global_variables.browser_name in ['ie', 'edge']:
                action1 = ActionChains(self.driver)
                action1.move_to_element_with_offset(select_file_obj, 350, 9).click().perform()
                del action1
            elif Global_variables.browser_name in ['firefox']:
                action1 = ActionChains(self.driver)
                action1.click(select_file_obj).perform()
                del action1
                time.sleep(15)
            else:
#                 select_file_obj.click()
                self.driver.execute_script('arguments[0].click();',select_file_obj)
            time.sleep(8)
#             Flat_file="\\data\\"+kwargs['flat_file']+","+Global_variables.browser_name
#             os.system(os.getcwd()+"\\common\\lib\\Upload_File.exe "+Flat_file)
            time.sleep(2)
        if 'excelSpread_sheet' in kwargs:
            excel_spreadsheet_obj=self.driver.find_element_by_css_selector(excel_spreadsheet_css)
            excel_spreadsheet_obj.click()
            time.sleep(1)
            if Global_variables.browser_name in ['ie', 'edge']:
                action1 = ActionChains(self.driver)
                action1.move_to_element_with_offset(select_file_obj, 350, 9).click().perform()
                del action1
            elif Global_variables.browser_name in ['firefox']:
                action1 = ActionChains(self.driver)
                action1.click(select_file_obj).perform()
                del action1
                time.sleep(15)
            else:
                select_file_obj.click()
            time.sleep(8)
#             excel_spreadsheet="\\data\\"+kwargs['excelSpread_sheet']+","+Global_variables.browser_name
#             os.system(os.getcwd()+"\\common\\lib\\Upload_File.exe "+excel_spreadsheet)
            time.sleep(2)
        if 'browse_okBtn' in kwargs:
            self.driver.find_element(okbtn_css).click()
            time.sleep(1)
        if 'browse_cancleBtn' in kwargs:
            self.driver.find_element_by_css_selector("form table tr td input[id='cancelBtn']").click()
            time.sleep(1)
        self.driver.switch_to_default_content()

    
    def traffic_light_toolbar_select(self, toolbar_btn_name, rownum, **kwargs):
        """
        :params: toolbar_btn_name='New' or 'Style'...
        :params : rownum=1,2,3..
        :Usage: traffic_light_toolbar_select('New')
                or
        :Usage: traffic_light_toolbar_select('Delete',2) for delete any row rownum value is needed
        """
        btn_ids={'New':'cstyAddNew', 'Delete':'cstyRemoveBtn', 'Style':'cstyStyle', 'DrillDown':'cstyDrillDownBtn'}
        row_elems=self.driver.find_elements_by_css_selector("#trafficLightsDlg #cstyMainPane [id^='condGridRowBox'] [id^='cstyCurrentBtn'] img")
        toolbar_btn_css="#trafficLightsDlg #cstyToolBar #" + btn_ids[toolbar_btn_name]
        toolbar_btn_obj=self.driver.find_element_by_css_selector(toolbar_btn_css)
        if toolbar_btn_name == 'Delete':
            row_elems_obj=row_elems[rownum-1]
            utillity.UtillityMethods.default_left_click(self, object_locator=row_elems_obj, **kwargs)
            utillity.UtillityMethods.default_left_click(self, object_locator=toolbar_btn_obj, **kwargs)
        else:
            CoreUtillityMethods.python_left_click('self', toolbar_btn_obj)
            time.sleep(2)
        if toolbar_btn_name == 'Style':
            self.traffic_light_set_style(rownum, **kwargs)
        
    def traffic_light_close_dialog(self, bottom_bar_btn_name):
        bottom_bar_btn_ids={'Ok':'trafficLightsOkBtn', 'Apply':'trafficLightsApplyBtn', 'Cancel':'trafficLightsCancelBtn'}
        bottom_bar_btn_css="#trafficLightsDlg [id^='IABottomBar'] #" + bottom_bar_btn_ids[bottom_bar_btn_name]
        self.driver.find_element_by_css_selector(bottom_bar_btn_css).click()

    
    def traffic_light_set_style(self, rownum, **kwargs):
        '''
        :params font_name='Ariel'
        :params font_size='12'
        :params bold=True
        :params italic=True
        :params underline=True
        :params left_justify=True
        :params center_justify=True
        :params right_justify=True
        :params text_color='red'
        :params background_color='yellow'
        :params btn_reset=True
        :Usage  set_report_style(font_name='Arial',font_size='12', bold=True, italic=True, underline=True, left_justify=True, background_color='yellow', btn_reset=True)
        '''
        if 'font_name' in kwargs:
            font_name_combo_elem=self.driver.find_element_by_css_selector("#csStyleDlg #FontNameCombo [class^='bi-button']")
            utillity.UtillityMethods.select_any_combobox_item(self, font_name_combo_elem, kwargs["font_name"])
            time.sleep(2)
            font_name_elem=self.driver.find_element_by_css_selector("#csStyleDlg #FontNameCombo")
            self.traffic_light_verify_style_popup(font_name_elem, font_name=kwargs['font_name'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_font_name=kwargs['font_name'])
            time.sleep(1)
        if 'font_size' in kwargs:
            font_size_combo_elem=self.driver.find_element_by_css_selector("#csStyleDlg #FontSizeCombo [class^='bi-button']")
            utillity.UtillityMethods.select_any_combobox_item(self, font_size_combo_elem, kwargs["font_size"])
            time.sleep(2)
            font_size_elem=self.driver.find_element_by_css_selector("#csStyleDlg #FontSizeCombo")
            self.traffic_light_verify_style_popup(font_size_elem, font_size=kwargs["font_size"])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_font_size=kwargs["font_size"])
            time.sleep(2)
        if 'bold' in kwargs:
            bold_obj=self.driver.find_element_by_css_selector("#csStyleDlg #Bold img")
            CoreUtillityMethods.python_left_click('self', bold_obj)
#             utillity.UtillityMethods.default_left_click(self, object_locator=bold_obj, **kwargs)
            bold_ele=self.driver.find_element_by_css_selector("#csStyleDlg #Bold")
            self.traffic_light_verify_style_popup(bold_ele, bold_btn=kwargs['bold'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_bold=kwargs['bold'])
            time.sleep(1)
        if 'italic' in kwargs:
            italic_obj=self.driver.find_element_by_css_selector("#csStyleDlg #Italic img")
            CoreUtillityMethods.python_left_click('self', italic_obj)
#             utillity.UtillityMethods.default_left_click(self, object_locator=italic_obj, **kwargs)
            italic_ele=self.driver.find_element_by_css_selector("#csStyleDlg #Italic")
            self.traffic_light_verify_style_popup(italic_ele, italic_btn=kwargs['italic'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_italic=kwargs['italic'])
            time.sleep(1)
        if 'underline' in kwargs:
            underline_obj=self.driver.find_element_by_css_selector("#csStyleDlg #Underline img")
            utillity.UtillityMethods.default_left_click(self, object_locator=underline_obj, **kwargs)
            underline_ele=self.driver.find_element_by_css_selector("#csStyleDlg #Underline")
            self.traffic_light_verify_style_popup(underline_ele, underline_btn=kwargs['underline'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_underline=kwargs['underline'])
            time.sleep(1)
        if 'left_justify' in kwargs:
            left_justify_obj=self.driver.find_element_by_css_selector("#csStyleDlg #Left img")
            utillity.UtillityMethods.default_left_click(self, object_locator=left_justify_obj, **kwargs)
            left_justify_ele=self.driver.find_element_by_css_selector("#csStyleDlg #Left")
            self.traffic_light_verify_style_popup(left_justify_ele, left_btn=kwargs['left_justify'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_left=kwargs['left_justify'])
            time.sleep(1)
        if 'center_justify' in kwargs:
            center_justify_obj=self.driver.find_element_by_css_selector("#csStyleDlg #Centre img")
            utillity.UtillityMethods.default_left_click(self, object_locator=center_justify_obj, **kwargs)
            center_justify_ele=self.driver.find_element_by_css_selector("#csStyleDlg #Centre")
            self.traffic_light_verify_style_popup(center_justify_ele, center_btn=kwargs['center_justify'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_center=kwargs['center_justify'])
            time.sleep(1)
        if 'right_justify' in kwargs:
            right_justify_obj=self.driver.find_element_by_css_selector("#csStyleDlg #Right img")
            utillity.UtillityMethods.default_left_click(self, object_locator=right_justify_obj, **kwargs)
            right_justify_ele=self.driver.find_element_by_css_selector("#csStyleDlg #Right")
            self.traffic_light_verify_style_popup(right_justify_ele, right_btn=kwargs['right_justify'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_right=kwargs['right_justify'])
            time.sleep(1)
        if 'text_color' in kwargs:
            text_color_obj=self.driver.find_element_by_css_selector("#csStyleDlg #FontColor img")
            CoreUtillityMethods.python_left_click('self', text_color_obj)
#             utillity.UtillityMethods.default_left_click(self, object_locator=text_color_obj, **kwargs)
            color_dialog_popup_css="div[id*='ColorPicker'] div[class*='window-active']"
            ok_btn_css=color_dialog_popup_css+" #BiColorPickerOkBtn"
            utillity.UtillityMethods.synchronize_with_number_of_element(self, ok_btn_css, 1, 25)
            self.set_color(kwargs['text_color'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_text_color=kwargs['text_color'])
            time.sleep(2)
        if 'background_color' in kwargs:
            background_color_obj=self.driver.find_element_by_css_selector("#csStyleDlg #FontBackColor img")
            CoreUtillityMethods.python_left_click('self', background_color_obj)
#             utillity.UtillityMethods.default_left_click(self, object_locator=background_color_obj, **kwargs)
            self.set_color(kwargs['background_color'])
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_background_color=kwargs['background_color'])
            time.sleep(2)
        if 'btn_reset' in kwargs:
            btn_reset_ele=self.driver.find_element_by_css_selector("#csStyleDlg #Reset img")
            utillity.UtillityMethods.default_left_click(self, object_locator=btn_reset_ele, **kwargs)
            time.sleep(1)
            self.traffic_light_verify_style_popup(btn_reset_ele, font_name='Arial', font_size='9', bold_btn=False, italic_btn=False, underline_btn=False,
                                                    left_btn=False, center_btn=False, right_btn=True)
            time.sleep(2)
            self.traffic_light_verify_preview(rownum, preview_font_name='Arial', preview_font_size=9, preview_bold=False, preview_italic=False, 
                                                    preview_underline=False, preview_left=False, preview_center=False, preview_right=True, 
                                                    preview_text_color='gray8', preview_background_color='white', preview_default_text='Arial 9')
            time.sleep(1)
    
    
    def traffic_light_verify_style_popup(self, popup_elem, **kwargs): 
        '''
        :params font_name='Arial'
        :params font_size=9
        :params bold_btn=True
        :params italic_btn=True
        :params underline_btn=True
        :params left_btn=True
        :params center_btn=True
        :params right_btn=True
        :Usage  verify_report_style_popup_property(font_name='Arial', font_size=12, bold=True, italic=True, underline=True, 
                                                    left_btn=True)
        '''
        if 'font_name' in kwargs:
            actual_font_name=popup_elem.find_element_by_css_selector("div[class*='combo-box-label']").text.strip().lower()
            expected_font_name=kwargs["font_name"].lower()
            utillity.UtillityMethods.asequal(self, expected_font_name, actual_font_name , "Step X: Verify " + kwargs["font_name"] + " font name within the style within style window.")
        if 'font_size' in kwargs:
            actual_font_size=str(popup_elem.find_element_by_css_selector("div[class*='combo-box-label']").text.strip())
            expected_font_size=str(kwargs["font_size"])
            utillity.UtillityMethods.asequal(self, expected_font_size, actual_font_size, "Step X: Verify " + str(kwargs["font_size"]) + " font size within the style within style window.")
        if 'bold_btn' in kwargs:
            actual_bold_btn_status=bool(re.match('.*checked\s*', popup_elem.get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['bold_btn'], actual_bold_btn_status , "Step X: Verify bold within the style within style window "+str(kwargs['bold_btn'])+".")
        if 'italic_btn' in kwargs: 
            actual_italic_btn_status=bool(re.match('.*checked\s*', popup_elem.get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['italic_btn'], actual_italic_btn_status, "Step X: Verify italic within the style within style window "+str(kwargs['italic_btn'])+".")
        if 'underline_btn' in kwargs:
            actual_underline_btn_status=bool(re.match('.*checked\s*', popup_elem.get_attribute("class"))) 
            utillity.UtillityMethods.asequal(self, kwargs['underline_btn'], actual_underline_btn_status, "Step X: Verify Underline within the style within style window "+str(kwargs['underline_btn'])+".")
        if 'left_btn' in kwargs:
            actual_left_btn_status=bool(re.match('.*checked\s*', popup_elem.get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['left_btn'], actual_left_btn_status, "Step X: Verify left justify within the style within style window "+str(kwargs['left_btn'])+".")
        if 'center_btn' in kwargs:
            actual_center_btn_status=bool(re.match('.*checked\s*', popup_elem.get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['center_btn'], actual_center_btn_status, "Step X: Verify center justify within the style within style window "+str(kwargs['center_btn'])+".")
        if 'right_btn' in kwargs:
            actual_right_btn_status=bool(re.match('.*checked\s*', popup_elem.get_attribute("class")))
            utillity.UtillityMethods.asequal(self, kwargs['right_btn'], actual_right_btn_status, "Step X: Verify right justify within the style within style window "+str(kwargs['right_btn'])+".")

         

    def traffic_light_verify_preview(self, rownum, **kwargs):
        '''
        :params preview_font_name='Arial'
        :params preview_font_size=9
        :params preview_bold=True
        :params preview_italic=True
        :params preview_underline=True
        :params preview_left=True
        :params preview_center=True
        :params preview_right=True
        :params preview_text_color='blue'
        :params preview_background_color='cyan'
        :params preview_default_text='Arial 9'
        :Usage  verify_report_style_popup_property(preview_font_name='Arial', preview_font_size=9, preview_bold=True, preview_italic=True, 
                                                     preview_underline=True, preview_left=True, preview_text_color='blue',
                                                     preview_background_color='cyan', preview_default_text='Arial 9')
        '''
        row_elems=self.driver.find_elements_by_css_selector("#trafficLightsDlg #cstyMainPane [id^='condGridRowBox']")
        preview_elem=row_elems[rownum-1].find_element_by_css_selector("[id^='cstyPreviewLabel']")
        if 'preview_font_name' in kwargs:
            expected_font_name=kwargs["preview_font_name"].lower()
            applied_font_name=preview_elem.value_of_css_property("font-family").strip('"').lower()
            utillity.UtillityMethods.asequal(self, expected_font_name, applied_font_name, "Step X: Verify font name "+str(kwargs["preview_font_name"])+" within the style within style Preview window.")
        if 'preview_font_size' in kwargs:
            expected_font_size=kwargs["preview_font_size"]
            applied_font_size=preview_elem.value_of_css_property("font-size")
            utillity.UtillityMethods.asequal(self, str(expected_font_size)+"px", applied_font_size , "Step X: Verify font size "+str(kwargs["preview_font_size"])+" within the style within style Preview window.")
        if 'preview_bold' in kwargs:
            try:
                if preview_elem.is_displayed():
                    status_bold=True
            except:
                status_bold=False
            utillity.UtillityMethods.asequal(self, kwargs['preview_bold'], status_bold, "Step X: Verify bold within the style within style preview window "+str(kwargs['preview_bold'])+".")
        if 'preview_italic' in kwargs: 
            try:
                if preview_elem.is_displayed():
                    status_italic=True
            except:
                status_italic=False
            utillity.UtillityMethods.asequal(self, kwargs['preview_italic'], status_italic, "Step X: Verify italic within the style within style preview window "+str(kwargs['preview_italic'])+".")
        if 'preview_underline' in kwargs:
            try:
                if preview_elem.is_displayed():
                    status_underline=True
            except:
                status_underline=False
            utillity.UtillityMethods.asequal(self, kwargs['preview_underline'], status_underline, "Step X: Verify Underline within the style within style preview window "+str(kwargs['preview_underline'])+".")
        if 'preview_left' in kwargs:
            val=preview_elem.value_of_css_property('text-align')
            status_left=True if val == 'left' else False
            utillity.UtillityMethods.asequal(self, kwargs['preview_left'], status_left, "Step X: Verify left justify within the style within style preview window "+str(kwargs['preview_left'])+".")
        if 'preview_center' in kwargs:
            val=preview_elem.value_of_css_property('text-align')
            status_center=True if val == 'center' else False
            utillity.UtillityMethods.asequal(self, kwargs['preview_center'], status_center, "Step X: Verify center justify within the style within style preview window "+str(kwargs['preview_center'])+".")
        if 'preview_right' in kwargs:
            val=preview_elem.value_of_css_property('text-align')
            status_right=True if val == 'right' else False
            utillity.UtillityMethods.asequal(self, kwargs['preview_right'], status_right, "Step X: Verify right justify within the style within style preview window "+str(kwargs['preview_right'])+".")
        if 'preview_text_color' in kwargs:
            expected_text_color=utillity.UtillityMethods.color_picker(self, kwargs['preview_text_color'], 'rgba')
            actual_text_color=Color.from_string(preview_elem.value_of_css_property("color")).rgba
            utillity.UtillityMethods.asequal(self, expected_text_color, actual_text_color , "Step X: Verify text color within the style within style preview window.")
        if 'preview_background_color' in kwargs:
            expected_bg_color=utillity.UtillityMethods.color_picker(self, kwargs['preview_background_color'], 'rgba')
            actual_bg_color=Color.from_string(preview_elem.value_of_css_property("background-color")).rgba
            utillity.UtillityMethods.asequal(self, expected_bg_color, actual_bg_color , "Step X: Verify  background color within the style within style preview window.")
        if 'preview_default_text' in kwargs:
            expected_text = kwargs['preview_default_text'].lower()
            actual_text=preview_elem.text.strip().lower()
            utillity.UtillityMethods.asequal(self, expected_text, actual_text , "Step X: Verify  preview default text 'Arail 9' within the style within style preview window.")
            
    def verify_Gradient_fill_bgcolor(self, parent_id, expected_bg_color1, expected_bg_color2, msg, **kwargs):
        """
        This function used to verify Gradient fill color
        :param parent_id='MAINTABLE_wbody0'
        :kwargs['parent_css']="#MAINTABLE_wbody0 rect.chartFrame"
        :param expected_bg_color1='gray'
        :param expected_bg_color2='white'
        :param msg='Step 9'
        :usage verify_Gradient_fill_bgcolor('MAINTABLE_wbody0', 'gray', 'white', 'Step 9')
            or
        :usage verify_Gradient_fill_bgcolor('MAINTABLE_wbody0', 'gray', 'white', 'Step 9', parent_css=""#MAINTABLE_wbody0 rect.chartFrame")
        """
        parent_css = kwargs['parent_css'] if 'parent_css' in kwargs else "#"+parent_id + " rect.chartFrame"
        backgrnd_value=self.driver.find_element_by_css_selector(parent_css).value_of_css_property('fill')        
        backgrnd_value=re.match('.*(#[a-zA-Z0-9_]+).*',backgrnd_value).group(1)
        backgrnd_value=backgrnd_value.replace('maintable', 'MAINTABLE')
        expected_color1=utillity.UtillityMethods.color_picker(self, expected_bg_color1, 'rgba')
        actual_Color1=Color.from_string(self.driver.find_element_by_css_selector("defs>"+backgrnd_value+">stop[offset='0']").value_of_css_property('stop-color')).rgba
        utillity.UtillityMethods.asequal(self, actual_Color1, expected_color1, msg+" : verify Gradient fill background color1.")
        expected_color2=utillity.UtillityMethods.color_picker(self, expected_bg_color2, 'rgba')
        actual_Color2=Color.from_string(self.driver.find_element_by_css_selector("defs>"+backgrnd_value+">stop[offset='1']").value_of_css_property('stop-color')).rgba
        utillity.UtillityMethods.asequal(self, actual_Color2, expected_color2, msg+".1 : verify Gradient fill background color2.")
        
    def verify_background_color(self, elem_css, color_name, **kwargs):
        """
        :Param:elem_css="TableChart_1"
        :@Param:color_name="blue"
        :@Usage:verify_canvas_background_color("TableChart_1", "blue")
        """
        expected_bg_color=utillity.UtillityMethods.color_picker(self, color_name, 'rgba')
        actual_bg_color=Color.from_string(elem_css.value_of_css_property("background-color")).rgba
        utillity.UtillityMethods.asequal(self, expected_bg_color, actual_bg_color , "Step X: Verify  background color in preview.")
    
    def type_text_in_editor(self, text_list):
        """
        This method used to type text in editor. Using this method we can type any number of line text
        Example Usage : type_text_in_editor(['This is Line 1', 'This is Line 2'])
        """
        editor=self.driver.find_element_by_css_selector("#subheaderDlg #Editor")
        utillity.UtillityMethods.click_on_screen(self, editor, coordinate_type='middle', click_type=0)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        time.sleep(2)
        for count, text_line in enumerate(text_list) :
            pyautogui.typewrite(str(text_line))
            time.sleep(2)
            if count != len(text_list)-1 :
                pyautogui.press('enter')
                time.sleep(2)
    
    def click_on_header_footer_editor(self):
        """
        Description : Left click on Header and Footer editor 
        """
        editor = self.driver.find_element_by_id("Editor")
        CoreUtillityMethods.left_click(self, editor)