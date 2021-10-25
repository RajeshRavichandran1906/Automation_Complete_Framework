from common.lib import utillity, javascript
from common.lib.base import BasePage
from common.locators.wf_mainpage_locators import WfMainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os, re, subprocess, time, sys
from common.pages import visualization_resultarea, vfour_miscelaneous
from common.lib import core_utility as core_utilobj
from common.lib.global_variables import Global_variables
from selenium.webdriver.support.color import Color
import pyautogui
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
    import clipboard
else:
    import uiautomation as automation
    import keyboard

class Wf_Legacymainpage(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Wf_Legacymainpage, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
        
    def verify_legacy_home_page_set_to_default(self):
        '''
        To check Legacy Home page set to default when login to webfocus home page.
        '''
        current_setup_name = self.driver.current_url
        legacy_domain_css = "#PortalResourcevBOX #bipTreePanel #treeView table tr td"
        error_msg = 'This setup "'+current_setup_name+'" does not set to Legacy Home page as default. Please change Legacy Home page as default to continue this test case.'
        try:
            self.driver.find_element_by_css_selector(legacy_domain_css)
        except NoSuchElementException:
            raise LookupError(error_msg)
    
    def set_field_new_portal_dialog(self, portal_name):
        """
        This action is used to set the text field in new portal dialog window.
        :param portal_name='Easy_selector'
        :Usage set_field_new_portal_dialog('Easy_selector')
        """
        elems=self.driver.find_elements_by_css_selector("div[id='dlgNewPortalDesigner'] [class*='window-active'] input")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, elems[0], portal_name)
        time.sleep(1)
        verify_text=elems[1].get_attribute("value")
        expected_text = portal_name.strip().replace(' ', '_')
        utillity.UtillityMethods.asequal(self, expected_text, verify_text, "Step X: Verify the Name field is populated.")
    
    def close_new_portal_dialog(self, option='Create'):
        """
        This action is used to close new portal dialog window.
        :param option='Create'
        :Usage close_new_portal_dialog(option='Create')
        """
        utillity.UtillityMethods.click_dialog_button(self, "div[id='dlgNewPortalDesigner'][style*='left']", option)
        
    def create_portal(self, repository_path, portal_name, **kwargs):
        """
        This action is first expand tree view then create new collaborative portal.
        folder_path = 'P116->S7068'
        folder_name=any name
        Syntax: create_domain_folder('Domain', 'bip')
        """
        mainpage_obj=Wf_Legacymainpage(self.driver)
        mainpage_obj.select_repository_menu(repository_path, 'New->Collaborative Portal', **kwargs)
        Wf_Legacymainpage.set_field_new_portal_dialog(self, portal_name)
        Wf_Legacymainpage.close_new_portal_dialog(self)
        time.sleep(2)
    
    def select_or_verify_top_banner_links(self, menu_path, **kwargs):
        """
        menu_path = 'Administration->Security Center'
        verify_list=['Security Center', 'Administration Console', 'Magnify Console', 'Manage Private Resources', 'Mode Normal', 'Mode Manager']
        Syntax: expand_repository_tree('Administration', verify_list=list)
        Syntax: expand_repository_tree('Administration')
        Syntax: expand_repository_tree('Administration->Security Center')
        @author = Niranjan
        """
        Wf_Legacymainpage.verify_legacy_home_page_set_to_default(self)
        utillobj = utillity.UtillityMethods(self.driver)
        menu_list=menu_path.split('->')
        main_menu_item=self.driver.find_element(*WfMainPageLocators.__dict__["banner_" + menu_list[0].lower().replace(' ', '_')])
        core_utilobj.CoreUtillityMethods.move_to_element(self, main_menu_item) 
        utillity.UtillityMethods.default_left_click(self, object_locator=main_menu_item, **kwargs)
        time.sleep(2)
        if 'verify_list' in kwargs:
            utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=kwargs['verify_list'], msg=kwargs['msg'])
        if len(menu_list)>1:
            utillity.UtillityMethods.select_or_verify_bipop_menu(self, menu_list[1])
            time.sleep(2) 
    
    def verify_folder_status(self, folder_path, status='selected', **kwargs):
        """
        folder_path = 'P116->S7068'
        status='selected' OR 'unpublished' OR 'hidden'
        Syntax: verify_folder_status('Public', status='selected')
        @author = Niranjan
        """
        msg = kwargs['msg'] if 'msg' in kwargs else 'X'
        folder_list=folder_path.split('->')
        Wf_Legacymainpage.expand_repository_tree(self, folder_path)
        status_code={'selected':'png', 'unpublished':'0.6', 'hidden':'0.3','published':'16.png'}
        BIPtree_rows=kwargs['BIPtree_css'] if 'BIPtree_css' in kwargs else "#bipTreePanel #treeView table>tbody>tr"
        repository_items = self.driver.find_elements_by_css_selector(BIPtree_rows)
        for i in range(1,len(repository_items)):
            if repository_items[i].text.strip() == folder_list[-1]:
                ret=self.driver.find_element_by_css_selector(BIPtree_rows + ":nth-child("+str(i+1)+")>td>img:nth-child(2)").get_attribute("src").endswith(status_code[status])
                break
        utillity.UtillityMethods.asequal(self,True, ret, "Step "+msg+". Verify "+folder_list[-1]+" Folder is "+status+".")
    
    def verify_repositery_item(self, folder_path, item_name, item_exit=True, **kwargs):
        """
        folder_path = 'P116->S7068'
        folder_exit=Ture or False
        Syntax: verify_repositery_folder_status('Public', folder_exit=False)
        """
        msg = kwargs['msg'] if 'msg' in kwargs else 'X'
        Wf_Legacymainpage.expand_repository_tree(self, folder_path, **kwargs)
        BIPtree_rows=kwargs['BIPtree_css'] if 'BIPtree_css' in kwargs else "#bipTreePanel #treeView table>tbody>tr"
        repository_items = self.driver.find_elements_by_css_selector(BIPtree_rows)
        statx = item_name in [i.text.strip() for i in repository_items]
        if item_exit == True:
            utillity.UtillityMethods.asequal(self,item_exit, statx, "Step "+msg+". Verify " + item_name + " File or Folder is Avialable.")
        else:
            utillity.UtillityMethods.asequal(self,item_exit, statx, "Step "+msg+". Verify " + item_name + " File or Folder is Not Avialable.")
    
    def create_folder(self, folder_path, folder_name, **kwargs):
        """
        folder_path = 'P116->S7068'
        folder_name=any name
        Syntax: create_folder('Domain', 'bip')
        @author = Niranjan
        """
        Wf_Legacymainpage.select_repository_menu(self, folder_path, 'New->Folder', **kwargs) 
        elem=self.driver.find_element_by_css_selector("#createFolderDialog input#newdesc")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, elem, folder_name)
        ok_btn=self.driver.find_element_by_css_selector("#createFolderDialog #btnOK")
        ok_btn.click()
        time.sleep(2)
        
    def expand_repository_tree(self, folder_path, scroll_elem=None, **kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        Syntax: expand_repository_tree('S7068->AR-RP-193')
        @author = Nasir
        """
        if scroll_elem!=None:
            scroll_obj=scroll_elem
        else:
            scroll_obj=self.driver.find_element_by_css_selector("#bipTreePanel div[class='bi-component'][id*='BiComponent']")
        core_utilobj.CoreUtillityMethods.python_move_to_element(self, scroll_obj)
        time.sleep(2)
        core_utilobj.CoreUtillityMethods.python_move_to_element(self, scroll_obj, yoffset=-9)
        Wf_Legacymainpage.verify_legacy_home_page_set_to_default(self)
        tree_rows="#bipTreePanel #treeView table>tbody>tr"
        folder_list=folder_path.split('->')
        repository_tree_items = self.driver.find_elements_by_css_selector(tree_rows)
        resource_tree_items_list = javascript.JavaScript.get_elements_text(self, repository_tree_items)
        folder_img_elem=utillity.UtillityMethods.validate_and_get_webdriver_object(self, "td>img[class='icon']", 'Resource tree', parent_object=repository_tree_items[resource_tree_items_list.index(folder_list[0])])
        vfour_miscelaneous.Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img_elem, number_of_time=19, direction='up')
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
                            vfour_miscelaneous.Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img)
                            core_utilobj.CoreUtillityMethods.left_click(self, folder_img)
                            time.sleep(3)
                            if item == folder_list[-1]:
                                return (i)
                        except:
                            if item == folder_list[-1]:
                                return (i)
                        break
            except NoSuchElementException as e:
                print(e,item + " not found in Repository Tree view. It might be a Bug also.")

    def right_click_repository_tree(self, item_name, **kwargs):                                                            
        """
        :Param : item_name = 'AR-RP-193'
        Syntax: right_click_repository_tree('AR-RP-193')
        @author = Nasir
        """
        BIPtree_rows="#bipTreePanel #treeView table>tbody>tr"
        rows = self.driver.find_elements_by_css_selector(BIPtree_rows)
        for i in range(len(rows)):
            td_item = BIPtree_rows + ":nth-child(" + str(i+1) + ")>td"
            get_td=self.driver.find_element_by_css_selector(td_item)
            if get_td.text == item_name:
                td_img = self.driver.find_element_by_css_selector(td_item + ">img.icon")
#                 self.driver.execute_script("arguments[0].scrollIntoView(true);", get_td)
                time.sleep(3)
                core_utilobj.CoreUtillityMethods.right_click(self, td_img)
                
    def select_repository_menu(self, folder_path, menu_item=None,**kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Param : menu_item = 'Edit' or 'Run'
        :kwargs['item_exit']= True or False
        :kwargs['expected_menu_list']= ['TextEditor', 'URL'] 
        :kwargs['msg']= "Step 11"
        :Syntax: select_repository_menu('S7068->AR-RP-193', 'Run')
            OR
        :Syntax: select_repository_menu('S7068->AR-RP-193', 'Run', item_exit=True, expected_menu_list=['Collaborative Portal', 'Page'], msg="Step 11")
            OR
        :Syntax: select_repository_menu('S7068->AR-RP-193', 'Run', item_exit=False, expected_menu_list=['Collaborative Portal', 'Page'], msg="Step 11")
        @author = Nasir
        """
        item_name=folder_path.split('->')[-1]
        Wf_Legacymainpage.expand_repository_tree(self, folder_path, **kwargs)
        Wf_Legacymainpage.right_click_repository_tree(self, item_name, **kwargs)
        time.sleep(5)
        popup_css="div[id^='BiPopup'][style*='inherit']"
        popup_menu_css="table>tbody>tr"
        #visualization_resultarea.Visualization_Resultarea.wait_for_property(self, popup_css, 1, expire_time=15)
        if menu_item == None:
            pass
        else:
            menu_list = menu_item.split('->')
            for j in range(len(menu_list)):
                popups = self.driver.find_elements_by_css_selector(popup_css)
                core_utilobj.CoreUtillityMethods.move_to_element(self, popups[-1], element_location='top_middle', yoffset=3)
                menu_items = popups[-1].find_elements_by_css_selector(popup_menu_css)
                for i in range(len(menu_items)):
                    if menu_list[-1] in menu_items[i].text.strip():
                        core_utilobj.CoreUtillityMethods.left_click(self, menu_items[i])
                        break
                    elif menu_list[j] in menu_items[i].text.strip():
                        arrow_elem=menu_items[i].find_element_by_css_selector("td.arrow")
                        core_utilobj.CoreUtillityMethods.move_to_element(self, arrow_elem, xoffset=3)
                        popups = self.driver.find_elements_by_css_selector(popup_css)
                        core_utilobj.CoreUtillityMethods.move_to_element(self, popups[-1], element_location='top_middle', yoffset=3)
        if 'expected_menu_list' in kwargs:
            popups = self.driver.find_elements_by_css_selector(popup_css)
            menu_items = popups[-1].find_elements_by_css_selector(popup_menu_css)
            actual_elem=[el.text.strip().replace(' ','') for el in menu_items]
            actual_elem = [elem for elem in actual_elem if elem != '']
            expected_elem = [exp.replace(' ', '') for exp in kwargs['expected_menu_list']]
            count_= 1
            for elem in expected_elem:
                status_=True if elem in actual_elem else False
                verification_msg = "Visible" if kwargs['item_exit'] == True else "Not Visible"
                utillity.UtillityMethods.asequal(self, kwargs['item_exit'], status_, str(kwargs['msg']) + "." + str(count_) + " : Verify "+ elem + " Option "+verification_msg+" in Repository menu")
                count_ += 1
        utillity.UtillityMethods.switch_to_default_content(self, pause=2)
     
    def select_repository_folder_item_menu(self, folder_path,item_name, menu_item_path,**kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Param : input_menu = 'Edit' or 'Run'
        select_repository_folder_item_menu('P116->S7215','91551','Edit With Text Editor')
        @author = Nasir
        """
        folder_path=folder_path+"->"+item_name
        Wf_Legacymainpage.select_repository_menu(self, folder_path, menu_item_path,**kwargs)
          
    def delete_repository_item(self, folder_path, dialog_parent_id, menu_item='Delete', option='Yes', **kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Param : input_menu = 'Edit' or 'Run'
        Syntax: select_repository_menu('S7068->AR-RP-193', 'Run')
        @author = Nasir
        """
        Wf_Legacymainpage.select_repository_menu(self, folder_path, menu_item, **kwargs)
        time.sleep(1.5)
        utillity.UtillityMethods.click_dialog_button(dialog_parent_id, option)

                
    def save_fex(self, fex_name='91551'):
        """
        Syntax: click_text_editor_ribbon_button('Run')
        :Param btn_name: Save or Run...
        @author = Niranjan
        """
        self.driver.find_element_by_css_selector("#IbfsOpenFileDialog7_cbFileName input").send_keys(fex_name)
        self.driver.find_element_by_css_selector("#IbfsOpenFileDialog7_btnOK").click()
    
    def click_text_editor_ribbon_button(self, btn_name, **kwargs):
        """
        Syntax: click_text_editor_ribbon_button('Run')
        :Param btn_name: Save or Run...
        @author = Niranjan
        """
        menu_btn={'Run':'toolbar_button_run', 'Save':'toolbar_button_save'}
        menu_item=self.driver.find_element_by_css_selector("#" + menu_btn[btn_name] + " img")
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#" + menu_btn[btn_name] + " img", 1, expire_time=50)
        utillity.UtillityMethods.default_left_click(self,object_locator=menu_item, **kwargs)
        time.sleep(2)
    
    def enter_data_to_texteditor_from_file(self, file_name):
        """
        Syntax: click_text_editor_ribbon_button('Run')
        :Param btn_name: Save or Run...
        @author = Niranjan
        """
        data_file=os.getcwd() + "\data\\" + file_name
        try:
            fileObj = open(data_file, "r")
            line = fileObj.readline()
            while line:
                self.driver.find_element_by_css_selector("#bipEditorArea").send_keys(line)
                time.sleep(1)
                line = fileObj.readline()
        except IOError:
            exit()
    
    def select_or_verify_properties_flaglist(self, opt,**kwargs):
        """
        Syntax: select_or_verify_properties_flaglist(opt='enable_auto_link',check=True, msg='Step 05a: verify properties flag')
        @author = Niranjan
        """
        flags={'user_list':'noShowUserList',
            'prompt_parameter':'chkParams',
            'run_olap':'chkRunAsOlap',
            'enable_auto_link':'enableCIO',
            'uer_run':'showAsStdRep',
            'automatic_open':'autoOpen',
            'only_run_deferred':'deferredOnly',
            'schedule_only':'scheduleOnly',
            'auto_link_target':'CIOtarget',
            'only_user_run':'showOnlyAsStdRep',
            'auto_create_folder':'autoCreateMRF',
            'deferred_report_desc':'useTitleDeferred',
            'restrict_schedule_to_library':'restrictSchedLibOnly',
            'auto_drill':'enableAutoDrill'
            }
        status={}
        for key in flags:
            status[key]=self.driver.find_element_by_css_selector("#flagList #" + flags[opt] + " input").is_selected()
        utillity.UtillityMethods.asequal(self, kwargs['check'], status[key], kwargs['msg'])

    def click_text_editor_window_caption_button(self, btn_name):
        """
        btn_name="minimize', OR 'maximize', OR 'close'
        """
        self.driver.find_element_by_css_selector("#bipEditor div[class*='" + btn_name + "']").click()
        time.sleep(2)
        
    def edit_fex_in_text_editor(self, **kwargs):
        """
        find='xxx'
        repl='yyy'
        Syntax: edit_fex_in_text_editor(find='xxx',repl='yyy')
        @author = Niranjan
        """
        editor_elem=(By.CSS_SELECTOR, '#bipEditor #menu_button_search')
        self._validate_page(editor_elem)  
        self.driver.find_element_by_css_selector("#bipEditor #menu_button_search").click()
        time.sleep(2)
        utillity.UtillityMethods.select_or_verify_bipop_menu(self,'Find')
        time.sleep(2)
        find_elem=self.driver.find_element_by_css_selector("#findReplace #findText")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, find_elem, kwargs['find'])
        find_elem=self.driver.find_element_by_css_selector("#findReplace #replaceText")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, find_elem, kwargs['repl'])
        self.driver.find_element_by_css_selector("#findReplace #btnReplaceAll").click()
        time.sleep(2)
        self.click_text_editor_ribbon_button("Save")
        time.sleep(2)
        self.click_text_editor_window_caption_button("close")
        time.sleep(2)
    
    def get_repository_item_availability(self, item_path):
        """
        Descr:- This will return "True" for availability, and "False" for non availability.
        :Param : item_path = 'P116->S7068->AR-RP-193'
        Syntax: get_repository_item_availability('P116->S7068->AR-RP-193')
        @author = Niranjan
        """
        Wf_Legacymainpage.expand_repository_tree(self, item_path)
        time.sleep(3)
        BIPtree_rows = "#bipTreePanel #treeView table>tbody>tr"
        repository_list = [el.text.strip() for el in self.driver.find_elements_by_css_selector(BIPtree_rows)]
        if item_path.split('->')[-1] in repository_list:
            print(item_path.split('->')[-1]+" exist")
            return(True)
        else:
            print(item_path.split('->')[-1]+" doesn't exist")
            return(False)
    
    def upload_file(self, uload_file_list, **kwargs):
        """
        :param file_name='upload.png'
        :kwargs parent_css="#dlgBipUpload [class*='active'][class*='window'] input[type='file']"
        :usage upload_file('uload.png')
        """
        file_path_location=kwargs['file_path_location'] if 'file_path_location' in kwargs else "\\\ibirisc2\\bipgqashare\\Images_and_Things\\"
        parent_elem=kwargs['parent_css'] if 'parent_css' in kwargs else "#dlgBipUpload [class*='active'] input[name^='fileName']"
        utillity.UtillityMethods.synchronize_until_element_is_visible(self, parent_elem, 90)
        parent_obj = self.driver.find_elements_by_css_selector(parent_elem)
        browser = Global_variables.browser_name
        for i in range(len(uload_file_list)):
            if i > 5:
                print("You have crossed maximum number of uploads.")
                break
            if browser in ['ie', 'edge']:
                utillity.UtillityMethods.click_on_screen(self, parent_obj[i], 'right', click_type=0, x_offset=-9)
            else:
                core_utilobj.CoreUtillityMethods.python_left_click(self, parent_obj[i], element_location='middle_left', xoffset=49)
            time.sleep(2)
