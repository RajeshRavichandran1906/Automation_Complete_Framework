from common.lib.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import time
import uiautomation as automation

class AS_Environment_Tree_And_Detail(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    
    def __init__(self, driver):
        super(AS_Environment_Tree_And_Detail, self).__init__(driver)
        
        self.driver = driver
        self.shortwait = WebDriverWait(self.driver, 50)
        self.mediumwait = WebDriverWait(self.driver, 100)
        self.longwait = WebDriverWait(self.driver, 150)
                            
    def ui_double_click_tree_view_item(self, tree_path,**kwargs):
        
        '''==========================================================================
        Description : To expand any folder or to double click any file.
        using click in right click menu for ENV Tree: as_utilo_obj.select_tree_view_item_using_ui(self,tree_path,**kwargs):
        @author: Robert
        ========================================================================='''
        
        try:
            pyautogui.FAILSAFE=False
            driver = self.driver
            if "Parent_Object" in kwargs:
                driver.find_element(*kwargs["Parent_Object"]).click()
            else:
                driver.find_element_by_class_name("SysTreeView32").click()
            pyautogui.hotkey("home")
            path_list=tree_path.split("->")
            for i in path_list:
                automation.TreeItemControl(Name=i).ScrollIntoView()
                automation.TreeItemControl(Name=i).DoubleClick()
        except:
                print("No Element Found")
                
    def select_component_by_right_click(self,**kwargs):
        
        '''==========================================================================
        Description : To select any component by right clicking in environment tree or environment detail
        using click in right click menu for ENV Tree: as_utilobj.select_component_by_right_click(right_click_folder=folder name or file name,click='New',click_sub_menu='Report',send_keys=['down','down','right'])
        using click in right click menu for ENV Detail: as_utilobj.select_component_by_right_click(right_click_item_env_detail=right_click_folder=folder name or file name,click='Run')
        @author: adithyaa
        ========================================================================='''
        
        env_list_class_name="SysListView32"
        right_click='right'
         
        try:
                          
            tree_view = automation.TreeControl(AutomationId="2")
            tree_view.Click(ratioX=10,ratioY=140)
            
            if 'right_click_folder' in kwargs:
                
                verify_tree_item=tree_view.TreeItemControl(Name=kwargs['right_click_folder']).Exists()
                
                if verify_tree_item != False:
                    tree_view.TreeItemControl(Name=kwargs['right_click_folder']).ScrollIntoView()
                    tree_view.TreeItemControl(Name=kwargs['right_click_folder']).Click()
                    time.sleep(1)
                    automation.SendKey(automation.Keys.VK_ESCAPE,waitTime=3)   
                    time.sleep(3)
                else:
                    print("Right_click_folder does not exist")
            
            if 'right_click_item' in kwargs:
                
                verify_tree_item=tree_view.TreeItemControl(Name=kwargs['right_click_item']).Exists()
                
                if verify_tree_item != False:
                    tree_view.TreeItemControl(Name=kwargs['right_click_item']).ScrollIntoView()
                    tree_view.TreeItemControl(Name=kwargs['right_click_item']).Click()
                    time.sleep(1)
                    automation.SendKey(automation.Keys.VK_ESCAPE,waitTime=3)  
                    time.sleep(3) 
                else:
                    print("Right_click_folder does not exist")
                
            if 'right_click_item_env_detail' in kwargs:
           
                list_view=automation.ListControl(ClassName=env_list_class_name)
                list_view.Click(ratioX=45,ratioY=60)
                
                verify_list_item=list_view.ListItemControl(Name=kwargs['right_click_item_env_detail']).Exists()
            
                if verify_list_item != False:
                    list_view.ListItemControl(Name=kwargs['right_click_item_env_detail']).ScrollIntoView()
                    list_view.ListItemControl(Name=kwargs['right_click_item_env_detail']).Click()
                    time.sleep(1)
                    automation.SendKey(automation.Keys.VK_ENTER,waitTime=3) 
                    time.sleep(3)
                else:
                    print("Right_click_env_detail_item could not be found") 
                
            pyautogui.click(button=right_click)
                
            if 'send_keys' in kwargs:
                pyautogui.press(kwargs['send_keys'],interval=0.25)
                
            if 'click' in kwargs:
                automation.MenuItemControl(Name=kwargs['click']).Click()
                
            if 'click_sub_menu' in kwargs:
                automation.MenuItemControl(Name=kwargs['click_sub_menu']).Click()
                    
        except Exception or TimeoutError or LookupError:
            print("No avaliability of searching element")
            
    def select_multiple_files(self,initial_file,files_to_select,**kwargs):
        
        '''===========================================================================================
        Usage: To select multiple files for doing any right click action
        :param: initial_file="first_file_name_to_be_clicked", files_to_select=['CarTwoParms','Chart1']
        :Syntax: as_utilobj.select_multiple_files("CarParm",['CarTwoParms','Chart1'])
        @author: adithyaa
        =============================================================================================='''
        
        list_view=self.driver.find_element_by_class_name("SysTreeView32")
        
        automation.TreeItemControl(Name=initial_file).Click()
        pyautogui.keyDown('ctrl')
        time.sleep(2)
        
        for items in files_to_select:
            if list_view.find_element_by_name(items).is_displayed():
                automation.TreeItemControl(Name=items).Click()
                time.sleep(2)
                            
        if "send_keys" in kwargs:
            pyautogui.click(button='right')
            pyautogui.keyUp('ctrl')
            time.sleep(1)
            pyautogui.press(kwargs["send_keys"])
            
        if "click" in kwargs:
            pyautogui.click(button='right')
            pyautogui.keyUp('ctrl')
            time.sleep(1)
            automation.MenuItemControl(Name=kwargs["click"]).Click()
            
        pyautogui.keyUp('ctrl')
        time.sleep(2)
        
    def click_element_using_ui(self,**kwargs): 
        
        '''==========================================================
        Description : To click the elements using ui automation functionality
        Usage : as_utility.click_element_using_ui(self,menu_item=True,name='Show Projects area')
        @author: adithyaa
        ===========================================================''' 
        
        try:
             
            if 'tree_item' in kwargs:
                automation.TreeItemControl(Name=kwargs['tree_item']).DoubleClick(waitTime=2)
                
            if 'tree_item_click' in kwargs:
                automation.TreeItemControl(Name=kwargs['tree_item_click']).Click()
            
            if "list_item" in kwargs:
                automation.ListItemControl(Name=kwargs['list_item']).Click()
                
            if "list_item_double_click" in kwargs:
                automation.ListItemControl(Name=kwargs["list_item_double_click"]).DoubleClick() 
                       
        except LookupError or TimeoutError:
            print("UI Click element cannot be found")
            
    def select_tree_view_pane_item(self,tree_path,**kwargs):
        
        """
        Usage: select_tree_view_pane_item(jawin7->Domains->P20", Parent_Object = driver.find_element_by_name("Static"))
        params:parent_obj="driver.find_element_by_name("Static" );"jawin7->Domains->P20"
        """ 
        try:
            pyautogui.FAILSAFE=False
            driver = self.driver
            if "Parent_Object" in kwargs:
                driver.find_element(*kwargs["Parent_Object"]).click()
            else:
                tree_view = automation.TreeControl(ClassName="SysTreeView32")
                tree_view.Click(ratioX=10,ratioY=140)
                automation.SendKey(automation.Keys.VK_HOME,waitTime=3) 
            path_list=tree_path.split("->")
            for i in path_list:
                automation.TreeItemControl(Name=i).ScrollIntoView()
                automation.TreeItemControl(Name=i).DoubleClick()
        except:
                print("Tree element does not exist")
            
    def select_right_click_options(self,**kwargs):
        
        '''==========================================================================
        @author: Adithyaa AK
        Description : To select any component by right clicking in environment tree or environment detail
        Usage: Use below function after "as_utilobj.select_tree_view_pane_item"
        
        using click in right click menu: as_utilobj.select_component_by_right_click(right_click_folder='S9100',click='Refresh Descendants')
                                                (((((or)))))
        using click in right click sub menu: as_utilobj.select_component_by_right_click("FWSubFolder",send_keys=['down','down','right'],click='Refresh Descendants')
        ========================================================================='''
        
        env_list_class_name="SysListView32"
        right_click='right'
         
        try:
                          
            tree_view = automation.TreeControl(AutomationId="2")
            tree_view.Click(ratioX=10,ratioY=140)
                
            if 'tree_item' in kwargs:
                
                verify_tree_item=tree_view.TreeItemControl(Name=kwargs['tree_item']).Exists()
                
                if verify_tree_item != False:
                    tree_view.TreeItemControl(Name=kwargs['tree_item']).ScrollIntoView()
                    tree_view.TreeItemControl(Name=kwargs['tree_item']).Click()
                    automation.SendKey(automation.Keys.VK_ENTER,waitTime=2)   
                else:
                    print("Right_click_item does not exist")
                     
            if 'list_item' in kwargs:
           
                list_view=automation.ListControl(ClassName=env_list_class_name)
                list_view.Click(ratioX=45,ratioY=60)
                
                verify_list_item=list_view.ListItemControl(Name=kwargs['list_item']).Exists()
            
                if verify_list_item != False:
                    list_view.ListItemControl(Name=kwargs['list_item']).ScrollIntoView()
                    list_view.ListItemControl(Name=kwargs['list_item']).Click()
    
                else:
                    print("Right_click_env_detail_item does not exist")
                
            pyautogui.click(button=right_click)
                
            if 'send_keys' in kwargs:
                pyautogui.press(kwargs['send_keys'],interval=0.25)
                
            if 'menu' in kwargs:
                automation.MenuItemControl(Name=kwargs['menu']).Click()
                
            if 'sub_menu' in kwargs:
                automation.MenuItemControl(Name=kwargs['sub_menu']).Click()
                    
        except Exception or TimeoutError or LookupError:
            print("No avaliability of searching element")
        