import time
from common.lib.base import BasePage
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods

class Insight_Header(BasePage):
    header_css = 'div.header-box'
    query_box_css = header_css + ' > .query-box'
    query_items_css =  query_box_css + " [class *='items-box']"
    option_box_css = header_css + ' > .options-box'
    option_items_css =  option_box_css + " [class *='options-bar']"
    chart_picker_popup = "[class^='chart-picker-popup']"
    field_selector_popup = ".pop-top div[class*='field-selector']"
    more_option_menu = "div[class*='er-option-menu']"
    filter_selector_popup = "div[class*='filter-popup']"
    filter_panel_css = "div[class^='filter-panel']"
    
    def __init__(self, driver):
        super(Insight_Header, self).__init__(driver)
    
    def get_query_bucket_container(self, bucket_name):
        container_css=Insight_Header.query_items_css + ' > .bucket-container'
        container_description='query buckets'
        container_elements=utillobject.validate_and_get_webdriver_objects(self, container_css, container_description)
        for container_element in container_elements:
            container_label_css='.bucket-label'
            container_label_description=bucket_name + ' in query bucket'
            container_label_element=utillobject.validate_and_get_webdriver_object(self, container_label_css, container_label_description, parent_object=container_element)
            if container_label_element.text.strip().lower() == bucket_name.lower():
                return container_element
    
    def get_field_container(self, bucket_name, field_name):
        container_element = Insight_Header.get_query_bucket_container(self, bucket_name)
        field_container_css="div[data-ibx-type='erFieldBucket']"
        field_container_description=field_name + ' inside ' + bucket_name + ' query bucket'
        field_container_elements=utillobject.validate_and_get_webdriver_objects(self, field_container_css, field_container_description, parent_object=container_element)
        for field_container_element in field_container_elements:
            field_container_label_css='.er-fb-field-label'
            field_container_label_description='field names labels in side query bucket'
            field_container_label_element=utillobject.validate_and_get_webdriver_object(self, field_container_label_css, field_container_label_description, parent_object=field_container_element)
            if field_container_label_element.text.strip().lower() == field_name.lower():
                return field_container_element
    
    def get_field_label_element(self, bucket_name, field_name, component_button_name):
        '''
        component_button_name = 'label' OR 'aggregate' OR 'by' OR 'delete'
        '''
        if component_button_name == 'label':
            required_field_element_css='.er-fb-field-label'
            required_field_element_description=field_name + '  label in side query bucket'
        elif component_button_name == 'aggregate':
            required_field_element_css='.er-fb-how-aggregate'
            required_field_element_description='aggregate button for ' + field_name + '  in side query bucket'
        elif component_button_name == 'by':
            required_field_element_css='.er-fb-by-label'
            required_field_element_description='By button for ' + field_name + '  in side query bucket'
        elif component_button_name == 'delete':
            required_field_element_css='.er-fb-delete-bucket'
            required_field_element_description='delete button for ' + field_name + '  in side query bucket'
        else:
            raise ValueError('[' + component_button_name + '] parameter value is incorrectly passed to the function.')
        field_container_element = Insight_Header.get_field_container(self, bucket_name, field_name)
        field_label_element=utillobject.validate_and_get_webdriver_object(self, required_field_element_css, required_field_element_description, parent_object=field_container_element)
        return field_label_element
    
    def select_header_option_item(self, option_item_name):
        '''
        option_item_name = 'reset' OR 'pivot' OR 'save' OR 'filter' OR 'more-options'
        '''
        dict_ids={'reset':" div[class^='reset'][title^='Reset'] div[class*='ibx-icons']",
                  'pivot':" div[class^='pivot'][title^='Swap  Axis'] div[class*='ibx-icons']",
                  'save':" div[class^='save'][title^='Save'] div[class*='ibx-icons']",
                  'change_chart':" div[class^='chart-picker-arrow']",
                  'filter':" div[class^='filter'][title='Show Filter'] div[class*='ibx-icons']",
                  'hide_filter':" div[class^='filter'][title='Hide Filter'] div[class*='ibx-icons']",
                  'more_options':" div[class^='more-options'][title^='More Options'] div[class*='ibx-icons']"}
        
        item_css = Insight_Header.option_items_css + dict_ids[option_item_name]
