from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.javascript import JavaScript
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.lib.base import BasePage
from selenium.webdriver.support.color import Color
from common.pages import visualization_ribbon,visualization_resultarea, ia_styling
from common.pages.ia_miscelaneous import IA_Miscelaneous as iamiscelaneousobject
from common.locators.ia_ribbon_locators import IaRibbonLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,re, os, pyautogui, subprocess
import sys
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard
    from pynput.keyboard import Key, Controller

class IA_Ribbon(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    def __init__(self, driver):
        super(IA_Ribbon, self).__init__(driver)
         
    def select_ia_top_toolbar_item(self, top_toolbar_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        param: item_name: 'new' OR 'run'.
        '''
        time.sleep(5)
        toolbar_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__['toolbar_'+top_toolbar_item_name])
        coreutillityobject.left_click(self, toolbar_item)
        time.sleep(8)
    
    def select_ia_application_menu_item(self, application_menu_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        param: item_name: 'save_as' OR 'run'.
        '''
        ia_btn=self.driver.find_element(*VisualizationRibbonLocators.Appbtn)
        coreutillityobject.left_click(self, ia_btn)
        elem1=VisualizationRibbonLocators.__dict__['menu_'+application_menu_item_name]
        self._validate_page(elem1)
        application_menu_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__['menu_'+application_menu_item_name])
        coreutillityobject.left_click(self, application_menu_item)
        time.sleep(8)
    
    def switch_ribbon_tab(self, tab_name): 
        '''
        Desc: This is used to switch to any visualization tab.
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        '''
        tab_css=VisualizationRibbonLocators.tab_css.format(tab_name)
        tab_elem=self.driver.find_element_by_css_selector(tab_css)
        coreutillityobject.left_click(self, tab_elem)
        enabled_tab_css="div[id='" + tab_name + "Tab'][style*='z-index: 1']" 
        utillityobject.synchronize_with_number_of_element(self, enabled_tab_css, 1, 30)
        time.sleep(1)
        
    def select_ia_ribbon_item(self, tab_name, ribbon_button_name):
        '''
        Desc: This is used to select any ribbon item within any tab.
        '''
        IA_Ribbon.switch_ribbon_tab(self, tab_name)
        button_name = tab_name.lower() + "_" + ribbon_button_name.lower()
        ribbon_item_css=VisualizationRibbonLocators.__dict__[button_name] 
        utillityobject.synchronize_with_number_of_element(self, ribbon_item_css[1], 1, 10)
        ribbon_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__[button_name])
        coreutillityobject.left_click(self, ribbon_item)
        
    def select_other_chart_types(self, chart_type, Chart_name, chart_index, starting_visibility_index=None, close_dialog='ok', verify_selection=True, verify_tooltip=None):
        '''
        Params: chart_type='bar','line','area','pie','x_y_plots','threed','stock','special','html5','map','html5_extension'.
        Params: Chart_name='vertical_clustered_bars', 'vertical_absolute_line'...(The name displayed when you hover over the chart image, with underscores, check the locator file)
        Params: chart_index=1, 2, 3...
        Params: starting_visibility_index=0, 1, 2, 3...(The index of the chart image which is visible)
        '''
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        iamiscelaneousobject.wait_for_object(self, ok_btn_css, option='number', expected_number=1)
        chart_type_elem=self.driver.find_element(*IaRibbonLocators.__dict__['select_{0}_chart'.format(chart_type)])
        JavaScript.scrollIntoView(self, chart_type_elem, wait_time=2)
        coreutillityobject.left_click(self, chart_type_elem)
        time.sleep(3)
        chart_elements=self.driver.find_elements(*IaRibbonLocators.__dict__['{0}_buttons'.format(chart_type)])
        if starting_visibility_index != None:
            chart_elements[int(starting_visibility_index)].click()
        else:
            chart_elements[0].click()
        time.sleep(2)
        elem1=(IaRibbonLocators.__dict__[Chart_name])
        self._validate_page(elem1)
        chart_elem = self.driver.find_element(*IaRibbonLocators.__dict__[Chart_name])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", chart_elem);
        if verify_tooltip != None :
            tooltip_css = "[class*='bi-tool-tip'][style*='inherit']"
            coreutillityobject.move_to_element(self, chart_elem)
            utillityobject.synchronize_until_element_is_visible(self, tooltip_css, 20)
            tooltip = utillityobject.validate_and_get_webdriver_object(self, tooltip_css, "Chart type tooltip")
            utillityobject.asequal(self, tooltip.text.strip(), verify_tooltip, "Step XX : Verify chart tooltip")
        coreutillityobject.left_click(self, chart_elem)
        time.sleep(3)  
        if verify_selection :     
            status=True if bool(re.match('.*charttypeRadioButton-checked.*', chart_elements[chart_index-1].get_attribute("class"))) else False
            utillityobject.asequal(self, True, status, "Step X: Verify the specified " + Chart_name + " is selected.")
        if close_dialog =='ok':
            self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(8)
                    
    """========================================Old functions==============================================="""
        
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
        
    
    def select_join_menu_buttons(self, btn_name, **kwargs):
        """
        ia_ribbonobj.select_join_menu_buttons("remove")
        """
        #browser=utillityobject.parseinitfile(self,'browser')
        button_name = "join_" + btn_name
        join_btn_name=self.driver.find_element(*IaRibbonLocators.__dict__[button_name])
        utillityobject.default_left_click(self, object_locator=join_btn_name, **kwargs)
        #self.driver.find_element(*IaRibbonLocators.__dict__[button_name]).click()
        '''if browser == 'Firefox':
            utillityobject.click_type_using_pyautogui(self, join_btn_name,leftClick=True, **kwargs)
        else:
            join_btn_name.click()'''
        time.sleep(2)
        if btn_name== "remove":
            btn_css="div[id^='BiDialog'] div[id^='BiOptionPane'] div[id^='BiButton']"
            elem=[el for el in self.driver.find_elements_by_css_selector(btn_css) if el.text.strip()=="OK"]
            elem[0].click()
            time.sleep(2)
        
    def create_hold_file(self, file_name, hold_format,**kwargs):
        """
        ia_resultobj.create_hold_file("C2163512", "Binary (*.ftm)")
        """
        visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual_ribbonobj.select_ribbon_item('Home', 'File')
        time.sleep(1)
        utillityobject.ibfs_save_as(self, file_name, hold_format,**kwargs)
        time.sleep(1)
    
    def create_join(self, target_table_path, master_file_name, new_join=True, **kwargs):
        """
        params: target_table_path='new_retail->dimension->wf_retail_time'
        params: new_join=True when you want to call first time for join
        params: new_join=False when you to add more master file in current join window
        Usage: create_join("new_retail->dimensions->wf_retail_vendor")
                        OR
        Usage: create_join("new_retail->dimensions->wf_retail_vendor", False)
        """
        if new_join==True:
            visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
            visual_ribbonobj.select_ribbon_item('Data', 'Join')
        css="#dlgJoin #dlgJoin_btnAddMaster"
        utillityobject.synchronize_with_number_of_element(self, css, 1, 20)
        join_add=self.driver.find_element(*IaRibbonLocators.join_add_new)
        coreutillityobject.python_left_click(self, join_add)
#         utillityobject.default_left_click(self, object_locator=join_add, **kwargs)
        time.sleep(10)
        open_dialog_file_name="#IbfsOpenFileDialog7_cbFileName"
        utillityobject.synchronize_with_number_of_element(self, open_dialog_file_name, 1, 20)
        if self.driver.find_element_by_css_selector(open_dialog_file_name).is_displayed()==False:
            coreutillityobject.python_left_click(self, join_add)
#             utillityobject.default_left_click(self, object_locator=join_add, **kwargs)
        utillityobject.synchronize_with_number_of_element(self, open_dialog_file_name, 1, 20)
        time.sleep(4)  
        utillityobject.select_masterfile_in_open_dialog(self, target_table_path, master_file_name)
            
    def create_join_to_handle_lessthan_two_targets(self, target_table_path, master_file_name, new_join=True, **kwargs):
        """
        params: target_table_path='new_retail->dimension->wf_retail_time'
        params: new_join=True when you want to call first time for join
        params: new_join=False when you to add more master file in current join window
        Usage: create_join("new_retail->dimensions->wf_retail_vendor")
                        OR
        Usage: create_join("new_retail->dimensions->wf_retail_vendor", False)
        """
        targets=target_table_path.split('->')
        if new_join==True:
            visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
            visual_ribbonobj.select_ribbon_item('Data', 'Join')
        time.sleep(1)
        join_add=self.driver.find_element(*IaRibbonLocators.join_add_new)
        utillityobject.default_left_click(self, object_locator=join_add, **kwargs)
        '''if browser == 'Firefox':
            utillityobject.click_type_using_pyautogui(self, join_add, browser_height=65, doubleClick=True)
        else:
            join_add.click()'''
        time.sleep(10)
        #self.driver.find_element(*IaRibbonLocators.join_add_new).click()
        open_dialog_file_name="#IbfsOpenFileDialog7_cbFileName"
        if self.driver.find_element_by_css_selector(open_dialog_file_name).is_displayed()==False:
            utillityobject.default_left_click(self, object_locator=join_add, **kwargs)
        elem1=(By.CSS_SELECTOR, open_dialog_file_name)
        self._validate_page(elem1)
        time.sleep(4)  
        if len(targets)>2:
            for app in targets[:-2]:
                apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
                x=[el.text.strip() for el in self.driver.find_elements_by_css_selector(apps_css)]
                apps=self.driver.find_elements_by_css_selector(apps_css)
                apps[x.index(app)].find_element_by_css_selector("img[src*='triangle']").click()
            time.sleep(5)
            '''apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
            x=[el.text.strip() for el in self.driver.find_elements_by_css_selector(apps_css)]
            apps=self.driver.find_elements_by_css_selector(apps_css)
            apps[0].click()
            time.sleep(5)'''
            get_folder=True
            counter=0
            while get_folder:
                x=[el.text.strip() for el in self.driver.find_elements_by_css_selector(apps_css)]
                if targets[-2] in x:
                    apps=self.driver.find_elements_by_css_selector(apps_css)
                    apps[x.index(targets[-2])].find_element_by_css_selector("img[src*='folder']").click()
                    time.sleep(5)
                    get_folder=False
                    break
                else:
                    counter+=1
                    action = ActionChains(self.driver)
                    action.send_keys(keys.Keys.PAGE_DOWN).perform()
                    time.sleep(5)
                    del action
                    if counter==10:
                        break
                time.sleep(1)
            time.sleep(1)
            '''apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
            x=[el.text.strip() for el in self.driver.find_elements_by_css_selector(apps_css)]
            apps=self.driver.find_elements_by_css_selector(apps_css)
            apps[x.index(targets[-2])].find_element_by_css_selector("img[src*='folder']").click()'''
            file_name_input_css="#IbfsOpenFileDialog7_cbFileName input" 
            self.driver.find_element_by_css_selector(file_name_input_css).click()
            time.sleep(2)    
            utillityobject.ibfs_save_as(self, targets[-1],**kwargs)
            time.sleep(1)
        else:
            utillityobject.select_masterfile_in_open_dialog(self, master_file_name, targets[-1])

    """ <<<<<<< New action implemented, hence once verified, can delete this >>>>>>>>>
    def create_join(self, target_table):
        visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual_ribbonobj.select_ribbon_item('Data', 'Join')
        time.sleep(1)
        self.driver.find_element(*IaRibbonLocators.join_add_new).click()
        time.sleep(1)
        utillityobject.ibfs_save_as(self, target_table)
        time.sleep(1)"""
    '''
    Use create_join("new_retail->dimensions->wf_retail_vendor", False)
    
    def add_more_join(self, target_table):
        """
        ia_ribbonobj.add_more_join("locator")
        """ 
        self.driver.find_element(*IaRibbonLocators.join_add_new).click()
        time.sleep(1)
        utillityobject.ibfs_save_as(self, target_table)
        time.sleep(1)
    '''   
    
    def verify_join_link_color(self, link_index, expected_color, msg):
        """
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 06a: verify Join link color 'blue' for first join")
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 06b: verify Join link color 'red' for second join")
        """ 
        link_css="#dlgJoin line[marker-start]"
        link_objs=self.driver.find_elements_by_css_selector(link_css)
        actual_color=link_objs[link_index].get_attribute("stroke")
        utillityobject.asequal(self,expected_color, actual_color, msg)
                
    def click_join_link(self, link_index):
        link_css="#dlgJoin line[marker-start]"
        link_objs=self.driver.find_elements_by_css_selector(link_css)
        link_objs[link_index].click()
        time.sleep(1)
        
    def create_join_link(self, source_master_index, source_field, target_master_index, target_field, **kwargs):
        """
        ia_ribbonobj.create_join_link(0, "ID_GEOGRAPHY", 1, "ID_GEOGRAPHY", target_scroll_down=2)
        param: kwargs['target_scroll_down'] -> number of times need to scroll_down in target join dialog
        """
        table_css="#dlgJoin #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        get_source=True
        source_tds=tables[source_master_index].find_elements_by_css_selector("td")
        utillityobject.click_on_screen(self, tables[source_master_index], coordinate_type='right', x_offset=-5)
        
        if 'source_scroll_down' in kwargs:
            
            for i in range(1,kwargs['source_scroll_down']):
                print ("source 1", 1)
                procesobj = subprocess.Popen(os.getcwd() + '\\common\\lib\\mouse_scroll.exe WheelDown 1')
                procesobj.wait()
                time.sleep(1)
                del procesobj
