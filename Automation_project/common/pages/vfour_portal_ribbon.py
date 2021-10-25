from common.lib import utillity, core_utility
from common.lib.base import BasePage
from selenium.webdriver.support import expected_conditions as EC
from common.locators.vfour_ribbon_locators import VfourRibbonLocators
import time
import sys
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class Vfour_Portal_Ribbon(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Vfour_Portal_Ribbon, self).__init__(driver)
         
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
        
    def select_tab(self, tabname):
        """
        :PARAM : tabname = 'Insert','Layout', 'Style'
        self.select_tab(tabname = "Insert")
        """
        tab_css="#BIPortalRibbon #" + tabname + "Tab_tabButton"
        elem=self.driver.find_element_by_css_selector(tab_css)
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
    def select_or_verify_layout_navigation(self, **kwargs):
        """
        navigate_item='Top'
        expected_btn_name_list=["None", "Top", "Left", "Right"]
        verify='True'
        """
        elem=self.driver.find_element_by_css_selector("#LayoutTab #LayoutNavigationMenuBtn")
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        btns=self.driver.find_elements_by_css_selector("#ChooseNavigationWindow div[id^='BiToolBarRadioButton']")
        actual_btn_name_list=[el.text.strip() for el in btns]
        if 'verify' in kwargs:
            utillity.UtillityMethods.asequal(self, kwargs['expected_btn_name_list'], actual_btn_name_list , kwargs['msg'])
        elem=btns[actual_btn_name_list.index(kwargs['navigate_item'])]
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
    def select_layout_banner(self, **kwargs):
        """
        banner_area='Top'
        expected_banner_name_list=["Top", "Bottom", "Left", "Right"]
        verify=True
        close=True
        """
        Vfour_Portal_Ribbon.select_ribbon_item(self, "Layout", 'Layout_Banner')
        time.sleep(2)
        banner=self.driver.find_elements_by_css_selector("#ChooseLayoutBannerWindow div[id^='BiToolBarRadioButton']")
        actual_banner_name_list=[el.text.strip() for el in banner]
        if 'verify' in kwargs:
            utillity.UtillityMethods.asequal(self, kwargs['expected_banner_name_list'], actual_banner_name_list , kwargs['msg'])
        elem=banner[actual_banner_name_list.index(kwargs['banner_area'])]
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        if 'close' in kwargs :
            elem=self.driver.find_element_by_css_selector("#ChooseLayoutBannerWindow div[class*='window-close-button']")
            utillity.UtillityMethods.default_click(self, elem)
            time.sleep(2)
    def select_layout_menubar(self, image_name, **kwargs):
        """
        image_name='menubar_topbar_center_32' OR 'menubar_topbar_left_32'...etc.
        verify='True'
        expected_no_of_btns=14(The number of buttons to be verified)
        """
        elem=self.driver.find_element_by_css_selector("#LayoutTab #LayoutMenuBarMenuBtn")
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        btns=self.driver.find_elements_by_css_selector("#ChooseLayoutMenuBarWindow div[id^='BiToolBarRadioButton']")
        if 'verify' in kwargs:
            utillity.UtillityMethods.asequal(self, kwargs['expected_no_of_btns'], len(btns), kwargs['msg'])
        elem=self.driver.find_element_by_css_selector("#ChooseLayoutMenuBarWindow img[src$='" + image_name + ".png']")
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
    def select_or_verify_layout_base_theme(self, button_click='OK', **kwargs):
        '''
        default_theme_name='Neutral'
        theme_name='Neutral'
        button_click='ok' or 'cancel'
        '''
        Vfour_Portal_Ribbon.select_ribbon_item(self, 'Layout', 'Layout_Theme')
        combo_elem="#dlgStyleFileInfo div[class*='combo-box-editable']"
        if 'default_theme_name' in kwargs:
            combo_text=combo_elem+" input"
            act=self.driver.find_element_by_css_selector(combo_text).get_attribute('value')
            utillity.UtillityMethods.asequal(self, act, kwargs['default_theme_name'], kwargs['msg'])
        if 'theme_name' in kwargs:
            combo_btn_elem=self.driver.find_element_by_css_selector(combo_elem+" div[id^='BiButton']")
            utillity.UtillityMethods.select_any_combobox_item(self, combo_btn_elem, kwargs['theme_name'])
        utillity.UtillityMethods.click_dialog_button(self, "#dlgStyleFileInfo", button_click)
    def select_layout_security(self):
        pass
    def select_layout_properties(self):
        pass
    def select_layout_layout(self, **kwargs):
        """
        navigate_item='One Column'
        expected_btn_name_list=["Single Area", "Fluid Canvas", "One Column", "Two Column", "Three Column", "Four Column"]
        verify='True'
        """
        elem=self.driver.find_element_by_css_selector("#LayoutTab #LayoutPageLayoutMenuBtn")
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        btns=self.driver.find_elements_by_css_selector("#ChooseLayoutPageWindow div[id^='BiToolBarRadioButton']")
        actual_btn_name_list=[el.text.strip() for el in btns]
        if 'verify' in kwargs:
            utillity.UtillityMethods.asequal(self, kwargs['expected_btn_name_list'], actual_btn_name_list , kwargs['msg'])
        elem=btns[actual_btn_name_list.index(kwargs['navigate_item'])]
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        
    def select_tool_menu_item(self, item_name, **kwargs):
        """
        param: item_name: 'menu_save' OR 'menu_run' - these need to be get it from Vfour_ribbon_locators.
        :usage select_tool_menu_item('menu_Exit')
        """
        ia_btn=self.driver.find_element(*VfourRibbonLocators.Appbtn)
        core_utility.CoreUtillityMethods.left_click(self, ia_btn)
