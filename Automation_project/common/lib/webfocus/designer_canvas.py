from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject
from common.locators.portal_designer import Vfive_Designer
from common.lib.javascript import JavaScript
from common.locators.page_designer_locators import PageDesigner

class Designer_Canvas(BasePage):

    def __init__(self, driver):
        super(Designer_Canvas, self).__init__(driver)
    
    def get_containers_title(self):
        """
        Description : This method will return all visible containers title in page canvas
        """
        containers_title_objs = utillobject.validate_and_get_webdriver_objects(self, Vfive_Designer.containers_title_css, "Containers title")
        containers_title = [container.text.strip() for container in containers_title_objs if container.is_displayed()]
        return containers_title
        
    def get_container_parent_object(self, container_title, container_title_index=1):
        """
        Description : This method will return given container title parent object. 
        If more than containers have same title then you can pass container_title_index to get exact object of container
        """
        containers_title = Designer_Canvas.get_containers_title(self)
        container_title_index_list = [index for index, title in enumerate(containers_title) if title==container_title]
        if len(container_title_index_list) > 0 :
            containers_obj_list = utillobject.validate_and_get_webdriver_objects(self, Vfive_Designer.containers_css, 'Containers')
            containers_obj_list = [container_obj for container_obj in containers_obj_list if container_obj.is_displayed()]
            container_obj = containers_obj_list[container_title_index_list[container_title_index - 1]]
            return container_obj
        else :
            error = "'{0}' container not visible in canvas".format(container_title)
            raise KeyError(error)
    
    def get_page_header_button_obj(self, button_name):
        """
        Description : This method will return all visible page header buttons object as list
        """
        button_css =Vfive_Designer.page_header_css + " div[title='" + button_name + "']"
        button_obj = utillobject.validate_and_get_webdriver_object(self, button_css, button_name)
        return button_obj
     
    def get_container_title_bar_button_obj(self, container_obj, button_name):
        """
        Description : This method will return title bar option example 'Maximize' or 'Options'
        """
        button_css = PageDesigner.PANEL_TITLE_CSS.format(button_name)
        button_obj = utillobject.validate_and_get_webdriver_object(self, button_css, button_name, parent_object=container_obj)
        return button_obj
    
    def get_panel_container_obj(self, container_obj):
        """
        Description : This method will return panel container object based on given container title
        """
        panel_container_ob = utillobject.validate_and_get_webdriver_object(self, Vfive_Designer.panel_container_css, 'Panel Container', container_obj)
        return panel_container_ob
        
    def get_panel_add_container_object(self, container_object, container_type):
        """
        Description : This method will return the add content button object.
        :@param : parent_obj - parent object of add content button. Add content button display on different containers so we should pass container object as parent
        """
        if container_type not in ['panel', 'tab', 'carousel', 'accordion']:
            raise KeyError("Please pass value from 'panel', 'tab', 'carousel', 'accordion'")
        cotainer_dict = {'panel':"div[class*='fa-plus-circle']", 'tab':".tpg-selected div[class*='fa-plus-circle']",
                         'carousel':"[title='Add content']:not([style*='none']) div[class*='fa-plus-circle']", 'accordion':".acc-pg-stretch div[class*='fa-plus-circle']"}
        add_content_button_icon_obj = utillobject.validate_and_get_webdriver_object(self, cotainer_dict[container_type], 'Add content button icon', container_object)
        return add_content_button_icon_obj
    
    def get_panel_type(self, container_object, container_type):
        """
        Description : This method will return panel type object example 'tab', 'carousel', 'accordion' .
        """
        if container_type not in ['tab', 'carousel', 'accordion']:
            raise KeyError("Please pass value from 'tab', 'carousel', 'accordion'")
        cotainer_dict = {'tab':".ibx-csl-items-box", 'carousel':".ibx-csl-page-markers[aria-label='Carousel Pages']", 
                         'accordion':".pd-container-content"}
        add_content_button_icon_obj = utillobject.validate_and_get_webdriver_object(self, cotainer_dict[container_type], '{0} panel'.format(container_type), container_object)
        return add_content_button_icon_obj
    
    def get_blank_canvas_text(self):
        """
        Description : This method will return blank canvas page text
        """
        blank_canvas_obj = utillobject.validate_and_get_webdriver_object(self, "#pagespane", 'Blank page canvas')
        actual_text = blank_canvas_obj.text.strip()
        return actual_text
    
    def get_page_header_title(self):
        """
        Description : 
        """
        page_header_title_obj = utillobject.validate_and_get_webdriver_object(self, Vfive_Designer.page_header_title_css, 'Page Header')
        actual_title = page_header_title_obj.text.strip()
        return actual_title
    
    def get_page_header_visible_buttons(self):
        """
       Description : This method will return page header visible buttons
        """
        current_button_icons = {'Share' : 'fa fa-share-alt', 'Stop sharing' : 'fa fa-share-alt', 'Refresh' : 'ds-icon-refresh', 'Bookmarks' : 'fas fa-bookmark', 'Delete' : 'fa fa-trash', 'Show filters' : 'ds-icon-filter',
                                'Export to file':'fa-file-export'}
        current_button_content = {'Share' : '\uf1e0', 'Stop sharing' : '\uf1e0', 'Refresh' : '\ue9ea', 'Bookmarks' : '\uf02e', 'Delete' : '\uf1f8', 'Show filters' : '\uea40','Export to file':'\f56e'}
        buttons_obj_list = utillobject.validate_and_get_webdriver_objects(self, Vfive_Designer.page_header_buttons_css, 'Page Header Buttons')
        actual_buttons_name_list = []
        visible_buttons_obj = [obj for obj in buttons_obj_list if obj.is_displayed()]
        for button_obj in visible_buttons_obj :
            button_title = utillobject.get_element_attribute(self, button_obj, 'title')
            if button_title in current_button_icons.keys() :
                button_icon_css = "div[class*='ibx-label-glyph'][class*='ibx-label-icon'][class*='{0}']".format(current_button_icons[button_title])
                button_icon_obj = utillobject.validate_and_get_webdriver_object(self, button_icon_css, button_obj, button_obj)
                button_icon_content = JavaScript.get_element_before_style_properties(self, button_icon_obj, 'content').replace('"', '').encode("utf-8")
                if button_icon_content == current_button_content[button_title].encode("utf-8") :
                    actual_buttons_name_list.append(button_title)    
            else :
                error = "'{0}' new button visible in page header. Icon css should add for this button in the method".format(button_title)
                raise KeyError(error)    
        return actual_buttons_name_list
    
    def get_add_content_button_icon_visible_status(self, add_content_object):
        """
        Description : This method used to verify all or specific visible container buttons in page canvas.
        """
        if add_content_object.is_displayed() :
            expected_icon_value = "\uf055".encode()
            actual_icon_value=JavaScript.get_element_before_style_properties(self, add_content_object, 'content').replace('"', '').encode()
            visible_status = True if expected_icon_value==actual_icon_value else False
        else :
            visible_status = False
        return visible_status
    
    def get_container_title_bar_visible_buttons(self, container_title, container_title_index=1):
        """
        Description : This method will return container title bar visible buttons
        """
        current_button_icons = {'Maximize' : 'ibx-glyph-expand', 'Restore' : 'ibx-glyph-expand', 'Options' : 'ibx-glyph-ellipsis-v'}
        current_button_content = {'Maximize' : '\uf065', 'Restore' : '\uf065', 'Options' : '\ue96d'}
        container_obj = Designer_Canvas.get_container_parent_object(self, container_title, container_title_index)
        buttons_obj_list = utillobject.validate_and_get_webdriver_objects(self, Vfive_Designer.container_title_bar_buttons_css, 'Container title bar buttons', container_obj)
        actual_buttons_name_list = []
        visible_buttons_obj = [obj for obj in buttons_obj_list if obj.is_displayed()]
        for button_obj in visible_buttons_obj :
            button_title = utillobject.get_element_attribute(self, button_obj, 'title')
            if button_title in current_button_icons.keys() :
                button_icon_css = "div[class*='ibx-label-glyph'][class*='ibx-label-icon'][class*='{0}']".format(current_button_icons[button_title])
                button_icon_obj = utillobject.validate_and_get_webdriver_object(self, button_icon_css, button_title, parent_object=button_obj)
                button_icon_content = JavaScript.get_element_before_style_properties(self, button_icon_obj, 'content').replace('"', '').encode("utf-8")
                if button_icon_content == current_button_content[button_title].encode("utf-8") :
                    actual_buttons_name_list.append(button_title)    
            else :
                error = "'{0}' new button visible in container title bar. Icon css should add for this button in the method".format(button_title)
                raise KeyError(error)
        return actual_buttons_name_list
    
    def get_dialog_button_object(self, button_name):
        """
        Description : This method will return dialog(Delete, Save and etc dialogs) buttons objects
        :arg - button_name = name of button (Save, Detete, OK)
        """
        dialog_buttons_obj = utillobject.validate_and_get_webdriver_objects(self, Vfive_Designer.dialog_buttons_css, 'Dialog buttons')
        dialog_button_index = JavaScript.find_element_index_by_text(self, dialog_buttons_obj, button_name)
        if dialog_button_index == None :
            error = "{0} button doesn't displayed in dialog box"
            raise KeyError(error)
        else :
            dialog_button_obj = dialog_buttons_obj[dialog_button_index]
            return dialog_button_obj
