from common.lib.base import BasePage
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.core_utility import CoreUtillityMethods as coreutilobj
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class Resource_Dialog(BasePage):
    parent_css = '.pop-top'
    resource_dialog_css='.open-dialog-resources{0}'.format(parent_css)
    dialog_name = None
    scroll_css=".tpg-selected div[class*='files-box-files']"
    scroll_list_css=".tpg-selected .files-box-files-area"
    button_row_css = ".ibx-dialog-button-box"
    resource_tree_css = ".tpg-selected #files-box-area > .fbx-block.fbx-column"
    resource_tree_list_css= ".tpg-selected .files-box-files-area [title] .ibx-label-text"
    grid_view_css = resource_dialog_css + " .tpg-selected div[data-ibx-name='tilesBox']:not([style*='none'])"
    list_view_css = resource_dialog_css + " .tpg-selected div[data-ibx-name='listBox']:not([style*='none'])"
    
    def __init__(self, driver):
        super(Resource_Dialog, self).__init__(driver)
    
    def verify_resource_dialog_is_visible(self, visible_mode, msg):
        '''
        '''
        utillobject.verify_object_visible(self, Resource_Dialog.resource_dialog_css, visible_mode, msg)
            
    def get_caption_title(self):
        caption_title_css='{0} .ibx-title-bar-caption'.format(Resource_Dialog.resource_dialog_css)
        caption_description='Caption'
        caption_title_obj=utillobject.validate_and_get_webdriver_object(self, caption_title_css, caption_description)
        return caption_title_obj.text.strip()
    
    def verify_caption_title(self, expected_title_name, msg):
        actual_title_name=Resource_Dialog.get_caption_title(self)
        utillobject.asequal(self, expected_title_name, actual_title_name, msg)
        
    def select_tab_button(self, tab_button_name):
        tab_button_css=Resource_Dialog.resource_dialog_css+' .ibx-csl-items-container .ibx-tab-button'
        tab_description=Resource_Dialog.dialog_name + ' tab buttons'
        tab_button_objs=utillobject.validate_and_get_webdriver_objects(self, tab_button_css, tab_description)
        for tab_button_obj in tab_button_objs:
            if tab_button_obj.text.strip()==tab_button_name:
                coreutilobj.left_click(self, tab_button_obj)
                break

    def get_crumb_item_list(self):
        crumb_css=Resource_Dialog.resource_dialog_css+" .sd-tab-page.tpg-selected .sd-toolbar > .sd-crumb-box [data-ibx-type='ibxButtonSimple']"
        crumb_description=Resource_Dialog.dialog_name + ' breed crumb'
        crumb_obj=utillobject.validate_and_get_webdriver_objects(self, crumb_css, crumb_description)
        return crumb_obj
    
    def verify_crumb_list(self, expected_crumb_list, msg):
        crumb_items_list=Resource_Dialog.get_crumb_item_list(self) 
        actual_crumb_list=[el.text.strip() for el in crumb_items_list if el.text.strip()!='']
        utillobject.asequal(self, expected_crumb_list, actual_crumb_list, msg)

    def select_crumb_item(self, crumb_item_name, selection_type='left'):
        crumb_item_name = 'Workspaces' if crumb_item_name == 'Domains' else crumb_item_name
        crumb_items_list=Resource_Dialog.get_crumb_item_list(self)
        for crumb_item in crumb_items_list:
            if crumb_item.text.strip() == crumb_item_name:
                if selection_type=='left':
                    coreutilobj.left_click(self, crumb_item)
                elif selection_type=='double':
                    coreutilobj.double_click(self, crumb_item)
                break
        utillobject.wait_for_page_loads(self, 60)
        
    def get_resource_items_from_gridview(self):
        resource_item_css='{0} {1}'.format(Resource_Dialog.resource_dialog_css, Resource_Dialog.resource_tree_css)
        resource_description=Resource_Dialog.dialog_name + ' file or folder items'
        resource_objects=utillobject.validate_and_get_webdriver_objects(self, resource_item_css, resource_description)
        return resource_objects
    
    def get_resource_item_from_gridview(self, resource_name):
        folder_obj=Resource_Dialog.get_resource_items_from_gridview(self)
        index = JavaScript.find_element_index_by_text(self, folder_obj, resource_name)
        if index==None:
            raise LookupError("'" + resource_name.capitalize() + "' not able to found in resource grid_view dialog.")
        if folder_obj == []:
            return ('{0} not found'.format(resource_name.capitalize()))
        else:
            scroll_css = '{0} {1}'.format(Resource_Dialog.resource_dialog_css, Resource_Dialog.scroll_css)
            scroll_obj=utillobject.validate_and_get_webdriver_object(self, scroll_css, 'Requested resource Scroll')
            scroll_bottom_cord = coreutilobj.get_web_element_coordinate(self, scroll_obj, 'bottom_middle')
            coreutilobj.python_move_to_element(self, scroll_obj)
            while True:
                item_bootm_cord = coreutilobj.get_web_element_coordinate(self, folder_obj[int(index)], 'bottom_middle')
                item_cord = int(item_bootm_cord['y']) + 9 if Global_variables.browser_name != 'firefox' else int(item_bootm_cord['y'])
                if item_cord > int(scroll_bottom_cord['y']):
                    utillobject.mouse_scroll(self, 'down', 1, option='uiautomation', pause=2)
                else:
                    return (folder_obj[int(index)])
    
    def get_resource_items_from_listview(self):
        
        resource_item_css='{0} {1}'.format(Resource_Dialog.resource_dialog_css, Resource_Dialog.resource_tree_list_css)
        resource_description=Resource_Dialog.dialog_name + ' file or folder items'
        resource_objects=utillobject.validate_and_get_webdriver_objects(self, resource_item_css, resource_description)
        return resource_objects
    
    def get_resource_item_from_listview(self, resource_name):
        folder_obj =Resource_Dialog.get_resource_items_from_listview(self)
        index = JavaScript.find_element_index_by_text(self, folder_obj, resource_name)
        if index==None:
            raise LookupError("'" + resource_name.capitalize() + "' not able to found in resource list_view dialog.")
        if folder_obj == []:
            return ('{0} not found'.format(resource_name.capitalize()))
        else:
            scroll_css = '{0} {1}'.format(Resource_Dialog.resource_dialog_css, Resource_Dialog.scroll_list_css)
            scroll_obj=utillobject.validate_and_get_webdriver_object(self, scroll_css, 'Requested resource Scroll')
            scroll_bottom_cord = coreutilobj.get_web_element_coordinate(self, scroll_obj, 'bottom_middle')
            coreutilobj.python_move_to_element(self, scroll_obj)
            while True:
                item_bootm_cord = coreutilobj.get_web_element_coordinate(self, folder_obj[int(index)], 'bottom_middle')
                if int(item_bootm_cord['y'])+9 > int(scroll_bottom_cord['y']):
                    utillobject.mouse_scroll(self, 'down', 1, option='uiautomation', pause=2)
                else:
                    return (folder_obj[int(index)])
             
    def select_resource_from_gridview(self, resource_name, selection_type='left'):
        required_resource_item=Resource_Dialog.get_resource_item_from_gridview(self, resource_name)
        if required_resource_item=='{0} not found'.format(resource_name.capitalize()):
            error_msg='The requested resource ' + resource_name + ' is not available in the grid view of ' + Resource_Dialog.dialog_name + '.'
            raise LookupError(error_msg)
        coreutilobj.left_click(self, required_resource_item)
        if selection_type=='double':
            coreutilobj.double_click(self, required_resource_item)
            
    def select_resource_from_listview(self, resource_name, selection_type='left'):
        required_resource_item=Resource_Dialog.get_resource_item_from_listview(self, resource_name)
        if required_resource_item=='{0} not found'.format(resource_name.capitalize()):
            error_msg='The requested resource ' + resource_name + ' is not available in the list view of ' + Resource_Dialog.dialog_name + '.'
            raise LookupError(error_msg)
        coreutilobj.left_click(self, required_resource_item)
        if selection_type=='double':
            coreutilobj.double_click(self, required_resource_item)
    
    def verify_resource_item_in_gridview(self, resource_name, comparison_type, msg):
        raw_resource_items = [element.text.strip().split('\n') for element in Resource_Dialog.get_resource_items_from_gridview(self)]
        resource_items = [item for list_item in raw_resource_items for item in list_item]
        if comparison_type == 'asin':
            utillobject.asin(self, resource_name, resource_items, msg)  
        elif comparison_type == 'asnotin':
            utillobject.as_notin(self, resource_name, resource_items, msg)
    
    def verify_resource_item_in_listview(self, resource_name, comparison_type, msg):
        raw_resource_items = [element.text.strip().split('\n') for element in Resource_Dialog.get_resource_items_from_gridview(self)]
        resource_items = [item for list_item in raw_resource_items for item in list_item]
        if comparison_type == 'asin':
            utillobject.asin(self, resource_name, resource_items, msg)  
        elif comparison_type == 'asnotin':
            utillobject.as_notin(self, resource_name, resource_items, msg)  
    
    def get_title_object(self):
        title_item_css=Resource_Dialog.resource_dialog_css+' .sd-text-input .sd-form-field-text-title'
        title_description=Resource_Dialog.dialog_name + ' Title input box'
        title_object=utillobject.validate_and_get_webdriver_object(self, title_item_css, title_description)
        return title_object
    
    def get_search_textbox_object(self):
        search_textbox_css=Resource_Dialog.resource_dialog_css+' .sd-txt-search input'
        search_textbox_description=Resource_Dialog.dialog_name + ' Search input box'
        search_textbox_object=utillobject.validate_and_get_webdriver_object(self, search_textbox_css, search_textbox_description)
        return search_textbox_object
    
    def get_name_object(self):
        name_item_css=Resource_Dialog.resource_dialog_css+' .sd-text-input .sd-form-field-text-name'
        name_description=Resource_Dialog.dialog_name + ' Name input box'
        name_object=utillobject.validate_and_get_webdriver_object(self, name_item_css, name_description)
        return name_object
    
    def set_title_text(self, title_string): 
        title_item=Resource_Dialog.get_title_object(self)
        title_input_elem = utillobject.validate_and_get_webdriver_object(self, 'input', title_string, parent_object=title_item)
        utillobject.set_text_to_textbox_using_keybord(self, title_string, text_box_elem=title_input_elem)
        
    def verify_name_textbox(self):
        pass
    
    def verify_title_textbox(self):
        pass
    
    def get_button_object(self, button_name):
        close_button_css = "[data-ibx-name='titleClose']"
        if button_name.lower() == 'close':
            button_object = utillobject.validate_and_get_webdriver_object(self, close_button_css, 'Resource close Button')
            return (button_object)
        else:
            button_row_css = '{0} {1}'.format(Resource_Dialog.parent_css, WfMainPageLocators.BUTTON_CSS)
            button_elements = utillobject.validate_and_get_webdriver_objects(self, button_row_css, 'Resource Buttons')
            button_element = [button for button in button_elements if button.is_displayed()]
            for button_object in button_element:
                if button_object.text.strip() == button_name:
                    return (button_object)
    
    def is_grid_view(self):
        """
        Description : Return True if resource dialog set grid view else False
        """
        try :
            grid_view = utillobject.validate_and_get_webdriver_object(self, Resource_Dialog.grid_view_css, "Grid view")
            if grid_view.is_displayed() :
                return True
            else :
                return False
        except AttributeError :
            return False
    
    def is_list_view(self):
        """
        Description : Return True if resource dialog set list view else False
        """
        try :
            grid_view = utillobject.validate_and_get_webdriver_object(self, Resource_Dialog.list_view_css, "Grid view")
            if grid_view.is_displayed() :
                return True
            else :
                return False
        except AttributeError :
            return False
    
    def get_resource_item_object(self, resource_name):
        """
        Description : Return resource item object
        """
        if Resource_Dialog.is_grid_view(self):
            return Resource_Dialog.get_resource_item_from_gridview(self, resource_name)
        elif Resource_Dialog.is_list_view(self):
            return Resource_Dialog.get_resource_item_from_listview(self, resource_name)
        else :
            msg = "Unable to find grid and list view in resource dialog"
            raise RuntimeError(msg)
        
    def get_all_resource_items_object(self):
        """
        Description : Return all resource items object as list
        """
        if Resource_Dialog.is_grid_view(self):
            return Resource_Dialog.get_resource_items_from_gridview(self)
        elif Resource_Dialog.is_list_view(self):
            return Resource_Dialog.get_resource_items_from_listview(self)
        else :
            msg = "Unable to find grid and list view in resource dialog"
            raise RuntimeError(msg)
    
    def get_tag_objects(self):
        """
        Description : Return the all tag items objects as list
        """
        tags_css = ".sd-tab-page.tpg-selected div[class*='sd-files']:not([style*='none']) .sd-category-button"
        tags_objects = utillobject.validate_and_get_webdriver_objects(self, tags_css, "Domain tags")
        return tags_objects
        
