from common.lib import utillity
from common.lib.base import BasePage
from common.locators.visualization_metadata_locators import VisualizationMetadataLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import re
import time
import pyautogui


class Active_Pivot_Comment(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Pivot_Comment, self).__init__(driver)

    def _validate_page(self, driver):
        print("Implement Page Loading wait")
    
    def create_comment(self, popup_id, *args):
        """
        Usage: create_comment('wall1', 'This is a Comment')
        """        
        text_area_css="#" + popup_id + " textarea"
        text_area_elem=self.driver.find_element_by_css_selector(text_area_css)
        text_area_elem.click()
        time.sleep(1)
        for arg in args:
            action = ActionChains(self.driver)
            action.send_keys_to_element(text_area_elem, arg).perform()
            del action
            time.sleep(1)
            pyautogui.press('enter', pause=1)
        add_btn_css="#" + popup_id + " .arPromptButton"
        self.driver.find_element_by_css_selector(add_btn_css).click()
    
    
    def delete_comment(self, popup_id, rownum):
        delete_btn_css="#" + popup_id + " #PromptTable1 tr:nth-child(" + rownum + ") > td:nth-child(1) div[title='Delete'] img"
        self.driver.find_element_by_css_selector(delete_btn_css)
        time.sleep(1)
    
    def verify_comment(self, popup_id, rownum, expected_comment, msg):
        """
        Usage: verify_comment('wall1', '1', 'Comment on last WA State row.', 'Step 07: Expect to see the text entered in step 5')
        Author: Niranjan
        """
        comment_date_css="#" + popup_id + " #PromptTable1 tr:nth-child(" + str(rownum) + ") > td.arCommentDate"
        comment_text_css="#" + popup_id + " #PromptTable1 tr:nth-child(" + str(rownum) + ") > td.arCommentText"
        ob=re.match(r'(\d+)/(\d+)/(\d+).*', self.driver.find_element_by_css_selector(comment_date_css).text)
        actual_date=ob.group(1) + "/" + ob.group(2) + "/" + ob.group(3)
        day=time.strftime("%d") if int(time.strftime("%d")) > 9 else list(time.strftime("%d"))[-1]
        month=time.strftime("%m") if int(time.strftime("%m")) > 9 else list(time.strftime("%m"))[-1]
        year=time.strftime("%Y")
        expected_date=month + "/" + day + "/" + year
        utillity.UtillityMethods.asequal(self, expected_date, actual_date, msg + " Comment date verification.")
        actual_commnet=self.driver.find_element_by_css_selector(comment_text_css).text
        utillity.UtillityMethods.asequal(self, expected_comment, actual_commnet, msg + " Comment string verification.")
    
    def close_comment_dialog(self):
        """
        @author = Niranjan 
        """
        top_buttons="#wall1 #wtop1 img"
        close_btns=self.driver.find_elements_by_css_selector(top_buttons)
        close_btns[1].click()
        time.sleep(1)
        
    def click_pivot_menu_bar_items(self, popup_id, item_index):
        """
        Syntax: click_pivot_menu_bar_items('wall1', 2)
        @author = Niranjan 
        """
        menu_items_css="#" + popup_id + " .arPivotMenuBar img"
        menu_items=self.driver.find_elements_by_css_selector(menu_items_css)
        menu_items[item_index].click()
        time.sleep(1)
        
    def create_new_item(self, popup_id, popup_instance, item_list,**kwargs):
        """
        Syntax: create_new_item('wall1', 0, 'Restore Original')
        Syntax: create_new_item('wall1', 1, 'Add (Y)->Product')
        item_list = 'Add (Y)->Product'/'Restore Original'/'New'
        Params: popup_instance :- If you are invoking this function freshly then use 0, else nonzero.
        @author = Niranjan
        """
        op_list=item_list.split('->')
        index=list(popup_id)[-1]
        if popup_instance==0:
            new_parent="0_cpop" + index + "_x__0"
            group_by_parent=new_parent + "_1"
            add_parent=new_parent + "_2"
        else:
            new_parent="0_cpop" + index + "_0"
            group_by_parent=new_parent + "_1"
            add_parent=new_parent + "_2"
        self.click_pivot_menu_bar_items(popup_id, 0)
        menus=self.driver.find_elements_by_css_selector("#dt" + new_parent + "  > table > tbody > tr")
        
        for i in range(len(menus)):
            set_item="set" + new_parent + "_" + str(i) + "i_t"
            if self.driver.find_element_by_id(set_item).text == op_list[0]:
                set_item_obj=self.driver.find_element_by_id(set_item)
                utillity.UtillityMethods.default_left_click(self,object_locator=set_item_obj,**kwargs)
                break
        
        if op_list[0]=='Group By (X)':
            menus=self.driver.find_elements_by_css_selector("#dt" + group_by_parent + " span[id^='set']")
            if self.browser=='Firefox' :
                utillity.UtillityMethods.click_type_using_pyautogui(self, menus[0], **kwargs)
            else :
                hov1 = ActionChains(self.driver)
                hov1.move_to_element(menus[0]).perform()
                del hov1
            menu_list=[]
            for i in range(len(menus)):
                lineObjbj = re.match(r'(\S.*)?.*', menus[i].text)
                menu_list.append(lineObjbj.group(1))
            position=menu_list.index(op_list[1])
            cur_item_id="set" + group_by_parent + "_" + str(position) + "i_t"
            cur_item_id_obj=self.driver.find_element_by_id(cur_item_id)
            utillity.UtillityMethods.default_left_click(self,object_locator=cur_item_id_obj,**kwargs)
            time.sleep(2)
        
        if op_list[0]=='Add (Y)':
            menus=self.driver.find_elements_by_css_selector("#dt" + add_parent + " span[id^='set']")
            if self.browser=='Firefox' :
                utillity.UtillityMethods.click_type_using_pyautogui(self, menus[0], **kwargs)
            else :
                hov1 = ActionChains(self.driver)
                hov1.move_to_element(menus[0]).perform()
                del hov1
            menu_list=[]
            for i in range(len(menus)):
                lineObjbj = re.match(r'(\S.*)?.*', menus[i].text)
                menu_list.append(lineObjbj.group(1))
            position=menu_list.index(op_list[1])
            cur_item_id="set" + add_parent + "_" + str(position) + "i_t"
            cur_item_id_obj=self.driver.find_element_by_id(cur_item_id)
            utillity.UtillityMethods.default_left_click(self,object_locator=cur_item_id_obj,**kwargs)
            time.sleep(2)
        
    def select_aggregate_function(self, popup_id, popup_instance, function_name, verify=True, **kwargs):
        """
        Syntax: select_aggregate_function('wall1', 0, 'Avg')
        Syntax: select_aggregate_function('wall1', 1, 'Avg')
        Params: popup_instance :- If you are invoking this function freshly then use 0, else nonzero.
        @author = Niranjan 
        """
        index=list(popup_id)[-1]
        self.click_pivot_menu_bar_items(popup_id, 2)
        function_list=[]
        if popup_instance==0:
            parent_css="0_SUM_" + index + "_x__0"
        else:
            parent_css="0_SUM_" + index + "_0"
        x=self.driver.find_elements_by_css_selector("#dt" + parent_css + " span[id ^='set']")
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            function_list.append(lineObjbj.group(1))
        position=function_list.index(function_name)
        cur_item_id="set" + parent_css + "_" + str(position) + "i_t"
        elem=self.driver.find_element_by_id(cur_item_id)
        utillity.UtillityMethods.default_left_click(self,object_locator=elem,**kwargs)
        time.sleep(1)
        selected_function_css="#" + popup_id + " .arPivotMenuBar #SUM_" + index
        actual_function_name=self.driver.find_element_by_css_selector(selected_function_css).text
        if verify==True:
            utillity.UtillityMethods.asequal(self, function_name, actual_function_name, "Step X: Verify " + function_name + " is displaying now.")
        else:
            utillity.UtillityMethods.as_not_equal(self, function_name, actual_function_name, "Step X: Verify " + function_name + " is not displaying.")


    
    def veryfy_pivot_table_title(self, pivot_id, expected_title, msg):
        """
        Syntax: veryfy_pivot_table_title('piv1', 'StateBYCategory,ProductID', 'Step 10: Veryfy filter row.')
        @author = Niranjan 
        """
        pivot_title_table= "#" + pivot_id + " > tbody > tr:nth-child(1) > td > table > tbody"
        actual_title=self.driver.find_element_by_css_selector(pivot_title_table).text
        actual_title=re.sub(r'\s*', '', actual_title)
        utillity.UtillityMethods.asequal(self, expected_title, actual_title, msg)
        
    def click_groupby_across_button(self, pivot_id, rownum, colnum, btn_index):
        """
        Syntax: click_groupby_across_button('piv1', 2, 1, 1)
        params: rownum starts with 1
        params: colnum starts with 1
        params: btn_index can be among 1, 2, 3, 4.
        @author = Niranjan 
        """
        pivot_data_table= "#" + pivot_id + " > tbody > tr:nth-child(2) > td > table > tbody"
        groupby_across_field=pivot_data_table + " > tr:nth-child(" + str(rownum) + ") > td:nth-child(" + str(colnum) + ") > table[class=arPivotColumnHeading]"
        btn_css=groupby_across_field + " img"
        buttons=self.driver.find_elements_by_css_selector(btn_css)
        buttons[btn_index-1].click()
        time.sleep(1)
        
    def verify_pivot_menu(self,popup_id,msg):
        """
        params: popup_id: wall1
        Syntax: verify_pivot_menu('wall2', 'Step 04: Verify pivot toolbar')
        @author: Sindhuja
        """
        index=list(popup_id)[-1]
        popup="#"+popup_id+" .arPivotMenuBarContainer div[id]"
        menu="['cpop" + str(index) + "', 'LINKIMG" +  str(index) + "_-1', 'SUM_" +  str(index) + "']"
        values=[]
        val = self.driver.find_elements(By.CSS_SELECTOR, popup)
        for i in range(len(val)):
            values.append(val[i].get_attribute('id'))
        utillity.UtillityMethods.asequal(self, str(values), menu, msg)

    

        