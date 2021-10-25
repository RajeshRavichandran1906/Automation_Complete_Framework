from common.lib.utillity import UtillityMethods
from common.lib.base import BasePage

CONTRNT_TREE_PARENT_CSS = "#WcMultiframesContentView-1"

class DataContentTree(BasePage): 
    
    def __init__(self, driver):

        super(DataContentTree, self).__init__(driver)
        self._util = UtillityMethods(self.driver)
    
    def get_content_tree_rows_object(self):
        """
        Description : This method will return content view tree items element object as list
        """
        content_tree_items_css = CONTRNT_TREE_PARENT_CSS + " div.wcx-grid-body-tree-row"
        content_tree_items_object = self._util.validate_and_get_webdriver_objects(content_tree_items_css, 'Data content view items')
        return content_tree_items_object
    
    def get_content_tree_items_text(self):
        """
        Description : This method will return content view tree item element text as list
        """
        items_css = "div.wcx-grid-body-row-cell>div:nth-child(2)>div[class='ibx-label-text']"
        content_tree_row_objects = self.get_content_tree_rows_object()
        content_tree_items_object = [self._util.validate_and_get_webdriver_object(items_css, 'Tree items', row_obj) for row_obj in content_tree_row_objects]
        content_tree_items_text_list = [item.text.strip() for item in content_tree_items_object] 
        return content_tree_items_text_list