#                 
#                 time.sleep(1)
#                 procesobj.wait()
#                 del procesobj
        time.sleep(1)
        table_css="#dlgJoin #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        source_tds=tables[source_master_index].find_elements_by_css_selector("td")
        source_list=[el.text for el in source_tds]
        print('source list', source_list)
        if source_field in source_list:
            source_elem=source_tds[source_list.index(source_field)].find_element_by_css_selector("img[src*='column']")
        time.sleep(4)
        """old code
        source_tds=tables[source_master_index].find_elements_by_css_selector("td")
        source_tds[0].click()
        while(get_source):
            if self.browser=='Firefox':
                pyautogui.hotkey('pagedown')
            else:
                action = ActionChains(self.driver)
                action.send_keys(keys.Keys.PAGE_DOWN).perform()
                del action
            time.sleep(1)
            table_css="#dlgJoin #metaDataBrowser"
            tables=self.driver.find_elements_by_css_selector(table_css)
            source_tds=tables[source_master_index].find_elements_by_css_selector("td")
            source_list=[el.text for el in source_tds]
            if source_field in source_list:
                src_td=source_tds[source_list.index(source_field)]  # temp
                src_elem=source_tds[source_list.index(source_field)].find_element_by_css_selector("img[src*='column']")
                get_source=False
                break
        time.sleep(1)"""
        
        
        target_tds=tables[target_master_index].find_elements_by_css_selector("td")
        utillityobject.click_on_screen(self, tables[target_master_index], coordinate_type='right', x_offset=-5)
        if 'target_scroll_down' in kwargs:
            for i in range(1,kwargs['target_scroll_down']):
                print ("target 1", 1)
                procesobj = subprocess.Popen(os.getcwd() + '\\common\\lib\\mouse_scroll.exe WheelDown 1')
                time.sleep(1)
                procesobj.wait()
                del procesobj
        time.sleep(1)
        table_css="#dlgJoin #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        target_tds=tables[target_master_index].find_elements_by_css_selector("td")
        target_list=[el.text for el in target_tds]
        print('target list', target_list)
        if target_field in target_list:
            target_elem=target_tds[target_list.index(target_field)].find_element_by_css_selector("img[src*='column']")
        time.sleep(4)
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type='left', sx_offset=55, **kwargs)
        time.sleep(2)
            
    def create_additional_join_link(self, source_master_index, source_field, target_master_index, target_field, **kwargs):
        """
        ia_ribbonobj.create_additional_join_link(0, "PIN", 1, "PIN")
        """
        table_css="#dlgJoin #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        get_source=True
        source_tds=tables[source_master_index].find_elements_by_css_selector("td")
        source_tds[0].click()
        while(get_source):
            if Global_variables.browser_name in ['firefox']:
                pyautogui.hotkey('pagedown')
            else:
                action = ActionChains(self.driver)
                action.send_keys(keys.Keys.PAGE_DOWN).perform()
                del action
            '''action = ActionChains(self.driver)
            action.send_keys(keys.Keys.PAGE_DOWN).perform()'''
            time.sleep(1)
            table_css="#dlgJoin #metaDataBrowser"
            tables=self.driver.find_elements_by_css_selector(table_css)
            source_tds=tables[source_master_index].find_elements_by_css_selector("td")
            source_list=[el.text for el in source_tds]
            if source_field in source_list:
                src_td=source_tds[source_list.index(source_field)]  # temp
                src_elem=source_tds[source_list.index(source_field)].find_element_by_css_selector("img[src*='column']")
                get_source=False
                break
            #del action
        target_tds=tables[target_master_index].find_elements_by_css_selector("td")
        target_tds[0].click()
        get_target=True
        while(get_target):
            if Global_variables.browser_name in ['firefox']:
                pyautogui.hotkey('pagedown')
            else:
                action1 = ActionChains(self.driver)
                action1.send_keys(keys.Keys.PAGE_DOWN).perform()
                del action1
            '''action1 = ActionChains(self.driver)
            action1.send_keys(keys.Keys.PAGE_DOWN).perform()'''
            time.sleep(1)
            table_css="#dlgJoin #metaDataBrowser"
            tables=self.driver.find_elements_by_css_selector(table_css)
            target_tds=tables[target_master_index].find_elements_by_css_selector("td")
            target_list=[el.text for el in target_tds]
            if target_field in target_list:
                target_td=target_tds[target_list.index(target_field)]   # temp
                target_elem=target_tds[target_list.index(target_field)].find_element_by_css_selector("img[src*='column']")
                get_source=False
                break
            #del action1
        time.sleep(4)
        utillityobject.drag_drop_using_uisoup(self, src_elem, target_elem, src_cord_type='left', sx_offset=55, **kwargs)
        time.sleep(2)
        
                
    def verify_join_filter_Condition(self, expected_condition, msg):
        filter_condition_list=(self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree table").text).split('\n')
        print(filter_condition_list)
        utillityobject.asin(self, expected_condition, filter_condition_list, msg)
    
    def select_condition_in_filter_dialog(self, rownum, condition_name, **kwargs):
        paste_icon_css='div[id="dlgWhere"] img[src*="paste_clipboard"][style*="opacity"]'
        utillityobject.synchronize_with_number_of_element(self, paste_icon_css, 1, 20)
        if Global_variables.browser_name in ['firefox', 'ie']:
            pass
        else:
            get_value_btn_css="#dlgWhereGetValueBox #dlgWhereValue_tbuttonGetValue" 
            elem=(By.CSS_SELECTOR, get_value_btn_css)
            self._validate_page(elem)
            self.driver.find_element_by_css_selector("#wndWhereValuePopup_btnCancel img").click()
            time.sleep(2)
        if Global_variables.browser_name in ['firefox', 'ie']:
            wheretree=self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree")
            utillityobject.click_type_using_pyautogui(self, wheretree, doubleClick=True, **kwargs)
        else:
            action4=ActionChains(self.driver)
            action4.double_click(self.driver.find_element_by_css_selector("#dlgWhere #dlgWhereWhereTree")).perform()
            time.sleep(5)
            del action4        
        condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(" + str(rownum) + ") span[class='selected lead']>span>span")
        condition_elem[len(condition_elem)-2].click() 
        if Global_variables.browser_name in ['firefox', 'ie']:
            utillityobject.click_type_using_pyautogui(self, condition_elem[len(condition_elem)-2],doubleClick=True, **kwargs)
            utillityobject.click_type_using_pyautogui(self, condition_elem[len(condition_elem)-2],leftClick=True, **kwargs)
        else:
            action1 = ActionChains(self.driver)
            action1.double_click(condition_elem[len(condition_elem)-2]).perform()
            del action1
        get_value_btn_css="#wndWhereOperatorPopup_list" 
        elem=(By.CSS_SELECTOR, get_value_btn_css)
        self._validate_page(elem)
        items=self.driver.find_elements_by_css_selector("#wndWhereOperatorPopup_list > div[id^='BiListItem']")
        items[[el.text.strip() for el in items].index(condition_name)].click()
        if Global_variables.browser_name in ['firefox']:
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
        else:
            action2=ActionChains(self.driver)
            time.sleep(1)
            action2.send_keys(Keys.ENTER).perform()
            time.sleep(1)  
            action2.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            del action2
        time.sleep(2) 
                
    def close_filter_dialog(self, btn='ok'):
        """
        params: btn='ok' or 'cancel'
        """
        close_elem = self.driver.find_element_by_css_selector("#dlgWhere  #dlgWhere_btnOK")
        time.sleep(2)
        coreutillityobject.python_left_click(self, close_elem)
                    
    def select_filter_values(self, filter_type, getvalue_params, list_value, **kwargs):
        if filter_type=='static':
            get_value_btn_css="#dlgWhereValue_tbuttonParamGetValue"
            value_item_css="#dlgWhereValue_listParamValues span"
            add_btn_css="#dlgWhereValue_btnParamGetValuesAdd img"
            selected_values_css="#id_wv_param_list_mvalues"
        if filter_type=='constant':
            get_value_btn_css="#dlgWhereValue_tbuttonGetValue"
            value_item_css="#dlgWhereValue_listValues span"
            add_btn_css="#dlgWhereValue_btnGetValuesAdd img"
            selected_values_css="#id_wv_list_mvalues"
        get_value_btn=self.driver.find_element_by_css_selector(get_value_btn_css)
        coreutillityobject.python_left_click(self, get_value_btn)
#         utillityobject.default_left_click(self, object_locator=get_value_btn, **kwargs)
        time.sleep(2)
        utillityobject.select_or_verify_bipop_menu(self, getvalue_params) 
        for value in list_value:
            values=self.driver.find_elements_by_css_selector(value_item_css)
#             coreutillityobject.python_left_click(self, values, element_location='top_left')
            values[0].click()        
            time.sleep(2)
            get_val=True
            while(get_val):
                action1 = ActionChains(self.driver)
                if Global_variables.browser_name in ['firefox']:
                    pyautogui.press('pagedown')
                else:
                    action1.send_keys(keys.Keys.PAGE_DOWN).perform()
                    time.sleep(1)
                values_elements=self.driver.find_elements_by_css_selector(value_item_css)
                value_list=[el.text for el in values_elements]
                time.sleep(10)
                if value in value_list:  
                    coreutillityobject.python_left_click(self, values_elements[value_list.index(value)])              
#                     utillityobject.default_left_click(self, object_locator=values_elements[value_list.index(value)], **kwargs)
                    time.sleep(4)
                    add_btn=self.driver.find_element_by_css_selector(add_btn_css)
                    time.sleep(1)
                    coreutillityobject.python_left_click(self, add_btn)              
#                     utillityobject.default_left_click(self, object_locator=add_btn, **kwargs)
                    time.sleep(1)
                    get_val=False
                    break
                del action1
        selected_value_list=self.driver.find_element_by_css_selector(selected_values_css).text.split('\n')     
        utillityobject.asin(self, value, selected_value_list, "Step X : " + value + " is selected.")
        #self.driver.find_element_by_id("wndWhereValuePopup_btnOK").click()
        time.sleep(1)
    
    def create_constant_filter_condition(self, getvalue_params, value, filter_dialog_close=True, **kwargs):   
        """
        params: getvalue_params='All' OR 'First', OR 'Last'....
        Usage: create_constant_filter_condition('All', '13000')
        Usage: create_parameter_filter_condition('Static',['AUDI','BMW','JAGUAR'],getvalue_params='All')
        """
        filtercaption_css="#dlgWhere [class*='active'] [class*='caption'] [class*='bi-label']"
        utillityobject.synchronize_with_number_of_element(self,filtercaption_css, 1, 190) 
#         rownum=kwargs['rownum'] if 'rownum' in kwargs else 2
#         if Global_variables.browser_name in ['firefox', 'ie']:
#         condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(" + str(rownum) + ")  span[class*='selected']>span>span")
#         utillityobject.click_on_screen(self, condition_elem[len(condition_elem)-1], 'middle', click_type=2, pause=1)
#         utillityobject.click_on_screen(self, condition_elem[len(condition_elem)-1], 'middle', click_type=0, pause=1)
        IA_Ribbon.open_where_value_popup(self, **kwargs)
        time.sleep(5)
        get_value_btn_css="#dlgWhereGetValueBox #dlgWhereValue_tbuttonGetValue" 
#         elem=(By.CSS_SELECTOR, get_value_btn_css)
#         self._validate_page(elem)
        utillityobject.synchronize_until_element_is_visible(self, get_value_btn_css, 190)
        time.sleep(2)       
        self.select_filter_values('constant', getvalue_params, value, **kwargs)
        ok="#wndWhereValuePopup_btnOK"
        ok_btn=self.driver.find_element_by_css_selector(ok)
        coreutillityobject.python_left_click(self, ok_btn)
#         utillityobject.default_left_click(self, object_locator=ok_btn, **kwargs)
        time.sleep(1)
        if filter_dialog_close==True:
            self.close_filter_dialog()
            
    def create_constant_filter_condition_for_textfield(self, field_name, filter_dialog_close=True, **kwargs):   
        """
        @PARAM: field_name  = 'COUNTRY'
        Usage: create_constant_filter_condition_for_textfield('ENGLAND' (OR) 'JAPAN')
        
        """
        filtercaption_css="#dlgWhere [class*='active'] [class*='caption'] [class*='bi-label']"
        utillityobject.synchronize_with_number_of_element(self,filtercaption_css, 1, 190) 
#         rownum=kwargs['rownum'] if 'rownum' in kwargs else 2
#         if Global_variables.browser_name in ['firefox', 'ie']:
#         condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(" + str(rownum) + ")  span[class*='selected']>span>span")
#         utillityobject.click_on_screen(self, condition_elem[len(condition_elem)-1], 'middle', click_type=2, pause=1)
#         utillityobject.click_on_screen(self, condition_elem[len(condition_elem)-1], 'middle', click_type=0, pause=1)
        IA_Ribbon.open_where_value_popup(self, **kwargs)
        time.sleep(8)
        textfield_css="#dlgWhereValue #id_wv_text_value"
        textfield_obj=self.driver.find_element_by_css_selector(textfield_css)
        time.sleep(2)
        utillityobject.set_text_field_using_actionchains(self, textfield_obj, field_name)
        add_css=self.driver.find_element_by_css_selector("#dlgWhereValue #dlgWhereValue_btnConstAdd")
#         utillityobject.default_left_click(self, object_locator=add_css, **kwargs)
        coreutillityobject.left_click(self, add_css)
        time.sleep(1)
        ok="#wndWhereValuePopup_btnOK"
        ok_btn=self.driver.find_element_by_css_selector(ok)
        coreutillityobject.left_click(self, ok_btn)
#         utillityobject.default_left_click(self, object_locator=ok_btn, **kwargs)
        time.sleep(1)
        if filter_dialog_close==True:
            self.close_filter_dialog()

    def create_parameter_filter_condition(self, parameter_type, value,filter_dialog_close=True,**kwargs):
        """
        params: parameter_type='static' or dynamic or simple 
        Usage: create_parameter_filter_condition('Dynamic', ['AREA'])
        kwargs: getvalue_params='All' or ParamMultiple=True or verify_radiobtn="true"
        Usage: create_parameter_filter_condition('Static',['AUDI','BMW','JAGUAR'],getvalue_params='All')
        Usage: create_parameter_filter_condition('Dynamic', ['COUNTRY'],ParamMultiple=True)
        Usage: create_parameter_filter_condition('Static',sel_list,verify_radiobtn="true",getvalue_params='All')
        """
        filtercaption_css="#dlgWhere [class*='active'] [class*='caption'] [class*='bi-label']"
        utillityobject.synchronize_with_number_of_element(self,filtercaption_css, 1, 60)
        IA_Ribbon.open_where_value_popup(self, **kwargs)
#         condition_elem=self.driver.find_element_by_css_selector("div[id^=InlineControlValue] .bi-label")
#         coreutillityobject.left_click(self, condition_elem)
        utillityobject.synchronize_with_number_of_element(self,"#dlgWhereValue", 1, 40) 
        utillityobject.select_combobox_item(self, 'id_wv_combo_type', 'Parameter')
        if 'verify_radiobtn' in kwargs:
            stat=self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamDynamic").get_attribute("disabled")
            utillityobject.asequal(self,stat,"true","Step X: Verify radio button is Enabled or Disabled")
        if parameter_type=='Simple':
            self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamSimple input").click()
            time.sleep(4)
        if parameter_type=='Static':
            self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamStatic input").click()
            time.sleep(4)
            self.select_filter_values('static', kwargs['getvalue_params'], value)
        if parameter_type=='Dynamic':
            self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamDynamic input").click()
            values=self.driver.find_elements_by_css_selector("#dlgWhereValue #metaDataBrowser .bi-tree-view-body-content td img.icon")
            values[0].click()
            action1 = ActionChains(self.driver)
            if Global_variables.browser_name in ['firefox']:
                pyautogui.press('home')
            else:
                action1.send_keys(keys.Keys.HOME).perform()
            time.sleep(1)
            get_val=True
            while(get_val):
                action2 = ActionChains(self.driver)
                if Global_variables.browser_name in ['firefox']:
                    pyautogui.press('pagedown')
                else:
                    action2.send_keys(keys.Keys.PAGE_DOWN).perform()
                time.sleep(1)
                values_elements=self.driver.find_elements_by_css_selector("#dlgWhereValue #metaDataBrowser .bi-tree-view-body-content td")
                value_list=[el.text.strip() for el in values_elements]
                if value[0] in value_list:
                    values_elements[value_list.index(value[0])].find_element_by_css_selector("img[src*='column']").click()
                    time.sleep(1)
                    get_val=False
                    break
                del action2 
        if 'ParamOptional' in kwargs:
            self.driver.find_element_by_css_selector("#dlgWhereValue_chkParamOptional").click()                
        if 'ParamMultiple' in kwargs:
            self.driver.find_element_by_css_selector("#dlgWhereValue_chkParamMultiple").click()
            time.sleep(2)
        ok_btn=self.driver.find_element_by_css_selector("#wndWhereValuePopup_btnOK")
        coreutillityobject.left_click(self, ok_btn)
#         utillityobject.default_left_click(self, object_locator=elem1, **kwargs)  
        time.sleep(6)          
        if filter_dialog_close==True:
            self.close_filter_dialog()
    
    def open_where_value_popup(self, **kwargs):
        if 'rownum' not in kwargs:
            rownum=2
        else:
            rownum=kwargs['rownum']
#         if Global_variables.browser_name in ['firefox']:
        condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(" + str(rownum) + ")  span[class*='selected']>span>span")
        elem=condition_elem[len(condition_elem)-1]
        coreutillityobject.python_doubble_click(self, elem)
#         utillityobject.click_on_screen(self, elem, 'middle', click_type=2, **kwargs)
        time.sleep(5)
        coreutillityobject.python_left_click(self, elem)
#         utillityobject.click_on_screen(self, elem, 'middle', click_type=0, **kwargs)
        filtercaption_css="#wndWhereValuePopup:not([style*='hidden'])"
        utillityobject.synchronize_until_element_is_visible(self, filtercaption_css, 190)
    
    def open_where_popup_in_filter_dialog(self, where_row, option):
        """
        Description : This method will open where field popup by double click.
        :arg - where_row : Row number of where condition. where_row should start from 1
        :Usage : open_where_popup_in_filter_dialog(1, "field")
        """
        if option == "field" :
            option_index = 1
            control_css = "div[id^='InlineControl-']"
            popup_css = "#wndWhereFieldPopup:not([style*='hidden'])"
        elif option == "operator" :
            option_index = 2
            control_css = "div[id^='InlineControlOperator-']"
            popup_css = "#wndWhereOperatorPopup:not([style*='hidden'])"
        elif option == "value" :
            option_index = 3
            control_css = "div[id^='InlineControlValue-']"
            popup_css = "#wndWhereValuePopup:not([style*='hidden'])"
        else :
            raise NotImplementedError
        control_dropdown_css = control_css + " .bi-button:not([style*='hidden'])"
        where_option_css = "#dlgWhereWhereTree .bi-tree-view-table>tbody>tr:nth-child({0}) span[class]>span[dir] span[dir]:nth-child({1})".format(int(where_row) + 1, option_index)
        where_option_obj = self.driver.find_elements_by_css_selector(where_option_css)
        if len(where_option_obj) > 0 :
            control_obj = where_option_obj[0]
        else :
            control_obj = utillityobject.validate_and_get_webdriver_object(self, control_css, "Filter dialog where condition")
        coreutillityobject.python_doubble_click(self, control_obj)
        utillityobject.synchronize_until_element_is_visible(self, control_dropdown_css, 10, pause_time=3) 
        control_dropdown_obj = utillityobject.validate_and_get_webdriver_object(self, control_dropdown_css, "Filter dialog field drop down")
        fields_popup = self.driver.find_elements_by_css_selector(popup_css)
        (len(fields_popup)==0) and coreutillityobject.left_click(self, control_dropdown_obj)
        utillityobject.synchronize_until_element_is_visible(self, popup_css, 30, pause_time=3)
    
    def select_parameter_type(self, parameter_type):
        if parameter_type=='Simple':
            self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamSimple input").click()
        if parameter_type=='Static':
            self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamStatic input").click()
        if parameter_type=='Dynamic':
            self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamDynamic input").click()
        time.sleep(4)
    
    def check_parameter_checkbox(self, ParamOptional=False, ParamMultiple=False):
        if ParamOptional == True:
            self.driver.find_element_by_css_selector("#dlgWhereValue_chkParamOptional").click()                
        if ParamMultiple  == True:
            self.driver.find_element_by_css_selector("#dlgWhereValue_chkParamMultiple").click()
    
    def close_where_value_popup(self):
        elem1=self.driver.find_element_by_css_selector("#wndWhereValuePopup_btnOK img")
        coreutillityobject.left_click(self, elem1)  
        time.sleep(6)  
    
    def create_field_filter_condition(self, rownum):   
        condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(" + rownum + ")  span[class='selected lead']>span>span")
        condition_elem[len(condition_elem)-1].click()  
        action = ActionChains(self.driver)
        action.double_click(condition_elem[len(condition_elem)-1]).perform()            
    
    def enter_where_value_text_field(self, field_name):
        css="#id_wv_text_name"
        text_field_elem=utillityobject.validate_and_get_webdriver_object(self, css, 'Field Name Text')
        utillityobject.set_text_field_using_actionchains(self, text_field_elem, field_name)
        
    def click_equal_to_condition_in_filter_dialog(self, filter_condition_type):
        '''
        This function is used to click Equal to condition in filter dialog
        click_equal_to_condition_in_filter_dialog('Greater than')
        '''
        equal_to_css="#dlgWhereWhereTree [id^='InlineControlOperator']"
        filter_condition_css="#wndWhereOperatorPopup_list > div[id^='BiListItem']"
        sync_css="#wndWhereOperatorPopup_list"
        elem=utillityobject.validate_and_get_webdriver_object(self, equal_to_css, 'Equal to condition in filter dialog')
        coreutillityobject.left_click(self, elem)
        utillityobject.synchronize_until_element_is_visible(self, sync_css, 10)
        list_items=utillityobject.validate_and_get_webdriver_objects(self, filter_condition_css, 'Equal to condition values in filter dialog')
        elm=list_items[[el.text.strip() for el in list_items].index(filter_condition_type)]
        coreutillityobject.double_click(self, elm)   
    
    def create_slicer(self, group_index, item_name, combo_item_list, data_type, btnname, **kwargs):
        """
        combo_item_list = ['ALL STEEL BODY', 'POWER FRONT BRAKES', 'REAR DRUM BRAKES', 'WRAP AROUND BUMPERS']
        params: create_slicer(1,'STANDARD', combo_item_list, 'large', 'ok', last_combo_item_no=50)
        
        [or]
        
        combo_item_list = ['ENGLAND', 'ITALY', 'W GERMANY']
        params: create_slicer(1,'COUNTRY', combo_item_list, 'small', 'ok')
        """
        self.select_group_slicer_dropdown(group_index, item_name)
        if data_type == 'large':
        #if last_combo_item_no > 7:
            self.select_slicer_values_from_multiple_list(combo_item_list,**kwargs)
        else:
            self.select_slicer_values_from_single_list(combo_item_list)
        time.sleep(1)
        self.close_slicer_dialog(btnname)
        time.sleep(4)
        
        '''group_css="#SlicersTab #SlicersCluster_" + group_index
        label_css=group_css + " div[id*='LabelSlicer']"
        x=self.driver.find_elements_by_css_selector(label_css)
        l=[el.text.strip() for el in x]
        combo_id="SlicersCluster_1_Control1Slicer_" + l.index(item_name)
        for combo_item in combo_item_list:
            utillityobject.select_combobox_item(self, combo_id, combo_item)
        ok_btn_css="#QbSlicerValuesDialog-3108 #filterValuesOkBtn"'''    
    
    def select_slicer_condition(self, group_index, condition_image_index, condition_name, **kwargs):
        """
        params: group_index:1, 2, 3...This will start from 1. and should be integer.
        params: group_image_index:1, 2, 3...This will start from 1. and should be integer.
        Usage:  select_slicer_condition(1, 0, 'gte')
        """
        slicer_condition_ids={'eq':'equalButton',
                    'ne':'notEqualButton',
                    'ir':'inRangeButton',
                    'nir':'notInRangeButton',
                    'gt':'greaterThanButton',
                    'lt':'lessThanButton',
                    'gte':'greaterThanEqualButton',
                    'lte':'lessThanEqualButton'}
        slicer_cond=self.driver.find_element_by_css_selector("#SlicersCluster_" + str(group_index) + " #SlicersCluster_" + str(group_index) + "_OperatorSlicer_" + str(condition_image_index) + " img")
        utillityobject.default_left_click(self, object_locator=slicer_cond, **kwargs)
        '''browser_height=80
        slicer_cond=self.driver.find_element_by_css_selector("#SlicersCluster_" + str(group_index) + " #SlicersCluster_" + str(group_index) + "_OperatorSlicer_" + str(condition_image_index) + " img")
        if self.browser=='Firefox':
            x_fr=slicer_cond.location["x"]
            y_fr=slicer_cond.location["y"]
            pyautogui.moveTo(x_fr+3,y_fr+browser_height)
            time.sleep(2)
            pyautogui.click(x_fr+3,y_fr+browser_height,button='left')
        else:
            slicer_cond.click()'''
        time.sleep(6)
#        self.driver.find_element_by_css_selector("#SlicersCluster_" + str(group_index) + " #SlicersCluster_" + str(group_index) + "_OperatorSlicer_" + str(condition_image_index) + " img").click()
#        time.sleep(1)
        slicer_cond_elem=self.driver.find_element_by_css_selector("#operatorsMenu #" + slicer_condition_ids[condition_name] + " img")
        utillityobject.default_left_click(self, object_locator=slicer_cond_elem, **kwargs)        
        '''if self.browser=='Firefox':
            x_fr=slicer_cond_elem.location["x"]
            y_fr=slicer_cond_elem.location["y"]
            pyautogui.moveTo(x_fr+3,y_fr+browser_height)
            time.sleep(2)
            pyautogui.click(x_fr+3,y_fr+browser_height,button='left')
        else:
            slicer_cond_elem.click()'''
        time.sleep(6)
    
    def verify_slicer_group(self, group_index, expected_list, msg):
        """
        params: group_index:1, 2, 3...This will start from 1. and should be integer.
        params: expected_list= ['Group 1', 'COUNTRY']
        Usage: verify_slicer_group(1, expected_list, "Step 1a: Verify the group 1")
        """
        group_css="#SlicersTab #SlicersCluster_"+str(group_index)+" [class*='bi-label']"
#         actual_list=self.driver.find_element_by_css_selector(group_css).text.strip().split("\n")
        slicer_list=[el.text.strip() for el in self.driver.find_elements_by_css_selector(group_css)]
        actual_list=[list_value for list_value in slicer_list if list_value not in '']
        utillityobject.asequal(self, expected_list, actual_list, msg)
    
    def drag_drop_fields_to_slicer(self, field_name, group_index, field_position=1, **kwargs):
        """
        params: group_index:1, 2, 3...This will start from 1. and should be integer.
        params: field_position:1, 2, 3...This will start from 1. and should be integer.
        :Usage: drag_drop_fields_to_slicer('CURR_SAL', 1, field_position=2)
        author = Niranjan 
        """
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'middle'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_yoff_set=kwargs['target_Yoffset'] if 'target_Yoffset' in kwargs else 20
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        element.clear()
        time.sleep(1)
        element.click()
        time.sleep(3)
        element.send_keys(field_name)
        time.sleep(3)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
        if Global_variables.browser_name in ['edge']:
            row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] td img[class='icon']"
        else:
            row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] td"
        source_item=self.driver.find_element_by_css_selector(row_css)
        group_css="#SlicersTab #SlicersCluster_" + str(group_index)
        target_group=self.driver.find_element_by_css_selector(group_css)
        utillityobject.drag_drop_using_uisoup(self, source_item, target_group, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, ty_offset=target_yoff_set, **kwargs)
        time.sleep(10)

    def select_group_slicer_dropdown(self, group_index, item_name):
        """
        params: group_index:1, 2, 3...This will start from 1. and should be integer.
        params: item_name:"COUNTRY" OR "MODEL" OR "Product,Category".
        :Usage: select_group_slicer_dropdown(1, "CAR")
        """
        group_css="#SlicersTab #SlicersCluster_" + str(group_index)
        label_css=group_css + " div[id*='LabelSlicer']"
        x=self.driver.find_elements_by_css_selector(label_css)
        l=[el.text.strip() for el in x]
        combo_id="SlicersCluster_" + str(group_index) + "_Control1Slicer_" + str(l.index(item_name))
        self.driver.find_element_by_css_selector("div[id*=" + combo_id + "] div[id^='BiButton']").click()
        time.sleep(10)
    
    def select_mutiple_slicer_values(self, slicer_values_list):
        """
        Description :  This method used to select slicer value from slicer value box
        Example usage : select_mutiple_slicer_values(['ENGLAND', 'ITALY', 'W GERMANY'])
        """
        scrollable_css = "#filterValuesList .bi-tree-view-body"
        slicer_values_css = "#filterValuesList table tr > td"
        slicer_values_box_obj = self.driver.find_element_by_id('filterValuesList')
        JavaScript.scroll_element(self, scrollable_css, 0, wait_time=2)
        coreutillityobject.python_move_to_element(self, slicer_values_box_obj)
        time.sleep(1)
        if sys.platform == 'linux':
            pass
        else:
            keyboard = Controller()
        for slicer_value in slicer_values_list :
            utillityobject.scroll_down_and_find_item_using_mouse(self, slicer_values_css, slicer_value)
            slicer_values_objs = utillityobject.validate_and_get_webdriver_objects(self, slicer_values_css, "Slicer Values")
            slicer_value_index = JavaScript.find_element_index_by_text(self, slicer_values_objs, slicer_value)
            if slicer_value_index != None :
                if sys.platform == 'linux':
                    pykeyboard.press_key(pykeyboard.control_key)
                    coreutillityobject.python_left_click(self, slicer_values_objs[slicer_value_index], element_location='middle_left', xoffset=20)
                    pykeyboard.release_key(pykeyboard.control_key)
                else:
                    keyboard.press(Key.ctrl)
                    coreutillityobject.python_left_click(self, slicer_values_objs[slicer_value_index], element_location='middle_left', xoffset=20)
                    keyboard.release(Key.ctrl)
            else :
                error_msg = "'{0}' not in slicer values".format(slicer_value)
                raise KeyError(error_msg)
            
    def select_slicer_values_from_single_list(self,combo_item_list):
        """ browser_height=80, source_x=35, source_y=8, 
        combo_item_list = ['ENGLAND', 'ITALY', 'W GERMANY']
        usage: select_slicer_values_from_single_list(combo_item_list)
        """
        
        if Global_variables.browser_name in ['ie', 'edge'] :
            IA_Ribbon.select_mutiple_slicer_values(self, combo_item_list) 
        else :
            if sys.platform == 'linux':
                pass
            else:
                keyboard = Controller()
            menu_items=utillityobject.validate_and_get_webdriver_objects(self, "#filterValuesList table tr > td", 'slicer')
            menu_list = [el.text.strip() for el in menu_items]
            coreutillityobject.python_left_click(self, menu_items[menu_list.index(combo_item_list[0])], element_location='middle_left', xoffset=20)
            if len(combo_item_list)>1:
                for i in range(1, len(combo_item_list)):
                    if sys.platform == 'linux':
                        pykeyboard.press_key(pykeyboard.control_key)
                        coreutillityobject.python_left_click(self, menu_items[menu_list.index(combo_item_list[i])], element_location='middle_left', xoffset=20)
                        pykeyboard.release_key(pykeyboard.control_key)
                    else:
                        keyboard.press(Key.ctrl)
                        coreutillityobject.python_left_click(self, menu_items[menu_list.index(combo_item_list[i])], element_location='middle_left', xoffset=20)
                        keyboard.release(Key.ctrl)

    def select_slicer_values_from_multiple_list(self,combo_item_list,**kwargs):
        """
        combo_item_list = ['ALL STEEL BODY', 'POWER FRONT BRAKES', 'REAR DRUM BRAKES', 'WRAP AROUND BUMPERS']
        usage: select_slicer_values_from_multiple_list(combo_item_list,last_combo_item_no=50)
        """
        if Global_variables.browser_name in ['ie', 'edge'] :
            IA_Ribbon.select_mutiple_slicer_values(self, combo_item_list)
        else :
            if sys.platform == 'linux':
                pass
            else:
                keyboard = Controller()
            keydown=0
            br=utillityobject.get_browser_height(self)
            browser_height=br['browser_height'] 
            for combo_item in combo_item_list:
                get_val=True
                while(get_val):
                    values_elements=self.driver.find_elements_by_css_selector("#filterValuesList table tr > td")
                    value_list=[el.text.strip() for el in values_elements]
                    time.sleep(1)
                    if combo_item in value_list:
                        action1 = ActionChains(self.driver)
                        if combo_item==combo_item_list[0]:
                            if Global_variables.browser_name in ['firefox']:
