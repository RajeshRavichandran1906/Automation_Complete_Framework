import time, pyautogui, subprocess, os, re, sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.lib.global_variables import Global_variables
from selenium.common.exceptions import TimeoutException
from common.lib.root_path import ROOT_PATH
from common.lib.javascript import JavaScript


if sys.platform == 'linux':
    from pymouse import PyMouse
else:
    from uisoup import uisoup
    import pywinauto
    import autopy
    import uiautomation

class CoreUtillityMethods(object):
    
    pyautogui.FAILSAFE=False
    
    def __init__(self, driver):
        self.driver = driver
        
    def parseinitfile(self, key):
        init_file = 'config.init'
        config_pair = {}
        try:
            fileObj = open(init_file, "r")
            line = fileObj.readline()
            while line:
                lineObjbj = re.match(r'(\S*)\s(.*)', line)
                keyName = lineObjbj.group(1)
                config_pair[keyName] = lineObjbj.group(2)
                line = fileObj.readline()
            fileObj.close()
        except IOError:
            exit()
        if key in config_pair:
            return (config_pair[key])
        else:
            return ('Key not found')
        
    def get_current_screen_specification(self):
        """
        This will return the specifications like height, width of the current monitor.
        :Usage browser_width, browser_height = CoreUtillityMethods.get_current_screen_specification(self)
        """
        dict_obj={}
        for _time in range(72):
            try:
                dict_obj['screen_width'] = self.driver.execute_script("return screen.width")
                dict_obj['screen_height'] = self.driver.execute_script("return screen.height")
                break
            except TimeoutException:
                time.sleep(5)
            except Exception as e:
                print("Exception occur in get_current_screen_specification- {0}".format(e))
        return (dict_obj)
    
    def get_current_browser_specification(self):
        """
        This will return the specifications like height, width of the actual working area of current focused browser.
        :Usage browser_width, browser_height = UtillityMethods.get_browser_height(self)
        """
        browser_specification_dict_obj={}
        if sys.platform == 'linux':
            browser_specification_dict_obj['browser_width']=self.driver.execute_script("return window.screenX")
            browser_screeny_=self.driver.execute_script("return window.screenY")
            outer_height = self.driver.execute_script("return window.outerHeight")
            inner_height = self.driver.execute_script("return window.innerHeight")
            browser_specification_dict_obj["browser_height"]=int(browser_screeny_ + (outer_height - inner_height))
        else:    
            screen_specification_dict_obj=CoreUtillityMethods.get_current_screen_specification(self)
            for _time in range(72):
                try:
                    outer_height = self.driver.execute_script("return window.outerHeight;")
                    availWidth = self.driver.execute_script("return screen.availWidth;")
                    availHeight = self.driver.execute_script("return screen.availHeight;")
                    innerWidth = self.driver.execute_script("return window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth || document.body.scrollWidth;")
                    scrollHeight=self.driver.execute_script("return document.body.scrollHeight || window.innerHeight;")
                    window_innerheight=self.driver.execute_script("return window.innerHeight || document.body.scrollHeight")
                    if scrollHeight > availHeight or scrollHeight < window_innerheight:
                        innerHeight = window_innerheight
                    else:
                        innerHeight = scrollHeight
                    break
                except TimeoutException:
                    time.sleep(5)
                except Exception as e:
                    print("Exception occur in get_current_browser_specification- {0}".format(e))
            browser_specification_dict_obj['browser_width'] = availWidth - innerWidth
            browser_specification_dict_obj['browser_height'] = availHeight - innerHeight
            browser_specification_dict_obj['outer_height'] = screen_specification_dict_obj['screen_height'] - outer_height
        return (browser_specification_dict_obj)
    
    def update_current_working_area_browser_specification(self):
        '''
        Desc:- This function will update current browser's 'browser_width' and 'browser_height' in the class variable 
        current_working_area_browser_width and current_working_area_browser_height. So when ever we move to any new page 
        we should call this function to keep update these two variables.
        '''
        browser_specification=CoreUtillityMethods.get_current_browser_specification(self)
        Global_variables.current_working_area_browser_x=browser_specification['browser_width']
        Global_variables.current_working_area_browser_y=browser_specification['browser_height']
       
    def get_web_element_coordinate(self, web_element, element_location='middle', xoffset=0, yoffset=0):
        '''
        Desc:- This function will return the any web_object's screen x-y co-ordinate in a dictionary format.
        :param web_element:- the web element whose co-ordinate to be derived.
        :param element_location:- middle, top_left, top_middle, top_right, right_middle, bottom_right, bottom_middle, bottom_left, left_middle, left_top
        elem:- This is the object for which x,y coordinate to be returned.
        coordinate_type='start' OR 'top_middle' OR 'top_right' OR 'left' OR 'middle' OR 'right' OR 'bottom_left' OR 'bottom_middle' OR 'bottom_right' OR 'offset'
        The return type is a dictionary like = {'x': 524, 'y': 993}
        '''
        element_coordinate_dict_obj={}
        elem_x=web_element.location['x'] + Global_variables.current_working_area_browser_x
        elem_y=web_element.location['y'] + Global_variables.current_working_area_browser_y
        elem_h=web_element.size['height']
        elem_w=web_element.size['width']
        if element_location=='top_left':
            element_coordinate_dict_obj['x'] = elem_x + xoffset
            element_coordinate_dict_obj['y'] = elem_y + yoffset
        if element_location=='top_middle':
            element_coordinate_dict_obj['x'] = elem_x + (elem_w/2) + xoffset
            element_coordinate_dict_obj['y'] = elem_y + yoffset
        if element_location=='top_right':
            element_coordinate_dict_obj['x'] = elem_x + elem_w + xoffset
            element_coordinate_dict_obj['y'] = elem_y + yoffset
        if element_location=='middle_left':
            element_coordinate_dict_obj['x'] = elem_x + xoffset
            element_coordinate_dict_obj['y'] = elem_y + (elem_h/2) + yoffset
        if element_location=='middle':
            element_coordinate_dict_obj['x'] = elem_x + (elem_w/2) + xoffset
            element_coordinate_dict_obj['y'] = elem_y + (elem_h/2) + yoffset
        if element_location=='middle_right':
            element_coordinate_dict_obj['x'] = elem_x + elem_w + xoffset
            element_coordinate_dict_obj['y'] = elem_y + (elem_h/2) + yoffset
        if element_location=='bottom_left':
            element_coordinate_dict_obj['x'] = elem_x + xoffset
            element_coordinate_dict_obj['y'] = elem_y + elem_h + yoffset
        if element_location=='bottom_middle':
            element_coordinate_dict_obj['x'] = elem_x + (elem_w/2) + xoffset
            element_coordinate_dict_obj['y'] = elem_y + elem_h + yoffset
        if element_location=='bottom_right':
            element_coordinate_dict_obj['x'] = elem_x + elem_w + xoffset
            element_coordinate_dict_obj['y'] = elem_y + elem_h + yoffset
        return(element_coordinate_dict_obj)
    
    def move_mouse_to_offset(self, x_offset=0, y_offset=0, mouse_move_duration=0.5, pause_time=Global_variables.shortwait):
        '''
        Desc:- This function is used for moving the mouse from the current mouse position to x and y offset provided.
        :param x_offset:- 0, 1, 2, 3.. 
        :param y_offset:- 0, 1, 2, 3..
        '''
        
        CoreUtillityMethods.python_move_to_offset(self, x_offset=x_offset, y_offset=y_offset, mouse_move_duration=mouse_move_duration)
        time.sleep(pause_time)
    
    def move_to_element(self, web_element, element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5, pause_time=Global_variables.shortwait):
        if Global_variables.browser_name in ['firefox','ie', 'edge']:
            CoreUtillityMethods.python_move_to_element(self, web_element, element_location=element_location, xoffset=xoffset, yoffset=yoffset, mouse_move_duration=mouse_move_duration)
        else:
#             CoreUtillityMethods.python_move_to_element(self, web_element, element_location=element_location, xoffset=xoffset, yoffset=yoffset, mouse_move_duration=mouse_move_duration)
            ActionChains(self.driver).move_to_element(web_element).perform()
        time.sleep(pause_time)
    
    def left_click(self, web_element, element_location='middle', xoffset=0, yoffset=0, action_chain_click=False, mouse_move_duration=0.5, pause_time=Global_variables.shortwait):
        '''
        Desc:- This function will click on any web_element on a specified location using option ActionChains and pyautogui action.
        :param web_element:- the web element whose co-ordinate to be derived.
        :param location:- middle, top_left, top_middle, top_right, right_middle, bottom_right, bottom_middle, bottom_left, left_middle, left_top
        '''
        if Global_variables.browser_name in ['ie', 'firefox', 'edge'] :
            CoreUtillityMethods.python_left_click(self, web_element, element_location=element_location, xoffset=xoffset, yoffset=yoffset, mouse_move_duration=mouse_move_duration)
        else:
            if action_chain_click==True:
                ActionChains(self.driver).move_to_element_with_offset(web_element, xoffset, yoffset).click().perform()
            else:
                web_element.click()
        time.sleep(pause_time)
    
    def right_click(self, web_element, element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5, pause_time=Global_variables.shortwait):
        '''
        Desc:- This function will click on any web_element on a specified location using option ActionChains and pyautogui action.
        :param web_element:- the web element whose co-ordinate to be derived.
        :param location:- middle, top_left, top_middle, top_right, right_middle, bottom_right, bottom_middle, bottom_left, left_middle, left_top
        '''
        if Global_variables.browser_name in ['firefox','ie', 'edge', 'chrome', 'msedge']:
            CoreUtillityMethods.python_right_click(self, web_element, element_location=element_location, xoffset=xoffset, yoffset=yoffset, mouse_move_duration=mouse_move_duration)
        else:
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(web_element, xoffset, yoffset).context_click().perform()
            del action
        time.sleep(pause_time)
        
    def double_click(self, web_element, element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5, pause_time=Global_variables.longwait):
        '''
        Desc:- This function will click on any web_element on a specified location using option ActionChains and pyautogui action.
        :param web_element:- the web element whose co-ordinate to be derived.
        :param location:- middle, top_left, top_middle, top_right, right_middle, bottom_right, bottom_middle, bottom_left, left_middle, left_top
        '''
        if Global_variables.browser_name in ['firefox','ie', 'edge', 'chrome', 'msedge']:
            CoreUtillityMethods.python_doubble_click(self, web_element, element_location=element_location, xoffset=xoffset, yoffset=yoffset, mouse_move_duration=mouse_move_duration)
        else:
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(web_element, xoffset, yoffset).double_click().perform()
            del action
        time.sleep(pause_time)
    
    def drag_and_drop(self, x1, y1, x2, y2, mouse_speed=25):
        '''
        Desc:- This function will drag and drop from x1,y1 location to x2,y2 location on the screen..
        :param x1:- start x-coordinate.
        :param y1:- start y-coordinate.
        :param x2:- end x-coordinate.
        :param y2:- end y-coordinate.
        :param mouse_speed:- This is the speed of the mouse per pixel. 25 is normal.
        '''
        if sys.platform == 'linux':
                mouse_=PyMouse() 
                mouse_.press(int(x1), int(y1))
                time.sleep(3)
                pyautogui.moveTo(int(x2), int(y2), duration=3)
                time.sleep(3)
                mouse_.release(int(x2), int(y2))
        else:
            if Global_variables.browser_name=='chrome':
                time.sleep(Global_variables.longwait)
                procesobj = subprocess.Popen(os.path.join(ROOT_PATH, 'drag_drop_helper.exe '+str(x1)+' '+ str(y1)+' '+ str(x2)+' '+ str(y2)+' '+str(mouse_speed)))
                procesobj.wait()
                time.sleep(Global_variables.mediumwait)
                del procesobj
            else:
                mouse_obj=uisoup.mouse
                mouse_obj.click(x1, y1)
                time.sleep(Global_variables.longwait)
                mouse_obj.drag(x1, y1, x2, y2)
                time.sleep(Global_variables.mediumwait)
                mouse_obj.click(x2, y2)
                time.sleep(2*Global_variables.longwait)
            
    def drag_and_drop_without_using_click(self, x1, y1, x2, y2, mouse_speed=25):
        '''
        Desc:- This function will drag and drop from x1,y1 location to x2,y2 location on the screen..
        :param x1:- start x-coordinate.
        :param y1:- start y-coordinate.
        :param x2:- end x-coordinate.
        :param y2:- end y-coordinate.
        :param mouse_speed:- This is the speed of the mouse per pixel. 25 is normal.
        '''
        if sys.platform == 'linux':
                mouse_=PyMouse() 
                mouse_.press(int(x1), int(y1))
                time.sleep(3)
                pyautogui.moveTo(int(x2), int(y2), duration=3)
                time.sleep(3)
                mouse_.release(int(x2), int(y2))
        else:
            if Global_variables.browser_name=='chrome':
                time.sleep(Global_variables.longwait)
                procesobj = subprocess.Popen(os.path.join(ROOT_PATH, 'drag_drop_helper.exe '+str(x1)+' '+ str(y1)+' '+ str(x2)+' '+ str(y2)+' '+str(mouse_speed)))
                procesobj.wait()
                time.sleep(Global_variables.mediumwait)
                del procesobj
            else:
                mouse_obj=uisoup.mouse
                time.sleep(Global_variables.longwait)
                mouse_obj.drag(x1, y1, x2, y2)
                time.sleep(Global_variables.mediumwait)
                time.sleep(2*Global_variables.longwait)
    
    def create_lasso(self, x1, y1, x2, y2, pause=0):
        """
        Desc:- This function will drag and drop from x1,y1 location to x2,y2 location on the screen..
        :param x1:- start x-coordinate.
        :param y1:- start y-coordinate.
        :param x2:- end x-coordinate.
        :param y2:- end y-coordinate.
        :param pause time: wait time after each actions.
        """
        x1, y1, x2, y2=int(x1), int(y1), int(x2), int(y2)
        if sys.platform == 'linux':
                mouse_=PyMouse() 
                time.sleep(pause)
                pyautogui.moveTo(int(x1)-9,int(y1)-9)
                mouse_.press(int(x1), int(y1))
                time.sleep(pause)
                pyautogui.moveTo(int(x2), int(y2), duration=3)
                time.sleep(pause)
                mouse_.release(int(x2), int(y2))
        else:
            import uiautomation as automate
            mouse_obj=uisoup.mouse
            #automate.Win32API.SetCursorPos(x1-9, y1-9)
            automate.SetCursorPos(x1-9, y1-9)
            time.sleep(pause)
            mouse_obj.move(x1, y1)
            time.sleep(pause)
            automate.mouse_event(automate.MouseEventFlag.LeftDown | automate.MouseEventFlag.Absolute, 0, 0, 0, 0)
            time.sleep(pause)
            mouse_obj.move(x2, y2)
            time.sleep(pause)
            automate.mouse_event(automate.MouseEventFlag.Absolute | automate.MouseEventFlag.LeftUp, 0, 0, 0, 0)
            mouse_obj.release_button()
