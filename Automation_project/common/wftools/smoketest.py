from common.lib.base import BasePage
from common.pages.wf_smoketest import Wf_Smoketest as wf_smoketestobject

class Smoketest(BasePage):
    
    def double_click_on_dimension_field(self, field_name):
        """
        Descriptions : This method used to double_click_on_dimension_field  
        """
        wf_smoketestobject.double_click_dimension_field_in_metadata_tree(self, field_name=field_name)
    
    def double_click_on_datetree_item(self, field_name, field_position):
        '''
        Desc:- This function is used to double click and select the field from data tree.
        :usage double_click_on_datetree_item('Revenue', 1)
        '''
        wf_smoketestobject.select_datatree_field(self, field_name, 'double', field_position)
    
    def save_designer_chart_from_toolbar(self, title_to_save, wait_time=3):
        """
        Descriptions : This method used to save_designer_chart_from_toolbar 
        """
        wf_smoketestobject.save_chart_from_toolbar(self, title_to_save=title_to_save, wait_time=wait_time)
    
    def save_ro_from_toolbar(self, file_name):
        """
        Descriptions : This method used to save_ro_from_toolbar 
        """
        wf_smoketestobject.select_top_toolbar_item(self, item_name='toptoolbar_save')
        wf_smoketestobject.ibfs_save_as(self, file_name, file_type=None)
        
    def select_item_in_top_toolbar(self, top_toolbar_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        '''
        wf_smoketestobject.select_ia_top_toolbar_item(self, top_toolbar_item_name)
        
    def save_file_in_save_dialog(self, file_name, file_type=None,**kwargs):
        '''
        Desc:-This function is used to save file in the save dialog
        '''
        wf_smoketestobject.ibfs_save_as(self, file_name, file_type,**kwargs)
        
    
