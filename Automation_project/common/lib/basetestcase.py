import unittest, time, sys, os
from common.lib.utillity import UtillityMethods
from common.lib import utillity, global_variables
import keyboard as virtual_keyboard
from common.lib.webdriverfactory.WebDriverFactory import WebDriverFactory
from threading import Thread
from selenium.common.exceptions import WebDriverException
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
else:
    import uiautomation 

class BaseTestCase(unittest.TestCase):
    
    
    def setUp(self):
        if sys.platform == 'linux':
            pykeyboard = PyKeyboard()
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            virtual_keyboard.release('ctrl')
        browser = UtillityMethods.parseinitfile(self,'browser')
        # Enables the Protected mode setting for all zones in IE browser
        if browser.lower() in ['ie', 'ie_current']:
            for zone in range(1,5):
                cmd = ('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet" "Settings\\Zones\\'+str(zone)+' /v 2500 /t REG_DWORD /d 0 /f')
                os.system(cmd)
            print(browser + "'s Protected Mode checked")
        UtillityMethods.kill_browser_process(self)
        self.driver = WebDriverFactory.getInstance(browser)
        global_variables.Global_variables.webdriver = self.driver
        self.driver.maximize_window()
        UtillityMethods.windows=self.driver.window_handles
        global_variables.Global_variables.windows_handles=self.driver.window_handles
        global_variables.Global_variables.current_test_case=self._testMethodName.replace('test_', '').strip()
        BRWSR_NAME=self.driver.desired_capabilities['browserName'].lower()
        if BRWSR_NAME=='microsoftedge':
            UtillityMethods.reset_edge_browser_zoom(self)
            global_variables.Global_variables.browser_name='edge'
        elif BRWSR_NAME=='internet explorer':
            global_variables.Global_variables.browser_name='ie'
        elif BRWSR_NAME == 'msedge':
            global_variables.Global_variables.browser_name='msedge'
        else:
            global_variables.Global_variables.browser_name=BRWSR_NAME
    
    
    def tearDown(self):
        filename_obj=self._testMethodName
        setup_url = str(UtillityMethods.get_setup_url(self))
#         filename = os.getcwd() + "\\failure_captures\\"+ self._testMethodName + ".png"
        script_failure_occurred=False
        for _, error in self._outcome.errors:
            if error:
                script_failure_occurred=True
                try:
                    utillity.UtillityMethods.take_monitor_screenshot(self, filename_obj, image_type='fail')
                except:
                    print("Exception in save_screenshot")
                    utillity.UtillityMethods.take_monitor_screenshot(self, filename_obj, image_type='fail')
        if global_variables.Global_variables.browser_name == 'edge' :
            logout_process = Thread(target=self.logout_webfocus)
            click_leave_button_process = Thread(target=self.click_on_leave_page_button)
            logout_process.start()
            click_leave_button_process.start()
            click_leave_button_process.join()
            logout_process.join()
        else :
            self.logout_webfocus()
        time.sleep(2)
        try:
            self.driver.quit()
        except:
            pass 
        verification_failure_msg='Check Point failure List: '       
        if global_variables.Global_variables.asert_failure_count>0 and script_failure_occurred==False:
            utillity.UtillityMethods.get_user_name(self)
            user_id = str(global_variables.Global_variables.used_username_in_current_session)
            self.generate_html_file_output()
            for item in global_variables.Global_variables.verification_failure_msg_list:
                verification_failure_msg = verification_failure_msg + '\n' + item
            raise_msg='Verification check point failed. The set up used is [{url}] - Test case credentials: [{user}]. \n {VP}'.format(url=setup_url, user=user_id, VP=verification_failure_msg)
            raise ValueError(raise_msg)
        elif script_failure_occurred==True:
            utillity.UtillityMethods.get_user_name(self)
            user_id = str(global_variables.Global_variables.used_username_in_current_session)
            self.generate_html_file_output(Flag=True)
            script_filure_error_msg='Script failed to complete the run. The set up used is [' + setup_url + '] - Test case credentials: [' + user_id + '].\n'
            raise RuntimeError(script_filure_error_msg)
        else:
            self.generate_html_file_output()
    
    def generate_html_file_output(self, Flag=False):
        '''
        This method will generate html file output
        '''
        try:
            if Flag:
                utillity.UtillityMethods.generate_verification_html_file(self, script_exception=True)
            else:
                utillity.UtillityMethods.generate_verification_html_file(self)
            utillity.UtillityMethods.generate_html_file(self)
        except:
            print('Unable to generate html output file ' + global_variables.Global_variables.current_test_case)
            
    
    def logout_webfocus(self): 
        """
        This method used to close window if opened more than one window and logout webfocus
        Note : This method should be remove once https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/16904736/ issue fixed for Edge browser 
        """
        try:
            UtillityMethods.switch_to_main_window(self)
            UtillityMethods.infoassist_api_logout(self)
        except:
            pass
    
    
    def click_on_leave_page_button(self):
        """
        This method used to click on Leave page button when leave page pop up widow appear.
        Note : This method should be remove once https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/16904736/ issue fixed for Edge browser 
        """
        try :
            button = uiautomation.ButtonControl(Name='Leave')
            button.Click()
        except :
            pass