#         item_css = Insight_Header.option_items_css +" div[class^="+option_item_name+"] div[class*='ibx-icons']"
        item_description= option_item_name+ 'available within insight header box'
        item_element=utillobject.validate_and_get_webdriver_object(self, item_css, item_description)
        CoreUtillityMethods.left_click(self, item_element)
        
    def get_field_in_filter_shelf(self, field_name):
        """
        Description: Will return the filter pill object based on field name
        """
        filter_pill = "div.filter-container-horizontal div[data-ibx-type='filterPill'] div.filter-field-box"
        filter_pill_objects = utillobject.validate_and_get_webdriver_objects(self, filter_pill, 'Filter pill')
        expected_filter_pill = JavaScript.find_elements_by_text(self, filter_pill_objects, field_name)
        return expected_filter_pill[0]
    
    def click_on_filter_shelf_item(self, field_name):
        """
        Description: Click on the field in filter shelf
        :usage - click_on_filter_shelf_item('COUNTRY')
        """
        filter_pill_obj = Insight_Header.get_field_in_filter_shelf(self, field_name)
        CoreUtillityMethods.left_click(self, filter_pill_obj)

    def click_on_field_in_query_bucket(self, bucket_name, field_name):
        """
        Description: Click on the field name in the query bucket
        :Usage - click_on_field_in_query_bucket('Measure', 'COUNTRY')
        """
        field_object = Insight_Header.get_field_container(self, bucket_name, field_name)
        CoreUtillityMethods.left_click(self, field_object)
        utillobject.synchronize_until_element_is_visible(self, Insight_Header.field_selector_popup, 30)
        
    def change_chart_type_from_chart_picker_option(self, chart_type):
        '''
        chart_type='Horizontal Bar', 'Vertical Bar', 'Vertical Stacked Bar', 'Ring Pie', 'Vertical Line', 'Area', 'Scatter', 'Circle Plot', 'Treemap', 'Matrix', 'Histogram', 'Point Map' ,'Choropleth Map'
        '''   
        Insight_Header.select_header_option_item(self, option_item_name='change_chart')
        utillobject.synchronize_with_number_of_element(self, Insight_Header.chart_picker_popup, 1, 45)
        chart_type_css = Insight_Header.chart_picker_popup + " div[title*='"+chart_type+"'] div[class*='ibx-label-icon']"
        item_description= chart_type+ 'available inside chart picker popup'
        chart_item=utillobject.validate_and_get_webdriver_object(self, chart_type_css, item_description)
        CoreUtillityMethods.left_click(self, chart_item)
        utillobject.synchronize_until_element_disappear(self, Insight_Header.chart_picker_popup, 30)
        
    def click_plus_icon_in_query_bucket_container(self, bucket_type):
        '''
        click_plus_icon_in_query_bucket_container('Layer')
        '''
        plus_icon_css=Insight_Header.query_items_css + " > .bucket-container div[class^='add-bucket'][aria-label*='"+bucket_type+"'] div[class$='plus']"
        item_description= bucket_type+ '-plus icon is available inside query bucket container'
        plus_icon=utillobject.validate_and_get_webdriver_object(self, plus_icon_css, item_description)
        CoreUtillityMethods.left_click(self, plus_icon)
        
    def search_and_add_field_to_query_bucket(self, bucket_type, field_name):  
        '''
        search_and_add_field_to_query_bucket('Layer', 'Store Country')
        '''  
        Insight_Header.click_plus_icon_in_query_bucket_container(self, bucket_type)
        search_css=Insight_Header.field_selector_popup+" input[type='search']"
        utillobject.synchronize_with_number_of_element(self, search_css, 1, expire_time=4)
        search_description= 'Search input box is available inside field-selector popup'
        search_field=utillobject.validate_and_get_webdriver_object(self, search_css, search_description)
