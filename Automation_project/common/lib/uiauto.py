import uiautomation as uiauto
import pyautogui

class Utils:
    
    @staticmethod
    def get_control_coordinates(control_object, location='middle', xoffset=0, yoffset=0):
        """
        Return specified location of rectangle based on x, y, width and height value
        @arg x = x value of rectangle
        @arg y = y value of rectangle
        @arg width = width of rectangle
        @arg height = height of rectangle
        @arg location = location of rectangle (example :  middle, top_middle, bottom middle)
        """
        x = control_object.BoundingRectangle[0]
        y = control_object.BoundingRectangle[1]
        width = control_object.BoundingRectangle[2] - control_object.BoundingRectangle[0]
        height = control_object.BoundingRectangle[3] - control_object.BoundingRectangle[1]
        if location.lower() == 'middle' :
            """Return x and y value of rectangle middle location as tuple"""
            x = x + (width/2) + xoffset
            y = y + (height/2) + yoffset
            return (x, y)
        elif location.lower() == 'middle_left' :
            """Return x and y value of rectangle middle left location as tuple"""
            x = x + xoffset
            y = y + (height/2) + yoffset
            return (x, y)
        elif location.lower() == 'middle_right' :
            """Return x and y value of rectangle middle right location as tuple"""
            x = x + width + xoffset
            y = y + (height/2) + yoffset
            return (x, y)
        elif location.lower() == 'top_middle' :
            """Return x and y value of rectangle top middle location as tuple"""
            x = x + (width/2) + xoffset
            y = y + yoffset
            return (x, y)
        elif location.lower() == 'top_left' :
            """Return x and y value of rectangle top left location as tuple"""
            x = x + xoffset
            y = y + yoffset
            return (x, y)
        elif location.lower() == 'top_right' :    
            """Return x and y value of rectangle top right location as tuple"""
            x = x + width + xoffset
            y = y + yoffset
            return (x, y)
        elif location.lower() == 'bottom_middle' :    
            """Return x and y value of rectangle bottom middle location as tuple"""
            x = x + (width/2) + xoffset
            y = y + height + yoffset
            return (x, y)
        elif location.lower() == 'bottom_left' : 
            """Return x and y value of rectangle bottom left location as tuple"""
            x = x + xoffset
            y = y + height + yoffset
            return (x, y)
        elif location.lower() == 'bottom_right' : 
            """Return x and y value of rectangle bottom right location as tuple"""
            x = x + width + xoffset
            y = y + height + yoffset
            return (x, y)
        else :
            error_msg = "{0} location currently not implemented".format(location)
            raise NotImplemented(error_msg)
    
class FileDialog:
    
    def __init__(self):
        
        self.parent_window = uiauto.WindowControl(ClassName='#32770')
        
    def enter_file_name(self, file_name):
        """
        Description : Enter the directory path in Address text box
        """
        self.parent_window.EditControl(Name='File name:').Exists(maxSearchSeconds=30, printIfNotExist=True)
        file_textbox = self.parent_window.EditControl(Name='File name:')
        file_textbox.SendKeys(file_name)
        file_textbox.SendKey(uiauto.Keys.VK_ENTER)
        
    def click_open_button(self):
        """
        Description : Left click open button
        """
        open_button = self.parent_window.ButtonControl(Name='Open', ClassName='Button')
        pyautogui.click(*Utils.get_control_coordinates(open_button))
    
    def click_cancel_button(self):
        """
        Description : Left click cancel button
        """
        open_button = self.parent_window.ButtonControl(Name='Cancel', ClassName='Button')
        pyautogui.click(*Utils.get_control_coordinates(open_button))
    
    def select_file(self, file_name):
        """
        Description : Left click on file to select
        """
        file_obj = self._get_file_list_item_object_(file_name)
        pyautogui.click(*Utils.get_control_coordinates(file_obj))
    
    def select_multiple_file(self, file_name_list):
        """
        Description : Left click on given all file to select
        :Usage - select_multiple_file(['__init__', 'as_panels'])
        """
        try:
            uiauto.PressKey(uiauto.Keys.VK_CONTROL)
            for file_name in file_name_list:
                file_obj = self._get_file_list_item_object_(file_name)
                pyautogui.click(*Utils.get_control_coordinates(file_obj))
            uiauto.ReleaseKey(uiauto.Keys.VK_CONTROL)
        except Exception:
            uiauto.ReleaseKey(uiauto.Keys.VK_CONTROL)
            raise(Exception)
        
    def open_file(self, file_path):
        """
        Description : Select given file and click on Open button
        """
        self.enter_file_name(file_path)
        
    def open_multiple_file(self, file_name_list, folder_path=None):
        """
        Description : Select given files and click on Open button
        """
        (folder_path != None) and self.enter_file_name(folder_path)
        self.select_multiple_file(file_name_list)
        self.click_open_button()
    
    def _get_file_list_item_object_(self, file_name):
        """
        Description : Return the file list item object if exists else raise error
        :Usage - _get_file_list_item_object_('test')
        """
        previous_files = []
        while True:
            file_list_items = self.parent_window.PaneControl(Name='Shell Folder View').ListControl(Name='Items View').GetChildren()
            current_file_name = [file.Name for file in file_list_items]
            if file_name in current_file_name:
                file_list_item = file_list_items[current_file_name.index(file_name)]
                file_list_item.ScrollIntoView()
                return file_list_item
            if previous_files == current_file_name:
                msg = '[{0}] File does not exists in [{1}] dialog window'.format(file_name, self._title_)
                raise FileNotFoundError(msg)
            else:
                file_list_items[-1].ScrollIntoView()
            previous_files = current_file_name.copy()