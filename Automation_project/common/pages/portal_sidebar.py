from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.portal_designer import Vfive_Designer
import sys
import time
from selenium.common.exceptions import ElementNotVisibleException
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class Two_Level_SideBar(BasePage):
        
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Two_Level_SideBar, self).__init__(driver)
        self._utillity = UtillityMethods(self.driver)
        self._coreutility = CoreUtillityMethods(self.driver)
        
    def get_all_folders_object(self):
        """
        Description : This method will return page folders object as list
        """
        page_folder_objects = self._utillity.validate_and_get_webdriver_objects(Vfive_Designer.left_panel_page_folder_group_css, 'Left side bar folders')
        return page_folder_objects
    
    def get_folders_name(self):
        """
        Description : This method will return page folders name values as list
        """
        page_folder_objects = self.get_all_folders_object()
        page_folders_name_list = [folder.find_element_by_css_selector('.ibx-accordion-button-text').text.strip() for folder in page_folder_objects]
        return page_folders_name_list
    
    def get_folder_object_index(self, folder_name):
        """
        Description : This method will return page folders object index
        """
        folders_name_list = self.get_folders_name()
        if folder_name in  folders_name_list :
            folder_index = folders_name_list.index(folder_name)
            return folder_index
        else :
            error_msg = "'{0}' folder doesn't exist in left side bar in portal page".format(folder_name)
            raise FileNotFoundError(error_msg)
    
    def get_folder_object(self, folder_name):
        """
        Description : This method will return page folders object
        """
        folders_object = self.get_all_folders_object()
        folder_index = self.get_folder_object_index(folder_name)
        folder_object = folders_object[folder_index]
        return folder_object
    
    def get_folder_group_object(self, folder_name):
        """
        Description : This method will return page folders group object
        """
        all_folder_group_objects = self._utillity.validate_and_get_webdriver_objects(Vfive_Designer.left_panel_page_folder_group_css, "Left side bar folder group")
        folder_object_index = self.get_folder_object_index(folder_name)
        folder_group_object = all_folder_group_objects[folder_object_index]
        return folder_group_object
    
    def get_folder_all_items_object(self, folder_name):
        """
        Description : This method will return specific page folder items object
        """
        folder_group_object = self.get_folder_group_object(folder_name)
        folder_all_items_object = self._utillity.validate_and_get_webdriver_objects(".ibx-accordion-page-content .bundle-folder-item", "Left slid bar foldr pages", folder_group_object)
        return folder_all_items_object
    
    def get_folder_items_name(self, folder_name):
        """
        Description : This method will return specific folder all pages name
        """
        items_obj = self.get_folder_all_items_object(folder_name)
        folder_items_name_list = [item.text.strip() for item in items_obj]
        return folder_items_name_list
    
    def get_folder_item_object(self, folder_name, item_name):
        """
        Description : This method will return specific folder item object 
        """
        folder_items_name_list = self.get_folder_items_name(folder_name)
        folder_items_list = self.get_folder_all_items_object(folder_name)
        if item_name in folder_items_name_list :
            item_index = folder_items_name_list.index(item_name)
            item_object = folder_items_list[item_index]
            return item_object
        else :
            error_msg = "'{0}' page doesn't exist under the '{1}' folder in left side bar in portal page".format(item_name, folder_name)
            raise FileNotFoundError(error_msg)
        
    def expand_or_collapse_folder(self, folder_name, action='expand'):
        """
        Description : This method will expand or collapse folder 
        """
        folder_object = self.get_folder_object(folder_name)
        expand_or_collapse_icon_css = Vfive_Designer.left_panel_page_folder_expand_icon_css if action == 'expand' else Vfive_Designer.left_panel_page_folder_collapse_css
        expand_or_collapse_icon_obj = folder_object.find_elements_by_css_selector(expand_or_collapse_icon_css)
        if expand_or_collapse_icon_obj != [] :
            self._coreutility.left_click(expand_or_collapse_icon_obj[0])
    
    def get_top_folder(self):
        """
        Description : This method will return bundle top folders
        """
        folder_css=".pvd-left-main-panel[data-ibx-type='ibxAccordionPane']"
        top_folder_object = self._utillity.validate_and_get_webdriver_object(folder_css, 'Top folder')
        return top_folder_object
    
    def select_page_from_top_folder(self, page_name):
        """
        Description : This method will select page from bundle top folder.
        """
        page_css = ".bundle-folder-item[data-ibx-type='pvdAccordionItem'] .ibx-label-text"
        top_folder_obj = self.get_top_folder()
        page_objects = self._utillity.validate_and_get_webdriver_objects(page_css, page_name, parent_object=top_folder_obj)
        page_object = [page_element for page_element in page_objects if page_element.text.strip()==page_name]
        if page_object[0] is not None:
            self._coreutility.left_click(page_object[0])
        else:
            raise LookupError('{0} page not found in Bundle top folder.'.format(page_name.capitalize()))
    
    def verify_page_from_top_folder(self, page_name_list, compare_type, msg):
        """
        Description : This method will verify page from bundle top folder.
        """
        page_css = ".bundle-folder-item[data-ibx-type='pvdAccordionItem'] .ibx-label-text"
        top_folder_obj = self.get_top_folder()
        page_objects = self._utillity.validate_and_get_webdriver_objects(page_css, 'Bundle top folder pages', parent_object=top_folder_obj)
        page_names_list = [page_element.text.strip() for page_element in page_objects]
        if compare_type == 'asin':
            for page_name in page_name_list:
                if page_name in page_names_list:
                    status = True
                else:
                    status = page_name
                    break
            self._utillity.asequal(True, status, msg)
        if compare_type == 'asequal':
            self._utillity.as_List_equal(page_name_list, page_names_list, msg)
        if compare_type == 'asnotin':
            for page_name in page_name_list:
                if page_name not in page_names_list:
                    status = True
                else:
                    status = page_name
                    break
            self._utillity.asequal(True, status, msg)
    
    def verify_selected_page_from_top_folder(self, page_name, msg):
        """
        Description : This method will verify selected page from bundle top folder.
        """
        page_css = ".bundle-folder-item[data-ibx-type='pvdAccordionItem'].pvd-left-main-panel-content-button-active .ibx-label-text"
        top_folder_obj = self.get_top_folder()
        selected_page_text = self._utillity.validate_and_get_webdriver_object(page_css, 'Bundle top folder selected page', parent_object=top_folder_obj).text.strip()
        self._utillity.asequal(page_name, selected_page_text, msg)
    
    def click_on_new_page_from_top_folder(self):
        """
        Description : This method will click on new page + icon from bundle top folder.
        """
        page_css = ".bundle-folder-item[data-ibx-type='pvdAccordionItem'].user-page-add .ibx-label-text"
        top_folder_obj = self.get_top_folder()
        new_page_object = self._utillity.validate_and_get_webdriver_object(page_css, 'Bundle top folder new page create', parent_object=top_folder_obj)
        self._coreutility.left_click(new_page_object)
    
    def rename_page_name_from_top_folder(self, page_name, name_to_change):
        """
        Description :  This method used to left click on page under the specific folder
        """
        page_css = ".bundle-folder-item[data-ibx-type='pvdAccordionItem']"
        top_folder_obj = self.get_top_folder()
        page_objects = self._utillity.validate_and_get_webdriver_objects(page_css, page_name, parent_object=top_folder_obj)
        page_object = [page_element for page_element in page_objects if page_element.text.strip()==page_name]
        if page_object[0] is not None:
            self._coreutility.double(page_object[0])
        else:
            raise LookupError('{0} page not found in Bundle top folder.'.format(page_name.capitalize()))
        rename_input_object = self._utillity.validate_and_get_webdriver_object('input', '{0} rename input box'.format(page_name), parent_object=page_object[0])
        self._utillity.set_text_to_textbox_using_keybord(name_to_change, text_box_elem=rename_input_object)
        self._utillity.synchronize_with_visble_text_within_parent_object(page_object[0], 'input', name_to_change, 90)
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard.press('ENTER')
           
    def select_page_from_folder(self, folder_name, page_name):
        """
        Description :  This method used to left click on page under the specific folder
        """
        self.expand_or_collapse_folder(folder_name)
        page_object = self.get_folder_item_object(folder_name, page_name)
        self._coreutility.left_click(page_object)
    
    def rename_page_under_the_folder(self, folder_name, page_name, name_to_change):
        """
        Description :  This method used to left click on page under the specific folder
        """
        self.expand_or_collapse_folder(folder_name)
        page_object = self.get_folder_item_object(folder_name, page_name)
        rename_obj=self._utillity.validate_and_get_webdriver_object(Vfive_Designer.LABEL_TEXT_CSS, page_name, parent_object=page_object)
        self._utillity.set_text_to_textbox_using_keybord(name_to_change, text_box_elem=rename_obj, click_type='double')
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard.press('ENTER')

    def verify_folder_expanded_or_collapsed_icon(self, folder_name, verify_icon, msg):
        """
        Description : This method will verify folder expanded or collapsed
        example usage : verify_folder_expanded_or_collapsed_icon('My Page', 'expanded', 'Step 01.1 : Verify My Page folder is expanded')
        example usage : verify_folder_expanded_or_collapsed_icon('My Page', 'collapsed', 'Step 01.1 : Verify My Page folder is collapsed')
        """
        expected_icon_text = "chevron_right"
        folder_object = self.get_folder_object(folder_name)
        expanded_or_collapsed_icon_css = Vfive_Designer.left_panel_page_folder_expand_icon_css if verify_icon == 'expanded' else Vfive_Designer.left_panel_page_folder_collapse_css
        expanded_or_collapsed_icon_obj = self._utillity.validate_and_get_webdriver_object(expanded_or_collapsed_icon_css, 'Left side bar folder ' + verify_icon + ' icon', folder_object)
        actual_icon_text = expanded_or_collapsed_icon_obj.text.strip()
        if actual_icon_text == expected_icon_text and expanded_or_collapsed_icon_obj.is_displayed() :
            status = True
        else :
            status = False
        self._utillity.asequal(True, status, msg)
        
    def verify_folders(self, expected_folders_list, msg, assert_type='asequal'):
        """
        Description : This method will verify all folders or any specific folders are displayed in left side bar 
        Example usage : verify_folders(['My Page1', 'My Page2', 'My Page3'], 'Step 01.1 : Verify 3 folders are displayed')
        Example usage : verify_folders(['My Page1'], 'Step 01.1 : Verify My Page1 folder is displayed', assert_type='asin')
        """
        actual_folders_list = self.get_folders_name()
        self._utillity.verify_list_values(expected_folders_list, actual_folders_list, msg, assert_type)
    
    def verify_pages_in_folder(self, folder_name, expected_pages_list, msg, assert_type='asequal'):
        """
        Description : This method will verify all pages or any specific pages are displayed under the folder in left side bar 
        Example usage : verify_folders('My Page1', ['Page 1', 'Page 2', 'Page 3'], 'Step 01.1 : Verify 3 pages are displayed under the My Page1 folder')
        Example usage : verify_folders('My Page1', ['Page 1'], 'Step 01.1 : Verify Page1 pages is displayed under the My Page1 folder', assert_type='asin')
        """
        actual_pages_list = self.get_folder_items_name(folder_name)
        self._utillity.verify_list_values(expected_pages_list, actual_pages_list, msg, assert_type)