#         CoreUtillityMethods.left_click(self, search_field)
#         keyboard.write(field_name, 1)
        utillobject.set_text_to_textbox_using_keybord(self, field_name, text_box_elem=search_field)
        time.sleep(Global_variables.shortwait)
        field_css=Insight_Header.field_selector_popup+" div[class*='ibx-select-item'] div[class='ibx-label-text']"
        field_description= field_name+' is available inside field-selector popup'
        field_list=utillobject.validate_and_get_webdriver_objects(self, field_css, field_description)
        requiredfield=field_list[[elem.text.strip() for elem in field_list].index(field_name)]
        CoreUtillityMethods.left_click(self, requiredfield)
        utillobject.synchronize_until_element_disappear(self, Insight_Header.field_selector_popup, 30)
        
    def select_or_verify_more_option_menu_item(self, menu_item, submenu_item=None, submenu=False, verify1=False, verify2=False, expected_menu_list=None, expected_submenu_list=None, msg1=None, msg2=None):  
        '''
        select_or_verify_more_option_menu_item_in_insight(menu_item='Series Layout', submenu_item='Side-by-Side', submenu=True)
        '''  
        Insight_Header.select_header_option_item(self, option_item_name='more_options')
        more_option_menu_css=Insight_Header.more_option_menu+" div[class*='optionsMenu-item'] div.ibx-label-text"
        more_option_menu_description= 'Items is available inside more_option_menu'
        menu_itemlist=utillobject.validate_and_get_webdriver_objects(self, more_option_menu_css, more_option_menu_description)
        if verify1 == True:
            actual_menu_list=[elem.text.strip() for elem in menu_itemlist if elem.text.strip()!='']
            utillobject.as_List_equal(self, expected_menu_list, actual_menu_list, msg1) 
        actual_menu_list=[elem.text.strip() for elem in menu_itemlist]
        menuitem=menu_itemlist[actual_menu_list.index(menu_item)]
        if submenu == True:
            CoreUtillityMethods.left_click(self, menuitem)
        else:
            CoreUtillityMethods.left_click(self, menuitem)
        if submenu == True:
            time.sleep(Global_variables.shortwait)
            utillobject.synchronize_with_number_of_element(self, "div[class*='pop-top']", 1, expire_time=4)
            submenu_css="div[class*='magic-menu'] div.ibx-label-text"
            submenu_description= 'Items is available inside more_option submenu'
            submenu_itemlist=utillobject.validate_and_get_webdriver_objects(self, submenu_css, submenu_description)
            if verify2 == True:
                actual_submenu_list=[elem.text.strip() for elem in submenu_itemlist if elem.text.strip()!='']
                utillobject.as_List_equal(self, expected_submenu_list, actual_submenu_list, msg2)
            actual_submenu_list=[elem.text.strip() for elem in submenu_itemlist]
            submenu_item=submenu_itemlist[actual_submenu_list.index(submenu_item)]
            CoreUtillityMethods.left_click(self, submenu_item)
            
    def delete_field_in_query_bucket_container(self, bucket_type, field_name):
        '''
        delete_field_in_query_bucket_container('Color', 'Product Subcategory')
        '''
        query_field_css=Insight_Header.query_items_css + " div[class^='bucket-content'] div[class*='er-field-bucket'][aria-label*='"+bucket_type+"'][aria-label*='"+field_name.lower()+"']"
        item_description= field_name+ ' is available inside ' +bucket_type+ ' in query bucket container'
        query_field=utillobject.validate_and_get_webdriver_object(self, query_field_css, item_description)
        utillobject.click_on_screen(self, query_field, 'middle')
        delete_icon=query_field.find_element_by_css_selector("div[class*='delete']")
        CoreUtillityMethods.left_click(self, delete_icon)
        
    def delete_field_in_filter_panel_container(self, field_name):
        '''
        delete_field_in_query_bucket_container('Color', 'Product Subcategory')
        '''
        field_css=Insight_Header.filter_panel_css + " div[class*='filter-pill'][aria-label*='"+field_name.lower()+"']"
        item_description= field_name+ ' - is available inside filter_panel_container'
        filter_field=utillobject.validate_and_get_webdriver_object(self, field_css, item_description)
        utillobject.click_on_screen(self, filter_field, 'middle')
        delete_icon=filter_field.find_element_by_css_selector("div[class^='delete-filter']")
        CoreUtillityMethods.left_click(self, delete_icon)
    
    def click_add_filter_in_top_filter_panel(self):
        add_filter_css = Insight_Header.filter_panel_css + " div[class^='new-filter'] div[class^='add-filter-button']"
        addfilter_description= 'Add new filter icon available inside filter panel'
        add_filterobj=utillobject.validate_and_get_webdriver_object(self, add_filter_css, addfilter_description)
        CoreUtillityMethods.left_click(self, add_filterobj)
                
    def add_field_to_filter_container(self, field_name, first_filter_selection=True):            
        '''
        add_field_to_filter_container('Product Subcategory')
        ''' 
        if first_filter_selection == True:
            Insight_Header.select_header_option_item(self, option_item_name='filter')
        else:
            Insight_Header.click_add_filter_in_top_filter_panel(self)
        fieldsearch_css=Insight_Header.filter_selector_popup+" input[type='search']"
        utillobject.synchronize_with_number_of_element(self, fieldsearch_css, 1, expire_time=4)
        search_description= 'Search input box is available inside filter-selector popup'
        fieldsearch=utillobject.validate_and_get_webdriver_object(self, fieldsearch_css, search_description)
