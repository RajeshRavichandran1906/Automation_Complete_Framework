from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.lib.base import BasePage
from common.locators.visualization_properties_locators import VisualizationPropertiesLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from common.lib.javascript import JavaScript as js
import time
import sys
from common.lib.global_variables import Global_variables
import pyautogui
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
    from pymouse import PyMouse
    mouse_=PyMouse()
else:
    from uisoup import uisoup
    import keyboard


class Visualization_Properties(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Visualization_Properties, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))

    def select_single_item_from_show_prompt_table(self, item_name, parent_prompt_css, javascript_scroll_down): 
        '''
        Desc: This function will select a single item from the frompt table. If the item is not visible, then use javascript to make it visible.
        '''   
        items_css=parent_prompt_css + "  table[style*=hidden] tr"
        prompt_items=self.driver.find_elements_by_css_selector(items_css)
        for elem in prompt_items: 
            if elem.text.strip()==item_name:
                required_item=elem.find_element_by_css_selector("input")
                if javascript_scroll_down == True:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", required_item)
                coreutillityobject.left_click(self, required_item)
                time.sleep(2)
                break
    
    def verify_show_prompt_table_list(self, expected_items_list, parent_prompt_css, msg):
        '''
        Desc: This function will verify all items in the table.
        '''
        items_css=parent_prompt_css + "  table[style*=hidden] tr"
        prompt_items=self.driver.find_elements_by_css_selector(items_css)
        actual_prompt_list=[el.text.strip() for el in prompt_items]
        utillityobject.as_List_equal(self, expected_items_list, actual_prompt_list, msg)
        
    def verify_item_checked_status_in_show_prompt_table(self, item_name, parent_prompt_css, javascript_scroll_down, checked_status, msg):
        '''
        Desc: This function will verify if the requested item is checked or not. If the item is not visible, then use javascript to make it visible.
        '''
        items_css=parent_prompt_css + "  table[style*=hidden] tr"
        prompt_items=self.driver.find_elements_by_css_selector(items_css)
        for elem in prompt_items: 
            if elem.text.strip()==item_name:
                time.sleep(2)
                val_obj=elem.find_element_by_css_selector("input")
                if javascript_scroll_down == True:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", val_obj)
                stat=val_obj.get_attribute('checked')
                status=True if stat=='true' else False
        utillityobject.asequal(self, checked_status, status, msg)
    
    def select_prompt_arrow(self, parent_prompt_css):
        '''
        Desc: This function will select the prompt menu item.
        '''
        prompt_menu_selector_arrow=self.driver.find_element_by_css_selector(parent_prompt_css + " table span")
        coreutillityobject.python_move_to_element(self, prompt_menu_selector_arrow)
        time.sleep(1)        
        self.driver.find_element(*VisualizationPropertiesLocators.prompt_dropdown).click()
        
    def select_prompt_menu(self, parent_prompt_css, prompt_menu_item):
        '''
        Desc: This function will select the prompt menu item.
        '''
        Visualization_Properties.select_prompt_arrow(self, parent_prompt_css)
        utillityobject.select_bipopup_list_item(self, prompt_menu_item)
        time.sleep(2)  
    
    def verify_prompt_menu(self, parent_prompt_css, expected_prompt_menu_list, msg):
        '''
        Desc: This function will select the prompt menu item.
        '''
        Visualization_Properties.select_prompt_arrow(self, parent_prompt_css)
        time.sleep(2)
        utillityobject.verify_bipopup_list_item(self, expected_prompt_menu_list, msg)
           
    
    def verify_prompt_title(self, parent_prompt_css, title_name):
        '''
        Desc: 
        '''
        prompt_title_obj=self.driver.find_element_by_css_selector(parent_prompt_css + " table span")
        utillityobject.asequal(self, prompt_title_obj.text.strip(), title_name, "Step X: Verify prompt title")
        
    def edit_prompt_title(self, parent_prompt_css, old_title, new_title, close_button_type):
        '''
        Desc: This function is used to edit the prompt title. Close button can be OK OR Cancel
        '''
        dialog_css = "div[id^='BiDialog'] [class*='window-active']"
        title_input_obj=self.driver.find_element_by_css_selector(dialog_css + " input[class*='text-field']")
        actual_title=title_input_obj.get_attribute('value')
        utillityobject.asequal(self, old_title, actual_title, "Step X: Verify Edit Title Appears.")
        if close_button_type=='OK':
            utillityobject.set_text_field_using_actionchains(self, title_input_obj, new_title)
            utillityobject.click_dialog_button(self, dialog_css, "OK")
            time.sleep(1)
            Visualization_Properties.verify_prompt_title(self, parent_prompt_css, new_title)
        elif close_button_type=='Cancel':
            utillityobject.click_dialog_button(self, dialog_css, "Cancel")
            time.sleep(1)
            Visualization_Properties.verify_prompt_title(self, parent_prompt_css, old_title)
    
    def verify_slider_min_max_value(self, parent_css, expected_val, msg, drag_button='min', comparison_type='integer'):
        '''
        Desc: This function is used to verify either minimum or maximum value of the slider. comparison_type can be'integer' OR 'floating'
        Live preview:
        verify_slider_range_filter_prompts('#ar_Prompt_1','min','12.22',msg="Step")
        verify_slider_range_filter_prompts('#ar_Prompt_1','max','122135656.22',msg="Step")
        Run window:
        verify_slider_range_filter_prompts('#LOBJ1_cs','min','12.22',msg="Step")
        verify_slider_range_filter_prompts('#LOBJ1_cs','max','122135656.22',msg="Step")
        verify_slider_range_filter_prompts('#sliderPROMPT_1','max','122135656.22',msg="Step")
        '''
        if drag_button == 'min':
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            final_start_val=int(initial_final_start_val) if comparison_type == 'integer' else float(initial_final_start_val) if comparison_type == 'floating' else initial_final_start_val
            utillityobject.as_LE(self, expected_val, final_start_val, msg)
            
        else:
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            start_val=int(initial_final_start_val) if comparison_type == 'integer' else float(initial_final_start_val) if comparison_type == 'floating' else initial_final_start_val
            utillityobject.as_LE(self, start_val, expected_val, msg)  
                      
    def move_slider_using_page_up_or_down_key(self, parent_css, drag_button, move_type, move_times, comparison_type):
        '''
        Desc: This function is used to drag the slider in prompt panel using Page up and Page Down movement. 
            Comparison_type can be'integer' OR 'floating'.
        parent_css: #ar_Prompt_1 or #ar_Prompt_2, ...etc.
        drag_button: 'min' OR 'max'(Only for range we will have min and max buttons, for others we will have only min button for dragging.) 
        move_type: 'left' OR 'right'('right' means left to right AND 'left' means right to left)
        move_times: 1, 2, 3...
        comparison_type='str' OR 'float' OR 'int'
        Usage: move_slider_measure('#ar_Prompt_1','min', 'left', 2, 'float')
        ''' 
        counter=0
        start_point_index = 0 if drag_button == 'min' else 1
        initial_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
        start_val=int(initial_start_val) if comparison_type == 'integer' else float(initial_start_val) if comparison_type == 'floating' else initial_start_val
        start_point=self.driver.find_elements_by_css_selector(parent_css + " div[id^='slider_'] [class^='ui-slider-handle']")[start_point_index]
        start_point.click()
        if Global_variables.browser_name in ['firefox']:
            time.sleep(8)
        else:
            time.sleep(3)
        if move_type == 'right':
            while counter < move_times:
                start_point.send_keys(keys.Keys.PAGE_UP) 
                time.sleep(5) 
                counter = counter+1
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            final_start_val=int(initial_final_start_val) if comparison_type == 'int' else float(initial_final_start_val) if comparison_type == 'float' else initial_final_start_val
            utillityobject.as_LE(self, start_val, final_start_val,"Step X : slider dragged from left to right.")
        elif move_type == 'left':
            start_point.click()
            while counter < move_times:
                start_point.send_keys(keys.Keys.PAGE_DOWN) 
                time.sleep(5) 
                counter = counter+1
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            final_start_val=int(initial_final_start_val) if comparison_type == 'int' else float(initial_final_start_val) if comparison_type == 'float' else initial_final_start_val
            utillityobject.as_GE(self, start_val, final_start_val, "Step X : slider dragged from right to left.") 
    
    def move_slider_using_arrow_left_and_right_key(self,promptNum, **kwargs):
        """
        :param self: 
        :param promptNum: prompt number should be given in this format '1'
        :param kwargs: r1 = 2 , or r2 = 6 r1 moves front left to right , r2 moves end point right to left value given should be integer
         function only applicable for measure field 
        :Usage:ia.move_slider_dimension_sale_month("1",r1=2,r2=6)
        :author: Gobinath 
        """ 
        prompt = self.driver.find_element_by_xpath(VisualizationPropertiesLocators.prompts.format(promptNum))
        sliders = prompt.find_elements_by_tag_name('span')
        start_val =sliders[0].text
        end_val = sliders[1].text
        s = prompt.find_element_by_css_selector("div[id^='slider_']").find_elements_by_tag_name('a')
        if 'r1' in kwargs:
            s[0].click()
            s2 = kwargs['r1'] - int(start_val)
            for _ in range(1,s2+1):
                s[0].send_keys(keys.Keys.ARROW_RIGHT)                     
            print('moved to value %s'%(sliders[0].text))
        if 'r2' in kwargs:
            s[1].click()   
            s2 = int(end_val)- kwargs['r2'] 
            for _ in range(1,s2+1):
                s[1].send_keys(keys.Keys.ARROW_LEFT)                     
            print('moved to value %s'%(sliders[1].text))         
                                   
    '''***********************************OLD FUNCTIONS*************************************'''
    ''' Filter Prompt '''
    def select_or_verify_show_prompt_item(self, prompt_index, item_name, verify=False, **kwargs):
        """
        Params: prompt_index: 1,2,3,... [Should be a integer and not string]
        Params:item_name: Item Name to be selected within the prompt box.
        Params:verify=False means to select the item. verify=True means to verify whether it is selected.
        Params:kwargs['verify_type']=can be True(Verify Checked)/False(Verify unchecked)
        kwargs: menu_list=['Video Production', 'Accessories']
        kwargs: scroll_down=True(In order to scroll down)
        Syntax:menu_list_items=['[All]', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        propertyobj.select_or_verify_show_prompt_item('1', '[All]', menu_list=menu_list_items,msg="Step18: Verify prompt menu list")
        author: Niranjan
        """
        prompt_css="div[id*='Prompt_" + str(prompt_index) + "'] table[style*=hidden] tr"
        prompt_items=self.driver.find_elements_by_css_selector(prompt_css)
        if 'menu_list' in kwargs:
            actual_prompt_list=[el.text.strip() for el in prompt_items]
            utillityobject.as_List_equal(self, kwargs['menu_list'], actual_prompt_list, kwargs['msg'])
        else:  
            if verify==True:
                for elem in prompt_items: 
                    if elem.text.strip()==item_name:
                        time.sleep(2)
                        val_obj=elem.find_element_by_css_selector("input")
                        if 'scroll_down' in kwargs:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", val_obj)
                        stat=val_obj.get_property('checked')
