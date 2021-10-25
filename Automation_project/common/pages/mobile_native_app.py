 
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction
from common.locators.mobile_native_locators import Android_App_Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.lib import mobile_utillity
from PIL import Image
import time,io,os,platform
from datetime import datetime

class Mobile_Faves(object):
 
    def __init__(self, driver):
         
        self.driver=driver
        self.shortwait = WebDriverWait(self.driver, 50)
        self.mediumwait = WebDriverWait(self.driver, 100)
        self.longwait = WebDriverWait(self.driver, 150)
    
    def wait_for_element(self,element,wait_method):
        '''
        Params : element=element
        params : wait_method= 0 (short time wait )
        params : wait_method= 1 (medium time wait ) 
        params : wait_method= 2 (long time wait )
        usage : wait_for_element(element,0) 
        usage : wait_for_element(element,2) 
        '''
        if wait_method==0 :
            self.shortwait.until(EC.visibility_of_element_located(element))
        elif wait_method==1 :
            self.mediumwait.until(EC.visibility_of_element_located(element))
        else :
            self.longwait.until(EC.visibility_of_element_located(element))
            
    def android_reset_and_invoke_app(self):
         
        """
        This function need to call when new Mobile faves app downloaded and invoke first time
        Usage:android_invoke_new_downloaded_app()
        @author: Prabhakaran 
        """
        self.driver.reset()
        time.sleep(5)
        done_button=(By.ID,"com.ibi.android.mobilefaves:id/done_button")
        utiliobj=mobile_utillity.UtillityMethods(self.driver)
        self.wait_for_element(done_button,1)
        self.driver.find_element(*Android_App_Locators.done_button).click()
        time.sleep(2)
        server_title=utiliobj.parseinitfile('nodeid')
        hostname=utiliobj.parseinitfile('nodeid')
        port=utiliobj.parseinitfile('httpport')
        alias=utiliobj.parseinitfile('alias')
        if port=='8080' :
            username=utiliobj.parseinitfile('mrid')
            password=utiliobj.parseinitfile('mrpass')
        else :
            username=utiliobj.parseinitfile('mrid01')
            password=utiliobj.parseinitfile('mrpass01')
        self.android_add_new_server(server_title,alias,hostname,port,username,password)
        time.sleep(3)
        self.android_edit_server(server_title,server_alias=alias,server_port=port)
        self.android_change_settings('Skip server list','off')
        
    def android_add_new_server(self,server_title,server_alias,hostname,port,username,password,https=False):
         
        """
            Usage:android_add_new_server('wfinst02','ibi_apps','wfinst02','8080','admin','admin',True)
            @author: Prabhakaran 
        """  
        driver=self.driver
        driver.find_element(*Android_App_Locators.add_servr).click()
        element=(By.XPATH,"//android.widget.TextView[@text='Add Server']")
        self.wait_for_element(element,1)
        if https==True :
            driver.find_element(*Android_App_Locators.https).click()
        driver.find_element(*Android_App_Locators.server_title).send_keys(server_title.strip())
        driver.find_element(*Android_App_Locators.host_name).send_keys(hostname.strip())
        driver.find_element(*Android_App_Locators.user_name).send_keys(username.strip())
        driver.find_element(*Android_App_Locators.password).send_keys(password.strip())
        driver.find_element(*Android_App_Locators.server_save).click()
        time.sleep(2)
    
    def android_edit_server(self,server_node,**kwargs):
        
        servernode=self.android_scroll_and_select_item(server_node, return_element=True)
        self.android_long_press_and_select_menu(servernode,'Edit')
        
        if 'server_alias' in kwargs :
            alias=self.driver.find_element(*Android_App_Locators.server_alias)
            alias.clear()
            alias.send_keys(kwargs['server_alias'].strip())
        if 'server_port' in kwargs :
            port=self.driver.find_element(*Android_App_Locators.server_port)
            port.clear()
            port.send_keys(kwargs['server_port'].strip())
        
        self.driver.find_element(*Android_App_Locators.server_save).click()

    def android_select_or_verify_welcomepage(self,**kwargs):
            
        """
            params:select_menu='done_button' or 'visit_our_site'
            params:verify='About','Privacy'
            params:msg='Verify X step'
            Usage:select_or_verify_welcomepage(select_menu='done_button',verify='About',msg='Step x :Verify About page')
            Usage:select_or_verify_welcomepage(select_menu='done_button')
            @author: Prabhakaran 
        """  
        if 'select_menu' in kwargs :
            button_name=kwargs['select_menu'].strip()
            select_menu=self.driver.find_element(*Android_App_Locators.__dict__[button_name])
            select_menu.click()
    
    def android_long_press_and_select_menu(self,element,select_menu):
        
        touch=TouchAction(self.driver)
        touch.long_press(element).perform()
        get_menus=self.driver.find_elements_by_class_name("android.widget.TextView")
        menu_iteams=[iteam.text.strip() for iteam in get_menus]
        menu=get_menus[menu_iteams.index(select_menu)]
        menu.click()
                 
    def android_select_fex_file(self,**kwarg):
        """
            params:server_node='wfinst02'
            params:folder='S7072
            params:fex='act-703a'
            param:grid_view=True (If grid view is enabled in setting option) else grid_view=False
            Usage1:android_select_fex_file('wfinst02','S7072','act-703a',grid_view=False)
            Usage2:android_select_fex_file('wfinst02','S7072','act-703a')
            Usage3:android_select_fex_file('wfinst02','act-703a') if server node contains only one folder then pass fex name only
            Usage4:android_select_fex_file('wfinst02','S7072') if server node contains more than one folder and only one fex then pass folder name only
            @author: Prabhakaran 
        """ 
        if 'server_node' in kwarg :
            self.android_scroll_and_select_item(kwarg['server_node'])
            wait_for_element=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/action_bar_title' and @text='"+kwarg['server_node']+"']")
            self.wait_for_element(wait_for_element,1)
        
        if 'folder' in kwarg :    
            grid_view=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/gridview")
            if len(grid_view)>0 :
                self.android_scroll_and_select_item(kwarg['folder'])
            else :
                self.android_scroll_and_select_item(kwarg['folder'])
        if 'fex' in kwarg :
            grid_view=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/gridview")
            if len(grid_view)>0 :
                self.android_scroll_and_select_item(kwarg['fex'])
                
            else :
                self.android_scroll_and_select_item(kwarg['fex'])
                
    def android_select_saved_report(self,**kwargs):
        '''
        params : folder='S7201'
        params : fex='act-001'
        params : saved_report='saved_act_001'
        usage  : android_select_saved_report(folder='S7201',fex='act-001',saved_report='saved_act_001')
        usage  : android_select_saved_report(fex='act-001',saved_report='saved_act_001') 
        '''
        
        if 'folder' in kwargs :
            grid_view=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/gridview")
            if len(grid_view)>0 :
                self.android_scroll_and_select_item(kwargs['folder'],return_element=True)
                folders=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/grid_item_text")
                grid_items=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/GridItem")
                folder_names=[name.text for name in folders]
                grid_items[folder_names.index(kwargs['folder'])].find_element_by_id("com.ibi.android.mobilefaves:id/grid_item_count").click()
            else :
