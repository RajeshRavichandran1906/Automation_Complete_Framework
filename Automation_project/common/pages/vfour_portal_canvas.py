from common.lib import utillity
from common.lib.base import BasePage
from common.pages import vfour_miscelaneous, visualization_resultarea, vfour_portal_ribbon, vfour_portal_properties
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
import time, pyautogui, subprocess, os, re
from common.lib.root_path import ROOT_PATH
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as local_keyboard

class Vfour_Portal_Canvas(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Vfour_Portal_Canvas, self).__init__(driver)
         
        
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def select_page_in_navigation_bar(self, page_name):
        """
        Desc:This function is used to select page in navigation bar
    
        :param page_name='Page 1'
        :Param msg="Step 9: Verify Page 1 in Navigation Bar."
        :Usage select_page_in_navigation_bar('Page 1')
        """
        elems=self.driver.find_elements_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']")
        act=[el.text.strip() for el in elems]
        try:
            ele_obj=elems[act.index(page_name)]
            utillity.UtillityMethods.default_left_click(self,object_locator=ele_obj)
            print(page_name+" Page is clicked.")
        except NoSuchElementException:
            print(page_name+" Page is Not found.")
        time.sleep(2)
    
    def verify_page_in_navigation_bar(self, page_name, msg, verify=True, page_order_list=None):
        """
        Desc:This function is used to verify the page in navigation bar
  
        :param page_name='Page 1'
        verify=True(when page is present) OR False (page is not present)
        :Param msg="Step 9: Verify Page 1 in Navigation Bar."
        :Usage verify_page_in_navigation_bar('Page 1', "Step 9: Verify Page 1 in Navigation Bar.")
        """
        step_number = re.search(r'\d+', msg).group()
        elems=self.driver.find_elements_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']")
        act=[el.text.strip() for el in elems if el != '']
        if verify==True:
            utillity.UtillityMethods.asin(self, page_name, act, msg)
        if verify==False:
            utillity.UtillityMethods.as_notin(self, page_name, act, msg)
        if page_order_list is not None:
            utillity.UtillityMethods.as_List_equal(self, act, page_order_list, "Step "+step_number+".a: Pages are Ordered in Navigation bar.")
        
    def add_page(self, page_template_name, close_add_page_dialog='Create', page_verify=True, **kwargs):
        """
        Desc:This function first click to 'New page icon', then select selection option based on user choice.
        Finaly Click 'Create' option in Add page Dialog Box.
        :param page_template_name="1 Column" or "2 Column" or etc.... 
        :kwargs['Page_title']='Page 1'
        :kwargs['Page_name']='Page_1'
        :kwargs['change_location']='BIP_V4_Portal->Pages_Folder'
        :kwargs['verify_location']='/Repository/P292/S10117/BIP_V4_Portal/Pages_Folder'
        :kwargs['btn_name']='Create' or 'Cancel'
        :kwargs['close_browser_folder_dialog']='ok' or 'Cancel'
        :kwargs['msg']="Step 5: verify location text in add page dialog window."
        :Usage add_page('2 Column', Page_title='Page_designer1', Page_name='Page_designer1', change_location=change_location, close_browser_folder_dialog='ok', verify_location=location_text, msg="Step 8: Verify location after changed.", page_verify=False)
        """
        elem = self.driver.find_element_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipAddButton']")
        utillity.UtillityMethods.default_click(self, elem)
        time.sleep(2)
        page_title = vfour_miscelaneous.Vfour_Miscelaneous.select_page_template(self, page_template=page_template_name, btn_name=close_add_page_dialog, **kwargs)
        if page_verify is True:
            Vfour_Portal_Canvas.verify_page_in_navigation_bar(self, page_title, "Step X1 : Verify " + page_template_name + " Is added to the navigation bar.")
    
    def scroll_down_to_search_element(self, item_name, tabel_parent_css, tabel_row_css, scroll_css="div.bi-tree-view-body", elem_location=0):
        '''
        Desc:- Search element using java-script scroll attribute.
        :param item_name='What element need to search.'
        :param tabel_parent_css='Scroll parent element css-value.'
        :param tabel_row_css='element row css-value.'
        :param scroll_css='Actual scroll css-value.'
        :param elem_location='current element location need to scroll inside java-script.'
        :usage  scroll_down_to_search_element('Page_designer1', "#paneIbfsExplorer_exList", "#paneIbfsExplorer_exList > div.bi-tree-view-body-content > table > tbody > tr")
        '''
        tabel_scroll_css = tabel_parent_css + " " + scroll_css
        run_=True
        old_list=[]
        elem_location = elem_location
        scroll_elem=self.driver.find_element_by_css_selector(tabel_scroll_css)
        utillity.UtillityMethods.click_on_screen(self, scroll_elem, 'middle', y_offset=-9)
        time.sleep(2)
        utillity.UtillityMethods.click_on_screen(self, scroll_elem, 'middle')
        while run_:
            elems = self.driver.find_elements_by_css_selector(tabel_row_css)
            current_list = [elem.text.strip() for elem in elems if elem.text.strip() != '']
            if old_list == current_list:
                run_ = False
                break
            if item_name not in current_list:
                Vfour_Portal_Canvas.scroll_panel(self, 0, 0, 'down', option='uiautomation', number_of_times=1, waitTime=0.5)
                time.sleep(1)
            else:
                run_ = False
                break
            old_list=current_list.copy()
        return (elem_location)
        
    def select_file_from_ibfs_explorer(self, file_name_list, file_type=None, verify_repository_file_selected=None, msg='Step X', close_ibfs_open_dialog='Open'):
        """
        Desc:-Select file from IBFS explorer dialog.
        :param file_name_list='list of Files need to select.'
        :param file_type='File type need to select.'
        :Usage select_file_from_ibfs_explorer(['Page_designer1'])
        """
        ibfs_file_list_css="#paneIbfsExplorer_exList"
        table_row_css = ibfs_file_list_css+" > div.bi-tree-view-body-content > table > tbody > tr"
        file_css = table_row_css+ " td[class]:nth-child(1)"
        selected_element_css = table_row_css+ "[class*='selected'] td[class]:nth-child(1)"
        wait_css = "#paneIbfsExplorer_exList > div.bi-tree-view-body-content > table"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, wait_css, 1, 90)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
        else:
            local_keyboard.press('ctrl')
        elem_location=0
        for name in file_name_list:
            elem_location += Vfour_Portal_Canvas.scroll_down_to_search_element(self, name, ibfs_file_list_css, file_css, elem_location=elem_location)
            time.sleep(1)
            try:
                elems = self.driver.find_elements_by_css_selector(file_css)
                file_elem = elems[[name in elem for elem in [elem.text.strip() for elem in elems if elem.text.strip() != '']].index(True)]
            except ValueError:
                raise ValueError("File name '" + name + "' not exist.")
            file_elem_image = file_elem.find_element_by_css_selector("img[src*='16.png']")
            utillity.UtillityMethods.click_on_screen(self, file_elem_image, 'middle')
            time.sleep(1)
            utillity.UtillityMethods.default_click(self, file_elem_image)
            utillity.UtillityMethods.synchronize_with_visble_text(self, selected_element_css, name.replace(' ',''), 10)
        if sys.platform == 'linux':
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            local_keyboard.release('ctrl')
        if verify_repository_file_selected is not None:
            selected_list = [elem.text.strip() for elem in self.driver.find_elements_by_css_selector(selected_element_css) if elem != '']
            utillity.UtillityMethods.as_List_equal(self, verify_repository_file_selected, selected_list, msg+" : Verify '"+str(verify_repository_file_selected)+"' is selected from ibfs explorer.")
        if file_type != None:
            utillity.UtillityMethods.select_combobox_item(self,'IbfsOpenFileDialog7_cbFilterType', file_type)
            time.sleep(1)
        button_css = 'OK' if close_ibfs_open_dialog.lower() == 'open' else 'Cancel'
        button_elem = self.driver.find_element_by_id("IbfsOpenFileDialog7_btn" + button_css)
        utillity.UtillityMethods.default_click(self, button_elem)
        
    def open_files_from_repository_window(self, folder_path, file_name_list, file_type=None, verify_repository_file_selected=None, msg='Step X', close_ibfs_open_dialog='Open'):
        """
        Desc:- This function first expand folder in reposititory window form left hand side, then 'Enter file name' which need to open
        :param folder_path='P292->S10117->BIP_V4_Portal'
        :param file_name_list=['honda_integra']
        :param file_type='JPEG (*.jpg;*.jpeg;*.jpe)'
        :param close_ibfs_open_dialog='Close opened IBFS explorer dialog'
        :usage open_files_from_repository_window('P292->S10117->BIP_V4_Portal', ['honda_integra'], file_type='JPEG (*.jpg;*.jpeg;*.jpe)')
        @AAkhan
        """
        dialog_css="#dlgIbfsOpenFile7 [class*='active'] #paneIbfsExplorer_exTree"
        tree_css = dialog_css+" > div.bi-tree-view-body-content table tr"
        path = folder_path.split('->')[0]
        utillity.UtillityMethods.synchronize_with_number_of_element(self, dialog_css, 1, 10)
        Vfour_Portal_Canvas.scroll_down_to_search_element(self, path, dialog_css, tree_css)
        elems = self.driver.find_elements_by_css_selector(tree_css)
        if path not in [elem.text.strip() for elem in elems]:
            raise ValueError("File name '" + path + "' not exist.")
        elem=self.driver.find_element_by_css_selector(dialog_css)
        folder_index_number = vfour_miscelaneous.Vfour_Miscelaneous.expand_tree(self, folder_path, tree_css=tree_css, scroll_elem=elem)
        repository_items = self.driver.find_elements_by_css_selector(tree_css)
        td_img = repository_items[folder_index_number].find_element_by_css_selector("img.icon")
        utillity.UtillityMethods.click_on_screen(self, td_img, 'middle')
        time.sleep(1)
        utillity.UtillityMethods.default_click(self, td_img)
        time.sleep(9)
        Vfour_Portal_Canvas.select_file_from_ibfs_explorer(self, file_name_list, file_type=file_type, verify_repository_file_selected=verify_repository_file_selected, msg=msg, close_ibfs_open_dialog=close_ibfs_open_dialog)
    
    def add_page_change_location(self, add_page_css, folder_path, close_browser_folder_dialog='ok'):
        '''
        Desc:- Change the location of page where need to save inside add page dialog.
        :param add_page_css='Dialog css-value.'
        :param folder_path='New location path.'
        :param close_browser_folder_dialog='Close opened browse path dialog'
        :usage add_page_change_location("div[id='dlgTitleExplorer'] [class*='window'][class*='active']", 'BIP_V4_Portal->Pages_Folder')
        '''
        utillity.UtillityMethods.click_dialog_button(self, add_page_css, 'Change Location...')
        dialog_css = "#dlgIbfsBrowseForFile [class*='active'] #IbfsBrowseForFolderDlg_exTree"
        tree_css = dialog_css+" > div.bi-tree-view-body-content table tr"
        path = folder_path.split('->')[0]
        utillity.UtillityMethods.synchronize_with_number_of_element(self, dialog_css, 1, 10)
        parent_elem = self.driver.find_element_by_css_selector(dialog_css)
        utillity.UtillityMethods.click_on_screen(self, parent_elem, 'middle')
        Vfour_Portal_Canvas.scroll_down_to_search_element(self, path, dialog_css, tree_css)
        elems = self.driver.find_elements_by_css_selector(tree_css)
        if path not in [elem.text.strip() for elem in elems]:
            raise ValueError("File name '" + path + "' not exist.")
        vfour_miscelaneous.Vfour_Miscelaneous.expand_tree(self, folder_path, tree_css=tree_css)
