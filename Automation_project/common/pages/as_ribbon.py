from common.lib import utillity
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from common.locators.as_ribbon_locators import AsRibbonLocators
import pyautogui
from pynput.keyboard import Controller
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import uiautomation as automation

class AS_Ribbon(BasePage):
    def __init__(self, driver):
        super(AS_Ribbon, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
       
    def switch_as_tab(self, tab_name): 
        """
        param tab_name: 'Home' OR 'Components....
        Syntax: switch_ia_tab('Components')
        @author = Jesmin        """    
        self.driver.find_element_by_name(tab_name).click() 
        time.sleep(2)
        
    def click_ribbon_item(self,tab_name, ribbon_button_name): 
        """
        param tab_name: 'Home' OR 'Components....
        Syntax: click_ribbon_item('Components','Report')
        Param: param name must be entered as it displayed in AS (upper, lower or mixed cases
        @author = Jesmin"""       
        self.switch_as_tab(tab_name)   
        button_name = tab_name.lower() + "_" + ribbon_button_name.lower()
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3) 
        
    def click_application_menu_item(self,ribbon_button_name):  
        # NEED to test it
        button_name = ribbon_button_name.lower()
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3)
    
    def click_quick_access_toolbar_item(self,ribbon_button_name):
        # NEED to test it
        button_name = ribbon_button_name.lower()
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3)       
              
    def save_document(self,button_name,File_Name):
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3)
        
    def Verify_Tooltip(self,tab_name,component,msg,**kwargs):
        
        '''@author: Adithyaa AK : Description : To verify document canvas panel tooltips 
           ================================================================================
           Usage : as_panels_obj.Verifypanel_Tooltip('5','5','Auto Hide',"Verified - Tooltip is Auto Hide",move_x=-43,move_y=-49)'''
        
        self.switch_as_tab(tab_name) 
        time.sleep(1)
        utilobj= utillity.UtillityMethods(self.driver)
        as1 = self.driver.find_element_by_name(component)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(as1,10,5).perform()
        time.sleep(2)
        del action
            
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
            time.sleep(1)
            
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,component,msg)
        del action 
        
    def Verify_Diff_Tooltip(self,tab_name,component,tooltipname,msg,**kwargs):
        
        '''@author: Adithyaa AK : Description : To verify document canvas ribbon tooltips when ribbon object name and tooltip name differs. 
           ================================================================================================================================
           Usage : as_ribbon_obj.Verify_Difftooltip('Controls','Slider','Horizontal Slider',"Step 14: Verify Generic Elements Tooltip is Grid - Insert Grid",move_x=5,move_y=5)'''

        self.switch_as_tab(tab_name) 
        time.sleep(1)
        utilobj= utillity.UtillityMethods(self.driver)
        as1 = self.driver.find_element_by_name(component)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(as1,10,5).perform()
        del action
        
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
            time.sleep(1)
            
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,tooltipname,msg)
        time.sleep(2)
        del action  
          
    def Verify_Single_Tooltip(self,tab_name,component,msg,**kwargs):
        
        ''':@author: Adithyaa AK : Description : To verify AS Ribbon tooltips for Ribbon Object
        ======================================================================================
        Usage : as_ribbon_obj.Verify_Difftooltip('Slider',"Step 14: Verify Generic Elements Tooltip is Grid - Insert Grid",move_x=5,move_y=5)'''
    
#         self.driver.find_element_by_name('Home').click()
        self.switch_as_tab(tab_name) 
        utilobj= utillity.UtillityMethods(self.driver)
        as1 = self.driver.find_element_by_name(component)
        action = ActionChains(self.driver)
        action.move_to_element(as1).perform()
        time.sleep(1)
        del action
        
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
            time.sleep(1)
            
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,component,msg)
        del action
            
    def Verify_Singlediff_Tooltip(self,tab_name,component,tooltipname,msg,**kwargs):
        
            ''':author: Adithyaa AK : Description : To verify AS Ribbon tooltips when ribbon object name and tooltip name differs.
            =====================================================================================================================
            Usage : as_ribbon_obj.Verify_Difftooltip('Slider','Horizontal Slider',"Step 14: Verify Generic Elements Tooltip is Grid - Insert Grid",move_x=5,move_y=5)'''
            