#                 self.android_scroll_and_select_item(kwargs['folder'], grid_view=False,return_element=True)
#                 folders=self.driver.find_element_by_id("com.ibi.android.mobilefaves:id/itemTitle")
#                 list_items=self.driver.find_element_by_id("")      
                pass
            
        if 'fex' in kwargs :
            grid_view=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/gridview")
            if len(grid_view)>0 :
                self.android_scroll_and_select_item(kwargs['fex'],return_element=True)
                fexs=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/grid_item_text")
                grid_items=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/GridItem")
                fex_names=[name.text for name in fexs]
                grid_items[fex_names.index(kwargs['fex'])].find_element_by_id("com.ibi.android.mobilefaves:id/grid_item_count").click()
            else :
                self.android_scroll_and_select_item(kwargs['fex'],return_element=True)
                fexs=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/itemTitle")
                list_views=self.driver.find_elements_by_xpath("//android.widget.ListView[@resource-id='android:id/list']//android.widget.LinearLayout")
                fex_names=[name.text for name in fexs]
                list_views[fex_names.index(kwargs['fex'])].find_element_by_id("com.ibi.android.mobilefaves:id/button").click() 
                       
        if 'saved_report' in kwargs :
            grid_view=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/gridview")
            if len(grid_view)>0 :
                self.android_scroll_and_select_item(kwargs['saved_report'])
            else :
                self.android_scroll_and_select_item(kwargs['saved_report'])
            
    def android_select_more_option(self,option):
        """
            params:option='Save' or 'Email'
            Usage:android_select_or_verify_moreoptions('Email')
            @author: Prabhakaran 
        """
        more_options=self.driver.find_element(*Android_App_Locators.more_option)
        more_options.click()
        time.sleep(2)
        options=self.driver.find_elements_by_id("android:id/title")
        option_list=[item.text.strip() for item in options]
        options[option_list.index(option)].click()
        time.sleep(1)
    
    def android_verify_more_options_enable(self,options,expected_enable_values,msg):
        
        self.driver.find_element(*Android_App_Locators.more_option).click()
        more_options=self.driver.find_elements_by_id("android:id/title")
        LinearLayout=self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        actual_enable_values=[]
        option_list=[item.text.strip() for item in more_options]
        for i in range(len(options)) :
            if options[i] in option_list :
                enable_value=LinearLayout[option_list.index(options[i])].get_attribute('enabled')
                actual_enable_values.append(enable_value)
        mobile_utillity.UtillityMethods.as_List_equal(self,actual_enable_values,expected_enable_values,msg)
        self.driver.back()
    
    def android_verify_report_preview_card(self,**kwargs):
        
        '''
        params : msg=' Step X : Verify Report preview will appear'
        params : list_view=True (if fex diplayed in list view)
        params : screenshot=True
        usage_1  : android_verify_report_preview_card(msg='Verify Report preview will appear')
        usage_2  : android_verify_report_preview_card(msg='Verify Report preview will appear',list_view=True)
        usage_3  : android_verify_report_preview_card(screenshot=True)
        '''
        if 'list_view' in kwargs :
            list_preview=self.driver.find_element_by_xpath("//android.widget.ListView//android.widget.ImageView[@resource-id='com.ibi.android.mobilefaves:id/itemIcon']")
            display=list_preview.is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True,display,kwargs['msg'])
        else :
            live_report_card=self.driver.find_element_by_xpath("//android.widget.GridView//android.widget.RelativeLayout//android.widget.ImageView[@resource-id='com.ibi.android.mobilefaves:id/grid_item_image']")
            display=live_report_card.is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True,display,kwargs['msg'])
            time.sleep(2)
        if 'screenshot' in kwargs :
            default_preview_image=self.driver.find_element_by_id("com.ibi.android.mobilefaves:id/GridItem")
            self.take_mobile_screenshot(default_preview_image,kwargs['file_name'], kwargs['image_type'])
        
    def android_scroll_and_select_item(self,item_text,**kwargs):
         
        """
            params:item_text='AR-HTML-01' or 'wfinst02'
            Usage:android_scroll_and_select_item('wfinst02'grid_view=False)
            Usage:android_scroll_and_select_item('AR-HTML-02')
            @author: Prabhakaran 
        """  
        grid_view=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/gridview")
        if len(grid_view)>0 : 
            wait_for_grid=(By.ID,"com.ibi.android.mobilefaves:id/gridview")
            self.wait_for_element(wait_for_grid,0)
            grid=self.driver.find_element_by_id('com.ibi.android.mobilefaves:id/gridview')
            scrollable=grid.get_attribute('scrollable')
        else :
            wait_for_list=(By.ID,"android:id/list")
            self.wait_for_element(wait_for_list,0)
            grid=self.driver.find_element_by_id("android:id/list")
            scrollable=grid.get_attribute("scrollable")
        if scrollable=='true' :
            item = self.driver.find_element_by_android_uiautomator( 
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "' 
            + item_text + '")')
            if 'return_element' in kwargs :
                return item
            else :
                item.click()
        else :
            item=self.driver.find_element_by_xpath("//android.widget.TextView[@text='"+item_text+"']")
            if 'return_element' in kwargs :
                return item
            else :
                item.click()
     
    def android_change_settings(self,setting_option,on_or_off):
        
        self.android_select_more_option(option='Settings')
        time.sleep(2)
        settings=self.driver.find_elements_by_xpath("//android.widget.ListView//android.widget.LinearLayout//android.widget.TextView[@resource-id='android:id/title']")
        linear_layout=self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.LinearLayout")
        setting_list=[iteam.text for iteam in settings]
        if 'Skin Color'==setting_option :
            pass
        else :
            check_box=linear_layout[setting_list.index(setting_option)].find_element_by_id("android:id/checkbox")
            verify_setting=check_box.get_attribute('checked')
            if verify_setting=='true' and on_or_off=='on' :
                print(setting_option+" is already On")
            elif verify_setting=='false' and on_or_off=='off' :
                print(setting_option+" is already Off")
            else :
                check_box.click()
        time.sleep(1)
        self.driver.find_element(*Android_App_Locators.setting_apply).click()
        self.driver.find_element(*Android_App_Locators.setting_done).click()
    
    
    def android_verify_settings(self,setting_option,on_or_off,msg):
        
        self.android_select_more_option(option='Settings')
        time.sleep(2)
        settings=self.driver.find_elements_by_xpath("//android.widget.ListView//android.widget.LinearLayout//android.widget.TextView[@resource-id='android:id/title']")
        linear_layout=self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.LinearLayout")
        setting_list=[iteam.text for iteam in settings]
        if 'Skin Color'==setting_option :
            pass
        else :
            check_box=linear_layout[setting_list.index(setting_option)].find_element_by_id("android:id/checkbox")
            actual_condion=check_box.get_attribute('checked')
            expected_condion=('true' if on_or_off=='on' else 'false')
            mobile_utillity.UtillityMethods.asequal(self,actual_condion,expected_condion,msg)
        self.driver.find_element(*Android_App_Locators.setting_done).click()   
    
    def android_back_to_mobile_faves(self):
        '''
        usage : android_back_to_mobile_faves()
        '''
        pass
