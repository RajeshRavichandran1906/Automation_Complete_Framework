import os, time
from selenium import webdriver
from runners.baserunner import BaseRunner as base 
import uiautomation as automation

class WiniumRunner(base):
    '''
    classdocs
    '''

    def __init__(self, confid, release):
        self.confid=confid
        self.release=release
        '''
        Constructor
        '''
        
    def execute(self):
        aspath='D:/'+self.confid+'/'+self.release+'/ibi/AppStudio82_'+self.release+'/bin/AppStudio.exe'
        os.system('start /min c:/Winium.Desktop.Driver.exe')
        time.sleep(30)
        time_out=80000
        if os.path.isfile(aspath):
            driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={'debugConnectToRunningApp': 'false',
                'app': aspath, 'launchTimeout': time_out, 'launchDelay': time_out
            })
            
            time.sleep(30)
            win_control=automation.WindowControl(ClassName="#32770")
            help_pane=automation.PaneControl(AutomationId="2054")
            automation.WaitForExist(win_control, 60)
            'closing document error window if exists'
            if win_control.Exists():
                automation.WindowControl(ClassName="#32770").Close()
            time.sleep(5)
            'closing welcome window if exists'
            if win_control.Exists():
                automation.WindowControl(ClassName="#32770").Close()
            time.sleep(5)
            'closing help pane by toggling the help button if pane exists'
            automation.WaitForExist(help_pane, 15)
            if help_pane.Exists():
                automation.CheckBoxControl(Name="Help Wizard").Toggle()
            time.sleep(10)
            
        else:
            print(aspath)
            exit()
        return(self)
   
    def close(self):
        os.system("taskkill /f /im  Winium.Desktop.Driver.exe")
        
class Focshell(base):
    '''
    classdocs
    '''

    def __init__(self, confid, release):
        self.confid=confid
        self.release=release
        '''
        Constructor
        '''
        
    def execute(self):
        aspath='D:/'+self.confid+'/'+self.release+'/ibi/AppStudio82_'+self.release+'/bin/FocShell.exe'
        os.system('start /min c:/Winium.Desktop.Driver.exe')
        time.sleep(30)
        time_out=80000
        if os.path.isfile(aspath):
            driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={'debugConnectToRunningApp': 'false',
                'app': aspath, 'launchTimeout': time_out, 'launchDelay': time_out
            })
            time.sleep(30)
            win_control=automation.WindowControl(ClassName="#32770")
            help_pane=automation.PaneControl(AutomationId="2054")
            automation.WaitForExist(win_control, 60)
            'closing document error window if exists'
            if win_control.Exists():
                automation.WindowControl(ClassName="#32770").Close()
            time.sleep(5)
            'closing welcome window if exists'
            if win_control.Exists():
                automation.WindowControl(ClassName="#32770").Close()
            time.sleep(5)
            'closing help pane by toggling the help button if pane exists'
            automation.WaitForExist(help_pane, 15)
            if help_pane.Exists():
                automation.CheckBoxControl(Name="Help Wizard").Toggle()
            time.sleep(10)
            
            
        else:
            print(aspath)
            exit()
        return(self)
   
    def close(self):
        os.system("taskkill /f /im  Winium.Desktop.Driver.exe")