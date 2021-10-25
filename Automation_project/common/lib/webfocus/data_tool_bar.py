from common.lib.utillity import UtillityMethods
from common.lib.javascript import JavaScript
from common.lib.base import BasePage

TOOL_BAR_PARENT_CSS = "div.wcx-mainribbon-bar"

class DataToolBar(BasePage): 
    
    def __init__(self, driver):

        super(DataToolBar, self).__init__(driver)
        self._util = UtillityMethods(self.driver)
        self._javascript = JavaScript(self.driver)
        
    def get_toolbar_items_object(self):
        """
        Description : This method will return data ribbon bar items element object as list
        """
        toolbar_bar_items_css = TOOL_BAR_PARENT_CSS + " div[title].wcx-ribbon-button"
        tool_bar_items_object = self._util.validate_and_get_webdriver_objects(toolbar_bar_items_css, 'Data tool bar items')
        return tool_bar_items_object
    
    def get_toolbar_item_object(self, toolbar_item_title):
        """
        Description : This method will return specific data ribbon bar icon element object
        """
        tool_bar_item_css = TOOL_BAR_PARENT_CSS + " div[title='{0}'].wcx-ribbon-button".format(toolbar_item_title)
        ribbon_bar_item_object = self._util.validate_and_get_webdriver_objects(tool_bar_item_css, 'Data tool bar {0} option'.format(toolbar_item_title))
        return ribbon_bar_item_object
    
    def get_visible_tool_bar_items_title(self):
        """
        """
        visible_toolbar_bar_items = []
        toolbar_item_icon_css = {
            'New' : 'ibi-icons',
            'Filter' : 'fa-filter',
            'Preferences' : 'fa-sliders-h',
            'Impact Analysis' : 'ibi-icons',
            'Manage' : 'material-icons',
            'Reset' : 'fa-undo-alt',
            'Start Over' : 'ibx-icons',
            'Options' : 'fa-ellipsis-v',
            'User' : 'fa-user',
            'Help' : 'ibi-icons'    
        }
        
        toolbar_item_icon_name = {
            'New' : 'new_item',
            'Impact Analysis' : 'impact_analysis',
            'Manage' : 'settings_applications',
            'Help' : 'help_question_mark'    
        }
        
        toolbar_item_icon_before_content_value = {
            'Filter' : '\uf0b0',
            'Reset' : '\uf2ea',
            'Start Over' : '\ue9c4',
            'Options' : '\uf142',
            'User' : '\uf007',
        }
        
        toolbar_item_icon_after_content_value = {
            'New' : '\uf0d7',
            'Filter' : '\uf0d7',
            'Impact Analysis' : '\uf0d7',
            'Manage' : '\uf0d7',
            'Options' : '\uf0d7',
            'User' : '\uf0d7',
            'Help' : '\uf0d7'    
        }
        visible_tool_bar_items_obj = [item_obj for item_obj in self.get_toolbar_items_object() if item_obj.is_displayed()]
        for toolbar_item in  visible_tool_bar_items_obj :
            visible_status = None
            toolbar_item_title = toolbar_item.get_attribute('qa')
            if toolbar_item_title in toolbar_item_icon_css :
                icon_css = "div.ibx-label-glyph.ibx-label-icon.{0}".format(toolbar_item_icon_css[toolbar_item_title])
                icon_obj = self._util.validate_and_get_webdriver_object(icon_css, '{0} option icon'.format(toolbar_item_title), toolbar_item)
                if toolbar_item_title in toolbar_item_icon_name :
                    icon_text = icon_obj.text.strip()
                    if icon_text == toolbar_item_icon_name[toolbar_item_title] :  
                        visible_status = True
                    else : 
                        continue
                else :
                    if icon_obj.text.strip() == '' :
                        visible_status = True 
                    else :
                        continue
                    
                if toolbar_item_title in toolbar_item_icon_before_content_value :
                    actual_icon_content = self._javascript.get_element_before_style_properties(icon_obj, 'content').replace('"', '').encode()
                    if actual_icon_content == toolbar_item_icon_before_content_value[toolbar_item_title].encode() :
                        visible_status = True
                    else :
                        continue
                    
                if toolbar_item_title in toolbar_item_icon_after_content_value : 
                    actual_icon_content = self._javascript.get_element_after_style_properties(icon_obj, 'content').replace('"', '').encode()
                    if actual_icon_content == toolbar_item_icon_after_content_value[toolbar_item_title].encode()   :
                        visible_status = True
                    else :
                        continue     
            else :
                error_msg = "{0} option css not implemented in get_visible_ribbon_bar_items_title() method".format(toolbar_item_title)
                raise NotImplementedError(error_msg)
            
            if visible_status ==  True :
                visible_toolbar_bar_items.append(toolbar_item_title)
                
        return visible_toolbar_bar_items