#         utillity.UtillityMethods.default_left_click(self, object_locator=ia_btn, **kwargs)
        elem1=VfourRibbonLocators.__dict__[item_name]
        Vfour_Portal_Ribbon._validate_page(self, elem1)
        obj_tool_menu=self.driver.find_element(*VfourRibbonLocators.__dict__[item_name])
        core_utility.CoreUtillityMethods.left_click(self, obj_tool_menu)
#         utillity.UtillityMethods.default_left_click(self, object_locator=obj_tool_menu, **kwargs)
        if item_name == 'menu_Save':
            try:
                parent_css= "div[id^='dlgPortalSaveDialog']"
                utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 1, 190)
                time.sleep(1)
                utillity.UtillityMethods.click_dialog_button(self, "#dlgPortalSaveDialog", "OK")
            except:
                print("Save Popup not Displayed")
        time.sleep(3)     
    
    def select_layout_from_page_canvas(self,**kwargs):
        """
        navigate_item='One Column'
        expected_btn_name_list=["Single Area", "Fluid Canvas", "One Column", "Two Column", "Three Column", "Four Column"]
        verify='True'
        """
        page_canvas=self.driver.find_element_by_css_selector("div[class*='bip-page']")
        utillity.UtillityMethods.default_click(self, page_canvas, click_option=1)
        time.sleep(2)
        elem=self.driver.find_element_by_css_selector("table[class*='bip-page-ctx-menu']>tbody>tr>td[class*='bip-icon-page-layout']")
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        btns=self.driver.find_elements_by_css_selector("#ChooseLayoutPageWindow div[id^='BiToolBarRadioButton']")
        actual_btn_name_list=[el.text.strip() for el in btns]
        if 'verify' in kwargs:
            utillity.UtillityMethods.asequal(self, kwargs['expected_btn_name_list'], actual_btn_name_list , kwargs['msg'])
        elem=btns[actual_btn_name_list.index(kwargs['navigate_item'])]
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        
    def select_ribbon_item(self, tab_name, item_name): 
        Vfour_Portal_Ribbon.select_tab(self, tab_name)
        time.sleep(5)
        element_obj=self.driver.find_element(*VfourRibbonLocators.__dict__[item_name])
        utillity.UtillityMethods.default_left_click(self,object_locator=element_obj)
        time.sleep(5)
    
    def select_or_verify_menu_bar(self, **kwargs):
        '''
        select=True
        position='left' or 'center' or 'right'
        position='right' OR 'middle' OR 'left'
        menu_item="Administrator", OR "Tools", OR "Help"...etc.
        menu_list=["Administrator", "Tools", "Administration"... "Help"]
        '''
        menu_bar=self.driver.find_element_by_css_selector("[class*='banner-top'] > div[class*='menu-bar']")
        if 'select' in kwargs :
            utillity.UtillityMethods.default_click(self, menu_bar)
            time.sleep(4)
        if 'position' in kwargs:
            banner=self.driver.find_element_by_css_selector("[class*='banner-top']")
            banner_width=int(banner.size['width'])
            menu_bar_x=int(menu_bar.location['x'])
            menu_bar_width=int(menu_bar.size['width'])
            if kwargs['position']=='left' :
                status=True if menu_bar_x in range(0,40) else False
                utillity.UtillityMethods.asequal(self,True,status,'Step X : Verify menu bar appears in left alignment')
            if kwargs['position']=='center' :
                menu_center=int((menu_bar_width/2)+menu_bar_x)
                banner_center=int(banner_width/2)
                status=True if menu_center in range((banner_center-10),(banner_center+20)) else False
                utillity.UtillityMethods.asequal(self,True,status,'Step X : Verify menu bar appears in center alignment')
            if kwargs['position']=='right' :
                width=menu_bar_x+menu_bar_width
                status=True if width in range((banner_width-20),(banner_width+1)) else False
                utillity.UtillityMethods.asequal(self,True,status,'Step X : Verify menu bar appears in right alignment')
        if 'menu_item' in kwargs:
            elems=menu_bar.find_elements_by_css_selector("span[class*='menu-bar-item']")
            actual_menu_bar_list=[el.text.strip() for el in elems]
            utillity.UtillityMethods.asin(self, kwargs['menu_item'], actual_menu_bar_list , kwargs['msg'])
        if 'menu_list' in kwargs:
            elems=menu_bar.find_elements_by_css_selector("span[class*='menu-bar-item']")
            actual_menu_bar_list=[el.text.strip() for el in elems] 
            utillity.UtillityMethods.asequal(self, kwargs['menu_list'], actual_menu_bar_list , kwargs['msg'])  
    def verify_menu_bar_style(self, **kwargs):
        '''
        :params menu_item = 'Administrstor' or 'tools' or 'Resource' or 'Signout'
        :params border_width = '4'
        :params border_color='red'
        :params border_style='solid'
        :params menubar_background='yellow'
        :params menu_item_font_name='Arial'
        :params menu_item_font_size=9
        :params menu_item_bold=True
        :params menu_item_italic=True
        :params menu_item_underline=True
        :params menu_item_text_color='blue'
        :Usage  verify_menu_bar_style(menu_item='Tools',menu_item_font_name='Arial', menu_item_font_size=9, menu_item_bold=True, menu_item_italic=True, 
                                                     menu_item_underline=True, border_width=4, menu_item_text_color='blue',
                                                     border_color='red', border_style='solid', menubar_background='yellow')
        '''
        menu_bar=self.driver.find_element_by_css_selector("[class*='banner-top'] > div[class*='menu-bar-item'][style*='inherit']")
        elems=menu_bar.find_elements_by_css_selector("span[class*='menu-bar-item']")
        actual_menu_bar_list=[el.text.strip() for el in elems]
        item_obj=elems[0]
        if 'menu_item' in kwargs:
            item_obj=elems[actual_menu_bar_list.index(kwargs['menu_item'])]
        if 'border_width' in kwargs:
            expected_border_width=kwargs["border_width"]
            actual_border_width=menu_bar.value_of_css_property("border-width")
            utillity.UtillityMethods.asequal(self, str(expected_border_width)+"px", actual_border_width , "Step X: Verify menu bar border width "+str(expected_border_width)+"px applied")
        if 'border_color' in kwargs:
            expected_border_color=utillity.UtillityMethods.color_picker(self, kwargs['border_color'], 'rgba')
            actual_border_color=Color.from_string(menu_bar.value_of_css_property("border-color")).rgba
            utillity.UtillityMethods.asequal(self, expected_border_color, actual_border_color , "Step X: Verify menu bar border color " +str(expected_border_color)+" applied")
        if 'border_style' in kwargs:
            expected_border_style=kwargs["border_style"]
            actual_border_style=menu_bar.value_of_css_property("border-style")
            utillity.UtillityMethods.asequal(self, expected_border_style, actual_border_style , "Step X: Verify menu bar border style "+str(expected_border_style)+" applied")
        if 'menubar_background' in kwargs:
            expected_background_color=utillity.UtillityMethods.color_picker(self, kwargs['menubar_background'], 'rgba')
            actual_background_color=Color.from_string(menu_bar.value_of_css_property("background-color")).rgba
            utillity.UtillityMethods.asequal(self, expected_background_color, actual_background_color , "Step X: Verify menu bar background color "+str(expected_background_color)+" applied")
        if 'menu_item_font_name' in kwargs:
            expected_menu_item_font_name=kwargs["menu_item_font_name"]
            actual_menu_item_font_name=item_obj.value_of_css_property("font-family")
            utillity.UtillityMethods.asequal(self, expected_menu_item_font_name, actual_menu_item_font_name , "Step X: Verify font size "+str(expected_menu_item_font_name)+" applied in menu bar item")
        if 'menu_item_font_size' in kwargs:
            expected_menu_item_font_size=kwargs["menu_item_font_size"]
            actual_menu_item_font_size=item_obj.value_of_css_property("font-size")
            utillity.UtillityMethods.asequal(self, str(expected_menu_item_font_size)+"px", actual_menu_item_font_size , "Step X: Verify font size "+str(expected_menu_item_font_size)+"px"+" applied in menu bar item")
        if 'menu_item_bold' in kwargs:
            actual_menu_item_bold=item_obj.value_of_css_property("font-weight")
            utillity.UtillityMethods.asequal(self, '700', actual_menu_item_bold, "Step X: Verify text Bold applied in menu bar item")
        if 'menu_item_italic' in kwargs: 
            actual_menu_item_italics=item_obj.value_of_css_property("font-style")
            utillity.UtillityMethods.asequal(self, 'italic', actual_menu_item_italics, "Step X: Verify text Italics applied in menu bar item")
        if 'menu_item_underline' in kwargs:
            actual_menu_item_underline=item_obj.value_of_css_property("text-decoration-line")
            utillity.UtillityMethods.asequal(self, 'underline', actual_menu_item_underline, "Step X: Verify text Underline applied in menu bar item")
        if 'menu_item_text_color' in kwargs:
            expected_text_color=utillity.UtillityMethods.color_picker(self, kwargs['menu_item_text_color'], 'rgba')
            actual_text_color=Color.from_string(item_obj.value_of_css_property("color")).rgba
            utillity.UtillityMethods.asequal(self, expected_text_color, actual_text_color , "Step X: Verify text color "+str(expected_text_color)+" applied in menu bar item") 
    
    def invoke_and_verify_wf_resource_tree(self, launch_point='bip_ribbon_bar', display_status=True): 
        '''
        launch_point='bip_ribbon_bar' OR 'keybord'
       
        '''  
        if launch_point=='bip_ribbon_bar':
            self.select_ribbon_item('Insert', 'Insert_WebFOCUSResources')
        if launch_point=='keybord':
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.function_keys[8])
            else:
                keyboard.send("F8")
        time.sleep(4)
        css="#ResourcesPanelID #bipResourcesPanel"
        self.driver.implicitly_wait=0
        try:
            status=self.driver.find_element_by_css_selector(css).is_displayed()
            status_msg = 'Invoked and Displayed in Canvas' if display_status == True else "Not Displayed in canvas"
            utillity.UtillityMethods.asequal(self, display_status, status , 'Step X : Verify resource tree '+status_msg+'.')
            canvas_width = self.driver.find_element_by_css_selector("#BIPortalPanel #canvasmainpanel").size['width']
            webresource_location =  self.driver.find_element_by_css_selector("#BIPortalPanel #ResourcesPanelID").location['x']
            if status and canvas_width==webresource_location:
                utillity.UtillityMethods.asequal(self, True, True , 'Step X : Verify "Resource Tree" is displayed right side in BIP Canvas.')
        except NoSuchElementException:
            utillity.UtillityMethods.asequal(self, display_status, False , 'Step X : Resource Tree is not invoked or not displaying.')
    
    def verify_ribbon_item_property(self, tab_name, item_name, msg, **kwargs):
        '''
        tab_name ='Layout', 'Insert', 'Style'
        item_name='Layout','Properties','Accordion','Repeat'
        item_property='disabled' OR 'enabled'
        property_value=true OR false
        @PARAM:'Layout', 'Layout', 'Step x:Verify that the layout button is disabled since there is no page.', item_property='disabled', property_value='true'
        '''
        Vfour_Portal_Ribbon.select_tab(self, tab_name)
        try:
            elem=self.driver.find_element(*VfourRibbonLocators.__dict__[item_name])
            utillity.UtillityMethods.verify_object_visible(self, 'dummy', True, "Step x: Object is visible", elem_obj=elem)
            if 'item_property' in kwargs:
                act=elem.get_property(kwargs['item_property'])
                utillity.UtillityMethods.asequal(self, kwargs['property_value'], act, msg)
        except:
            print(item_name+" is not present in DOM.")
            
    def select_or_verify_top_banner(self, **kwargs):
        '''
        select=True
        bg_color="red", OR "green",...etc.
        msg=your verification message.
        '''
        menu_bar=self.driver.find_element_by_css_selector("[class*='banner-top']")
        if 'select' in kwargs:
            utillity.UtillityMethods.click_on_screen(self, menu_bar, coordinate_type='start', click_type=0,x_offset=250,y_offset=20,**kwargs)
        if 'bg_color' in kwargs:
            expected_bg_color=utillity.UtillityMethods.color_picker(self, kwargs['bg_color'], 'rgba')
            actual_bg_color=Color.from_string(menu_bar.value_of_css_property('background-color')).rgba
            utillity.UtillityMethods.asequal(self, actual_bg_color, expected_bg_color, kwargs['msg'])
            
    def refresh_portal_page(self, verify_elements, launch_point='keybord'):
        '''
        launch_point='bip_ribbon_bar' OR 'keybord'

        ''' 
        if launch_point=='keybord':
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.function_keys[5])
            else:
                keyboard.send("F5")
        time.sleep(5)
        for elem in verify_elements:
            utillity.UtillityMethods.verify_object_visible(self, 'dummy', True, "Step X: Verify object visible after refresh.", elem_obj=elem)
            
    def bip_exit_save(self, btn_name):        
        css="#dlgSavepromptPortal [class*='active'][class*='window']"
        status=self.driver.find_element_by_css_selector(css).is_displayed()
        utillity.UtillityMethods.asequal(self, True, status , 'Step X : Verify BIP_Exit_Save pop-up is displayed')
        btn_css='yesDialogbtnAction' if btn_name=='Yes' else 'noDialogbtnAction' if btn_name=='No' else 'cancelDialogbtnCancel' 
        elem=self.driver.find_element_by_css_selector(css + " #"+ btn_css)
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        
    def bip_save_and_exit(self, btn_name):
        '''
        At this moment, this function is based on "btn_name=yes" condition. For some other scenario, we need to enhance the function
        ''' 
        Vfour_Portal_Ribbon.select_tool_menu_item(self,'menu_Exit')
        try:
            css="#dlgSavepromptPortal [class*='active'][class*='window']"
            status=self.driver.find_element_by_css_selector(css).is_displayed()
            utillity.UtillityMethods.asequal(self, True, status , 'Step X : Verify BIP_Exit_Save pop-up is displayed')
            btn_css='yesDialogbtnAction' if btn_name=='Yes' else 'noDialogbtnAction' if btn_name=='No' else 'cancelDialogbtnCancel' 
            elem=self.driver.find_element_by_css_selector(css + " #"+ btn_css)
            utillity.UtillityMethods.default_click(self, elem)
            time.sleep(2)
            if btn_name == 'Yes':
                parent_css= "div[id^='dlgPortalSaveDialog']"
                utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 1, 190)
                utillity.UtillityMethods.click_dialog_button(self, "#dlgPortalSaveDialog", "OK")
                time.sleep(3)
        except NoSuchElementException:
                pass
        
        
    def select_border_style(self, border_style):
        '''
        :Parm: border_style = 'solid' or 'groove' or 'inset'
        :Usage: self.set_border_style('dotted')
        '''
        styles={'none':'border_none_32.png',
                    'solid':'border_solid_32.png',
                    'dotted':'border_dotted_32.png',
                    'dashed':'border_dashed_32.png',
                    'double':'border_double_32.png',
                    'groove':'border_groove_32.png',
                    'ridge':'border_ridge_32.png',
                    'outset':'border_outset_32.png',
                    'inset':'border_inset_32.png'}
        btns=self.driver.find_elements_by_css_selector("#ChooseBorderStyleWindow div[id^='BiToolBarRadioButton']>div>img")
        actual_btn_name_list=[el.get_attribute('src').split('/')[-1] for el in btns]
        style_elem=btns[actual_btn_name_list.index(styles[border_style])]
        utillity.UtillityMethods.default_click(self, style_elem)
        time.sleep(2)
    
    def select_save_from_toolbar(self, **kwargs):
        parent_css= "div[id^='dlgPortalSaveDialog']"
        ia_btn=self.driver.find_element(*VfourRibbonLocators.toolbar_save)
        utillity.UtillityMethods.default_left_click(self, object_locator=ia_btn, **kwargs)
        try:
            utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 1, 190)
            time.sleep(1)
            save_dialog = self.driver.find_element_by_css_selector(parent_css).is_displayed()
            utillity.UtillityMethods.click_dialog_button(self, "#dlgPortalSaveDialog", "OK")
        except:
            save_dialog=False
        utillity.UtillityMethods.asequal(self, save_dialog, True, "Step X: Verify Save dialog appear and pressed ok button.")
        time.sleep(3)
        
        