#             time.sleep(2*Global_variables.longwait)
    
    def ie_crash_handler(self, window_title):
        '''
        This function check new browser window opened or browser window crashed in IE.
        '''
        current_working_browser_window_title=self.driver.title
        if window_title != None:
            search_new_window_title = window_title
        else:
            search_new_window_title = current_working_browser_window_title[0:10].replace(' ','').replace('-','')+" - Internet Explorer"
        for x in range(0, 5):
            self.driver.implicitly_wait=0
            try:
                pywinauto.findwindows.find_window(title_re=search_new_window_title)
                time.sleep(5)
                return(0)                     
            except:
                self.driver.implicitly_wait=0
                try:
                    pywinauto.findwindows.find_window(title_re='Internet Explorer')
                    time.sleep(2)
                    os.system(os.getcwd() + "\\common\\lib\\IE_crash_close_program.exe")
                    time.sleep(1)
                    return(1)
                except:
                    pass                            
            time.sleep(5)
        del x
    
    def switch_to_window(self):
        '''
        This function is used to switch from current working browser to specific browser window. 
        '''
        run_loop = True
        count_time=1
        while run_loop:
            if count_time == 90:
                raise TimeoutError('No new window found to switch.')
            if len(self.driver.window_handles) > len(Global_variables.windows_handles):
                run_loop = False
            count_time += 1
            time.sleep(1)
        old_windows=Global_variables.windows_handles
        new_windows=self.driver.window_handles
        new_set=set(new_windows)
        old_set=set(old_windows)
        diff_set=new_set-old_set
        last_window=list(diff_set)
        self.driver.switch_to.window(last_window[-1])
        
    def update_window_handles_list(self, update='add'):
        '''
        This Function will update the window handles and mantain the 'windows_handles' variable in init section.
        update='add' OR 'remove'
        ''' 
        if update=='add':
            Global_variables.windows_handles.append(self.driver.current_window_handle) 
        if update=='remove':
            unnecessary_window=Global_variables.windows_handles.pop() 
            del(unnecessary_window)
               
    def switch_to_new_window(self, current_browser_window_title=None, window_maximize=True):
        '''
        Desc:- This function will switch the control from the current window to a specified window.
            After switching this will update the browser height, width and window handle list in the available class variable, so that they can be 
            used later. If browser equal to 'IE' and next_window_num is greater than '0' then update only browser height. It will handle IE browser crashed
            only in visualization section.
        :param window_num:- window number Starts with 1, 2, 3..
        :param current_browser_window_title:- current browser window title 
        '''
        try :
            current_window_title = self.driver.title
        except :
            pass
        suite_type = CoreUtillityMethods.parseinitfile(self, 'suite_type')
        if suite_type.lower() == 'visualization' and Global_variables.browser_name in ('ie', 'edge'):
            time.sleep(Global_variables.shortwait)
            status=0
            total_window_num = len(Global_variables.windows_handles)
            if Global_variables.browser_name in ('ie', 'edge') and total_window_num > 1:
                status=CoreUtillityMethods.ie_crash_handler(self, window_title=current_browser_window_title)
            if  status > 0:
                Global_variables.ie_crash_wndnum=0
                raise ConnectionError('IE Browser Crashed.')
        else:
            time.sleep(Global_variables.shortwait)
            total_window_num = len(Global_variables.windows_handles)
        CoreUtillityMethods.switch_to_window(self)
        time.sleep(Global_variables.mediumwait)
        after_switch_window_widht = self.driver.execute_script("return window.innerWidth|| document.documentElement.clientWidth|| document.body.clientWidth;")
        if window_maximize == True:
            if after_switch_window_widht < self.driver.execute_script("return screen.availWidth;"):
                self.driver.maximize_window()
        time_count = 0
        while(after_switch_window_widht < self.driver.execute_script("return screen.availWidth;")):
            time_count+=1
            time.sleep(1)
            if time_count > 39:
                break
        time.sleep(Global_variables.shortwait)
        CoreUtillityMethods.update_current_working_area_browser_specification(self)
        CoreUtillityMethods.update_window_handles_list(self, update='add')
        if Global_variables.browser_name in ('ie') and total_window_num > 0:
            time.sleep(Global_variables.longwait)
            CoreUtillityMethods.update_current_working_area_browser_specification(self)
