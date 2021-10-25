from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject

class Poptop_Dialog(BasePage):
    
    poptop_dialog_css='.pop-top'
    dialog_name = 'New Portal Dialog' 
    caption_css = ".ibx-title-bar-caption"
    #caption_css = Poptop_Dialog.poptop_dialog_css + ".ibx-title-bar-caption"
    row_css = "> .ibx-dialog-main-box .ibx-flexbox-horizontal"
    #row_css = Poptop_Dialog.poptop_dialog_css + "> .ibx-dialog-main-box .ibx-flexbox-horizontal"
    
    def __init__(self, driver):
        super(Poptop_Dialog, self).__init__(driver)
    
    def verify_poptop_dialog_is_visible(self, dialog_css, visible_mode, msg):
        '''
        '''
        poptop_dialog_css='{0} {1}'.format(Poptop_Dialog.poptop_dialog_css, dialog_css)
        utillobject.verify_object_visible(self, poptop_dialog_css, visible_mode, msg)
             
    def get_caption_title(self):
        caption_title_css='{0} {1}'.format(Poptop_Dialog.poptop_dialog_css, Poptop_Dialog.caption_css)
        caption_description='{0} Caption'.format(Poptop_Dialog.dialog_name) 
        caption_title_obj=utillobject.validate_and_get_webdriver_object(self, caption_title_css, caption_description)
        return caption_title_obj.text.strip()
     
    def get_row_elements(self):
        row_elements_css='{0} {1}'.format(Poptop_Dialog.poptop_dialog_css, Poptop_Dialog.row_css)
        row_elements_description='{0} rows'.format(Poptop_Dialog.dialog_name)
        row_element_objects=utillobject.validate_and_get_webdriver_objects(self, row_elements_css, row_elements_description)
        return row_element_objects
     
    def get_row_element_according_to_text_string(self, unique_text_string, text_find_type='in'):
        row_elements=Poptop_Dialog.get_row_elements(self)
        token=False
        for row_element in row_elements:
            if text_find_type.lower() == 'in' :
                if unique_text_string in row_element.text:
                    token=True
                    return row_element
            else : 
                if row_element.text.strip().startswith(unique_text_string) :
                    token=True
                    return row_element
        if token==False:
            error_msg="The requested resource [{0}] row is not available in the '{1}' poptop.".format(unique_text_string, Poptop_Dialog.dialog_name)
            raise LookupError(error_msg)
     
    def get_element_in_dialog(self, unique_row_text_string, element_css, element_type, text_find_type='in'):
        row_element=Poptop_Dialog.get_row_element_according_to_text_string(self, unique_row_text_string, text_find_type=text_find_type)
        element_description=element_type + ' in ' + Poptop_Dialog.dialog_name + ' ' + unique_row_text_string + ' row.'
        required_element=utillobject.validate_and_get_webdriver_object(self, element_css, element_description, parent_object=row_element)
        return required_element
    
    def close_poptop_dialog(self):
        pass
    
class New_Portal_Dialog(Poptop_Dialog):
    
    def __init(self):
        Poptop_Dialog.dialog_name = 'New Portal Dialog'
    
    
class Edit_Portal_Dialog(Poptop_Dialog):
    
    def __init(self):
        Poptop_Dialog.dialog_name = 'New Portal Dialog'

class Select_Popup(Poptop_Dialog):
    
    def __init(self):
        Poptop_Dialog.dialog_name = 'New Portal Dialog'
          
class Share_With_Others(Poptop_Dialog):
    
    def __init(self):
        Poptop_Dialog.dialog_name = 'New Portal Dialog'

    def verify_search_box_text_property(self):
        pass
    
    def get_searchbox_element(self):
        searchbox_default_string='search'
        searchbox_object=Poptop_Dialog.get_row_element_according_to_text_string(self, searchbox_default_string)
        return searchbox_object
    
    def get_searchbox_input_element(self):
        searchbox_row = self.get_searchbox_element()
        searchbox_element_css='div.share-with-txt-search > input'
        searchbox_element_description='Searchbox inside Share With Others popup'
        required_element=utillobject.validate_and_get_webdriver_object(self, searchbox_element_css, searchbox_element_description, parent_object=searchbox_row)
        return required_element
    
    def get_searchbox_menu_button(self):
        searchbox_default_string='search'
        searchbox_row=Poptop_Dialog.get_row_element_according_to_text_string(self, searchbox_default_string)
        searchbox_element_css="div.Share-with-menu-btn > div[class*='ds-icon-caret-down']"
        searchbox_element_description='Searchbox menu button inside Share With Others popup'
        required_element=utillobject.validate_and_get_webdriver_object(self, searchbox_element_css, searchbox_element_description, parent_object=searchbox_row)
        return required_element
    
    def get_dropdown_searched_items(self):
        dropdown_searched_items_css=Share_With_Others.poptop_dialog_css + ' .share-with-dropdown .share-with-item'
        print(dropdown_searched_items_css)
        dropdown_searched_items_description='dropdown searched items inside Share With Others popup'
        dropdown_searched_items=utillobject.validate_and_get_webdriver_objects(self, dropdown_searched_items_css, dropdown_searched_items_description)
        return dropdown_searched_items
        
    def get_dropdown_searched_item_according_to_text_string(self, unique_text_string):
        row_elements=Share_With_Others.get_dropdown_searched_items(self)
        token=False
        for row_element in row_elements:
            if unique_text_string in row_element.text:
                token=True
                return row_element
        if token==False:
            error_msg='The requested item [' + unique_text_string + '] row is not available in the dropdown searched items inside Share With Others popup.'
            raise LookupError(error_msg)
    
    def get_shared_with_items(self):
        shared_with_items_css=Share_With_Others.poptop_dialog_css + ' .share-with-container .share-with-item'
        shared_with_items_description='shared items inside Sharee with Container'
        shared_with_items=utillobject.validate_and_get_webdriver_object(self, shared_with_items_css, shared_with_items_description)
        return shared_with_items