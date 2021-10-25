from common.pages import data_connect
from common.lib.base import BasePage

class ContentTree(BasePage):
    
    def __init__(self, driver):
        
        super(ContentTree, self).__init__(driver)
        self._content_tree = data_connect.ContentTree(self.driver)
    
    def verify_all_conternt_tree_items(self, expected_tree_list, msg):
        """
        Description : This method will all verify visible content tree items
        """
        self._content_tree.verify_conternt_tree_items(expected_tree_list, msg)
    
    def verify_specific_conternt_tree_items(self, expected_tree_list, msg):
        """
        Description : This method will verify specific visible content tree items
        """
        self._content_tree.verify_conternt_tree_items(expected_tree_list, msg, assert_type='asin') 
        
        
class ToolBar(BasePage):
    
    def __init__(self, driver):
        
        super(ToolBar, self).__init__(driver)
        self._toobar = data_connect.ToolBar(self.driver)
        
    def click_on_toolbar_button(self, button_name):
        """
        Description : This method will left click on top tool bar buttons
        @param : button_name = button name is title of tool bar icon. if mouse hover on any icon in tool bar, icon title will display.
        @usagw : click_on_toolbar_button('User') 
        """
        self._toobar.click_on_toolbar_button(button_name)
        
    def verify_all_visible_toolbar_buttons(self, expected_buttons_list, msg):
        """
        Description : This method will verify visible tool bar icons 
        """
        self._toobar.verify_visible_toolbar_buttons(expected_buttons_list, msg)
    
    def verify_specific_visible_toolbar_buttons(self, expected_buttons_list, msg):
        """
        Description : This method will verify specific visible tool bar icons 
        """
        self._toobar.verify_visible_toolbar_buttons(expected_buttons_list, msg, assert_type='asin')
    
    def verify_toolbar_button_not_visible(self, expected_buttons_list, msg):
        """
        Description : This method will verify specific tool bar icons are not visible in toolbar
        """
        self._toobar.verify_visible_toolbar_buttons(expected_buttons_list, msg, assert_type='asnotin')


class DataConnect(ContentTree, ToolBar):
    
    def __init__(self, driver):
        
        super(DataConnect, self).__init__(driver)