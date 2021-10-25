from common.lib import utillity, javascript
from common.lib.base import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException,\
    StaleElementReferenceException
import time, os, pyautogui, subprocess, re
from common.pages import visualization_resultarea, vfour_portal_canvas
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods
from common.lib import root_path
import sys
if sys.platform == 'linux':
    from pymouse import PyMouse
    mouse_=PyMouse()
else:
    from uisoup import uisoup

class Vfour_Miscelaneous(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Vfour_Miscelaneous, self).__init__(driver)
         
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def create_portal(self, repository_path, portal_name, **kwargs):
        """
        folder_path = 'P116->S7068'
        folder_name=any name
        Syntax: create_domain_folder('Domain', 'bip')
        @author = Niranjan
        """
        folder_list=repository_path.split('->')
        if len(folder_list)>1:
            Vfour_Miscelaneous.expand_resource_tree(self, repository_path, **kwargs) 
        Vfour_Miscelaneous.select_repository_menu(self, folder_list[-1], 'New->Collaborative Portal') 
        elems=self.driver.find_elements_by_css_selector("div[id='dlgNewPortalDesigner'][style*='inherit'] input")
        utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, portal_name, text_box_elem=elems[0])
        utillity.UtillityMethods.click_dialog_button(self, "div[id='dlgNewPortalDesigner'][style*='inherit']", "Create")
        time.sleep(2)
        
    def select_page_template(self, **kwargs):
        """
        :kwargs['page_template']="1 Column" or "2 Column" or etc.... 
        :kwargs['Page_title']='Page 1'
        :kwargs['Page_name']='Page_1'
        :kwargs['btn_name']="Create" or "Cancel" or etc....
        :usage select_page_template(page_template="1 Column", Page_title="Page 1", Page_name="Page_1", change_location='S10117->BIP_V4_Portal', 
                                    verify_location='/Repository/P292/S10117/BIP_V4_Portal/Pages_Folder', msg='Step 1: Verify page location from add page dialog.',
                                    btn_name="Create")
        """
        dialog_css = "div[id='dlgTitleExplorer'] [class*='window'][class*='active']"
        if "page_template" in kwargs:
            try:
                elems=utillity.UtillityMethods.validate_and_get_webdriver_objects(self, "#dlgTitleExplorer div[id^='TileExplorerItem']", 'Page Template')
                template_object = elems[[el.text.strip() for el in elems].index(kwargs['page_template'])]
                CoreUtillityMethods.left_click(self, template_object)
            except NoSuchElementException:
                print("Page Template is not Found.") 
        if 'Page_title' in kwargs:
            field_elem=utillity.UtillityMethods.validate_and_get_webdriver_objects(self, "div[id='dlgTitleExplorer'][style*='left'] input[id^='BiTextField']", 'Page Title Input')
            utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, kwargs['Page_title'],  text_box_elem=field_elem[0])
            visualization_resultarea.Visualization_Resultarea.wait_for_property(self, None, None, expire_time=90, text_option='text_value', string_value=kwargs['Page_title'], parent_object=field_elem[0])
        if 'Page_name' in kwargs:
            field_elem=utillity.UtillityMethods.validate_and_get_webdriver_objects(self, "div[id='dlgTitleExplorer'][style*='left'] input[id^='BiTextField']", 'Page Name Input')
            utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, kwargs['Page_name'],  text_box_elem=field_elem[1])
            visualization_resultarea.Visualization_Resultarea.wait_for_property(self, None, None, expire_time=90, text_option='text_value', string_value=kwargs['Page_name'], parent_object=field_elem[1])
        field_elem = self.driver.find_elements_by_css_selector("div[id='dlgTitleExplorer'][style*='left'] input[id^='BiTextField']")
        page_title = field_elem[0].get_attribute('value')
        if 'change_location' in kwargs:
            vfour_portal_canvas.Vfour_Portal_Canvas.add_page_change_location(self, dialog_css, kwargs['change_location'], kwargs['close_browser_folder_dialog'])
        if 'verify_location' in kwargs:
            vfour_portal_canvas.Vfour_Portal_Canvas.verify_add_page_location(self, kwargs['verify_location'], kwargs['msg'])
        if "btn_name" in kwargs:
            utillity.UtillityMethods.click_dialog_button(self, "div[id='dlgTitleExplorer'][style*='left']", kwargs['btn_name'])
            time.sleep(2)
        return (page_title.strip())
    
    def verify_page_template(self, msg, **kwargs):
        """
        :param msg="Step 3: Verify when Portal Designer loads you are on the Layout tab"
        :kwargs['page_template']="1 Column" or "2 Column" or etc.... 
        :kwargs['Page_title']='Page 1'
        :kwargs['Page_name']='Page_1'
        :usage verify_page_template("Step 3: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
        """
        if "page_template" in kwargs:
            try:
                elems=self.driver.find_elements_by_css_selector("#dlgTitleExplorer div[id^='TileExplorerItem']")
                actual_column = elems[[el.text.strip() for el in elems].index(kwargs['page_template'])].text.strip()
                utillity.UtillityMethods.asequal(self, kwargs['page_template'], actual_column, msg)
            except NoSuchElementException:
                print("Page Template is not Found.")
        if 'Page_title' in kwargs:
            field_elem = self.driver.find_elements_by_css_selector("div[id='dlgTitleExplorer'][style*='inherit'] input[id^='BiTextField']")
            page_title = field_elem[0].get_attribute('value')
            utillity.UtillityMethods.asequal(self, page_title, kwargs['Page_title'], msg)
        if 'Page_name' in kwargs:
            field_elem = self.driver.find_elements_by_css_selector("div[id='dlgTitleExplorer'][style*='inherit'] input[id^='BiTextField']")
            page_name = field_elem[1].get_attribute('value')
            utillity.UtillityMethods.asequal(self, page_name, kwargs['Page_name'], msg)
        
    def expand_resource_tree(self, folder_path, scroll_elem=None, **kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        Syntax: expand_resource_tree('S7068->AR-RP-193')
        """
        if scroll_elem!=None:
            scroll_obj=scroll_elem
        else:
            scroll_obj=self.driver.find_element_by_css_selector("#treeContainer")
        utillity.UtillityMethods.click_on_screen(self, scroll_obj, 'middle')
        time.sleep(2)
        utillity.UtillityMethods.click_on_screen(self, scroll_obj, 'middle', y_offset=-9)
        tree_rows=kwargs['tree_rows'] if 'tree_rows' in kwargs else "#bipResourcesPanel #treeView table>tbody>tr"
        folder_list=folder_path.split('->')
        repository_tree_items = self.driver.find_elements_by_css_selector(tree_rows)
        resource_tree_items_list = javascript.JavaScript.get_elements_text(self, repository_tree_items)
        folder_img_elem=utillity.UtillityMethods.validate_and_get_webdriver_object(self, "td>img[class='icon']", 'Resource tree', parent_object=repository_tree_items[resource_tree_items_list.index(folder_list[0])])
        Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img_elem, scroll_range=9999, number_of_time=19, direction='up')
        for item in folder_list:
            repository_items = self.driver.find_elements_by_css_selector(tree_rows)
            resource_tree_list = javascript.JavaScript.get_elements_text(self, repository_items)
            if item not in resource_tree_list:
                raise LookupError(item+ " Not Exist in setup "+ self.driver.current_url)
            try:
                for i in range(len(repository_items)):
                    if repository_items[i].text.strip() == item:
                        try:
                            if item == folder_list[-1]:
                                folder_img = repository_items[i].find_element_by_css_selector("td>img.icon")
                            else:
                                folder_img = repository_items[i].find_element_by_css_selector("td>img[src*='triangle_collapsed']")
                            Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img, scroll_range=9999)
                            CoreUtillityMethods.python_left_click(self, folder_img)
                            time.sleep(3)
                            if item == folder_list[-1]:
                                return (i)
                        except:
                            if item == folder_list[-1]:
                                return (i)
                        break
            except NoSuchElementException as e:
                print(e,item + " not found in Tree view.")
        
    def right_click_resource_tree(self, item_name, **kwargs):                                                            
        """
        :Param : item_name = 'AR-RP-193'
        Syntax: right_click_resource_tree('AR-RP-193')
        """
        BIPtree_rows="#bipResourcesPanel #treeView table>tbody>tr"
        rows = self.driver.find_elements_by_css_selector(BIPtree_rows)
        for i in range(len(rows)):
            td_item = BIPtree_rows + ":nth-child(" + str(i+1) + ")>td"
            get_td=self.driver.find_element_by_css_selector(td_item)
            if get_td.text == item_name:
                td_img = self.driver.find_element_by_css_selector(td_item + ">img.icon")
#                 self.driver.execute_script("arguments[0].scrollIntoView(true);", get_td)
                time.sleep(3)
                utillity.UtillityMethods.click_on_screen(self, td_img, 'middle', click_type=1, **kwargs)
                
    def select_resource_menu(self, folder_path, menu_item, **kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Param : menu_item = 'Edit' or 'Run'
        Syntax: select_resource_menu('S7068->AR-RP-193', 'Run')
        """
        item_name=folder_path.split('->')[-1]
        Vfour_Miscelaneous.expand_resource_tree(self, folder_path, **kwargs)
        Vfour_Miscelaneous.right_click_resource_tree(self,item_name, **kwargs)
        menu_list = menu_item.split('->')
        for j in range(len(menu_list)):
            popups = self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit']")
            menu_items = popups[-1].find_elements_by_css_selector("table>tbody>tr>[class='text']")
            for i in range(len(menu_items)):
                if menu_items[i].text.strip() == menu_list[j]:
                    menu_items[i].click()
                    break
        utillity.UtillityMethods.switch_to_default_content(self, pause=2)
        
    def delete_resource_item(self, folder_path, option='Yes', **kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Param : option = 'Yes' or 'No'
        Syntax: delete_resource_item('S7068->AR-RP-193', option='Yes')
        @author = AAkhan
        """
        Vfour_Miscelaneous.select_resource_menu(self, folder_path, 'Delete', **kwargs)
        time.sleep(1.5)
        dialog_parent_id = kwargs['dialog_parent_id'] if 'dialog_parent_id' in kwargs else "[id^='BiOptionPane']"
        utillity.UtillityMethods.click_dialog_button(self, dialog_parent_id, option)
    
    def create_resource_folder(self, folder_path, folder_name, **kwargs):
        """
        folder_path = 'P116->S7068'
        folder_name=any name
        Syntax: create_resource_folder('Domain', 'bip')
        """
        Vfour_Miscelaneous.select_resource_menu(self, folder_path, 'New->Folder', **kwargs) 
        elem=self.driver.find_element_by_css_selector("#createFolderDialog input#newdesc")
        utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, folder_name, text_box_elem=elem)
        ok_btn=self.driver.find_element_by_css_selector("#createFolderDialog #btnOK")
        utillity.UtillityMethods.click_on_screen(self, ok_btn, 'middle', click_type=0, **kwargs)
        time.sleep(1.5)
    
    def verify_resource_folder_status(self, folder_path, msg, status='selected', **kwargs):
        """
        folder_path = 'P116->S7068'
        msg='9'        #Step number
        status='selected' OR 'unpublished' OR 'hidden'
        Syntax: verify_resource_folder_status('Public', '9', status='selected')
        """
        folder_list=folder_path.split('->')
        Vfour_Miscelaneous.expand_resource_tree(self, folder_path, **kwargs)
        status_code={'selected':'png', 'unpublished':'0.6', 'hidden':'0.3'}
        BIPtree_rows="#bipResourcesPanel #treeView table>tbody>tr"
        repository_items = self.driver.find_elements_by_css_selector(BIPtree_rows)
        for i in range(1,len(repository_items)):
            if repository_items[i].text.strip() == folder_list[-1]:
                ret=self.driver.find_element_by_css_selector(BIPtree_rows + ":nth-child("+str(i+1)+")>td>img:nth-child(2)").get_attribute("src").endswith(status_code[status])
                break
        utillity.UtillityMethods.asequal(self,True, ret, "Step "+str(msg)+": Verify "+folder_list[-1]+" Folder is "+status+".")
    
    def verify_resource_item(self, folder_path, item_name, msg, item_exit=True, **kwargs):
        """
        folder_path = 'P116->S7068'
        item_name= 'S7067'
        msg='9'            #Step number
        item_exit=Ture or False
        Syntax: verify_resource_item('P116', 'S7067', '9', item_exit=True)
        """
        Vfour_Miscelaneous.expand_resource_tree(self, folder_path, **kwargs)
        BIPtree_rows="#bipResourcesPanel #treeView table>tbody>tr"
        tree_rows=kwargs['tree_rows'] if 'tree_rows' in kwargs else BIPtree_rows
        repository_items = self.driver.find_elements_by_css_selector(tree_rows)
        if item_exit == True:
            statx = item_name in [i.text.strip() for i in repository_items]
            file_name = item_name if statx is True else '{0} not exist under {1} repository'.format(item_name, folder_path)
            utillity.UtillityMethods.asequal(self,item_name, file_name, "Step "+str(msg)+": Verify " + item_name + " File or Folder is Avialable.")
        else:
            statx = item_name not in [i.text.strip() for i in repository_items]
            file_name = item_name if statx is True else '{0} is exist under {1} repository'.format(item_name, folder_path)
            utillity.UtillityMethods.asequal(self, item_name, file_name, "Step "+str(msg)+": Verify " + item_name + " File or Folder is Not Avialable.")
    
    def insert_image_or_file_from_bip_canvas(self, image_path, file_type):
        """
         image_path='P292->S10117->BIP_V4_Portal->honda_integra'
         file_type='JPEG (*.jpg;*.jpeg;*.jpe)'
         @PARAM = insert_image_or_file_from_bip_canvas('P292->S10117->BIP_V4_Portal->honda_integra', 'JPEG (*.jpg;*.jpeg;*.jpe)')
        """

        paths=image_path.split('->')
        if len(paths)>2:
            for app in paths[:-2]:
                apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
                x=[el.text.strip() for el in self.driver.find_elements_by_css_selector(apps_css)]
                apps=self.driver.find_elements_by_css_selector(apps_css)
                apps[x.index(app)].find_element_by_css_selector("img[src*='triangle']").click()
            time.sleep(5)
            get_folder=True
            counter=0
            while get_folder:
                x=[el.text.strip() for el in self.driver.find_elements_by_css_selector(apps_css)]
                if paths[-2] in x:
                    apps=self.driver.find_elements_by_css_selector(apps_css)
                    apps[x.index(paths[-2])].find_element_by_css_selector("img[src*='folder']").click()
                    time.sleep(5)
                    get_folder=False
                    break
                else:
                    counter+=1
                    action = ActionChains(self.driver)
                    action.send_keys(keys.Keys.PAGE_DOWN).perform()
                    time.sleep(5)
                    del action
                    if counter==10:
                        break
                time.sleep(1)
            time.sleep(1)
        file_name_input_css="#IbfsOpenFileDialog7_cbFileName input"
        self.driver.find_element_by_css_selector(file_name_input_css).click()
        time.sleep(2)
        utillity.UtillityMethods.ibfs_save_as(self, paths[-1], file_type)
        time.sleep(1)
    
    def open_file_from_repostitory_window(self, folder_path, file_name, file_type=None):
        """
        Desc:- This function first expand folder in reposititory window form left hand side, then 'Enter file name' which need to open
        :param folder_path='P292->S10117->BIP_V4_Portal'
        :param file_name='honda_integra'
        :param file_type='JPEG (*.jpg;*.jpeg;*.jpe)'
        :usage open_file_from_repostitory_window('P292->S10117->BIP_V4_Portal', 'honda_integra', file_type='JPEG (*.jpg;*.jpeg;*.jpe)')
        @AAkhan
        """
        dialog_css="#dlgIbfsOpenFile7 [class*='active'] #paneIbfsExplorer_exTree"
        tree_css = dialog_css+" > div.bi-tree-view-body-content table tr"
        path = folder_path.split('->')[0]
        parent_elem = self.driver.find_element_by_css_selector(dialog_css)
        utillity.UtillityMethods.click_on_screen(self, parent_elem, 'middle')
        vfour_portal_canvas.Vfour_Portal_Canvas.scroll_down_to_search_element(self, path, dialog_css, tree_css)
        elems = self.driver.find_elements_by_css_selector(tree_css)
        if path not in [elem.text.strip() for elem in elems]:
            raise ValueError("File name '" + path + "' not exist.")
        folder_index_number =Vfour_Miscelaneous.expand_tree(self, folder_path, tree_css=dialog_css)
        repository_items = self.driver.find_elements_by_css_selector(dialog_css)
        td_img = repository_items[folder_index_number].find_element_by_css_selector("img.icon")
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", repository_items[folder_index_number])
        time.sleep(3)
        utillity.UtillityMethods.default_click(self, td_img)
        utillity.UtillityMethods.select_item_from_ibfs_explorer_list(self, file_name, file_type=file_type)
    
    def drag_drop_in_bip(self, source_elem, target_elem,**kwargs):
        """
        This function to drag and drop object from source to target
        :Usage: drag_drop_using_pyautogui(source_elem,target_elem, 9, 0, 9, 0)
        """
        src_cord_type=kwargs['src_cord_type'] if 'src_cord_type' in kwargs else 'middle'
        trg_cord_type=kwargs['trg_cord_type'] if 'trg_cord_type' in kwargs else 'middle'
        source_offset_x=kwargs['sx_offset'] if 'sx_offset' in kwargs else 0
        source_offset_y=kwargs['sy_offset'] if 'sy_offset' in kwargs else 0
        target_offset_x=kwargs['tx_offset'] if 'tx_offset' in kwargs else 0
        target_offset_y=kwargs['ty_offset'] if 'ty_offset' in kwargs else 0
        pyautogui.FAILSAFE=False
        source_obj=utillity.UtillityMethods.get_object_screen_coordinate(self, source_elem, coordinate_type=src_cord_type, x_offset=source_offset_x, y_offset=source_offset_y)
        source_obj_x=source_obj['x']
        source_obj_y=source_obj['y']
        target_obj=utillity.UtillityMethods.get_object_screen_coordinate(self, target_elem, coordinate_type=trg_cord_type, x_offset=target_offset_x, y_offset=target_offset_y)
        target_obj_x=target_obj['x']
        target_obj_y=target_obj['y']
        Vfour_Miscelaneous.drag_drop(self, source_obj_x, source_obj_y, target_obj_x, target_obj_y, **kwargs)
    
    def drag_drop(self, source_obj_x, source_obj_y, target_obj_x, target_obj_y, **kwargs):
        time.sleep(2)
        if sys.platform == 'linux':
                mouse_.press(int(source_obj_x), int(source_obj_y))
                time.sleep(3)
                pyautogui.moveTo(int(target_obj_x), int(target_obj_y), duration=3)
                time.sleep(3)
                mouse_.release(int(target_obj_x), int(target_obj_y))
                time.sleep(5)
        else:
            if Global_variables.browser_name=='chrome':
                time.sleep(5)
                mouse_delay=kwargs['mouse_speed'] if 'mouse_speed' in kwargs else 25
                path_ = os.path.join(root_path.ROOT_PATH, 'drag_drop_bip_helper.exe '+str(source_obj_x)+' '+ str(source_obj_y)+' '+ str(target_obj_x)+' '+ str(target_obj_y)+' '+str(mouse_delay))
                procesobj = subprocess.Popen(path_)
                del procesobj
                time.sleep(5)
            else:
                mouse_obj=uisoup.mouse
                mouse_obj.click(source_obj_x,source_obj_y)
                time.sleep(5)
                mouse_obj.drag(source_obj_x,source_obj_y, target_obj_x, target_obj_y)
                time.sleep(5)
        time.sleep(10)
    
    def verify_difference(self, before_pro, after_pro, min_unit_difference, max_unit_difference, option, msg):
        """
        This function is used to verify size of 'Panel', 'Page' or 'Canvas'
        :param before_pro=27    'only interger number'
        :param after_pro=27    'only interger number'
        :param difference=27    'only interger number'
        :param option='less_than'        ''' If previous element value is Greter than Current element Value. '''
        :param option='Greater_than'        ''' If previous element value is Less than Current element Value. '''
        :param msg='Step 7: Verify Difference of panel 1 after shrink'
        :usage verify_difference(496, 270, 226, 'less_than', 'Step 7: Verify Difference of panel 1 after shrink'):
        """
        if option == 'less_than':
            status_=True if int(before_pro)-int(after_pro) in range(int(min_unit_difference), int(max_unit_difference)) else False
        if option == 'Greater_than':
            status_=True if int(after_pro)-int(before_pro) in range(int(min_unit_difference), int(max_unit_difference)) else False
        utillity.UtillityMethods.asequal(self, status_, True, msg)
    
    def edit_properties_dialog(self, tab_name, control_type, elem_name, **kwargs):
        """
        :param tab_name=value of tab :Example : tab_name='Advanced'
        :param control_type='textbox' OR 'checkbox' OR 'textline'
        :param elem_name=value of text line :Example : elem_name='Default Height'
        :Usage edit_properties_dialog('Advanced', 'textbox', 'Default Height', text_input='90')
        """
        popup_css = "#dlgProperties [class*='active']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, popup_css, 1, expire_time=15)
        tab_css = "#propTabPane [id*='BiTabBar'] [id*='BiTabButton']"
        tab_title_elems = self.driver.find_elements_by_css_selector(popup_css +" " + tab_css) 
        actual_tab = tab_title_elems[[elem.text.strip() for elem in tab_title_elems].index(tab_name)]
        actual_tab.click()
        if tab_name == 'Main Properties':
            '''
            Main Properties section
            '''
        elif tab_name == 'Advanced':
            tab_name=tab_name.lower()
            advance_tab_text_option = {'Default Height' : '0', 'Default Width' : '1'}
            if control_type == 'textbox':
                elems = self.driver.find_elements_by_css_selector(popup_css + " #" + tab_name + "Tab input[id*='BiTextField']")
                actual_elem = elems[int(advance_tab_text_option[elem_name])]
                utillity.UtillityMethods.set_text_to_textbox_using_keybord(self, kwargs['text_input'], text_box_elem=actual_elem)
            if control_type == 'combobox':
                elem = self.driver.find_element_by_css_selector(popup_css + " #" + tab_name + "Tab [id*='BiComboBox'] [id*='BiButton']")
                utillity.UtillityMethods.select_any_combobox_item(self, elem[0], kwargs['combobox_input'])
        else:
            print("Please select appropriate Tab option.")
        if control_type == 'button':
            btn_id = 'OK' if elem_name == 'OK' else 'Security' if elem_name == 'Security' else 'Cancel'
            button_elem = self.driver.find_element_by_css_selector(popup_css + " [id*='IABottomBar'] #btn" + btn_id)
            button_elem.click()
    
    def switch_to_frame_in_bip_page(self, frame_panel_name=None, frame_panel_css=None, expire_time=25):
        """
        Desc:- This function will handle frame synchronization and switch into it, Inside BIP current visible page in Edit or Run Mode.
        :usage switch_to_frame_in_bip_page(frame_panel_name=panel_name)
        @author: Aftab
        """
        if frame_panel_css != None and frame_panel_name == None:
            path_css = frame_panel_css
        elif frame_panel_css == None and frame_panel_name != None:
            path_css = "[class*='bi-iframe iframe'][name*='" + frame_panel_name + "']"
        Vfour_Miscelaneous.wait_for_property_in_bip_page(self, path_css, 1, expire_time=expire_time)
        curent_page_obj = vfour_portal_canvas.Vfour_Portal_Canvas.get_current_page(self)
        try:
            self.driver.switch_to.frame(curent_page_obj.find_element_by_css_selector(path_css))
        except NoSuchElementException:
            raise ValueError(str(path_css)+" CSS for frame not able to found in Current Page.")
        time.sleep(1)
        get_browser_height = utillity.UtillityMethods.get_browser_height(self)
        position_x = get_browser_height['browser_width']
        position_y = get_browser_height['browser_height']
        Global_variables.current_working_area_browser_x=position_x
        Global_variables.current_working_area_browser_y=position_y
        time.sleep(1)
    
    def wait_for_property_in_bip_page(self, parent_css, expected_number, expire_time=25, string_value=None):
        """
        Desc:- This function will handle synchronization inside BIP current visible page in Edit or Run Mode.
        :param parent_css = "#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"     '''This is css locator'''
        :param expected_number = 1,2,3.....                                                       '''Only Interger Number'''
        :param expire_time = 50 or 100                                                            '''Only Interger Number to wait time unitil condition not that specific time''
        :param string_value='Country'                                                             '''This need to verify the exact string visible in Dome without space.'''
        :Usage wait_for_property("#TableChart_1 [align='justify']", 1, expire_time= 50, string_value="Draganddropfield.")
        @author: Aftab
        """
        timeout=0
        run_ = True
        curent_page_obj = vfour_portal_canvas.Vfour_Portal_Canvas.get_current_page(self)
        while run_:
            timeout+=1
            if timeout == expire_time+1:
                print("'" + str(parent_css) + "' Css value not able to get expected number or String value in wait property Action.")
                run_=False
                break
            if string_value != None:
                try:
                    temp_str_value=curent_page_obj.find_element_by_css_selector(parent_css).text.strip().replace('\n','')
                except NoSuchElementException:
                    time.sleep(1)
                    continue
                except StaleElementReferenceException:
                    time.sleep(1)
                    continue
                str_value = re.sub(' ','',temp_str_value)
                if str_value == string_value.replace(' ',''):
                    run_=False
                    break
            else:
                try:
                    temp_obj = self.driver.find_elements_by_css_selector(parent_css)
                    check_obj_exist = temp_obj[0]
                    del check_obj_exist
                except IndexError:
                    time.sleep(1)
                    continue
                if len(temp_obj) == expected_number:
                    run_=False
                    break
    
    def expand_tree(self, folder_path, tree_css=None, scroll_elem=None):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Usage expand_tree('S7068->AR-RP-193')
        @author: AAkhan
        """
        if scroll_elem!=None:
            scroll_obj=scroll_elem
        else:
            scroll_obj=self.driver.find_element_by_css_selector("#treeContainer")
        utillity.UtillityMethods.click_on_screen(self, scroll_obj, 'middle')
        time.sleep(2)
        utillity.UtillityMethods.click_on_screen(self, scroll_obj, 'middle', y_offset=-9)
        if tree_css != None:
            tree_rows=tree_css
        else:
            tree_rows="#bipTreePanel #treeView table>tbody>tr"
        folder_list=folder_path.split('->')
        repository_tree_items = self.driver.find_elements_by_css_selector(tree_rows)
        resource_tree_items_list = javascript.JavaScript.get_elements_text(self, repository_tree_items)
        folder_img_elem=utillity.UtillityMethods.validate_and_get_webdriver_object(self, "td>img[class='icon']", 'Resource tree', parent_object=repository_tree_items[resource_tree_items_list.index(folder_list[0])])
        Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img_elem, number_of_time=19, direction='up')
        for item in folder_list:
            repository_items = self.driver.find_elements_by_css_selector(tree_rows)
            resource_tree_list = javascript.JavaScript.get_elements_text(self, repository_items)
            if item not in resource_tree_list:
                print(resource_tree_list)
                raise LookupError(item+ " Not Exist in setup "+ self.driver.current_url)
            try:
                for i in range(len(repository_items)):
                    if repository_items[i].text.strip() == item:
                        try:
                            if item == folder_list[-1]:
                                folder_img = repository_items[i].find_element_by_css_selector("td>img.icon")
                            else:
                                folder_img = repository_items[i].find_element_by_css_selector("td>img[src*='triangle_collapsed']")
                            Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img)
                            CoreUtillityMethods.left_click(self, folder_img)
                            time.sleep(3)
                            if item == folder_list[-1]:
                                return (i)
                        except:
                            if item == folder_list[-1]:
                                return (i)
                        break
            except NoSuchElementException as e:
                print(e,item + " not found in Repository Tree view. It might be a Bug also.")
                
    def get_browser_specification(self, pause=1, update_coordinate=True):
        """
        This is will return browser x,y coordinate
        """
        browser_name = self.driver.desired_capabilities['browserName']
        browser_class_dict={'chrome':self.driver.title, 'firefox':self.driver.title+' - Mozilla Firefox', 'ie':self.driver.title+' - Internet Explorer'}
        import uiautomation as automate
        if browser_name == 'chrome':
            automate.WindowControl(Name=browser_class_dict['chrome']).SetFocus()
            time.sleep(pause)
            br=list(automate.DocumentControl(ClassName="Chrome_RenderWidgetHostHWND").BoundingRectangle)
        elif browser_name == 'firefox':
            automate.WindowControl(Name=browser_class_dict['firefox']).SetFocus()
            time.sleep(pause)
            br=list(automate.DocumentControl(Name=self.driver.title).BoundingRectangle)
        elif browser_name == 'internet explorer':
            automate.WindowControl(Name=browser_class_dict['ie']).SetFocus()
            time.sleep(pause)
            br=list(automate.PaneControl(Name=browser_class_dict['ie']).BoundingRectangle)
        if len(br) != 4:
            raise IndexError('Browser x y coordinates not able to get.')
        if update_coordinate == True:
            Global_variables.current_working_area_browser_x=br[0]
            Global_variables.current_working_area_browser_y=br[1]
        time.sleep(pause+1)
        return (br)
    
    def scroll_within_resource_tree(self, resource_tree_elem, element, scroll_range=2, number_of_time=1, direction=None):
        '''
        This function is used to scroll within Resource tree panel.
        '''
        resource_tree_panel_top_location = utillity.UtillityMethods.get_object_screen_coordinate(self, resource_tree_elem, coordinate_type='top_middle')
        resource_tree_panel_bottom_location = utillity.UtillityMethods.get_object_screen_coordinate(self, resource_tree_elem, coordinate_type='bottom_left')
        element_middle_location = utillity.UtillityMethods.get_object_screen_coordinate(self, element)
        direction = None
        if int(element_middle_location['y']) < int(resource_tree_panel_top_location['y']):
            direction = 'up'
        elif int(element_middle_location['y']) > int(resource_tree_panel_bottom_location['y'])-19:
            direction = 'down'
        scroll_range=999
        for i in range(int(scroll_range)):
            if direction == 'up':
                element_bottom_middle_location = utillity.UtillityMethods.get_object_screen_coordinate(self, element, coordinate_type='top_middle')
                if int(element_bottom_middle_location['y']) in range(int(resource_tree_panel_top_location['y']), int(resource_tree_panel_bottom_location['y'])-19):
                    break
                else:
                    vfour_portal_canvas.Vfour_Portal_Canvas.scroll_panel(self, 0, 0, 'up', option='uiautomation', number_of_times=number_of_time, waitTime=0.5)
            if direction == 'down':
                element_bottom_middle_location = utillity.UtillityMethods.get_object_screen_coordinate(self, element, coordinate_type='bottom_middle')
                if int(element_bottom_middle_location['y']) in range(int(resource_tree_panel_top_location['y']), int(resource_tree_panel_bottom_location['y'])-19):
                    break
                else:
                    vfour_portal_canvas.Vfour_Portal_Canvas.scroll_panel(self, 0, 0, 'down', option='uiautomation', number_of_times=number_of_time, waitTime=0.5)
        del i
    
    def synchronize_until_element_disappear(self, element_css, expected_number, expire_time, pause_time=1):
        '''
        This function is used to check the length of element reduced.
        '''
        timeout=0
        run_ = True
        while run_:
            timeout+=1
            if timeout == int(expire_time)+1:
                print(str(element_css) + " Parent Css not having " + str(expected_number) + " expected number of element.")
                run_=False
                break
            try:
                temp_obj = self.driver.find_elements_by_css_selector(element_css)
                check_obj_exist = temp_obj[0]
                del check_obj_exist
            except IndexError:
#                 print(str(element_css) + " Parent Css having Zero reference.")
                time.sleep(pause_time)
            if len(temp_obj) == int(expected_number):
                run_=False
                break
            else:
                time.sleep(pause_time)
                continue
        time.sleep(pause_time)
        
    def verify_help_window_left_panel(self, expected_item, msg, frame_path=None, verify_link_active=True, left_panel_css="div#wai_application div#tree_root span a"):
        '''
        This will verify Help window Left panel
        :param expected_item_list='Portal Designer Overview'
        :param frame_path="[name='HelpFrame']->[name='NavFrame']->[name='ViewsFrame']->[name='toc']->[name='tocViewFrame']"
        :param verify_link_active=True|False  'This will tell left panel item is active(selcted)'
        :Usage verify_help_window_left_panel('Portal Designer Overview', 'Step 9: Verify')
        @autho Aftab
        '''
        try:
            frame_path_hierarchy=frame_path if frame_path != None else "[name='HelpFrame']->[name='NavFrame']->[name='ViewsFrame']->[name='toc']->[name='tocViewFrame']"
            frame_path_list=frame_path_hierarchy.split('->')
            for frame in frame_path_list:
                utillity.UtillityMethods.switch_to_frame(self, frame_css=frame)
            soup_obj=utillity.UtillityMethods.beautifulsoup_object_creation(self)
            temp_hyperlink_data_list = soup_obj.select(left_panel_css)
            hyperlink_data_list = [elem.get_text(strip=True) for elem in temp_hyperlink_data_list]
            if verify_link_active==True:
                link_status = temp_hyperlink_data_list[hyperlink_data_list.index(expected_item)].get_attribute_list('class')[0]
                if link_status=='active':
                    msg+=' link is active also.'
                    utillity.UtillityMethods.asin(self, expected_item, hyperlink_data_list, msg)
                else:
                    hyperlink_data_list = False
                    utillity.UtillityMethods.asequal(self, expected_item, hyperlink_data_list, msg)
        finally:
            utillity.UtillityMethods.switch_to_default_content(self)
        
    def verify_help_window_right_panel(self, expected_item_list, msg, frame_path=None, right_panel_css='h1.title.topictitle1'):
        '''
        This will verify Help window Right panel
        :param expected_item_list=['Portal Designer Overview']
        :param frame_path="[name='HelpFrame']->[name='NavFrame']->[name='ViewsFrame']->[name='toc']->[name='tocViewFrame']"
        :usage verify_help_window_right_panel('Portal Designer Overview', Step 9: Verify')
        @autho Aftab
        '''
        try:
            frame_path_hierarchy=frame_path if frame_path != None else "[name='HelpFrame']->[name='ContentFrame']->[name='ContentViewFrame']"
            frame_path_list=frame_path_hierarchy.split('->')
            for frame in frame_path_list:
                utillity.UtillityMethods.switch_to_frame(self, frame_css=frame)
            soup_obj=utillity.UtillityMethods.beautifulsoup_object_creation(self)
            temp_hyperlink_data_list = soup_obj.select(right_panel_css)
            hyperlink_data_list = [elem.get_text(strip=True) for elem in temp_hyperlink_data_list]
            for item in expected_item_list:
                if item in hyperlink_data_list:
                    status=True
                else:
                    status=False
                    break
            if status==True:
                utillity.UtillityMethods.asequal(self, status, status, msg)
            else:
                utillity.UtillityMethods.asin(self, item, hyperlink_data_list, msg)
        finally:
            utillity.UtillityMethods.switch_to_default_content(self)
            
    def select_bipop_menu(self, option_name, custom_css="tr[id^='BiComponent'][class^='bi-menu-item menu-item']:not([style*='hidden']) td.text"):
        """
        Syntax: select_bipop_menu_vfour('Edit')
        """
        bipopup_css="div[id^='BiPopup'][style*='inherit']"
        time.sleep(5)
        bipopups=self.driver.find_elements_by_css_selector(bipopup_css)
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector(custom_css)
        actual_popup_list=[el.text.strip() for el in menu_items]
        CoreUtillityMethods.python_move_to_element(self, menu_items[actual_popup_list.index(option_name)])
        time.sleep(1)
        CoreUtillityMethods.python_left_click(self, menu_items[actual_popup_list.index(option_name)])
        time.sleep(2)
    