class Three_Level_SideBar(BasePage):
        
    """ Inherit attributes of the parent class = Baseclass"""

    def __init__(self, driver):
        super(Three_Level_SideBar, self).__init__(driver)
        self._utillity = UtillityMethods(self.driver)
        self._coreutility = CoreUtillityMethods(self.driver)
        
    def get_three_level_top_folder_objects(self):
        """
        Description : This method will return top folders 
        """
        folder_css = '{0} {1} {2}'.format(Vfive_Designer.TOP_LEVEL_FOLDER_PARENT_CSS, Vfive_Designer.FOLDER_CSS, Vfive_Designer.LABEL_TEXT_CSS)
        top_folder_object = self._utillity.validate_and_get_webdriver_objects(folder_css, 'Top folder')
        return top_folder_object
    
    def get_three_level_top_folders_name(self):
        """
        Description : This method will return top folders name values as list
        """
        folder_objects = self.get_three_level_top_folder_objects()
        page_folders_name_list = [folder.text.strip() for folder in folder_objects if folder.is_displayed()]
        return page_folders_name_list
    
    def get_three_level_top_folders_object(self, folder_name):
        """
        Description : This method will return top folder object
        """
        folder_name_list = self.get_three_level_top_folders_name()
        if folder_name in folder_name_list :
            folder_objects = self.get_three_level_top_folder_objects()
            folder_object = folder_objects[folder_name_list.index(folder_name)]
            return folder_object
        else :
            error_msg = "[{0}] folder name doesn't displayed.".format(folder_name)
            raise ElementNotVisibleException(error_msg)
    
    def verify_three_level_top_folders(self, expected_tabs_list, msg, assert_type='asequal'):
        """
        Description : This method will verify top folder names
        @usage  : verify_three_level_top_folders(['Page 1', 'My Pages'], 'Step 01.1 : Verify ')
        """
        actual_tabs_list = self.get_three_level_top_folders_name()
        self._utillity.verify_list_values(expected_tabs_list, actual_tabs_list, msg, assert_type)
     
    def verify_three_level_top_folder_color(self, folder_name, expected_color_name, msg):
        """
        Description : This method will verify top folder background color
        @usage  : verify_three_level_top_folder_color('Pages 1', 'blue', 'Step 01.01 : Verify 'page 1' folder color')
        """
        folder_object = self.get_three_level_top_folders_object(folder_name)
        self._utillity.verify_element_color_using_css_property(None, expected_color_name, msg, attribute='background-color', element_obj=folder_object)
     
    def verify_selected_three_level_top_folder(self, selected_folder, msg):
        """
        Description : This method will verify selected top folder
        @usage  : verify_selected_action_bar_new_text_resource_tab(['Common'], 'Step 01.01 : Verify 'Common' tab is selected as default')
        """
        selected_tab_css = '{0} {1} {2}'.format(Vfive_Designer.TOP_LEVEL_FOLDER_PARENT_CSS, Vfive_Designer.SELECTED_FOLDER_CSS, Vfive_Designer.LABEL_TEXT_CSS)
        selected_tab_obj = self._utillity.validate_and_get_webdriver_object(selected_tab_css, 'Selected top folder')
        actual_selected_folder = selected_tab_obj.text.strip()
        self._utillity.asequal(selected_folder, actual_selected_folder, msg)
         
    def select_three_level_top_folder(self, folder_name):
        '''
        Description : This function is used to select top folder
        :Usage select_three_level_top_folder('Designer')
        '''
        folder_object = self.get_three_level_top_folders_object(folder_name)
        self._coreutility.left_click(folder_object)
    
    def get_top_folders_item_objects(self):
        """
        Description : This method will return page folders object as list
        """
        folder_css = '{0} {1}'.format(Vfive_Designer.left_panel_page_folders_container_css, Vfive_Designer.LEFT_PANEL_FOLDER_CSS)
        try:
            page_folder_objects = self._utillity.validate_and_get_webdriver_objects(folder_css, 'Left side folders')
            return page_folder_objects
        except:
            return []
    
    def get_top_folders_item_object_name(self):
        """
        Description : This method will return top folders item name values as list
        """
        page_folder_objects = self.get_top_folders_item_objects()
        if len(page_folder_objects) != 0:
            page_folders_name_list = [self._utillity.validate_and_get_webdriver_object(Vfive_Designer.LABEL_TEXT_CSS, 'Navigation page', parent_object=folder).text.strip() for folder in page_folder_objects if folder.is_displayed()]
            return page_folders_name_list
        else:
            return []
    
    def get_top_folders_item_object(self, folder_name):
        """
        Description : This method will return top folder item object
        """
        folder_name_list = self.get_top_folders_item_object_name()
        if folder_name in folder_name_list :
            folder_objects = self.get_top_folders_item_objects()
            folder_object = folder_objects[folder_name_list.index(folder_name)]
            return folder_object
        else :
            error_msg = "[{0}] folder name doesn't displayed.".format(folder_name)
            raise ElementNotVisibleException(error_msg)
    
    def verify_top_folder_items(self, expected_tabs_list, msg, assert_type='asequal'):
        """
        Description : This method will verify top folder item names
        @usage  : verify_top_folder_items(['Page 1', 'Page 2'], 'Step 01.1 : Verify ')
        """
        actual_tabs_list = self.get_top_folders_item_object_name()
        self._utillity.verify_list_values(expected_tabs_list, actual_tabs_list, msg, assert_type)
     
    def verify_top_folder_item_color(self, folder_name, expected_color_name, msg):
        """
        Description : This method will verify top folder background color
        @usage  : verify_three_level_top_folder_color('Pages 1', 'blue', 'Step 01.01 : Verify 'page 1' folder color')
        """
        folder_object = self.get_top_folders_item_object(folder_name)
        self._utillity.verify_element_color_using_css_property(None, expected_color_name, msg, attribute='background-color', element_obj=folder_object)
     
    def verify_selected_top_folder_item(self, selected_folder, msg):
        """
        Description : This method will verify selected top folder item
        @usage  : verify_selected_action_bar_new_text_resource_tab(['Common'], 'Step 01.01 : Verify 'Common' tab is selected as default')
        """
        selected_tab_css = '{0} {1} {2}'.format(Vfive_Designer.left_panel_page_folders_container_css, Vfive_Designer.SELECTED_LEFT_PANEL_FOLDER_CSS, Vfive_Designer.LABEL_TEXT_CSS)
        selected_tab_obj = self._utillity.validate_and_get_webdriver_object(selected_tab_css, 'Selected top folder')
        actual_selected_folder = selected_tab_obj.text.strip()
        self._utillity.asequal(self, selected_folder, actual_selected_folder, msg)
         
    def select_top_folder_item(self, folder_name):
        '''
        Description : This function is used to select top folder item
        :Usage select_top_folder_item('Designer')
        '''
        folder_object = self.get_top_folders_item_object(folder_name)
        self._coreutility.left_click(folder_object)
    
    def click_on_new_page_from_top_folder_item(self):
        """
        Description : This method will click on new page + icon from Top folder item.
        :Usage click_on_new_page_from_top_folder_item()
        """
        new_page_css = '{0} {1} {2}'.format(Vfive_Designer.left_panel_page_folders_container_css, Vfive_Designer.ADD_NEW_PAGE_CSS, Vfive_Designer.LABEL_TEXT_CSS)
        new_page_object = self._utillity.validate_and_get_webdriver_object(new_page_css, 'Top folder new page create')
        self._coreutility.left_click(new_page_object)
    
    def verify_plus_sign_from_top_folder_item(self, msg):
        """
        Description : This method used to verify plus sign under top folder item
        :Usage verify_plus_sign_from_top_folder_item('Step 9 Verify')
        """
        new_page_css = '{0} {1} {2}'.format(Vfive_Designer.left_panel_page_folders_container_css, Vfive_Designer.ADD_NEW_PAGE_CSS, Vfive_Designer.LABEL_TEXT_CSS)
        new_page_object = self._utillity.validate_and_get_webdriver_object(new_page_css, 'Top folder new page create').text.strip()
        expected='+'
        self._utillity.asequal(str(expected), str(new_page_object), msg)
    
    def rename_page_name_from_top_folder(self, folder_name, name_to_change):
        """
        Description :  This method used to left click on page under the specific folder
        :Usage click_on_new_page_from_top_folder_item()
        """
        folder_object = self.get_top_folders_item_object(folder_name)
        self._coreutility.double_click(folder_object)
        self._utillity.set_text_to_textbox_using_keybord(name_to_change, text_box_elem=folder_object)
        time.sleep(5)
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard.press('ENTER')
           
