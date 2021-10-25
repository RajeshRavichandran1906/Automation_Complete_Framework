
from appium.webdriver.common.mobileby import By

class Android_App_Locators(object):
    
    'Welcome Page'
    done_button=(By.ID,"com.ibi.android.mobilefaves:id/done_button")
    visit_our_page=(By.ID,"com.ibi.android.mobilefaves:id/visit_our_site")
    
    'Home Page' 
    add_servr=(By.ID,"Add Server Button")
    more_option=(By.ID,"More options")
    action_bar=(By.ID,"android:id/action_bar_title")
    
    'Add Server Page'
    https=(By.ID,"com.ibi.android.mobilefaves:id/ServerProtocol")
    server_title=(By.ID,"com.ibi.android.mobilefaves:id/ServerTitle")
    server_alias=(By.ID,"com.ibi.android.mobilefaves:id/ServerAlias")
    host_name=(By.ID,"com.ibi.android.mobilefaves:id/ServerName")
    server_port=(By.ID,"com.ibi.android.mobilefaves:id/ServerPort")
    user_name=(By.ID,"com.ibi.android.mobilefaves:id/Username")
    password=(By.ID,"com.ibi.android.mobilefaves:id/Password")
    server_save=(By.ID,"android:id/button1")
    server_cancel=(By.ID,"android:id/button2")
    
    'Setting Page'
    setting_reset=(By.ID,"com.ibi.android.mobilefaves:id/reset_button")
    setting_apply=(By.ID,"com.ibi.android.mobilefaves:id/apply_button")
    setting_done=(By.ID,"com.ibi.android.mobilefaves:id/done_button")
    
    'Save Report'
    save_report_name=(By.ID,"com.ibi.android.mobilefaves:id/savedReportName")
    save_report_comments=(By.ID,"com.ibi.android.mobilefaves:id/savedReportComments")
    save_report_ok=(By.ID,"android:id/button1")
    save_report_cancel=(By.ID,"android:id/button2")