from common.lib.base import BasePage
from common.pages.security_center import Security_Center as securitycenter_object
from common.pages.security_center import Rules_For_This_Group_Dialog as security_rules_object


class Security_Center(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    
    """ CSS can be given at global level which can be used for the below defined functions """
    
    def __init__(self, driver):
        super(Security_Center, self).__init__(driver)
        
    def left_click_on_group(self, group_path, select_type='left'):
        """ 
        This function is used to left click on any group
        left_click_on_group('Retail_Samples')
        """
        securitycenter_object.select_group_role_(self, group_path, select_type=select_type)
        
    def right_click_on_group(self, group_path, select_type='right'):
        """
        This function is used to right click on any group
        right_click_on_group('Retail_Samples->GroupAdmins')
        """
        securitycenter_object.select_group_role_(self, group_path, select_type)
    
    def select_group_context_menu(self, context_menu_path):
        """
        This function is used to select group context menu by right click on any group and select item in the popup.
        select_group_context_menu('Security->Rules for this Groups')
        """
        securitycenter_object.select_group_context_menu(self, context_menu_path)
        
    def expand_group_section_(self, group_path):
        """
        This function is used to expand group.
        expand_group_section('P292->P292_S10032_G157381')
        """
        securitycenter_object.expand_group_section_(self, group_path)
        
    def verify_caption_in_rules_for_this_group_dialog(self, expected_title, msg):
        """
        This function is used to verify caption of the rules for this group dialog
        verify_caption_in_rules_for_this_group_dialog('Rules for this Group - GroupAdmins', "Step X: Verify)
        """
        security_rules_object.verify_caption(self, expected_title, msg)
        
    def create_grid_data_in_rules_for_this_group_dialog(self, file_name):
        """
        This function is used to verify grid data in the rules for this grroup dialog
        verify_grid_data_in_rules_for_this_group_dialog("Test1.xlsx")
        """
        security_rules_object.create_grid_data(self, file_name)
        
    def click_close_button_in_rules_for_this_resource_dialog(self, button_name='close'):
        """
        This function is used to click close_button which is present in the group rules dialog
        click_close_button_in_rules_for_this_resource_dialog()
        """
        security_rules_object.select_buttons(self, button_name)
        
    def click_help_button_in_rules_for_this_group_dialog(self, button_name='help'):
        """
        This function is used to click help button which is present in the group rules dialog
        click_help_button_in_rules_for_this_group_dialog()
        """
        security_rules_object.select_buttons(self, button_name)
        
    def click_create_report_button_in_rules_for_this_group_dialog(self, button_name='create_report'):
        """
        This function is used to click create_report button which is present in the group rules dialog
        click_create_report_button_in_rules_for_this_group_dialog ()
        """
        security_rules_object.select_buttons(self, button_name)
        
    def get_list_of_groups(self):
        '''
        This function will return list of avilable groups in groups section in security centre
        '''
        securitycenter_object.get_group_table_row_elements(self)
        
    def get_group_name_from_the_parent_group(self, group_name):
        '''
        This function will return list of avilable groups in groups section in security centre
        '''
        securitycenter_object.get_group_table_row_element(self, group_name)
        
        
       
    
        
        
        
        
        
        
        
        
        