#             self.driver.find_element_by_name('App Studio').click()
            
            self.switch_as_tab(tab_name) 
            utilobj= utillity.UtillityMethods(self.driver)
            as1 = self.driver.find_element_by_name(component)
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(as1,10,2).perform()
            time.sleep(1)
            del action
            
            if 'move_x' in kwargs:
                action = ActionChains(self.driver)
                action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
                time.sleep(1)
                
            tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(tooltip,tooltipname,msg)
            del action
            
    def Verify_Ribbon_Checkbox(self,tab_name,component):
        
            ''':author: Adithyaa AK : Description : To verify AS Ribbon checkboxes.
            =====================================================================================================================
            Usage : as_ribbon_obj.Verify_Ribbon_Checkbox('File/Folder Properties')'''
        
            self.switch_as_tab(tab_name) 
            time.sleep(1)
            x=self.driver.find_element_by_name(component).is_selected()
            if x==True:
                print(component+'-Checked by default')
            else:
                print(component+'-Unchecked by default')
                
    def Verify_Dropdown_Tooltip(self,component,tooltip,msg,xoffset,yoffset):
        
            '''@author: Adithyaa AK : Description : To verify AS dropdown options tooltips providing direct offset x,y
            =========================================================================================================
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",5,20)'''
        
            utilobj= utillity.UtillityMethods(self.driver)
            self.driver.find_element_by_name(component).click()
            time.sleep(1)
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(1)
            self.driver.find_element_by_name(component).click()
            del action
            
    def Verify_Dropdown_Tooltip_Splitbox(self,component,tooltip,msg,elem_xoffset,elem_yoffset,xoffset,yoffset):
        
            '''===========================================================================================================
            @author: Adithyaa AK : Description : To verify AS dropdown options tooltips by locating element and moving x,y
            Component : Ribbon Element Name
            Tooptip : Tooltip Name
            Msg : Print any message
            elem_xoffset : X value should to click dropdown area of element
            elem_yoffset : Y value should to click dropdown area of element
            xoffset : X value to move to dropdown option
            yoffset : y value to move to dropdown option
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",27,10,5,20)
            ================================================================================================================================='''
        
            utilobj= utillity.UtillityMethods(self.driver)
            action = ActionChains(self.driver)
            x=self.driver.find_element_by_name(component)
            action.move_to_element_with_offset(x,elem_xoffset,elem_yoffset).click().perform()   
            time.sleep(1)
            del action
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(1)
            self.driver.find_element_by_name('Home').click()
            time.sleep(2)
            del action
            
    def Verify_Tab_Dropdown_Tooltip_Splitbox_Click(self,tab_name,component,tooltip,msg,elem_xoffset,elem_yoffset,xoffset,yoffset):
        
            '''===========================================================================================================
            @author: Adithyaa AK : Description : To verify AS dropdown options tooltips by locating element and moving x,y
            tab_name : Tab name to click and activate
            component : Ribbon Element Name
            Tooptip : Tooltip Name
            Msg : Print any message
            elem_xoffset : X value should to click dropdown area of element
            elem_yoffset : Y value should to click dropdown area of element
            xoffset : X value to move to dropdown option
            yoffset : y value to move to dropdown option
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",27,10,5,20)
            ================================================================================================================================='''
            
            self.switch_as_tab(tab_name) 
            utilobj= utillity.UtillityMethods(self.driver)
            action = ActionChains(self.driver)
            x=self.driver.find_element_by_name(component)
            action.move_to_element_with_offset(x,elem_xoffset,elem_yoffset).click().perform()   
            time.sleep(1)
            del action
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(1)
            self.driver.find_element_by_name('Home').click()
            time.sleep(2)
            del action
            
    def Verify_Tab_Dropdown_Tooltip_Splitbox_Move(self,tab_name,component,tooltip,msg,elem_xoffset,elem_yoffset,xoffset,yoffset):
        
            '''===========================================================================================================
            @author: Adithyaa AK : Description : To verify AS dropdown options tooltips by locating element and moving x,y
            tab_name : Tab name to click and activate
            component : Ribbon Element Name to MOVE
            Tooptip : Tooltip Name
            Msg : Print any message
            elem_xoffset : X value should to click dropdown area of element
            elem_yoffset : Y value should to click dropdown area of element
            xoffset : X value to move to dropdown option
            yoffset : y value to move to dropdown option
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",27,10,5,20)
            ================================================================================================================================='''
            
            self.driver.find_element_by_name('Home').click()
            self.switch_as_tab(tab_name) 
            utilobj= utillity.UtillityMethods(self.driver)
            action = ActionChains(self.driver)
            x=self.driver.find_element_by_name(component)
            action.move_to_element_with_offset(x,elem_xoffset,elem_yoffset).perform()   
            time.sleep(1)
            del action
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(2)
            del action
    
    def Click_Ribbon_Dropdown(self,tab,component,childid,dialogname,button,message,xoffset,yoffset):
        
            '''@author: Adithyaa AK : Description : To verify AS Ribbon dropdown Options.
            =================================================================================================================
            Usage : as_ribbon_obj.Click_Ribbon_Dropdown('Home','Data','1','Data Source Definition Wizard','Cancel','message',50,35):'''
        
            self.driver.find_element_by_name(tab).click()
            data=self.driver.find_element_by_name(component)
            data_button = ActionChains(self.driver)
            data_button.move_to_element_with_offset(data,20,50).click().perform()
            del data_button
            time.sleep(1)
            menu=self.driver.find_element_by_id(childid)
            toolbar = ActionChains(self.driver)
            toolbar.move_to_element_with_offset(menu,xoffset,yoffset).click().perform()
            time.sleep(5)
    
            '''Any Wizard opens'''
            booln=self.driver.find_element_by_name(dialogname).is_displayed()
            if booln==True:
                print(message)
                
            '''Click Cancel to close dialog'''
            self.driver.find_element_by_name(dialogname).find_element_by_name(button).click()
            time.sleep(5)
        
        #TODO: call Save As dialog function            
        #TODO: Check if the name already exists. If so, overwrite it. (Or am I supposed to throw an error instead?)
        #Otherwise, find name box within save screen, clear it, and enter the requested name
    '''
        if 'File_Name' in kwargs:
            pyautogui.typewrite(kwargs['File_Name'])
            time.sleep(1)
            self.driver.find_element_by_name("OK").click()
        time.sleep(1)

        try:
            self.driver.find_element_by_id("65535")
            self.driver.find_element_by_name("Yes").click()
            time.sleep(1)
        except: 
            print("Not prompted to overwrite existing HTML")   
            
        ''' 
        
    def as_menu(self,option): 
        """
        :param : option = 'open'
        :Usage: as_ribbon_obj.as_menu('save_as')
        :author: Jesmin
        :date: 04/11/17        """  
         
        opt={'open':'o', 'save':'s', 'save_as':'a','save_all':'l','run':'r','print':'close','close':'c','options':'t','exit':'x'}
        keyboard = Controller()
        pyautogui.PAUSE = 1
        pyautogui.hotkey('alt')
        pyautogui.hotkey('f')
        pyautogui.hotkey('alt')
        #time.sleep(1)
        pyautogui.hotkey('alt')
        #time.sleep(1)
        keyboard.type("f")
        time.sleep(1)
        keyboard.type(opt[option])
        time.sleep(1)
    
    def click_by_offset(self,xoffset,yoffset):
        
        '''@author: Adithyaa AK : Description : To click on any element using offset.
        =================================================================================================================
        Usage : as_ribbon_obj.click_by_offset(self,244,40)'''
         
        action = ActionChains(self.driver)
        action.move_by_offset(xoffset,yoffset).click().perform()
        time.sleep(2)
        del action
                
    def sendkeys_ribbon_shortcut(self,component,msg,**kwargs):
            
            '''@author: Adithyaa AK : Description : To click on any element using offset.
            ============================================================================
            Usage : as_ribbon_obj.click_by_offset(self,)'''
        
            keyboard = Controller()
            shortcut_keys = ActionChains(self.driver)
                