class New_Page_Template_Window(BasePage):
    
    def __init__(self, driver):
        
        super(New_Page_Template_Window, self).__init__(driver)
        self._utillity = UtillityMethods(self.driver)
        self._coreutility = CoreUtillityMethods(self.driver)
    
    def get_templates_object(self):
        """
        Description : This method will return the new page template options object as list
        """
        templates_object = self._utillity.validate_and_get_webdriver_objects(Vfive_Designer.new_page_template_options_css, "New page templates")
        return templates_object
    
    def get_templates_name(self):
        """
        Description : This method will return the new page template options name as list
        """
        templates_object = self.get_templates_object()
        templates_name_list = [template.text.strip() for template in templates_object]
        return templates_name_list
    
    def select_template(self, template_name):
        """
        Description : This method will select template to create new page
        """
        templates_name_list = self.get_templates_name()
        if template_name in templates_name_list :
            templates_object = self.get_templates_object()
            template_index = templates_name_list.index(template_name)
            template_obj = templates_object[template_index]
            self._coreutility.left_click(template_obj)
        else :
            error_msg = "'{0}' template currently doesn't display in new page template window".format(template_name)
            raise KeyError(error_msg)
    
    def click_on_link_to_an_existing_page_button(self):
        """
        Description : This method will click on Link to an existing page button 
        """
        existing_page_button_obj = self._utillity.validate_and_get_webdriver_object(Vfive_Designer.open_existing_page_button_css, 'Link to an existing page button')
        self._coreutility.left_click(existing_page_button_obj)
    
    def close_new_page_template_window(self):
        """
        Description : This method will click on close widow icon in new page template window 
        """
        close_icon_obj = self._utillity.validate_and_get_webdriver_object(Vfive_Designer.new_page_template_window_close_icon_css, 'New page template close window icon')
        self._coreutility.left_click(close_icon_obj)
    
    def verify_new_page_template_window_is_displayed(self, msg, expected_window_title='New Page'):
        """
        Description : This method will verify whether new page template window is displayed 
        """
        actual_template_window_title_obj = self._utillity.validate_and_get_webdriver_object(Vfive_Designer.new_page_template_window_title_bar_css, 'New page template title bar')
        actual_template_window_title = actual_template_window_title_obj.text.strip()
        self._utillity.asequal(expected_window_title, actual_template_window_title, msg)
        
    def verify_templates(self, expected_templates, msg, assert_type='asequal'):
        """
        Description : This method will verify visible all or specific templates
        """
        actual_templates = self.get_templates_name()
        self._utillity.verify_list_values(expected_templates, actual_templates, msg, assert_type)
    