#                                 x_fr=values_elements[value_list.index(combo_item)].location["x"]
#                                 y_fr=values_elements[value_list.index(combo_item)].location["y"]
#                                 pyautogui.moveTo(x_fr+20,y_fr+browser_height)
#                                 time.sleep(2)
#                                 pyautogui.click(x_fr+20,y_fr+browser_height,button='left')
                                pyautogui.press('down')
                                values_elements=self.driver.find_elements_by_css_selector("#filterValuesList table tr > td")
                                value_list=[el.text.strip() for el in values_elements]
                                coreutillityobject.python_left_click(self, values_elements[value_list.index(combo_item)], element_location='middle_left', xoffset=20)
                            else:
                            #utillityobject.default_left_click(self, object_locator=values_elements[value_list.index(combo_item)],action_move_offset=True,ax_offset=15,ay_offset=8)
                                print(values_elements[value_list.index(combo_item)])
                                print(combo_item)
                                values_elements[value_list.index(combo_item)].click()
#                                 action1.move_to_element_with_offset(values_elements[value_list.index(combo_item)], 15, 8).click().perform()
                        else:
                            time.sleep(2)
                            if Global_variables.browser_name in ['firefox']:
                                x_fr=values_elements[value_list.index(combo_item)].location["x"]
                                y_fr=values_elements[value_list.index(combo_item)].location["y"]
                                pyautogui.moveTo(x_fr+20,y_fr+browser_height)
                                time.sleep(2)
                            else:
                                action1.move_to_element_with_offset(values_elements[value_list.index(combo_item)], 5, 12).perform()
                            time.sleep(1)
                            if sys.platform == 'linux':
                                pykeyboard.press_key(pykeyboard.control_key)
                                pykeyboard.tap_key(pykeyboard.down_key)
                                pykeyboard.release_key(pykeyboard.control_key)
                                coreutillityobject.python_left_click(self, values_elements[value_list.index(combo_item)], element_location='middle_left', xoffset=20)
                            else:
                                keyboard.press(Key.ctrl)
                                keyboard.press(Key.down)
                                keyboard.release(Key.ctrl)
                                #keyboard.press(Key.space)
                                coreutillityobject.python_left_click(self, values_elements[value_list.index(combo_item)], element_location='middle_left', xoffset=20)
                        del action1
                        get_val=False
                        break
                    else:
                        if sys.platform == 'linux':
                            pykeyboard.press_key(pykeyboard.control_key)
                            pykeyboard.tap_key(pykeyboard.down_key)
                            pykeyboard.release_key(pykeyboard.control_key)
                        else:
                            keyboard.press(Key.ctrl)
                            keyboard.press(Key.down)
                            keyboard.release(Key.ctrl)
                        keydown += 1
                        print(keydown)
                        if keydown == kwargs['last_combo_item_no']+1:
                            get_val=False
                        time.sleep(2)
        time.sleep(1)
    
    def close_slicer_dialog(self,btnname):
        """
        usage: close_slicer_dialog('ok') or close_slicer_dialog('cancel')  
        """
        if btnname == 'ok':
            ok_btn_css="[id^='QbSlicerValuesDialog'] #filterValuesOkBtn img"   
            self.driver.find_element_by_css_selector(ok_btn_css).click()
        else:
            cancel_btn_css="[id^='QbSlicerValuesDialog'] #filterValuesCancelBtn img"   
            self.driver.find_element_by_css_selector(cancel_btn_css).click()
        time.sleep(1)  
            
    def drilldown_parameter_popup(self, **kwargs):
        """        
        Usage: create_drilldown_report("report",set_ampersend=True,name_select='DEPARTMENT', type_select='Constant', value_input="MIS", popup_close='ok')
        """
        if 'name_input' in kwargs:
            name_elem=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramValueName input")
            utillityobject.set_text_field_using_actionchains(self, name_elem, kwargs['name_input'])
        if 'name_select' in kwargs:
            name_elem=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramValueName div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self, name_elem, kwargs['name_select'])
        if 'type_input' in kwargs:
            type_elem=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramType input")
            utillityobject.set_text_field_using_actionchains(self, type_elem, kwargs['type_input'])
        if 'type_select' in kwargs:
            type_elem=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramType div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self, type_elem, kwargs['type_select'])
        if 'value_input' in kwargs:
            value_elem=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramValueConst")
            utillityobject.set_text_field_using_actionchains(self, value_elem, kwargs['value_input'])
        if 'value_select' in kwargs:
            value_elem=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramValueField div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self, value_elem, kwargs['value_select'])
        if 'popup_close' in kwargs:
            if kwargs['popup_close']=="ok":
                obj_ok=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramPopupOkBtn img")
                utillityobject.default_left_click(self,object_locator=obj_ok, **kwargs)
            else:
                obj_can=self.driver.find_element_by_css_selector("#drillDownParmPopup #paramPopupCancelBtn img")
                utillityobject.default_left_click(self,object_locator=obj_can, **kwargs)
        time.sleep(2)

            
    def create_drilldown_report(self, drilldown_type, **kwargs):
        """
        params: browse_file_name
        params: verify_left_pane
        params: set_description
        params: set_target
        params: msg
        params: verify_drilldown_type
        params: verify_enabled_left_pane_icons =['create','duplicate','rename','remove','options]
        params: create_new_drilldown
        params: click_ok or delete_all_and_exit or click_cancel
        params: set_ampersand='add' or 'edit' or 'remove'
        params: verify_enabled_parameter_icons = ['add','edit','remove']
        create_drilldown_report("report",set_ampersend='add',name_select='DEPARTMENT', type_select='Constant', value_input="MIS", popup_close='ok')
        create_drilldown_report("webpage", url_value="http://www.yahoo.com", click_ok='yes')
        create_drilldown_report("report",set_ampersand='remove')
        create_drilldown_report("report", verify_input_text=[],verify_enabled_parameter_icons=['add'], click_cancel='yes')
        """
        drilldown_type_radio={'report':'rBtnProc', 'refresh':'rBtnRefreshBIP', 'autolink':'rBtnAutoLink', 'webpage':'rBtnUrl'}
        drilldown_type_radio_css="#" + drilldown_type_radio[drilldown_type] + " > input"
        if 'verify_drilldown_type' in kwargs:
            status=self.driver.find_element_by_css_selector(drilldown_type_radio_css).is_selected()
            utillityobject.asequal(self, True, status, "Step X: Verify drilldown type"+"-drilldown_type")
        self.driver.find_element_by_css_selector(drilldown_type_radio_css).click()
        time.sleep(1)        
        if 'browse_file_name' in kwargs:
            obj_css=self.driver.find_element_by_css_selector("#btnBrowse")
            coreutillityobject.left_click(self, obj_css)
