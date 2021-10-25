from common.lib import utillity, core_utility
from common.lib.base import BasePage
from common.pages import active_miscelaneous
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
import re
import time
import pyautogui
from common.lib.global_variables import Global_variables
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard


class Active_Filter_Selection(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Filter_Selection, self).__init__(driver)

    def _validate_page(self):
        print("Implement Page Loading wait")
    
    def select_filter_values(self, index1, list_type, css, val, index, large_list_pgdn,**kwargs):
        css_obj=self.driver.find_element_by_css_selector("#"+ css  + " img")
        if list_type=='small':
            if kwargs['temp_val'] > 0:
                """Second time call funciton"""
                pass
            else:
                utillity.UtillityMethods.click_on_screen(self, css_obj, 'middle', click_type=0,**kwargs)
            time.sleep(1)
            parent_menu_css=index1+"_" + css + "_x__0" 
            x = self.driver.find_elements_by_css_selector("#dt"+ parent_menu_css + " span[id^='set']")
            menu_list=[]
            for i in range(len(x)):
                lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
                menu_list.append(lineObjbj.group(1))
            position=menu_list.index(val)
            cur_item_id="set" + parent_menu_css + "_" + str(position) + "i_t"
            curr_item_obj=self.driver.find_element_by_id(cur_item_id)
            utillity.UtillityMethods.default_left_click(self, object_locator=curr_item_obj, **kwargs)
            time.sleep(1)
        else:
            scroll_tabletop=self.driver.find_element_by_css_selector("#ITableData"+str(index1))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_tabletop);
#             utillity.UtillityMethods.switch_to_default_content(self, pause=0.2)
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.page_up_key)
            else:
                keyboard.send('page up')
            time.sleep(0.5)
            core_utility.CoreUtillityMethods.left_click(self, css_obj)
            time.sleep(0.5)
            parent_css= "#wall" + str(index+1) + " #wtop" + str(index+1)
            elem_css=parent_css+" "+kwargs['custom_css'] if 'cord_type' in kwargs else parent_css 
            draggable_popup=self.driver.find_element_by_css_selector(elem_css)
            target_loc=core_utility.CoreUtillityMethods.get_web_element_coordinate(self, draggable_popup)
            target_x=int(target_loc['x'])+600
            target_y=int(target_loc['y'])+50
            active_miscelaneous.Active_Miscelaneous.move_active_popup(self,str(index+1), target_x, target_y, pause=5)
            time.sleep(2)
            if large_list_pgdn > 0:
                action = ActionChains(self.driver)
                #Here you implement Action Chanin PG DOWN
                hov_ele=self.driver.find_element_by_css_selector("#wall2 #wbody2 td")                
                #if self.browser=='Firefox':
                if Global_variables.browser_name in ['firefox', 'ie', 'edge']:
                    utillity.UtillityMethods.click_type_using_pyautogui(self, hov_ele, **kwargs)
                else:
                    action.move_to_element(hov_ele).perform()
                for i in range(large_list_pgdn):
                    #if self.browser == 'Firefox':
                    if Global_variables.browser_name in ['firefox', 'ie', 'edge']:
                        pyautogui.press('pagedown')
                    else:
                        action.send_keys(keys.Keys.PAGE_DOWN).perform()
            time.sleep(2)
            val_obj=self.driver.find_element_by_xpath("//div[@id='wall" + str(index+1) + "']//span[normalize-space(text())='" + val + "']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", val_obj);
            val_obj.click()
            scroll_tabletop=self.driver.find_element_by_css_selector("#IWindowBody"+str(index1))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_tabletop);
#             utillity.UtillityMethods.switch_to_default_content(self, pause=0.2)
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.page_up_key)
            else:
                keyboard.send('page up')
            time.sleep(1)
            try:               
                close_btns=self.driver.find_elements_by_css_selector("#wall" + str(index+1) + " #wtop" + str(index+1) + " img")
                utillity.UtillityMethods.default_left_click(self, object_locator=close_btns[1], **kwargs)
            except:
                pass
            time.sleep(1)
        
                    
    def create_filter(self, rownum, condition_name, value_list_type='small', popup_id='wall1', large_list_pgdn=0, table_id='ITableData0', **kwargs):
        """
        :Syntax: create_filter(1, 'Equals', value1='IL')
        :Syntax: create_filter(1, 'Equals', value1='CA',value2='NY', value3='MA')
        :Syntax: create_filter(1, 'Equals', 'large', 'value1'='12345')
        :Syntax: create_filter(1, 'Between','large','wall1',1,value1='700',value2='900')#Pagedown=1
        :Syntax: create_filter(1, 'Not equal',popup_id='wall2',value1="R1019")
        @author = Niranjan 
        """
        index=int(list(popup_id)[-1])
        index1=str(list(table_id)[-1])
        wall_loc=self.driver.find_element_by_css_selector("#wall" + str(index) + " #wtop" + str(index)+" .arWindowBarTitle")
        obj_loc=core_utility.CoreUtillityMethods.get_web_element_coordinate(self, wall_loc)
        if obj_loc['x'] != 50 and obj_loc['y'] != 150:
            active_miscelaneous.Active_Miscelaneous.move_active_popup(self,str(index), str(249), str(209), pause=5)
        elif obj_loc['x'] != 50:
            active_miscelaneous.Active_Miscelaneous.move_active_popup(self,str(index), str(249), '209', pause=5)
        elif obj_loc['y'] != 150:
            active_miscelaneous.Active_Miscelaneous.move_active_popup(self,str(index), '249', str(209), pause=5)
        else:
            pass
