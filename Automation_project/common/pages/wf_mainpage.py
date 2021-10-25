import pyautogui
import sys
import time, re
from common.lib.base import BasePage
from common.lib.core_utility import CoreUtillityMethods as core_utils
from common.lib.javascript import JavaScript as j_script
from common.lib.utillity import UtillityMethods as util_method
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from common.lib.global_variables import Global_variables
from common.lib.webfocus.context_menu import Main_Page
from common.lib.webfocus import poptop_dialog
from selenium.webdriver.support.color import Color
from common.lib.webfocus.poptop_dialog import Poptop_Dialog as pop_obj
from common.lib.webfocus.resource_dialog import Resource_Dialog as resc_obj
from common.locators.wf_mainpage_locators import WfMainPageLocators

if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
    import clipboard
else:
    import uiautomation as automation
    import keyboard

class Wf_Mainpage(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    
    def __init__(self, driver):
        super(Wf_Mainpage, self).__init__(driver)
    
    def current_time(self):
        '''
        This function will get current date and update in global file variable current_time
        @author:Aftab_Alam_Khan
        '''
        Global_variables.current_time=time.strftime("X%H:%M:%S", time.localtime())
    
    def click_on_banner_logo(self):
        """
        This function will click on top banner of logo in main home page
        """
        banner_logo_css = ".home-banner .banner-logo"
        banner_logo_obj = util_method.validate_and_get_webdriver_object(self, banner_logo_css, 'Home page banner logo')
        core_utils.left_click(self, banner_logo_obj)
        
    def colapse_sidebar(self,button):
        '''
        This Function is used to colapse the sidebar in mainpage.
        @author:Nirajan Das
        '''
        colapse_sidebar_css="[class^='main-box'] [class^='home-banner ibx-widget'] [class^='menu-banner-logo-nav-button-{0}']>[data-ibxp-glyph-classes='fa fa-caret-{0}']".format(button)
        util_method.synchronize_with_number_of_element(self, colapse_sidebar_css, 1, 30)
        colapse_sidebar_object=self.driver.find_element_by_css_selector(colapse_sidebar_css)
        core_utils.left_click(self, colapse_sidebar_object)
        
    def verify_crumb_box(self, expected_crumb_box_text, msg='Step X'):
        '''
        @Param: expected_crumb_box_text = 'Domains->P292_S10660->G193250->Portals->V4 Portals'
        @param: msg: 'Step 9'
        Usage: verify_crumb_box("Domains->P292_S10660->G193250->Portals->V4 Portals", "Step 05")
        This will verify the crumb box text. User has to pass the text in this: 'Domains->P116->S7073' format.
        @author:Nirajan Das
        '''
        crumb_box_css="[class^='main-box'] [class^='main-panel'] [class^='right-main-panel'] [class^='crumb-box']"
        crumb_box_arrow_css="[class^='main-box'] [class^='main-panel'] [class^='right-main-panel'] [class^='crumb-box'] [class^='sd-right-carat']"
#         actual_crumb_box_text=self.driver.find_element_by_css_selector(crumb_box_css).text.replace('\n','->')
        actual_crumb_box_text=re.sub(r'\n+','->', self.driver.find_element_by_css_selector(crumb_box_css).text)
        custom_msg=msg + ": verify the crumb box text."
        util_method.asequal(self, expected_crumb_box_text, actual_crumb_box_text, custom_msg)
        expected_number_of_crumb_box_arrow_objects=len(expected_crumb_box_text.split('->'))-1
        actual_number_of_crumb_box_arrow_objects=len(self.driver.find_elements_by_css_selector(crumb_box_arrow_css))
        custom_msg=msg + ": verify the number of arrow separator present within crumb box."
        util_method.asequal(self, expected_number_of_crumb_box_arrow_objects, actual_number_of_crumb_box_arrow_objects, custom_msg)
    
    def select_option_from_crumb_box(self, crumb_box_ribbon_option_name):
        '''
        This function is used to select option from ribbon or crumb_box.
        @param crumb_box_ribbon_option_name: 'Domains'
        :Usage select_option_from_crumb_box('Domains')
        @author:Aftab_Alam_Khan
        '''
        crumb_box_ribbon_option_name = 'Workspaces' if crumb_box_ribbon_option_name == 'Domains' else crumb_box_ribbon_option_name
        if crumb_box_ribbon_option_name is None:
            raise KeyError('Please pass crumb_box_ribbon_option_name to use this method.')
        crumb_box_css = ".crumb-box [title] .ibx-label-text"
        try:
            crumb_elems=self.driver.find_elements_by_css_selector(crumb_box_css)
            temp=crumb_elems[0]
            try:
                domain_obj=[elem for elem in crumb_elems if elem.text.strip()==crumb_box_ribbon_option_name][0]
                core_utils.left_click(self, domain_obj)
                j_script.wait_for_page_loads(self, 120, pause_time=3)
            except IndexError:
                raise IndexError("{0} option not exist inside Crumb_box or Ribbon.".format(crumb_box_ribbon_option_name))
        except IndexError:
            del temp
            raise IndexError("Crumb_box or Ribbon option is not exist.")    
    
    def select_right_arrow_in_crumb_box(self, crumb_box_option_name):
        '''
        This will click on right arrow on next to option button name in crumb box.
        
        @param crumb_box_option_name: 'Domains'
        :Usage  select_right_arrow_in_crumb_box('Domains')
        '''
        crumb_box_css = ".crumb-box [title] .ibx-label-text"
        crumb_box_right_arrow_css="[class^='main-box'] [class^='main-panel'] [class^='right-main-panel'] [class^='crumb-box'] [class^='sd-right-carat']"
        if crumb_box_option_name is None:
            raise KeyError('Please pass crumb_box_option_name to use this method.')
        crumb_box_option_elem = util_method.validate_and_get_webdriver_objects(self, crumb_box_css, 'Home page crumb_box button name')
        for option_number in range(len(crumb_box_option_elem)):
            if crumb_box_option_elem[option_number].text.strip() ==  crumb_box_option_name:
                option_name_index = option_number-1
                break
        crumb_box_right_arrow_elem = util_method.validate_and_get_webdriver_objects(self, crumb_box_right_arrow_css, 'Home page crumb_box Right arrow')
        try:
            right_arrow_elem = crumb_box_right_arrow_elem[option_name_index]
        except IndexError:
            raise IndexError('"{0}" having no right arrow in crumb box'.format(crumb_box_option_name))
        core_utils.left_click(self, right_arrow_elem)
    
    def create_new_folder(self, folder_name):
        '''
        This function will create a new folder based on the provided folder name
        create_new_folder('Test Folder')
        '''
        row_element = pop_obj.get_row_element_according_to_text_string(self, 'Title')
        title_input_box_element = util_method.validate_and_get_webdriver_object(self, 'input', 'Title Input', parent_object=row_element)
        util_method.set_text_to_textbox_using_keybord(self, folder_name, text_box_elem=title_input_box_element)
        util_method.synchronize_with_visble_text_within_parent_object(self, row_element, 'input', folder_name, 45, text_option='value')
        ok_btn_element = util_method.validate_and_get_webdriver_object(self, ".pop-top [class*='ok-button']",'ok')
        core_utils.left_click(self, ok_btn_element)
        time.sleep(1)
        folder_exists_msg = self.driver.find_elements_by_css_selector(".pop-top .form-fill-error-text")
        if len(folder_exists_msg) >0  and 'Folder already exists' in folder_exists_msg[0].text :
            cancel_button = util_method.validate_and_get_webdriver_object(self, ".pop-top .ibx-dialog-cancel-button", "Folder creation cancel button")
            core_utils.left_click(self, cancel_button)
            util_method.synchronize_until_element_disappear(self, ".pop-top", 8)
            Wf_Mainpage.delete_exists_folder_and_create_new(self, folder_name)
        
    def verify_new_folder(self, caption_tile='New Folder', tile_value=None, name_value=None, step_number='X'):
        '''
        Description : This function will verify New Folder dialog
        Example : verify_new_folder(caption_tile='New Folder', tile_value='Test', name_value='Test', step_number='9')
        '''
        if caption_tile:
            actual_value = pop_obj.get_caption_title(self)
            expected_value = caption_tile
            msg='Step {0}: Verify {1} caption.'.format(step_number, caption_tile)
        if tile_value:
            title_input_box_element = pop_obj.get_element_in_dialog(self, 'Title', 'input', 'Title Input')
            actual_value = util_method.get_element_attribute(self, title_input_box_element, 'value')
            expected_value = tile_value
            msg='Step {0}: Verify {1} Title value.'.format(step_number, tile_value)
        if name_value:
            name_input_box_element = pop_obj.get_element_in_dialog(self, 'Name', 'input', 'Name Input')
            actual_value = util_method.get_element_attribute(self, name_input_box_element, 'value')
            expected_value = name_value
            msg='Step {0}: Verify {1} Name value.'.format(step_number, name_value)
        util_method.asequal(self,expected_value,actual_value,msg)
    
    def verify_username_dropdown_menu(self, expected_menu_item_list, navigate_path=None, msg='Step X', comparision_type='asequal', click_type='move'):
        '''
        This will verify the menu or submenu items from username dropdown.'Domains->P116->S7073' format.
        @author:Nirajan Das
        '''
        Wf_Mainpage.verify_new_welcome_page(self)
        pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']"
        username_dropdown_css="[class^='main-box'] [class^='home-banner ibx-widget'] [class^='right-menu-banner'] [class^='ibx-widget']"
        username_dropdown_object=self.driver.find_element_by_css_selector(username_dropdown_css)
        core_utils.python_left_click(self, username_dropdown_object)
        util_method.synchronize_with_number_of_element(self, pop_up_css, 1, 90)
        if navigate_path != None:
            Wf_Mainpage.select_context_menu_item(self, navigate_path, click_type=click_type)
        time.sleep(1)
        Wf_Mainpage.verify_context_menu_item(self, expected_menu_item_list, msg=msg, comparision_type=comparision_type)
    
    def verify_new_welcome_page(self):
        '''
        To check New Welcome Home page.
        '''
        current_setup_name = self.driver.current_url
        new_welcome_breadcrumb_css = WfMainPageLocators.CONTENT_ICON_CSS
        error_msg = 'This setup "'+current_setup_name+'" does not set to new Welcome Page. Please change to New welcome Page to continue this test case.'
        try:
            self.driver.find_element_by_css_selector(new_welcome_breadcrumb_css)
        except NoSuchElementException:
            raise LookupError(error_msg)
    
    def select_username_dropdown_menu(self, navigate_path=None):
        '''
        Desc: This will select the menu or submenu items from username dropdown.
        usage: wfmain_obj.select_username_dropdown_menu(navigate_path='Administration->Security Center')
        @author:Nirajan Das
        '''
        Wf_Mainpage.verify_new_welcome_page(self)
        pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']"
        username_dropdown_css="[class^='main-box'] [class^='home-banner ibx-widget'] [class^='right-menu-banner'] [class^='ibx-widget']"
        username_dropdown_object=self.driver.find_element_by_css_selector(username_dropdown_css)
        core_utils.left_click(self, username_dropdown_object)
        util_method.synchronize_with_number_of_element(self, pop_up_css, 1, 90)
        if navigate_path != None:
            Wf_Mainpage.select_context_menu_item(self, navigate_path)
        time.sleep(1)
    
    def get_repository_folder(self, folder_name, index=0):
        """
        Descriptions : This method will return the repository folder object 
        example usage : get_repository_folder('Retail Samples', index=1)
        """
        folder_name = 'Workspaces' if folder_name == 'Domains' else folder_name #After 8206, Domains has been changed as Workspaces
        scroll_css="div[class='ibfs-tree']"
        folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node']"
        folder_obj_list = util_method.validate_and_get_webdriver_objects(self, folder_css, folder_name)
        folder_obj=j_script.find_elements_by_text(self, folder_obj_list, folder_name)
        folder_not_found_error="[{0}] folder not found under the domains".format(folder_name)
        if folder_obj == []:
            raise FileNotFoundError(folder_not_found_error)
        else:
            j_script.scrollTop(self, scroll_css, folder_obj[int(index)], wait_time=1)
        return (folder_obj[int(index)])
    
    def verify_repository_folder_icon_plus_minus(self, folder_name, option_name, msg, index=0):
        """
        Descriptions : This method used to verify home page domains folder expand or collapse icon (+/-)
        example usage : verify_repository_folder_icon_plus_minus('Retail Samples', 'expand', 'Step 9: verify', index=1)
        """
        index_num= int(index)
        if option_name not in ['expand', 'collapse']:
            raise IndexError("Please pass option_name value 'expand' and 'colapse'.")
        expand_icon_css="div[class*='ibx-icons'][class*='plus']"
        collapse_icon_css="div[class*='ibx-icons'][class*='minus']"
        folder_obj = Wf_Mainpage.get_repository_folder(self, folder_name, index_num)
        if option_name.lower() == 'expand':
            visible_elem = util_method.validate_and_get_webdriver_object(self, expand_icon_css, 'Expand Icon', parent_object=folder_obj)
        else:
            visible_elem = util_method.validate_and_get_webdriver_object(self, collapse_icon_css, 'Collapse Icon', parent_object=folder_obj)
        util_method.verify_object_visible(self, None, True, msg, elem_obj=visible_elem)
               
    def expand_repository_folders(self, folder_path, index=0):
        """
        Descriptions : This method used to expand home page domains folder 
        example usage : expand_repository_folders('Retail Samples->Reports->Auto Link Targets')
        @author:Aftab_Alam_Khan
        """
        expand_icon_css="div[class*='plus']"
        folder_list=folder_path.split('->')
        index_num= int(index)
        for folder in folder_list:
            folder_obj = Wf_Mainpage.get_repository_folder(self, folder, index_num)
            try:
                expand_icon_obj=util_method.validate_and_get_webdriver_objects(self, expand_icon_css, folder, parent_object=folder_obj)
                if len(expand_icon_obj)>0 :
                    core_utils.left_click(self, expand_icon_obj[0])
            except AttributeError:
                pass
            if folder_list[-1] == folder:
                time.sleep(2)
                core_utils.left_click(self, folder_obj)
    
    def collapse_repository_folders(self, folder_name):
        """
        Descriptions : This method used to collapse home page repository folders 
        example usage : collapse_repository_folders('Retail Samples')
        @author:Aftab_Alam_Khan
        """
        collapse_icon_css="div[class*='ibx-icons'][class*='ds-icon-minus']"
        index=0
        folder_obj = Wf_Mainpage.get_repository_folder(self, folder_name, index)
        try:
            collapse_icon_obj=util_method.validate_and_get_webdriver_objects(self, collapse_icon_css, folder_name, parent_object=folder_obj)
            if len(collapse_icon_obj)>0 :
                core_utils.left_click(self, collapse_icon_obj[0])
        except AttributeError:
            pass
        time.sleep(2)
        core_utils.left_click(self, folder_obj)
    
    def verify_hidden_repository_folder(self, hidden_folder_name, msg, index=0):
        '''
        This function will verify repository folder is hidden using it's opacity value.
        @param hidden_folder_name: 'P116'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_hidden_repository_folder('P116', 'Step 9: Verify', index=0)
        '''
        repository_folder_opacity_value = '0.6' 
        folder_label_css = ".ibx-label-text"
        folder_obj = Wf_Mainpage.get_repository_folder(self, hidden_folder_name, index)
        hidden_folder_obj=util_method.validate_and_get_webdriver_object(self, folder_label_css, hidden_folder_name, parent_object=folder_obj)
        hidden_status_value = util_method.get_element_css_propery(self, hidden_folder_obj, 'opacity')
        util_method.asequal(self, repository_folder_opacity_value, hidden_status_value, msg)
    
    def verify_repository_folder_publish_or_unpublish(self, folder_name, folder_status, msg, index=0):
        '''
        This function will verify repository folder is publish or unpublish.
        @param folder_name: 'P116'
        @param folder_status: 'publish'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_repository_folder_publish_or_unpublish('P116', 'publish', 'Step 9: Verify', index=0)
        '''
        if folder_status.lower() not in ['publish', 'unpublish']:
            raise IndexError("Please pass folder_status as 'publish' or 'unpublish'")
        publish_folder_css = 'ibfs-item-published' 
        folder_obj = Wf_Mainpage.get_repository_folder(self, folder_name, index)
        element_class_attribute = util_method.get_element_attribute(self, folder_obj, 'class')
        actual_value = 'publish' if publish_folder_css in element_class_attribute else 'unpublish'
        util_method.asequal(self, folder_status, actual_value, msg)
    
    def verify_repository_folder_font_style(self, folder_name, font_name, msg, index=0):
        '''
        This function will verify repository folder font style.
        @param folder_name: 'P116'
        @param font_name: 'italic'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_repository_folder_font_style('P116', 'italic', 'Step 9: Verify', index=0)
        '''
        folder_obj = Wf_Mainpage.get_repository_folder(self, folder_name, index)
        actual_value = util_method.get_element_css_propery(self, folder_obj, 'font-style')
        util_method.asequal(self, font_name, actual_value, msg)
    
    def right_click_repository_folder(self, folder_path, expire_time=90, verification_state='expand'):                                                            
        """
        :Usage right_click_repository_folder('P242_S10674_G171304->My Content')
        @author:Aftab_Alam_Khan
        """
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected"
        if verification_state.lower()=='expand':
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        else:
            Wf_Mainpage.collapse_repository_folders(self, folder_path)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        selected_folder_obj = self.driver.find_element_by_css_selector(selected_folder_css)
        core_utils.right_click(self, selected_folder_obj)
    
    def double_click_repository_folder(self, folder_path, expire_time=90, verification_state='expand'):                                                            
        """
        :Usage double_click_repository_folder('P242_S10674_G171304->My Content')
         @author:Aftab_Alam_Khan
        """
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected"
        if verification_state.lower()=='expand':
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        else:
            Wf_Mainpage.collapse_repository_folders(self, folder_path)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        selected_folder_obj = self.driver.find_element_by_css_selector(selected_folder_css)
        core_utils.double_click(self, selected_folder_obj)
    
    def left_click_repository_folder(self, folder_path, expire_time=90, verification_state='expand'):                                                            
        """
        :Usage left_click_repository_folder('P242_S10674_G171304->My Content')
        @author:Aftab_Alam_Khan
        """
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected"
        if verification_state.lower()=='expand':
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        else:
            Wf_Mainpage.collapse_repository_folders(self, folder_path)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        
    def select_repository_folder_context_menu(self, folder_path, menu_item_path, expire_time=90, click_option='right_click', verification_state='expand'):
        """
        Desc:-This function is right click on content repository folder and select the item.
        :param folder_path='P242_S10674_G171304->Alert'
        :param menu_item_path='Security->Owner...'
        :param expire_time=This parameter is wait for an element.
        :Usage select_repository_folder_context_menu('P242_S10674_G171304', 'Properties')
        @author:Aftab_Alam_Khan
        """
        if click_option=='left_click':
            Wf_Mainpage.left_click_repository_folder(self, folder_path, expire_time=expire_time, verification_state=verification_state)
        elif click_option=='right_click':
            Wf_Mainpage.right_click_repository_folder(self, folder_path, expire_time=expire_time, verification_state=verification_state)
        elif click_option=='double_click':
            Wf_Mainpage.double_click_repository_folder(self, folder_path, expire_time=expire_time, verification_state=verification_state)
        Wf_Mainpage.select_context_menu_item(self, menu_item_path, expire_time=expire_time)
    
    def verify_repository_folders(self, folder_path, folder_name_list, msg, expire_time=90, verification_state='expand', comparion_type='asin'):    
        """
        @param verification_state:'expand' or 'collapse'
        :Usage verify_repository_folders('P242_S10674_G171304->My Content', ['autodevuser56'], 'Step 9: verify')
        @author:Aftab_Alam_Khan
        """
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected"
        folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node']"
        if verification_state.lower()=='expand':
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        elif verification_state.lower()=='collapse':
            Wf_Mainpage.collapse_repository_folders(self, folder_path)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        repository_folder_obj=self.driver.find_elements_by_css_selector(folder_css)
        repository_folder_list=[folder for folder in (folder.text.strip() for folder in repository_folder_obj if folder.is_displayed())]
        for folder_name in folder_name_list:
            if comparion_type.lower() == 'asin':
                if folder_name in repository_folder_list:
                    status=True
                else:
                    status=False
                    break
            elif comparion_type.lower() == 'asnotin':
                if folder_name not in repository_folder_list:
                    status=True
                else:
                    status=False
                    break
        if comparion_type.lower() == 'asin':
            if status == True:
                util_method.asequal(self, status, True, msg)
            else:
                util_method.asin(self, folder_name, repository_folder_list, msg)
        elif comparion_type.lower() == 'asnotin':
            if status == True:
                util_method.asequal(self, status, True, msg)
            else:
                util_method.as_notin(self, folder_name, repository_folder_list, msg)
        
    def verify_main_node_under_repository_folders(self, folder_name, folder_name_list, msg, expire_time=90, comparion_type='asequal'):    
        """
        This function is used to verify main nodes under domain tree.
        :Usage verify_repository_folders('P242_S10674_G171304', ['autodevuser56'], 'Step 9: verify')
        @author:Aftab_Alam_Khan
        """
        count = 1
        step_number = re.search(r'\d+', msg).group()
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected"
        folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node']"
        Wf_Mainpage.collapse_repository_folders(self, folder_name)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        repository_folder_obj=self.driver.find_elements_by_css_selector(folder_css)
        repository_folder_list=[folder.text.strip() for folder in repository_folder_obj]
        if comparion_type.lower()=='asequal':
            util_method.asequal(self, folder_name_list, repository_folder_list, msg)
        elif comparion_type.lower()=='asin':
            for folder in folder_name_list:
                custom_msg="Step {0}.{1}: Verify '{2}' items in the repository folders.".format(step_number, count, folder)
                count+=1
                util_method.asin(self, folder, repository_folder_list, custom_msg)
        elif comparion_type.lower()=='asnotin':
            for folder in folder_name_list:
                custom_msg="Step {0}.{1}: Verify '{2}' items not in the repository folders.".format(step_number, count, folder)
                count+=1
                util_method.as_notin(self, folder, repository_folder_list, custom_msg)
        
    def select_content_area_folder_context_menu(self, item_name, context_menu_item_path=None, folder_path=None, click_option='right_click', item_name_index=1):
        """
        :Usage select_content_area_folder_context_menu('My Content', 'Properties', folder_path='P116')
        @author:Aftab_Alam_Khan
        """
        if folder_path != None:
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        retun_obj=Wf_Mainpage.get_domain_folder_item(self, item_name, item_name_index=item_name_index)
        if click_option=='left_click':
            core_utils.left_click(self, retun_obj)
        if click_option=='right_click':
            core_utils.right_click(self, retun_obj)
            Wf_Mainpage.select_context_menu_item(self, context_menu_item_path)
        elif click_option=='double_click':
            core_utils.double_click(self, retun_obj)
        
    def select_repository_folder_item_context_menu(self, item_name, context_menu_item_path=None, folder_path=None, click_option='right_click', item_name_index=1):                                                            
        """
        :Usage select_repository_folder_item_context_menu('Report1.fex', 'Edit', folder_path='P116')
        @author:Aftab_Alam_Khan
        """
        if folder_path != None:
            Wf_Mainpage.expand_repository_folders(self, folder_path)
            time.sleep(2)
        retun_obj=Wf_Mainpage.get_domain_folder_item(self, item_name, item_name_index=item_name_index)
        if click_option=='left_click':
            core_utils.left_click(self, retun_obj)
        if click_option=='right_click':
            core_utils.right_click(self, retun_obj)
            Wf_Mainpage.select_context_menu_item(self, context_menu_item_path)
        elif click_option=='double_click':
            core_utils.double_click(self, retun_obj)
        
    def get_domain_folder_item(self, item_name, item_name_index=1):
        """
        Descriptions : This method used to find domain folder items and get it object. 
        example usage :  get_domain_folder_item('Retail Samples->Reports->Auto Link Targets', 'Act_fex')
        """
        scroll_css="div[class*='files-box-files']"
        item_not_found_error="[{0}] file not found in content area"
        items_css="div.files-box-files .fbx-block.fbx-column"
#         items_label_css="{0} div.ibx-label-text".format(items_css)
        item_obj_list=self.driver.find_elements_by_css_selector(items_css)
#         item_label_obj_list=self.driver.find_elements_by_css_selector(items_label_css)
        found_item_index = [index for index, item_obj in enumerate(item_obj_list) if item_obj.text.strip() == item_name]
        scroll_obj=self.driver.find_element_by_css_selector(scroll_css)
        scroll_bottom_cord = core_utils.get_web_element_coordinate(self, scroll_obj, 'bottom_middle')
        core_utils.python_move_to_element(self, scroll_obj)
        time.sleep(1)
        scroll_y = scroll_bottom_cord['y']
        if found_item_index != [] :
            item_index = found_item_index[item_name_index-1]
            item_obj=item_obj_list[item_index]
            while True :
                item_bootm_cord = core_utils.get_web_element_coordinate(self, item_obj, 'bottom_middle')
                item_bottom_y = item_bootm_cord['y']
                if item_bottom_y > scroll_y:
                    util_method.mouse_scroll(self, 'down', 1, option='uiautomation', pause=2)
                else :
                    break
            return item_obj
        else:
            raise FileNotFoundError(item_not_found_error.format(item_name))
        
    def double_click_on_content_area_items(self,item_name,folder_path=None,item_name_index=1):
        """
        Descriptions:This method is used to double click on content area items
        Example usage: double_click_on_content_area_items("Page 1")
        double_click_on_content_area_items("Page 1","P292_S10032->G435267",2)
        @param item_name_index = Need to be integer value ,if two items having same name.
        """
        folder_path and self.expand_repository_folders(folder_path)
        retun_obj=Wf_Mainpage.get_domain_folder_item(self, item_name, item_name_index=item_name_index)
        core_utils.double_click(self, retun_obj)
            
    def verify_content_area_folder_item(self, item_list, msg, content_option='item'):
        """
        Descriptions : This method used to verify content area items and folders
        content_option = 'item' or 'folder'
        usage : verify_content_area_folder_item(['Act_fex'],"Step02: Verify content area items")
        @Kiruthika
        """
        if content_option=='item':
            items_css="div[class*='files-box-files'] div[class*='file-item-shown'] div.ibx-label-text"
        elif content_option=='folder':
            items_css="div[class*='files-box-files'] div[class*='folder-item-shown']"
        items_label_elems = self.driver.find_elements_by_css_selector(items_css)
        actual_items_list = [el.text for el in items_label_elems]
        status=False
        for item in item_list:
            if item in actual_items_list:
                status=True
            else:
                status=False
                break
        util_method.asequal(self, True, status, msg+"{0} last verified item".format(item))
    
    def select_context_menu_item(self, menu_item_path, expire_time=90, pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']", row_css=" div[data-ibx-type*='MenuItem'] div[class='ibx-label-text']", click_type='left',element_location='middle',xoffset=0):
        """
        :Usage select_context_menu_item('Properties')
        @author:Aftab_Alam_Khan
        """
        pop_up_css=pop_up_css
        popup_menu_rows=pop_up_css+' '+row_css
        popup_menu_list=menu_item_path.split('->')
        for item in popup_menu_list:
            util_method.synchronize_with_number_of_element(self, pop_up_css, 1, expire_time=expire_time)            
            popup_items = self.driver.find_elements_by_css_selector(popup_menu_rows)
            return_obj=j_script.find_elements_by_text(self, popup_items, item)
            popup_ele = self.driver.find_element_by_css_selector(pop_up_css)
            j_script.scrollIntoView(self, return_obj[0])
            core_utils.python_move_to_element(self, popup_ele, element_location='top_middle', yoffset=12)
            if len(return_obj)==0:
                raise KeyError("[{0}] item not listed under the context Menu.".format(item))
            if click_type == 'left':
                core_utils.python_left_click(self, return_obj[0],element_location=element_location,xoffset=xoffset)
            else:
                core_utils.python_move_to_element(self, return_obj[0],element_location=element_location,xoffset=xoffset)
    
    def verify_context_menu_item(self, expected_context_menu_item_list, msg='Step X', comparision_type='asequal', pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']", row_css=" div[data-ibx-type*='MenuItem']"):
        '''
        This function will verify only the context menu list. So before calling this function make sure the context menu is visible.
        '''
        count = 1
        pop_up_css=pop_up_css
        popup_menu_rows=pop_up_css+' '+row_css
        util_method.synchronize_until_element_is_visible(self, pop_up_css, 60)
        popup_items = util_method.validate_and_get_webdriver_objects(self, popup_menu_rows, 'Context menu')
        actual_context_menu_item_list=[el.text.strip().replace('\n',' ') for el in popup_items  if bool(re.match('\S+', el.text.strip()))]
        if comparision_type.lower()=='asequal':
            custom_msg=msg + " : Verify {0} items in the visible context menu.".format(expected_context_menu_item_list)
            util_method.as_List_equal(self, expected_context_menu_item_list, actual_context_menu_item_list, custom_msg)
        elif comparision_type.lower()=='asnotin':
            for item in expected_context_menu_item_list:
                custom_msg=msg + ".{0} : Verify [{1}] item not in the visible context menu.".format(count, item)
                count+=1
                util_method.as_notin(self, item, actual_context_menu_item_list, custom_msg)
        elif comparision_type.lower()=='asin':
            for item in expected_context_menu_item_list:
                custom_msg=msg + ".{0} : Verify [{1}] item in the visible context menu.".format(count, item)
                count+=1
                util_method.asin(self, item, actual_context_menu_item_list, custom_msg)
        
    def verify_context_menu_item_checked_unchecked(self, expected_context_menu_item_list, status_type, msg, comparision_type='asequal', pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']", row_css=" div[data-ibx-type*='MenuItem']"):
        '''
        This function will verify the context menu list is checked or unchecked. So before calling this function make sure the context menu is visible.
        '''
        checked_list = []
        unchecked_list = []
        pop_up_css=pop_up_css
        popup_menu_rows=pop_up_css+' '+row_css
        util_method.synchronize_until_element_is_visible(self, pop_up_css, self.home_page_medium_timesleep)
        popup_items = util_method.validate_and_get_webdriver_objects(self, popup_menu_rows, 'Context menu')
        for opt_name in popup_items:
            checked_status = util_method.validate_and_get_webdriver_object(self, "[class*='ibx-marker-radio']", 'checked', parent_object=opt_name)
            class_data = util_method.get_element_attribute(self, checked_status, 'class')
            if 'ibx-marker-radio-check' in class_data:
                before_value = j_script.get_element_before_style_properties(self, checked_status, 'content').replace('"', '')
                print('\ue98e'.encode('utf-8'), before_value.encode('utf-8'))
                if '\ue98e'.encode('utf-8') == before_value.encode('utf-8'):
                    checked_list.append(opt_name.text.strip().replace('\n',' '))
            else:
                unchecked_list.append(opt_name.text.strip().replace('\n',' '))
        actual_context_menu_item_list = checked_list if status_type == 'check' else unchecked_list
        util_method.verify_list_values(self, expected_context_menu_item_list, actual_context_menu_item_list, msg, assert_type=comparision_type)
        
    def verify_context_submenu_item(self, menu_item_path, expected_context_menu_item_list, msg='Step X', comparision_type='asequal', close_context_menu_css=None, expire_time=90):
        '''
        This funciton will close contex menu
        @param menu_item_path: 'Edit->Run'
        @param expected_context_menu_item_list: ['Edit','Run']
        @param msg: 'step 9'
        @param comparision_type: 'asin','asnotin' or 'asequal'
        @param close_context_menu_css: '.banner-group-spacer'
        @param expire_time: 90
        :usage verify_context_submenu_item('Edit->Run', ['Edit','Run'], msg='step 9', comparision_type='asin', close_context_menu_css='.banner-group-spacer', expire_time=90)
        '''
        Wf_Mainpage.select_context_menu_item(self, menu_item_path, expire_time)
        util_method.synchronize_with_number_of_element(self, Main_Page.any_context_menu_css, 1, expire_time=expire_time)
        Wf_Mainpage.verify_context_menu_item(self, expected_context_menu_item_list, msg=msg, comparision_type=comparision_type)
        Wf_Mainpage.close_contex_menu(self, click_location_css=close_context_menu_css)
    
    def close_contex_menu(self, click_location_css=None):
        '''
        This funciton will close contex menu
        :usage close_contex_menu(click_location_css='.banner-group-spacer')
        '''
        if click_location_css != None:
            core_utils.left_click(self, util_method.validate_and_get_webdriver_object(self, click_location_css, 'click other element'))
        else:
            Main_Page.close_contex_menu(self)
     
    def verify_left_panel(self, content_list, msg, active="Content", comparision_type='asequal'):
        '''
        This function will verify left panel and its selected option
        active: to verify which option is selected
        content_list=['Content', 'Portals', 'Favorites', 'Mobile Favorites']
        :usage verify_left_panel(content_list, "Step02: verify left panel")
        @Kiruthika
        '''
        count=1
        left_panel_css ="div.left-main-panel-button-size:not([style*='none']) .left-main-panel-content .ibx-label-text"
        left_panel_elems =self.driver.find_elements_by_css_selector(left_panel_css)
        actual_list = [el.text for el in left_panel_elems if el.text!='']
        if comparision_type.lower()=='asequal':
            util_method.as_List_equal(self, content_list, actual_list, msg)
        elif comparision_type.lower()=='asnotin':
            for item in content_list:
                custom_msg=msg + ".{0}: Verify {1} items is not in the visible context menu.".format(count, item)
                count+=1
                util_method.as_notin(self, item, actual_list, custom_msg)
        elif comparision_type.lower()=='asin':
            for item in content_list:
                custom_msg=msg + ".{0}: Verify {1} items is in the visible context menu.".format(count, item)
                count+=1
                util_method.asin(self, item, actual_list, custom_msg)
        if active!='':    
            step_number = re.search(r'\d+', msg).group()
            active_content_css = ".main-panel .left-main-panel-content-button-active .left-main-panel-content .ibx-label-text"
            active_content_elems = self.driver.find_elements_by_css_selector(active_content_css)
            active_content_text = [el.text for el in active_content_elems if el.text!='']
            util_method.as_List_equal(self, [active],active_content_text, "Step {0}.a: {1} selected as default".format(step_number, active))
    
    def select_left_panel(self, option_name):
        '''
        This function will select left panel option form main home page.
        @author:Aftab_Alam_Khan
        '''
        left_panel_option_dict={'content':'content', 'portals':'portal', 'favorites':'favorites', 'mobilefavorites':'mobile-favorites', 'askwebfocus': 'askwebfocus'}
        actual_option_name=left_panel_option_dict[option_name.replace(' ','').lower()]
        left_panel_css=".main-panel .left-main-panel [class*='left-main-panel-{0}-button'] div[class*='image'] ".format(actual_option_name)
        temp_obj= self.driver.find_element_by_css_selector(left_panel_css)
        option_name_obj=temp_obj.find_element_by_css_selector(".ibx-label-icon")
        core_utils.left_click(self, option_name_obj)
    
    def verify_property_dialog_location(self, step_number):
        '''
        This function will check property dialog create a room in right side of New HOme page.
        :Usage verify_property_dialog_location('9')
        @author:Aftab_Alam_Khan
        '''
        explore_content_css='.explore-box'
        property_dialog_css='.properties-page.propPage'
        content_page_css='.content-box.ibx-widget'
        '''explore-area'''
        explore_content_temp_obj=self.driver.find_element_by_css_selector(explore_content_css)
        explore_content_obj_middle_right_location=core_utils.get_web_element_coordinate(self, explore_content_temp_obj, element_location='middle_right')
        explore_content_obj_top_middle_location=core_utils.get_web_element_coordinate(self, explore_content_temp_obj, element_location='top_middle')
        explore_content_obj_bottom_middle_location=core_utils.get_web_element_coordinate(self, explore_content_temp_obj, element_location='bottom_middle')
        '''content-area'''
        content_page_temp_obj=self.driver.find_element_by_css_selector(content_page_css)
        content_page_middle_right_location=core_utils.get_web_element_coordinate(self, content_page_temp_obj, element_location='middle_right')
        '''property-area'''
        property_dialog_temp_obj=self.driver.find_element_by_css_selector(property_dialog_css)
        property_dialog_middle_right_location=core_utils.get_web_element_coordinate(self, property_dialog_temp_obj, element_location='middle_right')
        property_dialog_middle_left_location=core_utils.get_web_element_coordinate(self, property_dialog_temp_obj, element_location='middle_left')
        property_dialog_top_middle_location=core_utils.get_web_element_coordinate(self, property_dialog_temp_obj, element_location='top_middle')
        property_dialog_bottom_middle_location=core_utils.get_web_element_coordinate(self, property_dialog_temp_obj, element_location='bottom_middle')
        '''check-point'''
        if int(explore_content_obj_middle_right_location['x']) == int(property_dialog_middle_right_location['x']):
            if int(content_page_middle_right_location['x']) == int(property_dialog_middle_left_location['x']):
                if int(explore_content_obj_top_middle_location['y']) ==  int(property_dialog_top_middle_location['y']):
                    if int(explore_content_obj_bottom_middle_location['y']) == int(property_dialog_bottom_middle_location['y']):
                        status=True
                    else:
                        status=False
                        print("int(explore_content_obj_bottom_middle_location) == int(property_dialog_bottom_middle_location)",int(explore_content_obj_bottom_middle_location),int(property_dialog_bottom_middle_location))
                else:
                    status=False
                    print("int(explore_content_obj_top_middle_location['y']) ==  int(property_dialog_top_middle_location['y'])",int(explore_content_obj_top_middle_location['y']),int(property_dialog_top_middle_location['y']))
            else:
                status=False
                print("int(content_page_middle_right_location['x']) == int(property_dialog_middle_left_location['x'])",int(content_page_middle_right_location['x']),int(property_dialog_middle_left_location['x']))
        else:
            status=False
            print("int(explore_content_obj_middle_right_location['x']) == int(property_dialog_middle_right_location['x'])",int(explore_content_obj_middle_right_location['x']),int(property_dialog_middle_right_location['x']))
        util_method.asequal(self, status, True, "Step "+str(step_number)+": Properties is displayed on right side and the WebFOCUS Explorer folds its content to make room.")             
    
    def get_property_dialog_rows_object(self, tab_name, property_name, step_number='X'):
        '''
        This function will return the property window rows object.
        :usage get_property_dialog_rows_object('Path', step_number='9')
        @author:Aftab_Alam_Khan
        '''
        properties_row_css=".propPage .tpg-selected [class^='properties-{0}']:not([style*='none']) [class*='properties-page-row']".format(tab_name.lower().replace(' ', '-'))
        properties_row_elems = util_method.validate_and_get_webdriver_objects(self, properties_row_css, tab_name+' Tab rows')
        try:
            for item in properties_row_elems:
                if property_name in item.text.strip():
                    return (item)
            raise IndexError("Step {0}: '{1}' property name not exist in property dialog in {2} tab.".format(step_number, property_name, tab_name))
        except:
            raise IndexError("Step {0}: '{1}' property name not exist in property dialog under {2} tab.".format(step_number, property_name, tab_name)) 
    
    def edit_property_dialog_value(self, property_name, property_type, property_value, typing_speed=0.5, tab_name='General'):
        '''
        This function is used to check verify property window.
        
        @param property_name: 'Title'
        @param property_type: 'text_value'
        @param property_value: 'Faves'
        @param typing_speed: 1
        @param tab_name: 'Advanced'
        :usage edit_property_dialog_value('Title', 'text_value', 'Faves', typing_speed=1, tab_name='Advanced')
        @author:Aftab_Alam_Khan
        '''
        tab_css="[class*='properties-{0}']".format(tab_name.lower())
        if property_type == 'tab_value':
            Wf_Mainpage.select_property_tab_value(self, property_value)
            tab_css="[class*='properties-{0}']".format(property_name.lower())
        else:
            properties_row_text_input_css="{0} [data-ibx-type*='ibxText'] input".format(tab_css)
            properties_row_text_textarea_css="{0} [data-ibx-type*='ibxText'] textarea".format(tab_css)
            radio_button_css="{0} [data-ibx-type='ibxRadioButtonSimple']".format(tab_css)
            properties_row_button_css="{0} [data-ibx-type='ibxButton']".format(tab_css)
            checkbox_css = ".ibx-check-box-simple-marker"
            rows_obj=Wf_Mainpage.get_property_dialog_rows_object(self, tab_name, property_name)
            if property_type == 'text_value':
                input_text_elem=rows_obj.find_element_by_css_selector(properties_row_text_input_css)
                util_method.set_text_to_textbox_using_keybord(self, property_value, text_box_elem=input_text_elem, type_speed=typing_speed)
            elif property_type == 'text_area':
                text_area_elem=rows_obj.find_element_by_css_selector(properties_row_text_textarea_css)
                util_method.set_text_to_textbox_using_keybord(self, property_value, text_box_elem=text_area_elem, type_speed=typing_speed)
            elif property_type == 'text':
                text_elem=rows_obj.find_element_by_css_selector(properties_row_button_css)
                core_utils.left_click(self, text_elem)
            elif property_type == 'radiobutton_value':
                radio_button_elems=rows_obj.find_elements_by_css_selector(radio_button_css)
                radio_list_elem=j_script.get_elements_text(self, radio_button_elems)
                radio_input_value=radio_button_elems[radio_list_elem.index(property_value)].find_element_by_css_selector("input")
                core_utils.left_click(self, radio_input_value)
            elif property_type == 'checkbox':
                checkbox_elem=rows_obj.find_element_by_css_selector(checkbox_css)
                element_class_attribute = util_method.get_element_attribute(self, checkbox_elem, 'class')
                status_value = 'check' if 'ibx-check-box-simple-marker-check' in element_class_attribute else 'uncheck'
                if property_value == status_value:
                    raise LookupError("'{0}' {1} already {2}.".format(property_name, property_type, property_value))
                core_utils.left_click(self, checkbox_elem)
        
    def verify_property_dialog_value(self, property_name, property_type, msg, property_value=None, user_name=None, tab_name='General'):
        '''
        This function is used to check verify property window.
        :usage verify_property_dialog_value('Title', 'text_value', "step 9: Verify", property_value='P242', user_name='autodevuser56'0)
        @author:Aftab_Alam_Khan
        '''
        tab_css="[class*='properties-{0}']".format(tab_name.lower())
        if property_type == 'tab_value':
            Wf_Mainpage.verify_property_tab_value(self, property_value, msg)
        else:
            step_number = re.search(r'\d+', msg).group()
            properties_row_text_input_css="input"
            properties_row_text_textarea_css="textarea"
            if property_name in ['Modified', 'Accessed']:
                properties_row_text_css="{0} [class*='properties'][class*='{1}']".format(tab_css, property_name)
            else:
                properties_row_text_css="{0} [class*='properties'][class*='{1}']".format(tab_css, property_name.lower())
            radio_button_css="{0} [data-ibx-type='ibxRadioButtonSimple']".format(tab_css)
            rows_obj=Wf_Mainpage.get_property_dialog_rows_object(self, tab_name, property_name, step_number)
            if property_type == 'text_value':
                actual_value=rows_obj.find_element_by_css_selector(properties_row_text_input_css).get_attribute('value')
            elif property_type == 'text_area':
                actual_value=rows_obj.find_element_by_css_selector(properties_row_text_textarea_css).get_attribute('value')
            elif property_type == 'text':
                actual_value_temp=rows_obj.find_element_by_css_selector(properties_row_text_css).text.strip()
                if property_name in ['Created', 'Modified', 'Accessed']:
                    property_value=True
                    actual_return_value=Wf_Mainpage.verify_property_created_modified_accessed_time(self, user_name, step_number, actual_value_temp, expected_list=property_value)
                    actual_value=actual_return_value
                else:
                    actual_value=actual_value_temp
            elif property_type == 'radiobutton_value':
                radio_button_elems=rows_obj.find_elements_by_css_selector(radio_button_css)
                radio_list_elem=j_script.get_elements_text(self, radio_button_elems)
                status_value=radio_button_elems[radio_list_elem.index(property_value)].find_element_by_css_selector("input").is_selected()
                option_dict={}
                option_dict[str(property_value)]=status_value
                if property_value=='Yes':
                    property_reverse_value='No'
                elif property_value=='No':
                    property_reverse_value='Yes'
                status_reverse_value=radio_button_elems[radio_list_elem.index(property_reverse_value)].find_element_by_css_selector("input").is_selected()
                option_dict[str(property_reverse_value)]=status_reverse_value
                if property_value=='Yes':
                    if option_dict=={'Yes': True, 'No': False}:
                        actual_value='Yes'
                    else:
                        actual_value='No'
                elif property_value=='No':
                    if option_dict=={'No': True, 'Yes': False}:
                        actual_value='No'
                    else:
                        actual_value='Yes'
            expected_value=property_value
            util_method.asequal(self, expected_value, actual_value, msg)
    
    def verify_property_dialog_enable_disable(self, property_name, property_type, property_value, msg, tab_name='General'):
        '''
        This function is used to check verify property window.
        :usage verify_property_dialog_enable_disable('Title', 'text_value', 'P242', "step 9: Verify")
        @author:Aftab_Alam_Khan
        '''
        tab_css="[class*='properties-{0}']".format(tab_name.lower())
        step_number = re.search(r'\d+', msg).group()
        item_disable_css=".ibx-widget-disabled"
        properties_row_text_input_css="{0} [data-ibx-type*='ibxText']{1} input".format(tab_css, item_disable_css)
        properties_row_text_input_readonly_css="{0} [data-ibx-type*='ibxText'] input".format(tab_css)
        properties_row_text_textarea_css="{0} [data-ibx-type*='ibxText']{1} textarea".format(tab_css, item_disable_css)
        properties_row_button_css="{0} [data-ibx-type='ibxButton']{1}".format(tab_css, item_disable_css)
        radio_button_css="{0} [data-ibx-type='ibxRadioButtonSimple']{1}".format(tab_css, item_disable_css)
        properties_dialog_checkbox_css="{0} [role='checkbox']{1}".format(tab_css, item_disable_css)
        rows_obj=Wf_Mainpage.get_property_dialog_rows_object(self, tab_name, property_name, step_number)
        if property_type == 'text_value':
            if property_name=='Path':
                    try:
                        temp_status=rows_obj.find_element_by_css_selector(properties_row_text_input_readonly_css).get_attribute('value')
                        temp_obj=rows_obj.find_element_by_css_selector(properties_row_text_input_readonly_css)
                        returned_obj=j_script.get_element_all_attributes(self, temp_obj)
                        if 'readonly' in [obj_text.strip() for obj_text in returned_obj.keys()] and temp_status == property_value:
                            status=temp_status
                        else:
                            status=False
                    except NoSuchElementException:
                        status=False
            else:
                try:
                    temp_status=rows_obj.find_element_by_css_selector(properties_row_text_input_css).get_attribute('value')
                    status=temp_status
                    if property_name=='Name':
                        temp_obj=rows_obj.find_element_by_css_selector(properties_row_button_css)
                        returned_obj=j_script.get_element_all_attributes(self, temp_obj)
                        if item_disable_css.replace('.','') in returned_obj['class'] and temp_status == property_value:
                            status=temp_status
                        else:
                            status=False
                except NoSuchElementException:
                    status=False
        elif property_type == 'text_area':
            try:
                status=rows_obj.find_element_by_css_selector(properties_row_text_textarea_css).get_attribute('value')
            except NoSuchElementException:
                status=False
        elif property_type == 'text':
            if property_name=='Language':
                try:
                    status=rows_obj.find_element_by_css_selector(properties_row_button_css).text.strip()
                except NoSuchElementException:
                    status=False
        elif property_type == 'radiobutton_value':
            radio_button_elems=rows_obj.find_elements_by_css_selector(radio_button_css)
            radio_list_elem=j_script.get_elements_text(self, radio_button_elems)
            try:
                temp_index=radio_list_elem[0]
                del temp_index
                status_value=radio_button_elems[radio_list_elem.index(property_value)].find_element_by_css_selector("input").is_selected()
                option_dict={}
                option_dict[str(property_value)]=status_value
                if property_value=='Yes':
                    property_reverse_value='No'
                elif property_value=='No':
                    property_reverse_value='Yes'
                status_reverse_value=radio_button_elems[radio_list_elem.index(property_reverse_value)].find_element_by_css_selector("input").is_selected()
                option_dict[str(property_reverse_value)]=status_reverse_value
                if property_value=='Yes':
                    if option_dict=={'Yes': True, 'No': False}:
                        status='Yes'
                    else:
                        status='No'
                elif property_value=='No':
                    if option_dict=={'No': True, 'Yes': False}:
                        status='No'
                    else:
                        status='Yes'
            except IndexError:
                status=False
        elif property_type == 'check_box':
            try:
                status=rows_obj.find_element_by_css_selector(properties_dialog_checkbox_css).text.strip()
            except NoSuchElementException:
                status=False
        util_method.asequal(self, status, property_value, msg)
    
    def verify_label_in_property_dialog(self, tab_name, label_name, step_number, checkbox=None):
        '''
        This function will verify property dialog label.
        
        @param  tab_name: 'Advanced'
        @param label_name: 'Title'
        @param step_number: '9'
        @param checkbox: 'enable' or 'disable'   #Optional
        @Usage verify_label_in_property_dialog('Advanced', 'Title', '9', checkbox='enable')
        @author: Aftab_Alam_Khan
        '''
        rows_obj=Wf_Mainpage.get_property_dialog_rows_object(self, tab_name, label_name, step_number)
        label_css = "[data-ibx-type='ibxLabel'] .ibx-label-text"
        checkbox_css = "[data-ibx-type='ibxCheckBoxSimple']"
        checkbox_label_css= ".ibx-label-text"
        if checkbox != None:
            if checkbox not in ['enable', 'disable']:
                raise IndexError("Please pass checkbox value 'enable' or 'disable'.")
            checkbox_elem = util_method.validate_and_get_webdriver_object(self, checkbox_css, label_name, rows_obj)
            checkbox_elem_class_attributes = util_method.get_element_attribute(self, checkbox_elem, 'class')
            if checkbox == 'enable':
                msg = "Step {0}.a: Verify '{1}' check-box is Enable.".format(str(step_number), label_name)
                util_method.as_notin(self, 'ibx-widget-disabled', checkbox_elem_class_attributes, msg)
            else:
                msg = "Step {0}.a: Verify '{1}' check-box is Enable.".format(str(step_number), label_name)
                util_method.asin(self, 'ibx-widget-disabled', checkbox_elem_class_attributes, msg)
            dis_msg = "Step {0}.b: Verify '{1}' check-box label.".format(str(step_number), label_name)
            checkbox_actual_label_text = util_method.validate_and_get_webdriver_object(self, checkbox_label_css, label_name, checkbox_elem).text.strip()
            util_method.asequal(self, label_name, checkbox_actual_label_text, dis_msg)
        else:
            actual_label_text = util_method.validate_and_get_webdriver_object(self, label_css, label_name, rows_obj).text.strip()
            dis_msg = "Step {0}: Verify '{1}' label.".format(str(step_number), label_name)
            util_method.asequal(self, label_name, actual_label_text, dis_msg)
    
    def select_property_dialog_save_cancel_button(self, button_name):
        """
        This function click save or cancel button in property dialog.
        @param button_name: 'Save' or 'Cancle'
        :Usage select_property_dialog_save_cancel_button('Save')
        @author:Aftab_Alam_Khan
        """
        properties_dialog_save_cancel_css=".properties-page-footer .properties-general-{0}-button"
        button_name_dict={'Save':'ok', 'Cancel':'cancel'}
        button_obj=self.driver.find_element_by_css_selector(properties_dialog_save_cancel_css.format(button_name_dict[button_name]))
        core_utils.left_click(self, button_obj)
        
    def verify_property_dialog_save_cancel_button_enable_disable(self, button_name, button_status, msg):
        """
        This function is verify save or cancel button is enable or disable in property dialog.
        :Usage verify_save_cancel_button_enable_disable('Save', 'enable', "Step 9: Verify")
        @author:Aftab_Alam_Khan
        """
        properties_dialog_save_cancel_css=".properties-page-footer .properties-general-{0}-button"
        item_disable_css=".ibx-widget-disabled"
        button_name_dict={'Save':'ok', 'Cancel':'cancel'}
        try:
            temp_status=self.driver.find_element_by_css_selector(properties_dialog_save_cancel_css.format(button_name_dict[button_name])).text.strip()
            temp_obj=self.driver.find_element_by_css_selector(properties_dialog_save_cancel_css.format(button_name_dict[button_name]))
            returned_obj=j_script.get_element_all_attributes(self, temp_obj)
            if item_disable_css.replace('.','') in returned_obj['class'] and temp_status == button_name:
                status='disable'
            else:
                status='enable'
        except NoSuchElementException:
            status=False
        util_method.asequal(self, button_status, status, msg)
    
    def verify_created_modified_accessed_time_formate(self, expected, user_name, msg):
        '''
        This function will verify date format for Created, Modified, Accessed in Property Dialog.
        Note:'E[D|S]T' not supported in IE browser. Function updated for IE
        @author:Aftab_Alam_Khan
        '''
        if Global_variables.browser_name in ['ie']:
            status=bool(re.match('[a-zA-Z]*day, [a-zA-Z]* \d{1,2}, \d\d\d\d \d{1,2}:\d\d:\d\d [A|P]M by '+user_name+'$', expected))
        else:
            status=bool(re.match('[a-zA-Z]*day, [a-zA-Z]* \d{1,2}, \d\d\d\d \d{1,2}:\d\d:\d\d [A|P]M E[D|S]T by '+user_name+'$', expected))
        util_method.asequal(self, True, status, msg)
        
    def get_property_created_modified_accessed_time(self, time_property_name, msg, tab_name='General'):
        '''
        This function will return date_time for 'Created', 'Modified' and 'Accessed'.
        :usage  get_property_created_modified_accessed_time('Created', "Step 9: verify")
        @author:Aftab_Alam_Khan
        '''
        tab_css=".properties-{0}-pane-tab".format(tab_name.lower())
        if time_property_name=='Created':
            properties_row_text_css="{0} [class*='properties'][class*='{1}']".format(tab_css, time_property_name.lower())
        else:
            properties_row_text_css="{0} [class*='properties'][class*='{1}']".format(tab_css, time_property_name)
        step_number = re.search(r'\d+', msg).group()
        rows_obj=Wf_Mainpage.get_property_dialog_rows_object(self, tab_name, time_property_name, step_number)
        row_text_obj = rows_obj.find_element_by_css_selector(properties_row_text_css)
        current_text=util_method.get_attribute_value(self, row_text_obj, 'dom_visible_text')
        return (current_text['dom_visible_text'])
    
    def verify_property_created_modified_accessed_time(self, user_name, step_number, actual_text, expected_list=None):
        '''
        This function will check date_time for 'Created', 'Modified' and 'Accessed'.
        :param actual_text : "Thursday, May 24, 2018 9:17:03 AM EDT by autodevuser43" 
        :param expected_list : ["Thursday,","May", "24,", "2018", "9:17:03", "AM", "EDT", "by", "autodevuser43"]
        :usage verify_property_created_modified_accessed_time(self, 'admin', '9', actual_text, expected_list=expected_list)
        @author:Aftab_Alam_Khan
        '''
        if expected_list==None:
            expected_list_output=time.strftime("%A, %B %d, %Y %p %Z by {0}".format(user_name), time.localtime()).replace('Eastern Daylight Time','EDT').split(' ')
        else:
            expected_list_output=expected_list
        temp_actual_output=actual_text.split(' ')
        for value in temp_actual_output:
            if ':' in value:
                temp_index_value=temp_actual_output.index(value)
                actual_time=value
                break
        temp_actual_output.remove(temp_actual_output[temp_index_value])
        temp_start_time=Global_variables.current_time
        if len(re.match('X(\d+):',temp_start_time).group(1)) > 1:
            if re.match('X(\d+):',temp_start_time).group(1)[0]=='0':
                start_time=temp_start_time.replace('X0','X').replace('X','')
            else:
                start_time=temp_start_time.replace('X','')
        temp_end_time=time.strftime("X%H:%M:%S", time.localtime())
        if len(re.match('X(\d+):',temp_end_time).group(1)) > 1:
            if re.match('X(\d+):',temp_end_time).group(1)[0]=='0':
                end_time=temp_end_time.replace('X0','X').replace('X','')
            else:
                end_time=temp_end_time.replace('X','') 
        if start_time < actual_time < end_time:
            if  expected_list_output == temp_actual_output:
                util_method.as_List_equal(self, expected_list_output, temp_actual_output, "Step {}.a: Verify date_time check point".format(step_number))
                status=True
            else:
                print(expected_list_output, '!=', temp_actual_output)
                status=False
        else:
            print(start_time, '<', actual_time, '<', end_time)
            status=False
        return (status)
        
    def verify_property_tab_value(self, expected_list, msg):
        '''
        This function will check the list of property tab values.
        :Usage verify_property_tab_value(['General', 'Advanced'], "Step 9: verify")
        @author:Aftab_Alam_Khan
        '''
        properties_tab_css=".properties-tab-pane [data-ibx-type$='TabGroup'] [data-ibx-type$='Button'][role='tab']"
        properties_tab_label_css="{0} .ibx-label-text".format(properties_tab_css)
        elem_obj=self.driver.find_elements_by_css_selector(properties_tab_label_css)
        returned_obj=j_script.get_elements_text(self, elem_obj)
        actual_list=[elem.strip() for elem in returned_obj]
        util_method.as_List_equal(self, actual_list, expected_list, msg)
    
    def verify_selected_tab_in_property_dialog(self, tab_name, msg):
        '''
        This function will check the list of property tab values.
        :Usage verify_property_tab_value('General', "Step 9: verify")
        @author:Aftab_Alam_Khan
        '''
        properties_tab_css=".properties-tab-pane [data-ibx-type$='TabGroup'] [data-ibx-type$='Button'][role='tab']"
        properties_selcected_tab_css="{0}.checked .ibx-label-text".format(properties_tab_css)
        sected_tab_value=self.driver.find_element_by_css_selector(properties_selcected_tab_css).text.strip()
        util_method.asequal(self, tab_name, sected_tab_value, msg)
        
    def select_property_tab_value(self, property_value):
        '''
        This function will check the list of property tab values.
        @param property_value: 'General' 
        :usage select_property_tab_value('Advanced')
        @author:Aftab_Alam_Khan
        '''
        properties_tab_css=".properties-tab-pane [data-ibx-type$='TabGroup'] [data-ibx-type$='Button'][role='tab']"
        try:
            elem_obj=self.driver.find_elements_by_css_selector("{0}  .ibx-label-text".format(properties_tab_css))
        except NoSuchElementException:
            raise LookupError('Tab list is not displayed under property dialog, Unable to find {} tab.'.format(property_value))
        elem_index_value=j_script.find_element_index_by_text(self, elem_obj, property_value)
        if elem_index_value == None:
            raise IndexError('{0} tab is not exist under property dialog.'.format(property_value))
        core_utils.left_click(self, elem_obj[elem_index_value])
        util_method.synchronize_with_number_of_element(self, "{0}.checked".format(properties_tab_css), 1, 36)
    
    def close_property_dialog(self):
        '''
        This function will close property dialog.
        :usage close_property_dialog()
        @author:Aftab_Alam_Khan
        ''' 
        properties_close_button_css=".properties-page.propPage .properties-page-close-button [class*='close']"
        try:
            elem=self.driver.find_element_by_css_selector(properties_close_button_css)
        except NoSuchElementException:
            raise LookupError("Close 'x' button is not displayed under property dialog.")
        core_utils.left_click(self, elem)
    
    def change_password(self, old_pass, new_pass, button='ok', msg="StepX:"):
        '''
        This function will change password in homepage
        :usage change_password('', 'new')
        @author:Kiruthika
        '''
        old_password_css = "[class*='dialog-main-box'] #sdtxtOldPassword>input"
        new_password_css = "[class*='dialog-main-box'] #sdtxtNewPassword>input"
        confirm_new_password_css = "[class*='dialog-main-box'] #sdtxtConfirmNewPassword>input"
        old_password_elem = self.driver.find_element_by_css_selector(old_password_css)
        new_password_elem = self.driver.find_element_by_css_selector(new_password_css)
        confirm_new_password_elem = self.driver.find_element_by_css_selector(confirm_new_password_css)
        util_method.set_text_to_textbox_using_keybord(self, old_pass, old_password_css)
        if old_pass=='':
            core_utils.left_click(self, old_password_elem)
        core_utils.left_click(self, old_password_elem)
        util_method.set_text_to_textbox_using_keybord(self, new_pass, new_password_css)
        if new_pass!='':
            core_utils.left_click(self, new_password_elem)
        util_method.set_text_to_textbox_using_keybord(self, new_pass, confirm_new_password_css)
        if new_pass!='':
            core_utils.left_click(self, confirm_new_password_elem)
        if button=='ok':
            button_css = "[class*='dialog-main-box'] [class*='dialog-ok-button']"
        elif button == 'cancel':
            button_css = "[class*='dialog-main-box'] [class*='dialog-cancel-button']"
        util_method.verify_object_visible(self, old_password_elem, False, "StepX: Verify Change Password dialog disappears")
        button_elem = self.driver.find_element_by_css_selector(button_css)
        core_utils.left_click(self, button_elem)
        util_method.verify_notify_popup(self, notify_text="Your password has been changed", msg=msg)
        
    def verify_grid_view(self, item1, item2, msg, item_type, grid_folder_distance=20):
        '''
        This function will verify the grid view by  verifying
        1. grid class visibility 
        2. list class invisibility
        3. y position of item1 top right and item2 top left is equal
        4. x position of item1 top right and item2 top left difference in the range of (20,22)
        :arg item_type = 'folder_item' or 'file_item', grid_folder_distance=20 expected distance between item1 and item2 filders
        :usage verify_grid_view("My Content", "Charts", "Step02: verify grid view")
        @Kiruthika
        '''
        grid_css =".content-box.ibx-widget .files-box-files"
        util_method.synchronize_with_number_of_element(self, grid_css, 1, 30)
        util_method.verify_object_visible(self, grid_css, True, msg+"-1.a.Verify grid view object visible")
        list_css =".content-box.ibx-widget .files-listing"
        util_method.verify_object_visible(self, list_css, False, msg+"-1.b.Verify list view object invisible")
        grid_folder_text_css = ".content-box.ibx-widget .files-box .{0} .ibx-label-text".format(item_type)
        grid_folder_text_elems = self.driver.find_elements_by_css_selector(grid_folder_text_css)
        grid_folder_text = [el.text for el in grid_folder_text_elems if el.text!='']
        grid_folder_css = ".content-box.ibx-widget .files-box .{0}".format(item_type)
        grid_folder_elems = self.driver.find_elements_by_css_selector(grid_folder_css)
        item1_obj = grid_folder_elems[grid_folder_text.index(item1)]
        item2_obj = grid_folder_elems[grid_folder_text.index(item2)]
        item1_coordinates = util_method.get_object_screen_coordinate(self, item1_obj, coordinate_type='top_right')
        item2_coordinates = util_method.get_object_screen_coordinate(self, item2_obj, coordinate_type='start')
        util_method.asequal(self, int(item1_coordinates['y']), int(item2_coordinates['y']), msg+"-1.c.Verify y position of {0} top right and {1} top left is equal".format(item1,item2))
        status=int(item2_coordinates['x']) in range(int(item1_coordinates['x'])+grid_folder_distance, int(item1_coordinates['x'])+grid_folder_distance+2)
        util_method.asequal(self, True, status, msg+"-1.d.Verify x position of {0} top right and {1} top left difference is in range of ({2},{3})".format(item1,item2,grid_folder_distance,grid_folder_distance+2))
        
    def verify_list_view(self, item1, item2, msg):
        '''
        This function will verify the list view by  verifying
        1. list class visibility 
        2. grid class invisibility
        3. Last modified in view title
        4. x position of item1 bottom middle and item2 top middle is equal
        :usage verify_list_view("My Content", "Charts", "Step02: verify list view")
        @Kiruthika
        '''
        list_css =".content-box.ibx-widget .files-listing"
        util_method.synchronize_with_number_of_element(self, list_css, 1, expire_time=60)
        util_method.verify_object_visible(self, list_css, True, msg+"-1.a.Verify list view visible")
        grid_css =".content-box.ibx-widget .files-box-files"
        util_method.verify_object_visible(self, grid_css, False, msg+"-1.b.Verify grid view invisible")
        list_title_elems =self.driver.find_elements_by_css_selector(".files-listing .files-box-files-title .ibx-label-text")
        list_title = [el.text for el in list_title_elems if el.text!='']
        util_method.asin(self, "Last modified", list_title, msg+"-1.c.Verify Last modified in List View Title")
        list_row_title_css =".files-listing .files-box-files-row>.grid-cell-data[title]"
        list_row_title_elems = self.driver.find_elements_by_css_selector(list_row_title_css)
        list_row_text = [el.text for el in list_row_title_elems if el.text!='']
        list_row_css = ".files-listing .files-box-files-row"
        list_row_elems = self.driver.find_elements_by_css_selector(list_row_css)
        item1_obj = list_row_elems[list_row_text.index(item1)]
        item2_obj = list_row_elems[list_row_text.index(item2)]
        item1_coordinates = util_method.get_object_screen_coordinate(self, item1_obj, coordinate_type='bottom_middle')
        item2_coordinates = util_method.get_object_screen_coordinate(self, item2_obj, coordinate_type='top_middle')
        util_method.asequal(self, item1_coordinates['x'], item2_coordinates['x'], msg+"-1.d.Verify x position of {0} bottom middle and {1} top middle is equal".format(item1,item2))
        
    def select_toolbar_button(self, button, tool_css=".toolbar .toolbar-button-div [class*='fa {0}']"):
        '''
        This function will select options in toolbar button
        button = list or grid or refresh
        :usage select_toolbar_button('list')
        @Kiruthika
        '''
        button_name_dict={'list':'fa-list', 'grid':'fa-th', 'refresh':'fa-refresh'}
        button_css = tool_css.format(button_name_dict[button])
        util_method.synchronize_with_number_of_element(self, button_css, 1, expire_time=30)
        button_elem = self.driver.find_element_by_css_selector(button_css)
        core_utils.left_click(self, button_elem)
        
    def select_choose_columns(self):
        '''
        This function will select choose columns in list view
        :usage select_choose_columns()
        @Kiruthika
        '''
        settings_css ="#files-listing-area .fa-cog"
        util_method.synchronize_with_number_of_element(self, settings_css, 1, expire_time=30)
        settings_elem = self.driver.find_element_by_css_selector(settings_css)
        core_utils.left_click(self, settings_elem)
    
    def select_list_view_columns(self, columns_name_list):
        """
        This function will select options in list view columns 
        :usage select_list_view_columns(['Name', 'Size'])
        """
        Wf_Mainpage.select_choose_columns(self)
        for column_name in columns_name_list :
            Wf_Mainpage.select_context_menu_item(self, column_name)
            
    def verify_repository_folder_item_context_menu(self, item_name, expected_context_menu_item_list, folder_path=None, msg='Step X', comparision_type='asequal', item_name_index=1):                                                            
        """
        :Usage verify_repository_folder_item_context_menu('Report1.fex', ['Run'], folder_path='P116->G132647')
        @author:Aftab_Alam_Khan
        """
        if folder_path != None:
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        retun_obj=Wf_Mainpage.get_domain_folder_item(self, item_name, item_name_index=item_name_index)
        core_utils.right_click(self, retun_obj)
        Wf_Mainpage.verify_context_menu_item(self, expected_context_menu_item_list, msg=msg, comparision_type=comparision_type)
    
    def verify_repository_folder_item_context_submenu(self, item_name, contex_sub_menu_item_path, expected_context_menu_item_list, folder_path=None, msg='Step X', comparision_type='asequal', item_name_index=1, close_context_menu_css=None, expire_time=90):                                                            
        '''
        Desc: This funciton will verify contex sub_menu and close contex menu
        @param item_name: 'V5 portal'
        @param contex_sub_menu_item_path: 'Edit->Run'
        @param expected_context_menu_item_list: ['Edit','Run']
        @param folder_path = 'P116->S10029'
        @param msg: 'step 9'
        @param comparision_type: 'asin','asnotin' or 'asequal'
        @param item_name_index: 'asin','asnotin' or 'asequal'
        @param close_context_menu_css: '.banner-group-spacer'
        @param expire_time: 90
        :Usage verify_repository_folder_item_context_submenu('V5 portal', 'Edit->Run', ['Edit','Run'],folder_path='P116->S10029', msg='step 9', comparision_type='asin', item_name_index=1, close_context_menu_css='.banner-group-spacer', expire_time=90)
        @author:Aftab_Alam_Khan
        '''
        if folder_path != None:
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        retun_obj=Wf_Mainpage.get_domain_folder_item(self, item_name, item_name_index=item_name_index)
        core_utils.right_click(self, retun_obj)
        Wf_Mainpage.verify_context_submenu_item(self, contex_sub_menu_item_path, expected_context_menu_item_list, msg, comparision_type, close_context_menu_css=close_context_menu_css, expire_time=expire_time)
    
    def verify_repository_folder_context_submenu(self, folder_path, contex_sub_menu_item_path, expected_context_menu_item_list, msg='Step X', comparision_type='asequal', verification_state='expand', close_context_menu_css=None, expire_time=90):
        '''
        @param folder_path: 'P116->S7067'
        @param expected_context_menu_item_list:['Edit']
        @param msg: "Step 9"
        @param verification_state:'exand' or 'collapse'
        :Usage verify_repository_folder_context_menu('P116->S7067', ['Edit'], msg='Step 9', comparision_type='asin', verification_state='collapse')
        @author:Aftab_Alam_Khan
        '''
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected .ibx-label-text"
        if verification_state.lower()=='expand':
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        else:
            Wf_Mainpage.collapse_repository_folders(self, folder_path)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        selected_folder_obj = self.driver.find_element_by_css_selector(selected_folder_css)
        core_utils.right_click(self, selected_folder_obj)
        Wf_Mainpage.verify_context_submenu_item(self, contex_sub_menu_item_path, expected_context_menu_item_list, msg, comparision_type, close_context_menu_css=close_context_menu_css, expire_time=expire_time)
    
    def select_repository_folder_context_submenu(self, folder_path, contex_sub_menu_item_list, verification_state='expand', expire_time=90):
        '''
        Desc: This funciton will select repository folder context sub_menu.
        @param folder_path: 'P116->S7067'
        @param contex_sub_menu_item_list: 'Eidt->text editor'
        @param verification_state:'exand' or 'collapse'
        :Usage select_repository_folder_context_submenu('P116->S7067', 'Eidt->text editor', verification_state='collapse')
        @author:Aftab_Alam_Khan
        '''
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected .ibx-label-text"
        if verification_state.lower()=='expand':
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        else:
            Wf_Mainpage.collapse_repository_folders(self, folder_path)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        selected_folder_obj = self.driver.find_element_by_css_selector(selected_folder_css)
        core_utils.right_click(self, selected_folder_obj)
        for opt in contex_sub_menu_item_list.split('->'):
            Wf_Mainpage.select_context_menu_item(self, opt, expire_time)
    
    def verify_repository_folder_context_menu(self, folder_path, expected_context_menu_item_list, expire_time=90, msg='Step X', comparision_type='asequal', verification_state='expand'):
        '''
        @param folder_path: 'P116->S7067'
        @param expected_context_menu_item_list:['Edit']
        @param msg: "Step 9"
        @param verification_state:'exand' or 'collapse'
        :Usage verify_repository_folder_context_menu('P116->S7067', ['Edit'], msg='Step 9', comparision_type='asin', verification_state='collapse')
        @author:Aftab_Alam_Khan
        '''
        selected_folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected .ibx-label-text"
        if verification_state.lower()=='expand':
            Wf_Mainpage.expand_repository_folders(self, folder_path)
        else:
            Wf_Mainpage.collapse_repository_folders(self, folder_path)
        util_method.synchronize_with_number_of_element(self, selected_folder_css, 1, expire_time=expire_time)
        selected_folder_obj = self.driver.find_element_by_css_selector(selected_folder_css)
        core_utils.right_click(self, selected_folder_obj)
        Wf_Mainpage.verify_context_menu_item(self, expected_context_menu_item_list, msg=msg, comparision_type=comparision_type)
    
    def verify_items_in_views(self, expected_list, comparision_type, msg, view_type='grid_view'):
        '''
        Usgae: verify_items_in_views(['Margin'], 'asListEqual', "Step11.2b: Verify Margin by Product Category report in grid view", view_type='list_view')
        '''
        if view_type != 'grid_view':
            view_css = ".files-listing .files-box-files-area .grid-cell-data:not(.files-box-files-folder-icon) .ibx-label-text"
        else:
            view_css = ".content-box.ibx-widget .files-box .file-item .ibx-label-text"
        list_title_elems = self.driver.find_elements_by_css_selector(view_css)
        actual_list_title = [elem.text for elem in list_title_elems if elem.text!='']
        if comparision_type=='asin':
            for item in expected_list:
                util_method.asin(self, item, actual_list_title, msg+" displays "+item)
        elif comparision_type=='asnotin':
            for item in expected_list:
                util_method.as_notin(self, item, actual_list_title, msg+" doesn't display "+item)
        else:
            util_method.as_List_equal(self, expected_list, actual_list_title, msg)
    
    def verify_folder_in_views(self, expected_list, comparision_type, msg, view_type='grid_view'):
        '''
        Usgae: verify_items_in_views(['Margin'], 'asListEqual', "Step11.2b: Verify Margin by Product Category report in grid view", view_type='list_view')
        '''
        if view_type != 'grid_view':
            view_css = ".files-listing .files-box-files-area .grid-cell-data.files-box-files-folder-icon .ibx-label-text"
        else:
            view_css = ".content-box.ibx-widget .files-box .folder-div .folder-image-text .ibx-label-text"
        list_title_elems = self.driver.find_elements_by_css_selector(view_css)
        actual_list_title = [elem.text for elem in list_title_elems if elem.text!='']
        if comparision_type=='asin':
            for item in expected_list:
                util_method.asin(self, item, actual_list_title, msg+" displays "+item)
        elif comparision_type=='asnotin':
            for item in expected_list:
                util_method.as_notin(self, item, actual_list_title, msg+" doesn't display "+item)
        else:
            util_method.as_List_equal(self, expected_list, actual_list_title, msg)
    
    
    def search_input_box_options(self, option_type='write', input_text_msg=None, verify_value=None, msg=None, input_css="[class*='div-search'] [class*='txt-search'] input"):
        '''
        @Param: option_type: 'write' or 'clear'
        '''
        search_box_css = input_css
        try:
            search_box_elem=self.driver.find_element_by_css_selector(search_box_css)
        except NoSuchElementException:
            raise AttributeError("Search box not fond in Web page.")
        if verify_value != None:
            acutal_value = util_method.get_element_attribute(self, search_box_elem, 'value')
            util_method.asequal(self, verify_value, acutal_value, msg)
        elif option_type == 'write':
            util_method.set_text_to_textbox_using_keybord(self, input_text_msg, text_box_elem=search_box_elem)
            util_method.synchronize_with_visble_text(self, search_box_css, input_text_msg, 45, text_option='text_value')
        elif option_type =='clear':
            if Global_variables.browser_name in ['firefox']:
                try:
                    search_box_elem=self.driver.find_element_by_css_selector(search_box_css)
                    text_input_value=search_box_elem.get_attribute('value')
                    core_utils.python_left_click(self, search_box_elem)
                    time.sleep(1)
                    if sys.platform == 'linux':
                        pykeyboard.tap_key(pykeyboard.end_key)
                    else:
                        keyboard.send('end')
                    time.sleep(1)
                    for i in range(len(text_input_value)+3):
                        if sys.platform == 'linux':
                            pykeyboard.tap_key(pykeyboard.backspace_key)
                        else:
                            keyboard.send('\x08')
                    del i
                except NoSuchElementException:
                    raise AttributeError("Search box not fond in Web page.")
            else:
                core_utils.python_left_click(self, search_box_elem, element_location='middle_right', xoffset=-9)
            util_method.synchronize_with_visble_text(self, search_box_css, '', 45, text_option='text_value')
    
    def click_search_input_box_option_dropdown(self):
        '''
        This funciton will select search input box option dropdown 
        :Usage click_search_input_box_option_dropdown()
        '''
        search_box_dropdown_css=".ibx-advancedfoldersearch.div-search .menu-btn-advanced-search .fa-caret-down"
        search_box_dropdown_element = util_method.validate_and_get_webdriver_object(self, search_box_dropdown_css, 'Search box dropdown')
        core_utils.left_click(self, search_box_dropdown_element)
        util_method.synchronize_with_number_of_element(self, '.advanced-folder-search.pop-top', 1, 90)
        
    def verify_advanced_folder_search_default(self, label_name, property_type, property_value, step_number):
        '''
        This function will verify Advanced search folder display values ['label text', 'default selected value' or 'button value']
        @param label_name: 'Search'
        @param property_type: 'text_box'
        @param property_value: 'Title'
        @param step_number: '9'
        :Usage verify_advanced_folder_search_default(self, 'Search', 'text_box', 'Title', '9')
        '''
        poptop_dialog.Poptop_Dialog.dialog_name = 'Advance search folder'
        poptop_dialog.Poptop_Dialog.row_css = ".ibx-flexbox-horizontal:not([style*='none'])"
        property_type_dict = {'text_box': ".advance-search-box input[type='text']", 'label_text':'.ibx-label-text', 'button': "[class*='search-button']"}
        if property_type not in property_type_dict.keys():
            raise IndexError("Please pass property_type value from {0} list values.".format(list(property_type_dict.keys())))
        property_element_css = property_type_dict[property_type]
        row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, property_element_css, label_name)
        if property_type == 'text_box':
            actual_value = util_method.get_element_attribute(self, row_element, 'value')
            msg="Step {0}: Verify {1} text-box.".format(str(step_number), label_name)
            util_method.asequal(self, property_value, actual_value, msg)
        elif property_type == 'label_text':
            actual_value = row_element.text.strip()
            msg="Step {0}: Verify {1} label text.".format(str(step_number), label_name)
            util_method.asequal(self, property_value, actual_value, msg)
        elif property_type == 'button':
            actual_value = row_element.text.strip()
            msg="Step {0}: Verify {1} button text.".format(str(step_number), label_name)
            util_method.asequal(self, property_value, actual_value, msg)
        poptop_dialog.Poptop_Dialog.dialog_name = 'New Portal Dialog'
        poptop_dialog.Poptop_Dialog.row_css = "> .ibx-dialog-main-box .ibx-flexbox-horizontal"
    
    def verify_advanced_folder_search_dropdown_options(self, label_name, step_number, drop_down_expected_list=None, comparision_type='asequal', drop_down_selected_list=None):
        '''
        This function will verify Advanced search folder drop down values values.
        @param label_name: 'Search'
        @param step_number: '9'
        @param drop_down_expected_list: ['text_box']
        @param comparision_type: 'asequal', 'asnotin' or 'asin'
        @param drop_down_selected_list: ['text_box']
        :Usage verify_advanced_folder_search_dropdown_options('Search', '9', drop_down_expected_list=['text_box'], comparision_type='asequal', drop_down_selected_list=['text_box'])
        '''
        poptop_dialog.Poptop_Dialog.dialog_name = 'Advance search folder'
        poptop_dialog.Poptop_Dialog.row_css = ".ibx-flexbox-horizontal:not([style*='none'])"
        drop_down_button_css = '.advance-search-box .ibx-select-open-btn'
        row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, drop_down_button_css, label_name)
        core_utils.left_click(self, row_element)
        util_method.synchronize_with_number_of_element(self, ".pop-top [data-ibx-type='ibxSelectItemList']", 1, self.home_page_medium_timesleep)
        poptop_dialog.Poptop_Dialog.row_css=".ibx-select-item"
        popup_row_elements = poptop_dialog.Select_Popup.get_row_elements(self)
        if drop_down_expected_list != None:
            count = 1
            actual_list = [element.text.strip() for element in popup_row_elements]
            if comparision_type.lower()=='asequal':
                custom_msg="Step {0}: Verify {1} items in the visible dropdown options.".format(str(step_number), label_name)
                util_method.as_List_equal(self, drop_down_expected_list, actual_list, custom_msg)
            elif comparision_type.lower()=='asnotin':
                for item in drop_down_expected_list:
                    custom_msg="Step {0}.{1}: Verify [{2}] item not in the visible dropdown options.".format(str(step_number), count, item)
                    count+=1
                    util_method.as_notin(self, item, actual_list, custom_msg)
            elif comparision_type.lower()=='asin':
                for item in drop_down_expected_list:
                    custom_msg="Step {0}.{1}: Verify [{2}] item in the visible dropdown options.".format(str(step_number), count, item)
                    count+=1
                    util_method.asin(self, item, actual_list, custom_msg)
        if drop_down_selected_list != None:
            count = 1
            for option in drop_down_selected_list:
                found_item = [item_obj for item_obj in popup_row_elements if item_obj.text.strip() == option]
                if found_item == []:
                    raise LookupError('{0} not found in {1} drop-down'.format(option, label_name))
                selectecd_element = util_method.validate_and_get_webdriver_object(self, '.ibx-check-box-simple-marker', option, parent_object=found_item[0])
                element_class_attribute = util_method.get_element_attribute(self, selectecd_element, 'class')
                actual_value = option if 'ibx-check-box-simple-marker-check' in element_class_attribute else '{0} not selected'.format(option.capitalize())
                custom_msg="Step {0}.{1}: Verify [{2}] item is selected in {3} drop-down options.".format(str(step_number), count, option, label_name)
                count+=1
                util_method.asequal(self, option, actual_value, custom_msg)
        core_utils.python_move_to_element(self, row_element)
        current_mouse_postion = pyautogui.position()
        core_utils.python_click_with_offset(self, int(current_mouse_postion[0])+19, int(current_mouse_postion[1]))
        poptop_dialog.Poptop_Dialog.dialog_name = 'New Portal Dialog'
        poptop_dialog.Poptop_Dialog.row_css = "> .ibx-dialog-main-box .ibx-flexbox-horizontal"
    
    def select_dropdown_items_in_advanced_folder_search(self, label_name, options):
        '''
        This function will select options inside Advanced search folder drop-down values.
        @param label_name: 'Search'
        @param options: ['text_box']
        :Usage select_dropdown_items_in_advanced_folder_search('Search', ['text_box'])
        '''
        if type(options) is not list:
            raise TypeError('Please pass options as list format example : "options=["text"]"')
        scroll_css = ".pop-top .ibx-select-item-list"
        poptop_dialog.Poptop_Dialog.dialog_name = 'Advance search folder'
        poptop_dialog.Poptop_Dialog.row_css = ".ibx-flexbox-horizontal:not([style*='none'])"
        drop_down_button_css = '.advance-search-box .ibx-select-open-btn'
        dropdown_button_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, label_name, drop_down_button_css, label_name)
        core_utils.left_click(self, dropdown_button_element)
        util_method.synchronize_with_number_of_element(self, ".pop-top [data-ibx-type='ibxSelectItemList']", 1, self.home_page_medium_timesleep)
        poptop_dialog.Poptop_Dialog.row_css=".ibx-select-item"
        for item in options:
            row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, item, '.ibx-label-text', item)
            j_script.scrollTop(self, scroll_css, row_element, wait_time=1)
            core_utils.left_click(self, row_element)
        core_utils.python_move_to_element(self, dropdown_button_element)
        current_mouse_postion = pyautogui.position()
        core_utils.python_click_with_offset(self, int(current_mouse_postion[0])+19, int(current_mouse_postion[1]))
        poptop_dialog.Poptop_Dialog.dialog_name = 'New Portal Dialog'
        poptop_dialog.Poptop_Dialog.row_css = "> .ibx-dialog-main-box .ibx-flexbox-horizontal"
    
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
        poptop_dialog.Poptop_Dialog.dialog_name = 'Advance search folder'
        poptop_dialog.Poptop_Dialog.row_css = ".ibx-flexbox-horizontal:not([style*='none'])"
        row_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, button_name, "[class*='search-button']", button_name)
        if select == True:
            core_utils.left_click(self, row_element)
        if color_name:
            expected_color_name = util_method.color_picker(self, color_name, rgb_type='rgba')
            actual_color_name = Color.from_string(util_method.get_element_css_propery(self, row_element, 'background-color')).rgba
            util_method.asequal(self, expected_color_name, actual_color_name, msg)
        if location == True:
            matching_behavior_input = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, 'Matching Behavior', ".advance-search-box input[type='text']", 'Matching Behavior')
            matching_behavior_input_text_box_middle_left_coordinate = core_utils.get_web_element_coordinate(self, matching_behavior_input, 'middle_left')
            matching_behavior_input_text_box_middle_right_coordinate = core_utils.get_web_element_coordinate(self, matching_behavior_input, 'middle_right')
            matching_behavior_input_text_box_bottom_middle_coordinate = core_utils.get_web_element_coordinate(self, matching_behavior_input, 'bottom_middle')
            button_bottom_top_middle_coordinate = core_utils.get_web_element_coordinate(self, row_element, 'top_middle')
            button_bottom_middle_left_coordinate = core_utils.get_web_element_coordinate(self, row_element, 'middle_left')
            button_bottom_middle_right_coordinate = core_utils.get_web_element_coordinate(self, row_element, 'middle_right')
            if int(button_bottom_middle_right_coordinate['x']) > int(matching_behavior_input_text_box_middle_right_coordinate['x']):
                if int(button_bottom_middle_left_coordinate['x']) > int(matching_behavior_input_text_box_middle_left_coordinate['x']):
                    if int(button_bottom_top_middle_coordinate['y']) > int(matching_behavior_input_text_box_bottom_middle_coordinate['y']):
                        expected,actual=True,True
                    else:
                        expected,actual=int(button_bottom_top_middle_coordinate['y']), int(matching_behavior_input_text_box_bottom_middle_coordinate['y'])
                else:
                    expected,actual=int(button_bottom_middle_left_coordinate['x']), int(matching_behavior_input_text_box_middle_left_coordinate['x'])
            else:
                expected,actual=int(button_bottom_middle_right_coordinate['x']), int(matching_behavior_input_text_box_middle_right_coordinate['x'])
            util_method.asequal(self, expected, actual, msg)
        poptop_dialog.Poptop_Dialog.dialog_name = 'New Portal Dialog'
        poptop_dialog.Poptop_Dialog.row_css = "> .ibx-dialog-main-box .ibx-flexbox-horizontal"
    
    def verify_advanced_folder_search_dialog_open_or_close(self, dialog_mode, msg):
        '''
        This function will verify advanced folder search dialog is open or close.
        @param dialog_mode: 'open'
        @param msg: 'Step 9: Verify'
        :Usage  verify_advanced_folder_search_dialog_open_or_close('open', 'Step 9: Verify')
        '''
        portal_dialog_css = '.advanced-folder-search.pop-top'
        if dialog_mode.lower() not in ['open', 'close']:
                raise IndexError("Please pass dialog_mode as 'open' or 'close'.")
        current_mode = True if dialog_mode == 'open' else False
        util_method.verify_object_visible(self, portal_dialog_css, current_mode, msg)
        
    def verify_view_title_labels(self, expected_list, msg, view_type='grid_view', label_type='files', list_view_css=".files-box-files-title", grid_view_css=".sd-content-title-label-{0}"):
        '''
        @Param: view_type: 'grid_view' or 'list_view'
        @param: if 'grid_view' then pass label_type: 'files' or 'folders'
        Usage: verify_view_title_labels([], "Step05: Verify title")
        '''
        if view_type=='grid_view':
            view_css=grid_view_css.format(label_type)
        elif view_type=='list_view':
            view_css=list_view_css
        try:
            content_title_elem = self.driver.find_element_by_css_selector(view_css)
        except NoSuchElementException:
            raise AttributeError("Content area is not displayed as '{0}'.".format(view_type))
        actual_title_list1 = content_title_elem.text.split('\n')
        actual_title_list=[item.strip() for item in actual_title_list1 if item!= '']
        util_method.as_List_equal(self, expected_list, actual_title_list, msg)
    
    def select_button_in_portal_content_area(self, option):
        '''
        Desc: This function will select button in portal content area
        usage: select_button_in_portal_content_area('Retail Samples')
        '''
        try:
            elems = self.driver.find_elements_by_css_selector(".sd-category-buttons .ibx-button")
        except NoSuchElementException:
            raise AttributeError("Select button in Portal Content area is not found")
        try:
            obj = [elem for elem in elems if elem.text.strip() == option]
            core_utils.left_click(self, obj[0])
        except:
            raise IndexError("option {0} is not found in Portal Content area select button".format(option))
        
    def ask_webfocus_search_bar_options(self, verify_option, display_status, msg):
        '''
        This function to used in side Ask webfocus page.
        Usage: ask_webfocus_search_bar_options('text_box', True, "Step02: Verify text box")
        '''
        search_bar_css=".right-main-panel .askwebfocus-bar"
        search_bar_textbox_css="[data-ibx-type='askWebFOCUS']"
        search_bar_speech_mic_css=".ask-speech-button [style*='mic.png']"
        search_bar_search_image_css=".ask-query-button .fa-search"
        search_bar_dropdown_css=".ask-search-type-button .ibx-glyph-caret-down"
        try:
            search_bar_elem=self.driver.find_element_by_css_selector(search_bar_css)
        except NoSuchElementException:
            raise AttributeError("Search bar option not found in Ask Webfocus page.")
        if verify_option.lower()=='text_box':
            try:
                actual_status=search_bar_elem.find_element_by_css_selector(search_bar_textbox_css).is_displayed()
            except NoSuchElementException:
                raise AttributeError("{0} option not found inside search bar in Ask Webfocus  page.".formate(verify_option.lower()))
        elif verify_option.lower()=='speech_mic':
            try:
                actual_status=search_bar_elem.find_element_by_css_selector(search_bar_speech_mic_css).is_displayed()
            except NoSuchElementException:
                raise AttributeError("{0} option not found inside search bar in Ask Webfocus  page.".formate(verify_option.lower()))    
        elif verify_option.lower()=='search_image':
            try:
                actual_status=search_bar_elem.find_element_by_css_selector(search_bar_search_image_css).is_displayed()
            except NoSuchElementException:
                raise AttributeError("{0} option not found inside search bar in Ask Webfocus  page.".formate(verify_option.lower()))
        elif verify_option.lower()=='dropdown':
            try:
                actual_status=search_bar_elem.find_element_by_css_selector(search_bar_dropdown_css).is_displayed()
            except NoSuchElementException:
                raise AttributeError("{0} option not found inside search bar in Ask Webfocus  page.".formate(verify_option.lower()))
        else:
            raise IndexError("Please select which option need to verify and select option from this list [text_box, speech_mic, search_image, dropdown]")
        util_method.asequal(self, display_status, actual_status, msg)  
    
    def ask_webfocus_content_area(self, verify_option, expected_text, msg):
        '''
        This function to used in side Ask webfocus page.
        verify_option : title or title_button_state or title_button_text
        '''  
        content_area_css=".right-main-panel .askwebfocus-recents"
        ask_label_text_css=".ibx-label-text"
        ask_title_css=".ask-title-label {0}".format(ask_label_text_css)
        ask_title_button_css=".ask-title-button"
        item_disable_css="ibx-widget-disabled"
        try:
            ask_webfocus_content_elem=self.driver.find_element_by_css_selector(content_area_css)
        except NoSuchElementException:
            raise AttributeError("content area not found in Ask Webfocus page.")
        if verify_option.lower()=='title':
            try:
                actual_status=ask_webfocus_content_elem.find_element_by_css_selector(ask_title_css).text.strip()
            except NoSuchElementException:
                raise AttributeError("{0} option not found inside content area in Ask Webfocus  page.".formate(verify_option.lower()))
        elif verify_option.lower()=='title_button_state':
            try:
                title_button_elem=ask_webfocus_content_elem.find_element_by_css_selector(ask_title_button_css)
                title_button_class_attributes=j_script.get_element_all_attributes(self, title_button_elem)['class']
                if item_disable_css in title_button_class_attributes:
                    actual_status=True
                else:
                    actual_status=True
                
            except NoSuchElementException:
                raise AttributeError("{0} option not found inside content area in Ask Webfocus  page.".formate(verify_option.lower()))  
        elif verify_option.lower()=='title_button_text':
            try:
                actual_status=ask_webfocus_content_elem.find_element_by_css_selector(ask_title_button_css+" {0}".format(ask_label_text_css)).text.strip()
            except NoSuchElementException:
                raise AttributeError("{0} option not found inside content area in Ask Webfocus  page.".formate(verify_option.lower()))  
        else:
            raise IndexError("Please select which option need to verify and select option from this list [title, title_button_state, title_button_text]")
        util_method.asequal(self, expected_text, actual_status, msg)
    
    def expand_collapse_resource_tree(self, selection_option):
        '''
        This function to used in expand and collapse resource tree and verify it's current state.
        @param selection_option:'expand' or 'collapse'
        :usage expand_collapse_resource_tree('expand')
        @author:Aftab_Alam_Khan
        '''
        collapse_expan_option_dict={'collapse':'collapse', 'expand':'showcollapse'}
        expand_collapse_resource_tree_css=".right-main-panel .explore-box .tree-{0}-button .ibx-label-icon".format(collapse_expan_option_dict[selection_option.lower()])
        try:
            expand_collapse_resource_tree_elem=self.driver.find_element_by_css_selector(expand_collapse_resource_tree_css)
            core_utils.left_click(self, expand_collapse_resource_tree_elem)
        except NoSuchElementException:
            raise AttributeError("'{0}' resource tree option not found inside content area.".format(selection_option))
    
    def verify_expand_collapse_resource_tree(self, verify_option, status, msg):
        '''
        This function is used to verify  expand and collapse resource tree current state.
        if verification for collapse then resource tree is displayed and if verification for expand then resource tree is not displayed
        @param verify_option:'expand' or 'collapse'
        @param status:True or False
        @param msg:"Step 9: Verify"
        :usage verify_expand_collapse_resource_tree('expand', True, "Step 9: Verify")
        @author:Aftab_Alam_Khan
        '''
        collapse_expan_option_dict={'collapse':'collapse', 'expand':'showcollapse'}
        expand_collapse_resource_tree_css=".right-main-panel .explore-box .tree-{0}-button .ibx-label-icon".format(collapse_expan_option_dict[verify_option.lower()])
        resource_tree_css=".explore-box .left-pane .ibfs-tree"
        step_number = re.search(r'\d+', msg).group()
        try:
            expand_collapse_resource_tree_elem_stauts=self.driver.find_element_by_css_selector(expand_collapse_resource_tree_css).is_displayed()
        except NoSuchElementException:
            raise AttributeError("'{0}' resource tree option not found inside content area.".format(verify_option.lower()))
        util_method.asequal(self, status, expand_collapse_resource_tree_elem_stauts, msg)
        if verify_option.lower() == 'collapse':
            try:
                expand_collapse_resource_tree_elem_stauts=self.driver.find_element_by_css_selector(resource_tree_css).is_displayed()
            except NoSuchElementException:
                expand_collapse_resource_tree_elem_stauts=False
            util_method.asequal(self, True, expand_collapse_resource_tree_elem_stauts, "Step {}.a: Verify resource tree is displayed.".format(step_number))
        else:
            try:
                expand_collapse_resource_tree_elem_stauts=self.driver.find_element_by_css_selector(resource_tree_css).is_displayed()
            except NoSuchElementException:
                expand_collapse_resource_tree_elem_stauts=True
            util_method.asequal(self, False, expand_collapse_resource_tree_elem_stauts, "Step {}.a: Verify resource tree is not displayed.".format(step_number))
            
    def verify_tags(self, expected_tag_list, step_num, comparision_type='asequal'):
        '''
        This function will verify tags in portals, favorites etc...
        
        @param expected_tag_list: ['Report']
        @param step_num: '9'
        @param comparision_type:'asequal' or 'asnotin' or 'asin'
        :Usage verify_tags(['Report'], "Step 9: Verify")
        @author:Aftab_Alam_Khan 
        '''
        toolbar_css = ".right-main-panel .toolbar [data-ibx-type='ibxLabel'][title] .ibx-label-text"
        tags_css = ".content-box [data-ibx-name='categoryButtons'] [data-ibx-type='ibxButton'] .ibx-label-text"
        try:
            tag_elem = self.driver.find_elements_by_css_selector(tags_css)
            actual_tag_list = [elem.text.strip() for elem in tag_elem]
        except:
            raise LookupError('No tags section displayed under content area.')
        try:
            toolbar_text = util_method.validate_and_get_webdriver_object(self, toolbar_css, 'Tool bar').text.strip()
        except AttributeError:
            toolbar_text = 'Domains'
        if comparision_type=='asequal':
            msg = 'Step {0}: Verify tags list {1} under {2}.'.format(step_num, expected_tag_list, toolbar_text)
            util_method.as_List_equal(self, expected_tag_list, actual_tag_list, msg)
        elif comparision_type=='asin':
            count_num=1
            for tag in expected_tag_list:
                msg = 'Step {0}.{1}: Verify tag {2} under {3}.'.format(step_num, count_num, expected_tag_list, toolbar_text)
                util_method.asin(self, tag, actual_tag_list, msg)
                count_num+=1
        elif comparision_type=='asnotin':
            count_num=1
            for tag in expected_tag_list:
                msg = 'Step {0}.{1}: Verify tag {2} not in under {3}.'.format(step_num, count_num, expected_tag_list, toolbar_text)
                util_method.as_notin(self, tag, actual_tag_list, msg)
                count_num+=1
    
    def close_or_open_view_dialog(self, title_name, button_name):
        '''
        This function will close view dialog.
        @param title_name: 'Gray'
        @param button_name: 'Open in new window'
        :Usage  close_or_open_view_dialog('Gray', 'close')
        '''
        if button_name not in ['Close', 'Open in new window']:
            raise IndexError("Please pass button_name as 'Close' or 'Open in new window'.")
        poptop_dialog.Poptop_Dialog.row_css='.ibx-flexbox-horizontal'
        current_button_name_css = "[class*='close-button']" if button_name in ['Close'] else "[class*='popout-button']"
        current_button_name_element = poptop_dialog.New_Portal_Dialog.get_element_in_dialog(self, title_name, current_button_name_css, title_name)
        poptop_dialog.Poptop_Dialog.row_css="> .ibx-dialog-main-box .ibx-flexbox-horizontal"
        core_utils.left_click(self, current_button_name_element)
    
    def verify_icon_type_in_content_area(self, folder_or_item_name, icon_type, step_number, verify_color_name=None, item_name_index=1):
        '''
        This will verify folder/item icon inside content area.
        @param folder_or_item_name: 'V5 portal'
        @param icon_type: 'portal'
        @param step_number: '9'
        @param verify_color_name: 'blue'
        @param item_name_index: 1
        :Usage  verify_icon_type_in_content_area('V5 portal', 'portal', '9', verify_color_name='blue', item_name_index=1)
        '''
        icon_css = ".ibx-label-icon:not([style*='none']) .fa-share-alt" if icon_type.lower() == 'share' else ".ibx-label-icon:not([style*='none'])"
        icon_type_dict = {'folder':'\uf07b', 'portal':'\ue91e', 'share':'\uf1e0','insight':'\ue9b5'}
        disp_icon_msg = "Step {0}.a: Verify {1} icon.".format(str(step_number), folder_or_item_name)
        disp_color_msg = "Step {0}.b: Verify {1} icon color.".format(str(step_number), folder_or_item_name)
        return_obj=Wf_Mainpage.get_domain_folder_item(self, folder_or_item_name, item_name_index=item_name_index)
        current_element = util_method.validate_and_get_webdriver_object(self, icon_css, folder_or_item_name, parent_object=return_obj)
        actual_alert_icon_value = j_script.get_element_before_style_properties(self, current_element, 'content').replace('"', '')
        util_method.asequal(self, icon_type_dict[icon_type.lower()].encode('utf-8'), actual_alert_icon_value.encode('utf-8'), disp_icon_msg)
        if verify_color_name:
            expected_color_name = util_method.color_picker(self, verify_color_name, rgb_type='rgba')
            actual_color_name = Color.from_string(util_method.get_element_css_propery(self, current_element, 'color')).rgba
            util_method.asequal(self, expected_color_name, actual_color_name, disp_color_msg)    
            
    def verify_content_area_element_publish_or_unpublish(self, folder_or_item_name, folder_or_item_type, folder_or_item_status, msg, index=1, pause=90):
        '''
        Desc: This function will verify repository folder is publish or unpublish.
        @param folder_or_item_name: 'P116'
        @param folder_or_item_type: 'folder' or 'file'
        @param folder_or_item_status: 'publish'
        @param msg: 'Step 9: Verify'
        @param index: 0
        :Usage verify_content_area_element_publish_or_unpublish('P116', 'folder', 'publish', 'Step 9: Verify', index=0)
        '''
        if folder_or_item_status.lower() not in ['publish', 'unpublish']:
            raise IndexError("Please pass folder_status as 'publish' or 'unpublish'")
        if folder_or_item_type.lower() not in ['folder', 'file']:
            raise IndexError("Please pass folder_status as 'folder' or 'file'")
        element_type_dict_css = {'folder':'.folder-div', 'file':'.file-item'}
        publish_folder_or_item_css = '{0}-item-publish'.format(folder_or_item_type)
        actual_value = Wf_Mainpage.get_content_element_stauts(self, folder_or_item_name, element_type_dict_css[folder_or_item_type], publish_folder_or_item_css, folder_or_item_status, index, pause)
        util_method.asequal(self, folder_or_item_status, actual_value, msg)
    
    def verify_content_area_element_shown_or_hide(self, folder_or_item_name, folder_or_item_type, folder_or_item_status, msg, index=1, pause=90):
        '''
        Desc: This function will verify repository folder is shown or hide.
        @param folder_or_item_name: 'P116'
        @param folder_or_item_type: 'folder' or 'file'
        @param folder_or_item_status: 'shown'
        @param msg: 'Step 9: Verify'
        @param index: 1
        :Usage verify_content_area_element_publish_or_unpublish('P116', 'folder', 'shown', 'Step 9: Verify', index=1)
        '''
        if folder_or_item_status.lower() not in ['shown', 'hide']:
            raise IndexError("Please pass folder_status as 'shown' or 'hide'")
        if folder_or_item_type.lower() not in ['folder', 'file']:
            raise IndexError("Please pass folder_status as 'folder' or 'file'")
        element_type_dict_css = {'folder':'.folder-div', 'file':'.file-item'}
        publish_folder_or_item_css = '{0}-item-shown'.format(folder_or_item_type)
        actual_value = Wf_Mainpage.get_content_element_stauts(self, folder_or_item_name, element_type_dict_css[folder_or_item_type], publish_folder_or_item_css, folder_or_item_status, index, pause)
        util_method.asequal(self, folder_or_item_status, actual_value, msg)
    
    def get_content_element_stauts(self, folder_or_item_name, element_css, status_css, expected_status, index, pause):
        '''
        Desc: This method will synchronize content area element
        @param folder_or_item_name: 'P116'
        @param element_css: '.folder-div'
        @param status_css: 'folder-item-shown'
        @param expected_status: 'shown'
        @param index: 1
        @param pause: 19
        :Usage get_content_element_stauts('P116', '.folder-div', 'folder-item-shown', 'shown', 1, 19)
        '''
        if expected_status.lower() in ['publish', 'unpublish']:
            expected_condition1, expected_condtion2 = 'publish', 'unpublish'
        elif expected_status.lower() in ['shown', 'hide']:
            expected_condition1, expected_condtion2 = 'shown', 'hide'
        for _ in range(pause):
                try:
                    return_obj=Wf_Mainpage.get_domain_folder_item(self, folder_or_item_name, item_name_index=index)
                    current_element = util_method.validate_and_get_webdriver_object(self, element_css, folder_or_item_name, parent_object=return_obj)
                    element_class_attribute = util_method.get_element_attribute(self, current_element, 'class')
                    status = expected_condition1 if status_css in element_class_attribute else expected_condtion2
                    if status:
                        return status
                    else:
                        time.sleep(1)
                except:
                    continue
    
    def verify_search_textbox_value(self, expected_value, msg):
        """
        This function will verify search textbox value
        """
        search_textbox_css = ".toolbar div[data-ibx-type='advancedFolderSearch'] input[type='search']"
        search_textbox_obj = util_method.validate_and_get_webdriver_object(self, search_textbox_css, 'Home page Search textbox')
        text_value = search_textbox_obj.get_attribute('value').strip()
        placeholder_text = search_textbox_obj.get_attribute('placeholder').strip()
        actual_value = text_value if text_value != '' else placeholder_text
        util_method.asequal(self, expected_value, actual_value, msg)
    
    def verify_folders_and_items_contain_searched_text(self, searched_text, msg, verify='folders'):
        """
        This function will verify folders or items are contain searched text. For example if enter 'x' in search text box, the result folders and items should be contain 'x'
        :param -  searched_text - text of entered in search text box
        """
        searched_items_css = ".files-box-files .folder-item" if verify=='folders' else ".files-box-files .file-item"
        searched_items_obj = util_method.validate_and_get_webdriver_objects(self, searched_items_css, 'Domain folders and items')
        status = None
        for item in searched_items_obj :
            if searched_text.lower() in item.text.lower() :
                status = True
            else :
                status = False
                msg = msg + " : [{0}]".format(item.text)
                break
        util_method.asequal(self, True, status, msg)
        
    def get_action_bar_tab_objects(self):
        """
        Description : This method will return all action bar tab buttons object as list
        """
        tabs_css = WfMainPageLocators.ACTION_TAB_CSS
        tab_objects = util_method.validate_and_get_webdriver_objects(self, tabs_css, "Home page action bar tabs")
        visble_tab_objects = [obj for obj in tab_objects if obj.is_displayed()]
        return visble_tab_objects
    
    def get_action_bar_tab_name(self):
        """
        Description : This method will return all action bar tab button name as list
        """
        tab_objects = Wf_Mainpage.get_action_bar_tab_objects(self)
        tab_name_list = [tab.text.strip() for tab in tab_objects]
        return tab_name_list
    
    def get_action_bar_tab_object(self, tab_name):
        """
        Description : This method will return specific action bar tab button object
        """
        tab_button_list = Wf_Mainpage.get_action_bar_tab_name(self)
        if tab_name in tab_button_list :
            tab_objects = Wf_Mainpage.get_action_bar_tab_objects(self)
            tab_object = tab_objects[tab_button_list.index(tab_name)]
            return tab_object
        else :
            error_msg = "[{0}] tab doesn't displayed in action bar".format(tab_name)
            raise ElementNotVisibleException(error_msg)
    
    def verify_action_bar_tabs(self, expected_tabs_list, msg, assert_type='asequal'):
        """
        Description : This method will verify action bar tab buttons
        @usage  : verify_action_bar_tabs(['Common', 'Data', 'Designer', 'InfoAssist', 'Schedule', 'Other'], 'Step 01.1 : Verify action bar tab buttons')
        """
        actual_tabs_list = Wf_Mainpage.get_action_bar_tab_name(self)
        util_method.verify_list_values(self, expected_tabs_list, actual_tabs_list, msg, assert_type)
    
    def verify_action_bar_tab_color(self, tab_name, expected_color_name, msg):
        """
        Description : This method will verify action bar tab button color
        @usage  : verify_action_bar_tab_button_color('Common', 'blue', 'Step 01.01 : Verify 'Common' tab button color')
        """
        tab_object = Wf_Mainpage.get_action_bar_tab_object(self, tab_name)
        util_method.verify_element_color_using_css_property(self, None, expected_color_name, msg, attribute='background-color', element_obj=tab_object)
    
    def verify_selected_action_bar_tab(self, selected_tab, msg):
        """
        Description : This method will verify selected action bar tab
        @usage  : verify_selected_action_bar_tab(['Common'], 'Step 01.01 : Verify 'Common' tab is selected as default')
        """
        selected_tab_css = "{0}.checked".format(WfMainPageLocators.ACTION_TAB_CSS)
        selected_tab_objs = util_method.validate_and_get_webdriver_objects(self, selected_tab_css, 'Selected action bar tab')
        actual_selected_tab = [selected_tab_obj.text.strip() for selected_tab_obj in selected_tab_objs]
        util_method.asequal(self, selected_tab, actual_selected_tab, msg)
        
    def select_action_bar_tab(self, btn_name):
        '''
        Description : This function is used to select action bar tab
        :Usage select_action_bar_tab('Designer')
        '''
        button_obj = Wf_Mainpage.get_action_bar_tab_object(self, btn_name)
        core_utils.left_click(self, button_obj)
    
    def get_action_bar_tab_option_objects(self):
        '''
        Descriptions : This method will return action bar selected tab option objects.
        usage : get_action_bar_tab_option_objects()
        '''
        action_bar_btn_css = "div:not([class*='tpg-hidden'])>div>div.create-new-item[role='button']"
        action_bar_tab_options_obj = util_method.validate_and_get_webdriver_objects(self, action_bar_btn_css, "Home page action bar tab options.")
        visble_action_bar_tab_options_obj = [obj for obj in action_bar_tab_options_obj if obj.is_displayed()]
        return visble_action_bar_tab_options_obj
    
    def get_action_bar_tab_options_name(self):
        '''
        Descriptions : This method will return action bar selected tab option objects.
        usage : get_action_bar_tab_option_objects()
        '''
        action_bar_tab_options_obj = Wf_Mainpage.get_action_bar_tab_option_objects(self)
        action_bar_tab_options_names = [button.text.strip() for button in action_bar_tab_options_obj]
        return action_bar_tab_options_names
        
    def get_action_bar_tab_option_object(self, option_name):
        """
        Description : This method will return specific action bar tab option object
        """
        tab_option_list = Wf_Mainpage.get_action_bar_tab_options_name(self)
        if option_name in tab_option_list :
            option_objects = Wf_Mainpage.get_action_bar_tab_option_objects(self)
            option_object = option_objects[tab_option_list.index(option_name)]
            return option_object
        else :
            error_msg = "[{0}] tab option doesn't displayed in action bar".format(option_name)
            raise ElementNotVisibleException(error_msg)
    
    def verify_action_bar_tab_option_color(self, option_name, expected_color, msg):
        """
        Descriptions : This method will verify action bar buttons color
        usage : verify_action_bar_button_color('Page', 'bar_blue', 'Step 01.01 : Verify Page button displayed with blue color)
        """
        option_object = Wf_Mainpage.get_action_bar_tab_option_object(self, option_name)
        option_color_obj = util_method.validate_and_get_webdriver_object(self, "div.ibx-label-glyph.ibx-label-icon", "Home page action bar option color", option_object)
        util_method.verify_element_color_using_css_property(self, None, expected_color, msg, attribute='background-color', element_obj=option_color_obj)
        
    def select_action_bar_tab_option(self, option_name):
        '''
        Descriptions : This method will select action bar tab option
        usage : select_action_bar_tab_option('Page')
        '''
        option_object = Wf_Mainpage.get_action_bar_tab_option_object(self, option_name)
        core_utils.left_click(self, option_object)
    
    def verify_action_bar_tab_options(self, expected_options_list, msg, assert_type='asequal'):
        '''
        Descriptions : This method will verify action bar tab option
        usage : verify_action_bar_tab_options(['Page'], 'Step 9: Verify')
        '''
        actual_options_list = Wf_Mainpage.get_action_bar_tab_options_name(self)
        util_method.verify_list_values(self, expected_options_list, actual_options_list, msg, assert_type)
    
    def verify_action_bar_is_not_visible(self, msg):
        """
        Description : This method will verify whether action bar tab is not displayed
        @usage : verify_action_bar_is_not_visible('Step 01.01 : Verify action bar is not display)
        """
        action_bar_css = "div.create-new-box"
        action_bar_obj = util_method.validate_and_get_webdriver_object(self, action_bar_css, 'Action bar')
        action_bar_visible_status = action_bar_obj.is_displayed()
        util_method.asequal(self, False, action_bar_visible_status, msg)
        
    def collapse_or_expand_action_bar(self, option_name): 
        '''
        This function is used to collapse_or_expand_action_bar
        @param option_name = 'expand' or 'collapse'
        :Usage collapse_or_expand_action_bar('collapse')
        '''   
        if option_name not in ['expand', 'collapse']:
            raise IndexError("Please pass option_name value 'expand' or 'collapse'.")
        expand_icon_css="div[class^='content-title-btn'][title*='Expand actions bar'] .ibx-label-icon"
        collapse_icon_css="div[class^='content-title-btn'][title*='Collapse actions bar'] .ibx-label-icon"
        if option_name.lower() == 'expand':
            btn_obj = util_method.validate_and_get_webdriver_object(self, expand_icon_css, 'Expand Icon')
        else:
            btn_obj = util_method.validate_and_get_webdriver_object(self, collapse_icon_css, 'Collapse Icon')
        core_utils.left_click(self, btn_obj)
    
    def add_comment(self, comment_message):
        '''
        Description : This function will add comment
        Example : add_comment(caption_tile='New Folder', tile_value='Test', name_value='Test', step_number='9')
        '''
        add_comment_text_css = ".annotations_new"
        popup_css ="#idannotationpopup"
        editor_css = "{0} .annotations_popup_edit".format(popup_css)
        post_button_css = "{0} .button.bi-button .bi-button-label".format(popup_css)
        add_comment_object = util_method.validate_and_get_webdriver_object(self, add_comment_text_css, 'Add comment')
        core_utils.left_click(self, add_comment_object)
        add_comment_object = util_method.validate_and_get_webdriver_object(self, editor_css, 'Add comment')
        util_method.set_text_to_textbox_using_keybord(self, comment_message, text_box_elem=add_comment_object)
        util_method.switch_to_frame(self, frame_css=editor_css)
        util_method.synchronize_until_element_is_visible(self, 'body', 90)
        util_method.switch_to_default_content(self)
        post_comment_object = util_method.validate_and_get_webdriver_object(self, post_button_css, 'Post comment button')
        core_utils.left_click(self, post_comment_object)
    
    def verify_comment(self, row_number, expected_comment_message, msg):
        '''
        Description : This function will add comment
        Example : verify_comment(1, caption_tile='New Folder', tile_value='Test', name_value='Test', step_number='9')
        '''
        verify_comment_text_css = ".annotations_list .annotations_cell"
        user_css = ".annotations_user"
        message_content_css = ".annotations_content"
        content_tag_css = ".annotations_meta_tags"
        footer_css = ".annotations_footer"
        comment_object = util_method.validate_and_get_webdriver_objects(self, verify_comment_text_css, 'Verify Comment message')[int(row_number) - 1]
        header_comment_message_object = util_method.validate_and_get_webdriver_object(self, user_css, "User Type", parent_object=comment_object)
        content_tag_object = util_method.validate_and_get_webdriver_object(self, content_tag_css, "Content tag", parent_object=comment_object)
        message_content_object = util_method.validate_and_get_webdriver_object(self, message_content_css, "Content message", parent_object=comment_object)
        footer_object = util_method.validate_and_get_webdriver_object(self, footer_css, "Footer text", parent_object=comment_object)
        actual_text = '{0}{1}{2}{3}'.format(header_comment_message_object.text.strip(), content_tag_object.text.strip(), message_content_object.text.strip(), footer_object.text.strip())
        util_method.asequal(self, expected_comment_message, actual_text, msg)
    
    def open_popup_dialog_from_action_bar(self, label_name, property_type, property_value=None, expire_time=45, text_find_type='in'):
        '''
        Description : This is the function will create new item in popup
        Example : open_popup_dialog_from_action_bar('Title', 'text_box', property_value='test')
        '''
        if property_type == 'text_box':
            input_box_element = pop_obj.get_element_in_dialog(self, label_name, "div[data-ibx-type^='ibxText']", '{0} text_box'.format(label_name), text_find_type=text_find_type)
            util_method.set_text_to_textbox_using_keybord(self, property_value, text_box_elem=input_box_element)
            util_method.synchronize_with_visble_text_within_parent_object(self, input_box_element, "[role='textbox']", property_value, expire_time, text_option='text_value')
        if property_type == 'text_area':
            input_box_element = pop_obj.get_element_in_dialog(self, label_name, "div[data-ibx-type^='ibxText']", '{0} text_box'.format(label_name), text_find_type=text_find_type)
            util_method.set_text_to_textbox_using_keybord(self, property_value, text_box_elem=input_box_element)
            util_method.synchronize_with_visble_text_within_parent_object(self, input_box_element, "textarea", property_value, expire_time, text_option='text_value')
        if property_type == 'drop_down':
            drop_down_element = pop_obj.get_element_in_dialog(self, label_name, ".hp-select-picker .ibx-select-open-btn", label_name)
            core_utils.left_click(self, drop_down_element)
            pop_obj.row_css=".ibx-select-item"
            popup_row_element = pop_obj.get_element_in_dialog(self, property_value, '.ibx-label-text', property_value)
            pop_obj.row_css="> .ibx-dialog-main-box .ibx-flexbox-horizontal"
            core_utils.left_click(self, popup_row_element)
        if property_type == 'check_box':
            row_element = pop_obj.get_element_in_dialog(self, label_name, "[role='checkbox'] .ibx-check-box-simple-marker", label_name)
            element_class_attribute = util_method.get_element_attribute(self, row_element, 'class')
            status_value = 'check' if 'ibx-check-box-simple-marker-check' in element_class_attribute else 'uncheck'
            if property_value == status_value:
                raise LookupError("'{0}' {1} already {2}.".format(label_name, property_type, property_value))
            core_utils.left_click(self, row_element)
        if property_type == 'radio_button':
            drop_down_element = pop_obj.get_element_in_dialog(self, label_name, "[role='radio'] .ibx-radio-button-simple-marker", label_name)
            element_class_attribute = drop_down_element.get_element_attribute(self, row_element, 'class')
            status_value = 'check' if 'ibx-check-box-simple-marker-check' in element_class_attribute else 'uncheck'
            if property_value == status_value:
                raise LookupError("'{0}' {1} already {2}.".format(label_name, property_type, property_value))
            core_utils.left_click(self, row_element)
    
    def verify_open_popup_dialog_from_action_bar(self, label_name, property_type, msg, property_value=None, comparison_type=None):
        '''
        Description : This is the function will verify new item in popup
        Example : verify_open_popup_dialog_from_action_bar('Title', 'text_box', 'Step 9', property_value='test')
        '''
        if property_type=='caption_tile':
            actual_value = pop_obj.get_caption_title(self)
            util_method.asequal(self, label_name, actual_value, msg)
        if property_type in ['text_box', 'drop_down_input_value']:
            input_box_element = pop_obj.get_element_in_dialog(self, label_name, "input", '{0} Input'.format(label_name))
            actual_value = util_method.get_element_attribute(self, input_box_element, 'value')
            util_method.asequal(self, property_value, actual_value, msg)
        if property_type == 'text_area':
            input_box_element = pop_obj.get_element_in_dialog(self, label_name, "textarea", '{0} Input'.format(label_name))
            actual_value = util_method.get_element_attribute(self, input_box_element, 'value')
            util_method.asequal(self, property_value, actual_value, msg)
        if property_type == 'drop_down':
            drop_down_css = '.hp-select-picker .ibx-select-open-btn'
            row_element = pop_obj.get_element_in_dialog(self, label_name, drop_down_css, label_name)
            core_utils.left_click(self, row_element)
            pop_obj.row_css=".ibx-select-item"
            current_drop_down_option_list = []
            all_row_element = pop_obj.get_row_elements(self)
            for option in all_row_element:
                current_drop_down_option_list.append(option.text.strip())
            pop_obj.row_css="> .ibx-dialog-main-box .ibx-flexbox-horizontal"
            core_utils.python_move_to_element(self, row_element)
            current_mouse_postion = pyautogui.position()
            core_utils.python_click_with_offset(self, int(current_mouse_postion[0])+19, int(current_mouse_postion[1]))
            util_method.as_List_equal(self, property_value, current_drop_down_option_list, msg)
            util_method.verify_list_values(self, current_drop_down_option_list, property_value, msg, assert_type=comparison_type)
        if property_type == 'check_box':
            row_element = pop_obj.get_element_in_dialog(self, label_name, "[role='checkbox'] .ibx-check-box-simple-marker", label_name)
            element_class_attribute = util_method.get_element_attribute(self, row_element, 'class')
            status_value = 'check' if 'ibx-check-box-simple-marker-check' in element_class_attribute else 'uncheck'
            util_method.asequal(self, property_value, status_value, msg)
        if property_type == 'radio_button':
            drop_down_element = pop_obj.get_element_in_dialog(self, label_name, "[role='radio'] .ibx-radio-button-simple-marker", label_name)
            element_class_attribute = drop_down_element.get_element_attribute(self, row_element, 'class')
            status_value = 'check' if 'ibx-check-box-simple-marker-check' in element_class_attribute else 'uncheck'
            util_method.asequal(self, property_value, status_value, msg)
        if property_type == 'text':
            message_text = pop_obj.get_element_in_dialog(self, property_value, "[data-ibx-name='message'].ibx-dialog-message", 'Popup Dmessage').text.strip()
            util_method.asequal(self, property_value, message_text, msg)
    
    def button_in_popup_dialog_from_action_bar(self, label_name, property_type, property_value=None, msg=None):
        '''
        Description : This is the function will click or verify on button inside popup.
        Example : button_in_popup_dialog_from_action_bar('OK', 'color_verify', property_value='Blue', msg='Step 9')
        '''
        if property_type == 'click':
            button_element = resc_obj.get_button_object(self, label_name)
            core_utils.left_click(self, button_element)
        if property_type == 'verify':
            button_element = resc_obj.get_button_object(self, label_name)
            actual_text = button_element.text.strip() if label_name.lower() != 'close' else util_method.get_element_attribute(self, button_element, 'title')
            util_method.asequal(self, label_name, actual_text, msg)
        if property_type == 'visibility':
            disable_css = "ibx-widget-disabled"
            button_element = resc_obj.get_button_object(self, label_name)
            element_class_attribute = util_method.get_element_attribute(self, button_element, 'class')
            actual_value = 'disable' if disable_css in element_class_attribute else 'enable'
            util_method.asequal(self, property_value, actual_value, msg)
        if property_type == 'color_verify':
            button_element = resc_obj.get_button_object(self, label_name)
            util_method.verify_element_color_using_css_property(self, None, property_value, msg, attribute='background-color', element_obj=button_element)
        
    def verify_popup_dialog_from_action_bar_is_displayed(self, visible_mode, msg):
        '''
        Description : This will verify popup dialog is displayed.
        Example : verify_popup_dialog_from_action_bar_is_displayed(True, 'Step 9: Verify')
        '''
        pop_obj.verify_poptop_dialog_is_visible(self, ".ibx-dialog-main-box[data-ibx-name='vbMain']", visible_mode, msg)  
        
    def get_action_bar_new_text_resource_tab_objects(self):
        """
        Description : This method will return all action bar new text resource tab buttons object as list
        """
        tabs_css = ".pop-top .ibx-csl-items-box [role='tab']"
        tab_objects = util_method.validate_and_get_webdriver_objects(self, tabs_css, "Home page action bar new text resource tabs")
        visble_tab_objects = [obj for obj in tab_objects if obj.is_displayed()]
        return visble_tab_objects
     
    def get_action_bar_new_text_resource_tab_name(self):
        """
        Description : This method will return all action bar new text resource tab button name as list
        """
        tab_objects = Wf_Mainpage.get_action_bar_new_text_resource_tab_objects(self)
        tab_name_list = [tab.text.strip() for tab in tab_objects]
        return tab_name_list
     
    def get_action_bar_new_text_resource_tab_object(self, tab_name):
        """
        Description : This method will return specific action bar new text resource tab button object
        """
        tab_button_list = Wf_Mainpage.get_action_bar_new_text_resource_tab_name(self)
        if tab_name in tab_button_list :
            tab_objects = Wf_Mainpage.get_action_bar_new_text_resource_tab_objects(self)
            tab_object = tab_objects[tab_button_list.index(tab_name)]
            return tab_object
        else :
            error_msg = "[{0}] tab doesn't displayed in action bar new text resource.".format(tab_name)
            raise ElementNotVisibleException(error_msg)
     
    def verify_action_bar_new_text_resource_tabs(self, expected_tabs_list, msg, assert_type='asequal'):
        """
        Description : This method will verify action bar new text resource tab buttons
        @usage  : verify_action_bar_new_text_resource_tabs(['Common', 'Data', 'Designer', 'InfoAssist', 'Schedule', 'Other'], 'Step 01.1 : Verify action bar tab buttons')
        """
        actual_tabs_list = Wf_Mainpage.get_action_bar_new_text_resource_tab_name(self)
        util_method.verify_list_values(self, expected_tabs_list, actual_tabs_list, msg, assert_type)
     
    def verify_action_bar_new_text_resource_tab_color(self, tab_name, expected_color_name, msg):
        """
        Description : This method will verify action bar new text resource tab button color
        @usage  : verify_action_bar_new_text_resource_tab_color('Common', 'blue', 'Step 01.01 : Verify 'Common' tab button color')
        """
        tab_object = Wf_Mainpage.get_action_bar_new_text_resource_tab_object(self, tab_name)
        util_method.verify_element_color_using_css_property(self, None, expected_color_name, msg, attribute='background-color', element_obj=tab_object)
     
    def verify_selected_action_bar_new_text_resource_tab(self, selected_tab, msg):
        """
        Description : This method will verify selected action bar new text resource tab
        @usage  : verify_selected_action_bar_new_text_resource_tab(['Common'], 'Step 01.01 : Verify 'Common' tab is selected as default')
        """
        selected_tab_css = ".pop-top [role='listbox'].ibx-csl-items-box [role='tab'].checked"
        selected_tab_obj = util_method.validate_and_get_webdriver_object(self, selected_tab_css, 'Selected action bar tab')
        actual_selected_tab = selected_tab_obj.text.strip()
        util_method.asequal(self, selected_tab, actual_selected_tab, msg)
         
    def select_action_bar_new_text_resource_tab(self, btn_name):
        '''
        Description : This function is used to select action bar new text resource tab
        :Usage select_action_bar_new_text_resource_tab('Designer')
        '''
        button_obj = Wf_Mainpage.get_action_bar_new_text_resource_tab_object(self, btn_name)
        core_utils.left_click(self, button_obj)
     
    def get_action_bar_new_text_resource_tab_option_objects(self):
        '''
        Descriptions : This method will return action bar new text resource selected tab option objects.
        usage : get_action_bar_new_text_resource_tab_option_objects()
        '''
        action_bar_btn_css = ".pop-top .tpg-selected .text-editor-file-type"
        action_bar_tab_options_obj = util_method.validate_and_get_webdriver_objects(self, action_bar_btn_css, "Home page action bar new text resource tab options.")
        visble_action_bar_tab_options_obj = [obj for obj in action_bar_tab_options_obj if obj.is_displayed()]
        return visble_action_bar_tab_options_obj
     
    def get_action_bar_new_text_resource_tab_options_name(self):
        '''
        Descriptions : This method will return action bar selected new text resource tab option objects.
        usage : get_action_bar_new_text_resource_tab_options_name()
        '''
        action_bar_tab_options_obj = Wf_Mainpage.get_action_bar_new_text_resource_tab_option_objects(self)
        action_bar_tab_options_names = [button.text.strip() for button in action_bar_tab_options_obj]
        return action_bar_tab_options_names
         
    def get_action_bar_new_text_resource_tab_option_object(self, option_name):
        """
        Description : This method will return specific action bar new text resource tab option object
        """
        tab_option_list = Wf_Mainpage.get_action_bar_new_text_resource_tab_options_name(self)
        if option_name in tab_option_list :
            option_objects = Wf_Mainpage.get_action_bar_new_text_resource_tab_option_objects(self)
            option_object = option_objects[tab_option_list.index(option_name)]
            return option_object
        else :
            error_msg = "[{0}] tab option doesn't displayed in action bar new text resource.".format(option_name)
            raise ElementNotVisibleException(error_msg)
     
    def select_action_bar_new_text_resource_tab_option(self, option_name):
        '''
        Descriptions : This method will select action bar new text resource tab option
        usage : select_action_bar_new_text_resource_tab_option('Page')
        '''
        option_object = Wf_Mainpage.get_action_bar_new_text_resource_tab_option_object(self, option_name)
        core_utils.left_click(self, option_object)
     
    def verify_action_bar_new_text_resource_tab_options(self, expected_options_list, msg, assert_type='asequal'):
        '''
        Descriptions : This method will verify action bar new text resource tab option
        usage : verify_action_bar_new_text_resource_tab_options(['Page'], 'Step 9: Verify')
        '''
        actual_options_list = Wf_Mainpage.get_action_bar_new_text_resource_tab_options_name(self)
        util_method.verify_list_values(self, expected_options_list, actual_options_list, msg, assert_type)
    
    def verify_resource_dialog_is_displayed(self, visible_mode, msg):
        '''
        Descriptions : This method will verify resource dialog is displayed.
        usage : verify_resource_dialog_is_displayed(True, 'Step 9: Verify')
        '''
        resc_obj.verify_resource_dialog_is_visible(self, visible_mode, msg)
    
    def verify_resource_dialog_caption_title(self, expected_title, msg):
        '''
        Descriptions : This method will verify resource dialog caption title.
        usage : verify_resource_dialog_caption_title('Select', 'Step 9: Verify')
        '''
        actual_title = resc_obj.get_caption_title(self) 
        util_method.asequal(self, expected_title, actual_title, msg)
    
    def verify_upload_message(self, file_name, msg, uploaded_msg=None, color_name=None):
        '''
        Descriptions : This method will verify upload dialog message.
        usage : verify_upload_message(''Bluehills.jpg'', 'Step 9: Verify', uploaded_msg='Bluehills.jpg upload completed', color_name='green')
        '''
        message_text_element = pop_obj.get_row_element_according_to_text_string(self, file_name, 'Popup Dmessage')
        if color_name:
            util_method.verify_element_color_using_css_property(self, '.upload-file-status-ok', color_name, msg, attribute='color', element_obj=message_text_element)
        else:
            actual_text = message_text_element.text.strip().replace('\n',' ')
            util_method.asequal(self, uploaded_msg, actual_text, msg)
    
    def upload_file_using_action_bar(self, upload_file_list, file_path_location="\\\ibirisc2\\bipgqashare\\Images_and_Things\\"):
        """
        Desc: This function uploads files in homepage using Upload_File action bar
        :param file_name='upload.png'
        :usage upload_file_using_action_bar('uload.png')
        """
        browser = Global_variables.browser_name
        for i in range(len(upload_file_list)):
            if i > 5:
                print("You have crossed maximum number of uploads.")
                break
            time.sleep(2)
            f_name=file_path_location + upload_file_list[i]
            if sys.platform == 'linux':
                time.sleep(3)
                pykeyboard.press_key(pykeyboard.control_key)
                pyautogui.press('l')
                pykeyboard.release_key(pykeyboard.control_key)
                time.sleep(3)
                clipboard.copy(f_name.replace('ibirisc2','se_workspace').replace('\\','/').replace(',{0}'.format(browser),''))
                time.sleep(5)
                pykeyboard.press_key(pykeyboard.control_key)
                pykeyboard.tap_key(character=u'\u0076')
                pykeyboard.release_key(pykeyboard.control_key)
                pykeyboard.tap_key(pykeyboard.enter_key)
            else:
                window_upload_ = automation.WindowControl(ClassName="#32770")
                upload_file_ = window_upload_.EditControl(ClassName="Edit")
                upload_file_.Exists(maxSearchSeconds=29, searchIntervalSeconds=1)
                upload_file_.SetFocus()
                window_upload_.SendKeys(f_name, waitTime=3)
