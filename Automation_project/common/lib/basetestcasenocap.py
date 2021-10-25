import unittest, time
from selenium import webdriver
from common.lib.utillity import UtillityMethods
from common.lib import utillity
from common.lib import global_variables
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
import uiautomation 

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        UtillityMethods.asert_failure_count=0
        browser = UtillityMethods.parseinitfile(self,'browser')
        browser_driver = UtillityMethods.parseinitfile(self,'browser_driver')
        if browser == 'Firefox':
            self.driver=webdriver.Firefox()
#             binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
#             self.driver = webdriver.Firefox(firefox_binary=binary)
        elif browser == 'Chrome':
            options = webdriver.ChromeOptions()
            prefs = {"download.prompt_for_download": False}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--disable-print-preview')
            options.add_argument('--disable-infobars')
            self.driver = webdriver.Chrome(browser_driver,chrome_options=options)
        elif browser == 'IE':
            cap = DesiredCapabilities.INTERNETEXPLORER
            #cap['enablePersistentHover'] = False
            cap['requireWindowFocus']=False
            #cap['nativeEvents']= True
            self.driver = webdriver.Ie(capabilities=cap)
        elif browser == 'Edge':
            cap = DesiredCapabilities.EDGE
            cap['pageLoadStrategy'] = "eager"
            self.driver = webdriver.Edge(capabilities=cap)
        elif browser == 'Safari':
            self.driver = webdriver.Safari()
        else:
            print('Verify Browser may not defined in config')
        self.driver.maximize_window()
        

    def tearDown(self):
        filename_obj=self._testMethodName
        setup_url = UtillityMethods.get_setup_url(self)
        user_id = UtillityMethods.parseinitfile(self, 'mrid')
#         filename = os.getcwd() + "\\failure_captures\\"+ self._testMethodName + ".png"
        script_failure_occurred=False
        for method, error in self._outcome.errors:
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
            for item in global_variables.Global_variables.verification_failure_msg_list:
                verification_failure_msg = verification_failure_msg + '\n' + item
            raise_msg='Verification check point failed. The set up used is [{url}] - mrid user: {user}. {VP}'.format(url=setup_url, user=user_id, VP=verification_failure_msg)
            raise ValueError(raise_msg)
        elif script_failure_occurred==True:
            script_filure_error_msg='Script failed to complete the run. The set up used is [' + setup_url + '] - user [' + user_id + '].'
            raise RuntimeError(script_filure_error_msg)
    
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