#         utillity.UtillityMethods.switch_to_default_content(self, pause=0.2)
        if condition_name != "":
#             menu_css="ft" + str(index) + "_" + str(rownum - 1)
            menu_css="ft" + str(index) + "_" + str(rownum - 1)
            parent_menu_css=index1+"_" + menu_css + "_x__0"
            menu_css_obj=self.driver.find_element_by_css_selector("#"+ menu_css  + " img")
            utillity.UtillityMethods.click_on_screen(self, menu_css_obj, 'middle', click_type=0, **kwargs)
            x = self.driver.find_elements_by_css_selector("#dt"+ parent_menu_css + " span[id^='set']")
            menu_list=[]
            for i in range(len(x)):
                lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
                menu_list.append(lineObjbj.group(1))
            position=menu_list.index(condition_name)
            cur_item_id="set" + parent_menu_css + "_" + str(position) + "i_t"
            cur_item_obj=self.driver.find_element_by_id(cur_item_id)
            utillity.UtillityMethods.click_on_screen(self, cur_item_obj, 'middle', click_type=0, **kwargs)
            time.sleep(1)
        temp_obj=0
        for key in kwargs:
            if condition_name in ['Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']:
                input_css="#fboxi" + str(rownum - 1) + " input"
                input_element = self.driver.find_element_by_css_selector(input_css)
                input_element.clear()
                #if self.browser=='Firefox':
                if Global_variables.browser_name in ['firefox', 'ie', 'edge']:
                    utillity.UtillityMethods.default_click(self, input_element) 
                    if sys.platform == 'linux':
                        pykeyboard.type_string(str(kwargs['value1']))
                        pykeyboard.tap_key(pykeyboard.enter_key)
                    else:
                        keyboard.write(kwargs['value1'])
                        keyboard.send('enter')
                else:  
                    action = ActionChains(self.driver)
                    action.send_keys_to_element(input_element, kwargs['value1']).send_keys(keys.Keys.ENTER).perform()
                time.sleep(1)
            else:
                if condition_name in ['Between', 'Not Between']:
                    button_css1="ftp" + str(index) + "_1_" + str(rownum - 1)
                    button_css2="ftp" + str(index) + "_2_" + str(rownum - 1)
                    if 'x_offset' in kwargs:
                        self.select_filter_values(index1, value_list_type, button_css1, kwargs['value1'], index, large_list_pgdn, temp_val=temp_obj, x_offset=kwargs['x_offset'], y_offset=kwargs['y_offset'])
                        self.select_filter_values(index1, value_list_type, button_css1, kwargs['value2'], index, large_list_pgdn, temp_val=temp_obj, x_offset=kwargs['x_offset'], y_offset=kwargs['y_offset'])
                    else:
                        self.select_filter_values(index1, value_list_type, button_css1, kwargs['value1'], index, large_list_pgdn, temp_val=temp_obj)
                        self.select_filter_values(index1, value_list_type, button_css2, kwargs['value2'], index, large_list_pgdn, temp_val=temp_obj)
                    break
                else:    