#                         if stat=='true':
#                             stat=True
#                         else:
#                             stat=False
                utillityobject.asequal(self, str(kwargs['verify_type']).lower(), str(stat).lower(), kwargs['msg'])
            else:
                for elem in prompt_items: 
                    if elem.text.strip()==item_name:
                        time.sleep(2)
                        val_obj=elem.find_element_by_css_selector("input")
                        if 'scroll_down' in kwargs:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", val_obj)
                        utillityobject.default_left_click(self,object_locator=val_obj,action_move=True, **kwargs)
                        time.sleep(2)
                        break
        time.sleep(1)

    def change_prompt_options(self,prompt_num,selectMenu, **kwargs):
        """
        :param prompt_num: 1,2,3,...(filter prompt number) (ia.change_prompt_options("1","Dropdown (Single Select)"))
        selectMenu: Equals, Not Equals,Dropdown (Single Select), List (Single Select)..
        author: Sindhuja & Gobinath Date: 23 May
        """
        move_prompt=self.driver.find_element_by_css_selector("div#ar_Prompt_" + prompt_num + " table span")
        element_coordinate = coreutillityobject.get_web_element_coordinate(self, move_prompt)
        if Global_variables.browser_name in ['firefox']:
            utillityobject.click_type_using_pyautogui(self, move_prompt, **kwargs)
        else:
            action = ActionChains(self.driver)
            action.move_to_element(move_prompt).perform()
            del action
        if Global_variables.browser_name in ['edge']:
            if sys.platform == 'linux':
                mouse_.move(int(element_coordinate['x']+9), int(element_coordinate['y']))
                time.sleep(.1)
                mouse_.click(element_coordinate['x']+9, element_coordinate['y'])
            else:
                uisoup.mouse.move(element_coordinate['x']+9, element_coordinate['y'])
                time.sleep(.01)
                import autopy
                autopy.mouse.smooth_move(element_coordinate['x'], element_coordinate['y'])
                time.sleep(.01)
                uisoup.mouse.move(element_coordinate['x']+9, element_coordinate['y'])
                time.sleep(.1)
                autopy.mouse.click()
        time.sleep(1)
        dropdown_elem=utillityobject.validate_and_get_webdriver_object(self, "[id^='FilterBox'] [src^='data:image/png;base64']", 'filter box')
        dropdown_elem.click()
        '''should revert this image click for 82xx once suite run happens from 8203 cvs track'''
        utillityobject.select_or_verify_bipop_menu(self, selectMenu)
        
    def filter_prompt_select_drop_down(self,prompt_num,values, **kwargs):
        """
        :param prompt_num: 1,2 (indicates filter prompt number)
        :param values: United States
        :Usgae: ia.filter_prompt_select_drop_down("2", "Brazil")
        :author: Sindhuja Date: June 10
        """
        promptNum = self.driver.find_element_by_xpath("//div[contains(@id,'ar_Prompt_"+prompt_num+"')]")
        action = ActionChains(self.driver)
        if Global_variables.browser_name in ['firefox']:
            utillityobject.click_type_using_pyautogui(self, promptNum, **kwargs)
        else:
            action.move_to_element(promptNum).perform()
        time.sleep(1)
        select = Select(self.driver.find_element_by_xpath("//select[contains(@id,'combobox')]"))
        select.select_by_visible_text(values)

        ''' Slider '''
       
    def verify_slider_range_filter_prompts(self,parent_css, drag_button, expected_val,comparison_type='str', **kwargs):
        """
        Live preview:
        verify_slider_range_filter_prompts('#ar_Prompt_1','min','12.22',msg="Step")
        verify_slider_range_filter_prompts('#ar_Prompt_1','max','122135656.22',msg="Step")
        Run window:
        verify_slider_range_filter_prompts('#LOBJ1_cs','min','12.22',msg="Step")
        verify_slider_range_filter_prompts('#LOBJ1_cs','max','122135656.22',msg="Step")
        verify_slider_range_filter_prompts('#sliderPROMPT_1','max','122135656.22',msg="Step")
        """
        if drag_button == 'min':
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            final_start_val=int(initial_final_start_val) if comparison_type == 'int' else float(initial_final_start_val) if comparison_type == 'float' else initial_final_start_val
            utillityobject.as_LE(self, expected_val, final_start_val,kwargs['msg'])
            
        else:
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            start_val=int(initial_final_start_val) if comparison_type == 'int' else float(initial_final_start_val) if comparison_type == 'float' else initial_final_start_val
            utillityobject.as_LE(self, start_val, expected_val,kwargs['msg'])  
                      
    def move_slider_measure(self,parent_css, drag_button, move_type, move_times, comparison_type='str'):
        """
        parent_css: #ar_Prompt_1 or #ar_Prompt_2, ...etc.
        drag_button: 'min' OR 'max'(Only for range we will have min and max buttons, for others we will have only min button for dragging.) 
        move_type: 'left' OR 'right'('right' means left to right AND 'left' means right to left)
        move_times: 1, 2, 3...
        comparison_type='str' OR 'float' OR 'int'
        Usage: move_slider_measure('#ar_Prompt_1','min', 'left', 2, 'float')
        """ 
        counter=0
        start_point_index = 0 if drag_button == 'min' else 1
        initial_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
        start_val=int(initial_start_val) if comparison_type == 'int' else float(initial_start_val) if comparison_type == 'float' else initial_start_val
        start_point=self.driver.find_elements_by_css_selector(parent_css + " div[id^='slider_'] [class^='ui-slider-handle']")[start_point_index]
        cursour_point = coreutillityobject.get_web_element_coordinate(self, start_point)
        coreutillityobject.python_move_to_offset(self, cursour_point['x'], cursour_point['y'])
        time.sleep(2)
        coreutillityobject.python_click_with_offset(self, cursour_point['x'], cursour_point['y'])
        js.wait_for_page_loads(self,30)
        coreutillityobject.python_click_with_offset(self, cursour_point['x'], cursour_point['y'])
        time.sleep(3)
        if move_type == 'right':
            while counter < move_times:
                if sys.platform == 'linux':
                    pykeyboard.tap_key(pykeyboard.page_up_key)
                else:
                    if Global_variables.browser_name=="edge":
                        start_point.send_keys(keys.Keys.PAGE_UP)
                    else: 
                        keyboard.send('page up') 
                time.sleep(5) 
                counter = counter+1
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            final_start_val=int(initial_final_start_val) if comparison_type == 'int' else float(initial_final_start_val) if comparison_type == 'float' else initial_final_start_val
            utillityobject.as_LE(self, start_val, final_start_val,"Step X : slider dragged from left to right.")
        else:
            start_point.click()
            while counter < move_times:
                if sys.platform == 'linux':
                    pykeyboard.tap_key(pykeyboard.page_down_key)
                else:
                    if Global_variables.browser_name=="edge":
                        start_point.send_keys(keys.Keys.PAGE_DOWN) 
                    else: 
                        keyboard.send('page down') 
                time.sleep(5) 
                counter = counter+1
            initial_final_start_val=self.driver.find_element_by_css_selector(parent_css + " span[id$='s_"+drag_button+"']").text.strip()
            final_start_val=int(initial_final_start_val) if comparison_type == 'int' else float(initial_final_start_val) if comparison_type == 'float' else initial_final_start_val
            utillityobject.as_GE(self, start_val, final_start_val, "Step X : slider dragged from right to left.") 
            
    def move_slider_dimension_sale_month(self,promptNum, **kwargs):
        """
        :param self: 
        :param promptNum: prompt number should be given in this format '1'
        :param kwargs: r1 = 2 , or r2 = 6 r1 moves front left to right , r2 moves end point right to left value given should be integer
         function only applicable for measure field 
        :Usage:ia.move_slider_dimension_sale_month("1",r1=2,r2=6)
        :author: Gobinath 
        """ 
        prompt = self.driver.find_element_by_xpath(VisualizationPropertiesLocators.prompts.format(promptNum))
        sliders = prompt.find_elements_by_tag_name('span')
        start_val =sliders[0].text
        end_val = sliders[1].text
        s = prompt.find_element_by_css_selector("div[id^='slider_']").find_elements_by_tag_name('a')
        if 'r1' in kwargs:
            s[0].click()
            s2 = kwargs['r1'] - int(start_val)
            for _ in range(1, s2+1):
                s[0].send_keys(keys.Keys.ARROW_RIGHT)                     
            print('moved to value %s'%(sliders[0].text))
        if 'r2' in kwargs:
            s[1].click()   
            s2 = int(end_val)- kwargs['r2'] 
            for _ in range(1, s2+1):
                s[1].send_keys(keys.Keys.ARROW_LEFT)                     
            print('moved to value %s'%(sliders[1].text))  

    def verify_filter_prompt_pane(self,msg):
        """
        :Usage: ia.verify_filter_prompt_pane("step8:")
        To verify that the Filter Prompts are cleared on the canvas
        """
        try:
            disp=self.driver.find_element_by_css_selector("div[id^='BoxLayoutFilterBox']").is_displayed()
            utillityobject.asequal(self, disp, False, msg+" Verify Filter Prompts are not cleared on the canvas")
        except NoSuchElementException:
            utillityobject.asequal(self, True, True, msg+" Verify Filter Prompts are cleared on the canvas")
    
    def select_or_verify_prompt_options(self, prompt_num, **kwargs):
        """
        :param prompt_num: 1,2,3,...(filter prompt number) (ia.change_prompt_options("1","Dropdown (Single Select)"))
        verify_prompt=True/False(This is to verify the drop down menu), if so provide the menu list also as parameter.
        menu_list: Equals, Not Equals,Dropdown (Single Select), List (Single Select)..
        edit_title=True/False
        old_prompt_title=
        new_prompt_title=
        hide_title=True/False
        Usage1: propertyobj.select_or_verify_prompt_options("1", edit_title = True, old_prompt_title = "Product,Category", new_prompt_title = "Product", msg = 'Step 08')
        Usage2: propertyobj.select_or_verify_prompt_options("1", show_title = True, msg = 'Step17')
        author: Niranjan/Magesh
        """
        if 'msg' in kwargs:
            kwargs['msg'] = kwargs['msg']
        else:
            kwargs['msg']= 'Step X'
        action = ActionChains(self.driver)
        if 'show_title' in kwargs:
            if kwargs['show_title']==True:
                move_prompt=self.driver.find_element_by_css_selector("div#ar_Prompt_" + prompt_num + " table")
        else:
            move_prompt=self.driver.find_element_by_css_selector("div#ar_Prompt_" + prompt_num + " table span")
            original_prompt_title=move_prompt.text.strip()
        if Global_variables.browser_name in ['firefox']:
            utillityobject.click_type_using_pyautogui(self, move_prompt, **kwargs)
        else:
            action.move_to_element(move_prompt).perform()
        time.sleep(1)        
        self.driver.find_element(*VisualizationPropertiesLocators.prompt_dropdown).click()
        time.sleep(5)
        if 'verify_prompt' in kwargs:
            if kwargs['verify_prompt']==True:
                utillityobject.select_or_verify_bipop_menu(self, kwargs['menu_list'])
        if 'edit_title' in kwargs:
            if kwargs['edit_title']==True:
                utillityobject.select_or_verify_bipop_menu(self, 'Edit Title...')
                time.sleep(3)
                self.driver.implicitly_wait=1
                btn_css = "div[id^='BiDialog'] [class*='window-active']"
                edit_title_obj=self.driver.find_element_by_css_selector(btn_css)
                actual_value=edit_title_obj.find_element_by_css_selector("input").get_attribute('value')
                utillityobject.asequal(self, actual_value, kwargs['old_prompt_title'], kwargs['msg']+": Verify Edit Title Appears.")
                if 'new_prompt_title' in kwargs:
                    text_field = edit_title_obj.find_element_by_css_selector("input")
                    utillityobject.set_text_field_using_actionchains(self, text_field, kwargs['new_prompt_title'])
                    utillityobject.click_dialog_button(self,btn_css,"OK")
                    time.sleep(1)
                    move_prompt=self.driver.find_element_by_css_selector("div#ar_Prompt_" + prompt_num + " table span")
                    utillityobject.asequal(self, move_prompt.text.strip(), kwargs['new_prompt_title'], kwargs['msg']+": Verify Prompt Title Changed.")
                else:
                    original_prompt_title=move_prompt.text.strip()
                    utillityobject.click_dialog_button(self,btn_css,"Cancel")
                    time.sleep(1)
                    utillityobject.asequal(self, original_prompt_title, kwargs['old_prompt_title'], kwargs['msg']+": Verify Prompt Title does not Change.")
        if 'hide_title' in kwargs:
            if kwargs['hide_title']==True:
                utillityobject.select_or_verify_bipop_menu(self, 'Hide Title')
                time.sleep(3)
                self.driver.implicitly_wait=1
                try:
                    status=self.driver.find_element_by_css_selector("div#ar_Prompt_" + prompt_num + " table span").is_displayed()
                    print(status)
                    utillityobject.asequal(self, status, False, kwargs['msg']+": Verify Hide Title does not work.")
                except NoSuchElementException:
                    utillityobject.asequal(self, True, True, kwargs['msg']+": Verify Hide Title works.")  
        if 'show_title' in kwargs:
            if kwargs['show_title']==True:
                utillityobject.select_or_verify_bipop_menu(self, 'Show Title')
                time.sleep(3)
                self.driver.implicitly_wait=1
                try:
                    status=self.driver.find_element_by_css_selector("div#ar_Prompt_" + prompt_num + " table span").is_displayed()
                    print(status)
                    utillityobject.asequal(self, status, True, kwargs['msg']+": Verify Show Title works.")
                except NoSuchElementException:
                    utillityobject.asequal(self, True, False, kwargs['msg']+": Verify Show Title does not works.")
                    
    
    def drag_minimum_value_slider_in_filter_prompt(self, target_value, prompt_css="#Prompt_1"): 
        """
        Description : Drag the minimum value slider in filter prompt
        :Usage : drag_minimum_value_slider_in_filter_prompt(14810)
        """
        minimum_value_css = prompt_css + " div[id^='slider_'] span[id$='s_min']"
        maximum_value_css = prompt_css + " div[id^='slider_'] span[id$='s_max']"
        minimum_value_slider_css = prompt_css + " div[id^='slider_'] [class^='ui-slider-handle']"
        slider_range_css = prompt_css + " div.ui-slider-range"
        target_value = float(target_value)
        minimum_value = float(self.driver.find_element_by_css_selector(minimum_value_css).text.strip())
        if minimum_value == target_value :
            raise_msg = "Minimum value {0} and target value {1} should not sample".format(minimum_value, target_value)
            raise ValueError(raise_msg)
        slider_range = self.driver.find_element_by_css_selector(slider_range_css)
        if minimum_value < target_value :
            maximum_value = float(self.driver.find_element_by_css_selector(maximum_value_css).text.strip())
            slider_range_width = slider_range.size['width']
            total_value = maximum_value - minimum_value
            distance_ratio = slider_range_width / total_value
            actual_distance_value = target_value - minimum_value
            target_value_distance = actual_distance_value * distance_ratio
        else :
            raise NotImplementedError
        min_value_slider = self.driver.find_element_by_css_selector(minimum_value_slider_css)
        min_value_slider_cord = coreutillityobject.get_web_element_coordinate(self, min_value_slider)
        x1 = min_value_slider_cord['x']
        y1 = min_value_slider_cord['y']
        x2 = min_value_slider_cord['x'] + target_value_distance
        y2 = min_value_slider_cord['y']
        if sys.platform == 'linux':
            mouse_.press(int(x1), int(y1))
            pyautogui.moveTo(int(x2), int(y2), duration=3)
            mouse_.release(int(x2), int(y2))
        else:
            uisoup.mouse.move(x1,y1)
            uisoup.mouse.drag(x1,y1, x2, y2)  
        minimum_value = float(self.driver.find_element_by_css_selector(minimum_value_css).text.strip())
        if minimum_value != target_value :
            key = 'right_arrow' if minimum_value < target_value else 'left_arrow'
            total_value = abs(minimum_value - target_value)
            while True :
                if sys.platform == 'linux':
                    if minimum_value < target_value:
                        pykeyboard.tap_key(pykeyboard.right_key)
                    else:
                        pykeyboard.tap_key(pykeyboard.left_key)
                else:
                    keyboard.press_and_release(key)
                minimum_value = float(self.driver.find_element_by_css_selector(minimum_value_css).text.strip())
                if minimum_value == target_value :
                    break
                