from common.lib import mobile_utillity
from common.lib.mobile_base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException
import time,re

class Mobile_Active_Miscelaneous(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Mobile_Active_Miscelaneous, self).__init__(driver)
        self.test=mobile_utillity.UtillityMethods.parseinitfile(self,'test')

    def _validate_page(self, driver):
        print("Implement Page Loading wait")
    
    def wait_for_date_set(self,table_id):
        
        '''
        usage : wait_for_date_set('IWindowBodyFTB_0_0')
        Author : Prabhakaran
        '''
        utiliobj=mobile_utillity.UtillityMethods(self.driver)
        table_id_css='#'+table_id
        data_set_table=(By.CSS_SELECTOR,table_id_css)
        utiliobj.wait_for_element(data_set_table,3)
        
    def verify_report_full_screen_mode(self,fullscreen_mode,msg):
        '''
        params : fullscreen_mode=True (if record view in fullscreenmode else False ) 
        usage : verify_report_full_screen_mode(True,'Step X : Verify fullscreen mode')
        '''
        fullscreen=self.driver.find_element_by_css_selector("[id='iosfullscreen'][class='activeMobile']").value_of_css_property('display')
        if fullscreen!='none' :
            mobile_utillity.UtillityMethods.asequal(self,True,fullscreen_mode,msg)
        else :
            mobile_utillity.UtillityMethods.asequal(self,False,fullscreen_mode,msg)
    
    def move_to_and_click(self,element):
        '''
        Syntax: move_to_and_click(element)
        Author : Prabhakaran
        '''
        if element.is_displayed() :
            element.click()
        else :
            test=mobile_utillity.UtillityMethods.parseinitfile(self,'test')
            if test=='android_web' or test=='android_app' :
                action=ActionChains(self.driver)
                action.move_to_element(element).click(element).perform()
            else :
                self.driver.execute_script("arguments[0].click();",element)
                
    def move_to_element(self,element):
        '''
        params :  element = webelement
        usage : move_to_element(element)
        '''
        test=mobile_utillity.UtillityMethods.parseinitfile(self,'test')
        if test=='android_web' or test=='android_app' :
            action=ActionChains(self.driver)
            action.move_to_element(element).perform()
            time.sleep(1)
        else :
            self.driver.execute_script("return arguments[0].scrollIntoView();",element)
                
    def select_menu_items(self, table_id, column_no, parent_menu, *args,**kwargs):
        '''
        params : table_id='IWindowBodyFTS_0_0'
        params : column_no= 4 (Colunm num start with 0)
        params : parent_menu= 'Filter'
        params : 'Condition->Between', 'Values->-966.00','Sales'
        params : Done=True or Back=True (If you want click on Done or Back button)
        usage1 : select_menu_items('IWindowBodyFTS_0_0',4,'Filter','Condition->Omits','Values->-966.00',Done=True)
        usage2 : select_menu_items('IWindowBodyFTS_0_0',4,'Visualize')
        usage3 : select_menu_items('IWindowBodyFTS_0_0','4','Chart','Chart Type->Other->CADTag Cloud','Aggregation->Count','Product')
        Author :'Prabhakaran'
        '''
        column_css="#iosfullscreen #"+table_id+" #TCOL_0_C_"+str(column_no)+"_f"
        column=self.driver.find_element_by_css_selector(column_css)
        self.move_to_and_click(column)
        time.sleep(2)
        menu_elements=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu1o li[class='iosDIVULLI'] span[class='amMenuItem']")
        #menu_items=[item.get_attribute('textContent') for item in menu_elements if bool(re.match(r'(^[a-zA-Z0-9].*)',item.get_attribute('textContent').strip()))]
        menu_items=[item.get_attribute('textContent').strip() for item in menu_elements]
        menu_item=menu_elements[menu_items.index(parent_menu)]
        self.move_to_and_click(menu_item)
        time.sleep(2)
        for i in range(len(args)) :
            menus=args[i].split('->')
            sub_elemnts=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu2o li[class='iosDIVULLI'] span[class='amMenuItem']")
            sub_elemnts=[reelement for reelement in sub_elemnts if reelement.get_attribute('textContent')!='>']
            sub_items=[item.get_attribute('textContent').strip() for item in sub_elemnts if item.get_attribute('textContent')!='>']
            sub_menu=sub_elemnts[sub_items.index(menus[0])]
            if len(menus)==1 :
                self.move_to_and_click(sub_menu)
                time.sleep(2)
            if len(menus)==2 :
                elemnts=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu2o li[class='iosDIVULLI']")
                drop_down=Select(elemnts[sub_items.index(menus[0])].find_element_by_css_selector("select"))
                drop_down.select_by_visible_text(menus[1])
                time.sleep(2)
            if len(menus)==3 :
                self.move_to_and_click(sub_menu)
                sub_elements1=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu3o li[class='iosDIVULLI'] span[class='amMenuItem']")
                sub_items1=[item.get_attribute('textContent').strip() for item in sub_elements1]
                sub_elements1[sub_items1.index(menus[1])].click()
                time.sleep(5)
                sub_elements2=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu4o div[id^='chticonp']")
                sub_items2=[item.get_attribute('textContent').strip() for item in sub_elements2]
                sub_ele=sub_elements2[sub_items2.index(menus[2])]
                self.move_to_and_click(sub_ele)
                if 'verify_chart_selection' in kwargs :
                    time.sleep(3)
                    selected_chart=self.driver.find_element_by_css_selector("#iosmenu2o span[id^='mychartname']").text.strip()
                    mobile_utillity.UtillityMethods.asequal(self,selected_chart,kwargs['verify_chart_selection'],'Step x : Verify '+menus[2]+' is selected')
                time.sleep(2)
        if 'Done' in kwargs :
            done=self.driver.find_element_by_css_selector("#iosmenu1 #iosmenu2o div[onclick*='doCreate']")
            done.click()
        if 'Back' in kwargs :
            back=self.driver.find_element_by_css_selector("#iosmenu1 #iosmenu2o div[onclick*='hideSub']")
            back.click()
                    
    def verify_page_summary(self, page_num, expected_title, msg):
        '''
        Syntax: verify_page_summary(0,'107of107records,Page1of2', 'Step 05: Verify Title')
        Syntax: verify_report_summary(0, 'SUB/TOT\n1of107records,Page1of1', 'Step 04: Verify Pagination shows: SUB/TOT')
        Author: Niranjan
        '''
        get_title=self.driver.find_element_by_css_selector("#iosfullscreen .arGridBar table").text
        actual_title=re.sub(r' ', '', get_title)
        if '\n' in actual_title:
            actual_title=re.sub(r' ', '', actual_title)
        #print(actual_title)
        mobile_utillity.UtillityMethods.asin(self,expected_title, actual_title, msg)
    
    def verify_report_page_summary(self, parent_id, expected_title, msg):
        '''
        parent_id='iosfullscreentop'
        Syntax: verify_page_summary('iosfullscreentop','107of107records,Page1of2', 'Step 05: Verify Title')
        Syntax: verify_report_summary('IWindowBody0', 'SUB/TOT\n1of107records,Page1of1', 'Step 04: Verify Pagination shows: SUB/TOT')
        Author: Prabhakaran
        '''
        parent_css='#'+parent_id+' .arGridBar table'
        get_title=self.driver.find_element_by_css_selector(parent_css).text
        actual_title=re.sub(r' ', '', get_title)
        if '\n' in actual_title:
            actual_title=re.sub(r' ', '', actual_title)
        mobile_utillity.UtillityMethods.asin(self,expected_title, actual_title, msg)
        
    def verify_visualization(self, table_id, tr_id, colnum, color_code, msg,**kwargs):
        '''
        Syntax: verify_visualization('ITableData0', 'I0r', 5, 'green', 'Step 05: Verify visualization added')
        Syntax: verify_visualization('ITableData0', 'I0r', 5, 'green', 'Step 05: Verify visualization removed',visualization_removed=True)
        param : kwargs=visualization_removed=True (if you want to verify visualization bar removed from report)
        column number starts with 0
        '''
        expected_color_code=mobile_utillity.UtillityMethods.color_picker(self,color_code, 'rgba')
        occurence = 0
        total_rows=self.driver.find_elements_by_css_selector("[id='{0}'] tr[id ^='{1}']".format(table_id, tr_id))
        if 'visualization_removed' in kwargs :
            for i in range(0, len(total_rows)):
                no_of_visualization=self.driver.find_elements_by_css_selector("[id=" + table_id + "] tr[id ^= '" + tr_id + str(i) +"'] > td:nth-child(" + str(colnum+2) + ") > table table td")
                if len(no_of_visualization)==0:
                    occurence=0
                else :
                    occurence = occurence + 1
                    break 
            mobile_utillity.UtillityMethods.asequal(self,0,occurence, msg)
        else :
            for i in range(0, len(total_rows)):
                actual_color_code=self.driver.find_element_by_css_selector("[id=" + table_id + "] tr[id ^= '" + tr_id + str(i) +"'] > td:nth-child(" + str(colnum+2) + ") > table table td").value_of_css_property('background-color')
                reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', actual_color_code)
                bg_color=reobj.group(1)
                if bg_color in expected_color_code:
                    occurence = occurence + 1 
                else:
                    break
            mobile_utillity.UtillityMethods.asequal(self, len(total_rows), occurence, msg)

    def verify_column_heading(self, table_id, expected_list, msg):

        """
        Params: table_id='ITableData0'
        Params: column=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        Syntax: verify_column_heading(table_id, expected_list,'Step 02: Verify column heading')
        Author: Sindhuja
        """
        column_heading_css = "#" + table_id + " .arGridColumnHeading > td"
        columns=self.driver.find_elements_by_css_selector(column_heading_css)
        actual_list=[re.sub('\s+', ' ', el.strip()) for el in [el1.get_attribute('textContent').strip() for el1 in columns]]
        mobile_utillity.UtillityMethods.asequal(self, expected_list, actual_list, msg)
     
    def verify_mobile_alert_tool_tip(self,element_css,expect_tooltip_value,msg):
        
        '''
        params: element_css='div[title='0 = 1 (20%)'][onclick="alert('0 = 1 (20%)')"]'
        params: tooltips_value='0 = 1 (20%)'
        params: msg='Step X " Verify tooltip value'
        usgae : verify_mobile_alert_tool_tip('div[title='0 = 1 (20%)'][onclick="alert('0 = 1 (20%)')"]','0 = 1 (20%)','Step X " Verify tooltip value')
        '''
        tooltip=self.driver.find_element_by_css_selector(element_css)
        tooltip.click()
        time.sleep(2)
        alert=self.driver.switch_to_alert()
        actual_tooltip_value=alert.text
        mobile_utillity.UtillityMethods.asequal(self,actual_tooltip_value,expect_tooltip_value,msg)
        alert.accept()    
    
    def verify_number_of_pie_riser(self, parent_id,expected_risers, msg):
        """
        parent_id: '#iosTabs0_f'
        expected_number: no of expected riser (10). 
        syntax : verify_number_of_pie_riser('MAINTABLE_wbody2', 10, 'Step 10: Verify number of pie chart segments displayed')
        @author: Prabhakaran
        """
        parent="#" + parent_id + " svg.rootPanel>g.chartPanel"
        actual_risers=len(self.driver.find_elements_by_css_selector(parent + " >g>g>g>path[class^='riser']"))
        mobile_utillity.UtillityMethods.asequal(self, expected_risers, actual_risers, msg)    
    
    def verify_riser_legends(self, parent_id, expected_legend_list, msg,**kwargs):
        """
        parent_id: 'iosTabs0_f'
        params: expected_legend_list=['Coffee','Food']        
        Syntax: verify_riser_pie_labels_and_legends('iosTabs0_f', ['Coffee','Food'],"Step 04: Verify Chart Legend")
        @author: Prabhakaran
        """
        legend_css="#" + parent_id + " .legend text"
        legend=self.driver.find_elements_by_css_selector(legend_css)
        actual_legend_list=[leg.text.strip() for leg in legend]
        #print(actual_legend_list)
        mobile_utillity.UtillityMethods.asequal(self,actual_legend_list,expected_legend_list,msg)
        dock_css="#"+parent_id+" .legend path[class='legend-dock-close']"
        legend_dock_close=self.driver.find_element_by_css_selector(dock_css).is_displayed()
        mobile_utillity.UtillityMethods.asequal(self,True,legend_dock_close,'Step X : Verify legend dock close icon displays')
        
    def verify_report_view(self,view,msg):
        '''
        params : view='full'
        usage 1 : verify_report_view('full','Step 01 :verify report displayed in fullscreen view')
        usage 2 : verify_report_view('original','Step 01 :verify report displayed in original view')
        '''
        full_view_css="#iosfullscreen .arGridBar span[title='Original View'] img"
        original_view_css="table[id='IWindowBody0'] .arGridBar span[title='Fullscreen'] img"
        full_view=self.driver.find_element_by_css_selector(full_view_css)
        original_view=self.driver.find_element_by_css_selector(original_view_css)
        if view=='full' :
            time.sleep(1)
            if full_view.is_displayed()==True and original_view.is_displayed()==False :
                status=True
            else :
                status=False
            mobile_utillity.UtillityMethods.asequal(self,True,status,msg)
        else :
            self.move_to_element(original_view)
            time.sleep(1)
            if full_view.is_displayed()==False and original_view.is_displayed()==True :
                status=True
            else :
                status=False
            mobile_utillity.UtillityMethods.asequal(self,True,status,msg)
    
    def verify_mobile_favorites_displayed(self,msg):
        '''
        usage : verify_mobile_favorites_displayed(msg)
        '''
        element_css="div[data-role='collapsible-set']>div[data-role='collapsible']"
        element=(By.CSS_SELECTOR,element_css)
        mobile_utillity.UtillityMethods.wait_for_element(self, element,0)
        time.sleep(1)
        mobile_fave_list=self.driver.find_element_by_css_selector(element_css)
        mobile_utillity.UtillityMethods.asequal(self,True,mobile_fave_list.is_displayed(),msg)
        
    def verify_menu_items(self, table_id, column_no,navigate_pattern,expected_menu_list,msg):
        '''
        params : table_id='IWindowBodyFTS_0_0'
        params : column_no= 4 (Colunm num start with 0)
        params : navigate_pattern='Chart->Chart Type' ( navigate_pattern=None when no need to verify submenus)
        params : expcted_menu_list :['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        usage : active_misce.verify_menu_items('IWindowBodyFTS_0_0',3,'Calculate',expected_menu_list2,'Step 03 : Verify non numeric columns Calculate menu options are displaying')
        Author :'Prabhakaran'
        '''
        column_css="#iosfullscreen #"+table_id+" #TCOL_0_C_"+str(column_no)+"_f"
        column=self.driver.find_element_by_css_selector(column_css)
        self.move_to_and_click(column)
        time.sleep(1)
        menu_elements=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu1o li[class='iosDIVULLI'] span[class='amMenuItem']")
        menu_items=[item.get_attribute('textContent').strip() for item in menu_elements]
        actual_menu_list=[item.get_attribute('textContent').strip() for item in menu_elements if bool(re.match(r'(^[a-zA-Z0-9].*)',item.get_attribute('textContent').strip()))]
        if navigate_pattern==None :
            mobile_utillity.UtillityMethods.asequal(self,actual_menu_list,expected_menu_list,msg)
        else :
            menus=navigate_pattern.split('->')
            self.move_to_and_click(menu_elements[menu_items.index(menus[0])])
            time.sleep(1)
            actual_submenu_list=None
            for i in range(len(menus)) :
                if i!=2 :
                    submenu_css="#iosmenu1 #iosmenu"+str(i+2)+"o li[class='iosDIVULLI'] span[class='amMenuItem']"
                else :
                    submenu_css="#iosmenu1 #iosmenu"+str(i+2)+"o div[id^='chticonp']"
                    time.sleep(3)
                sub_menu_elements=self.driver.find_elements_by_css_selector(submenu_css)
                sub_menu_elements=[filter_elements for filter_elements in sub_menu_elements if filter_elements.get_attribute('textContent')!='>']
                actual_submenu_list=[items.get_attribute('textContent').strip() for items in sub_menu_elements]
                if len(menus)!=i+1 :
                    sub_menu_elements[actual_submenu_list.index(menus[i+1])].click()
                    time.sleep(2)
            mobile_utillity.UtillityMethods.asequal(self,actual_submenu_list,expected_menu_list,msg)
            for j in range(len(menus),0,-1) :
                backmenu_css="#iosmenu"+str(j+1)+"o div[onclick^='ibi_iPadMenu.hide']"
                self.driver.find_element_by_css_selector(backmenu_css).click()
                time.sleep(1)
        cancel=self.driver.find_element_by_css_selector("#iosmenu2 div[onclick='ibi_iPadMenu.hideMain()']")
        cancel.click()    
    
    def verify_report_dropdown_menu_values(self,table_id,column_no,parent_menu,submenu_nagavigator,expected_values,msg,verify_default_value=None):
        '''
        params : table_id='IWindowBodyFTS_0_0'
        params : column_no= 4 (Colunm num start with 0)
        params : parent_menu=Rollup
        params : navigate_pattern = 'Chart->Chart Type'
        params : expected_values=['Sum','Avg','Min','Max'], expected_values='Sum' (When verify_default_value=True)
        params : verify_default_value=True (When you want to verify default value only) 
        usage1 : active_misce.verify_report_dropdown_menu_values('IWindowBodyFTS_0_0', 0, 'Rollup', 'Aggregation','Count','Step 03 : Verify for non numeric columns by defulat Rollup values are displaying aggregation value as count.',True)
        usage2 : active_misce.verify_report_dropdown_menu_values('IWindowBodyFTS_0_0', 4, 'Rollup', 'Aggregation',['Sum','Avg','Min','Max','Count','Distinct'],'Step 02 : Verify dropdowm values')
        '''
        column_css="#iosfullscreen #"+table_id+" #TCOL_0_C_"+str(column_no)+"_f"
        column=self.driver.find_element_by_css_selector(column_css)
        self.move_to_and_click(column)
        parent_menu_elements=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu1o li[class='iosDIVULLI'] span[class='amMenuItem']")
        parent_menu_items=[item.get_attribute('textContent').strip() for item in parent_menu_elements]
        menu=parent_menu_elements[parent_menu_items.index(parent_menu)]
        self.move_to_and_click(menu)
        time.sleep(2)
        sub_menus=submenu_nagavigator.split('->')
        if len(sub_menus)==1 :
            sub_elemnts=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu2o li[class='iosDIVULLI'] span[class='amMenuItem']")
            sub_elemnts=[reelement for reelement in sub_elemnts if reelement.get_attribute('textContent')!='>']
            sub_items=[item.get_attribute('textContent').strip() for item in sub_elemnts if item.get_attribute('textContent')!='>']
            elemnts=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu2o li[class='iosDIVULLI']")
            drop_down=Select(elemnts[sub_items.index(sub_menus[0])].find_element_by_css_selector("select"))
            if verify_default_value==None :
                actual_vlaues=[value.text for value in drop_down.options]
            else :
                actual_vlaues=drop_down.first_selected_option.text
            
            mobile_utillity.UtillityMethods.asequal(self,actual_vlaues,expected_values,msg)
            self.driver.find_element_by_css_selector("#iosmenu1 #iosmenu2o div[onclick*='hideSub']").click()
            time.sleep(1)
            
        self.driver.find_element_by_css_selector("#iosmenu2 div[onclick='ibi_iPadMenu.hideMain()']").click()   
          
    def verify_report_dropdown_menu_items(self,table_id,column_no,parent_menu,submenu_nagavigator,expected_values,msg,**kwargs):
        '''
        params : table_id='IWindowBodyFTS_0_0'
        params : column_no= 4 (Colunm num start with 0)
        params : parent_menu=Rollup
        params : navigate_pattern = 'Chart->Chart Type'
        params : expected_values=['Sum','Avg','Min','Max'], expected_values='Sum' (When verify_default_value=True)
        params : verify_default_value=True (When you want to verify default value only) 
        usage1 : active_misce.verify_report_dropdown_menu_items('IWindowBodyFTS_0_0',5,'Pivot (Cross Tab)','Aggregation',['Sum','Avg','Min','Max','Count','Distinct'],'Step 02.1 : Verify Expect to see the following Pivot(Cross Tab) menu',verify_default_item='Sum')
        usage2 : active_misce.verify_report_dropdown_menu_items('IWindowBodyFTS_0_0', 4, 'Rollup', 'Aggregation',['Sum','Avg','Min','Max','Count','Distinct'],'Step 02 : Verify dropdowm values')
        '''
        column_css="#iosfullscreen #"+table_id+" #TCOL_0_C_"+str(column_no)+"_f"
        column=self.driver.find_element_by_css_selector(column_css)
        self.move_to_and_click(column)
        parent_menu_elements=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu1o li[class='iosDIVULLI'] span[class='amMenuItem']")
        parent_menu_items=[item.get_attribute('textContent').strip() for item in parent_menu_elements]
        menu=parent_menu_elements[parent_menu_items.index(parent_menu)]
        self.move_to_and_click(menu)
        time.sleep(2)
        sub_menus=submenu_nagavigator.split('->')
        if len(sub_menus)==1 :
            sub_elemnts=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu2o li[class='iosDIVULLI'] span[class='amMenuItem']")
            sub_elemnts=[reelement for reelement in sub_elemnts if reelement.get_attribute('textContent')!='>']
            sub_items=[item.get_attribute('textContent').strip() for item in sub_elemnts if item.get_attribute('textContent')!='>']
            elemnts=self.driver.find_elements_by_css_selector("#iosmenu1 #iosmenu2o li[class='iosDIVULLI']")
            drop_down=Select(elemnts[sub_items.index(sub_menus[0])].find_element_by_css_selector("select"))
            if 'verify_default_item' in kwargs:
                default_value=drop_down.first_selected_option.text
                mobile_utillity.UtillityMethods.asequal(self,default_value,kwargs['verify_default_item'],'Step 0X.0 : Verify default selected value is '+kwargs['verify_default_item'])
            actual_vlaues=[value.text for value in drop_down.options]
            #print(actual_vlaues)
            mobile_utillity.UtillityMethods.asequal(self,actual_vlaues,expected_values,msg)
            self.driver.find_element_by_css_selector("#iosmenu1 #iosmenu2o div[onclick*='hideSub']").click()
            time.sleep(1)
        self.driver.find_element_by_css_selector("#iosmenu2 div[onclick='ibi_iPadMenu.hideMain()']").click()   
    
    def verify_tabbed_report(self,parent_id,expected_tab_list,msg):
        '''
        params : parent_id='iosfullscreentab' or 'MAINTABLE_wmenu0'
        params : expected_tab_list =['Report', 'Chart']
        usage : verify_tabbed_report('iosfullscreentab',['Report', 'Chart'],'Step x : verify report tab titles')
        '''
        time.sleep(5)
        tab_css="#"+parent_id+" [id^='tab_']"
        report_tabs=self.driver.find_elements_by_css_selector(tab_css)
        actual_tab_list=[title.text.strip() for title in report_tabs]
        mobile_utillity.UtillityMethods.asequal(self,expected_tab_list,actual_tab_list,msg)
    
    def navigate_tabs(self,tab_index,original_view=False):
        """
        :params: tab_index=0 or 1...
        :params: original_view=True (When report id displaying in original view)
        :usage: navigate_tabs(0)
        :usage: navigate_tabs(0,original_view=True)
        """
        if original_view==True :
            tab_css="[id^='MAINTABLE_wmenu'] > table > tbody > tr > td[id^='tab'] [onclick*='selectTab']"
        else :
            tab_css="[id^='iosfullscreentab'] > table > tbody > tr > td[id^='tab'] [onclick*='selectTab']"
        time.sleep(1)
        tab=self.driver.find_elements_by_css_selector(tab_css)
        tab[tab_index].click()
        time.sleep(2)
        
    def close_tabbed_report(self,tab_index,original_view=False):
        """
        :params: tab_index=0 or 1...
        :params: original_view=True (When report id displaying in original view)
        :usage: close_tabbed_report(0)
        :usage: close_tabbed_report(0,original_view=True)
        """
        if original_view==True :
            tab_css="[id='MAINTABLE_wmenu0'] td[id='tab_0_"+str(tab_index)+"'] table>tbody>tr>td img"
        else :
            tab_css="[id^='iosfullscreentab'] td[id='tab_0_"+str(tab_index)+"'] table>tbody>tr>td img"
        time.sleep(1)
        tab=self.driver.find_element_by_css_selector(tab_css)
        tab.click()
        time.sleep(2)
        
    def navigate_page(self, navigate_type,original_view=False,*args):
        '''
        Syntax: navigate_page('goto_page', 2)
        Syntax: navigate_page('next_page')
        Syntax: navigate_page('last_page')
        Syntax: navigate_page('previous_page')
        Syntax: navigate_page('first_page')
        Author: Niranjan 
        '''
        if navigate_type == 'goto_page':
            if original_view==False :
                btn_css="#iosfullscreen .arGridBar span[title='Goto Page']"
            else :
                btn_css="table .arGridBar span[title='Goto Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
            page_no=self.driver.find_element_by_id("formgoto")
            page_no.clear()
            page_no.send_keys(args[0])
            page_no.send_keys(Keys.ENTER)
            time.sleep(1)
        if navigate_type == 'next_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='Next Page']"
            else :
                btn_css="table .arGridBar span[title='Next Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
        if navigate_type == 'last_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='Last Page']"
            else :
                btn_css="table .arGridBar span[title='Last Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
        if navigate_type == 'previous_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='Previous Page']"
            else :
                btn_css="table .arGridBar span[title='Previous Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)
        if navigate_type == 'first_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='First Page']"
            else :
                btn_css="table .arGridBar span[title='First Page']"
            self.driver.find_element_by_css_selector(btn_css).click()
            time.sleep(1)    
            
    def verify_navigate_page(self, navigate_type, msg,original_view=False):
        '''
        :param : original_view=False (When report displaying in original view)
        Syntax: verify_navigate_page('goto_page', Step 02: Verify goto Page double arrow displayed")
        Syntax: verify_navigate_page('next_page',"Step 02: Verify next Page double arrow displayed")
        Syntax: verify_navigate_page('last_page',"Step 02: Verify Last Page double arrow displayed")
        Syntax: verify_navigate_page('previous_page',"Step 02: Verify previous_page double arrow displayed")
        Syntax: verify_navigate_page('first_page',"Step 02: Verify first Page double arrow displayed")
        Author: Niranjan
        '''
        if navigate_type == 'goto_page':
            if original_view==False :
                btn_css="#iosfullscreen .arGridBar span[title='Goto Page']"
            else :
                btn_css="table .arGridBar span[title='Goto Page']"
            img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'next_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='Next Page']"
            else :
                btn_css="table .arGridBar span[title='Next Page']"
            img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'last_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='Last Page']"
            else :
                btn_css="table .arGridBar span[title='Last Page']"
            img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'previous_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='Previous Page']"
            else :
                btn_css="table .arGridBar span[title='Previous Page']"
            img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
        if navigate_type == 'first_page':
            if original_view==False :
                btn_css="#iosfullscreen span[title='First Page']"
            else :
                btn_css="table .arGridBar span[title='First Page']"
            img_status=self.driver.find_element_by_css_selector(btn_css).is_displayed()
            mobile_utillity.UtillityMethods.asequal(self,True, img_status, msg)
            time.sleep(1)
            
    def verify_pagination_bar(self,msg,original_view=False):
        '''
        :param : msg='Step X : Verify pagination bar is displaying 
        :param : original_view=True (When report displaying in original view)
        :usage : verify_pagination_bar('Step X : Verify pagination bar is displaying',original_view=True)
        :usage : verify_pagination_bar('Step X : Verify pagination bar is displaying') when report is displaying in fullscreen view
        '''
        if original_view==False :
            pagination_css="[id='#iosfullscreen'] span[title]"
        else :
            pagination_css="table .arGridBar span[title]"
        pagination=self.driver.find_element_by_css_selector(pagination_css)
        if pagination.is_displayed()==False :
            self.move_to_element(pagination)
            time.sleep(2)
        mobile_utillity.UtillityMethods.asequal(self,True,pagination.is_displayed(),msg)
        
    def verify_active_chart_tooltip(self, parent_id, raiser_class, expected_tooltip_list, msg):
        """
        param: parent_id='iosTabs0_f'
        param: raiser_class='riser!s0!g5!mbar!'
        param: expected=['DEALER_COST, ENGLAND: 37,853']
        usage: verify_active_chart_tooltip('iosTabs0_f','riser!s0!g5!mbar!',['DEALER_COST, ENGLAND: 37,853'],'Step 02 : verify') 
        """
        action1 = ActionChains(self.driver)
        move1 = self.driver.find_element_by_css_selector("#"+ parent_id)
        action1.move_to_element_with_offset(move1,1,1).perform()
        time.sleep(5)
        del action1
        action = ActionChains(self.driver)        
        raiser_css="#"+ parent_id + " [class*='" + raiser_class + "']"
        tooltip_css="#"+ parent_id + " span[id*='tdgchart-tooltip'] > div"
        riser=self.driver.find_element_by_css_selector(raiser_css)
        action.move_to_element(riser).perform()
        del action
        time.sleep(2)
        tooltips=self.driver.find_element_by_css_selector(tooltip_css).text.split("\n")
        actual_tooltip_list=[el.strip() for el in tooltips]
        #print(actual_tooltip_list)
        mobile_utillity.UtillityMethods.asequal(self,expected_tooltip_list,actual_tooltip_list,msg)
        time.sleep(1)    
        
    def verify_active_chart_XY_labels(self, parent_id, expected_xval_list, expected_yval_list, msg):
        """
        params:parent_id='iosTabs0_f'
        params: expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...']
        params: expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        Syntax: verify_active_chart_XY_labels('iosTabs0_f', expected_xval_list, expected_yval_list, 'Step <no.>')
        """
        parent="#" + parent_id + " svg > g"
        if expected_xval_list !=[]:
            time.sleep(2)
            x=self.driver.find_elements_by_css_selector(parent + " text[class^='xaxis'][class*='labels']") 
            actual_x_label=[i.text.strip() for i in x]
            #print(actual_x_label)
            mobile_utillity.UtillityMethods.asequal(self,actual_x_label,expected_xval_list,msg+' Verify the x-Axis labels')
        if expected_yval_list !=[]:
            time.sleep(2)  
            y=self.driver.find_elements_by_css_selector(parent + " text[class^='yaxis-labels']") 
            actual_y_label=[l.text.strip() for l in y]
            #print(actual_y_label)
            mobile_utillity.UtillityMethods.asequal(self,actual_y_label,expected_yval_list,msg+' Verify the y-Axis labels')
    
    def verify_active_chart_color(self, parent_id, riser_class, color, msg, **kwargs):
        """
        param: parent_id='iosTabs0_f'
        param: riser_class='riser!s1!g8!mbar!'
        param: color='green' OR 'text-green'(text-green means it will verify only green not the rgb of green)
        param: kwargs = attribute='yes'(if want to verify attribute value for color instead pf css property)
        Syntax:verify_chart_color('iosTabs0_f ', 'riser!s1!g8!mbar!', 'green', 'Step 10: Verify Color')
        Syntax:verify_chart_color('iosTabs0_f ', 'riser!s1!g8!mbar!', 'green', 'Step 10: Verify Color',attribute='yes')
        """   
        attribute_type=kwargs['attribute_type'] if 'attribute_type' in kwargs else "fill"           
        custom_css=kwargs['custom_css'] if 'custom_css' in kwargs else "[class*='" + riser_class + "']"
        raiser_css="#"+ parent_id + " " + custom_css
        if 'attribute' in kwargs:
            temp_obj=((self.driver.find_element_by_css_selector(raiser_css).get_attribute('fill'))[:-10]+")")[4:]
            actual_color = "rgb"+temp_obj
            expected_color=mobile_utillity.UtillityMethods.color_picker(self,color, 'rgb')
        else:
            actual_color = Color.from_string(self.driver.find_element_by_css_selector(raiser_css).value_of_css_property(attribute_type)).rgba
            expected_color=mobile_utillity.UtillityMethods.color_picker(self,color, 'rgba')
        mobile_utillity.UtillityMethods.asequal(self,actual_color, expected_color, msg)        
    
    def verify_xaxis_and_yaxis_title(self,parent_id,expected_x_axis_title,expected_y_axis_title,msg):
        """
        Params: table_id='iosTabs0_f '
        Params: expected_x_axis_title='RCOUNTRY : CAR' or None (if do not want to verify X axis title)
        params: expected_y_axis_title='RCOUNTRY : CAR' or None (if do not want to verify y axis title)
        Syntax: verify_xaxis_title('iosTabs0_f', 'COUNTRY : CAR','COUNTRY : Unit Sales','Step 03: Verify Title')
        Syntax: verify_xaxis_title('iosTabs0_f', 'COUNTRY : CAR',None,'Step 03: Verify Title')
        """
        time.sleep(2)
        if expected_x_axis_title!=None :
            parent_css="#"+parent_id+" text[class^='xaxis'][class$='title']"
            actual_xaxis_title=self.driver.find_element_by_css_selector(parent_css).text.strip()
            mobile_utillity.UtillityMethods.asequal(self,actual_xaxis_title,expected_x_axis_title,msg+' Verify X axis tilte')
        if expected_y_axis_title!=None :
            parent_css="#"+parent_id+" text[class='yaxis-title']"
            actual_yaxis_title=self.driver.find_element_by_css_selector(parent_css).text.strip()
            mobile_utillity.UtillityMethods.asequal(self,actual_yaxis_title,expected_y_axis_title,msg+' Verify Y axis tilte')    
    
    def verify_active_chart_title(self,parent_id,expected_chart_title,msg):
        """
        Params: table_id='iosTabs0_ft'
        Params: expected_title='RETAIL_COST, P6.2 Dcost BY COUNTRY, CAR'
        Syntax: verify_active_chart_title('iosTabs0_ft', 'RETAIL_COST, P6.2 Dcost BY COUNTRY, CAR', 'Step 03: Verify Title')
        @Author: Kiruthika 
        """
        actual_chart_title=self.driver.find_element_by_css_selector("#"+parent_id+" tbody").text.strip()
        mobile_utillity.UtillityMethods.asequal(self,actual_chart_title,expected_chart_title,msg)
     
    def verify_number_of_riser(self, parent_id, expected_risers, msg):
        """
        params : parent_id = 'iosTabs0_f'
        params : expected_risers = 10
        usage : verify_number_of_riser('iosTabs0_f',10,'Step 10 : Verify no of chart risers')
        """
        parent="#" + parent_id + " svg g.risers"
        total_risers=self.driver.find_elements_by_css_selector(parent + " >g>rect[class^='riser']")
        actual_risers=0
        for riser in total_risers :
            if riser.is_displayed() :
                actual_risers=actual_risers+1
        #print(actual_risers)
        mobile_utillity.UtillityMethods.asequal(self, actual_risers, expected_risers, msg)
    
    def verify_active_default_chart_type(self,table_id,column_no,expected_chart_type,msg):
        '''
        params : table_id='IWindowBodyFTS_0_0'
        params : column_no=2 
        params : expected_chart_type='VBar'
        usage : verify_active_default_chart_type('IWindowBodyFTS_0_0',2,'VBar','Step 02 : Verify default chart type')
        '''
        column_css="#iosfullscreen #"+table_id+" #TCOL_0_C_"+str(column_no)+"_f"
        column=self.driver.find_element_by_css_selector(column_css)
        self.move_to_and_click(column)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#iosmenu1 #iosmenu1o div[onclick*='ibi_iPadMenu.ShowChartMenu']").click()
        time.sleep(2)
        default_chart_type=self.driver.find_element_by_css_selector("#iosmenu1 #iosmenu2o div[onclick*='ibi_iPadMenu.ShowChartMenu'] span[id='mychartname_0']").text.strip()
        mobile_utillity.UtillityMethods.asequal(self,default_chart_type,expected_chart_type,msg)   
        self.driver.find_element_by_css_selector("#iosmenu2o div[onclick*='ibi_iPadMenu.hideSub()']").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#iosmenu2 div[onclick='ibi_iPadMenu.hideMain()']").click()
        time.sleep(1)   
    
    def verify_chartToolbar_display(self,parent_id,no_of_toolbar_items,msg,original_view=False):
        '''
        params :parent_id='iosfullscreenbot' or MAINTABLE_wbodyMain0
        params :no_of_toolbar_items=10
        params : original_view=True (If want to verify chart tool bar in original view)
        usage 1: verify_chartToolbar_display('iosfullscreenbot',0,'Step 02 : Verify chart toolbar display in fullscreen view')
        usage 2: verify_chartToolbar_display('MAINTABLE_wbodyMain0',0,'Step 02 : Verify chart toolbar display in original view',original_view=True)
        '''
        if original_view==False :
            toolbar_css="#"+parent_id+" table>tbody>tr>td img"
        else :
            toolbar_css="#"+parent_id+" .arChartMenuBar  table>tbody>tr>td img"
        toolbar=self.driver.find_elements_by_css_selector(toolbar_css)
        count=0
        for item in toolbar :
            if item.is_displayed() :
                count=count+1
        mobile_utillity.UtillityMethods.asequal(self,count,no_of_toolbar_items,msg)
    
    def verify_riser_legends_color(self,parent_id,legend_name_color_name,msg,**kwargs):
        '''
        params : parent_id='iosTabs0_f'
        params : legend_name_color_name=['Coffee->bar_blue','Food->pale_green','Gifts->dark_green']
        params : kwargs = attribute='yes'(if want to verify attribute value for color instead pf css property)
        usage1 : verify_riser_legends_color('iosTabs0_f',['Coffee->bar_blue','Food->pale_green','Gifts->dark_green'],'Step 01.1 : Verify legends color')
        usage1 : verify_riser_legends_color('iosTabs0_f',['Coffee->bar_blue]','Step 01.1 : Verify legends color')
        '''
        legend_text_elements=self.driver.find_elements_by_css_selector("#"+parent_id+" .legend text")
        legends_text=[leg.text.strip() for leg in legend_text_elements]
        legend_marker_elements=self.driver.find_elements_by_css_selector("#"+parent_id+" .legend path[class^='legend-markers!s']")
        result_status=None
        for legend_and_color in legend_name_color_name :
            temp_leg=legend_and_color.split('->')
            legend_name=temp_leg[0]
            legend_color=temp_leg[1]
            legend_marker=legend_marker_elements[legends_text.index(legend_name)]
            if 'attribute' in kwargs:
                temp_obj=((legend_marker.get_attribute('fill'))[:-10]+")")[4:]
                actual_color = "rgb"+temp_obj
                expected_color=mobile_utillity.UtillityMethods.color_picker(self,legend_color, 'rgb')
                if expected_color==actual_color :
                    result_status=True
                else :
                    result_status=False
                    break
            else:
                actual_color = Color.from_string(legend_marker.value_of_css_property("fill")).rgba
                expected_color=mobile_utillity.UtillityMethods.color_picker(self,legend_color, 'rgba')
                if expected_color==actual_color :
                    result_status=True
                else :
                    result_status=False
                    break
        mobile_utillity.UtillityMethods.asequal(self,True,result_status,msg)
    
    def verify_pie_labels(self,parent_id,expected_label_list,msg):
        '''
        params : parent_id='iosTabs0_f' or 'wbody1_f'
        params : expected_label_list['State']
        usage : verify_pie_labels('wbody1_f',['State'],'Step 03.7 : Verify pie chart label in original screen')
        '''
        parent="#" + parent_id + " svg > g"
        actual_label_list=[]        
        labels=self.driver.find_elements_by_css_selector(parent + " text[class^='pieLabel!g']")
        for i in range(0,len(labels)):
            label=self.driver.find_element_by_css_selector(parent + " text[class='pieLabel!g" + str(i) + "!mpieLabel!']").text.strip()
            actual_label_list.append(label)
        mobile_utillity.UtillityMethods.asequal(self,expected_label_list, actual_label_list, msg)
        
    def verify_Chart_Tool_Bar(self,parent_id,expected_list,msg,original_view=False,**kwargs):
        
        '''
        :param : parent_id='iosfullscreenbot' or 'wmenu1'
        :param : exptected_list=['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart','Freeze icon','Aggregation']
        :param : original_view=True (When chart is displaying in original view) else original_view=Fals
        :param : **kwargs=default_aggregaion_text='Count' (Should be pass default aggregaion text when Aggregation is listed in exptected list)
        :usage1: verify_Chart_Tool_Bar('iosfullscreenbot',['More Options','Advanced Chart','Original Chart','Aggregation'],'Step 01 : Verify chart tool bars',default_aggregaion_text='Sum')
        :usage2: verify_Chart_Tool_Bar('MAINTABLE_wmenu0',['More Options','Advanced Chart','Original Chart','Aggregation'],'Step 01 : Verify chart tool bars',original_view=True,default_aggregaion_text='Sum') 
        '''
        
        actual_list=[]
        icons_css="#"+parent_id +" .arChartMenuBar td div[onclick] img" if original_view==True else "#"+parent_id+" table>tbody>tr>td div[onclick] img"
        total_icons=0
        icons=self.driver.find_elements_by_css_selector(icons_css)
        for icon in icons :
            if icon.is_displayed() :
                total_icons=total_icons+1
                
        '-------- More option -----'
        try :
            if original_view==False :
                parent_css="#"+parent_id+" div[id^='cpop'] div[onclick^='ibiMenu.Showmenu'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='More Options'] img"
            more=self.driver.find_element_by_css_selector(parent_css)
            if more.is_displayed() :
                actual_list.append('More Options')
        except : pass 
        
        '------ Bar and Column ------'
        try :
            if original_view==False :   
                bar=self.driver.find_element_by_css_selector("#"+parent_id+" div[title='Bar'] img")
                if bar.is_displayed() :
                    actual_list.append('Bar')
            else :
                column=self.driver.find_element_by_css_selector("#"+parent_id+" div[title='Column'] img")
                if column.is_displayed() :
                    actual_list.append('Column') 
        except :pass
        
        '------- Pie ------------'
        try :
            if original_view==False :
                parent_css="#"+parent_id+" div[title='Pie'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='Pie'] img"
            pie=self.driver.find_element_by_css_selector(parent_css)
            if pie.is_displayed() :
                actual_list.append('Pie')
        except : pass
        
        '------- Line ------'    
        try :
            if original_view==False :
                parent_css="#"+parent_id+" div[title='Line'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='Line'] img"
            line=self.driver.find_element_by_css_selector(parent_css)
            if line.is_displayed() :
                actual_list.append('Line')
        except : pass
        
        '-------  Scatter -----'        
        try :
            if original_view==False :
                parent_css="#"+parent_id+" div[title='Scatter'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='Scatter'] img"
            scatter=self.driver.find_element_by_css_selector(parent_css)
            if scatter.is_displayed() :
                actual_list.append('Scatter')
        except : pass
        
        '-------- Rollup ------'    
        try :
            if original_view==False :
                parent_css="#"+parent_id+" div[title='Rollup'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='Rollup'] img"
            rollup=self.driver.find_element_by_css_selector(parent_css)
            if rollup.is_displayed() :
                actual_list.append('Rollup')
        except : pass
        
        '-------- Advance Chart -----'
        try :        
            if original_view==False :
                parent_css="#"+parent_id+" div[title='Advanced Chart'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='Advanced Chart'] img"
            advchart=self.driver.find_element_by_css_selector(parent_css)
            if advchart.is_displayed() :
                actual_list.append('Advanced Chart')        
        except : pass
        
        '------- Original Chart -----'
        try :
            if original_view==False :
                parent_css="#"+parent_id+" div[title='Original Chart'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='Original Chart'] img"
            original_chart=self.driver.find_element_by_css_selector(parent_css)
            if original_chart.is_displayed() :
                actual_list.append('Original Chart')
        except : pass 
        
        '------ Freeze Icon -----'
        try :
            if original_view==False :
                parent_css="#"+parent_id+" [id^='LINKIMG'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar [id^='LINKIMG'] img"
            freeze_icon=self.driver.find_element_by_css_selector(parent_css)
            if freeze_icon.is_displayed() :
                actual_list.append('Freeze icon')
        except : pass
        
        '------- Aggregation ------'
        try :    
            if original_view==False :
                parent_css="#"+parent_id+" div[id^='SUMFS']>div[onclick^='ibiMenu.Showmenu'] img"
                text_css="#"+parent_id+" div[id^='SUMFS']>div[onclick^='ibiMenu.Showmenu'] td[class^='tabPagingText']"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar [id^='SUM'] [title='Aggregation'] img"
                text_css="#"+parent_id+" .arChartMenuBar [id^='SUM'] td[class^='tabPagingText']"
            aggregation=self.driver.find_element_by_css_selector(parent_css)
            actual_agg_text=self.driver.find_element_by_css_selector(text_css).text.strip()
            exptected_agg_text=exptected_agg_text=kwargs['default_aggregaion_text'] if 'default_aggregaion_text' in kwargs else 'Sum'
            if aggregation.is_displayed()==True and actual_agg_text==exptected_agg_text :
                actual_list.append('Aggregation')
        except : pass
        
        '------------- Remove Filter ---------'
        try :        
            if original_view==False :
                parent_css="#"+parent_id+" div[title='Remove Filter'] img"
            else :
                parent_css="#"+parent_id+" .arChartMenuBar div[title='Remove Filter'] img"
            remove_filter=self.driver.find_element_by_css_selector(parent_css)
            if remove_filter.is_displayed() :
                actual_list.append('Remove Filter')        
        except : pass
        
        #print(actual_list)
        
        if 'verify_position' in kwargs :
            if original_view==True :
                postion=self.driver.find_element_by_css_selector("#"+parent_id+" .arChartMenuBar")
                if postion.location['x']==0 and postion.location['y']==0 :
                    status=True
                else :
                    status=False
                mobile_utillity.UtillityMethods.asequal(self,True,status,'Step X : Verify the chart toolbars in the top of the report in original view')
            else :
                postion1=self.driver.find_element_by_css_selector("#"+parent_id+" [id^='iosfullscreenbot']>table")
                if postion1.location['x']==0 and postion1.location['y']!=0 :
                    status1=True
                else :
                    status1=False
                mobile_utillity.UtillityMethods.asequal(self,True,status1,'Step X : Verify the chart toolbars in bottom of the report in fullscreen view')    
        #print(total_icons)
        status=True if actual_list==expected_list and len(actual_list)==total_icons else False
        mobile_utillity.UtillityMethods.asequal(self,True,status,msg)
            
    def verify_line_chart_tooltip(self,parent_id,riser_class,expected_tooltip,msg):
        '''
        :param : parent_id = 'iosTabs0_f' or 'wbody1_f'
        :param : riser_class='marker!s0!g0!mmarker!'
        :param : expected_tooltip=['Unit Sales: 421K', 'X: Biscotti']
        :usage : verify_line_chart_tooltip('iosTabs0_f','marker!s0!g0!mmarker!',['Unit Sales: 421K', 'X: Biscotti'],'Step 02 : Verify Line Chart tooltip')
        '''
        move=self.driver.find_element_by_css_selector("#"+parent_id)
        mobile_utillity.UtillityMethods.move_to_element(self,move, x=1, y=1)
        riser_css='#'+parent_id+" circle[class*='"+riser_class+"']"
        grouppanel_css="#"+parent_id+" .eventPanel>rect[pointer-events='all']"
        group_panel=self.driver.find_element_by_css_selector(grouppanel_css)
        riser_trans=self.driver.find_element_by_css_selector(riser_css).get_attribute('transform')
        riser_location=riser_trans[10:-1]
        riser_offset=riser_location.split(',')
        mobile_utillity.UtillityMethods.move_to_element(self,group_panel,x=float(riser_offset[0]),y=float(riser_offset[1]))
        #time.sleep(2)
        tooltip_css="#"+ parent_id + " span[id='tdgchart-tooltip'] > div"
        tooltips=self.driver.find_element_by_css_selector(tooltip_css).text.split("\n")
        actual_tooltip_list=[el.strip() for el in tooltips]
        mobile_utillity.UtillityMethods.asequal(self,actual_tooltip_list,expected_tooltip,msg)
        time.sleep(1)
        
    def verify_number_of_line_chart_circle(self,parent_id,total_circles,msg):
        
        '''
        :param : parent_id = 'iosTabs0_f' or 'wbody1_f'
        :param : total_circles=10
        :usage : verify_number_of_line_chart_circle('iosTabs0_f',10,'Step 01 : Verify circle')
        '''
        parent_css="#"+parent_id+" .groupPanel circle[class^='marker']"
        total_actual_circles=len(self.driver.find_elements_by_css_selector(parent_css))
        mobile_utillity.UtillityMethods.asequal(self,total_actual_circles,total_circles,msg)
    
    def select_default_tooltip(self,parent_id,raiser_class,menu):
        
        '''
        :param: parent_id='iosTabs0_f' or 'MAINTABLE_wbody0_f'
        :param: raiser_class='riser!s0!g3!mbar!'
        :param: menu='Filter'
        :usage: select_default_tooltip('iosTabs0_f','riser!s0!g3!mbar!','IBI')
        '''
        utiliobj= mobile_utillity.UtillityMethods(self.driver)
        test=utiliobj.parseinitfile('test')
        parent_css="#"+parent_id
        raiser_css=parent_css+" [class*='" + raiser_class + "']"
        tooltip_css=parent_css+" span[id='tdgchart-tooltip']>div>ul>li[class='tdgchart-tooltip-pad'] [onclick]"
        move=self.driver.find_element_by_css_selector(parent_css)
        mobile_utillity.UtillityMethods.move_to_element(self,move,1,1)
        raiser=self.driver.find_element_by_css_selector(raiser_css)
        mobile_utillity.UtillityMethods.move_to_element(self,raiser)
        tooltip=self.driver.find_elements_by_css_selector(tooltip_css)
        tooltip_menus=[item.text.strip() for item in tooltip]
        tooltip_element=tooltip[tooltip_menus.index(menu)]
        if test=='android_web' or test=='android_app' :
            tooltip_element.click()
        else :
            utiliobj.webview_touch_actions(tooltip_element,action='tap')
        time.sleep(2)
    
    def verify_freeze_column_line(self,yes,msg):
        '''
        :param : yes=True (if want check whether freeze_column_line is displayed else yes=False)
        :usage : verify_freeze_column_line(True,'Step 03 : Verify that the report has changed and the report that aligns with the Bodytype field.')
        '''
        freeze_div_css="div[id='ios_div_0_move_0_l'][style*='left: 0px']"
        if yes==True :
            freeze_border_line=self.driver.find_element_by_css_selector(freeze_div_css).value_of_css_property('border-right')
            mobile_utillity.UtillityMethods.asequal(self,'1px solid rgb(0, 0, 0)',freeze_border_line,msg)
        else :
            try :
                freeze_border_line=self.driver.find_element_by_css_selector(freeze_div_css).value_of_css_property('border-right')
                mobile_utillity.UtillityMethods.as_not_equal(self,'1px solid rgb(0, 0, 0)',freeze_border_line,msg)
            except NoSuchElementException :
                mobile_utillity.UtillityMethods.asequal(self,True,True,msg)    
    
    def scroll_freeze_table(self):
        
        before_move_table_0=int(self.driver.find_element_by_css_selector("#ios_div_0_move_0").value_of_css_property('left').strip()[:-2])
        #print(before_move_table_0)
        test=mobile_utillity.UtillityMethods.parseinitfile(self,'test')
        if test=='android_app' or test=='android_web' :
            self.driver.switch_to.context("NATIVE_APP")
            size=self.driver.get_window_size()
            start_x=int(size['width'])-50
            start_y=int(size['height'])/4
            end_x=80
            self.driver.swipe(start_x,start_y,end_x,start_y,100)
            self.driver.switch_to.context("CHROMIUM")
        else :
            self.driver.execute_script('mobile: scroll', {'direction': 'right'});
        time.sleep(5)    
        after_move_table_0=int(self.driver.find_element_by_css_selector("#ios_div_0_move_0").value_of_css_property('left').strip()[:-2])
        freeze_table_left=int(self.driver.find_element_by_css_selector("#ios_div_0_move_0_l").value_of_css_property('left').strip()[:-2])
        #print(after_move_table_0)
        mobile_utillity.UtillityMethods.asequal(self,True,(before_move_table_0>after_move_table_0 and freeze_table_left==0),'Step X : Verify able to scroll the freeze table')    
        
    def create_lasso(self,parent_id,source_riser,target_riser,**kwargs):
        
        '''
        :param : parent_id='iosTabs0_f' or 'wbody1_f'
        :param : source_riser=''
        :param : target_riser=''
        :param : kwargs['verify']=['1 points', 'Filter Chart', 'Exclude from Chart']
        :param : kwargs['msg']='Step X : Verify lasso filters'
        :param : kwargs['select']='Filter Chart'
        :usage1: create_lasso('iosTabs0_f','riser!s0!g0!mbar!','riser!s0!g0!mbar!',verify=['1 points', 'Filter Chart', 'Exclude from Chart'],msg='Step 01 : ',select='Filter Chart')
        :usage2: create_lasso('iosTabs0_f','riser!s0!g0!mbar!','riser!s0!g0!mbar!',select='Filter Chart') 
        
        '''
        parent_css="#"+parent_id
        source_riser_css=parent_css+" [class*='" + source_riser + "']"
        target_riser_css=parent_css+" [class*='" + target_riser + "']"
        move=self.driver.find_element_by_css_selector(parent_css)
        mobile_utillity.UtillityMethods.move_to_element(self,move,1,1)
        test=mobile_utillity.UtillityMethods.parseinitfile(self,'test')
        source=self.driver.find_element_by_css_selector(source_riser_css)
        target=self.driver.find_element_by_css_selector(target_riser_css)
        if test=='android_web' or test=='android_app' :
            action=ActionChains(self.driver)
            action.drag_and_drop(source, target).perform()
            time.sleep(3)
        else :
            fromX=source.location['x']+(source.size['width']/2)
            fromY=source.location['y']+(source.size['height']/1.5)
            toX=target.location['x']+(target.size['width']/2)
            toY=target.location['y']+target.size['height']
            drag_drop_params={'duration':2.0,'fromX':fromX,'fromY':fromY,'toX':toX,'toY':toY}
            self.driver.execute_script('mobile: dragFromToForDuration',drag_drop_params)
            time.sleep(3)
        lasso_filter_css="div[id^='ibi'][class=tdgchart-tooltip] .tdgchart-tooltip-pad"
        lasso_filter_menus=self.driver.find_elements_by_css_selector(lasso_filter_css)
        menu_list=[menu.text.strip() for menu in lasso_filter_menus]
        #print(menu_list)
        if 'verify' in kwargs:
            mobile_utillity.UtillityMethods.asequal(self,menu_list,kwargs['verify'],kwargs['msg'])
        if 'select' in kwargs:
            lasso_filter_menus[menu_list.index(kwargs['select'])].click()
        time.sleep(3)
        
    def verify_drilldown_autolink_property(self,table_id,row_index,column_index,msg,**kwargs):
        '''
        :params : table_id='IWindowBodyFTB_0_0'
        :params : row_index=1 (index start from 1 )
        :params : column_index=1 (index start from 1 )
        :params : kwargs['total_link']=7,  kwargs['text_color']='cerulean_blue_2', kwargs['under_line']=True
        :usage : verify_drilldown_autolink_property('IWindowBodyFTB_0_0',1,1,'Step 01 :',total_link=7,text_color='cerulean_blue_2',under_line=True)
        '''
        autolink_css="#"+table_id+">tbody>tr>td:nth-child("+str(column_index)+") a[href]"
        table_index_css="#"+table_id+">tbody>tr:nth-child("+str(row_index)+")>td:nth-child("+str(column_index)+") a[href]"
        table_index=self.driver.find_element_by_css_selector(table_index_css)
        if 'total_link' in kwargs :
            total_autolink=len(self.driver.find_elements_by_css_selector(autolink_css))
            #print(total_autolink)
            mobile_utillity.UtillityMethods.asequal(self,total_autolink,kwargs['total_link'],msg+' Verify number of drilldown hyper links displayed')
        if 'text_color' in kwargs :
            expected_color=mobile_utillity.UtillityMethods.color_picker(self,kwargs['text_color'],'rgba')
            actual_text_color=Color.from_string(table_index.value_of_css_property("color")).rgba
            #print(actual_text_color)
            mobile_utillity.UtillityMethods.asequal(self,expected_color,actual_text_color,msg+' Verify drilldown hyper link color')
        if 'under_line' in kwargs :
            style=table_index.value_of_css_property("text-decoration")
            #print(style)
            mobile_utillity.UtillityMethods.asequal(self,True,('underline' in style),msg+' Verify drilldown hyper links displayed with underline')
    
    def select_field_menu_items(self,table_id,row_num,column_num,field_item=None,**kwargs):
        '''
        :param : table_id='IWindowBodyFTB_0_0'
        :param : row_num=2
        :param : column_num=1
        :param : field_item='Filter Cell' or field_item=None
        :usage1 : select_field_menu_items('IWindowBodyFTB_0_0',4,1,'Filter Cell')
        :usage2 : select_field_menu_items('IWindowBodyFTB_0_0',4,1)
        '''
        utiliobj= mobile_utillity.UtillityMethods(self.driver)
        test=utiliobj.parseinitfile('test')
        table_field_css="#"+table_id+" tr[id*='r" + str(row_num) + ".'] td[id$='C" + str(column_num) + "']"
        table_field=self.driver.find_element_by_css_selector(table_field_css)
        table_field.click()
        time.sleep(2)
        if field_item!=None :
            field_menu_css="#iosmenu2 #iosmenu1o li[class='iosDIVULLI'] span[class='amMenuItem']"
            field_menu=self.driver.find_elements_by_css_selector(field_menu_css)
            field_menu_items=[item.text.strip() for item in field_menu]
            if 'verify_field_items' in kwargs :
                #print(field_menu_items)
                utiliobj.asequal(field_menu_items,kwargs['verify_field_items'],kwargs['msg']) 
            field=field_menu[field_menu_items.index(field_item)]
            if test=='android_web' or test=='android_app' :
                field.click()
            else :
                utiliobj.webview_touch_actions(field,action='tap')
        time.sleep(2)
    
    def select_drilldown_table_cell(self,table_id,row_num,column_num):
        '''
        :param : table_id='IWindowBodyFTB_0_0'
        :param : row_num=2
        :param : column_num=1
        :usage : select_drilldown_table_cell('IWindowBodyFTB_0_0',4,1)
        '''
        utiliobj= mobile_utillity.UtillityMethods(self.driver)
        test=utiliobj.parseinitfile('test')
        table_field_css="#"+table_id+" tr[id*='r" + str(row_num) + ".'] td[id$='C" + str(column_num) + "'] a"
        table_field=self.driver.find_element_by_css_selector(table_field_css)
        time.sleep(2)
        if test=='android_web' or test=='android_app' :
                table_field.click()
        else :
            utiliobj.webview_touch_actions(table_field,action='tap')
        time.sleep(2)
            
    def long_press_on_raiser(self,parent_id,raiser_class):
        '''
        :param : parent_id='iosTabs0_f' or 'MAINTABLE_wbody0_f'
        :param : raiser_class='riser!s0!g3!mbar!'
        :usage : long_press_on_raiser('iosTabs0_f','riser!s0!g6!mbar!')
        '''
        utiliobj= mobile_utillity.UtillityMethods(self.driver)
        test=utiliobj.parseinitfile('test')
        parent_css="#"+parent_id
        raiser_css=parent_css+" [class*='" + raiser_class + "']"
        move=self.driver.find_element_by_css_selector(parent_css)
        mobile_utillity.UtillityMethods.move_to_element(self,move,1,1)
        raiser=self.driver.find_element_by_css_selector(raiser_css)
        if test=='android_web' or test=='android_app' :  
            ActionChains(self.driver).click_and_hold(raiser).release().perform()
            time.sleep(2)
        else :
            utiliobj.webview_touch_actions(raiser,action='long_press')
            time.sleep(2)
    
    def verify_table_cell_property(self, table_id, rownum, colnum, **kwargs):
        """
        :param : table_id = "IWindowBodyFTB_0_0"
        :param : colnum = 1, 2, 3...any integer value for cell number, including heading cells.
        :param : rownum= 1,2,3 ...
        :Usage : verify_report_cell_property("IWindowBodyFTB_0_0", 1,,1,bg_color='Cyan', font_color='magenta', text_value='CAR', font_name='Arial', font_size='10pt', bold=True, italic=True, underline=True, text_align='Center')
        """
        table_css="#" + table_id + " > tbody > tr:nth-child(" + str(rownum) + ") > td:nth-child(" + str(colnum) + ")"
        cell_obj=self.driver.find_element_by_css_selector(table_css)
        for key in kwargs:
            if 'bg_color' in key:
                expected_background_color=mobile_utillity.UtillityMethods.color_picker(self, kwargs['bg_color'], 'rgba')
                actual_background_color=Color.from_string(cell_obj.value_of_css_property("background-color")).rgba
                mobile_utillity.UtillityMethods.asin(self, actual_background_color, expected_background_color , kwargs['msg'] + ". Verification of Cell Background color.")
            if 'font_color' in key:
                expected_text_color=mobile_utillity.UtillityMethods.color_picker(self, kwargs['font_color'], 'rgba')
                actual_text_color=Color.from_string(cell_obj.value_of_css_property("color")).rgba
                mobile_utillity.UtillityMethods.asin(self, actual_text_color, expected_text_color, kwargs['msg'] + ". Verification of Cell Text color.")
            if 'text_value' in key:
                actual_text=cell_obj.text.strip()
                mobile_utillity.UtillityMethods.asequal(self, kwargs['text_value'], actual_text, kwargs['msg'] + ". Verification of Cell Text.")
            if 'font_name' in key:
                actual_font=cell_obj.value_of_css_property("font-family").strip('"').upper()
                mobile_utillity.UtillityMethods.asequal(self, kwargs['font_name'].upper(), actual_font, kwargs['msg'] + ". Verification of Cell Text Font name.")
            if 'font_size' in key:
                expected_font_size=round(float(1.333333*int(kwargs['font_size'][:-2])))
                actual_font_size=cell_obj.value_of_css_property("font-size")
                actual_font_size=round(float(actual_font_size[:-2]))
                mobile_utillity.UtillityMethods.asequal(self, expected_font_size, actual_font_size, kwargs['msg'] + ". Verification of Cell Text Font Size.")
            if 'bold' in key:
                actual_weight=True if cell_obj.value_of_css_property("font-weight") in ['700', 'bold'] else False
                mobile_utillity.UtillityMethods.asequal(self, kwargs['bold'], actual_weight, kwargs['msg'] + ". Verification of Cell Text is Bold.")
            if 'italic' in key:
                actual_style=True if cell_obj.value_of_css_property("font-style")=='italic' else False
                mobile_utillity.UtillityMethods.asequal(self, kwargs['italic'], actual_style, kwargs['msg'] + ". Verification of Cell Text is Italics.")
            if 'underline' in key:
                actual_decoration=True if 'underline' in cell_obj.value_of_css_property("text-decoration") else False
                mobile_utillity.UtillityMethods.asequal(self, kwargs['underline'], actual_decoration, kwargs['msg'] + ". Verification of Cell is underlined.")
            if 'text_align' in key:
                actual_font=cell_obj.value_of_css_property("text-align")
                mobile_utillity.UtillityMethods.asequal(self, kwargs['text_align'], actual_font, kwargs['msg'] + ". Verification of Cell Text alignment.")
            if 'title_popup' in key:
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element_by_css_selector(table_css)).perform()
                del action
                time.sleep(1)
                actual_popup=self.driver.find_element_by_css_selector("#IBI_popupHere table").text.strip()
                mobile_utillity.UtillityMethods.asequal(self, kwargs['title_popup'], actual_popup, kwargs['msg'] + ". Verification of Title Popup.")
    
    def select_drilldown_tooltip_menu(self,parent_id,raiser_class,menu,**kwargs):
        '''
        :param: parent_id=MAINTABLE_wbody0_f'
        :param: raiser_class='riser!s0!g3!mbar!'
        :param: menu='Filter'
        :usage: select_drilldown_tooltip_menu('iosTabs0_f','riser!s0!g3!mbar!','IBI')
        '''
        parent_css="#"+parent_id
        raiser_css=parent_css+" [class*='" + raiser_class + "']"
        tooltip_css=parent_css+" span[id='tdgchart-tooltip']>div>ul>li[class='tdgchart-tooltip-pad'] [onclick]"
        parent_element=self.driver.find_element_by_css_selector(parent_css)
        ActionChains(self.driver).move_to_element_with_offset(parent_element,1,1).perform()
        raiser=self.driver.find_element_by_css_selector(raiser_css)
        if 'touch_tap' in kwargs and self.test=='ios_web' :
            utliobj=mobile_utillity.UtillityMethods(self.driver)
            utliobj.webview_touch_actions(raiser,'tap')
        else :
            ActionChains(self.driver).move_to_element(raiser).perform()
        tooltip=self.driver.find_elements_by_css_selector(tooltip_css)
        tooltip_menus=[item.text.strip() for item in tooltip]
        tooltip_element=tooltip[tooltip_menus.index(menu)]
        if 'touch_tap' in kwargs and self.test=='ios_web' :
            utliobj.webview_touch_actions(tooltip_element,'tap')
        else :
            tooltip_element.click()
        time.sleep(2)
    
    def verify_chart_drilldown_navigation_menu(self,parent_id,expected_menu_list,msg):
        '''
        :Param : parent_id='MAINTABLE_wbody0_f'
        :Param : expected_menu_list=['Home', '->', 'Stereo Systems']
        :Usage : verify_drilldown_navigation_menu('MAINTABLE_wbody0_f',['Home', '->', 'Stereo Systems'],'Step 03.1 : Verify drilldown menu option')
        '''
        navigation_css="#"+parent_id+" foreignObject div>span"
        actual_menu_list=[]
        menu_elements=self.driver.find_elements_by_css_selector(navigation_css)
        for menu in menu_elements :
            if '\u2192' in menu.text.strip() :
                actual_menu_list.append('->')
            else :
                actual_menu_list.append(menu.text.strip())
        mobile_utillity.UtillityMethods.asequal(self,actual_menu_list,expected_menu_list,msg)
        