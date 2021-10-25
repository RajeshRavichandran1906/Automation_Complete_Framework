'''
Created on Feb 27, 2018

@author: qaauto
'''

import uiautomation as automation
from common.lib import utillity

class UIAutomation_Util_Methods(object):
    
    '''
    This module is based only on UIAutomation, No need of Remote driver [winnium]
    '''
    SHORTWAIT = 2
    WINDOW_WAIT=30
        
    def ui_expand_folder_under_environment_tree(self, window_title, specify_path_seprated_by_arrow):
        '''
        This function is used to expand the folder under envirnment tree
        '''
        AS_MainWindow=automation.WindowControl(Name=window_title)
        AS_MainWindow.SetFocus()
        menulist=specify_path_seprated_by_arrow.split('>')
        for item in menulist:
            if automation.ExpandCollapseState.Collapsed==AS_MainWindow.TreeItemControl(Name=item).CurrentExpandCollapseState():
                AS_MainWindow.TreeItemControl(Name=item).Expand(waitTime=self.SHORTWAIT)
    
    def ui_collapse_folder_under_environment_tree(self, window_title, specify_folder_to_collapse):  
        '''
        This function is used to collapse the folder under envirnment tree
        '''
        AS_MainWindow=automation.WindowControl(Name=window_title)
        AS_MainWindow.SetFocus()
        if automation.ExpandCollapseState.Expanded==AS_MainWindow.TreeItemControl(Name=specify_folder_to_collapse).CurrentExpandCollapseState():
            AS_MainWindow.TreeItemControl(Name=specify_folder_to_collapse).Collapse(waitTime=self.SHORTWAIT)
    
    def ui_add_fields_in_report_canvas(self, window_title, field_path_with_or_field_name):
        
        AS_MainWindow=automation.WindowControl(Name=window_title)
        AS_MainWindow.SetFocus()
        field_list=field_path_with_or_field_name.split('>')
        if len(field_list)>0:
            UIAutomation_Util_Methods.ui_expand_folder_under_environment_tree(self, window_title, field_list[:-1])
        AS_MainWindow.TreeItemControl(Name=field_list[-1]).DoubleClick(waitTime=self.SHORTWAIT*2)
        
    def verify_rightclick_menu_items(self, window_title, specify_folder_name, menu_className, expected_menu_list, msg):
        actual_menu_list=[]
        AS_MainWindow=automation.WindowControl(Name=window_title)
        AS_MainWindow.SetFocus()
        AS_MainWindow.TreeItemControl(Name=specify_folder_name).RightClick(waitTime=self.SHORTWAIT)
        Menu=AS_MainWindow.MenuControl(RegexName=menu_className).GetChildren()
        #Menu=AS_MainWindow.MenuControl(RegexName='AFX:.*').GetChildren()
        for MenuItem in Menu:
            if MenuItem.Name!='':
                actual_menu_list.append(MenuItem.Name)
        print(expected_menu_list)
        print(actual_menu_list)
        utillity.UtillityMethods.asequal(self, expected_menu_list, actual_menu_list, msg)
    
    def verify_item_exist_in_menu_list(self, window_title, specify_folder_name, menu_className, item_to_be_verified, msg):
        status=False
        AS_MainWindow=automation.WindowControl(Name=window_title)
        AS_MainWindow.SetFocus()
        AS_MainWindow.TreeItemControl(Name=specify_folder_name).RightClick(waitTime=self.SHORTWAIT)
        Menu=AS_MainWindow.MenuControl(RegexName=menu_className).GetChildren()
        #Menu=AS_MainWindow.MenuControl(RegexName='AFX:.*').GetChildren()
        for MenuItem in Menu:
            if MenuItem.Name == item_to_be_verified:
                status=True
                break
        utillity.UtillityMethods.asequal(self, True, status, msg)
        
    def select_rightclick_menu_item(self, window_title, specify_folder_name, menu_className, select_item):
        AS_MainWindow=automation.WindowControl(Name=window_title)
        AS_MainWindow.SetFocus()
        AS_MainWindow.TreeItemControl(Name=specify_folder_name).RightClick(waitTime=self.SHORTWAIT)
        Menu=AS_MainWindow.MenuControl(RegexName=menu_className).GetChildren()
        for MenuItem in Menu:
            if MenuItem.Name == select_item:
                AS_MainWindow.MenuItemControl(Name=MenuItem.Name).Click(waitTime=self.SHORTWAIT)
                break
                #MenuItem.Click(waitTime=self.SHORTWAIT)
        
    def verify_submenu_items(self, window_title, submenu_className,expected_submenu_list, msg):
        actual_submenu_list=[]
        AS_MainWindow=automation.WindowControl(Name=window_title)
        SubMenu=AS_MainWindow.MenuControl(RegexName=submenu_className).GetChildren()
        #Menu=AS_MainWindow.MenuControl(RegexName='AFX:.*', Name='New').GetChildren()
        for subMenuItem in SubMenu:
            if subMenuItem.Name!='':
                actual_submenu_list.append(subMenuItem.Name)
        utillity.UtillityMethods.asequal(self, expected_submenu_list, actual_submenu_list, msg)
    
    def verify_item_exist_in_submenu_list(self, window_title, submenu_className, submenu_name, item_to_be_verified, msg):
        status=False
        AS_MainWindow=automation.WindowControl(Name=window_title)
        SubMenu=AS_MainWindow.MenuControl(RegexName=submenu_className, Name=submenu_name).GetChildren()
        #Menu=AS_MainWindow.MenuControl(RegexName='AFX:.*', Name='New').GetChildren()
        for SubMenuItem in SubMenu:
            if SubMenuItem.Name == item_to_be_verified:
                status=True
                break
        utillity.UtillityMethods.asequal(self, True, status, msg)
        
    def select_submenu_item(self, window_title, submenu_className, submenu_name, select_submenu_item):
        AS_MainWindow=automation.WindowControl(Name=window_title)
        SubMenu=AS_MainWindow.MenuControl(RegexName=submenu_className, name=submenu_name).GetChildren()
        for SubMenuItem in SubMenu:
            if SubMenuItem.Name == select_submenu_item:
                AS_MainWindow.MenuItemControl(Name=SubMenuItem.Name).Click(waitTime=self.SHORTWAIT)
                break
                #SubMenuItem.Click(waitTime=self.SHORTWAIT)
                
    def close_current_window(self,windowname):
        '''
        This function is used to close a given window
        Usage: close_current_window('HtmlPag.*')
        '''
        automation.WindowControl(RegexName=windowname).Close()
        
    def maximize_window(self, windowname):
        '''
        This function is used to maximize a given window
        Usage: maximize_window('HtmlPag.*')
        '''
        control=automation.WindowControl(RegexName=windowname)
        automation.WaitForExist(control, self.WINDOW_WAIT)
        control.Maximize(self.SHORTWAIT)   
        
        
        
        
        
        
        
        
        