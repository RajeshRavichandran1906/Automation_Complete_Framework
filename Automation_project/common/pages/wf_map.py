from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.lib.base import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time, pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from common.lib.global_variables import Global_variables

class Wf_Map(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Wf_Map, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def set_geo_role_dialog(self, **kwargs):
        '''
        kwargs['dep_role_name'] = Enter Dependent role name
        kwargs['dep_store_as'] = Enter Dependent stored as
        kwargs['dep_field_name'] = Enter Depended Field name
        kwargs['dep_row_num'] = Enter the row number of the Depends on Fields. Example 1 or 2
        kwargs['assoc_cord'] = Enter Associate Cordinate
        kwargs['role_name'] = Enter role name
        kwargs['store_as'] = Enter Stored As
        kwargs['btn_click'] = Enter the button to be clicked 'Ok' or 'Cancel'
        Usage: set_geo_role(store_as='Name', dep_field_name='COUNTRY', btn_click='Ok')
        '''
        row_num=kwargs['dep_row_num'] if 'dep_row_num' in kwargs else 1
        
        row_index=(row_num-1)*3
        elist=[]
        for i in range(row_index, row_index+3):
            elist.append(i)
        if 'dep_role_name' in kwargs:
            arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
            utillityobject.select_combo_box_item(self, kwargs['dep_role_name'], combobox_dropdown_elem=arrowlst[elist[0]])
            time.sleep(1)
        if 'dep_store_as' in kwargs:
            arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
            utillityobject.select_combo_box_item(self, kwargs['dep_store_as'], combobox_dropdown_elem=arrowlst[elist[1]])
            time.sleep(1)
        if 'dep_field_name' in kwargs:
            arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
            utillityobject.select_combo_box_item(self, kwargs['dep_field_name'], combobox_dropdown_elem=arrowlst[elist[2]])
            time.sleep(1)
        if 'assoc_cord' in kwargs:
            set_assoc_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoAssocCoordinateHBox'][style*='inherit'] div[id='cbAssocGeoCoordinate'] div[id^='BiButton']")
            utillityobject.select_combo_box_item(self, kwargs['assoc_cord'], combobox_dropdown_elem=set_assoc_obj)
            time.sleep(1)
        if 'role_name' in kwargs:
            set_geo_role_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id$='GeoRoleBox'][style*='left'] div[id^='BiButton']")
            utillityobject.select_combo_box_item(self, kwargs['role_name'], combobox_dropdown_elem=set_geo_role_obj)
            time.sleep(1)
        
        if 'store_as' in kwargs:
            set_store_as_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoFormatBox'][style*='left'] div[id^='BiButton']")
            utillityobject.select_combo_box_item(self, kwargs['store_as'], combobox_dropdown_elem=set_store_as_obj)
            time.sleep(1)
            
        if 'user_defined' in kwargs:
            radio_objs=self.driver.find_elements_by_css_selector("div[id^='QbDialog']  div[id^='BiRadioButton'] input[id^='BiRadioButton']")
            radio_objs[1].click()
            time.sleep(2)
            bibtn_elems = self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiButton']> div[id^='BiLabel']")
            get_values_objs = bibtn_elems[[elem.text.strip() for elem in bibtn_elems].index('Get Values')]
            get_values_objs.click()
            time.sleep(2)
            get_values_table=self.driver.find_element_by_css_selector("#geoValuesPopup #geoValuesList")
            utillityobject.multiselect_item_using_scroll_operation(self, get_values_table, kwargs['user_defined_list'])
            ok_btn=self.driver.find_element_by_css_selector("#geoValuesPopupOkBtn")
            coreutillityobject.left_click(self, ok_btn)
            time.sleep(1)
            
        if 'btn_click' in kwargs:
            self.driver.find_element_by_css_selector("#geoRole"+kwargs['btn_click']+"Btn").click()
            time.sleep(1)
    
    def set_geo_role_location(self, **kwargs):
        '''   
        kwargs['role_name'] = Enter role name
        kwargs['btn_click'] = Enter the button to be clicked 'Ok' or 'Cancel'
        Usage: set_location_geo_role(role_name='state_name(Alabama,Alaska,Arizona)',btn_click='Ok')
        '''
        
        if 'role_name' in kwargs:
            set_geo_role_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id$='geoRoleComboBox'] div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self, set_geo_role_obj, kwargs['role_name'])
            time.sleep(1)
        if 'btn_click' in kwargs:
            self.driver.find_element_by_css_selector("#locType"+kwargs['btn_click']+"Btn").click()
            time.sleep(1)
            
    def select_pan_or_selection(self, parent_css, btn_name='Pan'):
        '''   
        btn_name='Pan' or 'Selection'
        Usage: select_pan_or_selection('#MAINTABLE_wbody2',btn_name='Pan')
        '''
        btn='Pan' if btn_name=='Pan' else 'Selection'
        btn=self.driver.find_element_by_css_selector(parent_css+" div[class*='SelectionButton UIButton toggleMode"+btn+"']")
        coreutillityobject.left_click(self, btn)
    
    '''**************************************OLD FUNCTIONS*************************************************'''
    
    
    def set_geo_role(self, **kwargs):
        """    
        
        kwargs['dep_role_name'] = Enter Dependent role name
        kwargs['dep_store_as'] = Enter Dependent stored as
        kwargs['dep_field_name'] = Enter Depended Field name
        kwargs['dep_row_num'] = Enter the row number of the Depends on Fields. Example 1 or 2
        kwargs['assoc_cord'] = Enter Associate Cordinate
        kwargs['role_name'] = Enter role name
        kwargs['store_as'] = Enter Stored As
        kwargs['btn_click'] = Enter the button to be clicked 'Ok' or 'Cancel'
        
        
        Usage: set_geo_role(store_as='Name', dep_field_name='COUNTRY', btn_click='Ok')
        """
        row_num=kwargs['dep_row_num'] if 'dep_row_num' in kwargs else 1
        
        row_index=(row_num-1)*3
        elist=[]
        for i in range(row_index, row_index+3):
            elist.append(i)
       
        
        if 'dep_role_name' in kwargs:
            arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
            #utillityobject.select_any_combobox_item(self, arrowlst[0], kwargs['dep_role_name'])
            utillityobject.select_any_combobox_item(self, arrowlst[elist[0]], kwargs['dep_role_name'])
            time.sleep(1)
        if 'dep_store_as' in kwargs:
            arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
            #utillityobject.select_any_combobox_item(self, arrowlst[1], kwargs['dep_store_as'])
            utillityobject.select_any_combobox_item(self, arrowlst[elist[1]], kwargs['dep_store_as'])
            time.sleep(1)
        if 'dep_field_name' in kwargs:
            arrowlst=self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiComboBox']  div[id^='BiButton']")
            #utillityobject.select_any_combobox_item(self, arrowlst[2], kwargs['dep_field_name'])
            utillityobject.select_any_combobox_item(self, arrowlst[elist[2]], kwargs['dep_field_name'])
            time.sleep(1)
        if 'assoc_cord' in kwargs:
            set_assoc_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoAssocCoordinateHBox'][style*='inherit'] div[id='cbAssocGeoCoordinate'] div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self,set_assoc_obj, kwargs['assoc_cord'])
            time.sleep(1)
        if 'role_name' in kwargs:
            set_geo_role_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id$='GeoRoleBox'][style*='left'] div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self, set_geo_role_obj, kwargs['role_name'])
            time.sleep(1)
        
        if 'store_as' in kwargs:
            set_store_as_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoFormatBox'][style*='left'] div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self, set_store_as_obj, kwargs['store_as'])
            time.sleep(1)
            
        if 'user_defined' in kwargs:
            radio_objs=self.driver.find_elements_by_css_selector("div[id^='QbDialog']  div[id^='BiRadioButton'] input[id^='BiRadioButton']")
            radio_objs[1].click()
            time.sleep(2)
            bibtn_elems = self.driver.find_elements_by_css_selector("div[id^='QbDialog'] [class*='group-box']  div[id^='BiButton']> div[id^='BiLabel']")
            get_values_objs = bibtn_elems[[elem.text.strip() for elem in bibtn_elems].index('Get Values')]
            get_values_objs.click()
            time.sleep(2)
            get_values_table=self.driver.find_element_by_css_selector("#geoValuesPopup #geoValuesList")
            utillityobject.click_on_screen(self, get_values_table, 'middle')
            rows=self.driver.find_elements_by_css_selector("#geoValuesPopup #geoValuesList table > tbody > tr")
            utillityobject.click_on_screen(self, rows[0], coordinate_type='left', click_type=0, x_offset=7)
            for e in kwargs['user_defined']:
                get_value=True
                while get_value:
                    browser=Global_variables.browser_name
                    if browser == 'firefox':
                        pyautogui.press('pagedown', pause=2)
                    else:
                        action = ActionChains(self.driver)
                        action.send_keys(keys.Keys.PAGE_DOWN).perform()
                        time.sleep(2)
                        del action
                    rows=self.driver.find_elements_by_css_selector("#geoValuesPopup #geoValuesList table > tbody > tr")
                    time.sleep(1)
                    tmp_list=[el.text.strip() for el in rows]
                    if e in tmp_list:
                        click_item=rows[tmp_list.index(e)]
                        utillityobject.click_on_screen(self, click_item, coordinate_type='left', x_offset=7)
                        utillityobject.click_on_screen(self, click_item, coordinate_type='left', click_type=0, x_offset=7)
                        get_value=False
                        break
                time.sleep(1)
                ok_btn=self.driver.find_element_by_css_selector("#geoValuesPopupOkBtn")
                utillityobject.click_on_screen(self, ok_btn, coordinate_type='middle', click_type=0)
            time.sleep(1)
            
        if 'btn_click' in kwargs:
            self.driver.find_element_by_css_selector("#geoRole"+kwargs['btn_click']+"Btn").click()
            time.sleep(1)
        
    def drag_layer_slider(self, drag_offset): 
        '''
        drag_offset= +ive(drag to right) or -ive value(drag to left).
        '''
        drag_obj=self.driver.find_element_by_css_selector(".TableOfContents .toc-slider-handle")
        coordinates=utillityobject.get_object_screen_coordinate(self, drag_obj, coordinate_type='middle')
        utillityobject.drag_drop_on_screen(self, sx_offset=coordinates['x'], sy_offset=coordinates['y'], tx_offset=coordinates['x']+drag_offset, ty_offset=coordinates['y'])

    def select_demographic_layer(self,lifestyle_list, population_list, **kwargs):
        '''
        lifestyle_list=[('item1',0),('item2', 1)]
        population_list=[('item1',0),('item2', 1)]
        kwargs['btn_click'] = Enter the button to be clicked 'Ok' or 'Cancel'
        usage:  lifestyle_list=[('USA Tapestry Segmentation 2012',0)]
                population_list=[('USA Unemployment Rate 2012',9)]
                wfmapobj.select_demographic_layer(lifestyle_list, population_list, btn_click='Ok')
        '''
        (lifestyle, population)=self.driver.find_elements_by_css_selector("[id^='QbDemographicLayersDlg'] [id^='DemographicLayerGrid']")
        if len(lifestyle_list) > 0:
            for (lifestyle_item, scroll_time) in lifestyle_list:
                inc=0
                while scroll_time > inc:
