'''
Created on Mar 23, 2017

@author: Prabhakaran

'''

class AppiumCapabilities(object):
    
    def Capabilities(self,test,device_id,device_version,device_name=None):
        
        if test.strip()=='android_app' :
            ANDROID_APP={
                'automationName': 'Appium',
                'platformName':'Android',
                'platformVersion':device_version,
                'deviceName':device_id,
                'appPackage':'com.ibi.android.mobilefaves',
                'appActivity':'com.ibi.android.mobilefaves.MainActivity',
                'newCommandTimeout':200,
                'noReset':True
                }
            return ANDROID_APP
        
        elif test.strip()=='android_web' :
            ANDROID_WEB={
                'automationName': 'Appium',
                'platformName':'Android',
                'platformVersion':device_version,
                'deviceName':device_id,
                'browserName':'Chrome',
                'newCommandTimeout':200
                }
            return ANDROID_WEB
        
        elif test.strip()=='ios_web' :
            iOS_WEB={
               'appium-version':'1.7.1',
               'automationName':'XCUITest',
               'platformName':'iOS',
               'platformVersion':device_version,
               'deviceName':device_name,
               'udid':device_id,
               'browserName':'Safari',
               "startIWDP": True,
               'autoAcceptAlerts':True,
               'newCommandTimeout':200,
               'noReset':False,
               'useNewWDA':False
               }
            return iOS_WEB
        else :
            pass
    
    
    