#         repository_items = self.driver.find_elements_by_css_selector(tree_css)
#         elem_location = self.driver.execute_script("return arguments[0].offsetTop;", repository_items[folder_index_number])
        time.sleep(3)
#         scroll_elem=self.driver.find_element_by_css_selector(dialog_css+" [style*='overflow-y']")
#         self.driver.execute_script("return arguments[0].scrollTop="+str(elem_location), scroll_elem)
        time.sleep(3)
        elems = self.driver.find_elements_by_css_selector(tree_css)
        file_elem = elems[[folder_path.split('->')[-1] in elem for elem in [elem.text.strip() for elem in elems if elem.text.strip() != '']].index(True)]
        td_img = file_elem.find_element_by_css_selector("img.icon")
        utillity.UtillityMethods.click_on_screen(self, td_img, 'bottom_middle', click_type=0)
        time.sleep(1)
        button_css = 'OK' if close_browser_folder_dialog.lower() == 'ok' else 'Cancel'
        button_elem = self.driver.find_element_by_id("IbfsBrowseForFolderDlg_btn" + button_css)
        utillity.UtillityMethods.default_click(self, button_elem)
    
    def verify_add_page_location(self, location, msg):
        '''
        Desc:- Verify page location from text box inside add page dialog.
        :param location='location of the page.'
        :param msg='Assertion message.'
        :usage verify_add_page_location('/Repository/P292/S10117/BIP_V4_Portal/Pages_Folder', 'Step 1: Verify page location.')
        '''
        dialog_css = "div[id='dlgTitleExplorer'] [class*='window'][class*='active']"
        field_elem = self.driver.find_elements_by_css_selector(dialog_css + " input[id^='BiTextField']")
        location_path_text = field_elem[2].get_attribute('value')
        utillity.UtillityMethods.asequal(self, location_path_text, location, msg+": Verify location path text.")
    
    def close_add_page_dialog(self, dialog_css, button_name):
        '''
        Desc:- Close opened add page dialog.
        :param dialog_css='add page dialog css-value.'
        :param button_name='button name('create' or 'cancel') to close add page dialog.'
        :usage close_add_page_dialog("div[id='dlgTitleExplorer'] [class*='window'][class*='active']", 'Create')
        '''
        utillity.UtillityMethods.click_dialog_button(self, dialog_css, button_name)
        
    def add_page_with_existing_link(self, launch_point, click_existing_button_name, folder_path, file_name_list, file_type="Portal Pages (*.page)", close_ibfs_open_dialog='open', 
                                   title=None, name=None, location=None, change_location_select_path=None, close_browser_folder_dialog='ok', verify_repository_file_selected=None, msg='Step X', close_add_page_dialog='Create'):
        """
        Desc:This function first click to 'New page icon', then select selection option based on user choice.
        :param launch_point='Start this from page(already add page dialog opened) or navigation bar'
        :param click_existing_button_name='click option to take an action.'
        :param folder_path='Path of the file'
        :param  file_name_list='Files name list to select.'
        :Usage add_page_with_existing_link('page','Link To Existing Page...', 'P292->S10117->BIP_V4_Portal', ['Page_designer1', 'Page_designer_fluid'], close_add_page_dialog=None)
        """
        dialog_css = "div[id='dlgTitleExplorer'] [class*='window'][class*='active']"
        option_dict = {'title':"input[id^='BiTextField']", 'name':"input[id^='BiTextField']", 'location':"input[id^='BiTextField']"}
        if launch_point == "navigation_bar":
            try:
                elem = self.driver.find_element_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipAddButton']")
                utillity.UtillityMethods.default_click(self, elem)
            except NoSuchElementException:
                raise ValueError("New page css value 'div[id^='BipNavigatorTop'] div[id^='BipAddButton']' not found.")
        utillity.UtillityMethods.synchronize_with_number_of_element(self, dialog_css, 1, 15)
        if click_existing_button_name in ['Link To Existing Page...','Copy Existing Page...']:
            utillity.UtillityMethods.click_dialog_button(self, dialog_css, click_existing_button_name)
        Vfour_Portal_Canvas.open_files_from_repository_window(self, folder_path, file_name_list, file_type=file_type, verify_repository_file_selected=verify_repository_file_selected, msg=msg, close_ibfs_open_dialog=close_ibfs_open_dialog)
        if title is not None:
            field_elem = self.driver.find_elements_by_css_selector(dialog_css + " " + option_dict['title'])
            utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, str(title), text_box_elem=field_elem[0])
        if name is not None:
            field_elem = self.driver.find_elements_by_css_selector(dialog_css + " " + option_dict['name'])
            utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, str(name), text_box_elem=field_elem[1])
        if change_location_select_path is not None:
            Vfour_Portal_Canvas.add_page_change_location(self, dialog_css, change_location_select_path, close_browser_folder_dialog=close_browser_folder_dialog)
        if location is not None:
            Vfour_Portal_Canvas.verify_add_page_location(self, location, msg+": Verify location path text.")
        if close_add_page_dialog is not None:
            Vfour_Portal_Canvas.close_add_page_dialog(self, dialog_css, close_add_page_dialog)
        
    def manage_page_menu(self, page_name, manage_item, **kwargs):
        """
        Desc: This function is used to Handle Navigation page menu bar option
        function testing is pending
        """
        elems=self.driver.find_elements_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']")
        tab_elem=elems[[el.text.strip() for el in elems].index(page_name)]
        utillity.UtillityMethods.default_click(self, tab_elem, click_option=1)
        utillity.UtillityMethods.select_or_verify_bipop_menu(self, manage_item)
        time.sleep(2)
        if manage_item=="Change Title":
            try:
                el=tab_elem.find_element_by_css_selector("input[id^='BipNavEdit']")
                if sys.platform == 'linux':
                    pykeyboard.type_string(str(kwargs['change_title']))
                    time.sleep(1)
                    pykeyboard.tap_key(pykeyboard.enter_key)
                else:
                    local_keyboard.write(kwargs['change_title'])
                    time.sleep(1)
                    local_keyboard.send("enter")
            except NoSuchElementException:
                print("Proper page is not selected to change the title.")    
        if manage_item == "Page Layout":
            time.sleep(2)
            btns=self.driver.find_elements_by_css_selector("#ChooseLayoutPageWindow div[id^='BiToolBarRadioButton']")
            actual_btn_name_list=[el.text.strip() for el in btns]
            elem=btns[actual_btn_name_list.index(kwargs['page_layout'])]
            utillity.UtillityMethods.default_click(self, elem)
            time.sleep(2)
        if manage_item == "Refresh":
            pass
        if manage_item == "Remove":
            Vfour_Portal_Canvas.verify_page_in_navigation_bar(self, page_name, "Step X1: Verify "+page_name+" is removed.", verify=False)
        if manage_item == "Delete":
            Vfour_Portal_Canvas.verify_page_in_navigation_bar(self, page_name, "Step X1: Verify "+page_name+" is Deleted.", verify=False)
    
    def verify_page_menu(self, page_name, expected_menu_list, msg):
        """
        Desc:This function is used to verify page menu option.
        :param page_name='Page 1'
        :param expected_menu_list='Refresh', 'Page Layout
        :param msg=
        :Usage verify_page_menu(
        """
        elems=self.driver.find_elements_by_css_selector("div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']")
        tab_elem=elems[[el.text.strip() for el in elems].index(page_name)]
        utillity.UtillityMethods.click_on_screen(self, tab_elem, 'middle', click_type=0)
        action = ActionChains(self.driver)
        action.move_to_element(tab_elem).context_click(tab_elem).perform()
        time.sleep(2)
        del action
        bipopup_css="div[id^='BiPopup'][style*='inherit']"
        bipopups=self.driver.find_elements_by_css_selector(bipopup_css)
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector("table tr")
        actual_menu_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        status_ = False
        for elem in expected_menu_list:
            if elem in actual_menu_list:
                status_ = True
            else:
                status_ = False
                break
        utillity.UtillityMethods.asequal(self, status_, True, msg)
    
    def get_current_page(self):
        "Desc:This function used to get current page"
        elems = self.driver.find_elements_by_css_selector("[class*='bip-canvas'] [class*='bip-page']")
        for el in elems:
            if el.value_of_css_property('visibility') != 'hidden':
                return (el)
    
    def get_column_obj(self, column_no):
        '''
        Desc:This function Retrun column element.
        :Param : column_no = 1 or 2,3,4 ( Column number start from 1 )
        :Usage : get_column_obj(1)
         or 
        :Usage : get_column_obj(2)
        '''
        current_page = Vfour_Portal_Canvas.get_current_page(self)
        colums=current_page.find_elements_by_css_selector("[class*='bip-column']")
        return(colums[column_no-1])
    
    def select_column(self, column_no):
        """
        Desc:This function is selecet column in canvas.
        :Param : column_no = 1 or 2,3,4 ( Column number start from 1 )
        :Usage : select_column(1)
        """
        elem=Vfour_Portal_Canvas.get_column_obj(self, column_no)
        utillity.UtillityMethods.click_on_screen(self, elem, 'top_middle', click_type=0)
    
    def get_panel_obj(self, panel_name):
        """
        Desc:This function Retrun panel element.
        :param: panel_name='Panel 1'
        :Usage:  get_panel_obj('Panel 1')
        """
        current_page = Vfour_Portal_Canvas.get_current_page(self)
        panel_elems = current_page.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        try:
            return(panel_elems[[panel_name in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)])
        except:
            print(panel_name+" panel name not in list ", [el.text.strip() for el in panel_elems])
        
    def select_panel_border(self, panel_name, click_on_panel_location='middle'):
        '''
        Desc:This function is call to click on panel border
        '''
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        utillity.UtillityMethods.click_on_screen(self, elem, click_on_panel_location, click_type=0)
        
    def select_panel(self, panel_name):
        """
        Desc:This function is select column in canvas.
        :Param :panel_name='Panel 1'
        :Usage : select_panel('Panel 1')
        """
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        panel_titles = elem.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        panel_title=panel_titles[[elem.text.strip() for elem in panel_titles].index(panel_name)]
        utillity.UtillityMethods.click_on_screen(self, panel_title, 'middle')
        time.sleep(1)
        utillity.UtillityMethods.click_on_screen(self, panel_title, 'middle', click_type=0)
    
    def select_panel_in_column(self, column_no, panel_name):
        '''
        Desc:This function select panel in specific column.
        '''
        column_obj = Vfour_Portal_Canvas.get_column_obj(self, column_no)
        panel_elems = column_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        try:
            elem = panel_elems[[panel_name in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        except ValueError:
            raise ValueError(panel_name+" panel name not in list ", [el.text.strip() for el in panel_elems])
        panel_titles = elem.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        panel_title=panel_titles[[elem.text.strip() for elem in panel_titles].index(panel_name)]
        utillity.UtillityMethods.click_on_screen(self, panel_title, 'middle')
        time.sleep(1)
        utillity.UtillityMethods.click_on_screen(self, panel_title, 'middle', click_type=0)
        
    def select_accordian_panel_title(self, panel_name, accordian_title):
        """
         Desc:This function is select accordian panel title in canvas.
        :Param :panel_name='Panel 1'
        :Usage : select_accordian_panel_title('Panel 1')
        """
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        accordian_titles = elem.find_elements_by_css_selector("[id^='BipAccordionPane'] [id^='BipAccordionButton'] [class*='bip-accordion-button']")
        accordian_title=accordian_titles[[elem.text.strip() for elem in accordian_titles].index(accordian_title)]
        utillity.UtillityMethods.click_on_screen(self, accordian_title, 'middle')
        time.sleep(1)
        utillity.UtillityMethods.click_on_screen(self, accordian_title, 'middle', click_type=0)
    
    def verify_accordian_panel_title(self, panel_name, expectecd_list, msg):
        """
        Desc:This function is Verify accordian panel title in canvas.
        :Param :panel_name='Panel 1'
        :Param :expectecd_list=['Area 1', 'New Area']
        :Param :msg='some message to print'
        :Usage : select_panel('Panel 1')
        """
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        accordian_titles = elem.find_elements_by_css_selector("[id^='BipAccordionPane'] [id^='BipAccordionButton'] [class*='bip-accordion-button']")
        accordian_title_list=[elem.text.strip() for elem in accordian_titles]
        for title in expectecd_list:
            utillity.UtillityMethods.asin(self, title, accordian_title_list, msg)
        
    def verify_column_panel_caption(self, column_no, panel_name, msg):
        '''
        Desc:Verify column panel caption is exits column.
        :Param : column_no = 1 or 2,3,4 ( Column number start from 1 )
        :param : panel_name='Panel 1' or 'any panel name'
        :param : msg = 'Step X : Verify first panel title'
        :Usage : verify_column_caption(1,'Panel 1','Step 02 : Verify first panel title') 
        '''
        col_obj=Vfour_Portal_Canvas.get_column_obj(self, column_no)
        panel_elems = col_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
        panel_elem = panel_elems[[panel_name in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)]
        panel_titles=panel_elem.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        panel_title=panel_titles[[elem.text.strip() for elem in panel_titles].index(panel_name)].text.strip()
        utillity.UtillityMethods.asequal(self, panel_name, panel_title, msg)
    
    def verify_panel_caption(self, panel_name, msg):
        '''
        Desc:Verify panel caption is exits column.
        :param : panel_name='Panel 1' or 'any panel name'
        :param : msg = 'Step X : Verify first panel title'
        :Usage : verify_panel_caption('Panel 1','Step 02 : Verify first panel title') 
        '''
        panel_elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        actual_title=panel_elem.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']").text.strip()
        utillity.UtillityMethods.asequal(self, panel_name, actual_title, msg)
    
    def scroll_panel(self, x_scroll, y_scroll, scroll, option='pyautogui', number_of_times=0, waitTime=2):
        """
        Desc:This function is scroll Hscroll or Vscroll.
        :param x_scroll=10                            ''' Interger number only    '''
        :param y_scroll=10                            ''' Interger number only    '''
        :param scroll='up' or 'down'
        :param option='pyautogui' or 'autohotkey'        ''' Select tool to scroll '''
        :param number_of_times=10                            ''' Interger number only    '''
        :Usage scroll_panel(100, 0, 'up')
            OR
        :Usage scroll_panel(-100, 0, 'down')
            OR
        :Usage croll_panel(-10000, 0, 'down', option='autohotkey', number_of_times=100)
        """
        if option == 'pyautogui':
            if scroll == 'up':
                pyautogui.scroll(x_scroll, y_scroll, pause=2)
            elif scroll == 'down':
                pyautogui.scroll(-x_scroll, y_scroll, pause=2)
            else:
                print("Please Select Scroll 'up' or 'down' option.")
        elif option == 'autohotkey':
            if scroll == 'up':
                procesobj = subprocess.Popen(os.path.join(ROOT_PATH, 'mouse_scroll.exe WheelUp '+str(number_of_times)))
                procesobj.wait()
                del procesobj
            elif scroll == 'down':
                procesobj = subprocess.Popen(os.path.join(ROOT_PATH, 'mouse_scroll.exe WheelUp '+str(number_of_times)))
                procesobj.wait()
                del procesobj
            else:
                print("Please Select Scroll 'up' or 'down' option.")
        elif option == 'uiautomation':
            import uiautomation as automation
            if scroll == 'up':
                automation.WheelUp(int(number_of_times), waitTime=waitTime)
            elif scroll == 'down':
                automation.WheelDown(int(number_of_times), waitTime=waitTime)
            else:
                print("Please Select Scroll 'up' or 'down' option.")
        else:
            print("Please Select appropriate option to scroll.")
    
    def select_tabbed_panel(self, panel_name, tabbed_panel_title, **kwargs):
        '''
        Desc:This function is select tabbed panel title in canvas.
        Param :panel_name='Panel 1'
        Param :tabbed_panel_title='title name'
        '''
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        elems = elem.find_elements_by_css_selector("[id^='BipTabBar'] [id^='BipTabButton']")
        tabbed_panel_elem=elems[[elem.text.strip() for elem in elems].index(tabbed_panel_title)]
        elem_pos = kwargs['elem_pos'] if 'elem_pos' in kwargs else 'middle'
        utillity.UtillityMethods.click_on_screen(self, tabbed_panel_elem, elem_pos)
        time.sleep(1)
        utillity.UtillityMethods.click_on_screen(self, tabbed_panel_elem, elem_pos, click_type=0)

    def verify_tabbed_panel(self, panel_name, expected_list, msg):
        '''
        Desc:This function is Verify tabbed panel title in canvas.
        :Param :panel_name='Panel 1'
        :Param :expectecd_list=['Area 1', 'New Area']
        :Param :msg='some message to print'
        '''
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        elems = elem.find_elements_by_css_selector("[id^='BipTabBar'] [id^='BipTabButton']")
        title_list=[elem.text.strip() for elem in elems]
        utillity.UtillityMethods.asin(self, expected_list[0], title_list, msg)
        if len(expected_list)>1:
            for title in expected_list[1:]:
                utillity.UtillityMethods.asin(self, title, title_list, msg)

    def scroll_tabbed_panel(self,  panel_name, scroll_type, scroll_times):
        '''
        Desc:This function is Verify tabbed panel title in canvas.
        Param :panel_name='Panel 1'
        Param :scroll_type='right' OR 'left'
        Param :scroll_times=1,2,3...
        '''
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        scroll_time=1
        while scroll_time <= scroll_times:
            elem1=elem.find_element_by_css_selector("[id^='BipTabBar'] [id^='BiRepeatButton'][class*='scroll-"+scroll_type+"']")
            utillity.UtillityMethods.default_click(self, elem1)
            scroll_time+=1
            time.sleep(1)
        
    def select_easy_selector_path(self, folder_path, launch_point='bip_ribbon_bar', **kwargs): 
        """
        Desc:This function is used to select_easy_selector_path in bip ribbon
        :param: folder_path='P292->S10117->BIP_V4_Portal'
        :param: launch_point='bip_ribbon_bar' OR 'canvas_column' OR 'canvas_panel'
        :kwargs: column_no=2                                                                ''' Interger number only.    ''''
        :kwargs: panel_name='Panel 1' or 'any panel name'
        :kwargs: verify_msg='Message to print for output'
        :kwargs: button='OK' or 'Cancel'
        :Usage:  select_easy_selector_path('P292->S10117->BIP_V4_Portal', launch_point='bip_ribbon_bar', verify_msg='Step 2: verify BIP_V4_Portal exits', button='Ok')
            OR
        :Usage:  select_easy_selector_path('P292->S10117->BIP_V4_Portal', launch_point='canvas_column', column_no=2, panel_name='Panel 1', verify_msg='Step 2: verify BIP_V4_Portal exits', button='Ok')
            OR
        :Usage:  select_easy_selector_path('P292->S10117->BIP_V4_Portal', launch_point='canvas_panel', panel_name='Panel 1', verify_msg='Step 2: verify BIP_V4_Portal exits', button='Ok')
        """  
        if launch_point=='bip_ribbon_bar':
            vfour_portal_ribbon.Vfour_Portal_Ribbon.select_ribbon_item(self, 'Insert', 'Insert_EasySelector')
        elif launch_point=='canvas_column':
            col_obj = Vfour_Portal_Canvas.get_column_obj(self, kwargs['column_no'])
            panel_elems = col_obj.find_elements_by_css_selector("[class*='bip-container'] [id^='BiDockPanel']")
            elem = panel_elems[[el.text.strip() for el in panel_elems].index(kwargs['panel_name'])]
            elem1=elem.find_element_by_css_selector("[id^='BipContentArea'] [class*='easy-selector-image']")
            utillity.UtillityMethods.default_click(self, elem1)
        elif launch_point == 'canvas_panel':
            panel_elem = Vfour_Portal_Canvas.get_panel_obj(self, kwargs['panel_name'])
            elem = panel_elem.find_element_by_css_selector("[id^='BipContentArea'] [class*='easy-selector-image']")
            utillity.UtillityMethods.default_click(self, elem)
        elif launch_point == 'property_tab':
            vfour_portal_properties.Vfour_Portal_Properties.edit_input_control(self, kwargs['section'], kwargs['item_name'], kwargs['control'], **kwargs)
        else:
            print("Launch Point Parameter missing not found.")
        browse_for_folder_dialog_css = "#dlgIbfsBrowseForFile [class*='window'][class*='active']"
        parent_css = browse_for_folder_dialog_css+" [class*='window-caption']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, parent_css, 1, expire_time=25)
        item_name = folder_path.split('->')
        parent_css = browse_for_folder_dialog_css+" table>tbody>tr"
        if 'scroll' in kwargs:
            elem = self.driver.find_element_by_css_selector(browse_for_folder_dialog_css+" #IbfsBrowseForFolderDlg_exTree")
            utillity.UtillityMethods.click_on_screen(self, elem, 'middle')
            time.sleep(2)
            x = kwargs['x_scroll'] if 'x_scroll' in kwargs else 0
            y = kwargs['y_scroll'] if 'y_scroll' in kwargs else 0
            Vfour_Portal_Canvas.scroll_panel(self, x, y, kwargs['scroll'])
        elem=self.driver.find_element_by_css_selector("#IbfsBrowseForFolderDlg_exTree")
        vfour_miscelaneous.Vfour_Miscelaneous.expand_resource_tree(self, folder_path, tree_rows=parent_css, scroll_elem=elem)
        elems = self.driver.find_elements_by_css_selector(parent_css)
        elem = elems[[el.text.strip() for el in elems].index(item_name[-1])]
        if 'verify_msg' in kwargs:
            utillity.UtillityMethods.asequal(self, elem.text.strip(), item_name[-1], kwargs['verify_msg'])
        elem1=elem.find_element_by_css_selector("img[src*='folder'][src*='.png']")
        utillity.UtillityMethods.click_on_screen(self, elem1, 'bottom_middle', click_type=0)
        time.sleep(3)
        if 'button' in kwargs:
            btn_id = 'OK' if kwargs['button'] == 'OK' else 'Cancel'
            btn_css=browse_for_folder_dialog_css+" #IbfsBrowseForFolderDlg_btn" + btn_id
            elem=self.driver.find_element_by_css_selector(btn_css)
            utillity.UtillityMethods.default_click(self, elem)
            
    def select_easy_selector_item(self, canvas_value, item_name, option='panel' ,**kwargs):
        """
        Desc:This function is used to select item in esay selector select item dialog box.
        :param: panel_name='Panel 1' or 'any panel name'
        :param: item_name='Red' or 'any item name display in select item dialog box'
        :kwargs: button='OK' or 'Cancel'
        :Usage select_easy_selector_item('Panel 1', 'Red', button='Add')
            OR
        :Usage select_easy_selector_item('Panel 1', 'Red', button='Cancel')
        """
        if option == 'panel':
            temp_elem = Vfour_Portal_Canvas.get_panel_obj(self, canvas_value)
        elif option == 'column':
            temp_elem = Vfour_Portal_Canvas.get_column_obj(self, canvas_value)
        else:
            print(option+"Option is used to select easy selector element.")   
        if option is not 'frame':
            elem = temp_elem.find_element_by_css_selector("[class*='bip'][class*='easy'][class*='selector'][class*='image']")
            utillity.UtillityMethods.default_click(self, elem)
        parent_css = "[id^='dlgIbfsOpenFile'] [class*='active'] [class*='window-caption']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, parent_css, 1, expire_time=25)
        time.sleep(0.3)
        selector_items = self.driver.find_elements_by_css_selector("[id^='dlgIbfsOpenFile'] [class*='active'] #paneIbfsExplorer_exList table tr td")
        elem = selector_items[[elem.text.strip() for elem in selector_items].index(item_name)]
        utillity.UtillityMethods.default_click(self, elem.find_element_by_css_selector("img"))
        if 'button' in kwargs:
            btn_id = 'OK' if kwargs['button'] == 'Add' else 'Cancel'
            btn_css="[id*='dlgIbfsOpenFile'] [class*='active'] [id*='IbfsOpenFileDialog'][id*='_btn" + btn_id+"']"
            elem=self.driver.find_element_by_css_selector(btn_css)
            utillity.UtillityMethods.default_click(self, elem)
        
    def verify_banner_position(self,position,msg):
        '''
        Desc:This function is used to verify_banner_position
        
        :Param : position = 'left' or 'right' or 'bottom'
        :Param : msg =' Step X : Verify that the banner now appears on the left'
        :Usage : verify_banner_position('left','Step 02 : Verify that the banner now appears on the left')
        '''
        bip_page=self.driver.find_element_by_css_selector("div[class*='bip-page']")
        bip_page_x=int(bip_page.location['x'])
        bip_page_width=int(bip_page.size['width'])
        bip_page_height=int(bip_page.size['height'])
        if position=='left' :
            left_area=self.driver.find_element_by_css_selector("div[class*='bip-banner-left']")
            left_area_x=int(left_area.location['x'])
            left_area_width=int(left_area.size['width'])
            left_status=True if left_area.is_displayed()==True and left_area_x in range(0,5) and left_area_width<=bip_page_x else False
            utillity.UtillityMethods.asequal(self,True,left_status,msg)
        if position=='right' :
            right_area=self.driver.find_element_by_css_selector("div[class*='bip-banner-right']")
            right_area_x=int(right_area.location['x'])
            right_status=True if right_area.is_displayed()==True and bip_page_width<=right_area_x else False
            utillity.UtillityMethods.asequal(self,True,right_status,msg)
        if position=='bottom' :
            bottom_area=self.driver.find_element_by_css_selector("div[class*='bip-banner-bottom']")
            bottom_area_x=int(bottom_area.location['x'])
            bottom_area_y=int(bottom_area.location['y'])
            bottom_status=True if bottom_area.is_displayed()==True and bottom_area_x in range(0,5) and bip_page_height<=bottom_area_y else False
            utillity.UtillityMethods.asequal(self,True,bottom_status,msg)
    
    def verify_column_selected(self,column_no,border_outline,msg):
        '''
        Desc:This function is used to verify column selected
        :Param : column_no = 1 or 2,3..
        :Param : border_outline= 'top' or 'left' or 'right' or 'bottom'
        :Param : msg = 'Step X : Verify column selected and the outlines show'
        :Usage : verify_column_selected(1,'left','Step 01 : Verify column selected and the outlines show')
        '''
        column_obj=self.get_column_obj(column_no)
        utillity.UtillityMethods.default_click(self, column_obj)
        time.sleep(3)
        bwidth=column_obj.value_of_css_property('border-'+border_outline+'-width')
        bstyle=column_obj.value_of_css_property('border-'+border_outline+'-style')
        bcolor=Color.from_string(column_obj.value_of_css_property('border-'+border_outline+'-color')).rgb
        border_value=bwidth+bstyle+bcolor
        selected_columns=len(self.driver.find_elements_by_css_selector("div[class*='bip-page'] div[class*='bip-column'][class*='selection-marquee']"))
        status=True if border_value=='3pxdashedrgb(255, 0, 0)' and selected_columns==1 else False
        utillity.UtillityMethods.asequal(self,True,status,msg)
    
    def verify_selected_panel_border(self, panel_name, output_msg, border_width='3px', border_style='dashed', border_color='red'):
        '''
        Desc:This function is used to verify selected panel border
        :Param : Panel_name = 'Panel 1'
        :Param : border_outline= 'top' or 'left' or 'right' or 'bottom'
        :Param : msg = 'Step X : Verify column selected and the outlines show'
        :Usage : verify_column_selected(1,'left','Step 01 : Verify column selected and the outlines show')
        '''
        selected_panel_index=None
        current_page = Vfour_Portal_Canvas.get_current_page(self)
        try:
            selected_item = current_page.find_elements_by_css_selector("[class*='selection-marquee']")
        except NoSuchElementException:
            raise AttributeError("No Panel is selected or css_value not able to found in browser.")
        current_page_panels_list=[elem.text for elem in selected_item]
        for panel in current_page_panels_list:
            if panel_name in panel:
                selected_panel_index = current_page_panels_list.index(panel)
                break
        if selected_panel_index == None:
            raise IndexError(panel_name + " not selected.")
        else:
            selected_panel = selected_item[selected_panel_index]
            border_color = utillity.UtillityMethods.color_picker(self, str(border_color.lower()),  rgb_type='rgba')
            border_style = str(border_width) + str(border_style.lower()) + str(border_color)
            curent_stauts = Vfour_Portal_Canvas.verify_bip_page_border_style(self, selected_panel, border_style)
            utillity.UtillityMethods.asequal(self, True, curent_stauts, output_msg)
    
    def verify_bip_page_border_style(self, selected_element_object, border_style):
        '''
        Desc :- This function will calculate border top, left, right and bottom style attribute
        '''
        '''verification of top border    '''
        btopwidth=selected_element_object.value_of_css_property('border-top-width')
        btopstyle=selected_element_object.value_of_css_property('border-top-style')
        btopcolor=Color.from_string(selected_element_object.value_of_css_property('border-top-color')).rgba
        border_top_value=btopwidth+btopstyle+btopcolor
        status_top = True if border_top_value==border_style else False
        '''verification of left border    '''
        bleftwidth=selected_element_object.value_of_css_property('border-left-width')
        bleftstyle=selected_element_object.value_of_css_property('border-left-style')
        bleftcolor=Color.from_string(selected_element_object.value_of_css_property('border-left-color')).rgba
        border_left_value=bleftwidth+bleftstyle+bleftcolor
        status_left = True if border_left_value==border_style else False
        '''verification of right border    '''
        brightwidth=selected_element_object.value_of_css_property('border-right-width')
        brightstyle=selected_element_object.value_of_css_property('border-right-style')
        brightcolor=Color.from_string(selected_element_object.value_of_css_property('border-right-color')).rgba
        border_right_value=brightwidth+brightstyle+brightcolor
        status_right = True if border_right_value==border_style else False
        '''verification of bottom border    '''
        bbottomwidth=selected_element_object.value_of_css_property('border-bottom-width')
        bbottomstyle=selected_element_object.value_of_css_property('border-bottom-style')
        bbottomcolor=Color.from_string(selected_element_object.value_of_css_property('border-bottom-color')).rgba
        border_bottom_value=bbottomwidth+bbottomstyle+bbottomcolor
        status_bottom = True if border_bottom_value==border_style else False
        status = True if status_top == True and status_left == True and status_right == True and status_bottom == True else False
        return (status)
        
    def verify_panel_portal_list(self, panel_name, portal_name, msg):
        """
        Desc:This function will verify panel portal list
        :Param1 : panel_name='Panel 2'
        :Param2 : portal_name='BIP_xxx_Portal123_V4'    ''''Any portal name inside the added portal list in the panel'''
        :Param3 : msg='Step x : The given portal is present in the created panel'
        :@Usage : verify_panel_portal_list('Panel 2', 'BIP_xxx_Portal123_V4', 'Step x : The given portal is present in the created panel')
        :@Author : Bhaga
        """
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        portal_list_elem = elem.find_elements_by_css_selector("div[id^='BipPortalTree'] table>tbody>tr")
        status=False
        for elem in portal_list_elem:
            if elem.text.strip() == portal_name :
                status=True
                break
        utillity.UtillityMethods.asequal(self, True, status, msg)
        
    def verify_panel_image(self, panel_name, image_name, msg):
        """
        Desc:This function will verify panel image
        :Param1 : panel_name = 'Panel 3'
        :Param2 : image_name ='babydeer' or 'blue_hills' or 'Integra_honda'
        :Param3 : msg ='Step X: The added Image is present in the created panel'
        :@Usage : verify_panel_image('panel 3', 'babydeer, 'Step X: The added Image is present in the created panel')
        :@Author : Bhaga 
        """
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        image_obj = elem.find_element_by_css_selector("img").get_attribute('src')
        utillity.UtillityMethods.asin(self, image_name, image_obj, msg)
        
    def verify_panel_text(self, panel_name, text_msg, msg):
        """
        Desc:This function will verify panel text
        :Param1 : panel_name='Panel 4' or 'Panel 1'
        :Param2 : text_msg='testing text panel area'
        :Param3 : msg='Stepx: The given text is present in the added panel'
        :@Usage : verify_panel_text(self, 'Panel 4', 'testing text panel area'
        :@Author : Bhaga
        """
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        panel_text = elem.find_element_by_css_selector("textarea").get_property('value')
        utillity.UtillityMethods.asin(self, text_msg, panel_text, msg)
    
    def add_text_into_panel(self, panel_name, text_string):
        '''
        Desc:This function will add text into panel
        :Param1 : panel_name='Panel 1' or 'Panel 2'
        :Param2 : text_string="This is a sample text' or 'Any text message'
        :Param3 : msg='Step X: Verify the added string the created panel'
        :@Author: Bhaga
        '''
        elem=Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        panel_text_obj = elem.find_element_by_css_selector("textarea")
        utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, text_string, text_box_elem=panel_text_obj)
    
    def dragdrop_repository_item_to_canvas(self, item_path, canvas_type, canvas_value, drop_point='middle', tx_offset=0, ty_offset=0):
        '''
        Desc:This function will dragdrop repository item to canvas
        :Param : item_path = P116->S7067
        :param : canvas_type = 'column' or 'panel'
        :Param : canvas_value = 1 or 'Panel 1' Always provide int value to column and string value to panel
        :Param : drop_point = 'middle', 'top', 'left', 'right', 'bottom'
        :Usage : vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas('Retail Samples', 'column', 1)
        '''
        resoure_tree_elem = self.driver.find_element_by_css_selector("#bipResourcesPanel")
        utillity.UtillityMethods.click_on_screen(self, resoure_tree_elem, 'top_middle')
        time.sleep(9)
        vfour_miscelaneous.Vfour_Miscelaneous.expand_resource_tree(self, item_path)
        item_name=item_path.split('->')[-1]
        BIPtree_rows="#bipResourcesPanel #treeView table>tbody>tr"
        rows = self.driver.find_elements_by_css_selector(BIPtree_rows)
        td_img=''
        for i in range(len(rows)):
            td_item = BIPtree_rows + ":nth-child(" + str(i+1) + ")>td"
            get_td=self.driver.find_element_by_css_selector(td_item)
            if get_td.text == item_name:
                td_img = self.driver.find_element_by_css_selector(td_item + ">img.icon")
#                 self.driver.execute_script("arguments[0].scrollIntoView(true);", get_td)
#                 time.sleep(3)
                break
        if td_img != '':
            source_elem=td_img
            if canvas_type=='column':
                target_elem=Vfour_Portal_Canvas.get_column_obj(self, canvas_value)
            else:
                target_elem=Vfour_Portal_Canvas.get_panel_obj(self, canvas_value)  
            if drop_point!='middle': 
                vfour_miscelaneous.Vfour_Miscelaneous.drag_drop_in_bip(self, source_elem, target_elem, trg_cord_type=drop_point, tx_offset=tx_offset, ty_offset=ty_offset)
            else:
                vfour_miscelaneous.Vfour_Miscelaneous.drag_drop_in_bip(self, source_elem, target_elem, tx_offset=tx_offset, ty_offset=ty_offset)
        else:
            print(item_name+" not found in Web Resource tree.")
    
    def multi_select_dragdrop_repository_item_into_canvas(self, item_path_list, canvas_type, canvas_value, drop_point='middle', tx_offset=0, ty_offset=0):
        '''
        Desc:This is used to multi select dragdrop repository item into canvas
        :Param : item_path = P116->S7067
        :param : canvas_type = 'column' or 'panel'
        :Param : canvas_value = 1 or 'Panel 1' Always provide int value to column and string value to panel
        :Param : drop_point = 'middle', 'top', 'left', 'right', 'bottom'
        :Usage : vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas('Retail Samples', 'column', 1)
        '''
        resoure_tree_elem = self.driver.find_element_by_css_selector("#bipResourcesPanel")
        utillity.UtillityMethods.click_on_screen(self, resoure_tree_elem, 'top_middle')
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
        else:
            local_keyboard.press('ctrl')
        item_index_number=0
        for path in item_path_list:
            item_index_number = vfour_miscelaneous.Vfour_Miscelaneous.expand_resource_tree(self, path)
            item_name=item_path_list[0].split('->')[-1]
            BIPtree_rows="#bipResourcesPanel #treeView table>tbody>tr"
            rows = self.driver.find_elements_by_css_selector(BIPtree_rows)
            td_img = rows[item_index_number].find_element_by_css_selector("img.icon")
            utillity.UtillityMethods.click_on_screen(self, td_img, 'bottom_middle', click_type=0, y_offset=-1)
            item_index_number=0
        if sys.platform == 'linux':
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            local_keyboard.release('ctrl')
        if td_img != '':
            source_elem=td_img
            if canvas_type=='column':
                target_elem=Vfour_Portal_Canvas.get_column_obj(self, canvas_value)
            else:
                target_elem=Vfour_Portal_Canvas.get_panel_obj(self, canvas_value)  
            if drop_point!='middle': 
                vfour_miscelaneous.Vfour_Miscelaneous.drag_drop_in_bip(self, source_elem, target_elem, trg_cord_type=drop_point, tx_offset=tx_offset, ty_offset=ty_offset)
            else:
                vfour_miscelaneous.Vfour_Miscelaneous.drag_drop_in_bip(self, source_elem, target_elem, tx_offset=tx_offset, ty_offset=ty_offset)
        else:
            print(item_name+" not found in Web Resource tree.")
    
    def dragdrop_repository_item_to_responsive(self, item_path, canvas_type, canvas_value, drop_point='middle', tx_offset=0, ty_offset=0):
        '''
        Desc:This is used to dragdrop repository item into responsive container
        :Param : item_path = P116->S7067
        :param : canvas_type = 'column' or 'panel'
        :Param : canvas_value = 1 or 'Panel 1' Always provide int value to column and string value to panel
        :Param : drop_point = 'middle', 'top', 'left', 'right', 'bottom'
        :Usage : vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas('Retail Samples', 'column', 1)
        '''
        resoure_tree_elem = self.driver.find_element_by_css_selector("#bipResourcesPanel")
        utillity.UtillityMethods.click_on_screen(self, resoure_tree_elem, 'top_middle')
        vfour_miscelaneous.Vfour_Miscelaneous.expand_resource_tree(self, item_path)
        item_name=item_path.split('->')[-1]
        BIPtree_rows="#bipResourcesPanel #treeView table>tbody>tr"
        rows = self.driver.find_elements_by_css_selector(BIPtree_rows)
        td_img=''
        for i in range(len(rows)):
            td_item = BIPtree_rows + ":nth-child(" + str(i+1) + ")>td"
            get_td=self.driver.find_element_by_css_selector(td_item)
            if get_td.text == item_name:
                td_img = self.driver.find_element_by_css_selector(td_item + ">img.icon")
#                 self.driver.execute_script("arguments[0].scrollIntoView(true);", get_td)
                time.sleep(3)
                break
        if td_img != '':
            source_elem=td_img
            if canvas_type=='column':
                target_elem=Vfour_Portal_Canvas.get_column_obj(self, canvas_value)
            else:
                target_elem=Vfour_Portal_Canvas.get_panel_obj_in_responsive(self, canvas_value)  
            if drop_point!='middle': 
                vfour_miscelaneous.Vfour_Miscelaneous.drag_drop_in_bip(self, source_elem, target_elem, trg_cord_type=drop_point, tx_offset=tx_offset, ty_offset=ty_offset)
            else:
                vfour_miscelaneous.Vfour_Miscelaneous.drag_drop_in_bip(self, source_elem, target_elem, tx_offset=tx_offset, ty_offset=ty_offset)
        else:
            print(item_name+" not found in Web Resource tree.")
    
    
    def verify_canvas_type(self, canvas_type, msg, displayed=True):
        """
        Desc:This function is used to verify canvas type example: one column, fluid canvas, or four column.
        :param canvas_type='one column' or 'fluid canvas' or etc.,
        :param msg="Step 9: verify Fluid canvas is displayed"
        :param displayed=True or False
        :usage verify_canvas_type('fluid_canvas', "Step 5: Verify that the page layout has changed to Fluid canvas")
        """
        if canvas_type == 'fluid_canvas':
            try:
                status = self.driver.find_element_by_css_selector("[id^='BoxLayoutManager']").is_displayed()
            except NoSuchElementException:
                status = False
            utillity.UtillityMethods.asequal(self, displayed, status, msg)
    
    def get_panel_obj_in_responsive(self, panel_name):
        """
        Desc:This function Retrun panel element.
        :param: panel_name='Panel 1'
        :Usage:  get_panel_obj('Panel 1')
        """
        
        panel_elems = self.driver.find_elements_by_css_selector("[class*='bip-canvas'] [class*='bip-page']:not([style*='hidden']) [class*='bip-container'] [id^='BiDockPanel'] [class*='flex-panel-item']")
        return(panel_elems[[panel_name in el1 for el1 in [el.text.strip() for el in panel_elems]].index(True)])
        
    def select_panel_in_responsive(self, panel_name):
        """
        Desc:This function is select column in canvas.
        :Param :panel_name='Panel 1'
        :Usage : select_panel('Panel 1')
        """
        elem=Vfour_Portal_Canvas.get_panel_obj_in_responsive(self, panel_name)
        panel_titles = elem.find_elements_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']")
        panel_title=panel_titles[[elem.text.strip() for elem in panel_titles].index(panel_name)]
        utillity.UtillityMethods.click_on_screen(self, panel_title, 'middle', click_type=0)
    
    def verify_panel_caption_in_responsive(self, panel_name, msg):
        '''
        Desc:Verify panel caption is exits column.
        :param : panel_name='Panel 1' or 'any panel name'
        :param : msg = 'Step X : Verify first panel title'
        :Usage : verify_panel_caption('Panel 1','Step 02 : Verify first panel title') 
        '''
        panel_elem=Vfour_Portal_Canvas.get_panel_obj_in_responsive(self, panel_name)
        actual_title=panel_elem.find_element_by_css_selector("[id^='BiLabel'][class*='bip-title-bar']").text.strip()
        utillity.UtillityMethods.asequal(self, panel_name, actual_title, msg)
    
    def verify_tabbed_panel_in_responsive(self, panel_name, expectecd_list, msg):
        '''
        Desc:This function is Verify tabbed panel title in canvas.
        :Param :panel_name='Panel 1'
        :Param :expectecd_list=['Area 1', 'New Area']
        :Param :msg='some message to print'
        '''
        elem=Vfour_Portal_Canvas.get_panel_obj_in_responsive(self, panel_name)
        elems = elem.find_elements_by_css_selector("[id^='BipTabBar'] [id^='BipTabButton']")
        title_list=[elem.text.strip() for elem in elems]
        utillity.UtillityMethods.asin(self, expectecd_list[0], title_list, msg)
        if len(expectecd_list)>1:
            for title in expectecd_list[1:]:
                utillity.UtillityMethods.asin(self, title, title_list, msg)
    
    def manage_panel_title_menubar(self, panel_name, verify=True, **kwargs):
        panel_elem = Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        panel_elem.find_element_by_css_selector("[id^='BipTitleBarMenuButton'][class*='button']").click()
        if verify == True:
            utillity.UtillityMethods.select_or_verify_bipop_menu(self, verify=True, expected_popup_list=kwargs['expected_opt'], msg=kwargs['msg'])
        else:
            select_menu_option = kwargs['select_menu_opt']
            utillity.UtillityMethods.select_or_verify_bipop_menu(self, select_menu_option)
    
    def get_comments_section(self, comment_section_exist_in='page', panel_name=None):
        '''
        Desc:This function is return visible comment section object
        :Param comment_section_exist_in='page' or 'panel'
        :Param panel_name='Panel 1'
        :Usage get_comments_section(comment_section_exist_in='panel', panel_name='Panel 1')
        '''
        if comment_section_exist_in == 'page':
            curent_page = Vfour_Portal_Canvas.get_current_page(self)
            comments_objs = curent_page.find_elements_by_css_selector("[id*='BipAnnotationsTree']")
        elif comment_section_exist_in == 'panel' and panel_name is not None:
            panel_obj = Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
            comments_objs = panel_obj.find_elements_by_css_selector("[id*='BipAnnotationsTree']")
        for comment_section in comments_objs:
            if comment_section.value_of_css_property('visibility') == 'visible':
                return (comment_section)
    
    def verify_comment_section_displayed(self, msg, expected_display_status=True, comment_section_exist_in='page', panel_name=None):
        '''
        Desc:This funciton will check comment section is displayed on page or panel.
        :Param msg='Step 16: Verify'
        :Param expected_display_status=True or False
        :Param comment_section_exist_in='page' or 'panel'
        :Param panel_name='Panel 1'
        :Usage verify_comment_section_displayed("Step 16: Verify the Comment panel disappeared", expected_display_status=False, comment_section_exist_in='panel', panel_name='Panel 1')
        '''
        try:
            comments_section_obj = Vfour_Portal_Canvas.get_comments_section(self, comment_section_exist_in=comment_section_exist_in, panel_name=panel_name)
            displayed_status = comments_section_obj.is_displayed()
        except AttributeError:
            displayed_status = False
        utillity.UtillityMethods.asequal(self, expected_display_status, displayed_status, msg)
        
    def resize_comments_section(self, resize_direction, msg, comment_section_exist_in='page', panel_name=None, src_cord_type='middle', source_offset_x=0, source_offset_y=0, target_offset_x=0, target_offset_y=0):
        '''
        Desc:This function will resize the comment section.
        :Param resize_direction='resize_up' or 'resize_down' or 'resize_left' or 'resize_right'
        :Param msg='Step 16: Verify'
        :Param comment_section_exist_in='page' or 'panel'
        :Param panel_name='Panel 1'
        :Usage resize_comments_section_on_page('resize_down', "Step 9: Verify the page adjusts for size of the Comment panel", target_offset_y=45, comment_section_exist_in='panel', panel_name='Panel 1')
        '''
        comment_resize_image_css = "[id*='BoxSplitter'][style*='resize'] img[src*='splitter']"
        if comment_section_exist_in == 'page':
            comments_section_obj = Vfour_Portal_Canvas.get_current_page(self)
        elif comment_section_exist_in == 'panel' and panel_name is not None:
            comments_section_obj = Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
        try:
            comments_section_obj_ = comments_section_obj.find_element_by_css_selector(comment_resize_image_css)
        except NoSuchElementException:
            raise ValueError(comment_resize_image_css+" css of comment_resize_image is not exist")
        if resize_direction not in ['resize_up', 'resize_down', 'resize_left', 'resize_right']:
            raise ValueError(resize_direction.upper()+" direction is not Valid.")
        source_obj=utillity.UtillityMethods.get_object_screen_coordinate(self, comments_section_obj_, coordinate_type=src_cord_type, x_offset=source_offset_x, y_offset=source_offset_y)
        if resize_direction == 'resize_up':
            target_offset_x, target_offset_y = source_obj['x'], int(source_obj['y'])-int(target_offset_y)
        elif resize_direction == 'resize_down':
            target_offset_x, target_offset_y = source_obj['x'], int(source_obj['y'])+int(target_offset_y)
        elif resize_direction == 'resize_left':
            target_offset_x, target_offset_y = int(source_obj['y'])-int(target_offset_y), source_obj['y']
        elif resize_direction == 'resize_right':
            target_offset_x, target_offset_y = int(source_obj['y'])+int(target_offset_y), source_obj['y']
        vfour_miscelaneous.Vfour_Miscelaneous.drag_drop(self, source_obj['x'], source_obj['y'], target_offset_x, target_offset_y)
        source_obj1=utillity.UtillityMethods.get_object_screen_coordinate(self, comments_section_obj_, coordinate_type=src_cord_type, x_offset=source_offset_x, y_offset=source_offset_y)
        resize_status = True if source_obj1['y'] > source_obj['y'] else False
        utillity.UtillityMethods.asequal(self, True, resize_status, msg)
        
    def verify_comments_section_text(self, msg, comment_text=None, comment_section_exist_in='page', panel_name=None, login_username_key='mrid03'):
        '''
        Desc:This function will verify comment section as in list.
        :Param msg='Step 16: Verify'
        :Param comment_text='This is a test for a Page'
        :Param comment_section_exist_in='page' or 'panel'
        :Param panel_name='Panel 1'
        :Param login_username_key='mrid03' or 'mrid' or ...
        :Usage verify_comments_section_text("Step 8.1: Verify that the user matches the name that is first in the Menu Bar.", 'This is a test for a Page', comment_section_exist_in='panel', panel_name='Panel 1')
        '''
        if comment_text is not None:
            developer_username=utillity.UtillityMethods.parseinitfile(self, login_username_key)
            expected_comment_list=['Addcomment...', str(developer_username), str(comment_text.replace(' ','')), 'Reply...']
        else:
            expected_comment_list=['Addcomment...']
        try:
            comments_section_obj = Vfour_Portal_Canvas.get_comments_section(self, comment_section_exist_in=comment_section_exist_in, panel_name=panel_name)
        except:
            raise AttributeError("Comments Section is not exist on "+comment_section_exist_in.upper())
        comment_section_message_list = [comment_section_text.replace(' ','') for comment_section_text in comments_section_obj.text.split('\n') if comment_section_text!='' and comment_section_text!=' ']
        if comment_text is not None:
            del comment_section_message_list[2]
        utillity.UtillityMethods.as_List_equal(self, expected_comment_list, comment_section_message_list, msg)
    
    def add_comment_on_comment_section(self, comment_text, comment_section_exist_in='page', panel_name=None, pause_time=1):
        '''
        Desc:This function will add a comment in comment section on page or panel.
        :Param comment_text='This is a test for a Page'
        :Param comment_section_exist_in='page' or 'panel'
        :Param panel_name='Panel 1'
        :Param pause_time=1 or 5 or ...
        :Usage add_comment_on_comment_section('This is a test for a Panel', pause_time=2, comment_section_exist_in='panel', panel_name='IA_Chart1')
        '''
        add_comment_css="[id*='BipAnnotationsInnerBox'] [id^='BipAnnotationsLabel']"
        add_comment_editor_popup_css="#idannotationpopup[class*='annotations_popup']"
        add_comment_editor_css="iframe[id^='BiRichEdit'][class*='annotations'][class*='popup']"
        try:
            comments_section_obj = Vfour_Portal_Canvas.get_comments_section(self, comment_section_exist_in=comment_section_exist_in, panel_name=panel_name)
        except:
            raise AttributeError("Comments Section is not exist on "+comment_section_exist_in.upper())
        add_comment_obj = comments_section_obj.find_element_by_css_selector(add_comment_css)
        utillity.UtillityMethods.click_on_screen(self, add_comment_obj, 'middle', click_type=0)
        utillity.UtillityMethods.synchronize_with_visble_text(self, add_comment_editor_popup_css, 'Post', 50)
        add_comment_editor_popup_obj = self.driver.find_elements_by_css_selector(add_comment_editor_popup_css)
        for editor_pop in add_comment_editor_popup_obj:
            if editor_pop.value_of_css_property('visibility') == 'visible':
                editor_popup_obj = editor_pop
                break
        try:
            editor_popup_obj.find_elements_by_css_selector(add_comment_editor_css)
        except NoSuchElementException:
            raise AttributeError("Add Comment editor not found in DOM")
        utillity.UtillityMethods.click_on_screen(self, editor_popup_obj, 'middle', click_type=0, y_offset=-10)
        time.sleep(pause_time)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.press_key(character=u'\u0061')
            pykeyboard.release_key(character=u'\u0061')
            pykeyboard.release_key(pykeyboard.control_key)
            time.sleep(pause_time)
            pykeyboard.tap_key(pykeyboard.delete_key)
            time.sleep(pause_time)
            pykeyboard.type_string(str(comment_text), interval=1)
        else:
            local_keyboard.press('ctrl')
            local_keyboard.press('a')
            local_keyboard.release('a')
            local_keyboard.release('ctrl')
            time.sleep(pause_time)
            local_keyboard.send('del')
            time.sleep(pause_time)
            local_keyboard.write(comment_text, delay=0.5)
        time.sleep(pause_time)
        utillity.UtillityMethods.click_dialog_button(self, add_comment_editor_popup_css, 'Post')
    
    def verify_comment_section_location(self, comment_section_location, msg, comment_section_exist_in='page', panel_name=None):
        '''
        Desc:This function is get the actual location of comment section.
        Warning: Before verify page comment section location, Please hide panels comment section.
        :Param comment_section_location='Top' or 'Bottom' or 'Left' or 'Right'
        :Param msg='Step 16: Verify'
        :Param comment_section_exist_in='page' or 'panel'
        :Param panel_name='Panel 1'
        :Param pause_time=1 or 5 or ...
        :Usage verify_comment_section_location('Bottom', "Step 26: Verify Comment Section is Displayed on Bottom of the IA_Chart1 panel.", comment_section_exist_in='panel', panel_name='IA_Chart1')
        '''
        panel_resize_handle_css="[id*='BiResizeHandle'][class*='resize']"
        if comment_section_location not in ['Top', 'Bottom', 'Left', 'Right']:
            raise ValueError(comment_section_location.upper()+" direction is not Valid.")
        if comment_section_exist_in == 'page':
            '''page calculation'''
            page_obj = Vfour_Portal_Canvas.get_current_page(self)
            page_border_top=re.match('.*(\d+)[a-z|A-Z]*.', page_obj.value_of_css_property('border-top-width')).group(1)
            page_border_bottom=re.match('.*(\d+)[a-z|A-Z]*.', page_obj.value_of_css_property('border-bottom-width')).group(1)
            page_border_left=re.match('.*(\d+)[a-z|A-Z]*.', page_obj.value_of_css_property('border-left-width')).group(1)
            page_border_right=re.match('.*(\d+)[a-z|A-Z]*.', page_obj.value_of_css_property('border-right-width')).group(1)
            page_top = utillity.UtillityMethods.get_object_screen_coordinate(self, page_obj, coordinate_type='top_middle', y_offset=int(page_border_top))
            page_bottom = utillity.UtillityMethods.get_object_screen_coordinate(self, page_obj, coordinate_type='bottom_middle', y_offset=-int(page_border_bottom))
            page_left = utillity.UtillityMethods.get_object_screen_coordinate(self, page_obj, coordinate_type='left', x_offset=int(page_border_left))
            page_right = utillity.UtillityMethods.get_object_screen_coordinate(self, page_obj, coordinate_type='right', x_offset=-int(page_border_right))
            '''comment section calculation'''
            try:
                comment_obj = Vfour_Portal_Canvas.get_comments_section(self)
            except:
                raise AttributeError("Comments Section is not exist on "+comment_section_exist_in.upper())
            comment_top = utillity.UtillityMethods.get_object_screen_coordinate(self, comment_obj, coordinate_type='top_middle')
            comment_bottom = utillity.UtillityMethods.get_object_screen_coordinate(self, comment_obj, coordinate_type='bottom_middle')
            comment_left = utillity.UtillityMethods.get_object_screen_coordinate(self, comment_obj, coordinate_type='left')
            comment_right = utillity.UtillityMethods.get_object_screen_coordinate(self, comment_obj, coordinate_type='right')
            if comment_section_location.lower() == 'top':
                comment_section_status = True if page_top['y']==comment_top['y'] and page_bottom['y']>comment_bottom['y'] and page_left['x']==comment_left['x'] and  page_right['x']==comment_right['x'] else False
            elif comment_section_location.lower() == 'bottom':
                comment_section_status = True if page_top['y']<comment_top['y'] and page_bottom['y']==comment_bottom['y'] and page_left['x']==comment_left['x'] and  page_right['x']==comment_right['x'] else False
            elif comment_section_location.lower() == 'left':
                comment_section_status = True if page_top['y']==comment_top['y'] and page_bottom['y']==comment_bottom['y'] and page_left['x']==comment_left['x'] and  page_right['x']>comment_right['x'] else False
            elif comment_section_location.lower() == 'right':
                comment_section_status = True if page_top['y']==comment_top['y'] and page_bottom['y']==comment_bottom['y'] and page_left['x']<comment_left['x'] and  page_right['x']==comment_right['x'] else False
            utillity.UtillityMethods.asequal(self, comment_section_status, True, msg)
        elif comment_section_exist_in == 'panel' and panel_name is not None:
            '''panel calculation'''
            panel_obj = Vfour_Portal_Canvas.get_panel_obj(self, panel_name)
            panel_top = utillity.UtillityMethods.get_object_screen_coordinate(self, panel_obj, coordinate_type='top_middle')
            panel_bottom = utillity.UtillityMethods.get_object_screen_coordinate(self, panel_obj, coordinate_type='bottom_middle')
            panel_left = utillity.UtillityMethods.get_object_screen_coordinate(self, panel_obj, coordinate_type='left')
            panel_right = utillity.UtillityMethods.get_object_screen_coordinate(self, panel_obj, coordinate_type='right')
            '''get visible resize panel obj'''
            panel_resize_handle_objs=self.driver.find_elements_by_css_selector(panel_resize_handle_css)
            for resize_handler in panel_resize_handle_objs:
                if resize_handler.value_of_css_property('visibility') == 'visible':
                    resize_handler_obj = resize_handler
                    break
            panel_resize_handler_height = resize_handler_obj.size['height']
            '''comment section calculation'''
            try:
                comments_section_obj = Vfour_Portal_Canvas.get_comments_section(self, comment_section_exist_in=comment_section_exist_in, panel_name=panel_name)
            except:
                raise AttributeError("Comments Section is not exist on "+comment_section_exist_in.upper())
            comment_top = utillity.UtillityMethods.get_object_screen_coordinate(self, comments_section_obj, coordinate_type='top_middle', y_offset=int(panel_resize_handler_height))
            comment_bottom = utillity.UtillityMethods.get_object_screen_coordinate(self, comments_section_obj, coordinate_type='bottom_middle', y_offset=int(panel_resize_handler_height))
            comment_left = utillity.UtillityMethods.get_object_screen_coordinate(self, comments_section_obj, coordinate_type='left', y_offset=int(panel_resize_handler_height))
            comment_right = utillity.UtillityMethods.get_object_screen_coordinate(self, comments_section_obj, coordinate_type='right', y_offset=int(panel_resize_handler_height))
            if comment_section_location.lower() != 'bottom':
                raise KeyError("For Panel comment_section_location equal to bottom only")
            comment_section_status = True if panel_top['y']<comment_top['y'] and panel_bottom['y']==comment_bottom['y'] and panel_left['x']==comment_left['x'] and  panel_right['x']==comment_right['x'] else False
            utillity.UtillityMethods.asequal(self, comment_section_status, True, msg)
    
    def verify_no_drag_drop_icon_on_canvas(self, folder_path, target_elem, file_name, msg, **kwargs):
        '''
        Desc:This funciton is used to verify no drop icon on canvas page or panel.
        :usage verify_no_drag_drop_icon_on_canvas(BIP_Portal_Path+'->BIP_xxx_Portal123_V4 Resources->Test_Page', target_elem, 'C2324241', 'Step 9: verify', ty_offset=150, mouse_duration=1)
        '''
        move_duration=kwargs['mouse_move_duration'] if 'mouse_move_duration' in kwargs else 0
        resoure_tree_elem = self.driver.find_element_by_css_selector("#bipResourcesPanel")
        utillity.UtillityMethods.click_on_screen(self, resoure_tree_elem, 'top_middle')
        no_icon_drop_css = "img[id^='BiImage'][class*='bi-component'][src*='nodrop']"
        step_number = re.search(r'\d+', msg).group()
        utillobj = utillity.UtillityMethods(self.driver)
        BIPtree_rows="#bipResourcesPanel #treeView table>tbody>tr"
        index_number = vfour_miscelaneous.Vfour_Miscelaneous.expand_tree(self, folder_path, tree_css=BIPtree_rows)
        time.sleep(2)
        rows = self.driver.find_elements_by_css_selector(BIPtree_rows)
        td_img = rows[index_number].find_element_by_css_selector("img.icon")
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", rows[index_number])
        time.sleep(3)
        utillobj.click_on_screen(td_img, 'middle', click_type=0)
        time.sleep(2)
        cord_type=kwargs['cord_type'] if 'cord_type' in kwargs else 'middle' 
        source_offset_x=kwargs['sx_offset'] if 'sx_offset' in kwargs else 0
        source_offset_y=kwargs['sy_offset'] if 'sy_offset' in kwargs else 0
        target_offset_x=kwargs['tx_offset'] if 'tx_offset' in kwargs else 0
        target_offset_y=kwargs['ty_offset'] if 'ty_offset' in kwargs else 0
        pyautogui.FAILSAFE=False  
        source_obj=utillobj.get_object_screen_coordinate(td_img, coordinate_type=cord_type, x_offset=source_offset_x, y_offset=source_offset_y)
        source_obj_x=source_obj['x']
        source_obj_y=source_obj['y']
        target_obj=utillobj.get_object_screen_coordinate(target_elem, coordinate_type=cord_type, x_offset=target_offset_x, y_offset=target_offset_y)
        target_obj_x=target_obj['x']
        target_obj_y=target_obj['y']
        time.sleep(2)
        pyautogui.mouseDown(source_obj_x,source_obj_y)
        time.sleep(3)
        pyautogui.moveTo(target_obj_x, target_obj_y, duration=move_duration)
        time.sleep(19)
        utillobj.verify_object_visible(no_icon_drop_css, True, msg)
        time.sleep(9)
        utillobj.take_browser_screenshot(str(file_name)+'_Actual_Step'+str(step_number))
        pyautogui.mouseUp()
        time.sleep(2)