#             utillityobject.default_left_click(self, object_locator=obj_css, **kwargs)
            time.sleep(1)
            utillityobject.ibfs_save_as(self, kwargs['browse_file_name'])
            time.sleep(1)
            x=self.driver.find_element_by_css_selector("#tfTypeComponent input#tfProcedure").get_attribute('value')
            utillityobject.asequal(self, bool(re.match(r".*" + kwargs['browse_file_name'] + ".*", x)), True, "Step X: Verify the fex is selected")
        if 'browse_file_using_path' in kwargs:
            obj_css1=self.driver.find_element_by_css_selector("#btnBrowse")
            coreutillityobject.left_click(self, obj_css1)
#             utillityobject.default_left_click(self, object_locator=obj_css1, **kwargs)
            time.sleep(1)
            utillityobject.select_masterfile_in_open_dialog(self, kwargs['browse_file_using_path'], kwargs['file_name'])
            time.sleep(1)
        if 'url_value' in kwargs:
            element = self.driver.find_element_by_css_selector("input#tfUrl")
            element.clear()
            time.sleep(2)
            element.click()
            time.sleep(2)
            element.send_keys(kwargs['url_value'])
            time.sleep(2)
            element.send_keys(Keys.TAB)
            time.sleep(2)
        if 'rename_drilldown' in kwargs:
            rename_drill =self.driver.find_element_by_css_selector("#drillDownRename img")
            if Global_variables.browser_name in ['firefox']:
                utillityobject.click_type_using_pyautogui(self, rename_drill,leftClick=True, **kwargs)
            else:
                rename_drill.click()
            time.sleep(2)
        if 'set_description' in kwargs:
            element = self.driver.find_element_by_css_selector("input#tfAltComment")
            element.clear()
            time.sleep(2)
            element.click()
            time.sleep(2)
            element.send_keys(kwargs['set_description'])
            time.sleep(2)
            element.send_keys(Keys.TAB)
            time.sleep(2)
        if 'set_target' in kwargs:
            utillityobject.select_combobox_item(self, 'cbTarget', kwargs['set_target'])
            time.sleep(1)
        if 'verify_left_pane' in kwargs:
            btn_css="#drillDownLeftPane #drillDownBtn_" + kwargs['verify_left_pane'][0]
            actual_value=self.driver.find_element_by_css_selector(btn_css).text.strip()
            utillityobject.asequal(self, actual_value, kwargs['verify_left_pane'][1], kwargs['msg'])    
        if 'verify_enabled_left_pane_icons' in kwargs:
            icons_list={'create':'drillDownNew', 'duplicate':'drillDownDuplicate', 'rename':'drillDownRename', 'remove':'drillDownRemove', 'options':'drillDownOptionsTB'}
            for a in kwargs['verify_enabled_left_pane_icons']:
                icons_list_css="#" + icons_list[a] + " div"
                disabled =self.driver.find_element_by_css_selector(icons_list_css).get_attribute('disabled')                
                utillityobject.asequal(self, disabled, None, "StepX: Verify Enabled left pane icons - "+a) 
        if 'create_new_drilldown' in kwargs:
            new_drill =self.driver.find_element_by_css_selector("#drillDownNew img")
            if Global_variables.browser_name in ['firefox']:
                utillityobject.click_type_using_pyautogui(self, new_drill,leftClick=True, **kwargs)
            else:
                new_drill.click()
            time.sleep(2)
        if 'set_ampersand' in kwargs:
            if kwargs['set_ampersand']=='add':
                amper=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #btnNewParam")
                coreutillityobject.left_click(self, amper)