#             br=CoreUtillityMethods.get_current_browser_specification(self)
#             get_outer_height = br['browser_height'] - br['outer_height']
#             Global_variables.current_working_area_browser_y=br['browser_height'] - get_outer_height
        try :
            if Global_variables.browser_name == 'edge' and suite_type =='visualization' :
                CoreUtillityMethods.bring_edge_window_to_foregound(self, current_window_title)
        except :
            pass
    
    def switch_to_previous_window(self, window_close=True):
        '''
        Desc:- This function will switch the control back to previous window by closing the current window.
        '''
        if window_close == True:
            self.driver.close()
        time.sleep(Global_variables.shortwait)
        CoreUtillityMethods.update_window_handles_list(self, update='remove')
        self.driver.switch_to.window(Global_variables.windows_handles[-1])
        CoreUtillityMethods.update_current_working_area_browser_specification(self)
        #time.sleep(Global_variables.shortwait)      
    
    '''
    This funciton hold for testing purpose
    '''
#     def get_frame_height(self):
#         """
#         This function return back frame height in IA.
#         """
#         dict_obj={}
#         screen_width=self.driver.execute_script("return window.innerWidth|| document.documentElement.clientWidth|| document.body.clientWidth;")
#         ia_tool_width=self.driver.execute_script("return document.getElementById('queryViewPane').clientWidth;")
#         dict_obj['excess_outer_grayed_width']=screen_width-ia_tool_width
#         innerHeight = self.driver.execute_script("return window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;")
#         ia_tool_toptoolbar_height=self.driver.execute_script("return document.getElementById('applicationToolBarBox').clientHeight;")
#         ia_tool_ribbon_height=self.driver.execute_script("return document.getElementById('HomeTab').offsetHeight;")
#         ia_tool_query_height=self.driver.execute_script("return document.getElementById('queryViewPane').clientHeight;")
#         ia_tool_status_height=self.driver.execute_script("return document.getElementById('sbMain').offsetHeight;")
#         dict_obj['excess_outer_grayed_height']=innerHeight-(ia_tool_toptoolbar_height+ia_tool_ribbon_height+ia_tool_query_height+ia_tool_status_height)
#         return (dict_obj)
        
    def switch_to_frame(self, frame_css="[id^='ReportIframe']", timeout=150):
        '''
        Desc:- This function will switch the control to a specified frame.
        :param frame_css:- window number Starts with 1, 2, 3.. 
        :param pause:- sleep control for specific time
        :param timeout:- terminate condition to switch side loop.
        '''
        frame_element_obj = self.driver.find_element_by_css_selector(frame_css)
        frame_actual_location = CoreUtillityMethods.get_web_element_coordinate(self, frame_element_obj, element_location='top_left')
        WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, frame_css)))
        time.sleep(Global_variables.shortwait)
        Global_variables.current_working_area_browser_x=frame_actual_location['x']
        Global_variables.current_working_area_browser_y=frame_actual_location['y']
        #time.sleep(Global_variables.shortwait)
    
    def switch_to_default_content(self):
        '''
        Desc:- This function will switch the default content.
        :param pause:- 0, 1, 2, 3.. 
        '''
        self.driver.switch_to.default_content()
        CoreUtillityMethods.update_current_working_area_browser_specification(self)
        #time.sleep(Global_variables.mediumwait)
        
    '''    **************** python click section    ************* '''
    def python_click_with_offset(self, x=0, y=0):
        '''
        Desc:- This function will do physical mouse click with the x and y values provided.
        :param x:- 0, 20...
        :param y:- 0, 20... 
        '''
        CoreUtillityMethods.python_move_to_offset(self, x_offset=x, y_offset=y, mouse_move_duration=0.5)
        time.sleep(Global_variables.shortwait)
        CoreUtillityMethods.python_click(self)
        
    def python_click(self):
        '''
        Desc:- This function will do physical mouse click on current mouse cursor.
        '''
        pyautogui.click()
        
    def python_left_click(self, web_element, element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5):
        '''
        Desc:- This function will left click on the element using physical mouse cursor move.
        :param web_element 
        :param element_location:- middle
        :param xoffset:- 0, 20...
        :param yoffset:- 0, 20...
        :param mouse_move_duration:- 0.5, 1...
        '''
        (x, y)=CoreUtillityMethods.python_move_to_element(self, web_element, element_location, xoffset, yoffset, mouse_move_duration)
        time.sleep(Global_variables.shortwait)
        if Global_variables.browser_name in ['ie', 'edge'] :
            uisoup.mouse.click(x, y)
        else :
            pyautogui.click(button='left')

    
    def python_right_click(self, web_element, element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5):
        '''
        Desc:- This function will right click on the element using physical mouse cursor move.
        :param web_element
        :param element_location:- middle
        :param xoffset:- 0, 20...
        :param yoffset:- 0, 20...
        :param mouse_move_duration:- 0.5, 1...
        '''
        (x, y)=CoreUtillityMethods.python_move_to_element(self, web_element, element_location, xoffset, yoffset, mouse_move_duration)
        time.sleep(Global_variables.shortwait)
        if Global_variables.browser_name in ['ie', 'edge'] :
            uisoup.mouse.click(x, y, button_name=uisoup.mouse.RIGHT_BUTTON)
        else :
            pyautogui.click(button='right')
    
    def python_doubble_click(self, web_element, element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5):
        '''
        Desc:- This function will double click on the element using physical mouse cursor move.
        :param web_element
        :param element_location:- middle
        :param xoffset:- 0, 20...
        :param yoffset:- 0, 20...
        :param mouse_move_duration:- 0.5, 1...
        '''
        (x,y) = CoreUtillityMethods.python_move_to_element(self, web_element, element_location, xoffset, yoffset, mouse_move_duration)
        time.sleep(Global_variables.shortwait)
        if Global_variables.browser_name in ['ie', 'edge'] :
            uisoup.mouse.double_click(x, y)
        else :
            pyautogui.doubleClick(button='left')
            
    def python_move_to_element(self, web_element, element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5):
        '''
        Desc:- This function will move physical mouse cursor to the element.
        :param web_element
        :param element_location:- middle
        :param xoffset:- 0, 20...
        :param yoffset:- 0, 20...
        :param mouse_move_duration:- 0.5, 1...
        '''
        element_coordinate=CoreUtillityMethods.get_web_element_coordinate(self, web_element, element_location=element_location, xoffset=xoffset, yoffset=yoffset)
        x=element_coordinate['x']
        y=element_coordinate['y']
        if Global_variables.browser_name in ['ie', 'edge'] :