#                 window_upload_.ButtonControl(Name="Open", foundIndex=3).MoveCursor()
                window_upload_.ButtonControl(Name="Open", foundIndex=3).Click()
#             temp_obj = subprocess.Popen(os.getcwd()+"\\common\\lib\\Upload_File1.exe "+f_name)
#             del temp_obj
            time.sleep(7)
        time.sleep(2)

    def get_master_file_data(self, file_folder_name):
        """
        Desc: This function will get master file folder or master file and return
        :usage get_master_file_data('car.mas')
        """
        file_folder_css = WfMainPageLocators.master_file_css
        file_select_obj = util_method.validate_and_get_webdriver_object(self, WfMainPageLocators.master_file_container_css, 'select_master_file_dialog')
        file_select_obj_location_top_middle_y = int(core_utils.get_web_element_coordinate(self, file_select_obj, element_location='top_middle')['y'])
        file_select_obj_location_bottom_middle_y = int(core_utils.get_web_element_coordinate(self, file_select_obj, element_location='bottom_middle')['y'])
        core_utils.python_move_to_element(self, file_select_obj)
        util_method.synchronize_with_visble_text(self, file_folder_css.format(file_folder_name), file_folder_name, Wf_Mainpage.home_page_medium_timesleep)
        file_obj = util_method.validate_and_get_webdriver_object(self, file_folder_css.format(file_folder_name), file_folder_name)
        object_location = int(core_utils.get_web_element_coordinate(self, file_obj, element_location='top_middle')['y'])
        direction = 'up' if  object_location < file_select_obj_location_top_middle_y else 'down'
        status_ = True
        while status_:
            object_location_top_middle = int(core_utils.get_web_element_coordinate(self, file_obj, element_location='top_middle')['y'])
            object_location_bottom_middle = int(core_utils.get_web_element_coordinate(self, file_obj, element_location='bottom_middle')['y'])
            if direction == 'up' and object_location_top_middle <= file_select_obj_location_top_middle_y:
                util_method.mouse_scroll(self, direction, 1, option='uiautomation', pause=2)
            elif direction == 'down' and object_location_bottom_middle >= file_select_obj_location_bottom_middle_y:
                util_method.mouse_scroll(self, direction, 1, option='uiautomation', pause=2)
            else:
                status_ = False
        return (file_obj)
    
    def select_master_file_or_folder(self, file_folder_name, click_type='left'):
        """
        Desc: This function will select master file folder or master file and return
        :usage select_master_file_or_folder('car.mas', click_type='double')
        """
        file_obj = Wf_Mainpage.get_master_file_data(self, file_folder_name)
        if click_type == 'left':
            core_utils.python_left_click(self, file_obj)
        elif click_type == 'double':
            core_utils.python_doubble_click(self, file_obj)
        
    def select_crumb_item_from_resource_dialog(self, crumb_item_name, selection_type='left'):
        """
        Desc: This function will select crumb item from resource dialog
        :usage select_crumb_item_from_resource_dialog('car.mas', click_type='double')
        """
        resc_obj.select_crumb_item(self, crumb_item_name, selection_type=selection_type)
    
    def select_file_or_folder_from_resource_dialog(self, resource_name, selection_type='left', view_type="list_view"):
        """
        Desc: This function will select file or folder from resource dialog
        :usage select_file_or_folder_from_resource_dialog('car.mas', click_type='double')
        """
        if view_type=='grid_view':
            resc_obj.select_resource_from_gridview(self, resource_name, selection_type=selection_type)
        elif view_type=='list_view':
            resc_obj.select_resource_from_listview(self, resource_name, selection_type=selection_type)
    
    def get_list_view_content_item_object(self, item_name):
        """
        Descriptions :  Return the lsit view content area item object
        example usage : get_list_view_content_item_object('P292')
        """
        item_css = ".files-listing:not([style*='none']) div[title='{0}']".format(item_name)
        item_object_list = self.driver.find_elements_by_css_selector(item_css)
        if len(item_object_list) > 0 :
            item_object = item_object_list[0]
            j_script.scrollIntoView(self, item_object)
            return item_object
        else :
            error_msg = "[{0}] file not found in list view content area".format(item_name)
            raise KeyError(error_msg)
    
    def double_click_content_item_in_list_view(self, item_name, folder_path=None, folder_index=0):
        """
        Description : double click on content file in list view.
        :arg - folder_path : If you want expand folders then pass folder path
        :Usage : double_click_content_item_in_list_view("C123456")
        """
        (folder_path!=None) and Wf_Mainpage.expand_repository_folders(self, folder_path, folder_index)
        item_object = Wf_Mainpage.get_list_view_content_item_object(self, item_name)
        core_utils.double_click(self, item_object)
        
    def verify_selected_resource_tree_item(self, expected_item_list, step_num):
        """
        Description : This method will verify selected resource tree item by comparing background-color value
        :Usage : verify_selected_resource_tree_item(['G435182'], "01.01")
        """
        selected_items = self.driver.find_elements_by_css_selector("div[class='ibfs-tree'] .ibfs-item-selected")
        actual_item_list = [item.text.strip() for item in selected_items if Color.from_string(item.value_of_css_property('background-color')).rgba == 'rgba(53, 184, 254, 0.4)']
        msg = "Step {0} : Verify {1} is selected in resource tree".format(step_num, expected_item_list)
        util_method.asequal(self, expected_item_list, actual_item_list, msg)
    
    def get_content_item_object_by_type(self, content_item_name, content_type):
        """
        Description : Return the content item object by its type.
        :arg - type = type of the content item. Type can be 'Folder', 'Portal', 'Fex'.
        """
        content_type_css = {'folder' : '.fa-folder', 'portal' : '.ibx-glyph-portal'}
        if Wf_Mainpage.is_grid_view(self) :
            xpath = "//div[contains(@id, 'files-box-area')][not(contains(@style, 'none'))] //div[normalize-space()='{0}'][contains(@class, 'fbx-column')]".format(content_item_name)
            content_objects = self.driver.find_elements_by_xpath(xpath)
        elif Wf_Mainpage.is_list_view(self) :
            css = "div.files-listing:not([style*='none']) div[title='{0}']".format(content_item_name)
            content_objects = self.driver.find_elements_by_css_selector(css)
        else :
            raise RuntimeError("Content are not visible")
        if content_type in content_type_css :
            type_css = content_type_css[content_type]
        else :
            raise NotImplementedError(content_type)
        for content in content_objects :
            type_object = content.find_elements_by_css_selector(type_css)
            if len(type_object) >0 :
                j_script.scrollIntoView(self, content)
                return content
        else :
            error = "{0} {1} not exists in content area.".format(content_item_name, content_type)
            raise FileNotFoundError(error)
            
    def is_grid_view(self):
        """
        Return True if content area in List view else False
        """
        list_view_css = "div.files-box-files:not([style*='none']"
        list_view = self.driver.find_elements_by_css_selector(list_view_css)
        if len(list_view) > 0 :
            return True
        else :
            return False
    
    def is_list_view(self):
        """
        Return True if content area in List view else False
        """
        list_view_css = "div.files-listing:not([style*='none'])"
        list_view = self.driver.find_elements_by_css_selector(list_view_css)
        if len(list_view) > 0 :
            return True
        else :
            return False
    
    def delete_exists_folder_and_create_new(self, folder_name):
        """
        Description : Delete exists folder in content area and create new folder
        :Usage : delete_exists_folder_and_create_new("Test folder")
        """
        ok_button_css = ".pop-top .ibx-dialog-ok-button"
        folder_obj = Wf_Mainpage.get_content_item_object_by_type(self, folder_name, 'folder')
        core_utils.right_click(self, folder_obj)
        Wf_Mainpage.select_context_menu_item(self, "Delete")
        util_method.synchronize_with_visble_text(self, ok_button_css, "OK", 10)
        ok_button = self.driver.find_element_by_css_selector(ok_button_css)
        core_utils.left_click(self, ok_button)
        time.sleep(4)
        Wf_Mainpage.select_action_bar_tab_option(self, 'Folder')
        util_method.synchronize_with_visble_text(self, '.pop-top', "New Folder", 12)
        Wf_Mainpage.create_new_folder(self, folder_name)
    
    def check_tags_in_homepage(self,tag_name):
        """
        Description : this method is used to click tags in homepage(ref enhancements tag section)
        :usage:check_tags_in_homepage("Personal")
        """
        tags_css = ".sd-category-buttons div[data-ibx-type='ibxButton']"
        tags_elem=util_method.validate_and_get_webdriver_objects(self, tags_css, "Home_page_tags")
        for tag in tags_elem:
            if tag.text == tag_name:
                core_utils.left_click(self,tag)
                break
        else:
            msg=("[{0}] item not listed under the tags.".format(tag_name))
            print(msg)   
        