#                     lifestyle.find_element_by_css_selector("[id^='BiRepeatButton'][class*='scroll-bar-inc']").click()
                    self.driver.find_elements_by_css_selector("[class*='bi-scroll-bar scroll-bar-vertical'] [id^='BiRepeatButton'][class*='scroll-bar-inc']").click()
                    inc=inc+1
                lifestyle_row_objs=lifestyle.find_elements_by_css_selector("table tr")
                required_row_obj=lifestyle_row_objs[[el.text.strip() for el in lifestyle_row_objs].index(lifestyle_item)]
                utillityobject.default_left_click(self,object_locator=required_row_obj,action_move=True)
        if len(population_list) > 0:
            for (population_item, scroll_time) in population_list:
                inc=0
                while scroll_time > inc:
#                     lifestyle.find_elements_by_css_selector("[class*='bi-scroll-bar scroll-bar-vertical'] [id^='BiRepeatButton'][class*='scroll-bar-inc']").click()
                    self.driver.find_elements_by_css_selector("[class*='bi-scroll-bar scroll-bar-vertical'] [id^='BiRepeatButton'][class*='scroll-bar-inc']")[1].click()
                    inc=inc+1
                population_row_objs=population.find_elements_by_css_selector("table tr")
                required_row_obj=population_row_objs[[el.text.strip() for el in population_row_objs].index(population_item)]
                utillityobject.default_left_click(self,object_locator=required_row_obj,action_move=True)
        if 'btn_click' in kwargs:
            self.driver.find_element_by_css_selector("#demographicLayersDlg"+kwargs['btn_click']+"Btn").click()
            time.sleep(1)
            
    def select_reference_layer(self, layer_list, **kwargs):
        '''
        layer_list=[('item1',0),('item2', 1)]
        kwargs['btn_click'] = Enter the button to be clicked 'Ok' or 'Cancel'
        usage:  layer_list=[('USA Countries Generalized',0)]
                wfmapobj.select_reference_layer(layer_list, btn_click='Ok')
        '''
        
        if len(layer_list) > 0:
            for (layer_item, scroll_time) in layer_list:
                inc=0
                while scroll_time > inc:
                    self.driver.find_elements_by_css_selector("[class*='bi-scroll-bar scroll-bar-vertical'] [id^='BiRepeatButton'][class*='scroll-bar-inc']")[0].click()
                    inc=inc+1
                layer_row_objs=self.driver.find_elements_by_css_selector("[id^='QbReferenceLayersDlg'] [id^='ReferenceLayerGrid'] table tr")
                required_row_obj=layer_row_objs[[el.text.strip() for el in layer_row_objs].index(layer_item)]
                utillityobject.default_left_click(self,object_locator=required_row_obj,action_move=True)
        
        if 'btn_click' in kwargs:
            self.driver.find_element_by_css_selector("#refLayersDlg"+kwargs['btn_click']+"Btn").click()
            time.sleep(1)
                
    def set_location_geo_role(self, **kwargs):
        """    
     
        kwargs['role_name'] = Enter role name
        
        kwargs['btn_click'] = Enter the button to be clicked 'Ok' or 'Cancel'
        
        
        Usage: set_location_geo_role(role_name='state_name(Alabama,Alaska,Arizona)',btn_click='Ok')
        """
        
        if 'role_name' in kwargs:
            utillityobject.synchronize_until_element_is_visible(self, element_css ="div[id^='QbDialog'] div[id$='geoRoleComboBox'] div[id^='BiButton']", expire_time = 30)
            set_geo_role_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id$='geoRoleComboBox'] div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self, set_geo_role_obj, kwargs['role_name'])
            time.sleep(1)
        
            
        if 'btn_click' in kwargs:
            btn_ele = self.driver.find_element_by_css_selector("#locType"+kwargs['btn_click']+"Btn")
            coreutillityobject.python_left_click(self, web_element= btn_ele)
            time.sleep(1)
                    

    def select_regionlabel_checkbox(self, labellist):
        """    
        Usage: select_regionlabel_checkbox(['Northeast', 'South'])
        """
        label_checkbox_css="#checkbox1 label"
        reference_name="regionlabel_checkbox in esri map"
        label_checkbox_obj=utillityobject.validate_and_get_webdriver_objects(self, label_checkbox_css, reference_name)
        for elem in label_checkbox_obj:
            for labelname in labellist:
                if elem.text.strip()==labelname:
                    required_check_box=elem.find_element_by_css_selector("input")
                    required_check_box.click()
        
    def select_mainmenu_btn(self, mainmenu_css, btn_name):
        """
        Usage: select_mainmenu_btn(mainmenu_css="#mainMenuemfobject1", btn_name='basemap')
        """
        mainmenu_btn_dict={'homebutton':mainmenu_css + " [class^='HomeButton']",
                        'layerswidget':mainmenu_css + " [class^='layersWidget']",
                        'selectionwidget':mainmenu_css + " [class^='selectionWidget']",
                        'basemap':mainmenu_css + " [class^='basemapBtn']"}
        reference_name="Mainmenu button" +mainmenu_btn_dict[btn_name]+ "in esri map"
        mainmenu_btn=utillityobject.validate_and_get_webdriver_object(self, mainmenu_btn_dict[btn_name], reference_name)  
        mainmenu_btn.click()
        
        
    def close_basemap_dialog(self):
        """
        Usage: close_basemap_dialog()
        """
        close_btn_css="#emfobject1_imFloatingPane span[class='dojoxFloatingCloseIcon']"
        reference_name="Close button in basemap dialog in esri map"
        close_btn=utillityobject.validate_and_get_webdriver_object(self, close_btn_css, reference_name)  
        close_btn.click()    
        
        
        
        
        
        
        
        
        
        