#             f_name=file_path_location + uload_file_list[i] + "," + browser
            f_name=file_path_location + uload_file_list[i]
            if sys.platform == 'linux':
                time.sleep(3)
                pykeyboard.press_key(pykeyboard.control_key)
                pyautogui.press('l')
                pykeyboard.release_key(pykeyboard.control_key)
                time.sleep(3)
                clipboard.copy(f_name.replace('ibirisc2','se_workspace').replace('\\','/').replace(',{0}'.format(browser),''))
                time.sleep(5)
                pykeyboard.press_key(pykeyboard.control_key)
                pyautogui.press('v')
                pykeyboard.release_key(pykeyboard.control_key)
                pykeyboard.press_key(pykeyboard.enter_key)
                pykeyboard.release_key(pykeyboard.enter_key)
            else:
                window_upload_ = automation.WindowControl(ClassName="#32770")
                upload_file_ = window_upload_.EditControl(ClassName="Edit")
                upload_file_.Exists(maxSearchSeconds=29, searchIntervalSeconds=1)
                upload_file_.SetFocus()
                upload_file_.SetValue(f_name, waitTime=3)
                window_upload_.ButtonControl(Name="Open", foundIndex=3).MoveCursor()
                window_upload_.ButtonControl(Name="Open", foundIndex=3).Click()