#         timeout=0
#         while(True) :
#             home=self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='android:id/action_bar_title' and @text='Mobile Faves']")
#             if len(home)==0 :
#                 self.driver.back()
#             else :
#                 print("Navigated to Mobile Faves Home Page")
#                 break
#             timeout+=1
#             if timeout==5:
#                 break
#             time.sleep(1)

    def android_save_report(self,name,comments):
        """
        params:name=Save_act_007
        params:comments='ABC Visualize'
        Usage:android_save_report('Save_act_007,'Visualize')
        @author: Prabhakaran 
        """           
        self.android_select_more_option('Save')
        time.sleep(3)
        report_name=self.driver.find_element(*Android_App_Locators.save_report_name)
        report_name.clear()
        report_name.send_keys(name)
        report_comments=self.driver.find_element(*Android_App_Locators.save_report_comments)
        report_comments.send_keys(comments)
        self.driver.find_element(*Android_App_Locators.save_report_ok).click()
    
    def android_edit_or_delete_saved_report(self,report_name,**kwargs):
        '''
        params : report_name='saved_ahtml001'
        params : Delete=True (if you want to delete the saved report)
        params : Edit=True (if you want to edit the saved report)
        params : name='renamed_saved_ahtml001'
        params : comments='recomments'
        usage_1:android_edit_or_delete_saved_report('saved_hml001',Edit=True,name='renamed_ahmlt001',comments='recomment')
        usage_2:android_edit_or_delete_saved_report('saved_hml001',Delete=True)
        '''
        saved_report=self.android_scroll_and_select_item(report_name, grid_view=True,return_element=True)
        if 'Delete' in kwargs :
            self.android_long_press_and_select_menu(saved_report,'Delete')
        if 'Edit' in kwargs :
            self.android_long_press_and_select_menu(saved_report,'Edit')
            time.sleep(1)
            if 'name' in kwargs :
                report_name=self.driver.find_element(*Android_App_Locators.save_report_name)
                report_name.clear()
                report_name.send_keys(kwargs['name'])
            if 'comments' in kwargs :
                report_comments=self.driver.find_element(*Android_App_Locators.save_report_comments)
                report_comments.clear()
                report_comments.send_keys(kwargs['comments'])
            self.driver.find_element(*Android_App_Locators.save_report_ok).click()
        
    def android_verify_report_count(self,report_title,no_of_count,msg):
        '''
        report_title='ahtml_001' or 'Email channel', or 'wfinst02'
        params : no_of_count=2
        params : msg='Verify no of count reports'
        usage : verify_saved_report_count('ahtml_001',1,'Verify no of count reports')
        Author : Prabhakaran
        '''
        actual_count=None
        grid_view=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/gridview")
        if len(grid_view)>0 :
            self.android_scroll_and_select_item(report_title,return_element=True)
            titles=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/grid_item_text")
            grid_items=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/GridItem")
            title_names=[name.text for name in titles]
            actual_count=grid_items[title_names.index(report_title)].find_element_by_id("com.ibi.android.mobilefaves:id/grid_item_count").text
        else :
            self.android_scroll_and_select_item(report_title,return_element=True)
            titles=self.driver.find_elements_by_id("com.ibi.android.mobilefaves:id/itemTitle")
            list_views=self.driver.find_elements_by_xpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout")
            title_names=[name.text for name in titles]
            actual_count=list_views[title_names.index(report_title)].find_element_by_id("com.ibi.android.mobilefaves:id/unReadReportNum").text 
        mobile_utillity.UtillityMethods.asequal(self,no_of_count,int(actual_count),msg)
    
    def android_verify_alet_message(self,alert_title,alert_mesage,msg):
        """
            params:alert_title='Saving Complete'
            params:alert_message='You have successfully saved the report'
            params:msg='Step X verify alert message'
            Usage:verify_alet_message(''Saving Completed','You have successfully saved the report','Step X verify alert message')
            @author: Prabhakaran 
        """     
        title=self.driver.find_element_by_id("android:id/alertTitle").text
        message=self.driver.find_element_by_id("android:id/message").text
        verify=(alert_title==title and alert_mesage==message)
        mobile_utillity.UtillityMethods.asequal(self,True,verify,msg)
        self.driver.find_element_by_id("android:id/button2").click()
    
    def android_verify_active_report_tooltip(self,element_css,expected_tooltip_value,msg):
        
        tooltip=self.driver.find_element_by_css_selector(element_css)
        tooltip.click()
        time.sleep(2)
        self.driver.switch_to.context("NATIVE_APP")
        actual_tooltip_value=self.driver.find_element_by_id("android:id/message").text
        mobile_utillity.UtillityMethods.asequal(self,actual_tooltip_value,expected_tooltip_value,msg)
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.switch_to.context("WEBVIEW")
    
    def android_email_report(self,email_type,email_id):
        '''
        params : email_type='ALL', or 'Content Only' or 'Screenshot Only'
        params : email_id='example@gmail.com'
        usage  : android_email_report('Content Only','activeteam85@gmail.com')
        Author : Prabhakran
        '''
        self.android_select_more_option('Email')
        time.sleep(1)
        etype=self.driver.find_element_by_xpath("//android.widget.TextView[@text='"+email_type+"']")
        etype.click()
        time.sleep(3)
        gmail=self.driver.find_element_by_xpath("//android.widget.TextView[@text='Gmail']")
        gmail.click()
        to_email=WebDriverWait(self.driver,50).until(EC.visibility_of_element_located((By.ID,"com.google.android.gm:id/to")))
        time.sleep(2)
        to_email.send_keys(email_id.strip())
        send_mail=self.driver.find_element_by_id("com.google.android.gm:id/send")
        send_mail.click()
        time.sleep(30)
    
    def android_open_report_from_gmail(self,report_name,open_with,**kwargs):
        '''
        params : report_name='ahtml_001'
        params : open_with='app' (if you want to open report with mobile faves app else) open_with='browser'
        params : verify=True ( if you want to verify whether report is received and displayed with .html format)
        params : msg='Step X : Verify email has been received and report displays in html'
        usage : android_open_report_from_gmail('ahtml_001','app',verify=True,msg='Step X : Verify report is recived')
        Author : Prabhakaran
        '''
        self.driver.start_activity("com.google.android.gm","com.google.android.gm.ConversationListActivityGmail")
        time.sleep(5)
        self.swipe()
        select_mail=WebDriverWait(self.driver,150).until(EC.visibility_of_element_located((By.XPATH,"//android.view.View[contains(@content-desc,'Unread me, "+report_name+"')]")))
        time.sleep(3)
        select_mail.click()
        WebDriverWait(self.driver,50).until(EC.visibility_of_element_located((By.ID,".html File, "+report_name+".html, Save button, Save to Drive button")))
        time.sleep(3)
        if 'verify' in kwargs :
            open_report=self.driver.find_element_by_id(".html File, "+report_name+".html, Save button, Save to Drive button")
            received_report=open_report.is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True,received_report,kwargs['msg'])
        open_report.click()
        app_list=(By.CLASS_NAME,"com.android.internal.widget.ResolverDrawerLayout")
        self.wait_for_element(app_list,3)
        time.sleep(1)                                               
        if open_with=='app' :
            default_app=self.driver.find_elements_by_xpath("//android.widget.TextView[@text='Open with Mobile Faves' and @resource-id='android:id/title']")
            if len(default_app)>0 :
                self.driver.find_element_by_id("android:id/button_once").click()
            else :
                app=self.driver.find_element_by_xpath("//android.widget.TextView[@text='Mobile Faves' and @resource-id='android:id/text1']")
                app.click()   
        else :
            default_browser=self.driver.find_elements_by_xpath("//android.widget.TextView[@text='Open with Chrome' and @resource-id='android:id/title']")
            if len(default_browser)>0 :
                self.driver.find_element_by_id("android:id/button_once").click()
            else :
                browser=self.driver.find_element_by_xpath("//android.widget.TextView[@text='Chrome' and @resource-id='android:id/text1']")
                browser.click()
        time.sleep(3)
        
    def take_mobile_screenshot(self,element,file_name,image_type='actual'):
        """
            params:elemnt=element1
            params:file_name='C2266365'
            params:image_type='actual' or image_type='base'
            Usage:stake_mobile_screenshot(eleemnt1,'C2266365',image_type='base')
            @author: Prabhakaran 
        """  
        location = element.location
        size = element.size
        IMG=self.driver.get_screenshot_as_png()
        im = Image.open(io.BytesIO(IMG)) # uses PIL library to open image in memory
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom)) # defines crop points
        location_path='actual_images' if image_type=='actual' else 'images'
        os_platform=platform.system()
        if os_platform=='Windows' :
            file_path=os.getcwd() + "\\" + location_path + "\\" + file_name + ".png"
        else :
            file_path=os.getcwd() + "/" + location_path + "/" + file_name + ".png"
        im.save(file_path) 
    
    def take_mobile_monitor_screenshot(self,file_name,image_type='actual'):
        """
            params:file_name='C2266365'
            params:image_type='actual' or image_type='base'
            Usage:stake_mobile_screenshot(eleemnt1,'C2266365',image_type='base')
            @author: Prabhakaran 
        """ 
        try : 
            os_platform=platform.system()
            location_path='actual_images' if image_type=='actual' else 'images'
            if os_platform=='Windows' :
                file_path=os.getcwd() + "\\" + location_path + "\\" + file_name + ".png"
            else :
                file_path=os.getcwd() + "/" + location_path + "/" + file_name + ".png"
            self.driver.save_screenshot(file_path)
        except :
            pass
    
    def verify_date_time_format(self,date_time,format_type,msg):
    
        '''
        params : date_time='Apr/09/17'
        params : fromat_type='%b/%d/%y %H:%M:%S'
        params : msg='Step X :  Verify date time'
        usage : verify_date_time_format('Apr/9/17 11:45:23','%b/%d/%y %H:%M:%S','Step X : Verify date time')
        '''
        validate_dt=None
        try :
            datetime.strptime(date_time,format_type)
            validate_dt=True
        except ValueError:
            validate_dt=False
        mobile_utillity.UtillityMethods.asequal(self,True,validate_dt,msg)
    
    def swipe(self,**kwargs):
        
        '''
        Need to modify
        '''
        size=self.driver.get_window_size()
        start_x=int(size['width'])/2
        start_y=int(size['height'])*0.80
        end_y=int(size['height'])*0.20
        self.driver.swipe(start_x,end_y,start_x,start_y,100)
       
       
         
        
    