from appium import webdriver
from common.lib.mobile_utillity import UtillityMethods
from common.lib.appiumcapabilities import AppiumCapabilities
import unittest,os,time,platform
 
class BaseTestCase(unittest.TestCase):
     
    def setUp(self):
         
        UtillityMethods.asert_failure_count=0
        self.test=UtillityMethods.parseinitfile(self,'test')
        device_name=UtillityMethods.parseinitfile(self,'device_name')
        device_id=UtillityMethods.parseinitfile(self,'device_id')
        device_version=UtillityMethods.parseinitfile(self,'device_version')
        appium_server=UtillityMethods.parseinitfile(self,'appium_server')
        capabilities=AppiumCapabilities.Capabilities(self, self.test,device_id,device_version,device_name)
        time.sleep(2)
        self.driver=webdriver.Remote('http://'+appium_server.strip()+'/wd/hub',capabilities)
        time.sleep(1)
        
    def tearDown(self):
        os_platform=platform.system()
        if os_platform=='Windows' :
            filename = os.getcwd() + "\\failure_captures\\"+ self._testMethodName + ".png"
        else :
            filename = os.getcwd() + "/failure_captures/"+ self._testMethodName + ".png"
         
        for method, error in self._outcome.errors:
            if error:
                try:
                    self.driver.save_screenshot(filename)
                except:
                    print("Exception in save_screenshot")
        try:
            if self.test=='android_web' or self.test=='ios_web' :
                self.driver.close()
                time.sleep(2)
            self.driver.quit()
        except:
            pass
        if UtillityMethods.asert_failure_count>0:
            self.fail('Verification check point failed')