#             temp_obj = subprocess.Popen(os.getcwd()+"\\common\\lib\\Upload_File1.exe "+f_name)
#             del temp_obj
            time.sleep(7)
        time.sleep(2)
    
    def upload_repository_document_and_image(self, uload_item_list, option='upload', publish=True, **kwargs):
        """
        :param item_name="upload.vbs"
        :param option="upload" or "close"
        :param publish=True or False
        :Usage upload_repository_document_and_image('upload.vbs', 'upload')
        """
        Wf_Legacymainpage.upload_file(self, uload_item_list, **kwargs)
        temp_obj = self.driver.find_element_by_css_selector("#dlgBipUpload [id^='FormComponent'] #isPrivateCheckbox input[type='checkbox']")
        if publish == True:
            if temp_obj.is_selected() == True:
                print('Upload item publish.')
            else:
                temp_obj.click()
                print('Upload item Publish sucessfully.')
        elif publish == False:
            temp_obj.click()
            print('Upload item UnPublish sucessfully.')
        else:
            print('Upload item Publish option missing.')
        if option == 'upload':
            self.driver.find_element_by_css_selector("#dlgBipUpload [id^='FormComponent'] #btnSubmit [class*='button']").click()
        elif option == 'close':
            self.driver.find_element_by_css_selector("#dlgBipUpload [id^='FormComponent'] #btnSubmit [class*='button']").click()
        else:
            print(option+" button is missing in upload Dialog window.")
        if 'ok' in kwargs:
            parent_css= "div[id^='BiDialog'][class*='bi-component']"
            utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 1, 25)
            css="div[id^='BiDialog'][class*='bi-component'] [class*='active']  [class*='caption'] [class*='bi-label']"
            text_css="div[id^='BiDialog'][class*='bi-component'] [class*='active'] div[id^='BiOptionPane']"
            utillity.UtillityMethods.verify_popup(self, css, "Step X: Verify upload message dialog appears", caption_css=text_css, caption_text=kwargs['popup_text'])
            utillity.UtillityMethods.click_dialog_button(self, parent_css, "OK")
        
    
    def verify_repository_menu_enabled(self, folder_path, menu_item_path,enabled=True,**kwargs):
        
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Param : input_menu = 'Edit' or 'Run'
        Syntax: select_repository_menu('S7068->AR-RP-193', 'Run')
        """
        item_name=folder_path.split('->')[-1]
        Wf_Legacymainpage.expand_repository_tree(self, folder_path, **kwargs)
        Wf_Legacymainpage.right_click_repository_tree(self, item_name, **kwargs)
        element=None
        menu_list = menu_item_path.split('->')
        for item in menu_list:
            popups = self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit']")
            menu_ele = popups[-1].find_elements_by_css_selector("table>tbody>tr")
            menu_text=[t.text.strip() for t in menu_ele]
            if item==menu_list[-1] :
                element=menu_ele[menu_text.index(item)]
            else :
                utillity.UtillityMethods.default_click(self, menu_ele[menu_text.index(item)])
                time.sleep(2)
        if enabled==True :
            disabled=bool(element.get_attribute("disabled"))
            enabled_color=Color.from_string(element.find_element_by_css_selector("td[class='text']").value_of_css_property("color")).rgb
            status=True if disabled==False and enabled_color=='rgb(59, 85, 101)' else False
            utillity.UtillityMethods.asequal(self,True,status,'Step X : Verify '+menu_list[-1]+' is enabled')
        else :
            disabled=bool(element.get_attribute("disabled"))
            enabled_color=Color.from_string(element.value_of_css_property("color")).rgb
            status=True if disabled==True and enabled_color=='rgb(109, 109, 109)' else False
            utillity.UtillityMethods.asequal(self,True,status,'Step X : Verify '+menu_list[-1]+' is disabled')
            
    def verify_properties_dialog(self, control_type, control_name, msg, tab_name='Main Properties', **kwargs):
        """
        :param control_type='textbox' OR 'checkbox' OR 'textline'
        :param control_name='Title' OR {'enable auto drill': 'enable'} OR {'enable auto drill': 'uncheck'}
        :param msg='Step 5: Verify properties dialog'
        :kwargs value='Folder Name'
        :kwargs enable=True
        :kwargs check=False
        :usage verify_properties_dialog('checkbox', {'enable auto drill': 'disable'}, 'Step 5: Verify properties dialog', enable=True)
        """
        popup_css = "#dlgProperties [class*='active']"
        tab_title_elems = self.driver.find_elements_by_css_selector(popup_css + " #propTabPane [id*='BiTabBar'] [id*='BiTabButton']") 
        actual_tab = tab_title_elems[[elem.text.strip() for elem in tab_title_elems].index(tab_name)]
        utillity.UtillityMethods.default_click(self, actual_tab)
        if tab_name == 'Main Properties':
            main_css=popup_css+" #maintab"
            flag_css=main_css+" #flagList div[style^='user-select']"
            y=self.driver.find_elements_by_css_selector(flag_css)
            lines = {}
            if control_type == 'textbox':
                elems=self.driver.find_elements_by_css_selector(main_css+" > div[id^='BiVBox'] > div[id^='BiHBox']")
                elem = elems[[control_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
                if 'Summary' in control_name:
                    curent_textbox = elem.find_element_by_css_selector("textarea").get_attribute('value')
                else:
                    curent_textbox = elem.find_element_by_css_selector("input[type='text']").get_attribute('value')
                utillity.UtillityMethods.asequal(self, curent_textbox, kwargs['value'], msg)
            if control_type == 'textline':
                elems=self.driver.find_elements_by_css_selector(main_css+" > div[id^='BiVBox'] > div[id^='BiHBox']")
                elem = elems[[control_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
                curent_textline = elem.text.strip().split('\n')[1]
                utillity.UtillityMethods.asequal(self, curent_textline, kwargs['expected_text_line'], msg)
            if control_type == 'checkbox':
                item=self.driver.find_element_by_css_selector("#dlgProperties #maintab div[id^='BiCheckBox']")
                if 'enable' in kwargs or 'disable' in kwargs:
                    lines[item.text.strip().lower()]=item.find_element_by_css_selector("input").is_enabled()
                    for item in y:
                        lines[item.text.strip().lower()]=item.find_element_by_css_selector("input").is_enabled()
                    for key in lines.keys():
                        lines[key]='enable' if lines[key] == True else 'disable'
                    for key in control_name.keys():
                        if control_name[key] == lines[key.lower()].lower():
                            status = True
                        else:
                            status = False
                            break
                    msg = msg if status == True else "Step "+str(re.search(r'\d+', msg).group())+ " " + str(key) +" not found in properties dialog."
                    utillity.UtillityMethods.asequal(self, status, True, msg)
                if 'check' in kwargs or 'uncheck' in kwargs:
                    lines[item.text.strip().lower()]=item.find_element_by_css_selector("input").is_selected()
                    for item in y:
                        lines[item.text.strip().lower()]=item.find_element_by_css_selector("input").is_selected()
                    for key in lines.keys():
                        lines[key]='check' if lines[key] == True else 'uncheck'
                    for key in control_name.keys():
                        if control_name[key].lower() == lines[key.lower()].lower():
                            status = True
                        else:
                            status = False
                            break
                    msg = msg if status == True else "Step "+str(re.search(r'\d+', msg).group())+ " " + str(key) +" not found in properties dialog."
                    utillity.UtillityMethods.asequal(self, status, True, msg)
                del lines
        elif tab_name == 'Advanced':
            tab_name=tab_name.lower()
            advance_tab_text_option = {'Default Height' : '0', 'Default Width' : '1'}
            if control_type == 'textbox':
                elems = self.driver.find_elements_by_css_selector(popup_css + " #" + tab_name + "Tab input[id*='BiTextField']")
                actual_text = elems[int(advance_tab_text_option[control_name])].get_attribute('value')
                utillity.UtillityMethods.asequal(self, actual_text, kwargs['textbox_value'], msg)
            if control_type == 'combobox':
                elem = self.driver.find_element_by_css_selector(popup_css + " #" + tab_name + "Tab [id*='BiComboBox']")
                actual_text = elem.text.strip()
                utillity.UtillityMethods.asequal(self, actual_text, kwargs['combobox_input'])
        if control_type == 'button':
            btn_id = 'OK' if control_name == 'OK' else 'Security' if control_name == 'Security' else 'Cancel'
            button_elem = self.driver.find_element_by_css_selector(popup_css + " [id*='IABottomBar'] #btn" + btn_id)
            utillity.UtillityMethods.default_click(self, button_elem)
        
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
        utillity.UtillityMethods.default_click(self, actual_tab)
        if tab_name == 'Main Properties':
            main_css=popup_css+" #maintab"
            if control_type == 'textbox':
                elems=self.driver.find_elements_by_css_selector(main_css+" > div[id^='BiVBox'] > div[id^='BiHBox']")
                elem = elems[[elem_name in el1 for el1 in [el.text.strip() for el in elems]].index(True)]
                if elem_name == 'File Name':
                    try:
                        elem.find_element_by_css_selector("div[id^='BiHBox'] input[id*='BiCheckBox'][checked]")
                    except NoSuchElementException:
                        temp_elem = elem.find_element_by_css_selector("div[id^='BiHBox'] input[id*='BiCheckBox']")
                        utillity.UtillityMethods.default_click(self, temp_elem)
                curent_textbox = elem.find_element_by_css_selector("input[type='text']")
                utillity.UtillityMethods.set_text_field_using_actionchains(self, curent_textbox, kwargs['textbox_input'])
            if control_type == 'checkbox':
                checkbox_elems=self.driver.find_elements_by_css_selector("#flagList div[class*='label']")
                elem=checkbox_elems[[el.text.strip() for el in checkbox_elems].index(elem_name)]
                try:
                    elem.find_element_by_css_selector("input[checked]")
                    current_status=True
                except NoSuchElementException:
                    current_status=False
                verify_status=False if kwargs['checkbox_input']=='check' else True
                verify_status_msg='UnCheck' if kwargs['checkbox_input']=='check' else 'Check'
                utillity.UtillityMethods.asequal(self, current_status, verify_status, kwargs['msg']+": Verify the "+elem_name+" default status "+verify_status_msg+".")
                utillity.UtillityMethods.default_click(self, elem)
        elif tab_name == 'Advanced':
            tab_name=tab_name.lower()
            advance_tab_text_option = {'Default Height' : '0', 'Default Width' : '1'}
            if control_type == 'textbox':
                elems = self.driver.find_elements_by_css_selector(popup_css + " #" + tab_name + "Tab input[id*='BiTextField']")
                actual_elem = elems[int(advance_tab_text_option[elem_name])]
                utillity.UtillityMethods.set_text_field_using_actionchains(self, actual_elem, kwargs['text_input'], keyboard_type=True)
            if control_type == 'combobox':
                elem = self.driver.find_element_by_css_selector(popup_css + " #" + tab_name + "Tab [id*='BiComboBox'] [id*='BiButton']")
                utillity.UtillityMethods.select_any_combobox_item(self, elem[0], kwargs['combobox_input'])
        else:
            print("Please select appropriate Tab option.")
        if control_type == 'button':
            btn_id = 'OK' if elem_name == 'OK' else 'Security' if elem_name == 'Security' else 'Cancel'
            button_elem = self.driver.find_element_by_css_selector(popup_css + " [id*='IABottomBar'] #btn" + btn_id)
            utillity.UtillityMethods.default_click(self, button_elem)
            
    def change_repository_elem_title(self, folder_path, menu_item, title_name, **kwargs):
        """
        :param folder_path="P292->S10117"
        :param menu_item="Change Title"
        :param title_name="BIP_Responsive"
        :usage change_repository_elem_title('P292->S10117->BIP_V4_Portal->BIP_Responsive', 'Change Title', 'testing change title')
        @author: AAkhan
        """
        Wf_Legacymainpage.select_menu(self, folder_path, menu_item, **kwargs)
        if sys.platform == 'linux':
            pykeyboard.type_string(str(title_name), interval=1)
            time.sleep(2)
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard.write(title_name, delay=0.5)
            time.sleep(2)
            keyboard.send('enter')
        time.sleep(3)
    
    def expand_tree(self, folder_path, tree_css=None, scroll_elem=None):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Usage expand_tree('S7068->AR-RP-193')
        @author: AAkhan
        """
        if scroll_elem!=None:
            scroll_obj=scroll_elem
        else:
            scroll_obj=self.driver.find_element_by_css_selector("#bipTreePanel div[class='bi-component'][id*='BiComponent']")
        core_utilobj.CoreUtillityMethods.python_move_to_element(self, scroll_obj)
        time.sleep(2)
        core_utilobj.CoreUtillityMethods.python_move_to_element(self, scroll_obj, yoffset=-9)
        Wf_Legacymainpage.verify_legacy_home_page_set_to_default(self)
        if tree_css != None:
            tree_rows=tree_css
        else:
            tree_rows="#bipTreePanel #treeView table>tbody>tr"
        folder_list=folder_path.split('->')
        repository_tree_items = self.driver.find_elements_by_css_selector(tree_rows)
        resource_tree_items_list = javascript.JavaScript.get_elements_text(self, repository_tree_items)
        folder_img_elem=utillity.UtillityMethods.validate_and_get_webdriver_object(self, "td>img[class='icon']", 'Resource tree', parent_object=repository_tree_items[resource_tree_items_list.index(folder_list[0])])
        vfour_miscelaneous.Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img_elem, number_of_time=19, direction='up')
        for item in folder_list:
            repository_items = self.driver.find_elements_by_css_selector(tree_rows)
            resource_tree_list = javascript.JavaScript.get_elements_text(self, repository_items)
            if item not in resource_tree_list:
                raise KeyError(item+ " Not Exist in setup "+ self.driver.current_url)
            try:
                for i in range(len(repository_items)):
                    if repository_items[i].text.strip() == item:
                        try:
                            if item == folder_list[-1]:
                                folder_img = repository_items[i].find_element_by_css_selector("td>img.icon")
                            else:
                                folder_img = repository_items[i].find_element_by_css_selector("td>img[src*='triangle_collapsed']")
                            vfour_miscelaneous.Vfour_Miscelaneous.scroll_within_resource_tree(self, scroll_obj, folder_img)
                            core_utilobj.CoreUtillityMethods.left_click(self, folder_img)
                            time.sleep(3)
                            if item == folder_list[-1]:
                                return (i)
                        except:
                            if item == folder_list[-1]:
                                return (i)
                        break
            except NoSuchElementException as e:
                print(e,item + " not found in Repository Tree view. It might be a Bug also.")

    def right_click_on_tree_elem(self, elem, **kwargs):
        """
        :Param : elem = elem                        '''Need to pass object of the element.'''
        :Usage right_click_on_tree_elem(elem)
        @author: AAkhan
        """ 
        tree_rows="#bipTreePanel #treeView table>tbody>tr"
        repository_items = self.driver.find_elements_by_css_selector(tree_rows)
        td_img = repository_items[elem].find_element_by_css_selector("img.icon")
        core_utilobj.CoreUtillityMethods.right_click(self, td_img)
        
    def select_menu(self, folder_path, menu_item=None, **kwargs):
        """
        :Param : folder_path = 'S7068->AR-RP-193'
        :Param : menu_item = 'Edit' or 'Run'
        :kwargs['item_exit']= True or False
        :kwargs['expected_menu_list']= ['TextEditor', 'URL'] 
        :kwargs['msg']= "Step 11"
        :Syntax: select_menu('S7068->AR-RP-193', 'Run')
        @author: AAkhan
        """
        expand = Wf_Legacymainpage.expand_tree(self, folder_path)
        repository_items = self.driver.find_elements_by_css_selector("#bipTreePanel #treeView table>tbody>tr")[expand]
        javascript.JavaScript.scrollIntoView(self, repository_items, wait_time=3)
        Wf_Legacymainpage.right_click_on_tree_elem(self, expand, **kwargs)
        popup_css="div[id^='BiPopup'][style*='inherit']"
        popup_menu_css="table>tbody>tr"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, popup_css, 1, expire_time=15)
        if menu_item == None:
            pass
        else:
            menu_list = menu_item.split('->')
            for j in range(len(menu_list)):
                popups = self.driver.find_elements_by_css_selector(popup_css)
                core_utilobj.CoreUtillityMethods.move_to_element(self, popups[-1], element_location='top_middle', yoffset=3)
                menu_items = popups[-1].find_elements_by_css_selector(popup_menu_css)
                for i in range(len(menu_items)):
                    if menu_list[-1] in menu_items[i].text.strip():
                        core_utilobj.CoreUtillityMethods.left_click(self, menu_items[i])
                        break
                    elif menu_list[j] in menu_items[i].text.strip():
                        arrow_elem=menu_items[i].find_element_by_css_selector("td.arrow")
                        core_utilobj.CoreUtillityMethods.move_to_element(self, arrow_elem, xoffset=3)
                        popups = self.driver.find_elements_by_css_selector(popup_css)
                        core_utilobj.CoreUtillityMethods.move_to_element(self, popups[-1], element_location='top_middle', yoffset=3)
        if 'expected_menu_list' in kwargs:
            popups = self.driver.find_elements_by_css_selector(popup_css)
            menu_items = popups[-1].find_elements_by_css_selector(popup_menu_css)
            actual_elem=[el.text.strip().replace(' ','') for el in menu_items]
            actual_elem = [elem for elem in actual_elem if elem != '']
            expected_elem = [exp.replace(' ', '') for exp in kwargs['expected_menu_list']]
            count_= 1
            for elem in expected_elem:
                status_=True if elem in actual_elem else False
                verification_msg = "Visible" if kwargs['item_exit'] == True else "Not Visible"
                utillity.UtillityMethods.asequal(self, kwargs['item_exit'], status_, str(kwargs['msg']) + "." + str(count_) + " : Verify "+ elem + " Option "+verification_msg+" in Repository menu")
                count_ += 1
        utillity.UtillityMethods.switch_to_default_content(self, pause=2)
    
    def create_url(self, url, **kwargs):   
        """
        :kwargs [url_title]='Open an existing Reporting Object to report from'
        :kwargs[ok_btn]=True
        :Syntax: create_url(setup_url, url_title='Open an existing Reporting Object to report from', ok_btn=True)
        """   
        css = "[id='createURLDialog'] [class*='active']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, css, 1, expire_time=15)
        if 'url_title' in kwargs:
            title=self.driver.find_element_by_css_selector("[id='urlnewdesc'][class*='text-field-focus']")
            utillity.UtillityMethods.set_text_field_using_actionchains(self, title, kwargs['url_title'])
        if 'url_summary' in kwargs:
            summary=self.driver.find_element_by_css_selector("[id='urlnewsummary'][class*='bi-text-field text-field']")
            utillity.UtillityMethods.set_text_field_using_actionchains(self, summary, kwargs['url_summary'])
        new_url=self.driver.find_element_by_css_selector("[id='newurl'][class*='bi-text-field text-field']")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, new_url, url)
        if 'ok_btn' in kwargs:
            clk_btn=self.driver.find_element_by_id('btnOK')
        else:
            clk_btn=self.driver.find_element_by_id('btnCancel')
        utillity.UtillityMethods.default_left_click(self,object_locator=clk_btn, **kwargs)
        time.sleep(2)
    