class Run(BasePage):
    
    def __init__(self, driver):
        super(Run, self).__init__(driver)   
        
    def verify_title(self, expected_title_list, step_num):
        """
        Description : Verify home page run dialog title
        Usage : verify_title(["C123456"], "10.01")
        """    
        util_method.synchronize_until_element_is_visible(self, WfMainPageLocators.run_title_css, 15)
        title_obj = util_method.validate_and_get_webdriver_objects(self, WfMainPageLocators.run_title_css, "Home page run dialog title")
        actual_title = [title.text.strip() for title in title_obj]
        msg = "Step {0} : Verify {1} title displayed in home page run window".format(step_num, expected_title_list)
        util_method.asequal(self, expected_title_list, actual_title, msg)
    
    def switch_to_frame(self):
        """
        Description : Switch to run frame
        Usage : switch_to_frame()
        """
        core_utils.switch_to_frame(self, WfMainPageLocators.run_frame_css)
    
    def close(self):
        """
        Description : Click on close icon to close run window.
        Usage : close()
        """
        util_method.synchronize_until_element_is_visible(self,  WfMainPageLocators.run_close_css, 10)
        close_icon_obj = util_method.validate_and_get_webdriver_object(self, WfMainPageLocators.run_close_css, "Home page run window close button")
        core_utils.left_click(self, close_icon_obj)
        util_method.synchronize_until_element_disappear(self, WfMainPageLocators.run_dialog_css, 8)
        
    def open_in_new_window(self):
        """
        Description : Click on open in new window button to open run file in new window
        Usage : open_in_new_window()
        """
        util_method.synchronize_until_element_is_visible(self,  WfMainPageLocators.run_open_in_new_window_css, 10)
        icon_obj = util_method.validate_and_get_webdriver_object(self, WfMainPageLocators.run_open_in_new_window_css, "Open in new window button")
        core_utils.left_click(self, icon_obj)
        core_utils.switch_to_new_window(self)
    
    def switch_to_default_content(self):
        """
        Description : Switch to default content from run window frame
        Usage : switch_to_default_content()
        """
        core_utils.switch_to_default_content(self)