class ResourceDialog():
    
    def __init__(self, driver):
        self._resource_dialog = Resource_Dialog(driver)
        Resource_Dialog.dialog_name = self._resource_dialog.get_caption_title()
        self.driver = driver
    
    def navigate_to_file(self, folder_path):
        """
        Description : Double click on folders item to navigate 
        :Usage : navigate_to_item("P292->S10046->G123456")
        """
        folder_path_list = folder_path.split("->")
        for folder in folder_path_list :
            folder_obj = self._resource_dialog.get_resource_item_object(folder)
            coreutilobj.double_click(self, folder_obj)
    
    def select_file(self, file_name, folder_path=None):
        """
        Description : Left click on file to select 
        :Usage : select_file("C123456")
        """
        if folder_path != None :
            self.navigate_to_file(folder_path)
        file_obj = self._resource_dialog.get_resource_item_object(file_name)
        coreutilobj.left_click(self, file_obj)
    
    def navigate_to_folder_and_select_file(self,folder_path, file_name):
        """
        Description : Double click on folders item to navigate and left click on file to select
        :Usage : navigate_to_folder_and_select_file("P292->G123456", "C123456")
        """
        self.select_file(file_name, folder_path)
        
    def click_button(self, button_name):
        """
        Description : click on any button in resource dialog.
        :Usage : click_button("Save")
        """
        button_object = self._resource_dialog.get_button_object(button_name)
        coreutilobj.left_click(self, button_object)
        
    def verify_caption_title(self, expected_title, step_num):
        """
        Description : Verify resource title
        :Usage : verify_caption_title("Open", "01.01")
        """
        msg = "Step {0} : Verify resource dialog opens with '{1}' title".format(step_num, expected_title)
        actual_title = self._resource_dialog.get_caption_title()
        utillobject.asequal(self, expected_title, actual_title, msg)
    
    def enter_title(self, title):
        """
        Description : Enter the title in title text box
        :Usage : enter_title("C12345")
        """
        self._resource_dialog.set_title_text(title)
    
    def enter_search_input(self, input_value):
        """
        Description : Enter the input value in search text box
        :Usage : enter_search_input("car")
        """
        searchbox_object = Resource_Dialog.get_search_textbox_object(self)
        utillobject.set_text_to_textbox_using_keybord(self, input_value, text_box_elem=searchbox_object)
    
    def verify_title_textbox_value(self, expected_title, step_num):
        """
        Description : Verify resource title text value
        :Usage : verify_title_textbox_value("Page 1", "01.01")
        """
        msg = "Step {0} : Verify '{1}' appear in title text box".format(step_num, expected_title)
        title_item=Resource_Dialog.get_title_object(self)
        title_input_elem = utillobject.validate_and_get_webdriver_object(self, 'input', "Title text box", parent_object=title_item)
        actual_title = title_input_elem.get_attribute("value").strip()
        utillobject.asequal(self, expected_title, actual_title, msg)
    
    def verify_name_textbox_value(self, expected_name, step_num):
        """
        Description : Verify resource name textbox value
        :Usage : verify_name_textbox_value("Page 1", "01.01")
        """
        msg = "Step {0} : Verify '{1}' appear in name text box".format(step_num, expected_name)
        title_item=Resource_Dialog.get_name_object(self)
        title_input_elem = utillobject.validate_and_get_webdriver_object(self, 'input', "Name text box", parent_object=title_item)
        actual_name = title_input_elem.get_attribute("value").strip()
        utillobject.asequal(self, expected_name, actual_name, msg)
    
    def click_crumb_item(self, item_name):
        """
        Description : Left click on crumb button
        :Usage - click_crumb_item("Domains")
        """
        Resource_Dialog.select_crumb_item(self, item_name)
    
    def click_tab(self, tab_name):
        """
        Description : Left click on tab button
        :Usage - click_tab('Server')
        """
        Resource_Dialog.select_tab_button(self, tab_name)
    
    def verify_files_contains_specific_value(self, value, step_num):
        """
        Description : Read all resource files text and verify whether specific text contains.
        :Usage - verify_files_contains_specific_value("car", "02.01")
        """
        flag = False
        resource_file_objects = Resource_Dialog.get_all_resource_items_object(self)
        for resource_file in resource_file_objects :
            if value.lower() in resource_file.text.lower() :
                flag = True
            else :
                flag = False
                break
        msg = "Step {0} : Verify resource files contains '{1}'".format(step_num, value)
        utillobject.asequal(self, True, flag, msg)
    
    def verify_files(self, expected_files_list, msg, assert_type='asequal'):
        """
        Description : Verify file text
        :Usage - verify_files("['baseapp', 'ibisamp']", "Step 02.01 : Verify files")
        """
        actual_files_list = [file_obj.text.strip() for file_obj in Resource_Dialog.get_all_resource_items_object(self)]
        utillobject.verify_list_values(self, expected_files_list, actual_files_list, msg, assert_type)
    
    def verify_tags(self, expected_tags_list, msg, assert_type='asequal'):
        """
        Description : Verify tags text
        :Usage - verify_tags(['P292', 'P116'], "Step 01.02 : Verify tags")
        """
        actual_tags = [tag.text.strip() for tag in Resource_Dialog.get_tag_objects(self)]
        utillobject.verify_list_values(self, expected_tags_list, actual_tags, msg, assert_type)
        
class OpenDialog(Resource_Dialog):
    Resource_Dialog.dialog_name = 'Open Dialog'   