#             uisoup.mouse.move(x, y)
            autopy.mouse.smooth_move(x, y)
        else :
            pyautogui.moveTo(x, y, mouse_move_duration)
        return (x, y)
        
    def python_move_to_offset(self, x_offset=0, y_offset=0, mouse_move_duration=0.5):
        '''
        Desc:- This function will move physical mouse cursor to the x,y values provided.
        :param xoffset:- 0, 20...
        :param yoffset:- 0, 20...
        :param mouse_move_duration:- 0.5, 1...
        '''
        if Global_variables.browser_name in ['ie', 'edge'] :
#             uisoup.mouse.move(x_offset, y_offset)
            autopy.mouse.smooth_move(x_offset, y_offset)
        else:
            pyautogui.moveTo(x_offset, y_offset, mouse_move_duration)
    
    def bring_edge_window_to_foregound(self, window_title):
        """
        Description : Using Uiautomation library bring hidden Edge browser window to foregound
        """
        edge_running_button = uiautomation.PaneControl(Name='Running applications').MenuItemControl(RegexName='Microsoft Edge')
        if edge_running_button.Exists() :
            x = edge_running_button.BoundingRectangle[0] + 20
            y = edge_running_button.BoundingRectangle[1] + 20
            CoreUtillityMethods.python_click_with_offset(self, x, y)
            edge_task_view = uiautomation.ListControl(Name='Task Switcher').ListItemControl(RegexName=window_title)
            (edge_task_view.Exists() != True ) and CoreUtillityMethods.python_click_with_offset(self, x, y)
            x1 = edge_task_view.BoundingRectangle[2] + 50
            y1 = edge_task_view.BoundingRectangle[1] + 50
            CoreUtillityMethods.python_click_with_offset(self, x1, y1)
    
    def get_element_object_by_text_using_javascript(self, element_objects, element_text, error_msg, index=1, scroll_into_view=True):
        """
        Description : Return the element object if element has given text using java script
        :param - element_objects : List of element objects 
        :prarm - element_text : Text value of element to find element
        :param - index - If more than one elements have same text then you can pass index accordingly to get element object. index start from 1
        :param - error_msg - Raise LookUp error if all elements not have given text. If error_msg is None then skip the raise statement
        :scroll_into_view - Bring the found element to view area by using java script. 
        """
        element_object = None
        element_index_list = JavaScript.find_all_index_of_element_by_text(self, element_objects, element_text)
        element_index = element_index_list[index - 1] if (len(element_index_list) >= index) else None
        if element_index is None and error_msg is not None:
            raise LookupError(error_msg)
        if element_index is not None:
            element_object = element_objects[element_index]
            scroll_into_view and JavaScript.scrollIntoView(self, element_object, wait_time=1)
        return element_object
        
    def get_element_object_by_text(self, element_objects, element_text, index=1, error_msg=None, scroll_into_view=True):
        """
        Description : Return the element object if element has given text
        :param - element_objects : List of element objects 
        :prarm - element_text : Text value of element to find element
        :param - index - If more than one elements have same text then you can pass index accordingly to get element object. index start from 1
        :param - error_msg - Raise LookUp error if all elements not have given text. If error_msg is None then skip the raise statement
        :scroll_into_view - Bring the found element to view area by using java script. 
        """
        element_object = None
        element_index_list = [_index_ for _index_, element in enumerate(element_objects) if element.text.strip() == element_text]
        element_index = element_index_list[index - 1] if (len(element_index_list) >= index) else None
        if element_index is None and error_msg is not None:
            raise LookupError(error_msg)
        if element_index is not None:
            element_object = element_objects[element_index]
            scroll_into_view and JavaScript.scrollIntoView(self, element_object, wait_time=1)
        return element_object
    
    def update_config_file(self, key, value):
        """
        Description : Update the script config.init file. 
        If key not in config.init file then create as a new key value
        """
        with open("config.init", "r") as file:
            lines = file.readlines()
        for index, line in enumerate(lines):
            if line.strip().startswith(key) : 
                lines[index] = "{key} {value}\n".format(key=key, value=value)
                break
        else:
            new_line = "\n{key} {value}".format(key=key, value=value)
            lines[-1] = lines[-1].strip()
            lines.append(new_line)
        text = "".join(lines)
        with open("config.init", "w") as file:
            file.write(text)
