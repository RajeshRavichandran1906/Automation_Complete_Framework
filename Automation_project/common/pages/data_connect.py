from common.lib.webfocus.data_tool_bar import DataToolBar
from common.lib.webfocus.data_content_tree import DataContentTree
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.base import BasePage


class ContentTree(BasePage):
    
    def __init__(self, driver):
        
        super(ContentTree, self).__init__(driver)
        self._util = UtillityMethods(self.driver)
        self._content_tree = DataContentTree(self.driver)
    
    def verify_conternt_tree_items(self, expected_tree_list, msg, assert_type='asequal'):
        """
        Description : This method will verify visible content tree items
        """
        actual_content_tree = self._content_tree.get_content_tree_items_text()
        self._util.verify_list_values(expected_tree_list, actual_content_tree, msg, assert_type)


class ToolBar(BasePage):
    
    def __init__(self, driver):
        
        super(ToolBar, self).__init__(driver)
        self._core_util = CoreUtillityMethods(self.driver)
        self._util = UtillityMethods(self.driver)
        self.__toolbar = DataToolBar(self.driver)
        
    def click_on_toolbar_button(self, button_name):
        """
        Description : This method will left click on top tool bar buttons
        @param : button_name = button name is title of tool bar icon. if mouse hover on any icon in tool bar, icon title will display.
        @usagw : click_on_toolbar_button('User') 
        """
        button_object = self.__toolbar.get_toolbar_item_object(button_name)
        self._core_util.left_click(button_object, button_object)
        
    def verify_visible_toolbar_buttons(self, expected_buttons_list, msg, assert_type='asequal'):
        """
        Description : This method will verify visible tool bar icons 
        """
        actual_visible_buttons_list = self.__toolbar.get_visible_tool_bar_items_title()
        self._util.verify_list_values(expected_buttons_list, actual_visible_buttons_list, msg, assert_type)