#             if 'key3' in kwargs:
            try:
                shortcut_keys.key_down(Keys.ALT).send_keys(kwargs['key1']).key_up(Keys.ALT).perform()
                del shortcut_keys
                keyboard.type(kwargs['key2'])
                time.sleep(2)   
                keyboard.type(kwargs['key3'])
                time.sleep(2)
                booln=self.driver.find_element_by_name(component).is_displayed()
                if booln==True:
                    print(msg)
            except NoSuchElementException:
                    print('Required Element not Found')
            time.sleep(5)  
            
    def verify_click_checkbox(self,msg,**kwargs):
        
        '''@author: Adithyaa AK : Description : To click any check box in App studio ribbon.
        =================================================================================================================
        Usage : as_ribbon_obj.click_ribbon_checkbox("App Studio",msg,click="Environments Tree")'''
        
        window_exist=automation.WindowControl(RegexName="App Studi.*").GetWindowText()
        automation.WindowControl(Name=window_exist)
        app_connect=automation.WindowControl(Name=window_exist)
        app_connect.SetFocus()
        
        if "click" in kwargs:    
            get_state=app_connect.CheckBoxControl(Name=kwargs['click']).CurrentToggleState()
            if get_state==0:
                app_connect.CheckBoxControl(Name=kwargs['click']).Click()
            else:
                print(kwargs["click"] + "  - Already Checked")
                
        if "uncheck" in kwargs:
                app_connect.CheckBoxControl(Name=kwargs['uncheck']).Click()
                
        if 'verify_checked' in kwargs:
            get_state=app_connect.CheckBoxControl(Name=kwargs['verify_checked']).CurrentToggleState()
            time.sleep(2)
            if get_state==1:
                utillity.UtillityMethods.asequal(self,get_state,1,msg  + kwargs['verify_checked'] + " item checked ")
            if get_state==0:
                utillity.UtillityMethods.asequal(self,get_state,0,msg  + kwargs['verify_checked'] + " item Unchecked ") 
            else:
                pass
            