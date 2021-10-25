from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.support import expected_conditions as EC
from common.locators import page_designer_design as DesignLocators
from common.lib.webfocus.designer_canvas import Designer_Canvas
from common.locators.page_designer_locators import PageDesigner as PD_LOCATORS
from common.locators.page_designer_design import FilterModalWindow as FilterModalWindowLocators
from common.locators.page_designer_design import ContentTab as ContentTab_Locators
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as pd_miscelaneous
from common.lib.core_utility import CoreUtillityMethods as coreutils
from common.pages.portal_canvas import Portal_canvas
from common.lib.global_variables import Global_variables
from common.lib.javascript import JavaScript as javascript
from common.lib.utillity import UtillityMethods as utils
from selenium.webdriver.support import color
from selenium.webdriver.common.keys import Keys
from common.lib.base import BasePage
from common.pages.wf_mainpage import Wf_Mainpage
import time, pyautogui
from common.lib.webfocus import poptop_dialog
from selenium.webdriver import ActionChains
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
#     import uiautomation
    import keyboard

class PageDesignerDesign(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(PageDesignerDesign, self).__init__(driver)
    
    def invoke_page_designer(self, mrid=None, mrpass=None, folder_path=None, from_designer_group=False):
        """
        Descriptions : This method used to invoke page designer page from given folder path
        example usage : invoke_page_designer()
        """
        folder_path=pd_miscelaneous.get_page_designer_folder_path(self) if folder_path==None else folder_path
        pd_miscelaneous.invoke_page_designer(self, folder_path, mrid, mrpass, from_designer_group)
        
    def invoke_page_designer_and_select_template(self, template_name, mrid=None, mrpass=None, folder_path=None, from_designer_group=False):
        """
        Descriptions : This method used to invoke page designer page and select template
        :arg- template names : 'Blank', 'Grid 2-1', 'Grid 4-2-1', 'Grid 3-3-3'
        example usage : invoke_page_designer_and_select_template('Blank')
        """
        PageDesignerDesign.invoke_page_designer(self, folder_path, mrid, mrpass, from_designer_group)
        pd_miscelaneous.select_page_designer_template(self, template_name)
    
    def select_option_from_carousel_items(self, option_name):
        """
        Descriptions : This method used to select carousel items
        :arg-option_name : 'Containers' or 'Content' or 'Controls'
        example usage : select_option_from_carousel_items('Containers')
        """
        if option_name not in ['Containers', 'Content', 'Controls']:
            raise KeyError("Please pass option_name from 'Containers', 'Content', 'Controls'")
        resource_panel_element = utils.validate_and_get_webdriver_object(self, ".pd-left-pane", 'Resource Panel')
        margin_value = utils.get_element_css_propery(self, resource_panel_element, 'margin-left')
        opacity_value = utils.get_element_css_propery(self, resource_panel_element, 'opacity')
        if (int(margin_value.replace('px','')) > -100) and (int(opacity_value) is 1):
            item_container_css = ".ibx-csl-items-container [title='{0}']".format(option_name)
            item_container_element = utils.validate_and_get_webdriver_object(self, item_container_css, option_name, parent_object=resource_panel_element)
            coreutils.left_click(self, item_container_element)
            synch_item_container_css = ".ibx-csl-items-container .checked[title='{0}']".format(option_name)
            utils.synchronize_with_number_of_element_within_parent_object(self, resource_panel_element, synch_item_container_css, 1, 19)
        else:
            raise LookupError('Resource Panel not visible and opened.')
    
    def collapse_content_folder(self, folder_path, left_click=True):
        """
        Description : This method will collapse content folders
        example usage1 : expand_pd_content_folder_and_select_item('Auto Link Targets->Reports->Retail Samples')
        """
        folder_list = folder_path.split('->')
        for folder in folder_list :
            expanded_folder_obj = utils.validate_and_get_webdriver_object(self, ContentTab_Locators.EXPANDED_CONTENT_LABEL_CSS, 'Collapse pd content folder')
            if expanded_folder_obj.text.strip() == folder:
                if left_click == True:
                    coreutils.left_click(self, expanded_folder_obj)
                else:
                    coreutils.python_doubble_click(self, expanded_folder_obj)
                time.sleep(1)
            else:
                error_msg = "Unable to find {0} folder in page designer domains content tab".format(folder)
                raise KeyError(error_msg)
            
    def drag_container_item_to_blank_canvas(self, container_name_to_drag, blank_grid_index_to_drop, section_num=1, element_location='middle', xoffset=0, yoffset=0):
        """
        Descriptions : This method used to drag container item to blank canvas
        :arg- container_name_to_drag : 'Panel' or 'Tab' or 'Carousel' or 'Accordion' or 'Grid'
        :arg- blank_grid_index_to_drop = Position of bank grid to drop item ( blank_grid_index start from 1)
        example usage : drag_container_item_to_blank_canvas('Panel', 1)
        """
        if container_name_to_drag not in ['Panel', 'Tab', 'Carousel', 'Accordion', 'Grid']:
            raise KeyError("Please pass container_name_to_drag from 'Panel', 'Tab', 'Carousel', 'Accordion', 'Grid'")
        resource_panel_element = utils.validate_and_get_webdriver_object(self, ".pd-left-pane", 'Resource Panel')
        margin_value = utils.get_element_css_propery(self, resource_panel_element, 'margin-left')
        opacity_value = utils.get_element_css_propery(self, resource_panel_element, 'opacity')
        if (int(margin_value.replace('px','')) > -100) and (int(opacity_value) is 1):
            basic_container_css = ContentTab_Locators.BASIC_CONTAINER_ITEM_CSS
            item_container_css = basic_container_css.format(container_name_to_drag.lower())
            item_container_element = utils.validate_and_get_webdriver_object(self, item_container_css, container_name_to_drag, parent_object=resource_panel_element)
            blank_grid_css="div[class='pd-page-section-grid-box']"
            section_obj = PageDesignerDesign._get_page_section_object(self, section_num)
            blank_grid_obj=section_obj.find_elements_by_css_selector(blank_grid_css)
            source_cord=coreutils.get_web_element_coordinate(self, item_container_element)
            target_cord=coreutils.get_web_element_coordinate(self, blank_grid_obj[blank_grid_index_to_drop-1], element_location=element_location, xoffset=xoffset, yoffset=yoffset)
            coreutils.drag_and_drop(self, source_cord['x'], source_cord['y'], target_cord['x'], target_cord['y'])
        else:
            raise LookupError('Resource Panel not visible and opened.')
    
    def drag_basic_container_to_canvas_container(self, basic_container_name, canvas_container_title,location,canvas_container_position=1):
        """
        Descriptions : This method will drag container to canvas container
        :Usage - drag_container_to_canvas_container("Grid", "Panel1")'
        """
        canvas_container_object =pd_miscelaneous.get_pd_container_object(self, canvas_container_title, canvas_container_position)
        basic_container_object = PageDesignerDesign.get_basic_container_object(self, basic_container_name)
        source_cord=coreutils.get_web_element_coordinate(self, basic_container_object)
        target_cord=coreutils.get_web_element_coordinate(self, canvas_container_object,location)
        coreutils.drag_and_drop(self, source_cord['x'], source_cord['y'], target_cord['x'], target_cord['y'])
    
    def drag_repository_widget_to_canvas_container(self, widget_name, canvas_container_title, canvas_container_position=1):
        """
        Descriptions : This method will drag container to canvas container
        :Usage - drag_container_to_canvas_container("Grid", "Panel1")'
        """
        canvas_container_object =pd_miscelaneous.get_pd_container_object(self, canvas_container_title, canvas_container_position)
        widget_object = PageDesignerDesign.get_repository_widget_object(self, widget_name)
        source_cord=coreutils.get_web_element_coordinate(self, widget_object)
        target_cord=coreutils.get_web_element_coordinate(self, canvas_container_object)
        coreutils.drag_and_drop(self, source_cord['x'], source_cord['y'], target_cord['x'], target_cord['y'])
    
    def drag_canvas_container_to_section_cell(self, canvas_container_title, section_cell_num, canvas_container_position=1, section_num=1):
        """
        Descriptions : This method will drag canvas container to blank section cell
        :Usage - drag_canvas_container_to_section_cell("Panel1", 4)'
        """
        canvas_container_object =pd_miscelaneous.get_pd_container_object(self, canvas_container_title, canvas_container_position)
        section= PageDesignerDesign._get_page_section_object(self, section_num)
        section_cell = utils.validate_and_get_webdriver_objects(self, "div[class='pd-page-section-grid-box']", "Section cell", section)
        source_cord=coreutils.get_web_element_coordinate(self, canvas_container_object)
        target_cord=coreutils.get_web_element_coordinate(self, section_cell[section_cell_num-1])
        coreutils.drag_and_drop(self, source_cord['x'], source_cord['y'], target_cord['x'], target_cord['y'])
        
    def verify_container_style_color(self, container_title, color_name, step_num, container_position=1):
        """
        Descriptions : This method will verify the container style color
        :Usage - verify_container_style_color("Panel1", 'blue')
        """
        title_bar_css = ".pd-container-title-bar"
        container_object = pd_miscelaneous.get_pd_container_object(self, container_title, container_position)
        container_title_bar_obj = utils.validate_and_get_webdriver_object(self, title_bar_css, container_title + " title bar", parent_object=container_object)
        actual_color = color.Color.from_string(utils.get_element_css_propery(self, container_title_bar_obj, "background-color")).rgb
        expected_color = utils.color_picker(self, color_name)
        msg = "Step {0} : Verify [{1}] color is applied for [{2}] container".format(step_num, color_name, container_title)
        utils.asequal(self, expected_color, actual_color, msg)
        
    def verify_filter_grid_style_color(self, color_name, step_num, grid_container_title=None, model_window=False):
        """
        Descriptions : This method will verify the container style color
        :arg - grid_container_title = 'Panel1'. If you want to get filter grid object from inside the grid container then pass grid container title. 
        :arg - model_window = True. If you want to get filter grid object from filter model window then pass model_window=True 
        :Usage - verify_filter_grid_style_color("01.02", 'blue')
        """
        filter_grid = pd_miscelaneous.get_filter_grid_object(self, grid_container_title, model_window)
        actual_color = color.Color.from_string(utils.get_element_css_propery(self, filter_grid, "background-color")).rgb
        expected_color = utils.color_picker(self, color_name)
        msg = "Step {0} : Verify [{1}] color is applied for filter grid".format(step_num, color_name)
        utils.asequal(self, expected_color, actual_color, msg)
        
    def get_basic_container_object(self, container_name):
        """
        Descriptions : This method return the basic container object
        :Usage - get_basic_container_object("Accordion")'
        """
        if container_name in ['Panel', 'Tab', 'Carousel', 'Accordion', 'Grid']:
            container_css = str(ContentTab_Locators.BASIC_CONTAINER_ITEM_CSS).format(container_name.lower())
            container_object = utils.validate_and_get_webdriver_object(self, container_css, container_name)
            if container_object.is_displayed() :
                return container_object
            else :
                error_msg = "[{0}] basic container not visible".format(container_name)
                raise selenium_exceptions.ElementNotVisibleException(error_msg)
        else :
            error_msg = "Given [{0}] container currently not supported in designer page".format(container_name)
            raise KeyError(error_msg)
            
    def expand_and_collapse_content_and_repository_widgets_tab(self, content=None, repository_widgets=None):
        '''
        Descriptions : This method used to expand and collapse content and repository tabs.
        example : expand_and_collapse_content_and_repository_widgets_tab(repository_widgets='expand')
        '''
        down_css ='.ibx-glyph-chevron-down'
        right_css = '.ibx-glyph-chevron-right'
        if content:
            if content in ['expand', 'collapse']: 
                content_expected_css = '.pd-resource-tree {0}'.format(right_css) if content == 'expand' else '.pd-resource-tree {0}'.format(down_css)
                coreutils.left_click(self, utils.validate_and_get_webdriver_object(self, content_expected_css, 'Content {0}'.format(content)))
            else:
                raise ValueError("Please pass content value from 'expand', 'collapse'")
        if repository_widgets:
            if repository_widgets in ['expand', 'collapse']: 
                repository_widgets_expected_css = '.pd-repository-widgets {0}'.format(right_css) if repository_widgets == 'expand' else '.pd-repository-widgets {0}'.format(down_css)
                coreutils.left_click(self, utils.validate_and_get_webdriver_object(self, repository_widgets_expected_css, 'Repository widgets {0}'.format(content)))
            else:
                raise ValueError("Please pass repository_widgets value from 'expand', 'collapse'")
    
    def verify_repository_widgets_items(self,expected_widgets_list,msg):
        """
        Descriptions : this method use to verify the itema in repository widgets:-
        @param: ['explorer','link_title']
        example usage:-verify_repository_widgets_items(['Explorer', 'Link tile'],"step 4")
        """
        repository_widgets_items=ContentTab_Locators.REPOSITORY_WIDGETS_CSS +" .pd-draggable-button"
        repository_widgets_obj=utils.validate_and_get_webdriver_objects(self, repository_widgets_items,"repository widgets items list")
        actual_widgets_list=[title.text.strip() for title in repository_widgets_obj if title.is_displayed()]
        utils.verify_list_values(self,expected_widgets_list,actual_widgets_list,msg)        
    
    
    def drag_repository_widgets_item_to_blank_canvas(self, repository_widgets_name_to_drag, blank_grid_index_to_drop, section_num=1):
        """
        Descriptions : This method will drag Repository Widgets item to blank canvas
        :arg- repository_widgets_name_to_drag : 'Explorer', 'Link tile'
        :arg- blank_grid_index_to_drop = Position of bank grid to drop item ( blank_grid_index start from 1)
        example usage : drag_repository_widgets_item_to_blank_canvas('Explorer', 1)
        """
        if repository_widgets_name_to_drag not in ['Explorer', 'Link tile']:
            raise KeyError("Please pass container_name_to_drag from 'Explorer', 'Link tile'")
        resource_panel_element = utils.validate_and_get_webdriver_object(self, ".pd-left-pane", 'Resource Panel')
        margin_value = utils.get_element_css_propery(self, resource_panel_element, 'margin-left')
        opacity_value = utils.get_element_css_propery(self, resource_panel_element, 'opacity')
        if (int(margin_value.replace('px','')) > -100) and (int(opacity_value) is 1):
            repository_widgets_css = ContentTab_Locators.REPOSITORY_WIDGETS_ITEM_CSS
            item_container_css = repository_widgets_css.format(repository_widgets_name_to_drag.lower().replace(' ', '-'))
            item_container_element = utils.validate_and_get_webdriver_object(self, item_container_css, repository_widgets_name_to_drag, parent_object=resource_panel_element)
            blank_grid_css="div[class='pd-page-section-grid-box']"
            section_obj = PageDesignerDesign._get_page_section_object(self, section_num)
            blank_grid_obj=section_obj.find_elements_by_css_selector(blank_grid_css)
            source_cord=coreutils.get_web_element_coordinate(self, item_container_element)
            target_cord=coreutils.get_web_element_coordinate(self, blank_grid_obj[blank_grid_index_to_drop-1])
            coreutils.drag_and_drop(self, source_cord['x'], source_cord['y'], target_cord['x'], target_cord['y'])
        else:
            raise LookupError('Resource Panel not visible and opened.')
        
    def drag_content_item_to_blank_canvas(self, content_item_to_drog, blank_grid_index_to_drop, content_folder_path=None):
        """
        Descriptions : This method used to drag content item to bank grid canvas
        :arg- content_item_drog = Which content item drag to canvas
        :arg- blank_grid_index_to_drop = Position of bank grid to drop item ( blank_grid_index start from 1)
        :arg- content_folder_path = Content folder path to select item 
        example usage : drag_content_item_to_blank_canvas('01 - Simple Input Required', 2)
        """
        content_folder_path=utils.parseinitfile(self, 'reference_folder').strip() if content_folder_path==None else content_folder_path
        content_folder_path = None if content_folder_path == "Key not found" or content_folder_path=="" else content_folder_path
        blank_grid_css=PD_LOCATORS.PAGE_SECTION_PARENT_CSS + " div[class='pd-page-section-grid-box']"
        blank_grid_obj=self.driver.find_elements_by_css_selector(blank_grid_css)
        pd_miscelaneous.drag_and_drop_from_content_to_container_obj(self, content_folder_path, content_item_to_drog, blank_grid_obj[blank_grid_index_to_drop-1])
    
    def drag_content_item_to_container(self, content_item_to_drog, container_title_to_drop, container_position=1, content_folder_path=None):
        """
        Descriptions : This method used to drag content item to container
        :arg- content_item_drog = Which content item drag to container
        :arg- container_title_to_drop = Which container to drop content item
        :arg- container_position = Position of container. Some times two or more containers have same title that time we can pass container_position. container_position start form 1
        example usage : drag_content_item_to_container('01 - Simple Input Required', 'Panel 1')
        """
        content_folder_path=utils.parseinitfile(self, 'reference_folder') if content_folder_path==None else content_folder_path
        content_folder_path = None if content_folder_path == "Key not found" or content_folder_path=="" else content_folder_path
        container_obj=pd_miscelaneous.get_pd_container_object(self, container_title_to_drop, container_position)
        pd_miscelaneous.drag_and_drop_from_content_to_container_obj(self, content_folder_path, content_item_to_drog, container_obj)
    
    def drag_content_item_to_container_and_verify_drop_color(self, content_item, container_title, step_num, container_position=1):
        """
        Description : Drag content item and drop to canvas container and verify drop background color
        :Usage - drag_content_item_to_container_and_verify_drop_color("report", "Panel1", "02.02")
        """
        content_obj = pd_miscelaneous.find_pd_content_item_and_scroll_into_view(self, content_item)
        container_obj = PageDesignerDesign.get_container_object(self, container_title, container_position)
        source_location = coreutils.get_web_element_coordinate(self, content_obj)
        target_location = coreutils.get_web_element_coordinate(self, container_obj)
        coreutils.left_click(self, content_obj)
        time.sleep(1)
        pyautogui.mouseDown(source_location['x'], source_location['y'], duration=1)
        pyautogui.moveTo(target_location['x'], target_location['y'], duration=1)
        time.sleep(1)
        drop_target_highlighted_obj = utils.validate_and_get_webdriver_object(self, ".pd-container-drop", "Drop background", container_obj)
        actual_color = color.Color.from_string(drop_target_highlighted_obj.value_of_css_property('background-color')).rgba if drop_target_highlighted_obj.is_displayed() else ""
        expected_color = "rgba(41, 182, 246, 1)"
        msg = "Step {0} : Verify '{1}' color shows while drop content in container".format(step_num, expected_color)
        utils.asequal(self, expected_color, actual_color, msg)
        pyautogui.mouseUp(target_location['x'], target_location['y'])
    
    def drag_content_item_to_section_cell_and_verify_drop_color(self, content_item, section_cell_num, step_num, section_num=1):
        """
        Description : Drag content item and drop to bank section grid-cell canvas and verify drop target highlighted background color
        :Usage - drag_content_item_to_section_cell_and_verify_drop_color("report", 1, "02.02", section_num=1)
        """
        content_obj = pd_miscelaneous.find_pd_content_item_and_scroll_into_view(self, content_item)
        source_location = coreutils.get_web_element_coordinate(self, content_obj)
        section= PageDesignerDesign._get_page_section_object(self, int(section_num))
        section_cell = utils.validate_and_get_webdriver_objects(self, "div[class='pd-page-section-grid-box']", "Section cell", section)
        target_location=coreutils.get_web_element_coordinate(self, section_cell[int(section_cell_num)-1])
        coreutils.left_click(self, content_obj)
        time.sleep(1)
        pyautogui.mouseDown(source_location['x'], source_location['y'], duration=1)
        pyautogui.moveTo(target_location['x'], target_location['y'], duration=1)
        time.sleep(1)
        drop_target_highlighted_obj = utils.validate_and_get_webdriver_object(self, ".grid-stack-placeholder .placeholder-content", "Section Cell Drop Background")
        actual_color = color.Color.from_string(drop_target_highlighted_obj.value_of_css_property('background-color')).rgba if drop_target_highlighted_obj.is_displayed() else ""
        expected_color = "rgba(87, 168, 250, 1)"
        msg = "Step {0} : Verify '{1}' color shows while drop content in container".format(step_num, expected_color)
        utils.asequal(self, expected_color, actual_color, msg)
        pyautogui.mouseUp(target_location['x'], target_location['y'])
    
    def get_container_object(self, container_title, container_title_index=1):
        """
        Description : This method will return given container title parent object. 
        If more than containers have same title then you can pass container_title_index to get exact object of container
        """
        containers_title_objs = utils.validate_and_get_webdriver_objects(self, ".tpg-selected [data-ibx-type='pdPageSection'] div[data-ibx-type='pdContainer'] .pd-container-title .ibx-label-text", "Containers title")
        containers_title = [container.text.strip() for container in containers_title_objs]
        container_title_index_list = [index for index, title in enumerate(containers_title) if title==container_title]
        if len(container_title_index_list) > 0 :
            containers_obj_list = utils.validate_and_get_webdriver_objects(self, ".tpg-selected [data-ibx-type='pdPageSection'] div[data-ibx-type='pdContainer']", 'Containers')
            container_obj = containers_obj_list[container_title_index_list[container_title_index - 1]]
            return container_obj
        else :
            error = "'{0}' container not visible in canvas".format(container_title)
            raise KeyError(error)
    
    def click_show_filters(self):
        """
        Descriptions : This method used to click on show filters option
        """
        show_filters_obj = utils.validate_and_get_webdriver_object(self, "div[title='Show filters'][class*='pd-header-button-filter']", 'show filters option')
        coreutils.left_click(self, show_filters_obj)
    
    def close_selections_filter_dialog(self):
        """
        Descriptions : This method used to click on close button in selections_filter_dialog
        """
        close_btn_obj = utils.validate_and_get_webdriver_object(self, "div[class^='ibx-dialog-main-box'] div[title='Close'].ibx-title-bar-close-button", 'close button in selections_filter_dialog')
        coreutils.left_click(self, close_btn_obj)
    
    def click_quick_filter(self):
        """
        Descriptions : This method used to click on quick filter option
        """
        quick_filter_obj=self.driver.find_element_by_css_selector(DesignLocators.ToolBar.QUICK_FILTER_BUTTON_CSS)
        coreutils.left_click(self, quick_filter_obj)
    
    def click_preview(self):
        """
        Descriptions : This method used to click on preview button 
        """
        preview_obj=self.driver.find_element_by_css_selector(DesignLocators.ToolBar.PREVIEW_BUTTON_CSS)
        coreutils.left_click(self, preview_obj)
        time.sleep(3)
    
    def click_toolbar_save(self):
        """
        Descriptions : This method used to click on toolbar save button 
        """
        save_button_obj=self.driver.find_element_by_css_selector(DesignLocators.ToolBar.SAVE_BUTTON_CSS)
        coreutils.left_click(self, save_button_obj)
    
    def click_property(self):
        """
        Descriptions : This method used to click on property save button
        """
        save_button_obj=self.driver.find_element_by_css_selector(DesignLocators.ToolBar.PROPERTY_BUTTON_CSS)
        coreutils.left_click(self, save_button_obj)
    
    def click_configuration(self):
        """
        Descriptions : This method used to click on configuration button
        """
        configuration_button_obj = self.driver.find_element_by_css_selector(DesignLocators.ToolBar.PAGE_FILTER_BUTTON_CSS)
        coreutils.left_click(self, configuration_button_obj)
        
    def select_filter_configuration(self, button_name):
        """
        Descriptions: This method is used to select the filter configurations
        """
        utils.synchronize_with_number_of_element(self, '.pop-top', 1, 40)
        if button_name not in ['Filter bar', 'Create empty filter bar', 'Filter modal window', 'Create empty filter modal window']:
            raise IndexError("Please pass button_name correctly.")
        poptop_dialog.Poptop_Dialog.row_css="> .ibx-dialog-main-box .pd-ps-cell"
        current_button_name_element = poptop_dialog.New_Portal_Dialog.get_row_element_according_to_text_string(self, button_name)
        element_role = utils.get_element_attribute(self, current_button_name_element, 'role')
        poptop_dialog.Poptop_Dialog.row_css="> .ibx-dialog-main-box .ibx-flexbox-horizontal"
        coreutils.left_click(self, current_button_name_element)
        if element_role == 'radio':
            ok_btn_element = utils.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']",'ok')
            coreutils.left_click(self, ok_btn_element)
            
    def close_page_designer_from_application_menu(self):
        """
        Descriptions : This method used to close the page desginer from application 
        """
        pd_miscelaneous.select_page_designer_application_menu(self, 'Close')
        
    def save_page_from_toolbar(self, page_title_to_save, wait_time=3):
        """
        Descriptions : This method used to click on save button on tool bar and save current page with default name  
        """
        PageDesignerDesign.click_toolbar_save(self)
        pd_miscelaneous.page_designer_open_dialog_resources(self, title=page_title_to_save, ok_button=True)
        time.sleep(wait_time)
    
    def click_dialog_box_button(self, button_name):
        """
        Description : Click on button in dialog box.
        :Usage : click_dialog_box_button('Yes')
        """
        pd_miscelaneous.dialog_box(self, button_name_to_click=button_name)
        
    def close_and_save_page(self, page_name_to_save, wait_time=2):
        """
        Descriptions : This method used to click on close button from application menu and save page
        """
        pd_miscelaneous.select_page_designer_application_menu(self, 'Close')
        pd_miscelaneous.dialog_box(self, button_name_to_click='Yes')
        pd_miscelaneous.page_designer_open_dialog_resources(self,  title=page_name_to_save, ok_button=True)
        time.sleep(wait_time)
        pd_miscelaneous.switch_to_previous_window(self, driver_close=False)
    
    def switch_to_container_frame(self, container_title, container_position=1, timeout=30, wait_time=1, frame_index=1):
        """
        Descriptions : This method used to switch to iframe in specific pd container   
        """
        container_obj=pd_miscelaneous.get_pd_container_object(self, container_title, container_position)
        frame_elements_obj = container_obj.find_elements_by_css_selector("iframe")
        frame_element_obj=[frame_obj for frame_obj in frame_elements_obj if frame_obj.is_displayed()][frame_index-1]
        frame_actual_location = coreutils.get_web_element_coordinate(self, frame_element_obj, element_location='top_left')
        WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_element_obj))
        Global_variables.current_working_area_browser_x=frame_actual_location['x']
        Global_variables.current_working_area_browser_y=frame_actual_location['y']
        time.sleep(wait_time)
         
    def verify_number_of_filter_grid_cells(self, expected_total_grid_cells, msg):
        """
        Descriptions : This method used to verify total filter grid cells in page designer
        example usage : verify_number_of_filter_grid_cells(6, 'Step 01.1 : Verify 6 filter grid cells are display')
        """
        filter_grid_cells_css=PD_LOCATORS.FILTER_GRID_PARENT_CSS + " div[class*='pd-filter-cell']"
        filter_cells_obj=self.driver.find_elements_by_css_selector(filter_grid_cells_css)
        utils.verify_visible_elements(self, filter_cells_obj, expected_total_grid_cells, msg)
    
    def run_page_designer(self, page_name_to_run, folder_path=None):
        """
        Descriptions : This method used to run the saved or already existed page designer
        example usage : run_page_designer('Page 1')
        """
        folder_path=pd_miscelaneous.get_page_designer_folder_path(self) if folder_path==None else folder_path
        pd_miscelaneous.select_domain_folder_item_context_menu(self, folder_path, page_name_to_run, 'Run')
    
    def edit_page_designer(self, page_name_to_edit, folder_path=None):
        """
        Descriptions : This method used to edit the saved or already existed page designer
        example usage : edit_page_designer('Page 1')
        """
        folder_path=pd_miscelaneous.get_page_designer_folder_path(self) if folder_path==None else folder_path
        pd_miscelaneous.select_domain_folder_item_context_menu(self, folder_path, page_name_to_edit, 'Edit')
        coreutils.switch_to_new_window(self)
        utils.synchronize_with_visble_text(self, ".ibx-tab-position-bottom:not([style*='none'])", page_name_to_edit, 60)

    def change_page_heading(self, new_heading):
        """
        Description : Double click on page heading and clear old heading and enter the new page heading and enter the key
        """
        title_obj=self.driver.find_element(*PD_LOCATORS.PAHE_HEADER_TITLE).find_element_by_css_selector(".ibx-label-text")
        if Global_variables.browser_name == "chrome":  
            ActionChains(self.driver).double_click(title_obj).send_keys(new_heading).send_keys(Keys.ENTER).perform()
        else : 
            coreutils.double_click(self, title_obj,element_location = 'top_left')
            title_obj.send_keys(new_heading)
            title_obj.send_keys(Keys.ENTER)

    def run_page_designer_in_new_window(self, page_name_to_run, folder_path=None):
        """
        Descriptions : This method used to run the saved or already existed page designer in new window by right click on pd fex and select Run in new window
        example usage : run_page_designer_in_new_window('Page 1')
        """
        folder_path=pd_miscelaneous.get_page_designer_folder_path(self) if folder_path==None else folder_path
        pd_miscelaneous.select_domain_folder_item_context_menu(self, folder_path, page_name_to_run, 'Run in new window')
        coreutils.switch_to_new_window(self)
        coreutils.update_current_working_area_browser_specification(self)
        
    def delete_saved_page_designer(self, page_name_to_delete, folder_path=None):
        """
        Descriptions : This method used to delete the saved or already existed page designer
        example usage : run_page_designer('Page 1')
        """
        folder_path=pd_miscelaneous.get_page_designer_folder_path(self) if folder_path==None else folder_path
        pd_miscelaneous.select_domain_folder_item_context_menu(self, folder_path, page_name_to_delete, 'Delete')
        pd_miscelaneous.dialog_box(self, button_name_to_click='OK')
        
    def verify_filter_control_labels(self, expected_label_list, msg, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to filter control labels in filter panel
        :arg - grid_container_title = 'Panel1'. If you want to get filter grid object from inside the grid container then pass grid container title. 
        :arg - model_window = True. If you want to get filter grid object from filter model window then pass model_window=True
        :Usage - get_filter_grid_object()
        example usage : verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], 'Step 01.1 : Verify filter panel heading labels)
        """
        label_css = "div[data-ibx-type='pdFilterPanel'] div[class*='pd-amper-label'] div[class='ibx-label-text']"
        filer_grid = pd_miscelaneous.get_filter_grid_object(self, grid_container_title, model_window)
        filter_panel_objs = filer_grid.find_elements_by_css_selector(label_css)
        actual_label_list=[label.text.strip() for label in filter_panel_objs]
        utils.asequal(self, expected_label_list, actual_label_list, msg)
    
    def verify_number_of_page_sections(self, expected_total_sections, msg):
        """
        Descriptions : This method used to verify total number of page sections displaying in canvas
        example usage : verify_number_of_page_sections(5, 'Step 01.1 : Verify 5 page sections are displaying in page canvas') 
        """
        sections_objs=self.driver.find_elements_by_css_selector(PD_LOCATORS.PAGE_SECTION_PARENT_CSS)
        utils.verify_visible_elements(self, sections_objs, expected_total_sections, msg)
    
    def _get_page_section_object(self, section_num):
        """
        Descriptions : Return page section object.
        :Usage - _get_page_section_object(1)
        """
        sections_objects = utils.validate_and_get_webdriver_objects(self, PD_LOCATORS.PAGE_SECTION_PARENT_CSS, "Page section")
        if len(sections_objects) >= section_num :
            section_object = sections_objects[section_num-1]
            javascript.scrollIntoView(self, section_object)
            return section_object
        else :
            error_msg = "{0} sections only added in page. But {1} were given to get section".format(len(sections_objects), section_num)
            raise IndexError(error_msg)

    def select_page_section(self, section_num, location='top_left', xoffset=0, yoffset=0):
        """
        Descriptions : Click on page section at top left to select
        example usage : select_page_section(1) 
        """
        section_object = PageDesignerDesign._get_page_section_object(self, section_num)
        coreutils.python_left_click(self, section_object, element_location=location, xoffset=xoffset, yoffset=yoffset)
    
    def select_page_section_context_menu(self, section_num, context_menu):
        """
        Descriptions : Right click on page section at top left and click context menu
        example usage : select_page_section_context_menu(1, "Style") 
        """
        section_object = PageDesignerDesign._get_page_section_object(self, section_num)
        coreutils.right_click(self, section_object, element_location="top_left", xoffset=2, yoffset=2)
        pd_miscelaneous.select_page_designer_context_menu(self, context_menu)
        
    def verify_page_section_style_color(self, section_num, color_name, step_num):
        """
        Descriptions : This method used to verify page section style color
        example usage : verify_page_section_style_color(1, 'blue', '04.01') 
        """
        section_object = PageDesignerDesign._get_page_section_object(self, section_num)
        actual_color = color.Color.from_string(utils.get_element_css_propery(self, section_object, "background-color")).rgb
        expected_color = utils.color_picker(self, color_name)
        msg = "Step {0} : Verify [{1}] color is applied for page section {2}".format(step_num, color_name, section_num)
        utils.asequal(self, expected_color, actual_color, msg)
        
    def verify_number_of_panels(self, expected_total_panels, msg):
        """
        Descriptions : This method used to verify total number of panels displaying on canvas
        example usage : verify_number_of_panels(5, 'Step 01.1 : Verify 5 panels are displaying in page canvas') 
        """
        panel_objs=self.driver.find_elements_by_css_selector(PD_LOCATORS.PD_PANEL_CSS)
        utils.verify_visible_elements(self, panel_objs, expected_total_panels, msg)
    
    def verify_containers_title(self, expected_title_list, msg):
        """
        Descriptions : This method used to verify pd container titles
        example usage: verify_containers_title(["Panel 1", "Panel 2", "Panel 3", "Category Sales"], 'Step 01.1 : Verify container titles') 
        """
        containers_title_css=PD_LOCATORS.PD_CONTAINER_CSS + " div[data-ibx-name='_title']"
        title_obj=self.driver.find_elements_by_css_selector(containers_title_css)
        actaul_title_list=[title.text.strip() for title in title_obj if title.is_displayed()]
        utils.asequal(self, expected_title_list, actaul_title_list, msg)
    
    def verify_container_title_bar_visible_buttons(self, container_title, expected_buttons, msg, container_position=1):
        """
        Descriptions : This method used to verify visible container title bar button such as 'Maximize', 'Options' and 'Restore'
        example usage : verify_container_title_bar_button_options('Panel 6', ['Maximize', 'Options'], 'Step 01.1 : Verify ['Maximize', 'Options'] buttons display on container tool bar')
        """
        actual_options=pd_miscelaneous.get_pd_container_title_bar_visible_button_name(self, container_title, container_position)
        utils.asequal(self, expected_buttons, actual_options, msg)
    
    def verify_quick_filter_value(self, expected_value, step_no):
        """
        Descriptions : This method used to verify quick filter value.
        example usage : verify_quick_filter_value('3', 'Step 01.1')
        """
        pd_miscelaneous.verify_quick_filter_properties(self, 'text', expected_value, step_no)
    
    def verify_quick_filter_properties(self, properties_as_dic, msg_step):
        """
        Descriptions : This method used to quick filter properties such as filter count value, backgroud_color, font size and etc..
        :arg- properties_as_dic = Should be paass as dictionary
        example usage : verify_quick_filter_properties({'text':'1', 'background_color':'mandy', 'font_size':'12px', 'position':'absolute', 'text_align':'center'}, 'Step01.1')
        """
        for property_name in properties_as_dic :
            pd_miscelaneous.verify_quick_filter_properties(self, property_name, properties_as_dic[property_name], msg_step)
    
    def verify_page_heading_title(self, expected_title_list, msg):
        """
        Descriptions : This method used to verify page header title. expected title should be pass as list
        example usage : verify_page_heading_title(['Page Heading'], 'Step 01.1 : Verify page title')
        """
        title_obj=self.driver.find_elements(*PD_LOCATORS.PAHE_HEADER_TITLE)
        actual_title_list=[title.text.strip() for title in title_obj]
        utils.asequal(self, expected_title_list, actual_title_list, msg)
    
    def verify_page_header_visible_buttons(self, expected_visible_buttons, msg):
        """
        Descriptions : This method used to verify page header visible buttons such as 'Refresh', 'Filter'
        example usage : verify_page_header_visible_buttons('['Refresh', 'Filter'], 'Step 01.1 : Verify Refresh and Filter button are display on page header')
        """
        actual_visible_buttons=pd_miscelaneous.get_page_heading_visible_button_name(self)
        utils.asequal(self, expected_visible_buttons, actual_visible_buttons, msg)
        
    def verify_page_tab_groups(self, expected_groups, msg):
        """
        Descriptions : This method used to verify page page tab group name. Page tab group appear on bottom of the page
        example usage : verify_page_tab_groups(['Page 1'], 'Step 01.1 : Verify page tab groups')
        """
        tab_groups_css=".wb-page-tab-button"
        tab_group_obj=self.driver.find_element(*PD_LOCATORS.PAGE_TAB_GROUP)
        actual_groups=[group.text.strip() for group in tab_group_obj.find_elements_by_css_selector(tab_groups_css)]
        utils.asequal(self, expected_groups, actual_groups, msg)
    
    def verify_filter_control_panel_is_selected(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether specific filter control panel is selected
        verify_filter_control_panel_is_selected('Business Region:', 'Step 01.1 : Verify Business Region control is selected')
        """
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position, grid_container_title, model_window)
        pd_miscelaneous.verify_page_designer_component_is_selected(self, filter_control_obj, border_width='1px', border_rgb_value='rgb(212, 73, 73)', border_style='dashed', position='absolute', msg=msg)
    
    def verify_filter_control_panel_is_not_selected(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether specific filter control panel is not selected
        verify_filter_control_panel_is_not_selected('Business Region:', 'Step 01.1 : Verify Business Region filter control is not selected')
        """
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position, grid_container_title, model_window)
        border_direction=['north', 'south', 'west', 'east']
        selection_xpath="./div[@class='pd-selection {0} hide']"
        for direction in border_direction :
            border_visibility=filter_control_obj.find_element_by_xpath(selection_xpath.format(direction)).is_displayed()
            if border_visibility==False :
                visibility_status=True
            else :
                visibility_status=False
                break
        utils.asequal(self, True, visibility_status, msg)
        
    def __verify_filter_control_is_not_optional(self, filter_control_name, inpubox_parent_css, msg, border_width, border_rgb_value, border_style, position, filter_control_position=1,grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If not optional means drop down control bounded with red solid border around it.
        example usage : __verify_filter_control_is_not_optional('Business Region:', ,'Step 01.1 : Verify Business Region control input box is selected')
        """
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        inpubox_obj=filter_control_obj.find_element_by_css_selector(inpubox_parent_css)
        pd_miscelaneous.verify_page_designer_component_is_selected(self, inpubox_obj, border_width, border_rgb_value, border_style, position, msg, selection_class='pd-amper-invalid')
    
    def __verify_filter_control_is_optional(self, filter_control_name, inputbox_parent_css, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If optional means drop down control not bounded with red solid border around it.
        example usage : __verify_filter_control_is_optional('Business Region:', 'Step 01.1 : Verify Business Region control input box is not selected')
        """
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        border_css=inputbox_parent_css + ">div[class='pd-amper-invalid {0}']"
        border_direction=['north', 'south', 'west', 'east']
        for direction in border_direction :
            border_direction_css=border_css.format(direction)
            border_visibility=filter_control_obj.find_element_by_css_selector(border_direction_css).is_displayed()
            if border_visibility==False :
                visibility_status=True
            else :
                visibility_status=False
                break
        utils.asequal(self, True, visibility_status, msg)
        
    def __verify_filter_inpubox_control_value(self, filter_control_name, inputbox_css, expected_value_list, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify filter control input box text values and placeholder value.
        """
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position, grid_container_title, model_window)
        inputbox_objs=filter_control_obj.find_elements_by_css_selector(inputbox_css)
        actual_value_list=[]
        for inputbox in inputbox_objs :
            if inputbox.is_displayed()==True :
                inputbox_value=inputbox.get_attribute('value').strip()
                inputbox_value=inputbox.get_attribute('placeholder') if inputbox_value=='' else inputbox_value
                actual_value_list.append(inputbox_value)
        utils.asequal(self, expected_value_list, actual_value_list, msg)
    
    def verify_filter_inputbox_is_not_optional(self, filter_control_name, msg, border_width, border_rgb_value, border_style, position, filter_control_position=1,grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If not optional means drop down control bounded with red solid border around it.
        example usage : verify_filter_inputbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region control input box is selected')
        """
        inpubox_parent_css="div[data-ibx-type='ibxTextField']"
        PageDesignerDesign.__verify_filter_control_is_not_optional(self, filter_control_name, inpubox_parent_css, msg, border_width, border_rgb_value, border_style, position, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
        
    def verify_filter_inputbox_is_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If optional means drop down control not bounded with red solid border around it.
        example usage : verify_filter_inputbox_is_optional('Business Region:', 'Step 01.1 : Verify Business Region control input box is not selected')
        """
        inputbox_parent_css="div[data-ibx-type='ibxTextField']"
        PageDesignerDesign.__verify_filter_control_is_optional(self, filter_control_name, inputbox_parent_css, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_inputbox_value(self, filter_control_name, expected_value_list, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter input box values
        example usage : verify_filter_inputbox_value('Business Region:', ['EMP'], 'Step 01.1 : Verify Business Region condition inbutbox is value is none')
        """
        inputbox_css="div[data-ibx-type='ibxTextField']>input"
        PageDesignerDesign.__verify_filter_inpubox_control_value(self, filter_control_name, inputbox_css, expected_value_list, msg, filter_control_position)
        
    def verify_filter_dropdown_is_not_optional(self, filter_control_name, msg, border_width, border_rgb_value, border_style, position, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter dropbdown control is optional. If not optional means drop down control bounded with red solid border around it.
        example usage : verify_filter_dropdown_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter drop down control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_not_optional(self, filter_control_name, PD_LOCATORS.FILTER_DROPDOWN_PARENT_CSS, msg, border_width, border_rgb_value, border_style, position, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_dropdown_is_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter drop down control is optional. If optional means drop down control not bounded with red solid border around it.
        example usage : verify_filter_dropdown_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter drop down control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_optional(self, filter_control_name, PD_LOCATORS.FILTER_DROPDOWN_PARENT_CSS, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_buttonset_is_not_optional(self, filter_control_name, msg, border_width, border_rgb_value, border_style, position, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If not optional means button set control bounded with red solid border around it.
        example usage : verify_filter_buttonset_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter button set control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_not_optional(self, filter_control_name, '.pd-amper-control-wrapper', msg, border_width, border_rgb_value, border_style, position, filter_control_position)
    
    def verify_filter_buttonset_is_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If optional means button set control not bounded with red solid border around it.
        example usage : verify_filter_buttonset_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter button set control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_optional(self, filter_control_name, '.pd-amper-control-wrapper', msg, filter_control_position)

    def verify_selected_value_of_filter_dropdown(self, filter_control_name, expected_value_list, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify filter drop down selected value or default value
        example usage : verify_selected_value_of_filter_dropdown('Business Region:', ['EMP'], 'Step 01.1 : Verify Business Region drop down selected EMP value')
        """
        dropdown_inputbox_css=PD_LOCATORS.FILTER_DROPDOWN_PARENT_CSS + ">input"
        PageDesignerDesign.__verify_filter_inpubox_control_value(self, filter_control_name, dropdown_inputbox_css, expected_value_list, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def get_property_tab_object(self, tab_name):
        """
        Descriptions : This method used to get property tab object
        example usage : get_property_tab_object('settings)
        """
        tab_name = tab_name.capitalize()
        current_tab_name = 'Format' if tab_name == 'Style' else tab_name #In 8207, Style tab has been changed as Format
        tab_object = utils.validate_and_get_webdriver_object(self, DesignLocators.ToolBar.PROPERTY_TAB_CSS.format(current_tab_name), '{0} tab'.format(current_tab_name))
        return tab_object
    
    def select_property_tab(self, tab_name):
        """
        Descriptions : This method will select specific property tab
        example usage : select_property_tab('settings)
        """
        tab_object = PageDesignerDesign.get_property_tab_object(self, tab_name)
        coreutils.left_click(self, tab_object)
    
    def verify_property_tabs(self, expected_tabs, msg):
        """
        Descriptions : This method used to verify property widow tabs
        example usage : verify_property_tabs(['Settings', 'Style'], 'Step 06.1 : Verify Property_tabs')
        """
        tabs_css="div[data-ibx-type='ibxTabPane'][class*='ibxtool-right-tab-pane'] div[class^='ibx-tab-button']"
        tabs_obj=self.driver.find_elements_by_css_selector(tabs_css)
        actual_tabs=[tab.get_attribute('title').strip() for tab in tabs_obj if tab.is_displayed()==True]
        utils.asequal(self, expected_tabs, actual_tabs, msg)
    
    def get_property_content_tabs_object(self, tab_name):
        """
        Descriptions : This method used to get property content tabs
        example usage : get_setting_tabs_object('settings')
        """
        current_tab_name = tab_name.lower()
        tabs_css=DesignLocators.ToolBar.PROPERTY_TAB_CONTENT_CSS.format(current_tab_name)
        tabs_obj=utils.validate_and_get_webdriver_objects(self, tabs_css, '{0} Tab'.format(current_tab_name))
        actual_tabs = (tab for tab in tabs_obj if tab.is_displayed())
        return actual_tabs
        
    def verify_setting_tabs(self, expected_tabs, msg):
        """
        Descriptions : This method used to verify setting tabs
        example usage : verify_setting_tabs(['General Settings', 'Control Settings', 'Data Settings', 'Parameters'], 'Step 01.1 : Step 06.2 : Verify ['General Settings', 'Control Settings', 'Data Settings', 'Parameters'] tabs are display in setting tab - PASSED.')
        """
        tabs_obj = PageDesignerDesign.get_property_content_tabs_object(self, 'settings')
        actual_tabs=[tab.text.strip() for tab in tabs_obj]
        utils.asequal(self, expected_tabs, actual_tabs, msg)
    
    def verify_setting_tab_properties(self,tab_name, expected_properties, msg, property_tab_name='settings'):
        """
        Descriptions : This method used to verify specific setting tab properties
        example usage1 : verify_setting_tab_properties('General Settings', ['Type=Input', 'Tooltip=', 'Global name='], 'Step 06.3 : Verify General Settings properties')
        example usage2 : verify_setting_tab_properties('Control Settings', ['Optional=off', 'Placeholder text='], 'Step 06.3 : Verify Control Settings properties')
        """
        prop_label=''
        value=''
        actual_properties=[]
        tab_obj=PageDesignerDesign.get_setting_tab_object(self, tab_name, property_tab_name=property_tab_name)
        tab_properties_obj=tab_obj.find_elements_by_css_selector("div[data-ibx-type='ibxGrid']>div[data-ibx-row][data-ibx-col]:not([style*='none'])")
        for col, prop_obj in enumerate(tab_properties_obj, 1) :
            if prop_obj.is_displayed()==True :
                if (col%2)==0 : #label or value
                    textbox_obj=prop_obj.find_elements_by_css_selector("input[type='text']")
                    if len(textbox_obj)>0 : #t extbox 
                        for textbox in textbox_obj :
                            text_value=textbox.get_attribute('value')
                            if text_value=='' :
                                text_value=textbox.get_attribute('placeholder')
                            value=text_value
                    else :
                        checkbox_calss_attribute=prop_obj.get_attribute('class').lower()
                        value='on' if 'checked' in checkbox_calss_attribute else 'off' 
                    if prop_label == 'ID' :
                        value = value.split('-')[0]
                    actual_properties.append(prop_label + '=' + value)
                else : # Checkbox
                    prop_label=prop_obj.text.strip()
        utils.asequal(self, expected_properties, actual_properties, msg)
    
    def select_property_tab_content_properties(self, property_tab_name, tab_name, property_type, property_name, property_value):
        """
        Descriptions : This method used to select specific property tab content properties
        example usage : select_property_tab_content_properties('Style', 'Page Style', 'text_box', 'Light')
        """
#         prop_label=''
#         value=''
#         actual_properties=[]
        tab_obj=PageDesignerDesign.get_setting_tab_object(self, tab_name, property_tab_name=property_tab_name)
        tab_properties_obj=tab_obj.find_elements_by_css_selector("div[data-ibx-type='ibxGrid']>div[class^='pd-ps'][data-ibx-row][data-ibx-col]")
        for col in range(0, len(tab_properties_obj), 2):
#         for col, prop_obj in enumerate(tab_properties_obj, 1) :
            if tab_properties_obj[col].is_displayed()==True and tab_properties_obj[col].text == property_name:
                textbox_obj=tab_properties_obj[col+1].find_elements_by_css_selector("input[type]")
                if len(textbox_obj)>0 : #t extbox 
                    if property_type == 'text_box':
                        utils.set_text_to_textbox_using_keybord(self, property_value, text_box_elem=textbox_obj[0])
                        break
                    elif property_type == 'drop_down':
                        coreutils.left_click(self, textbox_obj[0])
                        Wf_Mainpage.select_context_menu_item(self, property_value,5, pop_up_css="div[class*='pop-top']", row_css="[data-ibx-type='ibxSelectItemList'] [data-ibx-type='ibxSelectItem']")
                        coreutils.python_left_click(self, textbox_obj[0], element_location='middle_left', xoffset=-19)
                        break
                if property_type == 'radio_button' :
                    radio_button_obj = tab_properties_obj[col+1].find_element_by_css_selector(".ibx-switch-slider")
                    coreutils.python_left_click(self, radio_button_obj)
    
    def verify_property_tab_content_properties(self, property_tab_name, tab_name, property_type, property_value_list , msg, comparision_type='asequal'):
        """
        Descriptions : This method used to verify specific property tab content properties
        example usage : select_property_tab_content_properties('Style', 'Page Style', 'text_box', ['Light'], 'Step 9: verify')
        """
#         prop_label=''
#         value=''
#         actual_properties=[]
        tab_obj=PageDesignerDesign.get_setting_tab_object(self, tab_name, property_tab_name=property_tab_name)
        tab_properties_obj=tab_obj.find_elements_by_css_selector("div[data-ibx-type='ibxGrid']>div[class^='pd-ps'][data-ibx-row][data-ibx-col]")
        for col, prop_obj in enumerate(tab_properties_obj, 1) :
            if prop_obj.is_displayed()==True :
                if (col%2)==0 : #label or value
                    textbox_obj=prop_obj.find_elements_by_css_selector("input[type='text']")
                    if len(textbox_obj)>0 : #t extbox 
                        if property_type is 'text_box':
                            actual_list_value = utils.get_element_attribute(self, textbox_obj, 'value')
                            utils.verify_list_values(self, property_value_list, actual_list_value, msg, assert_type=comparision_type)
                        elif property_type is 'drop_down':
                            coreutils.left_click(self, textbox_obj)
                            Wf_Mainpage.verify_context_menu_item(self, property_value_list, msg=msg, comparision_type=comparision_type)
                            coreutils.python_left_click(self, textbox_obj, element_location='middle_left', xoffset=-19)
                    else :
                        pass
#                         checkbox_calss_attribute=prop_obj.get_attribute('class').lower()
#                         value='on' if 'checked' in checkbox_calss_attribute else 'off' 
#                     if tab_name == 'General Settings' and prop_label == 'ID' :
#                         value = value.split('-')[0]
#                     actual_properties.append(prop_label + '=' + value)
                else : # Checkbox
                    pass
#                     prop_label=prop_obj.text.strip()
    
    def verify_setting_parameter_tab_properties(self, expected_values, msg):
        """
        Descriptions : This method used to verify parameter tab properties in setting tab
        """
        parameter_obj=PageDesignerDesign.get_setting_tab_object(self, 'Parameters')
        input_obj=parameter_obj.find_elements_by_css_selector('input')
        actual_values=[inputbox.get_attribute('value').strip() for inputbox in input_obj if inputbox.is_displayed()==True]
        utils.asequal(self, expected_values, actual_values, msg)
        
    def get_setting_tab_object(self, tab_name, property_tab_name='settings'):
        """
        Descriptions : This method used to find and get setting tab object based on tab name
        example usage : get_setting_tab_object('Data Settings')
        """
        tab_parent_css="div[class^='pd-{0}-tab-page'] div[data-ibx-type='ibxAccordionPage']".format(property_tab_name.lower())
        tabs_label_css=tab_parent_css + " div[class*='ibx-accordion-button-text']"
        tab_objs=self.driver.find_elements_by_css_selector(tab_parent_css)
        tab_label_objs=self.driver.find_elements_by_css_selector(tabs_label_css)
        tab_label_list=javascript.get_elements_text(self, tab_label_objs)
        if tab_name in tab_label_list :
            tab_obj=tab_objs[tab_label_list.index(tab_name)]
            return tab_obj
        else :
            error_msg="['{0}'] tab not display in settings window".format(tab_name)
            raise KeyError(error_msg)
    
    def verify_default_output_for_input_required_container(self, container_title, msg, expected_output, container_position=1):
        """
        Descriptions : This method used to verify default output for input required fex contains container text
        example usage : verify_default_output_for_input_required_container('01 - Simple Input Required', 'Step 01.1 : Verify report added to the page successfully.')
        """
        PageDesignerDesign.switch_to_container_frame(self, container_title, container_position)
        actual_output=self.driver.find_element_by_css_selector('body').text.strip()
        utils.asequal(self, expected_output, actual_output, msg)
        self.driver.switch_to.default_content()
        coreutils.update_current_working_area_browser_specification(self)
        
    def select_filter_control_context_menu(self, filter_control_name, context_menu, control_position=1):
        """
        Descriptions : This method used to select filter control context menu
        example usage : select_filter_control_context_menu('Business Region:', 'Settings')
        """
        filter_control_obj=pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, control_position)
        coreutils.right_click(self, filter_control_obj)
        pd_miscelaneous.select_page_designer_context_menu(self, context_menu)
    
    def select_container_context_menu(self, container_title, context_menu, container_position=1):
        """
        Descriptions : This method used to right click on container and select context menu
        example usage : select_container_context_menu('Panel1', 'Settings')
        """
        container_obj=PageDesignerDesign.get_container_object(self, container_title, container_position)
        coreutils.right_click(self, container_obj)
        pd_miscelaneous.select_page_designer_context_menu(self, context_menu)
    
    def verify_container_context_menu(self, container_title, expected_context_menu_list, step_no, container_position=1, comparision_type='asequal'):
        """
        Descriptions : This method used to right click on container and verify context menu
        example usage : select_container_context_menu('Panel1', ['Settings'], '09.00')
        """
        container_obj=PageDesignerDesign.get_container_object(self, container_title, container_position)
        coreutils.right_click(self, container_obj)
        Wf_Mainpage.verify_context_menu_item(self, expected_context_menu_list, msg='Step {0}'.format(step_no), comparision_type=comparision_type)
        
    def select_container(self, container_title, container_position=1, xoffset=2, yoffset=2):
        """
        Descriptions : This method used to left click on container at top left to select
        example usage : select_container_context_menu('Panel1')
        """
        container_obj=PageDesignerDesign.get_container_object(self, container_title, container_position)
        coreutils.left_click(self, container_obj, element_location="top_left", xoffset=xoffset, yoffset=yoffset, action_chain_click=True)
       
    def verify_blank_container_output(self, container_title, msg, container_position=1):
        """
        Descriptions : This method used to verify blank containers output which means blank container should be blank
        example usage : verify_blank_container_output('Panel 2', 'Step 01.1 : Verify Panel 1 is blank')
        """
        timeout=30
        container_obj=pd_miscelaneous.get_pd_container_object(self, container_title, container_position)
        container_output=container_obj.find_element_by_css_selector("div[data-ibx-type='pdContent']").text.strip()
        frame_element_obj = container_obj.find_element_by_css_selector("iframe")
        WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_element_obj))  
        iframe_output=self.driver.find_element_by_css_selector('body').text.strip()
        utils.asequal(self, container_output, iframe_output, msg)
        self.driver.switch_to.default_content()
        coreutils.update_current_working_area_browser_specification(self)
    
    def verify_report_has_vertical_scrollbar(self, report_scroll_css, msg):
        """
        Descriptions : This method used to verify whether specific container html report has vertical scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because html report placed inside the container iframe
        """
        report_obj = self.driver.find_element_by_css_selector(report_scroll_css)
        utils.verify_element_has_vertical_scrollbar(self, report_obj, msg)
        
    def verify_report_has_horizontal_scrollbar(self, report_scroll_css, msg):
        """
        Descriptions : This method used to verify whether specific container html report has horizontal scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        report_obj = self.driver.find_element_by_css_selector(report_scroll_css)
        utils.verify_element_has_horizontal_scrollbar(self, report_obj, msg)
        
    def verify_report_does_not_have_vertical_scrollbar(self, report_scroll_css, msg):
        """
        Descriptions : This method used to verify whether specific container report does not have vertical scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because html report placed inside the container iframe
        """
        report_obj = self.driver.find_element_by_css_selector(report_scroll_css)
        utils.verify_element_does_not_have_vertical_scrollbar(self, report_obj, msg)
       
    def verify_report_does_not_have_horizontal_scrollbar(self, report_scroll_css, msg):
        """
        Descriptions : This method used to verify whether specific container report does not have horizontal scroll bar
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        report_obj = self.driver.find_element_by_css_selector(report_scroll_css)
        utils.verify_element_does_not_have_horizontal_scrollbar(self, report_obj, msg)
    
    def verify_report_vertical_scrollbar_reached_bottom(self, report_scroll_css, msg):
        """
        Descriptions : This method used to verify whether specific container report vertical scroll bar reached bottom
        Note : Should be call switch_to_container_frame() method before call this method because report placed inside the container iframe
        """
        report_obj = self.driver.find_element_by_css_selector(report_scroll_css)
        utils.verify_vertical_scrollbar_reached_bottom(self, report_obj, msg)
    
    def verify_filter_buttonset_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter buttonset options
        example usage : verify_filter_buttonset_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter button set control')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        buttonset_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_BUTTONSET_OPTIONS_CSS)
        actaul_options = [option.text.strip() for option in buttonset_options_list]
        utils.asequal(self, expected_options, actaul_options, msg)
    
    def verify_selected_options_in_filter_buttonset(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter button set control.It will verify selected options based on backgroud color of option
        example usage : verify_filter_buttonset_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter button set control')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        buttonset_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_BUTTONSET_OPTIONS_CSS + "[class*='checked']")
        actaul_selected_options = [option.text.strip() for option in buttonset_options_list if color.Color.from_string(option.value_of_css_property('background-color')).rgba == 'rgba(238, 238, 238, 1)']
        utils.asequal(self, expected_selected_options, actaul_selected_options, msg)
    
    def convert_filter_control(self, filter_control_name, control_name_to_convert, filter_control_position=1):
        """
        Descriptions : This method used to convert filter control to some other filter controls. For example convert  drop down control to button set control. 
        example usage : convert_filter_control('Select North America', 'Button set')
        """
        PageDesignerDesign.select_filter_control_context_menu(self, filter_control_name, 'Convert', filter_control_position)
        utils.synchronize_with_number_of_element(self, PD_LOCATORS.FILTER_CONTROL_CONVERTOR_POP_CSS, 1, expire_time=25)
        controls_obj_list = self.driver.find_elements_by_css_selector(PD_LOCATORS.FILTER_CONTROL_CONVERTOR_OPTIONS_CSS)
        control_index = javascript.find_element_index_by_text(self, controls_obj_list, control_name_to_convert)
        if control_index != None :
            control_obj = controls_obj_list[control_index]
            coreutils.left_click(self, control_obj)
        else :
            erroe_msg = "[{0}] control not display in filter control converter window".format(control_name_to_convert)
            raise KeyError(erroe_msg)
    
    def verify_filter_control_converter_window(self, filter_control_name, msg_step_no, expected_controls_list=None, verify_window_display_position=False, window_title='Convert Control To', filter_control_position=1):
        """
        Descriptions : This method used to verify filter control converter window.
        :arg : msg_step_no ='01.1'
        :arg : expected_controls_list=['Button set', 'Checkbox']
        example usage : verify_filter_control_converter_window('Select North America', '01.1', expected_controls_list=['Button set', 'Checkbox'], verify_window_display_position=True]
        """
        PageDesignerDesign.select_filter_control_context_menu(self, filter_control_name, 'Convert', filter_control_position)
        utils.synchronize_with_number_of_element(self, PD_LOCATORS.FILTER_CONTROL_CONVERTOR_POP_CSS, 1, expire_time=25)
        if expected_controls_list !=None :
            controls_obj_list = self.driver.find_elements_by_css_selector(PD_LOCATORS.FILTER_CONTROL_CONVERTOR_OPTIONS_CSS)
            actaul_controls = [control.text.strip() for control in controls_obj_list]
            utils.asequal(self, expected_controls_list, actaul_controls, 'Step ' + str(msg_step_no) + ' : Verify [{0}] controls are display in control converter window'.format(expected_controls_list))
        if window_title != None :
            title_css = PD_LOCATORS.FILTER_CONTROL_CONVERTOR_POP_CSS + " div[class^='ibx-dialog-title-box']"
            actaul_title = self.driver.find_element_by_css_selector(title_css).text.strip()
            utils.asequal(self, window_title, actaul_title, 'Step ' + str(msg_step_no) + ' : Verify control converter window display')
        if verify_window_display_position == True :
            pass
        close_btn_obj = self.driver.find_element_by_css_selector(PD_LOCATORS.FILTER_CONTROL_CONVERTOR_POP_CLOSE_BTN_CSS)
        coreutils.left_click(self, close_btn_obj)
    
    def verify_filter_radio_group_is_not_optional(self, filter_control_name, msg, border_width, border_rgb_value, border_style, position, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter radio button group control is not optional. If not optional means button set control bounded with red solid border around it.
        example usage : verify_filter_radio_group_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_not_optional(self, filter_control_name, PD_LOCATORS.FILTER_RADIOGROUP_PARENT_CSS, msg, border_width, border_rgb_value, border_style, position, filter_control_position)
    
    def verify_filter_radio_group_is_optional(self, filter_control_name, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify whether filter button set control is optional. If optional means button set control not bounded with red solid border around it.
        example usage : verify_filter_radio_group_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_optional(self, filter_control_name, PD_LOCATORS.FILTER_RADIOGROUP_PARENT_CSS, msg, filter_control_position)
    
    def verify_filter_radio_group_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter radio group options
        example usage : verify_filter_radio_group_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter radio group control')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        radio_group_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_RADIOGROUP_OPTIONS_CSS)
        actaul_options = [option.text.strip() for option in radio_group_options_list]
        utils.asequal(self, expected_options, actaul_options, msg)
    
    def verify_selected_options_in_filter_radio_group(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter radio group control.
        example usage : verify_selected_options_in_filter_radio_group('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter radio group control')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        radio_group_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_RADIOGROUP_OPTIONS_CSS)
        actaul_selected_options = [option.text.strip() for option in radio_group_options_list if len(option.find_elements_by_css_selector(PD_LOCATORS.SELECTED_FILTER_RADIOGROUP_BUTTON_ICON_CSS)) == 1]
        utils.asequal(self, expected_selected_options, actaul_selected_options, msg)
    
    def verify_filter_date_picker_is_not_optional(self, filter_control_name, msg, border_width, border_rgb_value, border_style, position, filter_control_position=1,grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter date picker control is not optional. If not optional means date picker control bounded with red solid border around it.
        example usage : verify_filter_date_picker_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter date picker control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_not_optional(self, filter_control_name, PD_LOCATORS.FILTER_DATE_PICKER_PARENT_CSS, msg, border_width, border_rgb_value, border_style, position, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_filter_date_picker_is_optional(self, filter_control_name, msg, filter_control_position=1, grid_container_title=None, model_window=False):
        """
        Descriptions : This method used to verify whether filter date picker is optional. If optional means date picker control not bounded with red solid border around it.
        example usage : verify_filter_date_picker_is_optional('Business Region:', 'Step 01.1 : Verify Business Region filter date picker control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_optional(self, filter_control_name, PD_LOCATORS.FILTER_DATE_PICKER_PARENT_CSS, msg, filter_control_position, grid_container_title=grid_container_title, model_window=model_window)
    
    def verify_selected_date_in_filter_date_picker(self, filter_control_name, expected_selected_date, msg, filter_control_position=1,):
        """
        Descriptions : This method used to verify selected date value in filter data picker control
        example usage : verify_selected_date_in_filter_date_picker('Select 2016/03/17', ['Jun 19, 2018'], 'Step 01.1 : Verify Jun 19, 2018 date selected in data picker control')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        date_picker_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_DATE_PICKER_PARENT_CSS)
        actual_selected_date = [date.text.strip() for date in date_picker_list]
        utils.asequal(self, expected_selected_date, actual_selected_date, msg)
    
    def verify_filter_checkbox_is_not_optional(self, filter_control_name, msg, border_width, border_rgb_value, border_style, position, filter_control_position=1):
        """
        Descriptions : This method used to verify whether filter checkbox group control is not optional. If not optional means checkbox control bounded with red solid border around it.
        example usage : verify_filter_checkbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_not_optional(self, filter_control_name, PD_LOCATORS.FILTER_CHECKBOX_PARENT_CSS, msg, border_width, border_rgb_value, border_style, position, filter_control_position)
    
    def verify_filter_checkbox_is_optional(self, filter_control_name, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify whether filter checkbox control is optional. If optional means checkbox control not bounded with red solid border around it.
        example usage : verify_filter_checkbox_is_not_optional('Business Region:', 'Step 01.1 : Verify Business Region filter radio group control bounded to the page with red solid border around it.')
        """
        PageDesignerDesign.__verify_filter_control_is_optional(self, filter_control_name, PD_LOCATORS.FILTER_CHECKBOX_PARENT_CSS, msg, filter_control_position)
    
    def verify_filter_checkbox_options(self, filter_control_name, expected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter checkbox options
        example usage : verify_filter_checkbox_options('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are display in filter radio group control')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        checkbox_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_CHECKBOX_OPTIONS_CSS)
        actaul_options = [option.text.strip() for option in checkbox_options_list]
        utils.asequal(self, expected_options, actaul_options, msg)
    
    def verify_selected_options_in_filter_checkbox(self, filter_control_name, expected_selected_options, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify selected option in filter checkbox control.
        example usage : verify_selected_options_in_filter_checkbox('Select North America', ['EMEA', 'South America'], 'Step 01.1 : Verify ['EMEA', 'South America'] options are selected in filter radio group control')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        checkbox_options_list = filter_control_obj.find_elements_by_css_selector(PD_LOCATORS.FILTER_CHECKBOX_OPTIONS_CSS)
        actaul_selected_options = [option.text.strip() for option in checkbox_options_list if len(option.find_elements_by_css_selector(PD_LOCATORS.SELECTED_FILTER_CHECKBOX_OPTION_ICON_CSS)) == 1]
        utils.asequal(self, expected_selected_options, actaul_selected_options, msg)
    
    def verify_filter_slider_values(self, filter_control_name, expected_values, msg, filter_control_position=1):
        """
        Descriptions : This method used to verify filter slider control range values. Range value means slider minimum value, selected value and maximum value. 
        example usage : verify_filter_slider_values('Move Slider to 5011', ['MIN=5000', 'SELECTED=5008', 'MAX=5020'], 'Step 01.1 : Verify slider range values')
        """
        actula_values = []
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        min_value = filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_SLIDER_MIN_VAL_CSS).text.strip()
        max_value = filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_SLIDER_MAX_VAL_CSS).text.strip()
        selected_value =  filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_SLIDER_SELECTED_VAL_CSS).text.strip()
        actula_values.append('MIN=' + str(min_value))
        actula_values.append('SELECTED=' + str(selected_value))
        actula_values.append('MAX=' + str(max_value))
        utils.asequal(self, expected_values, actula_values, msg)
    
    def verify_filter_slider_range_line_color(self, filter_control_name, msg , color_name='bar_blue1', filter_control_position=1):
        """
        Descriptions : This method used to verify slider range line color 
        example usage : verify_filter_slider_range_line_color('Move Slider to 5011', 'Step 01.1 : Verify slider range line color is blue')
        """
        filter_control_obj = pd_miscelaneous.get_pd_filter_control_object(self, filter_control_name, filter_control_position)
        expected_color = utils.color_picker(self, color_name)
        actual_color = color.Color.from_string(filter_control_obj.find_element_by_css_selector(PD_LOCATORS.FILTER_SLIDER_RANGE_LINE_CSS).value_of_css_property('background-color')).rgb
        utils.asequal(self, expected_color, actual_color, msg)
    
    def verify_style_options(self, tab_name, step_num):
        """
        Descriptions : This method used to style options
        example usage : verify_style_options("Grid Style", "04.01")
        """
        expected_options = [('Default', 'rgb(0, 0, 0)'), ('Style 2', 'rgb(51, 122, 183)'), ('Style 3', 'rgb(92, 184, 92)'), ('Style 4', 'rgb(91, 192, 222)'), ('Style 5', 'rgb(240, 173, 78)'), ('Style 6', 'rgb(217, 83, 79)'), ('Style 7', 'rgb(6, 30, 62)'), ('Style 8', 'rgb(163, 175, 183)')]
        style_options_css = "div[data-ibxp-btn-options*='{0}'] div.pd-control-value".format(tab_name)
        style_options_objects = utils.validate_and_get_webdriver_objects(self, style_options_css, tab_name + " Options")
        actual_options = []
        for style_option in style_options_objects :
            style_name = style_option.text.strip()
            style_color = color.Color.from_string(utils.get_element_css_propery(self, style_option, "background-color")).rgb
            actual_options.append((style_name, style_color))
        msg = "Step {0} : Verify {1} options".format(step_num, tab_name)
        utils.asequal(self, expected_options, actual_options, msg)
    
    def select_style(self, tab_name, style_name):
        """
        Descriptions : This method used to click on style
        example usage : select_style("Grid Style", "Style 3")
        """
        style_options_css = "div[data-ibxp-btn-options*='{0}'] div.pd-control-value".format(tab_name)
        style_options_objects = utils.validate_and_get_webdriver_objects(self, style_options_css, tab_name + " Options")
        for style_option in style_options_objects :
            if style_option.text.strip() == style_name :
                style_object = style_option
                break
        else :
            error_msg = "[{0}] style not exists in {1}".format(style_name, tab_name)
            raise LookupError(error_msg)
        coreutils.left_click(self, style_object)
    
    def select_filter_grid_cell(self, cell_num, grid_container_title=None, model_window=False, click_on_location='top_left', click_type='left'):
        """
        Descriptions : This method used to click on filter grid cell at top left corner
        example usage : select_filter_grid_cell(1)
        """
        filter_grid_obj=pd_miscelaneous.get_filter_grid_object(self, grid_container_title, model_window)
        grid_cell_objs = utils.validate_and_get_webdriver_objects(self, "div[class*='pd-filter-cell']", "Filter grid cell", parent_object=filter_grid_obj)
        cell_object = grid_cell_objs[cell_num - 1]
        if click_type == 'left':
            coreutils.python_left_click(self, cell_object, element_location=click_on_location, xoffset=2, yoffset=2)
        elif click_type == 'right':
            coreutils.python_right_click(self, cell_object, element_location=click_on_location)
        elif click_type == 'double':
            coreutils.python_doubble_click(self, cell_object, element_location=click_on_location)
    
    def select_filter_grid_panel(self, cell_num, click_on_location='top_left', click_type='left'):
        """
        Descriptions : This method used to click on filter grid cell at top left corner
        example usage : select_filter_grid_cell(1)
        """
        grid_cell_objs = utils.validate_and_get_webdriver_objects(self, "div[data-ibx-type*='pdFilterPanel']", "Filter grid cell")
        cell_object = grid_cell_objs[cell_num - 1]
        if click_type == 'left':
            coreutils.python_left_click(self, cell_object, element_location=click_on_location, xoffset=2, yoffset=2)
        elif click_type == 'right':
            coreutils.python_right_click(self, cell_object, element_location=click_on_location)
        elif click_type == 'double':
            coreutils.python_doubble_click(self, cell_object, element_location=click_on_location)    
    
    
    def verify_page_domain_tree_node(self, expected_domain_tree_list, msg, tree_node_css=None, assert_type='asin'):
        """
        Descriptions : This method used to verify_page_domain_tree_node
        example usage : verify_page_domain_tree_node(['Domains', 'P292_S19901', 'P398_S10799', 'Public', 'S9100', 'Retail Samples'], msg='Step 01.1 : Verify slider range line color is blue')
        """
        tree_node_css = tree_node_css if tree_node_css else "[data-ibx-type=pdTreeBrowserNode] .ibx-label-text"
        utils.synchronize_until_element_is_visible(self, tree_node_css, expire_time=60)
        tree_node_objs = utils.validate_and_get_webdriver_objects(self, tree_node_css, 'Domain tree')
        tree_node_iter=[tree_node_value.text.strip() for tree_node_value in tree_node_objs if tree_node_value.is_displayed()]
        utils.verify_list_values(self, expected_domain_tree_list, tree_node_iter, msg, assert_type=assert_type)
    
    def close_filter_model_window(self):
        """
        Description : Click on close icon button to close filter model window
        """
        close_btn_class = "div[data-ibx-type='pdFilterWindow'] .ibx-title-bar-close-button"
        close_btn_obj = utils.validate_and_get_webdriver_object(self, close_btn_class, "Filter model window close button")
        coreutils.left_click(self, close_btn_obj)
        
    def select_page_from_bottom_tab(self, page_name):
        """
        Descriptions : This method used to click on tab in bottom page tab.
        example usage : select_page_from_bottom_tab("Panel 1")
        """
        tabs_css = ".designer-pane>.ibx-tab-position-bottom .ibx-tab-button"
        tabs_obj = utils.validate_and_get_webdriver_objects(self, tabs_css, "Bottom page tabs")
        for tab in tabs_obj :
            if tab.text.strip() == page_name :
                page_tab = tab
                break
        else :
            error_msg = "[{0}] page not exists in bottom page tab".format(page_name)
            raise LookupError(error_msg)
        coreutils.left_click(self, page_tab)

    def maximize_container(self, container_title, container_position=1):
        """
        Descriptions : Click on maximize icon to maximize container
        example usage : maximize_container("Panel 1")
        """
        container_object = pd_miscelaneous.get_pd_container_object(self, container_title, container_position)
        maximize_icon = utils.validate_and_get_webdriver_object(self, ".pd-container-title-button .ibx-glyph-expand", "Container maximize", container_object)
        coreutils.left_click(self, maximize_icon)
        
    def minimize_container(self, container_title, container_position=1):
        """
        Descriptions : Click on maximize icon to maximize container
        example usage : minimize_container("Panel 1")
        """
        container_object = pd_miscelaneous.get_pd_container_object(self, container_title, container_position)
        minimize_icon = utils.validate_and_get_webdriver_object(self, ".pd-container-title-button .ibx-glyph-compress", "Container minimize", container_object)
        coreutils.left_click(self, minimize_icon)
    
    def select_container_option(self, container_title, option, container_position=1):
        """
        Descriptions : click on container options icon and select option
        example usage : select_container_option("Panel 1", "Refresh")
        """
        container_object = pd_miscelaneous.get_pd_container_object(self, container_title, container_position)
        option_icon_obj = utils.validate_and_get_webdriver_object(self, "[title='Options']", "Container option menu icon", container_object)
        coreutils.left_click(self, option_icon_obj)
        pd_miscelaneous.select_page_designer_context_menu(self, option)
    
    def search_content(self, text, enter=False, click_search_icon=False):
        """
        Descriptions : Click on content search textbox and type text to search contents
        :arg1 - enter - Press enter key if enter = True.
        :arg2 - click_search - click on search icon button if click_search = True.
        :Usage - search_content("Category", enter=True)
        """
        search_textbox = utils.validate_and_get_webdriver_object(self, ContentTab_Locators.CONTENT_SEARCH_TEXTBOX_CSS, "Content search textbox")
        coreutils.left_click(self, search_textbox)
        search_textbox.send_keys(text)
        time.sleep(1)
        if enter == True :
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.enter_key)
            else:
                keyboard.send('enter')
        if click_search_icon == True :
            search_btn = utils.validate_and_get_webdriver_object(self, ContentTab_Locators.CONTENT_SEARCH_BUTTON_CSS, "Content search button")
            coreutils.left_click(self, search_btn)
    
    def click_clear_content_search(self):
        """
        Descriptions : Click on content search clear icon button to clear 
        Usage : clear_content_search("Category", "01.01")
        """
        search_textbox = utils.validate_and_get_webdriver_object(self, ContentTab_Locators.CONTENT_SEARCH_TEXTBOX_CSS, "Content search textbox")
        coreutils.python_left_click(self, search_textbox)
        search_textbox_btn = utils.validate_and_get_webdriver_object(self, ContentTab_Locators.CONTENT_SEARCH_BUTTON_CSS, "Content search textbox")
        if Global_variables.browser_name == "firefox" :
            search_textbox.clear()
        else :
            coreutils.python_left_click(self, search_textbox_btn, element_location="middle_left", xoffset=-16)
        
    def verify_content_items_contain_specific_text(self, specific_text, step_num):
        """
        Descriptions : Verify content item contain specific text value.
        Usage : verify_content_items_contain_specific_text("Category", "01.01")
        """
        contents_obj = utils.validate_and_get_webdriver_objects(self, ContentTab_Locators.EXPANDED_CONTENT_ITEMS_CSS, "Content items")
        contents_items_text = javascript.get_elements_text(self, contents_obj)
        status = False
        for content_text in contents_items_text :
            if specific_text.lower() in content_text.lower() :
                status = True
            else :
                status = False
                break
        msg = "Step {0} : Verify all content items contain [{1}] text".format(step_num, specific_text)
        utils.asequal(self, status, True, msg)
    
    def find_content_item_and_scroll_into_view(self, content_item):
        """
        Descriptions : Find and scroll content item to bring into visible area.
        :Usage : find_content_item_and_scroll_into_view("Category_Sales")
        """
        pd_miscelaneous.find_pd_content_item_and_scroll_into_view(self, content_item)
        
    def verify_content_item_tooltip(self, content_item, expected_tooltip, step_num):
        """
        Descriptions : Hover mouse of content item and verify tooltip value
        :Usage : verify_content_item_tooltip("Category Sales", expcted_tooltip, "07.01")
        """
        msg = "Step {0} : Verify [{1}] tooltip displayed after hover mouse on [{2}] content item".format(step_num, expected_tooltip, content_item)
        content_item_obj = pd_miscelaneous.find_pd_content_item_and_scroll_into_view(self, content_item)
        coreutils.python_move_to_element(self, content_item_obj)
        time.sleep(2)
        actual_tooltip = utils.get_element_attribute(self, content_item_obj, 'title')
#         actual_tooltip = uiautomation.ToolTipControl().Name
        utils.asequal(self, expected_tooltip, actual_tooltip, msg)
    
    def verify_published_or_unpublished_content_items(self, content_type, expected_contents, step_num, assert_type="asin"):
        """
        Descriptions : Verify published or unpublished contents text
        :arg1 - content_type = 'published' or 'unpublshed'
        :Usage - verify_published_or_unpublished_content_items("published", ["C1224", "C34456"], "01.02")
        """
        actual_contents_text = []
        if content_type.lower() == "published":
            contents_css = ContentTab_Locators.PUBLISHED_CONTENT_CSS
            expected_style = "none"    
        elif content_type.lower() == "unpublished" :
            contents_css = ContentTab_Locators.UNPUBLISHED_CONTENT_CSS
            expected_style = "grayscale(1)"
        else :
            msg = "Invalid content type passed. Please 'published' or 'unpublished'"
            raise KeyError(msg)
        object_name = "{0} contents".format(content_type)
        contents = utils.validate_and_get_webdriver_objects(self, contents_css, object_name)
        visible_contents = [content for content in contents if content.is_displayed()]
        for content_obj in visible_contents:
            actual_style = content_obj.value_of_css_property("filter")
            content_text_obj = utils.validate_and_get_webdriver_object(self, ".tnode-label", "Content label", content_obj)
            if actual_style == expected_style :
                actual_contents_text.append(content_text_obj.text.strip())
        msg = "Step {0} : Verify {1} contents {2}".format(step_num, expected_contents, content_type)
        utils.verify_list_values(self, expected_contents, actual_contents_text, msg, assert_type)
    
    def verify_resource_or_parameters_label_value(self, panel_index, label_type, expected_label_value_list, step_num, assert_type="asequal"):
        """
        Descriptions : verify_resource_or_parameters_label_value
        :arg1 - panel_index = '1' or 2 or 3
        :arg2 - label_type = 'resource' or 'parameters'
        :arg3 - expected_label_value_list = ['Resource', 'Not set']
        :arg4 - step_num = '01.01'
        :Usage - verify_resource_or_parameters_label_value(1, "resource", ['Resource', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Category_Sales.fex'], "01.02")
        """
        index = str(panel_index) if type(panel_index) == int else panel_index
        panel_css = PD_LOCATORS.PD_CONTAINER_CSS+"[data-ibxp-title$='TITLE_"+index+"'] "
        resource_css = "div[class*='pdcnt-resource']"
        parameters_css = "div[class*='pdcnt-parameters']"
        resource_css_objs = utils.validate_and_get_webdriver_objects(self, panel_css+resource_css, 'resource label value')
        parameters_css_objs = utils.validate_and_get_webdriver_objects(self, panel_css+parameters_css, 'parameters label value')
        if label_type == 'resource':
            label_value_css = resource_css_objs
        if label_type == 'parameters':
            label_value_css = parameters_css_objs
        actual_label_value_list=[label_value.text.strip().replace('\n', ' ') for label_value in label_value_css if label_value.is_displayed()]
        msg = "Step {0} : Verify {1} label value {2} in panel{3}".format(step_num, label_type, expected_label_value_list, index)
        utils.verify_list_values(self, expected_label_value_list, actual_label_value_list, msg, assert_type)
    
    def verify_filter_modal_window_buttons(self, expected_buttons, msg, assert_type="asequal"):
        """
        Description : Verify filter modal window visible buttons text.
        :Usage - verify_filter_modal_window_buttons(["Submit", "Reset"], "Step 01.01 : Verify ["Submit", "Reset"] button are displayed")
        """
        buttons_objects = utils.validate_and_get_webdriver_objects(self, FilterModalWindowLocators.BUTTONS_CSS, "Filter modal window buttons")
        actual_buttons = [button.text.strip() for button in buttons_objects if button.is_displayed()]
        utils.verify_list_values(self, expected_buttons, actual_buttons, msg, assert_type)
    
    def verify_repository_widgets_items_text(self, expected_items_list, msg, assert_type="asequal"):
        """
        Description : Verify Repository Widgets tab items text 
        :Usage : verify_repository_widgets_items_text(["Explorer", "Link tile"], "Step 05.01 : Verify ["Explorer", "Link tile"] items displayed in Repository Widgets tab)
        """
        items_object = utils.validate_and_get_webdriver_objects(self, ".pd-repository-widgets [data-ibx-type='pdDraggableButton']", "Repository Widgets items")
        actual_items_list = [item.text.strip() for item in items_object if item.is_displayed()]
        utils.verify_list_values(self, expected_items_list, actual_items_list, msg, assert_type)
    
    def get_repository_widget_object(self, widget_name):
        """
        Description : Return the repository widget item object
        :usage - get_repository_widget_object("Link tile")
        """
        xpath = "//div[contains(@class, 'pd-repository-widgets')]//div[@data-ibx-type='pdDraggableButton'][normalize-space()='{0}']".format(widget_name)
        widget_objects = [widget for widget in self.driver.find_elements_by_xpath(xpath) if widget.is_displayed()]
        if widget_objects != [] :
            return widget_objects[0]
        else :
            error_msg = "'{0}' not exists in repository widget".format(widget_name)
            raise selenium_exceptions.NoSuchElementException(error_msg)
    
    def get_link_tile_widget_object_from_canvas(self, widget_position):
        """
        Description : Return the widget object from canvas
        """
        widget_objects = utils.validate_and_get_webdriver_objects(self, "div[data-ibx-type='pdContainer'].toolbar-hidden", "Canvas Link Tile Widget")
        widget_obj = widget_objects[widget_position -1]
        if widget_obj.is_displayed() :
            return widget_obj
        else :
            error_msg = "Link tile widget not visible in canvas"
            raise selenium_exceptions.ElementNotVisibleException(error_msg)
    
    def select_link_tile_widget_in_canvas(self, widget_position):
        """
        Description : Left click on link tile widget in canvas to select.
        :usage - select_link_tile_widget_in_canvas(1)
        """
        widget_obj = PageDesignerDesign.get_link_tile_widget_object_from_canvas(self, widget_position)
        coreutils.left_click(self, widget_obj)
    
    def select_container_in_canvas(self, container_title, container_title_index=1):
        """
        Description : Left click on link tile widget in canvas to select.
        :usage - select_container_in_canvas("Panel 1")
        """
        container_object = PageDesignerDesign.get_container_object(self, container_title, container_title_index)
        coreutils.left_click(self, container_object)
        
    def verify_add_content_dialog(self,expected_content_options,msg):
        """
        Descriptions:This method is used to verify the add content dialog.
        Scenario: add content appears while drag drop the content item to existing item it throws add_content_dialog
        Example usage:verify_add_content_panel_dialog(['Replace content','Add content as new tab','Cancel'], msg="Step 4.1")
        """
        content_option_elem=utils.validate_and_get_webdriver_objects(self,"[data-ibx-name='vbMain'] .ibx-dialog-content [class^='pd-add-content']","add_dialog_button")
        element=[i.text.strip() for i in content_option_elem if i.is_displayed()]
        utils.as_List_equal(self,element,expected_content_options,msg)
        
    def select_options_add_content_dialog(self,item_to_select):
        """
        Descriptions:This method is used to select options from the add content dialog.
        Scenario: add content appears while drag drop the content item to existing item in blank canvas it throws add_content_dialog
        Example usage:select_options_add_content_dialog(self,"Add content as new tab")
        """
        content_option_elem=utils.validate_and_get_webdriver_objects(self,"[data-ibx-name='vbMain'] .ibx-dialog-content [class^='pd-add-content']","add_dialog_button")
        for x in content_option_elem:
            if x.is_displayed() and x.text.strip() == item_to_select:
                option_to_select= x
                break
        else:
            raise LookupError('add_content_dialog not visible and opened.or might be CSS is wrong')
        coreutils.left_click(self,option_to_select)
    
    def select_options_from_add_content_dropdown(self,dropdown_option):
        """
        Descriptions:This method is used to select options from the add content dialog dilog dropdown values.
        Scenario: add content appears while drag drop the content item to existing item in blank canvas it throws add_content_dialog in this select options from dropdown
        Example usage:select_options_from_add_content_dropdown(self,"Add content as new slide")
        """
        dropdown_elem = utils.validate_and_get_webdriver_object(self,"[data-ibx-name='vbMain'] div[title='Show Menu']","add_content_dropdown_elem")
        coreutils.left_click(self,dropdown_elem)
        Wf_Mainpage.select_context_menu_item(self,dropdown_option)
        
    def verify_tooltip_of_carousel_item(self,expected_tooltip,msg):
        """
        Description: This method is uesd to verify the tooltip option is avialable in carousel items
        @param: ['Containers','Content','Controls']
        """
        carousel_items_elem=utils.validate_and_get_webdriver_objects(self,".ibx-csl-items-container [title^={0}]".format(expected_tooltip),"Carousel_items_css")
        for carousel_elem in carousel_items_elem:
            actual_tooltip=utils.get_element_attribute(self,carousel_elem,"title")
        utils.asequal(self,actual_tooltip,expected_tooltip,msg)
    
    def verify_tooltip_for_container_options(self,container_title,expected_title,msg):
        """
        Description: This method is used to verify the tooltip options for panel
        @param:coantainer_title= "Panel 1","Panel 2"
        Scenario: add container need to verify the the tooltip of panel option eg: maximize and options so on
        """
        container_obj=PageDesignerDesign.get_container_object(self, container_title)
        toolt_tip_obj=container_obj.find_element_by_css_selector("[title='{0}']".format(expected_title))
        actual_title=utils.get_element_attribute(self, toolt_tip_obj,"title")
        utils.asequal(self,actual_title,expected_title,msg)
    
    def click_options_verify_message(self,container_title,expected_message,msg):
        """
        Description:This method is used to verify the click options in panel and verify the message
        Usage:-click_options_verify_message("Panel 1","This feature is enable only techinal preview is enable","Step 6.1")
        """
        container_obj=PageDesignerDesign.get_container_object(self, container_title)
        option_obj=container_obj.find_element_by_css_selector("[title='Options']")
        coreutils.python_left_click(self,option_obj)
        time.sleep(2)
        actual_message=utils.validate_and_get_webdriver_object(self, ".pd-cont-menu-notif-text","panel_notification").text.strip()
        utils.asequal(self,actual_message,expected_message,msg)
    
    def verify_notification_popup_message(self, expected_msg, step_num):
        """
        Description : Verify any notification popup message
        :Usage : verify_notification_popup_message("Sample notification", "01.02")
        """
        popup_css = ".ibxtool-filter-notif-popup.pop-top"
        utils.synchronize_until_element_is_visible(self, popup_css, 20)
        actual_msg = self.driver.find_element_by_css_selector(popup_css).text.strip()
        msg = "Step {0} : Verify notification popup message".format(step_num)
        utils.asequal(self, expected_msg, actual_msg, msg)
    
    def _get_embedded_content_object(self, content):
        """
        Description : Return the Embedded content object
        :Usage - _get_embedded_content_object('Chart 1')
        """
        xpath = "//div[contains(@class, 'pd-embedded-tree')]//div[@data-ibx-type='pdEmbeddedTreeNode'][normalize-space()='{0}']".format(content)
        content = self.driver.find_elements_by_xpath(xpath)
        if content != [] :
            return content[0]
        else :
            raise_msg = "'{0}' not exists in Embedded content container".format(content)
            raise KeyError(raise_msg)
    
    def drag_embedded_content_to_canvas_section(self, content, canvas_section_cell, section_num=1):
        """
        Descriptions : This method used to drag Embedded content to page container section
        :Usage - drag_embedded_content_to_canvas_section('Chart 1', 1)
        """
        content_obj = PageDesignerDesign._get_embedded_content_object(self, content)
        section_obj = PageDesignerDesign._get_page_section_object(self, section_num)
        section_cell_obj = section_obj.find_elements_by_css_selector(".pd-page-section-grid-box")[canvas_section_cell-1]
        source_cord=coreutils.get_web_element_coordinate(self, content_obj)
        target_cord=coreutils.get_web_element_coordinate(self, section_cell_obj)
        coreutils.drag_and_drop(self, source_cord['x'], source_cord['y'], target_cord['x'], target_cord['y'])
        
class AddFilterControlsDialog(BasePage):
    
    parent_css = "div[data-ibx-type='pdAddFilters']"
    parameter_values_css = parent_css + " div[style*='grid-column-start: 2'].pd-af-list-cell"
    
    def __init__(self, driver, parameter=None):
        super(AddFilterControlsDialog, self).__init__(driver)
        self.parameter = parameter
    
    def check(self):
        """
        Description : This method will click on parameter checkbox to check
        """
        uncheck_css = "div[class*='marker-uncheck']"
        checkbox_cell_obj = self.__get_cell_object_by_parameter(1)
        checkbox_obj = utils.validate_and_get_webdriver_object(self, uncheck_css, "Add filter controls parameter uncheck box", parent_object=checkbox_cell_obj)
        coreutils.left_click(self, checkbox_obj)
        
    def uncheck(self):
        """
        Description : This method will click on parameter check box to uncheck
        """
        checkbox_css = "div[class*='marker-check']"
        checkbox_cell_obj = self.__get_cell_object_by_parameter(1)
        checkbox_obj = utils.validate_and_get_webdriver_object(self, checkbox_css, "Add filter controls parameter check box", parent_object=checkbox_cell_obj)
        coreutils.left_click(self, checkbox_obj)
        
    def verify_title(self, step_num):
        """
        Description : This method will verify the title
        """
        expected_title = "Add Filter Controls"
        title_css = AddFilterControlsDialog.parent_css + " .ibx-title-bar-caption"
        actual_title = utils.validate_and_get_webdriver_object(self, title_css, "Add filter controls dialog title").text.strip()
        msg = "Step {0} : Verify Add filter controls dialog displayed with {1} title".format(step_num, expected_title)
        utils.asequal(self, expected_title, actual_title, msg)
    
    def click_add_filter_controls_button(self):
        """
        Description : This method will left click on Add filter controls button
        """
        btn_css = AddFilterControlsDialog.parent_css + " .ibx-dialog-apply-button"
        btn_obj = utils.validate_and_get_webdriver_object(self, btn_css, "Add filter controls button")
        coreutils.left_click(self, btn_obj)
        utils.synchronize_until_element_disappear(self, AddFilterControlsDialog.parent_css, 40)
        
    def click_cancel_filter_controls_button(self):
        """
        Description : This method will left click on Cancel button
        """
        btn_css = AddFilterControlsDialog.parent_css + " .ibx-dialog-cancel-button"
        btn_obj = utils.validate_and_get_webdriver_object(self, btn_css, "Add filter controls dialog Cancel button button")
        coreutils.left_click(self, btn_obj)
        utils.synchronize_until_element_disappear(self, AddFilterControlsDialog.parent_css, 40)    
        
    def __get_cell_object_by_parameter(self, column_number):
        """
        Descriptions : This method will return the cell object by parameter value
        example usage : __get_cell_object_by_parameter(1)
        """
        parameter_values_objects = utils.validate_and_get_webdriver_objects(self, AddFilterControlsDialog.parameter_values_css, "Add filter controls parameter values")
        starting_row = 2
        for row, parameter in enumerate(parameter_values_objects, starting_row) :
            if parameter.text.strip() == self.parameter :
                break
        else :
            error_msg = "[{0}] parameter not exists in Add filter Controls dialog".format(self.parameter)
            raise LookupError(error_msg)
        cell_css = AddFilterControlsDialog.parent_css + " div[style*='grid-row-start: {row}'][style*='grid-column-start: {column}']".format(row=row, column=column_number)
        cell_object = utils.validate_and_get_webdriver_object(self, cell_css, "Add filter controls cell")
        return cell_object

class TabContainer :
    
    def __init__(self, driver, container_title, container_position=1):
        
        self.driver = driver
        self.__container_title = container_title
        self.__container_obj = pd_miscelaneous.get_pd_container_object(self, self.__container_title, container_position)
        self.__javascript = javascript(self.driver)
        
    def select_tab(self, tab_name, tab_index=1):
        """
        Descriptions : Click on tab to select
        example usage : select_tab("Tab1")
        """
        xpath = "//div[normalize-space()='{0}'][@role='tab'][{1}]".format(tab_name, tab_index)
        tab_objs = self.__container_obj.find_elements_by_xpath(xpath)
        if len(tab_objs)>0 :
            self.__javascript.scrollIntoView(tab_objs[0])
            coreutils.left_click(self, tab_objs[0])
        else :
            error_msg = "[{0}] tab not added in [{1}] container".format(tab_name, self.__container_title)
            raise LookupError(error_msg)
        
    def select_tab_from_tab_overflow_popup(self, tab_name, tab_index=1):
        """
        Descriptions : select_tab_from_tab_overflow_menu
        example usage : select_tab_from_tab_overflow_popup("Tab1")
        """
        xpath = "//div[normalize-space()='{0}'][@role='menuitem'][{1}]".format(tab_name, tab_index)
        tab_objs = self.driver.find_elements_by_xpath(xpath)
        if len(tab_objs)>0 :
            coreutils.left_click(self, tab_objs[0])
        else :
            error_msg = "[{0}] tab not added in [{1}] container".format(tab_name, self.__container_title)
            raise LookupError(error_msg)
    
    def click_new_tab_plus_icon(self):
        """
        Descriptions : Click on new tab plus icon in tab container
        example usage : click_new_tab_plus_icon()
        """
        plus_icon_obj = utils.validate_and_get_webdriver_object(self, ".tab-new-button", "Tab container 'New tab' plus icon", self.__container_obj)
        coreutils.left_click(self, plus_icon_obj)
    
    def click_new_tab_plus_icon_in_tab_overflow_popup(self):
        """
        Descriptions : Click on new tab plus icon in tab overflow menu 
        example usage : click_new_tab_plus_icon_in_tab_overflow_popup()
        """
        plus_icon_obj = utils.validate_and_get_webdriver_object(self, ".tab-overflow-menu .ibx-glyph-plus.ibx-label-glyph.ibx-icons", "Tab container 'New tab' plus icon")
        coreutils.left_click(self, plus_icon_obj)
        
    def click_tab_overflow_icon(self):
        """
        Descriptions : Click on tab overflow icon in tab container
        example usage : click_tab_overflow_icon()
        """
        overflow_icon_obj = utils.validate_and_get_webdriver_object(self, ".tab-overflow-button", "Tab container 'Tab overflow' icon", self.__container_obj)
        coreutils.left_click(self, overflow_icon_obj)
    
    def maximize(self):
        """
        Descriptions : Click on maximize icon to maximize
        example usage : maximize()
        """
        PageDesignerDesign.maximize_container(self, self.__container_title)
        
    def minimize(self):
        """
        Descriptions : Click on maximize icon to maximize
        example usage : minimize()
        """
        PageDesignerDesign.minimize_container(self, self.__container_title)
        
    def verify_tabs(self, expected_tabs_list, step_num, compare_type='asequal'):
        """
        Descriptions : Verify visible tabs title.
        example usage : verify_tabs(['Tab 1', 'Tab 2', 'Tab 3'], "04.01")
        """
        tabs_objects = utils.validate_and_get_webdriver_objects(self, ".ibx-tab-button .ibx-label-text", "Tab container tabs", self.__container_obj)
        actual_tabs = [tab.text.strip() for tab in tabs_objects if tab.is_displayed()]
        msg = "Step {0} : Verify {1} tabs are added in [{2}] tab container".format(step_num, expected_tabs_list, self.__container_title)
        utils.verify_list_values(self, expected_tabs_list, actual_tabs, msg, assert_type=compare_type)
    
    def verify_tabs_in_tab_overflow_popup(self, expected_tabs_list, step_num, compare_type='asequal'):
        """
        Descriptions : Verify visible tabs title in tab overflow popup.
        example usage : verify_tabs_in_tab_overflow_popup(['Tab 1', 'Tab 2', 'Tab 3'], "04.01")
        """
        tabs_objects = utils.validate_and_get_webdriver_objects(self, "div.tab-overflow-menu-item:not([title])", "Tab overflow menu items")
        actual_tabs = [tab.text.strip() for tab in tabs_objects if tab.is_displayed()]
        msg = "Step {0} : Verify {1} tabs are displayed in tab overflow popup".format(step_num, expected_tabs_list, self.__container_title)
        utils.verify_list_values(self, expected_tabs_list, actual_tabs, msg, assert_type=compare_type)
        
    def verify_new_tab_plus_icon_displayed(self, step_num):
        """
        Descriptions : Verify New Tab plus icon is displayed in tab container
        example usage : verify_new_tab_plus_icon_displayed("01.01")
        """
        expected_icon_value = "\ue97d".encode()
        plus_icon_obj = utils.validate_and_get_webdriver_object(self, ".tab-new-button .ibx-glyph-plus.ibx-label-glyph.ibx-icons", "Tab container 'New tab' plus icon", self.__container_obj)
        actual_icon_value=javascript.get_element_before_style_properties(self, plus_icon_obj, 'content').replace('"', '').encode()
        visible_status = True if expected_icon_value == actual_icon_value and plus_icon_obj.is_displayed() else False
        msg = "Step {0} : Verify 'New tab' plus icon displayed in [{1}] container".format(step_num, self.__container_title)
        utils.asequal(self, visible_status, True, msg)
        
    def verify_new_tab_plus_icon_not_displayed(self, step_num):
        """
        Descriptions : Verify New Tab plus icon is not displayed in tab container
        example usage : verify_new_tab_plus_icon_not_displayed("01.01")
        """
        plus_icon_obj = utils.validate_and_get_webdriver_object(self, ".tab-new-button", "Tab container 'New tab' plus icon", self.__container_obj)
        msg = "Step {0} : Verify 'New tab' plus icon not displayed in [{1}] container".format(step_num, self.__container_title)
        utils.asequal(self, plus_icon_obj.is_displayed(), False, msg)
    
    def verify_selected_tab(self, selected_tab_list, step_num):
        """
        Descriptions : Verify selected tab 
        example usage : verify_selected_tab(["Tab 2"], "01.01")
        """
        selected_tab_objs = utils.validate_and_get_webdriver_objects(self, ".ibx-tab-button.checked", "Tab container selected tab", self.__container_obj)
        actual_selected_tabs = [tab.text.strip() for tab in selected_tab_objs if tab.is_displayed()]
        msg = "Step {0} : Verify {1} tab selected in [{2}] container".format(step_num, selected_tab_list, self.__container_title)
        utils.asequal(self, selected_tab_list, actual_selected_tabs, msg)
        
    def verify_selected_tab_in_tab_overflow_popup(self, selected_tab_list, step_num):
        """
        Descriptions : Verify selected tab 
        example usage : verify_selected_tab(["Tab 2"], "01.01")
        """
        selected_tab_objs = utils.validate_and_get_webdriver_objects(self, "div.tab-overflow-menu-item.selected-page", "Tab overflow selected tab")
        actual_selected_tabs = [tab.text.strip() for tab in selected_tab_objs if tab.is_displayed() and tab.value_of_css_property("font-weight") == '700']
        msg = "Step {0} : Verify {1} tab selected in tab overflow popup".format(step_num, selected_tab_list)
        utils.asequal(self, selected_tab_list, actual_selected_tabs, msg)
        
    def verify_tab_overflow_icon_displayed(self, step_num):
        """
        Descriptions : Verify tab overflow icon is displayed in tab container
        example usage : verify_tab_overflow_icon_displayed("01.01")
        """
        expected_icon_value = "\ue96e".encode()
        overflow_icon_obj = utils.validate_and_get_webdriver_object(self, ".tab-overflow-button .ibx-glyph-ellipsis-h.ibx-label-glyph.ibx-icons", "Tab container 'Tab overflow' icon", self.__container_obj)
        actual_icon_value=javascript.get_element_before_style_properties(self, overflow_icon_obj, 'content').replace('"', '').encode()
        visible_status = True if expected_icon_value == actual_icon_value and overflow_icon_obj.is_displayed() else False
        msg = "Step {0} : Verify 'Tab overflow' icon displayed in [{1}] container".format(step_num, self.__container_title)
        utils.asequal(self, visible_status, True, msg)
        
    def verify_tab_overflow_icon_not_displayed(self, step_num):
        """
        Descriptions : Verify tab overflow icon is not displayed in tab container
        example usage : verify_tab_overflow_icon_not_displayed0("01.01")
        """
        overflow_icon_obj = utils.validate_and_get_webdriver_object(self, ".tab-overflow-button", "Tab container 'Tab overflow' icon", self.__container_obj)
        msg = "Step {0} : Verify 'Tab overflow' icon not displayed in [{1}] container".format(step_num, self.__container_title)
        utils.asequal(self, overflow_icon_obj.is_displayed(), False, msg)
    
    def verify_new_tab_plus_icon_displayed_in_tab_overflow_popup(self, step_num):
        """
        Descriptions : Verify New Tab plus icon is displayed in tab container
        example usage : verify_new_tab_plus_icon_displayed_in_tab_overflow_popup("01.01")
        """
        expected_icon_value = "\ue97d".encode()
        last_menu_item = utils.validate_and_get_webdriver_objects(self, ".tab-overflow-menu .tab-overflow-menu-item", "Tab overflow menu items")[-1]
        plus_icon_obj = utils.validate_and_get_webdriver_object(self, ".ibx-glyph-plus.ibx-label-glyph.ibx-icons", "'Tab overflow New tab' plus icon", last_menu_item)
        actual_icon_value=javascript.get_element_before_style_properties(self, plus_icon_obj, 'content').replace('"', '').encode()
        visible_status = True if expected_icon_value == actual_icon_value and plus_icon_obj.is_displayed() else False
        msg = "Step {0} : Verify 'New tab' plus icon displayed in tab overflow menu".format(step_num)
        utils.asequal(self, visible_status, True, msg)
        
    def verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup(self, step_num):
        """
        Descriptions : Verify New Tab plus icon is not displayed in tab overflow menu
        example usage : verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("01.01")
        """
        plus_icon_obj = self.driver.find_elements_by_css_selector(".tab-overflow-menu .ibx-glyph-plus.ibx-label-glyph.ibx-icons")
        msg = "Step {0} : Verify 'New tab' plus icon not displayed in tab overflow menu".format(step_num)
        utils.asequal(self, len(plus_icon_obj), 0, msg)
    
    def verify_add_content_button_displayed(self, step_num):
        """
        Descriptions : Verify Add content button displayed in Tab container
        example usage : verify_add_content_button_displayed("01.01")
        """
        selected_tab_obj = utils.validate_and_get_webdriver_object(self, ".tpg-selected", "Selected tab", self.__container_obj)
        add_content_obj = Designer_Canvas.get_panel_add_container_object(self, selected_tab_obj, 'tab')
        actual_status = Designer_Canvas.get_add_content_button_icon_visible_status(self, add_content_obj)
        msg = "Step {0} : Verify 'Add Content' plus button displayed in [{1}] container".format(step_num, self.__container_title)
        utils.asequal(self, True, actual_status, msg)
    
    def click_add_content_button(self):
        """
        Descriptions : Click on Add content button in Tab container
        example usage : click_add_content_button()
        """
        selected_tab_obj = utils.validate_and_get_webdriver_object(self, ".tpg-selected", "Selected tab", self.__container_obj)
        add_content_obj = Designer_Canvas.get_panel_add_container_object(self, selected_tab_obj, 'tab')
        coreutils.left_click(self, add_content_obj)
    
    def verify_add_content_button_tooltip(self, step_num):
        """
        Descriptions : Verify Add content button tooltip in Tab container
        example usage : verify_add_content_button_tooltip("01.01")
        """
        selected_tab_obj = utils.validate_and_get_webdriver_object(self, ".tpg-selected", "Selected tab", self.__container_obj)
        msg = "Step {0} : Verify 'Add content' tooltip displayed after hover mouse on add content in [{1}] tab container".format(step_num, self.__container_title)
        Portal_canvas(self.driver).verify_add_content_button_tooltip_in_container(selected_tab_obj, "tab", "Add content", msg)
    
    def select_option(self, option_name):
        """
        Description : Click on options icon and select option
        :usage - select_option("Remove")
        """
        PageDesignerDesign.select_container_option(self, self.__container_title, option_name)

class AccordionContainer :
    
    def __init__(self, driver, title, position=1):
        
        self.driver = driver
        self.__title = title
        self.__parent_css = ".pd-cont-accordion-pane"
        self.__container = pd_miscelaneous.get_pd_container_object(self, self.__title, position)
    
    def verify_area_title(self, expected_area, step_num, assert_type='asequal'):
        """
        Description : Verify area titles
        Example : verify_area_title(['Area 1'], "01.02")
        """
        area_objects = self.__container.find_elements_by_css_selector(self.__parent_css + " .ibx-accordion-page-button")
        actual_area = [area.text.strip() for area in area_objects if area.is_displayed()]
        msg = "Step {0} : Verify accordion area title".format(step_num)
        utils.verify_list_values(self, expected_area, actual_area, msg, assert_type)