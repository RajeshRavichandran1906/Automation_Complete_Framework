from common.lib import utillity
from common.lib.base import BasePage
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import re
import time,os,pyautogui
from common.locators import active_miscelaneous_locators
import colorsys
from selenium.webdriver.support.color import Color

class Active_Miscelaneous(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Miscelaneous, self).__init__(driver)

    def _validate_page(self, driver):
        print("Implement Page Loading wait")
    
    def select_menu_items(self, table_id, column_no, column_name, *args, **kwargs):
        '''
        Syntax: select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)','Product Category', 'MSRP')
        Author: Niranjan
        '''
        index=list(table_id)[-1]
        main_menu_id=""+str(index)+"_" + str(column_no) + "_0"
        menu_btn_css="#" + table_id + " #popid" + str(index) + "_" + str(column_no) + " img"
        parent="#dt" + main_menu_id
        menu_btn_click=self.driver.find_element_by_css_selector("#" + table_id + " #TCOL_" + str(index) + "_C_" + str(column_no))
        utillity.UtillityMethods.default_left_click(self,object_locator=menu_btn_click, **kwargs)
        menu_btn=self.driver.find_element_by_css_selector(menu_btn_css)
        utillity.UtillityMethods.default_left_click(self,object_locator=menu_btn, **kwargs)
        time.sleep(3)
        x = self.driver.find_elements_by_css_selector("#dt"+ main_menu_id + ">table>tbody>tr")
        for i in range(len(x)):
            item_css="set" + main_menu_id + "_" + str(i)
            lineObjbj = self.driver.find_element_by_css_selector("#"+ item_css + "i_t").text
            if lineObjbj == column_name:
                if column_name == 'Show Columns':
                    hov_elem1 = self.driver.find_element_by_css_selector("#"+ item_css + "i_t")
                    if self.browser=='Firefox':
                        utillity.UtillityMethods.click_type_using_pyautogui(self, hov_elem1, **kwargs)
                    else:
                        hov1 = ActionChains(self.driver)
                        hov1.move_to_element(hov_elem1).perform()
                else:
                    item=self.driver.find_element_by_css_selector("#"+ item_css + "i_t")
                    utillity.UtillityMethods.default_left_click(self,object_locator=item, **kwargs)
                break
            else:
                pass
        time.sleep(1)
        for arg in args:
            parent= parent + "_" + str(i)
            css=parent + ">table>tbody>tr"
            hov_elem = self.driver.find_element_by_css_selector(css)
            if self.browser=='Firefox':                 
                utillity.UtillityMethods.click_type_using_pyautogui(self, hov_elem, **kwargs)                 
            else:
                hov = ActionChains(self.driver)
                hov.move_to_element(hov_elem).perform()
                del hov
            x = self.driver.find_elements_by_css_selector(css)             
            for i in range(len(x)):
                sub_item_css=item_css + "_" + str(i)
                lineObjbj = self.driver.find_element_by_css_selector("#"+ sub_item_css + "i_t").text
                if lineObjbj == arg:
                    sub_item=self.driver.find_element_by_css_selector("#"+ sub_item_css + "i_t")
                    utillity.UtillityMethods.default_left_click(self,object_locator=sub_item, **kwargs)
                    break
                else:
                    pass                 
            item_css=sub_item_css     
        time.sleep(5)
 
    
    def verify_page_summary(self, page_num, expected_title, msg):
        '''
        Syntax: verify_page_summary(0,'107of107records,Page1of2', 'Step 05: Verify Title')
        Syntax: verify_report_summary(0, 'SUB/TOT\n1of107records,Page1of1', 'Step 04: Verify Pagination shows: SUB/TOT')
        Author: Niranjan
        '''
        get_title=self.driver.find_element_by_css_selector("table[id='IWindowBody" + str(page_num) + "'] .arGridBar table>tbody").text.strip()
        actual_title=re.sub('\s', '', get_title)
        utillity.UtillityMethods.asin(self,expected_title, actual_title, msg)

        
    def verify_pagination_textbox(self, value, msg):
        '''
        Syntax: verify_pagination_textbox('3', 'Step 05: Verify Textbox value')
        Author: Niranjan
        '''
        btn_css="table .arGridBar span[title='Goto Page']"
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(1)
        text_box = "//input[@id='formgoto']"
        try:
            actual_status=self.driver.find_element_by_xpath(text_box).is_displayed()
            utillity.UtillityMethods.asequal(self,True, actual_status, msg)
            text = self.driver.find_element_by_xpath(text_box).get_attribute('value')
            utillity.UtillityMethods.asequal(self,value, text, msg)            
        except:
            actual_status='False'
            utillity.UtillityMethods.asequal(self,True, actual_status, msg)
        
    def navigate_page(self, navigate_type, *args):
        '''
        Syntax: navigate_page('goto_page', 2)
        Syntax: navigate_page('next_page')
        Syntax: navigate_page('last_page')
        Syntax: navigate_page('previous_page')
        Syntax: navigate_page('first_page')
        Author: Niranjan
        '''
        if navigate_type == 'goto_page':
            btn_css="table .arGridBar span[title='Goto Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
            page_no=self.driver.find_element_by_id("formgoto")
            page_no.clear()
            page_no.send_keys(args[0])
            page_no.send_keys(keys.Keys.ENTER)
            time.sleep(1)
        if navigate_type == 'next_page':
            btn_css="table .arGridBar span[title='Next Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
        if navigate_type == 'last_page':
            btn_css="table .arGridBar span[title='Last Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
        if navigate_type == 'previous_page':
            btn_css="table .arGridBar span[title='Previous Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
        if navigate_type == 'first_page':
            btn_css="table .arGridBar span[title='First Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
        
    def verify_navigate_page(self, navigate_type, msg):
        '''
        Syntax: verify_navigate_page('goto_page', Step 02: Verify goto Page double arrow displayed")
        Syntax: verify_navigate_page('next_page',"Step 02: Verify Last Page double arrow displayed")
        Syntax: verify_navigate_page('last_page',"Step 02: Verify Last Page double arrow displayed")
        Syntax: verify_navigate_page('previous_page',"Step 02: Verify Last Page double arrow displayed")
        Syntax: verify_navigate_page('first_page',"Step 02: Verify Last Page double arrow displayed")
        Author: Niranjan
        '''
        if navigate_type == 'goto_page':
            btn_css="table .arGridBar span[title='Goto Page']"
            try:
                img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            except:
                img_status='False'
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'next_page':
            btn_css="table .arGridBar span[title='Next Page']"
            try:
                img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            except:
                img_status='False'
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'last_page':
            btn_css="table .arGridBar span[title='Last Page']"
            try:
                img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            except:
                img_status='False'
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'previous_page':
            btn_css="table .arGridBar span[title='Previous Page']"
            try:
                img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            except:
                img_status='False'
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'first_page':
            btn_css="table .arGridBar span[title='First Page']"
            try:
                img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            except:
                img_status='False'
                utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)

        
    
    def verify_highlighted_rows(self, table_id, expected_count, msg):
        '''
        Syntax: verify_highlighted_rows('ITableData0', 7, 'Step 05: Verify Title')
        Author: Niranjan
        '''
        rows_css="#" + table_id + " tr[style*='rgb']"
        actual_count=len(self.driver.find_elements_by_css_selector(rows_css))
        utillity.UtillityMethods.asequal(self,expected_count, actual_count, msg)
        
    def select_field_menu_items(self, table_id, rownum, colnum, field_val,**kwargs):
        '''
        :param:field_list='CIOS->By Region->By Date->Year to date'
            or
        :param:field_list='CIOS'
        :Usage: select_field_menu_items('ITableData0', 0, 2, 'CIOS->By Region->By Date->Year to date')
                OR
        Syntax: select_field_menu_items('ITableData0', 0, 0,'Comments')
        select_field_menu_items('ITableData0', 0, 0,'Highlight Row',original_rownum=0)
        params: rownum and colnum start with 0,0.
        Author: Niranjan
        '''
        index=list(table_id)[-1]
        menu_btn_click=self.driver.find_element_by_css_selector("#" + table_id + " #TCOL_" + str(index) + "_C_" + str(colnum))
        utillity.UtillityMethods.default_left_click(self,object_locator=menu_btn_click, **kwargs)
        time.sleep(1)
        field_list=field_val.split('->')
        field_css="#" + table_id + " tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "']"
        elem = self.driver.find_element_by_css_selector(field_css)
        utillity.UtillityMethods.default_left_click(self,object_locator=elem, **kwargs)
        time.sleep(1)
        if 'original_rownum' in kwargs:
            rownum=kwargs['original_rownum']
        temp=0
        increment=0
        add=''
        menu_items_css="div[id^='dt0_I0r" + str(rownum) + "'][style*='block']"
        for arg in field_list: 
            x = self.driver.find_elements_by_css_selector(menu_items_css+" span[id^='set']")
            for i in range(len(x)):
                if increment > 2:
                    hover_item_css="div[id^='dt0_I0r" + str(rownum) + "'][id$='"+str(temp)+""+add+"'][style*='block'] table tbody>tr"
                else:   
                    hover_item_css="div[id^='dt0_I0r" + str(rownum) + "'][id$='"+str(temp)+"'][style*='block'] table tbody>tr"
                hover_item=self.driver.find_element_by_css_selector(hover_item_css)
                time.sleep(1)
                if self.browser=='Firefox':
                    utillity.UtillityMethods.click_type_using_pyautogui(self, hover_item, **kwargs)
                else:
                    ActionChains(self.driver).move_to_element(hover_item).perform()
                time.sleep(1)
                lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
                if lineObjbj.group(1) == arg:
                    temp=i
                    increment+=1 
                    if self.browser=='Firefox':
                        utillity.UtillityMethods.click_type_using_pyautogui(self, x[i], **kwargs)
                    else:
                        ActionChains(self.driver).move_to_element(x[i]).perform()
                    time.sleep(2)
                if lineObjbj.group(1) == arg and arg == field_list[-1]:
                    x[i].click()
                    break
            if increment > 2:
                add +='_1'
                menu_items_css="div[id^='dt0_I0r" + str(rownum) + "'][id$='"+str(temp)+""+add+"'][style*='block']"
            else:
                menu_items_css="div[id^='dt0_I0r" + str(rownum) + "'][id$='"+str(temp)+"'][style*='block']"
            time.sleep(1)
    
    def select_field_menu_items_using_pyautogui(self, table_id, rownum, colnum, field_val,**kwargs):
        '''
        Syntax: select_field_menu_items('ITableData0', 0, 0,'Comments')
        select_field_menu_items('ITableData0', 0, 0,'Highlight Row',original_rownum=0)
        params: rownum and colnum start with 0,0.
        Author: Niranjan
        '''
        field_css="#" + table_id + " tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "']"
        elem = self.driver.find_element_by_css_selector(field_css)
        utillity.UtillityMethods.default_left_click(self,object_locator=elem, **kwargs)
        time.sleep(2)
        if 'original_rownum' in kwargs:
            rownum=kwargs['original_rownum']
        menu_items_css="div[id^='dt0_I0r" + str(rownum) + "'][style*='block'] span[id^='set']"
        x = self.driver.find_elements_by_css_selector(menu_items_css)
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            if lineObjbj.group(1) == field_val:
                utillity.UtillityMethods.click_type_using_pyautogui(self, x[i], leftClick=True, **kwargs)
                time.sleep(2)
                break
            else:
                pass
            
    def hover_field_menu_items_using_pyautogui(self, table_id, rownum, colnum, field_val,**kwargs):
        '''
        Syntax: hover_field_menu_items_using_pyautogui('ITableData0', 0, 0,'Comments')
        hover_field_menu_items_using_pyautogui('ITableData0', 0, 0,'Highlight Row',original_rownum=0)
        params: rownum and colnum start with 0,0.
        Author: Niranjan
        '''
        field_css="#" + table_id + " tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "']"
        elem = self.driver.find_element_by_css_selector(field_css)
        utillity.UtillityMethods.default_left_click(self,object_locator=elem, **kwargs)
        time.sleep(2)
        if 'original_rownum' in kwargs:
            rownum=kwargs['original_rownum']
        menu_items_css="div[id^='dt0_I0r" + str(rownum) + "'][style*='block'] span[id^='set']"
        x = self.driver.find_elements_by_css_selector(menu_items_css)
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            if lineObjbj.group(1) == field_val:
                utillity.UtillityMethods.click_type_using_pyautogui(self, x[i], **kwargs)
                time.sleep(2)
                break
            else:
                pass
            
    def verify_field_menu_items(self, table_id, rownum, colnum,expected_value,msg,**kwargs):
        """
        Usage:values = ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 106, 3,values,'Step 03: Verify Active row options')
        Author: Sindhuja
        """
        field_css="#" + table_id + " tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "']"
        field=self.driver.find_element_by_css_selector(field_css)
        utillity.UtillityMethods.default_left_click(self,object_locator=field, **kwargs)
        time.sleep(2)
        menus=self.driver.find_elements_by_css_selector("div[id^='dt0_I0r'][style*='block']")
        x = menus[-1].find_elements_by_css_selector("span[id^='set0_I0r']")
        actual_value=[el.text for el in x if el.text != '']
        utillity.UtillityMethods.asequal(self, expected_value, actual_value, msg)
    
    
    def navigate_coordinate_report_page(self,page_num):
        '''
        Syntax: navigate_tab_report_page("2")
        params: page_num -> Page number -> 1,2,3
        Author: Sindhuja
        '''
        page="[id='iLay$"+page_num+"']"
        self.driver.find_element_by_css_selector(page).click()
        
    def verify_comment_field(self, table_id, rownum, colnum, expected_field_val, msg):
        '''
        Syntax: verify_comment_field('ITableData0', 0, 0,'ENGLAND', 'Step 05: Verify Comment is added')
        params: rownum and colnum start with 0,0.
        Author: Niranjan
        '''
        field_css="#" + table_id + " tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "'] div.arGridComment"
        img_css=field_css + " img"
        expected_background_color=utillity.UtillityMethods.color_picker(self,'comment', 'rgba')
        actual_field_val=self.driver.find_element_by_css_selector(field_css).text
        utillity.UtillityMethods.asequal(self,expected_field_val, actual_field_val, msg+" for the "+actual_field_val+" field. ")
        actual_background_color=self.driver.find_element_by_css_selector(field_css).value_of_css_property('background-color')
        reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', actual_background_color)
        bg_color=reobj.group(1)
        utillity.UtillityMethods.asin(self, bg_color, expected_background_color , msg+" - background color")
        try:
            img_status=self.driver.find_element_by_css_selector(img_css).is_displayed()
            utillity.UtillityMethods.asequal(self,True, img_status, msg+" - image")
        except:
            img_status='False'
            utillity.UtillityMethods.asequal(self,True, img_status, msg)

    def verify_move_to_bottom(self,position, msg):
        """
        Syntax: verify_move_to_bottom('Bottom', 'Step 05: Verify Move to Top displayed')
        Syntax: verify_move_to_bottom('Top', 'Step 05: Verify Move to Bottom displayed')
        Author: Niranjan
        """
        if position=='Top':
            btn_css="table[id='IWindowBody0'] .arGridBar span[title='Move to Bottom'] img"
        else:
            btn_css="table[id='IWindowBody0'] .arGridBar span[title='Move to Top'] img"
        try:
            img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
            utillity.UtillityMethods.asequal(self,True, img_status, msg)
        except:
            img_status='False'
            utillity.UtillityMethods.asequal(self,True, img_status, msg)
            
    def verify_page_scroll(self,main_body_ID,scroll,msg):
        '''
        Syntax: verify_page_scroll("0", "no", "Step 02: Expect to see no scroll bars on Page 1.")
        verify_page_scroll("1", "yes", "Step 03: Expect to see both upward and downward arrows on the scroll bar.")
        params: main_body_ID -> 0, 1 
        Author: Sindhuja & Gobinath
        '''
        doc = "[id='MAINTABLE_wbodyMain"+main_body_ID+"']"
        doc_heigt = self.driver.find_element_by_css_selector(doc).value_of_css_property('height')[:-2]
        doc_heigt_int = int(doc_heigt)
        client = self.driver.execute_script("return document.documentElement.clientHeight;")
        if scroll=='yes':
            utillity.UtillityMethods.as_GE(self,doc_heigt_int,client,msg)
        if scroll=='no':
            utillity.UtillityMethods.as_LE(self,doc_heigt_int,client,msg)
            
    def verify_calculated_value(self, rownum, colnum, expected_text,verify, msg, table_id='ITableData0'):
        '''
        Syntax: verify_calculated_value(2, 6, "Total Sum 46,156,290",True, "Step 02: Verify Total Sum - TOT displayed on pagination bar", table_id='ITableData0')
        verify_calculated_value(2, 6, "Total Sum 46,156,290", False,"Step 02: Verify Total Sum - TOT not displayed on pagination bar", table_id='ITableData1')
        params: rownum = 2, colnum = 6 (starts from 1) 
        Author: Niranjan
        '''
        text_css="#" + table_id + " tr:nth-child(" + str(rownum) + ") > td:nth-child(" + str(colnum) + ")"   
        actual_text=self.driver.find_element_by_css_selector(text_css).text 
        print(actual_text)
        if verify == True:
            utillity.UtillityMethods.asequal(self, expected_text, actual_text, msg)
        else:
            utillity.UtillityMethods.as_not_equal(self, expected_text, actual_text, msg)
        
    def check_menu(self, raw_menu_list, expected_menu_list, all_items, msg):
        actual_menu_list=[]
        for i in range(len(raw_menu_list)):
            lineObjbj = re.match(r'(\S.*)?.*', raw_menu_list[i].text)
            if lineObjbj.group(1) != None:
                actual_menu_list.append(lineObjbj.group(1))
        if all_items == 'yes':
            utillity.UtillityMethods.asequal(self, expected_menu_list, actual_menu_list, msg)
        else:
            utillity.UtillityMethods.asin(self, expected_menu_list, actual_menu_list, msg)

    def verify_menu_items(self, table_id, colnum, navigate_pattern, expected_menu_list, msg, all_items='yes', **kwargs):

        '''
        Syntax: select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)->Product Category')
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        verify_menu_items('ITableData0',3,'Filter',option,'Step 02: Verify Filter menu')
        option='Group By (X)(COU)'
        miscelanousobj.verify_menu_items('ITableData0', 4, "Rollup",option,"Step 02: Expect to see Group by (X)(COU) which indicates a Count value will be produced.",all_items='no')
        column: starts from '0'
        Author: Niranjan
        '''
        index=list(table_id)[-1]
        main_menu_id="0_" + str(colnum) + "_0"
        menu_btn_css="#" + table_id + " #popid0_" + str(colnum) + " img"
        parent="#dt" + main_menu_id
        menu_btn_obj=self.driver.find_element_by_css_selector(menu_btn_css)
        menu_btn_click=self.driver.find_element_by_css_selector("#" + table_id + " #TCOL_" + str(index) + "_C_" + str(colnum))
        utillity.UtillityMethods.default_left_click(self,object_locator=menu_btn_click, **kwargs)
        utillity.UtillityMethods.default_left_click(self,object_locator=menu_btn_obj, **kwargs)
        time.sleep(2)
        if navigate_pattern == None:
            list_obj = self.driver.find_elements_by_css_selector("#dt"+ main_menu_id + " span[id^='set']")
            self.check_menu(list_obj, expected_menu_list, all_items, msg)
        else:
            navigate_list=navigate_pattern.split('->')
            x = self.driver.find_elements_by_css_selector("#dt"+ main_menu_id + ">table>tbody>tr")
            for i in range(len(x)):
                item_css="set" + main_menu_id + "_" + str(i)
                lineObjbj = self.driver.find_element_by_css_selector("#"+ item_css + "i_t").text
                if lineObjbj == navigate_list[0]:
                    if navigate_list[0] == 'Show Columns':
                        hov_elem1 = self.driver.find_element_by_css_selector("#"+ item_css + "i_t")
                        if self.browser=='Firefox':
                            utillity.UtillityMethods.click_type_using_pyautogui(self, hov_elem1, **kwargs)
                        else:
                            hov1 = ActionChains(self.driver)
                            hov1.move_to_element(hov_elem1).perform()
                            del hov1
                    else:
                        menu_item_css=self.driver.find_element_by_css_selector("#"+ item_css + "i_t")
                        utillity.UtillityMethods.default_left_click(self,object_locator=menu_item_css, **kwargs)
                    break
                else:
                    pass
            for arg in navigate_list[1:]:
                parent= parent + "_" + str(i)
                css=parent + ">table>tbody>tr"
                hov_elem = self.driver.find_element_by_css_selector(css)
                if self.browser=='Firefox':                 
                    utillity.UtillityMethods.click_type_using_pyautogui(self, hov_elem, **kwargs)                 
                else:
                    ActionChains(self.driver).move_to_element(hov_elem).perform()
                x = self.driver.find_elements_by_css_selector(css)
                for i in range(len(x)):
                    sub_item_css=item_css + "_" + str(i)
                    lineObjbj = self.driver.find_element_by_css_selector("#"+ sub_item_css + "i_t").text
                    if lineObjbj == arg:
                        menu_sub_item=self.driver.find_element_by_css_selector("#"+ sub_item_css + "i_t")
                        utillity.UtillityMethods.default_left_click(self,object_locator=menu_sub_item, **kwargs)
                        break
                    else:
                        pass
                item_css=sub_item_css 
            list_obj = self.driver.find_elements_by_css_selector(parent + "_" + str(i) + " span[id^='set']") 
            self.check_menu(list_obj, expected_menu_list,all_items, msg)    
 

    def move_active_popup(self, index, x, y, **kwargs):
        """
        Syntax:  miscelanousobj.move_active_popup("1", "600", "200")
        Author: Niranjan
        """
        parent_css= "#wall" + str(index) + " #wtop" + str(index)
        elem_css=parent_css+" "+kwargs['custom_css'] if 'cord_type' in kwargs else parent_css 
        draggable_popup=self.driver.find_element_by_css_selector(elem_css)
        if self.browser == 'Firefox':
            utillity.UtillityMethods.mouse_action_using_pyautogui(self, draggable_popup, mouse_down=True, **kwargs)
            time.sleep(2)
            utillity.UtillityMethods.mouse_action_using_pyautogui(self, draggable_popup, int(x), int(y), mouse_up=True, **kwargs)
        else:
            ActionChains(self.driver).drag_and_drop_by_offset(draggable_popup, int(x), int(y)).perform()


    def verify_summation(self,msg):
        """
        Usage: verify_summation("Step 03: Verify summation")
        Author: Sindhuja
        """
        try:
            img =self.driver.find_element(*ActiveMiscelaneousLocators.summation).is_displayed()
            utillity.UtillityMethods.asequal(self,True,img,msg)
        except:
            img = False
            utillity.UtillityMethods.asequal(self,True,img,msg)
            
    def verify_column_heading(self, table_id, expected_list, msg):

        """
        Params: table_id='ITableData0'
        Params: column=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        Syntax: verify_column_heading(table_id, expected_list,'Step 02: Verify column heading')
        Author: Sindhuja
        """
        column_heading_css = "#" + table_id + " .arGridColumnHeading > td"
        columns=self.driver.find_elements_by_css_selector(column_heading_css)
        actual_list=[re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in columns]]
        utillity.UtillityMethods.asequal(self, expected_list, actual_list, msg)
            
    def verify_field_color(self,class_name,text_color,expected_no_of_items,msg):
        """
        Usage: verify_field_color("IBIS0_1", "green", 57, "Step 02: Verify % of Total field color")
        class_name: IBIS0_1
        text_color: green or black
        expected_no_of_items: field count
        Author: Niranjan
        """
        expected_color_code=utillity.UtillityMethods.color_picker(self, text_color, 'rgba')
        '''Verify Text Color'''
        actual_color = self.driver.find_element_by_css_selector("[class='"+class_name+"']").value_of_css_property('color')
        reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', actual_color)
        bg_color=reobj.group(1)
        utillity.UtillityMethods.asin(self, bg_color, expected_color_code , msg+" - color")
        '''Verify Number of Items'''
        expected_item=self.driver.find_elements_by_css_selector("[class='"+class_name+"']")
        items = len(expected_item)
        utillity.UtillityMethods.asequal(self, items, expected_no_of_items, msg)
        
    def verify_visualization(self, table_id, tr_id, colnum, color_code, msg, **kwargs):
        '''
        Syntax: verify_visualization('ITableData0', 'I0r', 5, 'green', 'Step 05: Verify visualization added')
        column number starts with 0
        '''
        expected_color_code=utillity.UtillityMethods.color_picker(self,color_code, 'rgba')
        occurence = 0
        if 'desired_no_of_rows' in kwargs:
            total_rows=int(kwargs['desired_no_of_rows'])
            print(total_rows)
        else:
            actual_no_of_rows=self.driver.find_elements_by_css_selector("[id='{0}'] tr[id ^='{1}']".format(table_id, tr_id))
            total_rows=len(actual_no_of_rows)
        for i in range(0, total_rows):
            actual_color_code=self.driver.find_element_by_css_selector("[id=" + table_id + "] tr[id ^= '" + tr_id + str(i) +"'] > td:nth-child(" + str(colnum+2) + ") > table table td").value_of_css_property('background-color')
            reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', actual_color_code)
            bg_color=reobj.group(1)
            if bg_color in expected_color_code:
                occurence = occurence + 1 
            else:
                break
        utillity.UtillityMethods.asequal(self, total_rows, occurence, msg)

    def close_popup_dialog(self,popup_index):
        """
        @author = Niranjan 
        """
        top_buttons="#wall"+popup_index+" #wtop"+popup_index+" img"
        close_btns=self.driver.find_elements_by_css_selector(top_buttons)
        close_btns[1].click()
        time.sleep(1)
        
    def verify_horizontal_page_scroll(self,table,scroll,msg):
        '''
        Syntax: verify_horizontal_page_scroll('MAINTABLE_wbodyMain0', 'yes', 'Step 01.4: Notice that the horizontal scroll bar is present')
        Author: Sindhuja
        '''
        var = "[id='"+table+"']"
        value=self.driver.find_element(By.CSS_SELECTOR, var)
        actual_size = value.size['width']
        client = self.driver.execute_script("return document.documentElement.clientWidth;")
        if scroll == 'yes':
            utillity.UtillityMethods.as_GE(self,actual_size,client,msg)
        if scroll=='no':
            utillity.UtillityMethods.as_LE(self,actual_size,client,msg)
        
    def verify_freeze_column(self,scroll,scroll_window_id,msg):
        '''
        Syntax: verify_freeze_column('yes','IScrollWindowBody0',"Step 03: verify freeze column scroll bar")
        verify_freeze_column('no','IScrollWindowBody0',"Step 03: verify no freeze column scroll bar")
        author: Sindhuja
        '''
        value="[id='"+scroll_window_id+"']"
        if scroll == 'yes':
            try:
                freeze_column=self.driver.find_element(By.CSS_SELECTOR,value).is_displayed()
                utillity.UtillityMethods.asequal(self,True,freeze_column,msg)
            except NoSuchElementException:
                freeze_column=False
                utillity.UtillityMethods.asequal(self,True,freeze_column,msg)
        if scroll == 'no':
            try:
                freeze_column=self.driver.find_element(By.CSS_SELECTOR,value).is_displayed()
                utillity.UtillityMethods.asequal(self,False,freeze_column,msg)
            except NoSuchElementException:
                freeze_column=True
                utillity.UtillityMethods.asequal(self,True,freeze_column,msg)
    
    
    def verify_cell_property_size(self, table_id, rownum, colnum, expected, msg):
 
        '''
        Syntax: verify_cell_color_property('ITableData0', 0, 0,'R100', 'Step 05: Verify Comment is added', text_color='white', bg_color='red')
        params: rownum and colnum start with 0,0.
        Author: Gobi
        '''
        cell_css="table[id='" + table_id + "'] tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "']"
        actual_size=self.driver.find_element_by_css_selector(cell_css).size
            
        if int(actual_size['width']) in range(int(expected['width']), int(expected['width'])+8):
            print(msg + " Actual " + str(actual_size['width']) + " is present.- PASSED")
        else:
            print(msg + " Actual " + str(actual_size['width']) + " is present.- FAILED")
          
        if int(actual_size['height']) in range(int(expected['height'])-6, int(expected['height'])+10):
            print(msg + " Actual " + str(actual_size['height']) + " is present. - PASSED")
        else:
            print(msg + " Actual " + str(actual_size['height']) + " is present. - FAILED")
        
            
    def toc_select_item(self, main_table_index, item):
        """
        Usgae: active_misobj.toc_select_item(0, '[All]')
        """
        item_css="#MAINTABLE_" + str(main_table_index) + " table[class='arByToc'] span[class='arByTocItem']"
        items=self.driver.find_elements_by_css_selector(item_css)
        for i in range(len(items)):
            if items[i].text==item:
                items[i].click()
                time.sleep(2)
                break
            else:
                continue
    
    def toc_verify_bgcolor(self, main_table_index, item, color, msg):
        """
        Usage: verify_comment_field('ITableData0', 0, 0,'ENGLAND', 'Step 10.2: Verify Comment is added for ENGLAND')
        """
        all_css="#MAINTABLE_" + str(main_table_index) + " table[class='arByToc'] td[class='arByTocItemSelected']"
        item_css="#MAINTABLE_" + str(main_table_index) + " table[class='arByToc'] tr[class='arByTocItemSelected']"
        expected_color=utillity.UtillityMethods.color_picker(self, color, 'rgba')
        if item=='[All]':
            actual_item=(self.driver.find_element_by_css_selector(all_css).text).strip()
            utillity.UtillityMethods.asequal(self, item, actual_item, msg + " " + actual_item + " is selected in TOC.")
            actual_bg_color=self.driver.find_element_by_css_selector(all_css).value_of_css_property('background-color')
            utillity.UtillityMethods.asequal(self, expected_color, actual_bg_color, msg + " Background Color is " + actual_bg_color)
        else:
            actual_item=(self.driver.find_element_by_css_selector(item_css).text).strip()
            utillity.UtillityMethods.asequal(self,item, actual_item, msg + " " + actual_item + " is selected in TOC.")
            actual_bg_color=self.driver.find_element_by_css_selector(item_css).value_of_css_property('background-color')
            utillity.UtillityMethods.asequal(self, expected_color, actual_bg_color, msg + " Background Color is " + actual_bg_color)

    def verify_cell_property(self, table_id, rownum, colnum, field_value, msg, **kwargs):
        '''
        Syntax: verify_cell_property('ITableData0', 0, 0,'R100', 'Step 05: Verify row highlighted in Red with White text.', text_color='white', bg_color='red')
        verify_cell_property('ITableData0',5,1'ALFA ROMEO','Step 02:Verify row highlighted',text_color='white',bg_color='red')
        params: rownum and colnum start with 0,0.
        params: kwargs: text_color, bg_color
        Author: Niranjan
        '''
        cell_css="table[id='" + table_id + "'] tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "']" 
        actual_field_val=self.driver.find_element_by_css_selector(cell_css).text
        utillity.UtillityMethods.asequal(self,field_value, actual_field_val, msg + " " + actual_field_val + " is being considered.")
        if 'text_color' in kwargs:
            expected_text_color=utillity.UtillityMethods.color_picker(self, kwargs['text_color'], 'rgba')
            actual_text_color=self.driver.find_element_by_css_selector(cell_css).value_of_css_property('color')
            reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', actual_text_color)
            text_color=reobj.group(1)
            utillity.UtillityMethods.asin(self, text_color,expected_text_color, msg + "- text Color is " + actual_text_color)
            
        if 'bg_color' in kwargs:
            if kwargs['bg_color']=='transparent':
                expected_bg_color=Color.from_string(kwargs['bg_color']).rgba
            else:
                expected_bg_color=utillity.UtillityMethods.color_picker(self, kwargs['bg_color'], 'rgba')
            actual_bg_color=self.driver.find_element_by_css_selector(cell_css).value_of_css_property('background-color')
            bg_color=Color.from_string(actual_bg_color).rgba
            utillity.UtillityMethods.asin(self,bg_color,expected_bg_color, msg + "- Background Color is " + actual_bg_color)

    def verify_comment_tooltip(self, table_id, rownum, colnum, expected_tooltip_list, msg):
        """
        Usage: verify_cell_property('ITableData0', 0, 0,['This is the comment'],"Step 10: Verify tooltip comment")
        """
        tooltip_css="table[id='" + table_id + "'] tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "'] > div > span"
        tooltips=self.driver.find_element_by_css_selector(tooltip_css).get_attribute('title').strip()
        actual_tooltip_list=re.match('.*M]([a-zA-Z0-9\s]+)', tooltips).group(1).split("\n")
        utillity.UtillityMethods.asequal(self, expected_tooltip_list, actual_tooltip_list, msg)

    def verify_active_chart_tooltip(self, parent_id, raiser_class, expected_tooltip_list, msg, **kwargs):
        """
        Usage: expected=['DEALER_COST, ENGLAND: 37,853']
        usage : 
        miscelaneousobj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mbar',expected,"Step 01: Verify the bar riser")
        or 
        miscelaneousobj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mbar',expected,"Step 01: Verify the bar riser")
        
        """
        if 'default_move' in kwargs:
            pass
        else:
            action1 = ActionChains(self.driver)
            move1 = self.driver.find_element_by_css_selector("#"+ parent_id)
            if self.browser == 'Firefox':
                utillity.UtillityMethods.click_type_using_pyautogui(self, move1, move=True, **kwargs)
            else:
                action1.move_to_element_with_offset(move1,1,1).perform()
            time.sleep(5)
            del action1
        action = ActionChains(self.driver)        
        if 'default_move' in kwargs:
            pass
        else:
            raiser_css="#"+ parent_id + " [class*='" + raiser_class + "']"
            riser=self.driver.find_element_by_css_selector(raiser_css)
            if self.browser=='Firefox':
                utillity.UtillityMethods.click_type_using_pyautogui(self, riser, **kwargs)            
            else:
                action.move_to_element(riser).perform()
                del action
        time.sleep(2)
        tooltip_css="#"+ parent_id + " span[id='tdgchart-tooltip'] > div"
        tooltips=self.driver.find_element_by_css_selector(tooltip_css).text.split("\n")
        actual_tooltip_list=[el.strip() for el in tooltips]
        print(actual_tooltip_list)
        utillity.UtillityMethods.asequal(self,expected_tooltip_list,actual_tooltip_list,msg)

    def verify_active_popup_chart_tooltip(self, popup_id, chart_type, tooltip_lval, expected_tooltip,verify_color, msg):
        """
        Usage: verify_active_popup_chart_tooltip('wall2','bar','DEALER_COST','DEALER_COST:4,631',"Step 10: Verify tooltip")
        Usage: verify_active_popup_chart_tooltip('wall2','pie','FRANCE','FRANCE=5610(11%)','Pomegranate',"Step 10: Verify tooltip FRANCE=5610(11%)")
        params: popup_id='wall1' or 'wall2'
        params: tooltip_lval='DEALER_COST' OR 'ENGLAND'
        params: tooltip_lval: ITALY=51065(29.5%) (Note: Here no space in between values)
        Author: Nasir
        """
        if chart_type in ('bar', 'line'):
            raiser_css="#" + popup_id + " div[title^='" + tooltip_lval + " '][style*='background']"
        elif chart_type in ('scatter'):
            raiser_css="#" + popup_id + " div[title^='" + tooltip_lval + "=']"
        else:
            raiser_css="#" + popup_id + " div[title^='" + tooltip_lval + " =']"
        tooltips=self.driver.find_element_by_css_selector(raiser_css).get_attribute("title")
        actual_tooltip=re.sub("\s", "", tooltips)
        utillity.UtillityMethods.asequal(self, expected_tooltip, actual_tooltip, msg)
        fill2 = self.driver.find_element_by_css_selector(raiser_css).value_of_css_property("background-color")
        reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', fill2)
        bg_color=reobj.group(1)
        expected_color= utillity.UtillityMethods.color_picker(self, verify_color,'rgba')
        utillity.UtillityMethods.asin(self,bg_color,expected_color,msg+"Verify Color -"+verify_color+" ")
        
    def verify_popup_title(self, popup_id, expected_title, msg):
        """
        Params: table_id='wall1'
        Params: expected_title='Gross Profit BY Store Business Region'
        Syntax: verify_popup_title('wall1', 'Gross Profit BY Store Business Region', 'Step 03: Verify Title')
        @Author: Nasir 
        """
        r_title=self.driver.find_element_by_css_selector("#" + popup_id + " div.arWindowBar>table>tbody>tr>td.arWindowBarTitle").text
        r_cond=r_title.strip()==expected_title
        utillity.UtillityMethods.asequal(self,True, r_cond, msg)
    
    def verify_expandable_comment_tooltip(self, table_id, rownum, colnum, expected_tooltip_list, msg):
        """
        Usage: verify_cell_property('ITableData0', 0, 0,['This is the comment'],"Step 10: Verify tooltip comment")
        """
        tooltip_css="table[id='" + table_id + "'] tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "'] div[class='arCommentCell']"
        tooltips=self.driver.find_element_by_css_selector(tooltip_css).text.split('\n')
        actual_tooltip_list=[]
        for i in range(len(tooltips)):
            ob=re.match(r'.*[AP]M\s*(.*)', tooltips[i])
            actual_tooltip_list.append(ob.group(1))
        utillity.UtillityMethods.asequal(self, expected_tooltip_list, actual_tooltip_list, msg)

    def verify_active_lasso_menu(self,menu,msg):
        """miscelanousobj.verify_active_lasso_menu(menu_list, 'Step 02: Verify these menu items appear on the chart:')
           @author: Gobizen """
           
        selector= "[id*='ibi$tt$']"
        menu_act = []
        menu_act.append(self.driver.find_element_by_css_selector(selector).text) 
        utillity.UtillityMethods.asequal(self, menu, menu_act, msg)
    
    def select_active_lasso_menu(self, menu_name): 
        """miscelanousobj.select_active_lasso_menu('Filter Chart')
        @author: Gobizen"""
        selector= "[id*='ibi$tt$'] span"
        s = self.driver.find_elements_by_css_selector(selector)
        for x in range(len(s)):
            if s[x].text == menu_name:
                s[x].click()
                break
    def expand_or_colapse_accordian_field(self, table_id, rownum, colnum): 
        """expand_or_colapse_accordian_field('ITableData0', 0, 0)"""
        plus_minus_btn="table[id='" + table_id + "'] tr[id*='r" + str(rownum) + ".'] td[id$='C" + str(colnum) + "'] > div > span" 
        self.driver.find_element_by_css_selector(plus_minus_btn).click() 
        time.sleep(1) 
    
    def navigate_tabbed_report(self, main_table_index, tab_index):
        """
        params: main_table_index=0 or 1...
        params: tab_index=0 or 1...
        Usage: navigate_tabbed_report(0, 1)
        @author: Niranjan
        """
        tab_css="#MAINTABLE_" + str(main_table_index) + " #MAINTABLE_wmenu" + str(main_table_index) + " > table > tbody > tr > td"
        tabs=self.driver.find_elements_by_css_selector(tab_css)
        tabs[tab_index-1].click()
        time.sleep(1)

    def close_tabbed_report(self, main_table_index, tab_index):
        """
        params: main_table_index=0 or 1...
        params: tab_index=0 or 1...
        Usage: close_tabbed_report(0, 1)
        @author: Niranjan
        """
        tab_css="#MAINTABLE_" + str(main_table_index) + " #MAINTABLE_wmenu" + str(main_table_index) + " > table > tbody > tr img"
        tabs=self.driver.find_elements_by_css_selector(tab_css)
        tabs[tab_index].click()
        time.sleep(1)
        
    def verify_tabbed_report(self, main_table_index, expected_tab_list, msg):
        """
        params: main_table_index=0 or 1...
        params: expected_tab_list=[Report, Chart]...This can be full list or partial list
        Usage: verify_tabbed_report(0, [Report, Chart])
        @author: Niranjan
        """
        actual_tab_list=[]
        status=True
        tab_css="#MAINTABLE_" + str(main_table_index) + " #MAINTABLE_wmenu" + str(main_table_index) + " > table > tbody > tr >td"
        tabs=self.driver.find_element_by_css_selector(tab_css)
        for tab_items in tabs:
            actual_tab_list.append(tab_items.text.strip())
        for i in expected_tab_list:
            if i in actual_tab_list:
                pass
            else:
                status=False
                break
        self.asequal(status, True, msg)
        
    def verify_popup_appears(self, popup_id, expected_title, msg):
        """
        Params: table_id='wall1'
        Params: expected_title='Grid Tool'
        Syntax: verify_tool_popup('wall1', 'Grid Tool', 'Step 03: Verify Grid tool popup opened')
        @Author: Sindhuja 
        """
        index=list(popup_id)[-1]
        popup_title_css="#" + popup_id + " #wtop" + str(index)
        actual_title=self.driver.find_element_by_css_selector(popup_title_css).text.strip()
        utillity.UtillityMethods.asequal(self, expected_title, actual_title, msg)
        
        
    def verify_chart_title(self,popup_id,expected_title,msg):
        """
        Params: table_id='MAINTABLE_wbody0_ft'
        Params: expected_title='RETAIL_COST, P6.2 Dcost BY COUNTRY, CAR'
        Syntax: verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST, P6.2 Dcost BY COUNTRY, CAR', 'Step 03: Verify Title')
        @Author: Kiruthika 
        """
        cr_title=self.driver.find_element_by_css_selector("#"+popup_id+" tbody").text.strip()
        utillity.UtillityMethods.asequal(self,cr_title,expected_title,msg)
        
    def verify_arChartToolbar(self,window_id,menu,msg, **kwargs):
        """
        :param self: Current object 
        :param window_id: wall1 or wall2 or MAINTABLE_0 
        :param menu=['More Options','Column','Pie','Line','Scatter']
        :param :kwargs['custom_css'] = ".chartPanel [tdgtitle]"       (Other css value user pass)
        :param :kwargs['attribute_type'] = "title" OR 'Value'                   (attribute Value  user pass)
        :param :kwargs['text'] = True
        :Usage :verify_arChartToolbar('MAINTABLE_0',['More Options','Column','Pie','Line','Scatter'],"Step 02: Verify Chart toolbar")
        :Usage :verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 3.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        :Usage :verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 3.10: Verify Chart toolbar", custom_css='#MAINTABLE_wmenu0 .arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]', text=True)
        """
        custom_css=kwargs['custom_css'] if 'custom_css' in kwargs else ".arChartMenuBarContainer div[title]"
        attribute_type=kwargs['attribute_type'] if 'attribute_type' in kwargs else "title"
        css= "#" + window_id + " " + custom_css
        actual = []
        elm = self.driver.find_elements_by_css_selector(css)
        if 'text' in kwargs:
            for x in range(0,len(elm)):
                text =elm[x].text.strip().replace('\n','')
                actual.append(re.sub(' ','',text))
        else:
            for x in range(0,len(elm)):
                actual.append(elm[x].get_attribute(attribute_type))
        utillity.UtillityMethods.as_List_equal(self,actual,menu,msg)
        
        
    def send_as_email(self,filename,replace,filter,save,SaveReport=True):
        """
        :param filename: C1029345.htm
        :param replace: False
        :param filter: False
        :param save: False
        :param SaveReport: False
        :Syntax: send_as_email(Test_Case_ID+".htm",False,False,False)
        """
        self.driver.find_element_by_css_selector("form input").click()
        ele=self.driver.find_element_by_css_selector("form input")
        ele.send_keys(keys.Keys.CONTROL, 'a')
        ele.clear()
        dir=os.getcwd() + "\data\\" + filename
        ele.send_keys(dir)
        time.sleep(5)
        if replace == True:
            self.driver.find_element_by_css_selector("form[name='promptform'] input[id='ovverride']").click()
        if filter == True:
            self.driver.find_element_by_css_selector("form[name='promptform'] input[id='filtered']").click()
        if save == True:
            self.driver.find_element_by_css_selector("form[name='promptform'] input[id='savechange']").click()
        if SaveReport==True:
            self.driver.find_element_by_css_selector("div[class='arPromptButton']").click()
            
    def save_changes(self,filename,replace=True,filter=False,SaveReport=True,):
        """
        :param filename: C1029345.htm
        :param replace: False (default True which means replace is checked)
        :param filter: True (default False which means Filtered Only option is unchecked)
        :param SaveReport: False (default True which means it will click SaveReport button)
        :Usage: save_changes(Test_Case_ID+".htm")
        :Usage: save_changes(Test_Case_ID+".htm",False,True,False)
        """
        self.driver.find_element_by_css_selector("form input").click()
        ele=self.driver.find_element_by_css_selector("form input")
        ele.send_keys(keys.Keys.CONTROL, 'a')
        ele.clear()
        dir=os.getcwd() + "\data\\" + filename
        ele.send_keys(dir)
        time.sleep(5)
        if replace == False:
            self.driver.find_element_by_css_selector("form[name='promptform'] input[name='ovverride']").click()
        if SaveReport==True:
            self.driver.find_element_by_css_selector("div[class='arPromptButton']").click()
        if filter == True:
            self.driver.find_element_by_css_selector("form[name='promptform'] input[name='filtered']").click()
        
    def create_active_csv(self, windownum, file_name):
        """
        Usage: create_active_csv(3,'C2140681.csv')
        @author: Niranjan
        """
        time.sleep(20)
        self.driver.switch_to_window(self.driver.window_handles[windownum])
        time.sleep(20)
        base_csv=os.getcwd() + "\data\\" + file_name
        try:
            fileObj = open(base_csv, "w")
            fileObj.writelines(self.driver.find_element_by_css_selector("body").text)
            fileObj.close()
        except IOError:
            exit()
    def compare_active_csv(self, windownum, file_name, msg):
        """
        Usage: compare_active_csv(3)
        @author: Niranjan
        """
        time.sleep(20)
        self.driver.switch_to_window(self.driver.window_handles[windownum])
        time.sleep(20)
        base_csv=os.getcwd() + "\data\\" + file_name
        expected_list=[]
        actual_list=self.driver.find_element_by_css_selector("body").text.split('\n')
        try:
            fileObj = open(base_csv, "r")
            line = fileObj.readline()
            while line:
                expected_list.append(line.strip())
                line = fileObj.readline()
        except IOError:
            exit()
        utillity.UtillityMethods.asequal(self,expected_list, actual_list, msg)