#                 utillityobject.default_left_click(self,object_locator=amper, **kwargs)
                time.sleep(2)
                self.drilldown_parameter_popup(**kwargs)
            if kwargs['set_ampersand']=='edit':
                #Future improve to select 1 or 2nd option
                select=self.driver.find_element_by_css_selector("#gridParams [class*='bi-grid-row grid-row']")
                coreutillityobject.left_click(self, select)
#                 utillityobject.default_left_click(self,object_locator=select[0], **kwargs)
                time.sleep(2)
                amper=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #btnEditParam")
                coreutillityobject.left_click(self, amper)
#                 utillityobject.default_left_click(self,object_locator=amper, **kwargs)
                time.sleep(2)
                self.drilldown_parameter_popup(**kwargs)
            if kwargs['set_ampersand'] =='remove':
                select=self.driver.find_elements_by_css_selector("#gridParams [class*='bi-grid-row grid-row']")
                coreutillityobject.left_click(self, select[0])
#                 utillityobject.default_left_click(self,object_locator=select[0], **kwargs)
                time.sleep(2)
                amper=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #btnDelParam")
                coreutillityobject.left_click(self, amper)
#                 utillityobject.default_left_click(self,object_locator=amper, **kwargs)
                time.sleep(2)
        if 'verify_enabled_parameter_icons' in kwargs:
            par_icons={'add':'btnNewParam', 'edit':'btnEditParam', 'remove':'btnDelParam'}
            for a in kwargs['verify_enabled_parameter_icons']:
                icons_list_css="#" + par_icons[a]
                disabled =self.driver.find_element_by_css_selector(icons_list_css).get_attribute('disabled')                
                utillityobject.asequal(self, disabled, None, "StepX: Verify Enabled parameter icons - "+a) 
        if 'verify_input_text' in kwargs:
            css=("#gridParams [class*='bi-grid-cell grid-cell col']")
            text_obj=[el.text.strip() for el in self.driver.find_elements_by_css_selector(css)]
            print(text_obj)
            utillityobject.as_List_equal(self,text_obj, kwargs['verify_input_text'],"StepX: Verify input text in Parameter")
        if 'click_ok' in kwargs:
            ok_btn_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
            self.driver.find_element_by_css_selector(ok_btn_css).click()
            time.sleep(2)
        if 'click_cancel' in kwargs:
            can_btn_css="div[id^='QbDialog'] div[id^='IABottomBar'] #cancel"
            self.driver.find_element_by_css_selector(can_btn_css).click()
            time.sleep(2)
        if 'delete_all_and_exit' in kwargs:
            delete_btn_css="div[id^='QbDialog'] div[id^='IABottomBar'] #deleteDD"
            self.driver.find_element_by_css_selector(delete_btn_css).click()
            time.sleep(2)
            del_confirm_css="div[id^='BiDialog'] div[id^='BiOptionPane'] div[id^='BiButton']"
            btns=self.driver.find_elements_by_css_selector(del_confirm_css)
            btn_obj="[id^='BiDialog'] [id^='BiOptionPane'] [class*='button-focus']"
            visualization_resultarea.Visualization_Resultarea.wait_for_property(self, btn_obj, 0, string_value='Yes')
            btns[[el.text.strip() for el in btns].index('Yes')].click()
            
    def select_other_chart_type(self, chart_type, Chart_name, chart_index, **kwargs):
        """
        Params: chart_type='bar','line','area','pie','x_y_plots','threed','stock','special','html5','map','html5_extension'.
        Params: Chart_name='vertical_clustered_bars', 'vertical_absolute_line'...(The name displayed when you hover over the chart image, with underscores, check the locator file)
        Params: chart_index=1, 2, 3...
        Params: pg_dn=1, 2, 3...(How many times you make page down)
        Params: starting_visibility_index=0, 1, 2, 3...(The index of the chart image which is visible)
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_clustered_bars', 1,ok_btn_click=True )
        """
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        elem=(By.CSS_SELECTOR, ok_btn_css)
        self._validate_page(elem)
        time.sleep(3)
        chart_type_elem=self.driver.find_element(*IaRibbonLocators.__dict__['select_{0}_chart'.format(chart_type)])
        if Global_variables.browser_name in ['firefox']:
            coreutillityobject.left_click(self, chart_type_elem)
        else:
            chart_type_elem.click()
        time.sleep(3)
        chart_elements=self.driver.find_elements(*IaRibbonLocators.__dict__['{0}_buttons'.format(chart_type)])
        if 'starting_visibility_index' in kwargs:
            chart_elements[kwargs['starting_visibility_index']].click()
        else:
            chart_elements[0].click()
        time.sleep(2)
        elem1=(IaRibbonLocators.__dict__[Chart_name])
        self._validate_page(elem1)
        chart_elem = self.driver.find_element(*IaRibbonLocators.__dict__[Chart_name])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", chart_elem);
        coreutillityobject.left_click(self, chart_elem)
        time.sleep(3)        
        if 'ok_btn_click' in kwargs:
            self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(8)
        
    def verify_check_visible_chart_list(self, expected_visible, msg):
            actual_visible=[]
            chart_elements=self.driver.find_elements(*IaRibbonLocators.__dict__['pie_buttons'])
            for i in range(len(chart_elements)):
                if bool(re.match('.*disabled*.', chart_elements[i].get_attribute("class"))):
                    pass
                else:
                    visible_obj=chart_elements[i].find_element_by_css_selector('img').get_attribute("id").replace('ChartTypeButton_Icon_','')
                    actual_visible.append(visible_obj)
            utillityobject.as_List_equal(self, expected_visible,actual_visible, msg)

    def active_report_options(self, tab_name, **kwargs):
        """
        Params: tab_name = 'General', OR 'Menu Options' OR 'Colors' OR 'Advanced'
        active_report_options('Advanced', advanced_expiration=True, advanced_expirationDateTxtFld='171231', advanced_password='New1', btnOk=True)
        active_report_options('Menu Options',menu_options=True, menu_value='Basic')
        """
        tab_btns=self.driver.find_elements_by_css_selector("#activeReportOptionsLeftContainer  div[class^='bi-tool-bar-button']")
        tab_obj=tab_btns[[el.text.strip() for el in tab_btns].index(tab_name)]
        utillityobject.default_left_click(self, object_locator=tab_obj, **kwargs)
        time.sleep(2)
        if 'general_window' in kwargs:
            general_window_combo_elem=self.driver.find_element_by_css_selector("#generalPane #genWindowCombo [id^='BiButton']")
            utillityobject.select_any_combobox_item(self, general_window_combo_elem, kwargs['general_window'])
        if 'general_freeze_columns' in kwargs:
            general_freeze_columns_combo_elem=self.driver.find_element_by_css_selector("#generalPane #freezeColsCombo [id^='BiButton']")
            utillityobject.select_any_combobox_item(self, general_freeze_columns_combo_elem, kwargs['general_freeze_columns'])
        if 'general_record_per_page' in kwargs:
            general_record_per_page_combo_elem=self.driver.find_element_by_css_selector("#generalPane #recordsPerPageCombo [id^='BiButton']")
            utillityobject.select_any_combobox_item(self, general_record_per_page_combo_elem, kwargs['general_record_per_page'])
        if 'general_display_page_info' in kwargs:
            self.driver.find_element_by_css_selector("#generalPane #displayPageInfoCheckbox input").click()
        if 'general_alignment_left' in kwargs:
            obj_cell_css=self.driver.find_element_by_css_selector("#generalPane #Left img")
            utillityobject.default_left_click(self,object_locator=obj_cell_css, **kwargs)
        if 'general_alignment_center' in kwargs:
            obj_cell_css=self.driver.find_element_by_css_selector("#generalPane #Center img")
            utillityobject.default_left_click(self,object_locator=obj_cell_css, **kwargs)
        if 'general_alignment_right' in kwargs:
            obj_cell_css=self.driver.find_element_by_css_selector("#generalPane #Right img")
            utillityobject.default_left_click(self,object_locator=obj_cell_css, **kwargs)
        if 'general_location' in kwargs:
            general_location_combo_elem=self.driver.find_element_by_css_selector("#generalPane #pageLocationCombo [id^='BiButton']")
            utillityobject.select_any_combobox_item(self, general_location_combo_elem, kwargs['general_location'])
        if 'menu_options' in kwargs:
            if 'menu_value' in kwargs:
                drop_down = self.driver.find_element_by_css_selector('[id="userTypeCombo"] div div[class*="combo-box-arrow"]')
                utillityobject.select_any_combobox_item(self, drop_down, kwargs['menu_value'])