#                     button_css1="ftp" + str(index) + "_1_" + str(rownum - 1)
                    button_css1="ftp" + str(index) + "_1_" + str(rownum - 1)
                    if 'x_offset' in kwargs:
                        self.select_filter_values(index1, value_list_type, button_css1, kwargs[key], index, large_list_pgdn,temp_val=temp_obj, x_offset=kwargs['x_offset'], y_offset=kwargs['y_offset'])
                    else:
                        self.select_filter_values(index1, value_list_type, button_css1, kwargs[key], index, large_list_pgdn,temp_val=temp_obj)
            temp_obj=temp_obj+1
                    
                
    def delete_filter(self, rownum):
        """
        :Usage: delete_filter(1)
        @author = Niranjan 
        """
        actual_rownum=rownum+1
        delete_btn_css="#wall1 tr:nth-child(" + str(actual_rownum) + ") div[title='Delete'] img"
        self.driver.find_element_by_css_selector(delete_btn_css).click()
        time.sleep(1)
        
    def close_filter_dialog(self,popup_id='wall1'):
        """
        @author = Niranjan 
        :Usage: close_filter_dialog()
        :Usage: close_filter_dialog(popup_id='wall2')
        """
        index=int(list(popup_id)[-1])
        top_buttons="#"+popup_id+" #wtop"+str(index)+" img"
        close_btns=self.driver.find_elements_by_css_selector(top_buttons)
        utillity.UtillityMethods.click_on_screen(self, close_btns[1], 'middle', click_type=0)
        time.sleep(5)

        
    def filter_button_click(self, btn_name,popup_id='wall1'):
        """
        :Usage: filter_button_click('Add Condition')
        :Usage: filter_button_click('Filter',popup_id="wall2")
        @author = Niranjan 
        """
        
        filter_buttons_css="#"+popup_id+" .arFilterButton"
        filter_buttons=self.driver.find_elements_by_css_selector(filter_buttons_css)
        if (btn_name == 'Operator: AND') or (btn_name == 'Operator: OR'):
            n=0
        if btn_name == 'Add Condition':
            n=1
        if btn_name == 'Filter':
            n=2
        if btn_name == 'Highlight':
            n=3
        if btn_name == 'Clear All':
            n=4
        filter_buttons[n].click()
        time.sleep(8)

            
    def add_condition_field(self, field_name):
        """
        :Usage: filter_button_click('State')
        @author = Niranjan 
        """
        self.filter_button_click('Add Condition')
        parent_menu_css="0_filtop0_0" 
        x = self.driver.find_elements_by_css_selector("#dt"+ parent_menu_css + " span[id^='set']")
        
        menu_list=[]
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            menu_list.append(lineObjbj.group(1))
        print(menu_list)   
        position=menu_list.index(field_name)
        
        cur_item_id="set" + parent_menu_css + "_" + str(position) + "i_t"
        elem=self.driver.find_element_by_id(cur_item_id)
        utillity.UtillityMethods.default_left_click(self, object_locator=elem)
        time.sleep(1)
        
        
    def add_global_condition_field(self, field_name, parent_menu_css=None):
        """
        :Usage: filter_button_click('State')
         
        """
        self.filter_button_click('Add Condition')
        menu_css = parent_menu_css if parent_menu_css != None else "1_globalop_x__0" 
        x = self.driver.find_elements_by_css_selector("#dt"+ menu_css + " span[id^='set']")
        menu_list=[]
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            menu_list.append(lineObjbj.group(1))
        position=menu_list.index(field_name)
        cur_item_id="set"+ menu_css + "_" + str(position) + "i_t"
        elem=self.driver.find_element_by_id(cur_item_id)
        utillity.UtillityMethods.default_left_click(self, object_locator=elem)
        time.sleep(1)
        
        
    def verify_filter_buttons(self, expected_btn_level_text, msg):
        """
        :Usage: verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight','Clear All'], 'Step 10: Veryfy All buttons Present.')
        :Usage: verify_filter_buttons(['Operator: OR', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], 'Step 10: Veryfy All buttons Present.')
        @author = Niranjan 
        """
        filter_buttons_css="#wall1 .arFilterButton"
        filter_buttons=self.driver.find_elements_by_css_selector(filter_buttons_css)        
        actual_btn_level_text=[]
        for i in range(len(filter_buttons)):
            actual_btn_level_text.append(filter_buttons[i].text)
        print(expected_btn_level_text)
        print(actual_btn_level_text)
        utillity.UtillityMethods.asequal(self, expected_btn_level_text, actual_btn_level_text, msg)
        print(actual_btn_level_text)
        
    def check_menu(self, raw_menu_obj_list, expected_menu_list, msg):
        actual_menu_list=[]
        for i in range(len(raw_menu_obj_list)):
            lineObjbj = re.match(r'(\S.*)?.*', raw_menu_obj_list[i].text)
            if lineObjbj.group(1) != None:
                actual_menu_list.append(lineObjbj.group(1))
        utillity.UtillityMethods.asequal(self, expected_menu_list, actual_menu_list, msg)


    def verify_filter_condition_menu_list(self,rownum, msg):

        """
        :Usage: verify_filter_condition_menu_list(1, 'Step 10: Veryfy All buttons Present.')
        :params: rownum starts with 1
        @author = Nasir 
        """
        expected_menu_list = ['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        menu_css="ft1_" + str(rownum - 1)
        self.driver.find_element_by_css_selector("#"+ menu_css  + " img").click()
        parent_menu_css="0_" + menu_css + "_x__0" 
        list_obj = self.driver.find_elements_by_css_selector("#dt"+ parent_menu_css + " span[id^='set']")
        Active_Filter_Selection.check_menu(self, list_obj, expected_menu_list, msg)

    def verify_filter_selection_dialog(self,verify, msg,*args,popup_id='wall1', **kwargs):
        """
        :Usage: verify_filter_selection_dialog(True,'Step 10: Verify filter row.','Unit Sales')
        :Usage: verify_filter_selection_dialog(True,'Step 10: Verify filter row.',['Unit Sales', 'Less than', '15905'])
        :Usage: verify_filter_selection_dialog(False,'Step 10: Verify filter rows.',['Unit Sales', 'Less than', '15905'], ['Product', 'Equals'])
        :Usage: verify_filter_selection_dialog(False,'Step 10: Verify filter rows.','Unit Sales', 'Product')
        :Usage: verify_filter_selection_dialog(True, "Step 04: Expect to see the Filter selection box",['ALPHA Store Code','Not equal'],popup_id="wall2")
        @author = Nasir 
        """
        row_num=kwargs['row_num'] if 'row_num' in kwargs else 2
        for arg in args:
            row_css="#"+popup_id+" tr:nth-child(" + str(row_num) + ")"
            actual_row_list=(self.driver.find_element_by_css_selector(row_css).text).split('\n')
            actual=[el.strip() for el in actual_row_list if bool(re.match('\S',el))]
            if verify == True:
                if isinstance(arg, str):
                    utillity.UtillityMethods.asin(self, arg, actual, msg)
                else:
                    utillity.UtillityMethods.asequal(self, arg, actual, msg)
            else:
                if isinstance(arg, str):
                    utillity.UtillityMethods.as_notin(self, arg, actual, msg)
                else:
                    utillity.UtillityMethods.as_not_equal(self, arg, actual, msg)
            row_num=row_num+1

    def verify_filter_values_menu_list(self, rownum, expected_menu_list, msg):
        """
        :Usage: verify_filter_values_menu_list(1, menu_list, 'Step 10: Veryfy All buttons Present.')
        :params: rownum starts with 1 (which row in Filter Selection, when we add another condition it will 2nd row)
        :params: menu_list = ['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        @author = Nasir 
        """
        menu_css="ftp1_1_" + str(rownum - 1)
        self.driver.find_element_by_css_selector("#"+ menu_css  + " img").click()
        parent_menu_css="0_" + menu_css + "_x__0" 
        list_obj = self.driver.find_elements_by_css_selector("#dt"+ parent_menu_css + " span[id^='set']")
        Active_Filter_Selection.check_menu(self, list_obj, expected_menu_list, msg)

    def verify_value_selection(self, rownum, value_list, msg):
        """
        :Usage: verify_value_selection(1, menu_list, 'Step 10: Veryfy All buttons Present.')
        :params: rownum starts with 1
        :params: value_list = ['C141', 'C142']
        @author = Nasir 
        """
        selected_value_list=[]
        menu_css="ftp1_1_" + str(rownum - 1)
        self.driver.find_element_by_css_selector("#"+ menu_css  + " img").click()
        parent_menu_css="0_" + menu_css + "_x__0" 
        x = self.driver.find_elements_by_css_selector("#dt"+ parent_menu_css + " span[id^='set']")
        for menu_item in value_list:
            for i in range(len(x)):
                item_css=parent_menu_css + "_" + str(i)
                lineObjbj = self.driver.find_element_by_css_selector("#set"+ item_css + "i_t").text
                if lineObjbj == menu_item:
                    item_row = self.driver.find_element_by_css_selector("#t"+ item_css).text
                    match_obj=re.match(r'(.)\s+(.*)', item_row)
                    if ord(match_obj.group(1))==8730 or ord(match_obj.group(1))==214:
                        selected_value_list.append(match_obj.group(2).strip())
                    break
                else:
                    pass
        utillity.UtillityMethods.asequal(self, value_list, selected_value_list, msg)

    def verify_add_condition_menu(self, expected_menu_list, msg):

        """
        :Usage: verify_add_condition_menu('State')
        @author = Niranjan 
        """
        self.filter_button_click('Add Condition')
        parent_menu_css="0_filtop0_0" 
        x = self.driver.find_elements_by_css_selector("#dt"+ parent_menu_css + " span[id^='set']")
        actual_menu_list=[]
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            actual_menu_list.append(lineObjbj.group(1))
        utillity.UtillityMethods.asequal(self, expected_menu_list, actual_menu_list, msg)
    
    def verify_visibility_of_filter_popup(self,visibility,msg):
        """
        :Usage: verify_visibility_of_filter_popup(False,'Step 06:  Verify filter options are wiped out from the pop up')
        @author: Sindhuja
        """
        if visibility==True:
            pop_up=self.driver.find_element_by_css_selector("#wall1").is_displayed()
            utillity.UtillityMethods.asequal(self,True,pop_up,msg)
        else:
            pop_up=False
            utillity.UtillityMethods.asequal(self,False,pop_up,msg)