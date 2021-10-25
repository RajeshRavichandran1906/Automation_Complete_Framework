from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import ia_join as Locators
import time

class IAJoin :
    
    def __init__(self, driver):
        
        self.driver = driver
        self._utils = UtillityMethods(self.driver)
        self._coreutils = CoreUtillityMethods(self.driver)
        self._locators = Locators
        self._short_time_sleep = 20
        self._medium_time_sleep = 80
        self._long_time_sleep = 180
        
    def click_add_new(self):
        """
        Description : Left click on Add New option in top tool bar
        """
        add_new = self.driver.find_element(*self._locators.TopToolBar.AddNew)
        self._coreutils.left_click(add_new)
        self._utils.synchronize_with_visble_text("#dlgIbfsOpenFile7", "Open", self._medium_time_sleep)
    
    def click_blend(self):
        """
        Description : Left click on Blend option in top tool bar
        """
        blend = self.driver.find_element(*self._locators.TopToolBar.Blend)
        self._coreutils.left_click(blend)
    
    def click_edit(self):
        """
        Description : Left click on Edit option in top tool bar
        """
        edit = self.driver.find_element(*self._locators.TopToolBar.Edit)
        self._coreutils.left_click(edit)
    
    def click_filter(self):
        """
        Description : Left click on Filter option in top tool bar
        """
        filter_ = self.driver.find_element(*self._locators.TopToolBar.Filter)
        self._coreutils.left_click(filter_)
    
    def click_index_only(self):
        """
        Description : Left click on Index Only option in top tool bar
        """
        index_only = self.driver.find_element(*self._locators.TopToolBar.IndexOnly)
        self._coreutils.left_click(index_only)
    
    def click_view(self):
        """
        Description : Left click on View option in top tool bar
        """
        view = self.driver.find_element(*self._locators.TopToolBar.View)
        self._coreutils.left_click(view)
    
    def click_remove(self):
        """
        Description : Left click on Remove option in top tool bar
        """
        remove = self.driver.find_element(*self._locators.TopToolBar.Remove)
        self._coreutils.left_click(remove)
        
    def click_ok_button(self):
        """
        Description : Left click on OK button in bottom tool bar
        """
        ok_button = self.driver.find_element(*self._locators.BottomToolBar.Ok)
        self._coreutils.left_click(ok_button)
        self._utils.synchronize_until_element_disappear(self._locators.PARENT_ID, self._medium_time_sleep)
    
    def click_cancel_button(self):
        """
        Description : Left click on Cancel button in bottom tool bar
        """
        ok_button = self.driver.find_element(*self._locators.BottomToolBar.Ok)
        self._coreutils.left_click(ok_button)
        self._utils.synchronize_until_element_disappear(self._locators.PARENT_ID, self._medium_time_sleep)
    
    def link_fields(self, source_title, source_field, target_title, target_field, source_title_index=1, target_title_index=1, source_field_index=1, target_field_index=1):
        """
        Description : Drag the join field from source master file and drop in target field to link join
        :Usage : link_fields("baseapp/dimensions/wf_retail_product", "ID_VENDOR", "baseapp/dimensions/wf_retail_vendor", "ID_VENDOR")
        """
        source_field_object = self.__get_join_field_object(source_title, source_field, source_title_index, source_field_index)
        target_field_object = self.__get_join_field_object(target_title, target_field, target_title_index, target_field_index)
        source_field_location = self._coreutils.get_web_element_coordinate(source_field_object)
        target_field_location = self._coreutils.get_web_element_coordinate(target_field_object)
        self._coreutils.drag_and_drop(source_field_location['x'], source_field_location['y'], target_field_location['x'], target_field_location['y'])
    
    def add_new_data_file(self, folder_path, file_name):
        """
        Description : Click on Add New button and select data file to join
        :Usage : add_new_data_file("baseapp", "wf_retail_lite)
        """
        self.click_add_new()
        self._utils.select_masterfile_in_open_dialog(folder_path, file_name)
        self._utils.synchronize_with_visble_text(self._locators.PARENT_ID, file_name, self._medium_time_sleep)
        
    def __get_join_panel_object(self, panel_title, panel_index=1):
        """
        Description : Return the join panel object by title
        :arg - panel_title : Name of the master file name (join panel title)
        :arg - panel_index : panel_index = 2 if two join panels are have same title
        :Usage : __get_join_panel_object("baseapp/dimensions/wf_retail_product")
        """
        panels_object = self.driver.find_elements(*self._locators.Canvas.JoinPanels)
        panels_title = [title.text.strip() for title in self.driver.find_elements(*self._locators.Canvas.JoinPanelsTitle)]
        panels_index = [index for index, title in enumerate(panels_title) if title == panel_title]
        if panels_index != [] and len(panels_index) >= panel_index:
            panel_object = panels_object[panels_index[panel_index - 1]]
            return panel_object
        else :
            msg = "'{0}' join panel not exists".format(panel_title)
            raise KeyError(msg)
    
    def __get_join_field_object(self, panel_title, field_name, panel_index=1, field_index=1):
        """
        Description : Return the join field object by title from specific join panel
        :Usage : __get_join_field_object("baseapp/dimensions/wf_retail_product", "ID_PRODUCT")
        """
        join_panel_object = self.__get_join_panel_object(panel_title, panel_index)
        join_panel_id = join_panel_object.get_attribute("id")
        join_fields_css = "#" + join_panel_id + " " + self._locators.Canvas.JoinFields[1]
        self._coreutils.python_move_to_element(join_panel_object)
        time.sleep(2)
        self._utils.scroll_down_and_find_item_using_mouse(join_fields_css, field_name)
        field_xpath = "//div[@id='{0}']//table/tbody/tr/td[normalize-space()='{1}'][1]".format(join_panel_id, field_name)
        field_objects = self.driver.find_elements_by_xpath(field_xpath)
        if field_objects != [] and len(field_objects) >= field_index:
            return field_objects[field_index - 1]
        else :
            msg = "'{0}' field not exists in '{0}' join panel".format(field_name, panel_title)
            raise KeyError(msg)
            