#         CoreUtillityMethods.left_click(self, fieldsearch)
#         keyboard.write(field_name, 1)
        utillobject.set_text_to_textbox_using_keybord(self, field_name, text_box_elem=fieldsearch)
        time.sleep(Global_variables.shortwait)
        field_css=Insight_Header.filter_selector_popup+" div[class*='ibx-select-item'] div[class='ibx-label-text']"
        field_description= field_name+' is available inside filter-selector popup'
        field_list=utillobject.validate_and_get_webdriver_objects(self, field_css, field_description)
        requiredfield=field_list[[elem.text.strip() for elem in field_list].index(field_name)]
        CoreUtillityMethods.left_click(self, requiredfield)
        
    def select_or_verify_filter_grid_values(self, field_name, item_list, verify=False, expected_item_list=None, msg=None): 
        '''
        select_or_verify_filter_grid_values('Product Subcategory', item_list=['Accessories', 'Camcorder', 'Computers'])
        '''   
        filterpopup_css = Insight_Header.filter_selector_popup+"[aria-label*='"+field_name.lower()+"']"
        utillobject.synchronize_with_number_of_element(self, filterpopup_css, 1, expire_time=4)
        filterpopup_item_css=filterpopup_css+" div[class*='select-check-item']"
        item_description= field_name+' is available inside filter-selector popup'
        popup_items=utillobject.validate_and_get_webdriver_objects(self, filterpopup_item_css, item_description)
        actual_item_list=[el.text.strip() for el in popup_items]
        if verify == True:
            utillobject.as_List_equal(self, expected_item_list, actual_item_list, msg)
        for item in item_list:
            flag = True
            while flag:
                if item in actual_item_list:
                    popup_items[actual_item_list.index(item)].find_element_by_css_selector("div[class*='check-box']").click()
                flag = False
    
    def verify_field_visible_in_query_bucket_container(self, bucket_type, field_name, msg, visible=True):
        '''
        verify_field_in_query_bucket_container('Color', 'Product Subcategory', msg='step:')
        '''
        query_field_css=Insight_Header.query_items_css + " div[class^='bucket-content'] div[class*='er-field-bucket'][aria-label*='"+bucket_type+"'][aria-label*='"+field_name.lower()+"']"
        utillobject.verify_element_visiblty(self, element_css=query_field_css, visible=visible, msg=msg)
        
    def verify_field_visible_in_filter_panel_container(self, field_name, msg, visible=True):
        '''
        verify_field_in_filter_panel_container('Product Subcategory', msg='step:')
        '''
        field_css=Insight_Header.filter_panel_css + " div[class*='filter-pill'][aria-label*='"+field_name.lower()+"']"
        utillobject.verify_element_visiblty(self, element_css=field_css, visible=visible, msg=msg)
        
    def verify_add_filter_btn_visible_in_filter_panel_container(self, msg, visible=True):
        '''
        verify_add_filter_btn_visible_in_filter_panel_container(msg='step:')
        '''
        filter_btn_css=Insight_Header.filter_panel_css + " div[class^='new-filter'] div[class^='add-filter-button']"
        utillobject.verify_element_visiblty(self, element_css=filter_btn_css, visible=visible, msg=msg)    
        
    def click_on_blank_area_in_insight_chart(self, insight_css='#runbox_id', coordinate_type='start'):
        insight_description= 'Blank area in the insight chart'
        insight_chart=utillobject.validate_and_get_webdriver_object(self, insight_css, insight_description)
        CoreUtillityMethods.left_click(self, insight_chart)
    
    def verify_option_tooltip(self, option_title, step_num):
        """
        Description : This method will insight option verify tool tip
        :Usage : verify_options_tooltip("Filter Show", "01.02")
        """
        option_css = ".options-bar div[title='{0}']".format(option_title)
        tooltip_status = len(self.driver.find_elements_by_css_selector(option_css)) > 0
        msg = "Step {0} : Verify [{1}] tool tip appear after hover mouse on [{1}] option".format(step_num, option_title)
        utillobject.asequal(self, True, tooltip_status, msg)
        
    def verify_selected_field_in_query_bucket(self, bucket_type, expected_field_name, step_num):
        """
        Description : This method will helps to verify selected field in query bucket
        :Usage : verify_selected_field_query_bucket("Horizontal Axis ", "BY COUNTRY")
        """
        query_field_css=Insight_Header.query_items_css + " div[class^='bucket-content'] div[class*='er-field-bucket'][aria-label*='"+bucket_type + "']"
        field_obj = utillobject.validate_and_get_webdriver_object(self, query_field_css, "Insight selected field")
        aggregation_fun = [aggre.get_attribute('value') for aggre in field_obj.find_elements_by_css_selector("input")]
        field_name=self.driver.find_element_by_css_selector(query_field_css).text.replace("\n", " ")
        actual_field_name = (aggregation_fun[-1] + " " + field_name).strip()
        msg = "Step {0} : Verify [{1}] is selected in [{2}]".format(step_num, field_name, bucket_type)
        utillobject.asequal(self,expected_field_name, actual_field_name, msg)
    
    def verify_data_fields(self, expected_fields_list, msg, assert_type="asequal"):
        """
        Description : This method will verify data fields in fields dialog box.
        :Usage : verify_data_fields(["CAR"], "Step 01.01 : Verify CAR fields displayed")
        """
        fields_objects = utillobject.validate_and_get_webdriver_objects(self, " .ibx-selection-manager.pop-top div[data-ibx-type='erFieldSelector'] .ibx-label", "data_fileds") 
        actual_fields_text = [field.text.strip() for field in fields_objects if field.is_displayed()]    
        utillobject.verify_list_values(self, expected_fields_list, actual_fields_text, msg, assert_type)   