#         self.driver.find_element_by_xpath("//div[contains(text(),'Basic')]").click()
        if 'advanced_rows_retrieved' in kwargs:
            rows_retrieved_combo_elem=self.driver.find_element_by_css_selector("#advancedPane #rowsRetrievedCombo  [id^='BiButton']")
            utillityobject.select_any_combobox_item(self, rows_retrieved_combo_elem, kwargs['advanced_rows_retrieved'])
        if 'advanced_password' in kwargs:
            password_combo_elem=self.driver.find_element_by_css_selector("#advancedPane #advSecurityPassHBox  input")
            utillityobject.set_text_field_using_actionchains(self, password_combo_elem, kwargs['advanced_password'])
        if 'advanced_expiration' in kwargs:
            if kwargs['advanced_expiration']==True:
                status=self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").is_selected()
                utillityobject.asequal(self, False, status, "Step X: Verify Expiration is unchecked previously.")
                self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").click()
                time.sleep(1)
            if kwargs['advanced_expiration']==False:
                status=self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").is_selected()
                utillityobject.asequal(self, True, status, "Step X: Verify Expiration is checked previously.")
                self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").click()
                time.sleep(1)
        if 'advanced_date' in kwargs:
            self.driver.find_element_by_css_selector("#advancedPane #securityDateRadioBtn input").click()
            time.sleep(1)
        if 'advanced_days' in kwargs:
            self.driver.find_element_by_css_selector("#advancedPane #securityDaysRadioBtn input").click()
            time.sleep(1)
        if 'advanced_expirationDateTxtFld' in kwargs:
            expir_DateTxtFld=self.driver.find_element_by_css_selector("#advancedPane #expireComponent input#expirationDateTxtFld")
            utillityobject.set_text_field_using_actionchains(self, expir_DateTxtFld, kwargs['advanced_expirationDateTxtFld'])
            time.sleep(2)
        if 'btnApply' in kwargs:
            self.driver.find_element_by_css_selector("[class*='active window'] #activeReportOptionsApplyBtn img").click()
            time.sleep(1)
        if 'btnCancle' in kwargs:
            self.driver.find_element_by_css_selector("[class*='active window'] #activeReportOptionsCancelBtn img").click()
            time.sleep(1)
        if 'btnOk' in kwargs:
            self.driver.find_element_by_css_selector("[class*='active window'] #activeReportOptionsOkBtn img").click()
            time.sleep(1)
        time.sleep(2)
        
    def dropdown_row_verification(self, property_name, parent_css,  label=None, default_value=None, dropdown_list=None, enable = None, step='X'):
        '''
        Desc: used to verify dropdown value, dropdown_label, dropdown_list,dropdown obj enabled or not
        '''
        property_label = property_name + '_label'
        parent_obj=utillityobject.validate_and_get_webdriver_object(self, parent_css, "Tab obj")
        
        if label:
            observed_text = utillityobject.validate_and_get_webdriver_objects_using_locator(self, IaRibbonLocators.__dict__[property_label] , property_label, parent_obj)
            utillityobject.asequal(label, observed_text.strip(), 'Step {0}: Verify the {1} label'.format(step, property_name))
        if default_value:
            property_value = property_name + '_default_value'
            actual_text=utillityobject.validate_and_get_webdriver_object_using_locator(self, IaRibbonLocators.__dict__[property_value] , property_value, parent_obj)
            actual_text=utillityobject.get_attribute_value(self, actual_text, "text")
            utillityobject.asequal(self, default_value, actual_text["text"].strip(), 'Step {0}: Verify the {1} default value'.format(step, property_name))
        if dropdown_list:
            property_dropdown = property_name + '_dropdown'
            dropdown_obj=utillityobject.validate_and_get_webdriver_object_using_locator(self, IaRibbonLocators.__dict__[property_dropdown], property_dropdown, parent_obj)
            utillityobject.verify_combo_box_item(self, dropdown_list, combobox_dropdown_elem=dropdown_obj, msg='Step {0}: Verify the {1} dropdown value'.format(step, property_name))
            coreutillityobject.left_click(self, dropdown_obj)
        if enable:
            actual_obj=utillityobject.validate_and_get_webdriver_object_using_locator(self, IaRibbonLocators.__dict__[property_label], property_label, parent_obj)
            actual_obj=actual_obj.get_attribute("disabled")
            if enable == True:
                utillityobject.asequal(self, None, actual_obj,'Step {0}: Verify the {1} enabled'.format(step, property_name))
            else:
                utillityobject.asequal(self, 'true', actual_obj, 'Step {0}: Verify the {1} disabled'.format(step, property_name))
        
    def checkbox_verification(self, property_name, parent_css, checked = False, step = 'X'):
        '''
        Desc: used to verify checkbox enabled or not in active report options dialog
        '''
        property_checkbox = property_name + '_checkbox'
        parent_obj=utillityobject.validate_and_get_webdriver_object(self, parent_css, "Tab obj")
        
        actual_obj=utillityobject.validate_and_get_webdriver_object_using_locator(self, IaRibbonLocators.__dict__[property_checkbox], "check", parent_obj)
        actual_obj=actual_obj.get_attribute("checked")
        if checked:
            utillityobject.asequal(self, 'true', actual_obj, 'Step {0}: Verify the {1} checked'.format(step, property_name))
        else:
            utillityobject.asequal(self, None, actual_obj, 'Step {0}: Verify the {1} unchecked'.format(step, property_name))
    
    def alignment_verification(self, parent_css, alignment_property='alignment', value=None, enable=None, step ='X'):
        '''
        Desc: used to verify alignment in active report options dialog
        '''
        alignment_label = alignment_property + '_label'
        parent_obj=utillityobject.validate_and_get_webdriver_object(self, parent_css, "Tab obj")
        observed_text = utillityobject.validate_and_get_webdriver_object_using_locator(self, IaRibbonLocators.__dict__[alignment_label], alignment_label, parent_obj)
        utillityobject.asequal(alignment_property, observed_text.strip(), 'Step {0}: Verify the {1} label'.format(step, alignment_property))
        if value:
            if value == "left":
                left_align=utillityobject.validate_and_get_webdriver_object_using_locator(self, "#Left", "Left alignment is enabled", parent_obj)
                utillityobject.verify_checked_class_property(self, left_align, 'Step {0}: Verify the alignment is {1}'.format(step, value))
            elif value == "center":
                center_align=utillityobject.validate_and_get_webdriver_object_using_locator(self, "#Center", "center alignment is enabled", parent_obj )
                utillityobject.verify_checked_class_property(self, center_align, 'Step {0}: Verify the alignment is {1}'.format(step, value))
            elif value == "right":
                right_align=utillityobject.validate_and_get_webdriver_object_using_locator(self, "#Right", "right alignment is enabled", parent_obj)
                utillityobject.verify_checked_class_property(self, right_align, 'Step {0}: Verify the alignment is {1}'.format(step, value))
        if enable:
            actual_obj=utillityobject.validate_and_get_webdriver_object_using_locator(self, IaRibbonLocators.__dict__[alignment_label], alignment_label, parent_obj)
            actual_obj=actual_obj.get_attribute("disabled")
            if enable ==  True:
                utillityobject.asequal(self, None, actual_obj, 'Step {0}: Verify the {1} enabled'.format(step, alignment_property))
            else:
                
                utillityobject.asequal(self, 'true', actual_obj, 'Step {0}: Verify the {1} disabled'.format(step, alignment_property))    
    
    def verify_active_report_options_general_tab(self, tab_name, msg,**kwargs):
        
        """
        Usage : Function used to verify the dropdown, checkbox and alignment in the General tab of active report options dialog box  
        Params: tab_name = 'General'
        ia_ri_obj.verify_active_report_options_general_tab("General", "Verify active report option",general_alignment="left")
        ia_ri_obj.verify_active_report_options_general_tab("General", "Verify active report option",general_display_page_info="enabled")
        ia_ri_obj.verify_active_report_options_general_tab("General", "Verify active report option",general_window="Cascade")
        """
        
        tab_btns=utillityobject.validate_and_get_webdriver_objects(self, IaRibbonLocators.active_report_option_tabs, "Tabs_list in active report dropdown")
        tab_obj=tab_btns[[el.text.strip() for el in tab_btns].index(tab_name)]
        coreutillityobject.left_click(self, tab_obj)
        if 'general_window' in kwargs:
            actual_text=utillityobject.validate_and_get_webdriver_object(self, IaRibbonLocators.general_window_default_value, "General Window")
            actual_text=utillityobject.get_attribute_value(self, actual_text, "text")
            utillityobject.asequal(self, kwargs["general_window"], actual_text["text"].strip(), msg)
        if 'general_freeze_columns' in kwargs:
            actual_text=utillityobject.validate_and_get_webdriver_object(self, IaRibbonLocators.general_freeze_columns_default_value, "General Freeze Column")
            actual_text=utillityobject.get_attribute_value(self, actual_text, "text")
            utillityobject.asequal(self, kwargs["general_freeze_columns"], actual_text["text"].strip(), msg)
        if 'general_record_per_page' in kwargs:
            actual_text=utillityobject.validate_and_get_webdriver_object(self, IaRibbonLocators.general_records_per_page_default_value, "General Records Per Page")
            actual_text=utillityobject.get_attribute_value(self, actual_text, "value")
            utillityobject.asequal(self, kwargs["general_record_per_page"], actual_text["value"].strip(), msg)
        if 'general_display_page_info' in kwargs:
            if kwargs["general_display_page_info"]=="disabled":
                actual_obj=utillityobject.validate_and_get_webdriver_object(self, "#generalPane #pageInfoPropsBox", "general_display_page_info is disabled")
                actual_obj=actual_obj.get_attribute("disabled")
                utillityobject.asequal(self, 'true', actual_obj, "Step x : Display page info is disabled")
            if kwargs["general_display_page_info"]=="enabled":
                actual_obj=utillityobject.validate_and_get_webdriver_object(self, "#displayPageInfoCheckbox [type*='checkbox']", "general_display_page_info is enabled")
                actual_obj=actual_obj.get_attribute("checked")
                utillityobject.asequal(self, 'true', actual_obj, "Step x : Display page info is enabled")
        if 'general_alignment' in kwargs:
            if kwargs['general_alignment'] == "left":
                left_align=utillityobject.validate_and_get_webdriver_object(self, IaRibbonLocators.alignment_left, "Left alignment is enabled")
                utillityobject.verify_checked_class_property(self, left_align, "Step x : verify left alignment is enabled")
            if kwargs['general_alignment'] == "center":
                center_align=utillityobject.validate_and_get_webdriver_object(self, IaRibbonLocators.alignment_center, "center alignment is enabled")
                utillityobject.verify_checked_class_property(self, center_align, "Step x : verify center alignment is enabled")
            if kwargs['general_alignment'] == "right":
                right_align=utillityobject.validate_and_get_webdriver_object(self, IaRibbonLocators.alignment_right, "right alignment is enabled")
                utillityobject.verify_checked_class_property(self, right_align, "Step x : verify right alignment is enabled")
        if 'general_location' in kwargs:
            actual_text=utillityobject.validate_and_get_webdriver_object(self, "#generalPane #pageLocationCombo input", "General Location")
            actual_text=utillityobject.get_attribute_value(self, actual_text, "text")
            utillityobject.asequal(self, kwargs["general_location"], actual_text["text"].strip(), msg)
            
    def verify_active_report_options_dropdown_list(self, exp_list, dropdown_css, dropdown_name=None):
        
        """
        Usage : Function used to verify the dropdown list of active report options  
        Params: exp_list=["Cascade", "Tabs"], dropdown_css="#generalPane #genWindowCombo [id^='BiButton']", 
        ia_ri_obj.verify_active_report_options_dropdown_list(["Cascade","Tabs"], "#generalPane #genWindowCombo [id^='BiButton']", "General Window")
        """
        dropdown_obj=utillityobject.validate_and_get_webdriver_object(self, dropdown_css, dropdown_name)
        utillityobject.verify_combo_box_item(self, exp_list, combobox_dropdown_elem=dropdown_obj, msg="Step X")
        coreutillityobject.left_click(self, dropdown_obj)
        
    def select_frame_background_options(self, tab_name, **kwargs):
        """
        Params: tab_name = 'Frame', OR 'Frame Edge' OR 'Background'
        select_frame_background_options('Frame', depth_angle='45', depth_radius='17', advanced_password='New1', btnOk=True)
        select_frame_background_options('Menu Options',menu_options=True, menu_value='Basic')
        """
        tab_btns=self.driver.find_elements_by_css_selector("[class*='active'] #frameLeftContainer div[class^='bi-tool-bar-button']")
        tab_obj=tab_btns[[el.text.strip() for el in tab_btns].index(tab_name)]
        coreutillityobject.left_click(self, web_element=tab_obj)
        time.sleep(2)
        '''Frame'''
        if 'depth_angle' in kwargs:
            depth_angle_elem=self.driver.find_element_by_css_selector("#frameOptionsPane input#depthAngleValue")
            utillityobject.set_text_field_using_actionchains(self, depth_angle_elem, kwargs['depth_angle'], **kwargs)
        if 'depth_radius' in kwargs:
            depth_radius_elem=self.driver.find_element_by_css_selector("#frameOptionsPane input#depthRadiusValue")
            utillityobject.set_text_field_using_actionchains(self, depth_radius_elem, kwargs['depth_radius'], **kwargs)
        if 'no_fill' in kwargs:
            no_fill_elem=self.driver.find_element_by_css_selector("#frameOptionsPane #frameTwoDFillTypeNone input[id^='BiRadioButton']")
            coreutillityobject.left_click(self, web_element=no_fill_elem)
        if 'solid_fill' in kwargs:
            solid_fill_elem=self.driver.find_element_by_css_selector("#frameOptionsPane #frameTwoDFillTypeColor input[id^='BiRadioButton']")
            coreutillityobject.left_click(self, web_element=solid_fill_elem)
        if 'gradient_fill' in kwargs:
            gradient_fill_elem=self.driver.find_element_by_css_selector("#frameOptionsPane #frameTwoDFillTypeGradient input[id^='BiRadioButton']")
            coreutillityobject.left_click(self, web_element=gradient_fill_elem)
        if 'direction' in kwargs:
            direction_elem=self.driver.find_element_by_css_selector("#frameOptionsPane #frameGradientDirectionComboBox [class*='bi-button']")
            utillityobject.select_any_combobox_item(self, direction_elem, kwargs['direction'], **kwargs)
        if 'show_shadow' in kwargs:
            show_shadow_elem=self.driver.find_element_by_css_selector("#frameOptionsPane #frameShowShadowCheckBox input[id^='BiCheckBox']")
            coreutillityobject.left_click(self, web_element=show_shadow_elem)
        '''Background'''
        if 'show_border_color' in kwargs:
            show_border_color_elem=self.driver.find_element_by_css_selector("#backgroundOptionsPane #backgroundBorderColorCheckBox input[id^='BiCheckBox']")
            coreutillityobject.left_click(self, web_element=show_border_color_elem)
        if 'border_color' in kwargs:
            border_color_elem=self.driver.find_element_by_css_selector("#backgroundOptionsPane #backgroundBorderColorBtn img")
            coreutillityobject.left_click(self, web_element=border_color_elem)
            ia_styling.IA_Style.set_color(self, kwargs['border_color'])
        if 'btnApply' in kwargs:
            self.driver.find_element_by_css_selector("[class*='active window'] #frameApplyBtn img").click()
            time.sleep(1)
        if 'btnCancle' in kwargs:
            self.driver.find_element_by_css_selector("[class*='active window'] #frameCancelBtn img").click()
            time.sleep(1)
        if 'btnOk' in kwargs:
            self.driver.find_element_by_css_selector("[class*='active window'] #frameOkBtn img").click()
            time.sleep(1)
        time.sleep(2)
        
    
    def select_or_verify_output_type(self,**kwargs):
            
        """
        launch_point="Home" Or "bottom_tool_bar"
        item_select_path='Excel (xlsx)->Excel Formula (xlsx)'
        expected_output_list1=['HTML', 'Active Report', 'PDF', 'Excel (xlsx)', 'PowerPoint (pptx)']
        expected_output_list2=['Excel (xlsx)', 'Excel', 'Excel Formula (xlsx)', 'Excel Formula']
        msg1="Step X: Verify all output types are displaying."
        msg2="Step X: Verify all output sub_types are displaying."
        
        usage 1 :  select_or_verify_output_type(launch_point='Home',selected_format='HTML',item_select_path='Excel (xlsx)->Excel Formula (xlsx)',expected_output_list1=list1,expected_output_list2=list2,msg1="Verify X",msg2="Verify X") 
        usage 2 :  select_or_verify_output_type(launch_point='Home',item_select_path='Excel (xlsx)',expected_output_list1=list1,msg1="Verify X")     
        usage 3 :  select_or_verify_output_type(launch_point='Home',item_select_path='PDF')
   
        """
        
        if kwargs['launch_point']=='Home':
            visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
            visual_ribbonobj.select_ribbon_item('Home', 'format_type')
        else:
            bottom_tool_bar=self.driver.find_element_by_css_selector("#sbpOutputFormatPanel div[class$='drop-down-arrow']")
            utillityobject.default_left_click(self,object_locator=bottom_tool_bar, **kwargs)    
        time.sleep(2)
        bipopup_css="div[class='bi-popup'][style*='inherit']"
        bipopups=self.driver.find_elements_by_css_selector(bipopup_css)
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector("div[id^='menu_'][class*='tool-bar-split-menu']")
        time.sleep(2)
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        if 'expected_output_list' in kwargs:
            flag=True
            for item in kwargs['expected_output_list']:
                if item in actual_popup_list:
                    flag=True
                else:
                    flag=False
                    break
            utillityobject.asequal(self,flag, True,kwargs['msg'])
        if 'expected_output_list1' in kwargs:
            print("Actual output formats : ",actual_popup_list)
            utillityobject.as_List_equal(self,kwargs['expected_output_list1'], actual_popup_list,kwargs['msg1'])
        if 'item_select_path' in kwargs:
            items=kwargs['item_select_path'].split("->")
            if len(items)==1:
                menu_item=menu_items[actual_popup_list.index(items[0])]
                utillityobject.default_left_click(self,object_locator=menu_item, **kwargs)
                time.sleep(2)
            else:    
                menu_arrow=menu_items[actual_popup_list.index(items[0])].find_element_by_css_selector("div[id*='toolbarBtn']")
                utillityobject.default_left_click(self,object_locator=menu_arrow, **kwargs)
                time.sleep(2)
                bipopups=self.driver.find_elements_by_css_selector(bipopup_css)
                menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector("div[id^='menu_'][class*='tool-bar-split-menu']")
                time.sleep(2)
                actual_popup_list=[el.text.strip() for el in menu_items if bool(re.match('\S+', el.text.strip()))]
               
                if 'expected_output_list2' in kwargs:
                    print("Actual sub types output formats : ", actual_popup_list)
                    utillityobject.as_List_equal(self,kwargs['expected_output_list2'], actual_popup_list,kwargs['msg2'])
                sub_menu=menu_items[actual_popup_list.index(items[1])]
                utillityobject.default_left_click(self,object_locator=sub_menu, **kwargs)
                time.sleep(2)
                
    def verify_output_format(self, expected_format, msg="Step x"):
        '''
        Desc : Function to verify the output format
        usage: ia_ribbon_obj.verify_output_format("Active PDF", msg="Step 1")
        '''
        actual_format=utillityobject.validate_and_get_webdriver_object(self, IaRibbonLocators.output_format, "Output Format").text.strip()
        utillityobject.asequal(self,expected_format,actual_format,"{0} : Verify the output format".format(msg)) 
                   
    def select_report_output_window(self, output_window_name, **kwargs):
        """
        @Param: output_window_name: 'Single Window'
        @Usage: select_report_output_window('Single Window')
        """
        elem=self.driver.find_element_by_css_selector("#sbpTargetOutputPanel")
        elem.click()
        time.sleep(1)
        utillityobject.select_or_verify_bipop_menu(self, output_window_name,**kwargs)
        time.sleep(5)
         
    def select_buttons_in_add_slicer_dialog(self, btn_name):
        """
        @Param : btn_name = "Ok" or "Cancel"
        @Usage : add_slicer("Ok")
        """
        css="#addSlicerDlg [class*='active'][class*='window']"
        status=self.driver.find_element_by_css_selector(css).is_displayed()
        utillityobject.asequal(self, True, status , 'Step X : Verify add slicer dialog is displayed')
        btn_css=css+ " #addSlicer"+btn_name+"Btn"
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(2)

    def set_record_limit_homepage(self,record_limits):
        '''
        Descriptions : Type record limits in home page
        :param : record_limits=15 or etc 
        :usage : set_record_limit_homepage(200)
        '''
        visualization_ribbon.Visualization_Ribbon.switch_ia_tab(self,'Home')
        time.sleep(2)
        record_css="#HomeRecordLimit input[id^='BiTextField']"
        record=self.driver.find_element_by_css_selector(record_css)
        utillityobject.click_on_screen(self, record,'middle',0)
        record.clear()
        time.sleep(1)
        record.send_keys(record_limits)
        time.sleep(2)
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard.press_and_release('enter')
        time.sleep(2)
    
    def set_record_limits(self,mode,record_limits):
        '''
        Descriptions : Type record limits for preview or run mode to display limited reports
        :param : mode ='Preview' or 'RunTime' 
        :param : record_limits=15 or etc 
        :usage : set_record_limits('RunTime',15) or set_record_limits('Preview',15)
        '''
        visualization_ribbon.Visualization_Ribbon.switch_ia_tab(self,'Slicers')
        time.sleep(2)
        mode_css="#Slicers{0}ComboBox input".format(mode)
        mode=self.driver.find_element_by_css_selector(mode_css)
        utillityobject.click_on_screen(self, mode,'middle',0)
        mode.clear()
        time.sleep(1)
        mode.send_keys(record_limits)
        time.sleep(2)
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard.press_and_release('enter')
        time.sleep(2)
    
    def select_hold_format_type(self,hold_format_type,**kwargs):
        '''
        Descriptions : Select file format to create hold  (examples : Create Report,Create Chart, Create Document)
        :param : hold_format_type =' Create Report'
        :usage : select_hold_format_type('Create Report')
        '''
        utillityobject.synchronize_with_number_of_element(self, "#holdDockPane #createFromHoldMenuBtn", 1, 90)
        time.sleep(2)
        menu_btn=self.driver.find_element_by_css_selector("#holdDockPane #createFromHoldMenuBtn")
        utillityobject.default_left_click(self, object_locator=menu_btn, **kwargs)
        time.sleep(3)
        utillityobject.select_or_verify_bipop_menu(self,hold_format_type,**kwargs)
    
    def procedure_setting_dialogverify(self, bihbox_item_name, input_control, expected_visible_symbol_or_text, msg, position=1):
        '''
        :usage = procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 07.5 : Verify Decimal Notation OFF is selected',2)
        '''
        rows=self.driver.find_elements_by_css_selector("[id^='QbSetEnvParametersDlg'] [id^='BiHBox']")
        for row in rows:
            if bihbox_item_name in row.text.split('\n'):
                current_obj=row
                if input_control in ('checkbox'):
                    expected_status = True if expected_visible_symbol_or_text == 'checked' else False
                    total_check_box=current_obj.find_elements_by_css_selector("input[type='checkbox']")
                    actual_status=total_check_box[position-1].is_selected()
                    utillityobject.asequal(self, expected_status, actual_status, msg)
                if input_control in ('radiobutton'):
                    expected_status = True if expected_visible_symbol_or_text == 'checked' else False
                    total_check_box=current_obj.find_elements_by_css_selector("input[type='radio']")
                    actual_status=total_check_box[position-1].is_selected()
                    utillityobject.asequal(self, expected_status, actual_status, msg)
                if input_control == 'combobox':
                    actual_visible_symbol_or_text=current_obj.find_element_by_css_selector("[class^='bi-combo-box']").text.strip()
                    utillityobject.asequal(self, expected_visible_symbol_or_text, actual_visible_symbol_or_text, msg)
                if input_control == 'textbox':
                    actual_visible_symbol_or_text=current_obj.find_element_by_css_selector("[class*='bi-text-field']").get_attribute("value")
                    utillityobject.asequal(self, expected_visible_symbol_or_text, actual_visible_symbol_or_text, msg)
                break
    
    def procedure_setting_dialog_input(self, bihbox_item_name, input_control, input_symbol_or_item_or_text, position=1, **kwargs):
        '''
        input_symbol_or_item_or_text='checked' OR 'uncheck' OR combo item value, OR text box value
        '''
        rows=self.driver.find_elements_by_css_selector("[id^='QbSetEnvParametersDlg'] [id^='BiHBox']")
        for row in rows:
            if bihbox_item_name in row.text.split('\n'):
                current_obj=row
                if input_control in ('checkbox'):
                    expected_status = True if input_symbol_or_item_or_text == 'checked' else False
                    total_check_box=current_obj.find_elements_by_css_selector("input[type='checkbox']")
                    actual_status=total_check_box[position-1].is_selected()
                    utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify before selecting checkbox.")
                    utillityobject.click_on_screen(self,total_check_box[position-1], "middle", click_type=0)
                if input_control in ('radiobutton'):
                    expected_status = True if input_symbol_or_item_or_text == 'checked' else False
                    total_check_box=current_obj.find_elements_by_css_selector("input[type='radio']")
                    actual_status=total_check_box[position-1].is_selected()
                    utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify before selecting radio button.")
                    utillityobject.click_on_screen(self,total_check_box[position-1], "middle", click_type=0)
                if input_control == 'combobox':
                    elem=current_obj.find_element_by_css_selector("[class^='bi-combo-box'] div[id^='BiButton']")
                    utillityobject.select_any_combobox_item(self, elem, input_symbol_or_item_or_text,**kwargs)
                if input_control == 'textbox':
                    elem=current_obj.find_element_by_css_selector("[class*='bi-text-field']")
                    utillityobject.set_text_field_using_actionchains(self, elem, input_symbol_or_item_or_text)
                break
        time.sleep(2)

    def procedure_setting_dialog_dismiss(self, button_name):
        '''
        button_name='OK' OR 'Reset' OR 'Cancel'
        '''
        btn_index={'OK':0, 'Reset':1, 'Cancel':2}
        button=int(btn_index[button_name])
        buttons=self.driver.find_elements_by_css_selector("[id^='QbSetEnvParametersDlg'] [id^='IABottomBar'] [class^='bi-button button']")
        utillityobject.click_on_screen(self,buttons[button], "middle", click_type=0, pause=1)
        
    def set_format_vertical_axis_scale(self, input_control_type, input_control_name, input_control_value, synchronize_timeout=90):
        '''
        @param : input_control_type=checkbox Or textbox
        @param : input_control_value='check' OR 'uncheck', OR any text
        @usgae : set_format_vertical_scale('textbox','automatic_minimum','3000')
        '''
        checkbox_objects={'automatic_minimum':' #scalePane #autoMinCheckBox input', 
                            'automatic_maximum':' #scalePane #autoMaxCheckBox input', 
                            'automatic_grid_step':' #scalePane #autoGridStepCheckBox input', 
                            'logarithmic_scale':' #scalePane #logScaleCheckBox input',
                            'include_zero_on_scale':' #scalePane #includeZeroCheckBox input'}
        textbox_objects={'minimum_value':' #scalePane input#minValueField', 
                         'maximum_value':' #scalePane input#maxValueField', 
                         'grid_step_value':' #scalePane input#gridStepField'}
        parent_css="[id^='QbDialog'] [class*='active'] #axesSplitPane"
        scale_css="#leftPane #scaleOptions"
        right_pane_css="#rightPane"
        utillityobject.synchronize_with_visble_text(self, parent_css + " " + scale_css, 'Scale', synchronize_timeout)
        label_elem=self.driver.find_element_by_css_selector(parent_css + " " + scale_css)
        coreutillityobject.left_click(self, label_elem)
        time.sleep(2)
        right_pane_obj=self.driver.find_element_by_css_selector(parent_css + " " + right_pane_css)
        if input_control_type=='checkbox':
            elem=right_pane_obj.find_element_by_css_selector(checkbox_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify Checkbox status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
        if input_control_type=='textbox':
            elem=right_pane_obj.find_element_by_css_selector(textbox_objects[input_control_name])
            utillityobject.set_text_field_using_actionchains(self, elem, input_control_value)
            
    def set_format_horizontal_axis_labels(self, input_control_type, input_control_name, input_control_value, synchronize_timeout=90):
        '''
        @param : input_control_type=checkbox Or textbox
        @param : input_control_value='check' OR 'uncheck', OR any text
        @Usage : set-format_horizontal_axis_labels('checckbox','show_labels','check')
        '''
        checkbox_objects={'show_labels':" #labelsPane:not([style*='hidden']) #showLabelsCheckBox input", 
                            'stagger_labels':" #labelsPane:not([style*='hidden']) #staggerLabelsCheckBox input", 
                            'concatenate_labels':" #labelsPane:not([style*='hidden']) #concatenateLabelsCheckBox input"}
        combobox_objects={'axis_side':" #labelsPane:not([style*='hidden']) #axisSideHorizComboBox_MOONBEAM > [id^='BiButton']"}
        styleimage_objects={'style_labels':"#labelsPane:not([style*='hidden']) #labelsStyleBtn img"}
        
        parent_css="[id^='QbDialog']:not([style*='hidden']) #axesSplitPane"
        labels_css="#leftPane #labelsOptions"
        right_pane_css="#rightPane"
        utillityobject.synchronize_with_visble_text(self, parent_css + " " + labels_css, 'Labels', synchronize_timeout)
        label_elem=self.driver.find_element_by_css_selector(parent_css + " " + labels_css)
        coreutillityobject.left_click(self, label_elem)
        time.sleep(2)
        right_pane_obj=self.driver.find_element_by_css_selector(parent_css + " " + right_pane_css)
        if input_control_type=='checkbox':
            elem=right_pane_obj.find_element_by_css_selector(checkbox_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify Checkbox status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
            
        if input_control_type=='combobox':
            elem=right_pane_obj.find_element_by_css_selector(combobox_objects[input_control_name])
            utillityobject.select_any_combobox_item(self, elem, input_control_value)
        if input_control_type=='styleimage_objects':
            elem=right_pane_obj.find_element_by_css_selector(styleimage_objects[input_control_name])
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
            
    def set_format_horizontal_grid_lines_major(self, input_control_type, input_control_name, input_control_value, synchronize_timeout=90):
        '''
        @param : input_control_type=checkbox Or textbox
        @param : input_control_value='check' OR 'uncheck', OR any text
        @Usage : set-format_horizontal_axis_labels('checckbox','show_labels','check')
        '''
        checkbox_objects={'show_grid_lines':" #majorGridLineOptionsPane #showMajorGridLinesCheckBox input", 
                            'show_ticks':" #majorGridLineOptionsPane #majorGridLinesTicksCheckBox input"}
        combobox_objects={'tick_style':" #majorGridLineOptionsPane #majorTickStyleComboBox > [id^='BiButton']"}
        styleimage_objects={'style_button_1':"#majorGridLineOptionsPane #majorGridLineStyleColorBtn img",
                            'style_button_2':'#majorGridLineOptionsPane #majorTickLineStyleBtn img'}
        
        parent_css="[id^='QbDialog'] [class*='active'] #gridLinesSplitPane"
        major_css="#leftPane #majorGridLineOptions"
        right_pane_css="#rightPane"
        utillityobject.synchronize_with_visble_text(self, parent_css + " " + major_css, 'Major Grid Lines', synchronize_timeout)
        major_grid_lines_elem=self.driver.find_element_by_css_selector(parent_css + " " + major_css)
        coreutillityobject.left_click(self, major_grid_lines_elem)
        time.sleep(2)
        right_pane_obj=self.driver.find_element_by_css_selector(parent_css + " " + right_pane_css)
        if input_control_type=='checkbox':
            elem=right_pane_obj.find_element_by_css_selector(checkbox_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify Checkbox status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
            
        if input_control_type=='combobox':
            elem=right_pane_obj.find_element_by_css_selector(combobox_objects[input_control_name])
            utillityobject.select_any_combobox_item(self, elem, input_control_value)
        if input_control_type=='styleimage_objects':
            elem=right_pane_obj.find_element_by_css_selector(styleimage_objects[input_control_name])
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)  
    
    def set_format_vertical_grid_lines_major(self, input_control_type, input_control_name, input_control_value, synchronize_timeout=90):
        '''
        @param : input_control_type=checkbox Or textbox
        @param : input_control_value='check' OR 'uncheck', OR any text or None
        @Usage : set-format_horizontal_axis_labels('checckbox','show_labels','check')
        '''
        checkbox_objects={'show_grid_lines':" #majorGridLineOptionsPane #showMajorGridLinesCheckBox input", 
                            'show_ticks':" #majorGridLineOptionsPane #majorGridLinesTicksCheckBox input"}
        combobox_objects={'tick_style':" #majorGridLineOptionsPane #majorTickStyleComboBox > [id^='BiButton']"}
        styleimage_objects={'style_button_1':"#majorGridLineOptionsPane #majorGridLineStyleColorBtn img",
                            'style_button_2':'#majorGridLineOptionsPane #majorTickLineStyleBtn img'}
        
        parent_css="[id^='QbDialog'] [class*='active'] #gridLinesSplitPane"
        major_css="#leftPane #majorGridLineOptions"
        right_pane_css="#rightPane"
        utillityobject.synchronize_with_visble_text(self, parent_css + " " + major_css, 'Major Grid Lines', synchronize_timeout)
        major_grid_lines_elem=self.driver.find_element_by_css_selector(parent_css + " " + major_css)
        coreutillityobject.left_click(self, major_grid_lines_elem)
        time.sleep(2)
        right_pane_obj=self.driver.find_element_by_css_selector(parent_css + " " + right_pane_css)
        if input_control_type=='checkbox':
            elem=right_pane_obj.find_element_by_css_selector(checkbox_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify Checkbox status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
            
        if input_control_type=='combobox':
            elem=right_pane_obj.find_element_by_css_selector(combobox_objects[input_control_name])
            utillityobject.select_any_combobox_item(self, elem, input_control_value)
        if input_control_type=='styleimage_objects':
            elem=right_pane_obj.find_element_by_css_selector(styleimage_objects[input_control_name])
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
            
    def set_format_frame_and_background(self, input_control_type, input_control_name, input_control_value, synchronize_timeout=90):
        '''
        @param : input_control_type=checkbox Or textbox
        @param : input_control_value='check' OR 'uncheck', OR any text
        @Usage : set-format_horizontal_axis_labels('checckbox','show_labels','check')
        '''
        checkbox_objects={'show_shadow':" #frameOptionsPane #frameShowShadowCheckBox input"}
        textbox_objects={'depth_angle':" #frameOptionsPane input#depthAngleValue",
                         'depth_radius':" #frameOptionsPane input#depthRadiusValue",
                         'depth_radius':" #frameOptionsPane #frameFillColorTransparencySpinner input"}
        radiobutton_objects={'no_fill':"#frameOptionsPane #frameTwoDFillTypeNone input[type='radio']",
                            'solid_fill':"#frameOptionsPane #frameTwoDFillTypeColor input[type='radio']",
                            'gradient_fill':"#frameOptionsPane #frameTwoDFillTypeGradient input[type='radio']"}
        styleimage_objects={'style_button':"#frameOptionsPane #frameFillSwatch img",
                            'first_color':"#frameOptionsPane #frameGradientSwatch1 img",
                            'second_color':"#frameOptionsPane #frameGradientSwatch2 img"}
        
        parent_css="[id^='QbDialog'] [class*='active'] #frameSplitPane"
        frame_css="#leftPane #frameOptionsBtn"
        right_pane_css="#rightPane"
        utillityobject.synchronize_with_visble_text(self, parent_css + " " + frame_css, 'Frame', synchronize_timeout)
        frame_elem=self.driver.find_element_by_css_selector(parent_css + " " + frame_css)
        coreutillityobject.left_click(self, frame_elem)
        time.sleep(2)
        right_pane_obj=self.driver.find_element_by_css_selector(parent_css + " " + right_pane_css)
        if input_control_type == 'checkbox':
            elem=right_pane_obj.find_element_by_css_selector(checkbox_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify Checkbox status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
        if input_control_type == 'radiobutton':
            elem=right_pane_obj.find_element_by_css_selector(radiobutton_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify radio button status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
        if input_control_type=='textbox':
            elem=right_pane_obj.find_element_by_css_selector(textbox_objects[input_control_name])
            utillityobject.set_text_field_using_actionchains(self, elem, input_control_value)
        if input_control_type=='styleimage_objects':
            elem=right_pane_obj.find_element_by_css_selector(styleimage_objects[input_control_name])
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1) 
            
    def select_infomini_option(self, options_list, popup_table_css='table tr'):
        """
        This Function is used to select Info_mini options.
        :Param options_list = ['Series Tab', 'Resources/Field Tab']
        :Param popup_table_css='table tr'
        :Usage select_infomini_option(['Series Tab', 'Resources/Field Tab'], popup_table_css='table tr')
        """
        visualization_ribbon.Visualization_Ribbon.switch_ia_tab(self, "Format")
        for item in options_list:
            button_name = 'format_infomini_arrow'
            ribbon_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__[button_name])
            utillityobject.default_left_click(self, object_locator=ribbon_item)
            visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "[id*='BiPopup'][class*='menu']", 1, expire_time=15)
            bipopup_css="div[id^='BiPopup'][style*='inherit']"
            bipopups=self.driver.find_elements_by_css_selector(bipopup_css)
            menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector(popup_table_css)
            actual_popup_list=[el.text.strip() for el in menu_items]
            menu_items[actual_popup_list.index(item)].click()
            time.sleep(1)        
        time.sleep(0.5)
    
    def verify_infomini_option(self, expected_list, msg, popup_table_css='table tr'):
        """
        This Function is used to verify Info_mini options.
        :Param option = 'Series Tab'
        :Param expected_list = ['Series Tab']
        :Param msg = "Step 7: Verify infomini option"
        :Param popup_table_css='table tr'
        :Usage verify_infomini_option('Series Tab', ['Series Tab'], "Step 7: Verify infomini option", popup_table_css='table tr')
        """
        visualization_ribbon.Visualization_Ribbon.select_ribbon_item(self, "Format", "Infomini_arrow")
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "[id*='BiPopup'][class*='menu']", 1, expire_time=15)
        bipopup_css="div[id^='BiPopup'][style*='inherit']"
        bipopups=self.driver.find_elements_by_css_selector(bipopup_css)
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector(popup_table_css)
        time.sleep(2)
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        utillityobject.as_List_equal(self, expected_list, actual_popup_list, msg)
        time.sleep(0.5)
        
    def set_format_labels_general(self, input_control_type, input_control_name, input_control_value, **kwargs):
        '''
        @param : input_control_type=checkbox Or textbox
        @param : input_control_value='check' OR 'uncheck', OR any text
        @Usage : set-format_horizontal_axis_labels('checckbox','show_labels','check')
        '''
        checkbox_objects={'show_data_label':" #generalBLAPane #generalBLAshowDataLabelsCheckBox input",
                          'show_cumulative_sums':" #generalBLAPane #generalStackedShowCumulativeSumCheckBox input",
                          'show_stacked_total':" #generalStackedPane #stackedShowTotalCheckBox input"}
        textbox_objects={'custom_format':" #generalBLAPane input#generalBLAcustomDataLabelTextField"}
        combobox_objects={'position':"#generalBLAPane #generalBLApositionDataLabelComboBox_MOONBEAM  > [id^='BiButton']",
                          'format_labels':"#generalBLAPane #generalBLAformatDataLabelsComboBox  > [id^='BiButton']"}
        styleimage_objects={'style_button':"#generalBLAPane #generalBLAdataLabelsStyleColorBtn img"}
        
        parent_css="[id^='QbDialog'] [class*='active'] #dataLabelSplitPane"
        general_option_css="#leftPane [id^='general'][class*='tool-bar-button']"
        right_pane_css="#rightPane"
        self.driver.find_element_by_css_selector(parent_css + " " + general_option_css).click()
        time.sleep(2)
        right_pane_obj=self.driver.find_element_by_css_selector(parent_css + " " + right_pane_css)
        if input_control_type == 'checkbox':
            elem=right_pane_obj.find_element_by_css_selector(checkbox_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify Checkbox status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
        if input_control_type=='combobox':
            elem=right_pane_obj.find_element_by_css_selector(combobox_objects[input_control_name])
            utillityobject.select_any_combobox_item(self, elem, input_control_value)
        if input_control_type=='textbox':
            elem=right_pane_obj.find_element_by_css_selector(textbox_objects[input_control_name])
            utillityobject.set_text_field_using_actionchains(self, elem, input_control_value)
        if input_control_type=='styleimage_objects':
            elem=right_pane_obj.find_element_by_css_selector(styleimage_objects[input_control_name])
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
        if 'ok_btn' in kwargs:
            ok_btn_css = self.driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='dataLabelsOkBtn']")
            utillityobject.click_on_screen(self, ok_btn_css, "middle", click_type=0, pause=1)
            
    def set_password_active_report_options(self, input_control_type, input_control_name, input_control_value):
        '''
        @param : input_control_type=checkbox Or textbox
        @param : input_control_value='check' OR 'uncheck', OR any text
        @Usage : set-format_horizontal_axis_labels('checckbox','show_labels','check')
        '''
        checkbox_objects={'password_expiration':"#advancedPane #securityExpirationCheckBox input"}
        textbox_objects={'password_field':"#advancedPane #securityPasswordFld",
                         'expire_date':"#advancedPane #expirationDateTxtFld",
                         'expire_days':"#advancedPane #expirationDaysSpinner input"}
        radiobutton_objects={'date_selection':"#advancedPane #securityDateRadioBtn input[type='radio']",
                            'days_selection':"#advancedPane #securityDaysRadioBtn input[type='radio']"}
                            
        button_objects={'ok_button':"[id^='QbDialog'] #activeReportOptionsOkBtn",
                        'cancel_button':"[id^='QbDialog'] #activeReportOptionsCancelBtn",
                        'apply_button':"[id^='QbDialog'] #activeReportOptionsApplyBtn"}
        
        parent_css="[id^='QbDialog'] #activeReportOptionsSplitPane"
        frame_css="#activeReportOptionsLeftPane #activeReportStyleAdvanced"
        right_pane_css="#activeReportOptionsRightPane"
        elem=self.driver.find_element_by_css_selector(parent_css + " " + frame_css)
        coreutillityobject.left_click(self, elem)
        time.sleep(2)
        right_pane_obj=self.driver.find_element_by_css_selector(parent_css + " " + right_pane_css)
        if input_control_type == 'checkbox':
            elem=right_pane_obj.find_element_by_css_selector(checkbox_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify Checkbox status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
        if input_control_type == 'radiobutton':
            elem=right_pane_obj.find_element_by_css_selector(radiobutton_objects[input_control_name])
            expected_status = True if input_control_value == 'check' else False
            actual_status=elem.is_selected()
            utillityobject.asequal(self, expected_status, actual_status, "Step X: Verify radio button status before click.")
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
        if input_control_type=='textbox':
            elem=right_pane_obj.find_element_by_css_selector(textbox_objects[input_control_name])
            utillityobject.set_text_field_using_actionchains(self, elem, input_control_value)
        if input_control_type=='button':
            elem=self.driver.find_element_by_css_selector(button_objects[input_control_name])
            utillityobject.click_on_screen(self, elem, "middle", click_type=0, pause=1)
    
    def verify_ribbon_item_is_disabled_or_enabled(self, ribbon_button_name, step_num, enabled=True):
        """
        Description : This method will verify whether ribbon is disabled 
        :usage : verify_ribbon_item_is_disabled("format_auto_drill", "01.02")
        """
        ribbon_item = self.driver.find_element(*VisualizationRibbonLocators.__dict__[ribbon_button_name])
        style_value = ribbon_item.get_attribute("style")
        if enabled == True:
            status = True if "opacity" not in style_value else False
            msg = "Step {0} : Verify [{1}] is enabled in ribbon bar".format(step_num, ribbon_button_name)
        else :
            status = True if "opacity" in style_value and "0.2" in style_value else False
            msg = "Step {0} : Verify [{1}] is disabled in ribbon bar".format(step_num, ribbon_button_name)
        utillityobject.asequal(self, True, status, msg)
    
    def select_output_format(self, format_path, select_from="ribbon_bar"):
        """
        Description : Click on format button(from Ribbon or Status bar) and select output format options
        :usage : select_output_format("Html")
        """
        format_types_css = "#HomeFormatTypeMenu .tool-bar-split-menu-button"
        sub_format_css = "[id^='IAMenuPopup'] .tool-bar-split-menu-button"
        format_button_css = "#sbpOutputFormat img" if select_from.lower() == "status_bar" else "#HomeFormatType img"
        format_button = utillityobject.validate_and_get_webdriver_object(self, format_button_css, "format button")
        coreutillityobject.left_click(self, format_button)
        utillityobject.synchronize_until_element_is_visible(self, format_types_css, 30, 2)
        format_options_obj = utillityobject.validate_and_get_webdriver_objects(self, format_types_css, "Output format options")
        formats = format_path.split("->")
        for format_output in format_options_obj :
            if format_output.text.strip() == formats[0].strip() :
                format_obj = format_output
                break
        else : 
            error = "[{0}] Output format not exists".format(formats[0])
            raise KeyError(error)
        if len(formats) > 1 :
            arror_obj = utillityobject.validate_and_get_webdriver_object(self, "[id^='menu_toolbarBtn']", "Sub format expand icon", format_obj)
            coreutillityobject.left_click(self, arror_obj)
            utillityobject.synchronize_until_element_is_visible(self, sub_format_css, 10, 1)
            sub_formats_obj = utillityobject.validate_and_get_webdriver_objects(self, sub_format_css, "Sub output format options")
            for sub_format_output in sub_formats_obj :
                if sub_format_output.text.strip() == formats[1].strip() :
                    sub_format_obj = sub_format_output
                    break
            else : 
                error = "[{0}] Output format not exists".format(formats[1])
                raise KeyError(error)
            coreutillityobject.left_click(self, sub_format_obj)    
        else :
            coreutillityobject.left_click(self, format_obj)
        
    
    def verify_ribbon_item_selected_or_not(self, ribbon_button_name, step_num, selected=True):
        """
        Description : Verify ribbon bar item is selected by using background color
        :usage : verify_ribbon_item_selected_or_not("format_auto_drill", "02.01")
        """
        expected_color = "rgba(184, 223, 255, 1)" if selected == True else "rgba(0, 0, 0, 0)"
        item_css = VisualizationRibbonLocators.__dict__[ribbon_button_name][1].replace(" img", "")
        ribbon_item = self.driver.find_element_by_css_selector(item_css)
        actual_color = Color.from_string(ribbon_item.value_of_css_property("background-color")).rgba
        msg = "Step {0} : Verify [{1}] is selected in ribbon bar".format(step_num, ribbon_button_name)
        utillityobject.asequal(self, expected_color, actual_color, msg)