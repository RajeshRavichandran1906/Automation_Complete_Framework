from common.lib.utillity import UtillityMethods as util_method
from common.lib.base import BasePage
from common.pages import wf_mainpage
from common.lib.webfocus.resource_dialog import ResourceDialog
from common.locators.wf_mainpage_locators import WfMainPageLocators

class Wf_Mainpage(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Wf_Mainpage, self).__init__(driver)
    
    def click_on_banner_logo(self):
        """
        This function will click on top banner of logo in main home page
        """
        wf_mainpage.Wf_Mainpage.click_on_banner_logo(self)
        
    def select_username_dropdown_menu(self, navigate_path=None):
        '''
        Desc: This will select the menu or submenu items from username dropdown.
        usage: wfmain_obj.select_username_dropdown_menu(navigate_path='Administration->Security Center')
        '''
        wf_mainpage.Wf_Mainpage.select_username_dropdown_menu(self, navigate_path)
        
    def verify_username_dropdown_menu(self, expected_menu_item_list, navigate_path=None, msg='Step X: Verify username dropdown menu', comparision_type='asequal'):
        '''
        Desc: This will verify the menu or submenu items from username dropdown
        usage: verify_username_dropdown_menu(['Administration','Tools','Preferences','Help','Legacy Home Page','Change Password','Sign Out'], "Step:X")
        '''
        wf_mainpage.Wf_Mainpage.verify_username_dropdown_menu(self, expected_menu_item_list, navigate_path, msg, comparision_type=comparision_type)
    
    def signout_from_username_dropdown_menu(self):
        '''
        Desc: This will select Signout from username dropdown.
        usage: wfmain_obj.signout_from_username_dropdown_menu()
        '''
        wf_mainpage.Wf_Mainpage.select_username_dropdown_menu(self, 'Sign Out')
        
    def create_new_folder(self, folder_name):
        '''
        This function will create a new folder based on the provided folder name
        create_new_folder('Test Folder')
        '''
        wf_mainpage.Wf_Mainpage.create_new_folder(self,folder_name)
        
    def verify_new_folder_caption_title(self, step_number='X'):
        '''
        This function will verify caption of New Folder dialog
        verify_new_folder_caption_title()
        '''
        wf_mainpage.Wf_Mainpage.verify_new_folder(self, step_number=step_number)
        
    def verify_new_folder_title_value(self, title_value, step_number):
        '''
        This function will verify Title of New Folder dialog
        verify_new_folder_title_value('test', '9')
        '''
        wf_mainpage.Wf_Mainpage.verify_new_folder(self, tile_value=title_value, step_number=step_number)
    
    def verify_new_folder_Name_value(self, name_value, step_number):
        '''
        This function will verify Name of New Folder dialog
        verify_new_folder_Name_value('test', '9')
        '''
        wf_mainpage.Wf_Mainpage.verify_new_folder(self, name_value=name_value, step_number=step_number)
           
    def change_password(self, old_pass, new_pass, button='ok'):
        '''
        Desc: This function will change password in new homepage
        :usage change_password('', 'new')
        '''
        wf_mainpage.Wf_Mainpage.change_password(self, old_pass, new_pass, button=button)
        
    def signin_from_username_dropdown_menu(self):
        '''
        Desc: This will select Signin from username dropdown.
        usage: wfmain_obj.signin_from_username_dropdown_menu()
        '''
        wf_mainpage.Wf_Mainpage.select_username_dropdown_menu(self, 'Sign In')
        username_css = 'input[id=SignonUserName]'
        util_method.synchronize_with_number_of_element(self, username_css, 1, 60)
        util_method.verify_object_visible(self, username_css, True, "StepX: Verify user name object visible in SignIn Page")
        
    def verify_left_panel(self, content_list, msg, default_selected='Content', comparision_type='asequal'):
        '''
        Desc: This function will verify left panel options and its selected option
        usage: wfmain_obj.verify_left_panel(['Content','Portals'], )
        '''
        wf_mainpage.Wf_Mainpage.verify_left_panel(self, content_list, msg, active=default_selected, comparision_type=comparision_type)
        
    def verify_folder_item_grid_view(self, item1, item2, msg, item_type='folder-item', grid_folder_distance=20):
        '''
        Desc: This function will verify the grid view by  verifying
        1. grid class visibility 
        2. list class invisibility
        3. y position of item1 top right and item2 top left is equal
        4. x position of item1 top right and item2 top left difference in the range of (20,22)
        :arg grid_folder_distance=20 expected distance between folder1 and folder2
        usage: wfmain_obj.verify_folder_item_grid_view("My Content", "Charts", "Step02: verify grid view")
        '''
        wf_mainpage.Wf_Mainpage.verify_grid_view(self, item1, item2, msg, item_type=item_type, grid_folder_distance=grid_folder_distance)
        
    def verify_file_item_grid_view(self, item1, item2, msg, item_type='file-item', grid_folder_distance=20):
        '''
        Desc: This function will verify the grid view by  verifying
        1. grid class visibility 
        2. list class invisibility
        3. y position of item1 top right and item2 top left is equal
        4. x position of item1 top right and item2 top left difference in the range of (20,22)
        :arg grid_folder_distance=20 expected distance between item1 and item2 files
        usage:  wfmain_obj.verify_file_item_grid_view("V3 portal", "V4 Portal", "Step06.1a: Verify content area shows in grid view")
        '''
        wf_mainpage.Wf_Mainpage.verify_grid_view(self, item1, item2, msg, item_type=item_type, grid_folder_distance=grid_folder_distance)
        
    def verify_list_view(self, item1, item2, msg):
        '''
        This function will verify the list view by  verifying
        1. list class visibility 
        2. grid class invisibility
        3. Last modified in view title
        4. x position of item1 bottom middle and item2 top middle is equal
        :usage verify_list_view("My Content", "Charts", "Step02: verify list view")
        '''
        wf_mainpage.Wf_Mainpage.verify_list_view(self, item1, item2, msg)
    
    def select_list_view(self):
        '''
        Desc: This function will select list view image
        usage: select_list_view()
        '''
        wf_mainpage.Wf_Mainpage.select_toolbar_button(self,'list')
        
    def select_grid_view(self):
        '''
        Desc: This function will select grid view image
        usage: select_list_view()
        '''
        wf_mainpage.Wf_Mainpage.select_toolbar_button(self,'grid')
    
    def select_choose_columns_in_list_view(self):
        '''
        Desc: This function will select 'choose columns' in list view
        usage: select_choose_columns()
        '''
        wf_mainpage.Wf_Mainpage.select_choose_columns(self)
    
    def select_list_view_columns(self, columns_name_list):
        """
        This function will select options in list view columns 
        :usage select_list_view_columns(['Name', 'Size'])
        """
        wf_mainpage.Wf_Mainpage.select_list_view_columns(self, columns_name_list)
        
    def verify_choose_columns_context_menu_items(self, expected_context_menu_item_list, msg, comparision_type='asequal'):
        '''
        Desc: This function will verify only the context menu list. So before calling this function make sure the context menu is visible.
        usage: verify_choose_columns_context_menu_items(['Title','Name','Summary','Last Modified','Created On','Size','Owner','Published','Shown'],"Step02: Verify")
        '''
        popup_css = "div.ibx-popup.pop-top"
        util_method.synchronize_with_number_of_element(self, popup_css, 1, expire_time=30)
        wf_mainpage.Wf_Mainpage.verify_context_menu_item(self, expected_context_menu_item_list, msg, comparision_type=comparision_type)
        
    def select_content_from_sidebar(self):
        '''
        Desc: This function will select Content from left panel option from main home page.
        usage: select_content_from_sidebar()
        '''
        util_method.synchronize_with_number_of_element(self, WfMainPageLocators.CONTENT_ICON_CSS, 1, 120)
        wf_mainpage.Wf_Mainpage.select_left_panel(self, 'content')
        
    def select_portals_from_sidebar(self):
        '''
        Desc: This function will select Portals from left panel option from main home page.
        usage: select_portals_from_sidebar()
        '''
        util_method.synchronize_with_number_of_element(self, WfMainPageLocators.PORTAL_ICON_CSS, 1, 30)
        wf_mainpage.Wf_Mainpage.select_left_panel(self, 'portals')
    
    def select_favorites_from_sidebar(self):
        '''
        Desc: This function will select Favorites from left panel option from main home page.
        usage: select_favorites_from_sidebar()
        '''
        util_method.synchronize_with_number_of_element(self, WfMainPageLocators.FAVORITE_ICON_CSS, 1, 30)
        wf_mainpage.Wf_Mainpage.select_left_panel(self, 'favorites')
        
    def select_mobilefavorites_from_sidebar(self):
        '''
        Desc: This function will select Mobile Favorites from left panel option from main home page.
        usage: select_mobilefavorites_from_sidebar()
        '''
        wf_mainpage.Wf_Mainpage.select_left_panel(self, 'mobilefavorites')
    
    def select_ask_webfocus_from_sidebar(self):
        '''
        Desc: This function will select Mobile Favorites from left panel option from main home page.
        usage: select_ask_webfocus_from_sidebar()
        '''
        wf_mainpage.Wf_Mainpage.select_left_panel(self, 'askwebfocus')
    
    def select_button_in_portal_content_area(self, option):
        '''
        Desc: This function will select button in portal content area
        usage: select_button_in_portal_content_area('Retail Samples')
        '''
        wf_mainpage.Wf_Mainpage.select_button_in_portal_content_area(self, option)
    
    def verify_favorites_tags(self, expected_tag_list, step_num, comparision_type='asequal'):
        '''
        Desc: This function will verify tags under Favorites.
        usage: verify_favorites_tags(['Retail Samples'], '9')
        '''
        wf_mainpage.Wf_Mainpage.verify_tags(self, expected_tag_list, step_num, comparision_type=comparision_type)
        
    def ask_webfocus_search_bar_options(self, verify_option, display_status, msg):
        '''
        This function to used in side Ask webfocus page.
        Usage: ask_webfocus_search_bar_options('text_box', True, "Step02: Verify text box")
        '''
        wf_mainpage.Wf_Mainpage.ask_webfocus_search_bar_options(self, verify_option, display_status, msg)
    
    def ask_webfocus_content_area(self, verify_option, expected_text, msg):
        '''
        This function to used in side Ask webfocus page.
        verify_option : title or title_button_state or title_button_text
        ask_webfocus_content_area('title', 'Last Viewed Questions', 'Step02: Verify title')
        '''  
        wf_mainpage.Wf_Mainpage.ask_webfocus_content_area(self, verify_option, expected_text, msg)
    
    def click_repository_folder(self, folder_path):
        '''
        Desc: This function will left click on repository folder
        usage: click_repository_folder('Retail Samples')
        '''
        wf_mainpage.Wf_Mainpage.left_click_repository_folder(self, folder_path)
        
    def double_click_on_content_area_items(self,item_name,folder_path=None, item_name_index=1):
        '''
        Desc: This function is used to double click a content items(fexes)in content area
        Example usage: double_click_on_content_area_items('Retail Samples')
        @param item_name_index = Need to be integer value ,if two items having same name.
        '''
        wf_mainpage.Wf_Mainpage.double_click_on_content_area_items(self, item_name, folder_path, item_name_index)
    
    def right_click_folder_item_and_select_menu(self, item_name, context_menu_item_path=None, folder_path=None, click_option='right_click', item_name_index=1):
        '''
        Desc: This function will expand folder path, right on folder item and select menu
        usage: right_click_folder_item_and_select_menu("Margin by Product Category", 'Add to Favorites', 'Retail Samples->Reports')
        '''
        wf_mainpage.Wf_Mainpage.select_repository_folder_item_context_menu(self, item_name, context_menu_item_path, folder_path, click_option, item_name_index=item_name_index)
        
    def double_click_folder_item_and_select_menu(self, item_name, context_menu_item_path=None, folder_path=None, click_option='double_click', item_name_index=1):
        '''
        Desc: This function will expand folder path, right on folder item and select menu
        usage: right_click_folder_item_and_select_menu("Margin by Product Category", 'Add to Favorites', 'Retail Samples->Reports')
        '''
        wf_mainpage.Wf_Mainpage.select_repository_folder_item_context_menu(self, item_name, context_menu_item_path, folder_path, click_option, item_name_index=item_name_index)
        
    def verify_favorites_notify_popup(self, step_no):
        '''
        Desc: This function will verify Favorites added notify popup text, background transparency and background color
        usage: verify_favorites_notify_popup("Step21")
        '''
        util_method.verify_notify_popup(self, notify_text="Favorite added", msg=step_no)
        
    def verify_mobile_favorites_notify_popup(self, step_no):
        '''
        Desc: This function will verify Mobile Favorites added notify popup text, background transparency and background color
        usage: verify_mobile_favorites_notify_popup("Step21")
        '''
        util_method.verify_notify_popup(self, notify_text="Mobile Favorite added", msg=step_no)
        
    def collapse_side_bar(self):
        '''
        Desc: This function will collapse side menu bar
        usage: collapse_side_bar()
        '''
        wf_mainpage.Wf_Mainpage.colapse_sidebar(self, 'left')
        
    def expand_side_bar(self):
        '''
        Desc: This function will show side menu bar
        usage: expand_side_bar()
        '''
        wf_mainpage.Wf_Mainpage.colapse_sidebar(self, 'right')
        
    def verify_items_in_grid_view(self, expected_list, comparision_type, msg):
        '''
        Usgae: verify_items_in_grid_view(expected_portals, 'asListEqual', "Step06.2b: Verify Retail Samples and V3 portals listed in portal grid view")
        '''
        wf_mainpage.Wf_Mainpage.verify_items_in_views(self, expected_list, comparision_type, msg, view_type='grid_view')
        
    def verify_items_in_list_view(self, expected_list, comparision_type, msg):
        '''
        Usgae: verify_items_in_list_view(expected_portals, 'asListEqual', "Step06.2b: Verify Retail Samples and V3 portals listed in portal list view")
        '''
        wf_mainpage.Wf_Mainpage.verify_items_in_views(self, expected_list, comparision_type, msg, view_type='list_view')
    
    def verify_folders_in_grid_view(self, expected_list, comparision_type, msg):
        '''
        Usgae: verify_folders_in_grid_view(expected_folders, 'asListEqual', "Step06.2b: Verify Retail Samples and V3 portals listed in portal list view")
        '''
        wf_mainpage.Wf_Mainpage.verify_folder_in_views(self, expected_list, comparision_type, msg, view_type='grid_view')
    
    def verify_folders_in_list_view(self, expected_list, comparision_type, msg):
        '''
        Usgae: verify_folders_in_list_view(expected_folders, 'asListEqual', "Step06.2b: Verify Retail Samples and V3 portals listed in portal list view")
        '''
        wf_mainpage.Wf_Mainpage.verify_folder_in_views(self, expected_list, comparision_type, msg, view_type='list_view')
    
    def verify_repository_folder_item_context_menu(self, item_name, expected_context_menu_item_list, folder_path=None, msg='Step X', comparision_type='asequal', item_name_index=1):                                                            
        """
        :Usage verify_repository_folder_item_context_menu('Report1.fex', ['Run'], folder_path='P116->G132647', msg="Step 9")
        """
        wf_mainpage.Wf_Mainpage.verify_repository_folder_item_context_menu(self, item_name, expected_context_menu_item_list, folder_path=folder_path, msg=msg, comparision_type=comparision_type, item_name_index=item_name_index)
    
    def search_input_box_options(self, option_type ='write', input_text_msg=None, verify_value=None, msg=None):
        '''
        @Param: option_type: 'write' or 'clear'
        '''   
        wf_mainpage.Wf_Mainpage.search_input_box_options(self, option_type=option_type, input_text_msg=input_text_msg, verify_value=verify_value, msg=msg)
    
    def verify_repository_folder_item_context_submenu(self, item_name, contex_sub_menu_item_path, expected_context_menu_item_list, folder_path=None, msg='Step X', comparision_type='asequal', item_name_index=1, close_context_menu_css=None, expire_time=90):
        """
        :Usage verify_content_area_folder_context_menu('Portal for Context Menu Testing', ['Run'], folder_path='P116->G132647', msg="Step 9")
        """
        wf_mainpage.Wf_Mainpage.verify_repository_folder_item_context_submenu(self, item_name, contex_sub_menu_item_path, expected_context_menu_item_list, folder_path=folder_path, msg=msg, comparision_type=comparision_type, item_name_index=item_name_index, close_context_menu_css=close_context_menu_css, expire_time=expire_time)
        
    def verify_list_view_title_labels(self, expected_list, msg):
        '''
        @Param: expected_portals_list_view_titles = ['arrow_upward\nTitle', 'Summary', 'Last modified']
        Usage: verify_view_title_labels([], "Step05: Verify title")
        '''
        wf_mainpage.Wf_Mainpage.verify_view_title_labels(self, expected_list, msg, view_type='list_view')
        
    def verify_grid_view_title_labels(self, expected_list, msg, label_type='files'):
        '''
        @Param: expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        @param: label_type: 'files' or 'folders'
        Usage: verify_grid_view_title_labels([], "Step05: Verify title")
        '''
        wf_mainpage.Wf_Mainpage.verify_view_title_labels(self, expected_list, msg, view_type='grid_view', label_type=label_type)
    
    def verify_crumb_box(self, expected_crumb_box_text, msg):
        '''
        @Param: expected_crumb_box_text = 'Domains->P292_S10660->G193250->Portals->V4 Portals'
        @param: msg: 'Step 9'
        Usage: verify_crumb_box('Domains->P292_S10660->G193250->Portals->V4 Portals', 'Step 9')
        '''
        wf_mainpage.Wf_Mainpage.verify_crumb_box(self, expected_crumb_box_text, msg=msg)
        
    def expand_resource_tree(self):
        '''
        :Usage expand_resource_tree()
        '''
        wf_mainpage.Wf_Mainpage.expand_collapse_resource_tree(self, 'expand')
    
    def collapse_resource_tree(self):
        '''
        :Usage collapse_resource_tree()
        '''
        wf_mainpage.Wf_Mainpage.expand_collapse_resource_tree(self, 'collapse')
        
    def verify_expand_resource_tree(self, status, msg):
        '''
        @param status: True or False
        @param msg:"step 9: verify" 
        :Usage verify_expand_resource_tree(True, "step 9: verify" )
        '''
        wf_mainpage.Wf_Mainpage.verify_expand_collapse_resource_tree(self, 'expand', status, msg)
    
    def verify_collapse_resource_tree(self, status, msg):
        '''
        @param status: True or False
        @param msg:"step 9: verify" 
        :Usage verify_collapse_resource_tree(True, "step 9: verify" )
        '''
        wf_mainpage.Wf_Mainpage.verify_expand_collapse_resource_tree(self, 'collapse', status, msg)
        
    def select_option_from_crumb_box(self, crumb_box_ribbon_option_name):
        '''
        @param crumb_box_ribbon_option_name: 'Domains'
        :Usage select_option_from_crumb_box('Domains')
        '''
        wf_mainpage.Wf_Mainpage.select_option_from_crumb_box(self, crumb_box_ribbon_option_name)
    
    def verify_options_form_right_arrow_in_crumb_box(self, crumb_box_option_name, expected_option_list, step_number, comparision_type='asequal'):
        '''
        This will verify pop_up option after click on right arrow in crumb box.
        
        @param crumb_box_option_name: 'Domains'
        @param expected_option_list: ['My Content', 'Reports', 'Charts']
        @param step_number: '9'
        @param comparision_type: 'asequal' or 'asnotin' or 'asin'
        :Usage  verify_options_form_right_arrow_in_crumb_box('Domains', ['My Content', 'Reports', 'Charts'], '9', comparision_type='asin')
        '''
        wf_mainpage.Wf_Mainpage.select_right_arrow_in_crumb_box(self, crumb_box_option_name)
        step_number = 'Step {0}'.format(step_number)
        wf_mainpage.Wf_Mainpage.verify_context_menu_item(self, expected_option_list, msg=step_number, comparision_type=comparision_type)
        
    def select_options_form_right_arrow_in_crumb_box(self, crumb_box_option_name,  right_arrow_popup_option_path):
        '''
        This will verify pop_up option after click on right arrow in crumb box.
        
        @param crumb_box_option_name: 'Domains'
        @param expected_option_list: ['My Content', 'Reports', 'Charts']
        @param step_number: '9'
        @param comparision_type: 'asequal' or 'asnotin' or 'asin'
        :Usage  verify_options_form_right_arrow_in_crumb_box('Domains', ['My Content', 'Reports', 'Charts'], '9', comparision_type='asin')
        '''
        wf_mainpage.Wf_Mainpage.select_right_arrow_in_crumb_box(self, crumb_box_option_name)
        wf_mainpage.Wf_Mainpage.select_context_menu_item(self, right_arrow_popup_option_path)
    
    def verify_repository_folder_icon_plus_minus(self, folder_name, option_name, msg, index=0):
        """
        Descriptions : This method used to verify home page domains folder expand or collapse icon (+/-)
        example usage : verify_repository_folder_icon_plus_minus('Retail Samples', 'expand', 'Step 9: verify', index=1)
        """
        wf_mainpage.Wf_Mainpage.verify_repository_folder_icon_plus_minus(self, folder_name, option_name, msg, index=index)
               
    def expand_repository_folders_and_verify(self, folder_path, folder_name_list, msg, expire_time=90, comparion_type='asin'):
        '''
        :Usage expand_repository_folders_and_verify('P242_S10674_G171304->My Content', ['autodevuser56'], 'Step 9: verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_repository_folders(self, folder_path, folder_name_list, msg, expire_time=expire_time, verification_state='expand', comparion_type=comparion_type)
    
    def collapse_repository_folders_and_verify(self, folder_name, folder_name_list, msg, expire_time=90, comparion_type='asin'):
        '''
        :Usage collapse_repository_folders_and_verify('P242_S10674_G171304', ['autodevuser56'], 'Step 9: verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_repository_folders(self, folder_name, folder_name_list, msg, expire_time=expire_time, verification_state='collapse', comparion_type=comparion_type)
    
    def verify_main_node_under_repository_folders(self, folder_name, folder_name_list, msg, expire_time=90, comparion_type='asequal'):
        '''
        :Usage verify_main_node_under_repository_folders('P242_S10674_G171304', ['autodevuser56'], 'Step 9: verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_main_node_under_repository_folders(self, folder_name, folder_name_list, msg, expire_time=expire_time, comparion_type=comparion_type)
    
    def expand_repository_folder(self, folder_name_path, index=0):
        '''
        This will expand the repository folder.
        
        @param folder_name_path: Domain->P292_S10660->G169261
        :Usage expand_repository_folder('Domain->P292_S10660->G169261')
        '''
        wf_mainpage.Wf_Mainpage.expand_repository_folders(self, folder_name_path, index=index)
    
    def collapse_repository_folder(self, folder_name):
        '''
        This will collapse the repository folder.
        
        @param folder_name:  'P292_S10660'
        :Usage collapse_repository_folders('P292_S10660')
        '''
        wf_mainpage.Wf_Mainpage.collapse_repository_folders(self, folder_name)
        
    def verify_repository_folder_context_menu(self, folder_path, expected_context_menu_item_list, expire_time=90, msg='Step X', comparision_type='asequal', verification_state='expand'):
        '''
        @param comparision_type:'asequal' or 'asnotin' or 'asin'
        @param verification_state:'expand' or 'collpase'  
        :Usage verify_repository_folder_context_menu('P242_S10674_G171304', ['Edit'], msg='Step 9', comparision_type='asin', verification_state='collapse')
        '''
        wf_mainpage.Wf_Mainpage.verify_repository_folder_context_menu(self, folder_path, expected_context_menu_item_list, expire_time=expire_time, msg=msg, comparision_type=comparision_type, verification_state=verification_state)
    
    def verify_repository_folder_context_submenu(self, folder_path, contex_sub_menu_item_path, expected_context_menu_item_list, msg='Step X', comparision_type='asequal', verification_state='expand', close_context_menu_css=None, expire_time=90):
        '''
        @param comparision_type:'asequal' or 'asnotin' or 'asin'
        @param verification_state:'expand' or 'collpase'  
        :Usage verify_repository_folder_context_submenu('P242_S10674_G171304', 'Run', ['Edit'], msg='Step 9', comparision_type='asin', verification_state='collapse', close_context_menu_css='.banner-group-spacer', expire_time=90)
        '''
        wf_mainpage.Wf_Mainpage.verify_repository_folder_context_submenu(self, folder_path, contex_sub_menu_item_path, expected_context_menu_item_list, msg, comparision_type, verification_state, close_context_menu_css=close_context_menu_css, expire_time=expire_time)
        
    def select_repository_folder_context_menu(self, folder_path, menu_item_path, expire_time=90, click_option='right_click', verification_state='expand'):
        '''
        @param verification_state:'expand' or 'collpase'  
        :Usage select_repository_folder_context_menu('P242_S10674_G171304', 'Edit->Run', msg='Step 9', verification_state='collapse')
        '''
        wf_mainpage.Wf_Mainpage.select_repository_folder_context_menu(self, folder_path, menu_item_path, expire_time=expire_time, click_option=click_option, verification_state=verification_state)
        
    def select_repository_folder_item_context_submenu(self,folder_path,menu_item_path,verification_state='expand',expire_time=90):
        '''
        Desc: function is used to verify the context sub_menu
        @param verification_state:'expand' or 'collpase'  
        :Usage select_repository_folder_context_menu_submenu('P242_S10674_G171304', 'Edit->Run with->Run in new window', msg='Step 9', verification_state='collapse')
        '''
        wf_mainpage.Wf_Mainpage.select_repository_folder_context_submenu(self,folder_path,menu_item_path,verification_state=verification_state,expire_time=expire_time)
    
    def select_property_tab_value(self, property_value):
        '''
        This function will check the list of property tab values.
        @param property_value: 'General' 
        :usage select_property_tab_value('Advanced')
        '''
        wf_mainpage.Wf_Mainpage.select_property_tab_value(self, property_value)
    
    def verify_label_in_property_dialog(self, tab_name, label_name, step_number, checkbox=None):
        '''
        This function will verify property dialog label.
        
        @param  tab_name: 'Advanced'
        @param label_name: 'Title'
        @param step_number: '9'
        @param checkbox: 'enable' or 'disable'   #Optional
        @Usage verify_lable_in_property_dialog('Advanced', 'Title', '9', checkbox='enable')
        '''
        wf_mainpage.Wf_Mainpage.verify_label_in_property_dialog(self, tab_name, label_name, step_number, checkbox=checkbox)
    
    def select_property_dialog_save_cancel_button(self, button_name):
        """
        This function click save or cancel button in property dialog.
        @param button_name: 'Save' or 'Cancle'
        :Usage select_property_dialog_save_cancel_button('Save')
        """
        wf_mainpage.Wf_Mainpage.select_property_dialog_save_cancel_button(self, button_name)
    
    def close_property_dialog(self):
        '''
        This function will close property dialog.
        :usage close_property_dialog()
        ''' 
        wf_mainpage.Wf_Mainpage.close_property_dialog(self)
    
    def edit_property_dialog_value(self, property_name, property_type, property_value, typing_speed=0.5, tab_name='General'):
        '''
        This function is used to edit property window.
        
        @param property_name: 'Title'
        @param property_type: 'text_value'
        @param property_value: 'Faves'
        @param typing_speed: 1
        @param tab_name: 'Advanced'
        :usage edit_property_dialog_value('Title', 'text_value', 'Faves', typing_speed=1, tab_name='Advanced')
        '''
        wf_mainpage.Wf_Mainpage.edit_property_dialog_value(self, property_name, property_type, property_value, typing_speed=typing_speed, tab_name=tab_name)
    
    def verify_property_dialog_value(self, property_name, property_type, property_value, msg, user_name=None, tab_name='General'):
        '''
        This function is used to verify property window.
        
        @param property_name: 'Title'
        @param property_type: 'text_value'
        @param property_value: 'Faves'
        @param msg: 'Step 9: Verify property window.'
        @param user_name: 'autodevuser19'
        @param tab_name: 'Advanced'
        :usage edit_property_dialog_value('Title', 'text_value', 'Faves','Step 9: Verify property window.', user_name='autodevuser19, tab_name='Advanced')
        '''
        wf_mainpage.Wf_Mainpage.verify_property_dialog_value(self, property_name, property_type, msg, property_value=property_value, user_name=user_name, tab_name=tab_name)
        
    def verify_selected_tab_in_property_dialog(self, tab_name, msg):
        '''
        This function will verify selected tab label in property dialog.
        :Usage verify_selected_tab_in_property_dialog('General', "Step 9: verify")
        '''
        wf_mainpage.Wf_Mainpage.verify_selected_tab_in_property_dialog(self, tab_name, msg)
    
    def verify_property_dialog_tab_list(self, expected_list, msg):
        '''
        This function will check the list of property dialog tab label.
        :Usage verify_property_tab_value(['General', 'Advanced'], "Step 9: verify")
        '''
        wf_mainpage.Wf_Mainpage.verify_property_tab_value(self, expected_list, msg)
        
    def verify_created_modified_accessed_time_stamp_format(self, time_stamp_label, user_name, msg):
        '''
        This will verify created, modified, accessed time stamp format.
        @param time_stamp_label: 'Created'
        @param user_name: 'admin'
        @param msg: 'Step 9: Verify'
        :usage verify_created_modified_accessed_time_stamp_format('Created', 'admin', 'Step 9: Verify')
        '''
        expected_time_stamp_label_value = wf_mainpage.Wf_Mainpage.get_property_created_modified_accessed_time(self, time_stamp_label, msg, tab_name='General')
        wf_mainpage.Wf_Mainpage.verify_created_modified_accessed_time_formate(self, expected_time_stamp_label_value, user_name, msg)
        
    def verify_hidden_repository_folder(self, hidden_folder_name, msg, index_number=0):
        '''
        This function will verify repository folder is hidden using it's opacity value.
        @param hidden_folder_name: 'P116'
        @param folder_path: 'P116->S10229'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_hidden_repository_folder('P116', 'P116->S10229', 'Step 9: Verify', index=0)
        '''
        wf_mainpage.Wf_Mainpage.verify_hidden_repository_folder(self, hidden_folder_name, msg, index=index_number)
    
    def verify_property_dialog_save_cancel_button_enable_disable(self, button_name, button_status, msg):
        '''
        This function is verify save or cancel button is enable or disable in property dialog.
        :Usage verify_save_cancel_button_enable_disable('Save', 'enable', "Step 9: Verify")
        '''
        wf_mainpage.Wf_Mainpage.verify_property_dialog_save_cancel_button_enable_disable(self, button_name, button_status, msg)
    
    def verify_property_dialog_enable_disable(self, property_name, property_type, property_value, msg, tab_name='General'):
        '''
        This function is used to check verify property window.
        :usage verify_property_dialog_enable_disable('Title', 'text_value', 'P242', "step 9: Verify", tab_name='General')
        '''
        wf_mainpage.Wf_Mainpage.verify_property_dialog_enable_disable(self, property_name, property_type, property_value, msg, tab_name=tab_name)
    
    def verify_repository_folder_publish_or_unpublish(self, folder_name, folder_status, msg, index=0):
        '''
        This function will verify repository folder is publish or unpublish.
        @param folder_name: 'P116'
        @param folder_status: 'publish'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_repository_folder_publish_or_unpublish('P116', 'publish', 'Step 9: Verify', index=0)
        '''
        wf_mainpage.Wf_Mainpage.verify_repository_folder_publish_or_unpublish(self, folder_name, folder_status, msg, index=index)
    
    def verify_repository_folder_font_style(self, folder_name, font_name, msg, index=0):
        '''
        This function will verify repository folder font style.
        @param folder_name: 'P116'
        @param font_name: 'italic'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_repository_folder_font_style('P116', 'italic', 'Step 9: Verify', index=0)
        '''
        wf_mainpage.Wf_Mainpage.verify_repository_folder_font_style(self, folder_name, font_name, msg, index=index)
    
    def close_view_dialog(self, title_name):
        '''
        This function will close view dialog.
        @param title_name: 'Gray'
        :Usage  close_view_dialog('Gray')
        '''
        wf_mainpage.Wf_Mainpage.close_or_open_view_dialog(self, title_name, 'Close')
    
    def open_view_dialog_in_new_window(self, title_name):
        '''
        This function will open view dialog in new window.
        @param title_name: 'Gray'
        :Usage  open_view_dialog_in_new_window('Gray')
        '''
        wf_mainpage.Wf_Mainpage.close_or_open_view_dialog(self, title_name, 'Open in new window')
    
    def verify_folder_icon_in_content_area(self, folder_name, icon_type, step_number, verify_color_name=None, item_name_index=1):
        '''
        This will verify folder icon inside content area.
        @param folder_name: 'V5 portal'
        @param icon_type: 'portal'
        @param step_number: '9'
        @param verify_color_name: 'blue'
        @param item_name_index: 1
        :Usage  verify_icon_type_in_content_area('V5 portal', 'portal', '9', verify_color_name='blue', item_name_index=1)
        '''
        wf_mainpage.Wf_Mainpage.verify_icon_type_in_content_area(self, folder_name, icon_type, step_number, verify_color_name=verify_color_name, item_name_index=item_name_index)
    
    def verify_item_icon_in_content_area(self, item_name, icon_type, step_number, verify_color_name=None, item_name_index=1):
        '''
        This will verify item icon inside content area.
        @param item_name: 'V5 portal'
        @param icon_type: 'portal'
        @param step_number: '9'
        @param verify_color_name: 'blue'
        @param item_name_index: 1
        :Usage  verify_icon_type_in_content_area('V5 portal', 'portal', '9', verify_color_name='blue', item_name_index=1)
        '''
        wf_mainpage.Wf_Mainpage.verify_icon_type_in_content_area(self, item_name, icon_type, step_number, verify_color_name=verify_color_name, item_name_index=item_name_index)
    
    def verify_content_area_folder_publish_or_unpublish(self, folder_name, folder_status, msg, index=1):
        '''
        This function will verify content area folder is publish or unpublish.
        @param folder_name: 'P116'
        @param folder_status: 'publish'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_content_area_element_publish_or_unpublish('P116', 'publish', 'Step 9: Verify', index=0)
        '''
        wf_mainpage.Wf_Mainpage.verify_content_area_element_publish_or_unpublish(self, folder_name, 'folder', folder_status, msg, index=index)
    
    def verify_content_area_item_publish_or_unpublish(self, item_name, item_status, msg, index=1):
        '''
        This function will verify content area item is publish or unpublish.
        @param item_name: 'P116'
        @param item_status: 'publish'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_content_area_element_publish_or_unpublish('test', 'publish', 'Step 9: Verify', index=0)
        '''
        wf_mainpage.Wf_Mainpage.verify_content_area_element_publish_or_unpublish(self, item_name, 'file', item_status, msg, index=index)
    
    def verify_content_area_folder_shown_or_hide(self, folder_name, folder_status, msg, index=1):
        '''
        This function will verify content area folder is shown or publish.
        @param folder_name: 'P116'
        @param folder_status: 'shown'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_content_area_item_shown_or_hide('P116', 'shown', 'Step 9: Verify', index=0)
        '''
        wf_mainpage.Wf_Mainpage.verify_content_area_element_shown_or_hide(self, folder_name, 'folder', folder_status, msg, index=index)
    
    def verify_content_area_item_shown_or_hide(self, item_name, item_status, msg, index=1):
        '''
        This function will verify content area item is publish or unpublish.
        @param item_name: 'P116'
        @param item_status: 'publish'
        @param msg: 'Step 9: shown'
        @param index: 0
        :Usage verify_content_area_item_shown_or_hide('test', 'shown', 'Step 9: Verify', index=0)
        '''
        wf_mainpage.Wf_Mainpage.verify_content_area_element_shown_or_hide(self, item_name, 'file', item_status, msg, index=index)
    
    def click_search_input_box_option_dropdown(self):
        '''
        This function will select search input box option drop-down 
        :Usage click_search_input_box_option_dropdown()
        '''
        wf_mainpage.Wf_Mainpage.click_search_input_box_option_dropdown(self)
        
    def search_dropdown_in_advanced_folder_search(self, select_options=None, verify_selected=None, verify_list_options=None, drop_down_selected_list=None, label_text=None, comparision_type=None, step_number=None):
        '''
        This function will select, verify for Search option inside advance search folder.
        @param select_options: ['text']
        @param verify_selected:  'text'
        @param verify_list_options: ['text'] 
        @param drop_down_selected_list: ['text'] 
        @param label_text= 'Search'  
        @param comparision_type:'asequal', 'asnotin' or 'asin'
        @param step_number: '9'
        :Usage search_dropdown_in_advanced_folder_search(select_options=['text'], verify_selected='text', verify_list_options=['text'], drop_down_selected_list=['text'], label_text='Search', comparision_type='asin', step_number='9') 
        '''
        if select_options != None:
            wf_mainpage.Wf_Mainpage.select_dropdown_items_in_advanced_folder_search(self, 'Search', select_options)
        if verify_selected != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_default(self, 'Search', 'text_box', verify_selected, step_number)
        if verify_list_options != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_dropdown_options(self, 'Search', step_number, drop_down_expected_list=verify_list_options, comparision_type=comparision_type)
        if drop_down_selected_list != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_dropdown_options(self, 'Search', step_number, drop_down_selected_list=drop_down_selected_list)
        if label_text != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_default(self, 'Search', 'label_text', label_text, step_number)
            
    def type_dropdown_in_advanced_folder_search(self, select_options=None, verify_selected=None, verify_list_options=None, drop_down_selected_list=None, label_text=None, comparision_type=None, step_number=None):
        '''
        This function will select, verify for Type option inside advance search folder.
        @param select_options: ['text']
        @param verify_selected:  'text'
        @param verify_list_options: ['text'] 
        @param drop_down_selected_list: ['text'] 
        @param label_text= 'Type'  
        @param comparision_type:'asequal', 'asnotin' or 'asin'
        @param step_number: '9'
        :Usage type_dropdown_in_advanced_folder_search(select_options=['text'], verify_selected='text', verify_list_options=['text'], drop_down_selected_list=['text'], label_text='Type', comparision_type='asin', step_number='9') 
        '''
        if select_options != None:
            wf_mainpage.Wf_Mainpage.select_dropdown_items_in_advanced_folder_search(self, 'Type', select_options)
        if verify_selected != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_default(self, 'Type', 'text_box', verify_selected, step_number)
        if verify_list_options != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_dropdown_options(self, 'Type', step_number, drop_down_expected_list=verify_list_options, comparision_type=comparision_type)
        if drop_down_selected_list != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_dropdown_options(self, 'Type', step_number, drop_down_selected_list=drop_down_selected_list)
        if label_text != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_default(self, 'Type', 'label_text', label_text, step_number)
        
    def matching_behavior_dropdown_in_advanced_folder_search(self, select_options=None, verify_selected=None, verify_list_options=None, drop_down_selected_list=None, label_text=None, comparision_type=None, step_number=None):
        '''
        This function will select, verify for Matching Behavior option inside advance search folder.
        @param select_options: ['text']
        @param verify_selected:  'text'
        @param verify_list_options: ['text'] 
        @param drop_down_selected_list: ['text'] 
        @param label_text= 'Matching Behavior'  
        @param comparision_type:'asequal', 'asnotin' or 'asin'
        @param step_number: '9'
        :Usage matching_behavior_dropdown_in_advanced_folder_search(select_options=['text'], verify_selected='text', verify_list_options=['text'], drop_down_selected_list=['text'], label_text='Matching Behavior', comparision_type='asin', step_number='9') 
        '''
        if select_options != None:
            wf_mainpage.Wf_Mainpage.select_dropdown_items_in_advanced_folder_search(self, 'Matching Behavior', select_options)
        if verify_selected != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_default(self, 'Matching Behavior', 'text_box', verify_selected, step_number)
        if verify_list_options != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_dropdown_options(self, 'Matching Behavior', step_number, drop_down_expected_list=verify_list_options, comparision_type=comparision_type)
        if drop_down_selected_list != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_dropdown_options(self, 'Matching Behavior', step_number, drop_down_selected_list=drop_down_selected_list)
        if label_text != None:
            wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_default(self, 'Matching Behavior', 'label_text', label_text, step_number)
    
    def button_in_advanced_folder_search(self, button_name, select=None, color_name=None, location=None, msg=None):
        '''
        This function will select, verify button inside Advanced search folder.
        @param button_name: 'Reset'
        @param select: True
        @param color_name: 'blue'
        @param location: True
        @param msg: 'Step 9: Verify'
        :Usage button_in_advanced_folder_search('Reset', , select=True, color_name='blue', location=True, msg='Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.button_in_advanced_folder_search(self, button_name, select=select, color_name=color_name, location=location, msg=msg)
    
    def verify_advanced_folder_search_dialog_open_or_close(self, dialog_mode, msg):
        '''
        This function will verify advanced folder search dialog is open or close.
        @param dialog_mode: 'open'
        @param msg: 'Step 9: Verify'
        :Usage  verify_advanced_folder_search_dialog_open_or_close('open', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_advanced_folder_search_dialog_open_or_close(self, dialog_mode, msg)
        
    def verify_search_textbox_value(self, expected_value, msg):
        """
        This function will verify search textbox value
        """
        wf_mainpage.Wf_Mainpage.verify_search_textbox_value(self, expected_value, msg)
    
    def verify_folders_contain_searched_text_in_grid_view(self, searched_text, msg):
        """
        This function will verify folders or items are contain searched text. For example if enter 'x' in search text box, the result folders and items should be contain 'x'
        :param -  searched_text - text of entered in search text box
        :usage : verify_folders_contain_searched_text_in_grid_view('x', 'Step 04.01 : Verify folders contains "x"')
        """
        wf_mainpage.Wf_Mainpage.verify_folders_and_items_contain_searched_text(self, searched_text, msg, verify='folders')
        
    def verify_items_contain_searched_text_in_grid_view(self, searched_text, msg):
        """
        This function will verify folders or items are contain searched text. For example if enter 'x' in search text box, the result folders and items should be contain 'x'
        :param -  searched_text - text of entered in search text box
        :usage : verify_items_contain_searched_text_in_grid_view('x', 'Step 04.01 : Verify folder items contains "x"')
        """
        wf_mainpage.Wf_Mainpage.verify_folders_and_items_contain_searched_text(self, searched_text, msg, verify='items')
    
    def select_action_bar_tab(self, btn_name):
        '''
        Description : This function is used to select action bar tab
        :Usage select_action_bar_tab('Designer')
        '''
        wf_mainpage.Wf_Mainpage.select_action_bar_tab(self, btn_name)
    
    def verify_action_bar_all_tabs(self, expected_tabs_list, msg):
        """
        Description : This method will verify action bar all visible tabs.
        @usage  : verify_action_bar_all_tabs(['Common', 'Data', 'Designer', 'InfoAssist', 'Schedule', 'Other'], 'Step 01.1 : Verify.')
        """
        wf_mainpage.Wf_Mainpage.verify_action_bar_tabs(self, expected_tabs_list, msg)
    
    def verify_action_bar_specific_tabs(self, expected_tabs_list, msg):
        """
        Description : This method will verify action bar specific visible tabs.
        @usage  : verify_action_bar_specific_tabs(['Common', 'Data'], 'Step 01.1 : Verify.')
        """
        wf_mainpage.Wf_Mainpage.verify_action_bar_tabs(self, expected_tabs_list, msg, assert_type='asin')
    
    def verify_action_bar_tab_not_visible(self, expected_tabs_list, msg):
        """
        Description : This method will verify action bar not visible tabs.
        @usage  : verify_action_bar_tab_not_visible(['Common', 'Data'], 'Step 01.1 : Verify.')
        """
        wf_mainpage.Wf_Mainpage.verify_action_bar_tabs(self, expected_tabs_list, msg, assert_type='asnotin')
    
    def verify_action_bar_tab_color(self, tab_name, expected_color_name, msg):
        """
        Description : This method will verify action bar tab color
        @usage  : verify_action_bar_tab_color('Common', 'blue', 'Step 01.01 : Verify 'Common' tab color')
        """
        wf_mainpage.Wf_Mainpage.verify_action_bar_tab_color(self, tab_name, expected_color_name, msg)
        
    def select_action_bar_tabs_option(self, option_name):
        '''
        Descriptions : This method will select action bar tab option
        usage : select_action_bar_tabs_option('Page')
        '''
        wf_mainpage.Wf_Mainpage.select_action_bar_tab_option(self, option_name)
    
    def verify_action_bar_tab_all_options(self, expected_options_list, msg):
        '''
        Descriptions : This method will verify action bar tab all options
        usage : verify_action_bar_tab_all_options(['Folder', 'Upload Data', 'Connect', 'Workbook', 'Chart', 'Report', 'Page'], 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_action_bar_tab_options(self, expected_options_list, msg)
    
    def verify_action_bar_tab_specific_options(self, expected_options_list, msg):
        '''
        Descriptions : This method will verify action bar tab specific options
        usage : verify_action_bar_tab_specific_options(['Folder', 'Upload Data'], 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_action_bar_tab_options(self, expected_options_list, msg, assert_type='asin')
    
    def verify_action_bar_tab_options_not_visible(self, expected_options_list, msg):
        '''
        Descriptions : This method will verify action bar tab options not visible
        usage : verify_action_bar_tab_options_not_visible(['Folder', 'Upload Data', 'Connect', 'Workbook', 'Chart', 'Report', 'Page'], 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_action_bar_tab_options(self, expected_options_list, msg, assert_type='asnotin')
    
    def verify_action_bar_tab_option_color(self, option_name, expected_color, msg):
        """
        Descriptions : This method will verify action bar tab options color
        usage : verify_action_bar_tab_option_color('Folder', 'blue', 'Step 01.01 : Verify 'Common' tab option color')
        """
        wf_mainpage.Wf_Mainpage.verify_action_bar_tab_option_color(self, option_name, expected_color, msg)
       
    def verify_selected_action_bar_tab(self, selected_tab, msg):
        """
        Description : This method will verify selected action bar tab
        @usage  : verify_selected_action_bar_tab(['Common'], 'Step 01.01 : Verify 'Common' tab is selected as default')
        """
        wf_mainpage.Wf_Mainpage.verify_selected_action_bar_tab(self, selected_tab, msg)
    
    def verify_popup_dialog_caption(self, expected_title, msg):
        '''
        Description : This will verify popup dialog caption title.
        Example : verify_popup_dialog_caption('New Domains', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, expected_title, 'caption_tile', msg)
    
    def verify_new_domain_type_selected_value(self, expected_value, msg):
        '''
        Description : This will verify value in new domain Type
        Example : verify_new_domain_type_selected_value('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Type', 'drop_down_input_value', msg, property_value=expected_value)
    
    def verify_new_domain_all_type_drop_down_options(self, expected_list, msg):
        '''
        Description : This will verify value in new domain Type
        Example : verify_new_domain_type_selected_value(['test', 'test1'], 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Type', 'drop_down', msg, property_value=expected_list, comparison_type='asequal')
    
    def verify_new_domain_specific_value_in_type_drop_down_options(self, expected_list, msg):
        '''
        Description : This will verify specific value in new domain Type drop down
        Example : verify_new_domain_specific_value_in_type_drop_down_options(['test', 'test1'], 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Type', 'drop_down', msg, property_value=expected_list, comparison_type='asin')
    
    def verify_new_domain_type_drop_down_options_not_display(self, expected_list, msg):
        '''
        Description : This will verify new domain Type drop down value not displayed. 
        Example : verify_new_domain_type_drop_down_options_not_display(['test', 'test1'], 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Type', 'drop_down', msg, property_value=expected_list, comparison_type='asnotin')
    
    def select_new_domain_type_drop_down_option(self, expected_value):
        '''
        Description : This will select new domain Type drop down value not displayed. 
        Example : verify_new_domain_type_drop_down_options_not_display(['test', 'test1'], 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Type', 'drop_down', property_value=expected_value)
        
    def enter_new_domain_title_value(self, title_value):
        '''
        Description : This will enter value in new domain Title.
        Example : enter_new_domain_title_value('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Title', 'text_box', property_value=title_value)
        
    def verify_new_domain_title_value(self, title_value, msg):
        '''
        Description : This will verify value in new domain Title
        Example : verify_new_domain_title_value('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Title', 'text_box', msg, property_value=title_value)
    
    def enter_new_domain_name_value(self, name_value):
        '''
        Description : This will enter value in new domain Name.
        Example : enter_new_domain_name_value('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Name', 'text_box', property_value=name_value)
        
    def verify_new_domain_name_value(self, name_value, msg):
        '''
        Description : This will verify value in new domain Name
        Example : verify_new_domain_name_value('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Name', 'text_box', msg, property_value=name_value)
    
    def select_new_domain_create_reporting_server_application_checkbox(self, check=True):
        '''
        Description : This will Create Reporting Server Application check box in new Domains popup.
        Example : select_new_domain_create_reporting_server_application_checkbox(check=True)
        '''
        check_type = 'check' if check == True else 'uncheck'
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Create Reporting Server Application', 'check_box', property_value=check_type)
        
    def verify_new_domain_create_reporting_server_application_checkbox(self, msg, check=True):
        '''
        Description : This will Create Reporting Server Application check box in new Domains popup.
        Example : verify_new_domain_create_reporting_server_application_checkbox(check=True, 'Step 9: Verify')
        '''
        check_type = 'check' if check == True else 'uncheck'
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Create Reporting Server Application', 'check_box', msg, property_value=check_type)
    
    def click_button_on_popup_dialog(self, button_name):
        '''
        Description : This will click button on popup dialog.
        Example : click_button_on_popup_dialog('OK')
        '''
        wf_mainpage.Wf_Mainpage.button_in_popup_dialog_from_action_bar(self, button_name, 'click')
    
    def verify_button_text_on_popup_dialog(self, button_name, msg):
        '''
        Description : This will click ok button in new Domains popup.
        Example : verify_button_text_on_popup_dialog('OK', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.button_in_popup_dialog_from_action_bar(self, button_name, 'verify', msg=msg)
    
    def verify_button_enable_or_disable_on_popup_dialog(self, button_name, msg, enable=True):
        '''
        Description : This will click ok button in new Domains popup.
        Example : verify_button_text_on_popup_dialog('OK', 'Step 9: Verify')
        '''
        expected_status = 'enable' if enable == True else 'disable'
        wf_mainpage.Wf_Mainpage.button_in_popup_dialog_from_action_bar(self, button_name, 'visibility', property_value=expected_status, msg=msg)
    
    def verify_button_color_on_popup_dialog(self, button_name, expected_color, msg):
        '''
        Description : This will click ok button in new Domains popup.
        Example : verify_button_text_on_popup_dialog('OK', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.button_in_popup_dialog_from_action_bar(self, button_name, 'color_verify', property_value=expected_color, msg=msg)
    
    def verify_delete_message_in_popup_dialog(self, expected_message, msg):
        '''
        Description : This will verify delete message in popup dialog.
        Example : verify_delete_message_in_popup_dialog('OK', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, None, 'text', msg, property_value=expected_message)
    
    def verify_popup_dialog_is_displayed(self, visible_mode, msg):    
        '''
        Description : This will verify popup dialog is displayed.
        Example : verify_popup_dialog_is_displayed(True, 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_popup_dialog_from_action_bar_is_displayed(self, visible_mode, msg)
    
    def enter_new_folder_title_in_popup_dialog(self, title_value):
        '''
        Description : This will enter value in new folder Title.
        Example : enter_new_folder_title_in_popup_dialog('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Title', 'text_box', property_value=title_value)
        
    def verify_new_folder_title_in_popup_dialog(self, title_value, msg):
        '''
        Description : This will verify value in new folder Title
        Example : verify_new_folder_title_in_popup_dialog('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Title', 'text_box', msg, property_value=title_value)
    
    def enter_new_folder_name_in_popup_dialog(self, name_value):
        '''
        Description : This will enter value in new folder Name.
        Example : enter_new_folder_name_in_popup_dialog('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Name', 'text_box', property_value=name_value)
        
    def verify_new_folder_name_in_popup_dialog(self, name_value, msg):
        '''
        Description : This will verify value in new folder Name
        Example : verify_new_folder_name_in_popup_dialog('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Name', 'text_box', msg, property_value=name_value)

    def enter_url_title_in_popup_dialog(self, title):
        '''
        Description : This will enter the URL title in URL dialog window.
        Example : enter_url_title_in_popup_dialog('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Title', 'text_box', property_value=title)
    
    def verify_url_title_in_popup_dialog(self, actual_title, msg):
        '''
        Description : This will verify the URL title in URL dialog window.
        Example : verify_url_title_in_popup_dialog('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Title', 'text_box', msg, property_value=actual_title)
    
    def enter_url_name_in_popup_dialog(self, name):
        '''
        Description : This will enter the URL name in URL dialog window.
        Example : enter_url_name_in_popup_dialog('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Name', 'text_box', property_value=name)
    
    def verify_url_name_in_popup_dialog(self, actual_name, msg):
        '''
        Description : This will verify the URL name in URL dialog window.
        Example : verify_url_name_in_popup_dialog('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Name', 'text_box', msg, property_value=actual_name)
    
    def enter_url_summary_in_popup_dialog(self, summary):
        '''
        Description : This will enter the URL summary in URL dialog window.
        Example : enter_url_summary_in_popup_dialog('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Summary', 'text_box', property_value=summary)
    
    def verify_url_summary_in_popup_dialog(self, actual_summary, msg):
        '''
        Description : This will verify URL summary in URL dialog window.
        Example : verify_url_summary_in_popup_dialog('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Summary', 'text_box', msg, property_value=actual_summary)
    
    def enter_url_in_popup_dialog(self, url, text_find_type='startwith'):
        '''
        Description : This will enter the URL value in URL dialog window.
        Example : enter_url_in_popup_dialog('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'URL', 'text_box', property_value=url, text_find_type=text_find_type)
    
    def verify_url_in_popup_dialog(self, actual_url, msg):
        '''
        Description : This will verify URL value in URL dialog window.
        Example : verify_url_in_popup_dialog('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'URL', 'text_box', msg, property_value=actual_url)
    
    def add_comment_in_blog(self,comment):
        '''
        Description : This will add comments in the blog window
        Example : add_Comment_in_blog('Weather is good today') 
        '''
        wf_mainpage.Wf_Mainpage.add_comment(self, comment)
        
    def verify_comment_in_blog(self,comment_row, comment_to_verify, msg):
        '''
        Description : This will verify the comments in the launcher window 
        Example : verify_comment_in_blog(1, 'This is awesome' , 'Step 4.1: Verify the Comment )
        '''
        wf_mainpage.Wf_Mainpage.verify_comment(self, comment_row, comment_to_verify, msg)
    
    def enter_blog_title_in_popup_dialog(self,title):
        '''
        Description : This will enter the Blog Title in dialog window.
        Example : add_blog_title_in_popup_dialog('test')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Title', 'text_box', property_value=title)
    
    def enter_blog_summary_in_popup_dialog(self, summary):
        '''
        Description : This will enter the URL summary in URL dialog window.
        Example : add_blog_summary_in_popup_dialog('This is blog 2')
        '''
        wf_mainpage.Wf_Mainpage.open_popup_dialog_from_action_bar(self, 'Summary', 'text_area', property_value=summary)
    
    def verify_blog_title_in_popup_dialog(self, actual_title, msg):
        '''
        Description : This will verify blog title in  dialog window.
        Example : verify_blog_title_in_popup_dialog('test', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Title', 'text_box', msg, property_value=actual_title)
    
    def verify_blog_summary_in_popup_dialog(self, actual_summary, msg):
        '''
        Description : This will verify blog sumamry in dialog window. 
        Example : verify_blog_summary_in_popup_dialog('test if fine', 'Step 9: Verify')
        '''
        wf_mainpage.Wf_Mainpage.verify_open_popup_dialog_from_action_bar(self, 'Summary', 'text_area', msg, property_value=actual_summary)
    
    def verify_action_bar_is_not_visible(self, msg):
        """
        Description : This method will verify whether action bar tab is not displayed
        @usage : verify_action_bar_is_not_visible('Step 01.01 : Verify action bar is not display)
        """
        wf_mainpage.Wf_Mainpage.verify_action_bar_is_not_visible(self, msg)
        
    def collapse_action_bar(self, option_name='collapse'):
        """
        Descriptions : This method will collapse_action_bar
        usage : collapse_action_bar(option_name='collapse')
        """
        wf_mainpage.Wf_Mainpage.collapse_or_expand_action_bar(self, option_name=option_name)
        
    def expand_action_bar(self, option_name='expand'):
        """
        Descriptions : This method will expand_action_bar
        usage : expand_action_bar(option_name='expand')
        """
        wf_mainpage.Wf_Mainpage.collapse_or_expand_action_bar(self, option_name=option_name)
        
    def verify_resource_dialog_is_visible(self, visibility, msg):
        """
        Description: This method is used to find if resource dialogue is visible
        usage: verify_resource_dialog_is_visible(True,'Step 4.2: ') 
        """
        wf_mainpage.Wf_Mainpage.verify_resource_dialog_is_displayed(self, visibility, msg)
        
    def verify_caption_title_in_resource_dialog(self, title, msg):
        """
        Description: This method is used to verify the title in resource dialog
        usage: verify_caption_title_in_resource_dialog('Select', 'Step 9: Verify')
        """
        wf_mainpage.Wf_Mainpage.verify_resource_dialog_caption_title(self, title, msg)
    
    def verify_upload_message(self, file_name, uploaded_msg, msg):
        """
        Description: This method is used to verify uploaded message
        usage: verify_upload_message('Bluehills.jpg', 'Bluehills.jpg upload completed', 'Step 9: Verify')
        """
        wf_mainpage.Wf_Mainpage.verify_upload_message(self, file_name, msg, uploaded_msg=uploaded_msg)
    
    def verify_upload_complete_text_message_color(self, file_name, color_name, msg):
        """
        Description: This method is used to verify uploaded message text color
        usage: verify_upload_message('Bluehills.jpg', 'green', 'Step 9: Verify')
        """
        wf_mainpage.Wf_Mainpage.verify_upload_message(self, file_name, msg, color_name=color_name)
        
    def select_action_bar_new_text_resource_tab(self, btn_name):
        '''
        Description : This function is used to select action bar new text resource tab
        :Usage select_action_bar_new_text_resource_tab('Designer')
        '''
        wf_mainpage.Wf_Mainpage.select_action_bar_new_text_resource_tab(self, btn_name)
    
    def select_action_bar_new_text_resource_tab_option(self, option_name):
        '''
        Descriptions : This method will select action bar new text resource tab option
        usage : select_action_bar_new_text_resource_tab_option('Page')
        '''
        wf_mainpage.Wf_Mainpage.select_action_bar_new_text_resource_tab_option(self, option_name)
        
    def upload_file_using_action_bar(self, upload_file_list, Path="\\\ibirisc2\\bipgqashare\\Images_and_Things\\"):
        """
        Desc: This function uploads files in homepage using Upload_File action bar
        :param file_name='upload.png'
        :usage upload_file_using_action_bar('uload.png')
        """        
        wf_mainpage.Wf_Mainpage.upload_file_using_action_bar(self, upload_file_list, file_path_location=Path)
    
    def select_toolbar_button_from_resource_dialog(self, button):
        '''
        Desc: This function will select options in toolbar button
        button = list or grid or refresh
        :usage select_toolbar_button('list')
        '''
        wf_mainpage.Wf_Mainpage.select_toolbar_button(self, button, tool_css=".pop-top [class*='toolbar'] [class*='toolbar-button-div'] [class*='fa {0}']")
    
    def select_search_input_box_from_resource_dialog(self, option_type='write', input_text_msg=None, verify_value=None, msg=None, input_box_css=".pop-top [class*='div-search'] [class*='txt-search'] input"):
        '''
        Desc: This function will select options in toolbar button
        button = list or grid or refresh
        :usage select_toolbar_button('list')
        '''
        wf_mainpage.Wf_Mainpage.search_input_box_options(self, option_type=option_type, input_text_msg=input_text_msg, verify_value=verify_value, msg=msg, input_css=input_box_css)
    
    def select_crumb_item_from_resource_dialog(self, crumb_item_name, selection_type='left'):
        """
        Desc: This function will select crumb item from resource dialog
        :usage select_crumb_item_from_resource_dialog('car.mas', click_type='double')
        """
        wf_mainpage.Wf_Mainpage.select_crumb_item_from_resource_dialog(self, crumb_item_name, selection_type=selection_type)
    
    def select_file_or_folder_from_resource_dialog(self, item_name, selection_type='left', view_type="list_view"):
        """
        Desc: This function will select file or folder from resource dialog
        :usage select_file_or_folder_from_resource_dialog('car.mas', click_type='double')
        """
        wf_mainpage.Wf_Mainpage.select_file_or_folder_from_resource_dialog(self, item_name, selection_type=selection_type, view_type=view_type)
    
    def verify_view_title_labels_from_resource_dialog(self, expected_list, msg, view_type='grid_view', label_type='files', list_view_css=".pop-top [class*='files-box-files-title']", grid_view_css=".pop-top [class*='sd-content-title-label-{0}']"):
        '''
        Desc: This function will select file or folder from resource dialog
        :usage select_file_or_folder_from_resource_dialog('car.mas', click_type='double')
        '''
        wf_mainpage.Wf_Mainpage.verify_view_title_labels(self, expected_list, msg, view_type=view_type, label_type=label_type, list_view_css=list_view_css, grid_view_css=grid_view_css)
    
    def double_click_content_item_in_list_view(self, item_name, folder_path=None, folder_index=0):
        """
        Description : double click on content file in list view.
        :arg - folder_path : If you want expand folders then pass folder path
        :Usage : double_click_content_item_in_list_view("C123456")
        """
        wf_mainpage.Wf_Mainpage.double_click_content_item_in_list_view(self, item_name, folder_path, folder_index)
    
    def verify_selected_resource_tree_item(self, expected_item_list, step_num):
        """
        Description : This method will verify selected resource tree item by comparing background-color value
        :Usage : verify_selected_resource_tree_item(['G435182'], "01.01")
        """
        wf_mainpage.Wf_Mainpage.verify_selected_resource_tree_item(self, expected_item_list, step_num)
    
    def check_tags_in_homepage(self,tag_name):
        """
        Description : this method is used to click tags in homepage(ref enhancements tag section)
        :usage:check_tags_in_homepage("Personal")
        """
        wf_mainpage.Wf_Mainpage.check_tags_in_homepage(self, tag_name)
    
    def resource_dialog(self):
        """
        Description : This method will return object of ResourceDialog class
        Using this method we can perform all actions related to resource dialog
        """
        return ResourceDialog(self.driver)
              
class Run(BasePage):
    
    def __init__(self, driver):
        super(Run, self).__init__(driver)   
        
    def verify_title(self, expected_title_list, step_num):
        """
        Description : Verify home page run dialog title
        Usage : verify_title(["C123456"], "10.01")
        """    
        wf_mainpage.Run.verify_title(self,expected_title_list, step_num)
    
    def switch_to_frame(self):
        """
        Description : Switch to run frame
        Usage : switch_to_frame()
        """
        wf_mainpage.Run.switch_to_frame(self)
    
    def close(self):
        """
        Description : Click on close icon to close run window.
        Usage : close()
        """
        wf_mainpage.Run.close(self)
    
    def open_in_new_window(self):
        """
        Description : Click on open in new window button to open run file in new window
        Usage : open_in_new_window()
        """
        wf_mainpage.Run.open_in_new_window(self)
    
    def switch_to_default_content(self):
        """
        Description : Switch to default content from run window frame
        Usage : switch_to_default_content()
        """
        wf_mainpage.Run.switch_to_default_content(self)