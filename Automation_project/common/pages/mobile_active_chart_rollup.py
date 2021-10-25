from common.lib import mobile_utillity
from common.lib.mobile_base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Active_Chart_Rollup(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Chart_Rollup, self).__init__(driver)

    def _validate_page(self, driver):
        print("Implement Page Loading wait")
    
    def verify_rollup_report_title(self,parent_id,expected_title,msg):
        '''
        params : parent_ID='IWindowBodyFTS_4_0'
        params : expected_title='Product BY State
        usage : verify_rollup_report_title('IWindowBodyFTS_4_0','Product BY State','Step 01 : Verify rollup report title")
        '''
        parent_css="#"+parent_id+" tt>div"
        actual_title=self.driver.find_element_by_css_selector(parent_css).text.strip()
        #print(actual_title)
        mobile_utillity.UtillityMethods.asequal(self,actual_title,expected_title,msg)
    
    def verify_arChartMenu_toolbar(self,parent_id,msg,original_view=False):
        '''
        params :parent_id='iosfullscreenbot' or wmenu1
        params :no_of_toolbar_items=10
        params : original_view=True (If want to verify chart tool bar in original view)
        usage 1: verify_arChartMenu_toolbar('iosfullscreenbot',0,'Step 02 : Verify chart toolbar display in fullscreen view')
        usage 2: verify_arChartMenu_toolbar('MAINTABLE_wbodyMain0',0,'Step 02 : Verify chart toolbar display in original view',original_view=True)
        '''
        if original_view==True :
            original_view_menus_list=['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart','Freeze icon','Aggregation']
            ov_toolbar_img_css="#"+parent_id+" .arChartMenuBar  table>tbody>tr>td img"
            ov_toolbar_title_css="#"+parent_id+" .arChartMenuBarContainer div[title]"
            '<------ Check all tool bar images are displaying ------>' 
            ov_toolbar_img=self.driver.find_elements_by_css_selector(ov_toolbar_img_css)
            ov_display_count=0
            for img in ov_toolbar_img :
                if img.is_displayed() :
                    ov_display_count=ov_display_count+1
            '<------ get all tool bar title ------>' 
            title_elements=self.driver.find_elements_by_css_selector(ov_toolbar_title_css)
            actual_title=[title.get_attribute("title") for title in title_elements]
            fi = self.driver.find_element_by_css_selector("#"+parent_id+" [id^='LINKIMG'] img").is_displayed()
            if fi :
                actual_title.append('Freeze icon')
            actual_title.append(self.driver.find_element_by_css_selector("#"+parent_id+" [id^='SUM'] [title]").get_attribute("title").strip())
            total_title=0
            if actual_title==original_view_menus_list :
                total_title=len(original_view_menus_list)
            mobile_utillity.UtillityMethods.asequal(self,ov_display_count,total_title,msg)
                
        else :
            full_view_menus_list=['More Options','Bar','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart','Freeze icon','Aggregation']
            toolbar_img_css="#"+parent_id+" [id^='iosfullscreenbot'] table>tbody>tr>td img"
            toolbar_title_css="#"+parent_id+" div[title]"
            '<------ Check all tool bar images are displaying ------>'   
            toolbar=self.driver.find_elements_by_css_selector(toolbar_img_css)
            fv_display_count=0
            for item in toolbar :
                if item.is_displayed() :
                    fv_display_count=fv_display_count+1
            more=self.driver.find_element_by_css_selector("#"+parent_id+" div[id^='cpop']>div[onclick^='ibiMenu.Showmenu'] img").is_displayed()
            actual_title_list=[]
            if more :
                actual_title_list.append('More Options')
            title_elements=self.driver.find_elements_by_css_selector(toolbar_title_css)
            for title in title_elements :
                actual_title_list.append(title.get_attribute("title").strip())
            fi = self.driver.find_element_by_css_selector("#"+parent_id+" [id^='LINKIMG'] img").is_displayed()
            if fi :
                actual_title_list.append('Freeze icon')
            agg=self.driver.find_element_by_css_selector("#"+parent_id+" div[id^='SUMFS']>div[onclick^='ibiMenu.Showmenu'] img")
            if agg :
                actual_title_list.append('Aggregation')
            if actual_title_list==full_view_menus_list :
                total_title=len(full_view_menus_list)
            mobile_utillity.UtillityMethods.asequal(self,fv_display_count,total_title,msg)
    
    def click_chart_menu_bar_items(self, parent_id, item_index):
        """
        :param: parent_id='MAINTABLE_wbody1' or iosfullscreenbot
        :param: item_index=1 or 2 or 3 or ...
        :Usage click_chart_menu_bar_items('MAINTABLE_0', 1,original_view=True)
        :Usage click_chart_menu_bar_items('iosfullscreenbot', 1,original_view=False)
        """
        menu_items_css="#" + parent_id + "  div[onclick] img"
        menu_items=self.driver.find_elements_by_css_selector(menu_items_css)
        menu_items[item_index].click()
        time.sleep(1)
    
    def select_more_options_menu(self,parent_id,navigate_patten,original_view=False):
        '''
        :param : parent_id='iosfullscreenbot' or wall1
        :param : navigate_patten='Add (Y)->Product' or New
        :param : original_view=True (When repor is displaying in original view ) else original_view=False
        :usage : select_more_options_menu('iosfullscreenbot','Add (Y)->Product',original_view=False)
        '''
        
        if original_view==True :
            menu_css="#"+ parent_id +" .arChartMenuBar div[title='More Options'] img"
        else :
            menu_css="#"+ parent_id +" div[id^='cpop']>div[onclick^='ibiMenu.Showmenu'] img"
        self.driver.find_element_by_css_selector(menu_css).click()
        menu=navigate_patten.split('->')
        for i in range(len(menu)):
            sub_menu_css="#iosmenu2 #iosmenu"+str(i+1)+"o li[class='iosDIVULLI'] span[class='amMenuItem']"
            temp_elements=self.driver.find_elements_by_css_selector(sub_menu_css)
            sub_menu_elements=[filter_element for filter_element in temp_elements if filter_element.text!='>']
            del temp_elements
            sub_menus=[item.text.replace('√','').strip() for item in sub_menu_elements]
            sub_menu_elements[sub_menus.index(menu[i])].click()
            del sub_menu_elements
            del sub_menus
            time.sleep(1)
            
    def verify_more_options_menu(self,parent_id,sub_menu,expected_menu_list,msg,original_view=False): 
        '''
        :param : parent_id='iosfullscreenbot' or wall1
        :param : sub_menu='Add (Y)' or None (When do no verify sub menus)
        :param : expected_menu_list = ['New', 'Original View', 'Group By (X)', 'Add (Y)', 'Restore Original']
        :param : original_view=True (When repor is displaying in original view ) else original_view=False
        :usage : select_more_options_menu('iosfullscreenbot','Add (Y)->Product',original_view=False)
        '''
        if original_view==True :
            menu_css="#"+ parent_id +" .arChartMenuBar div[title='More Options'] img"
        else :
            menu_css="#"+ parent_id +" div[id^='cpop']>div[onclick^='ibiMenu.Showmenu'] img"
        self.driver.find_element_by_css_selector(menu_css).click()
        time.sleep(1)
        sub_menu_css="#iosmenu2 #iosmenu1o li[class='iosDIVULLI'] span[class='amMenuItem']"
        temp_elements=self.driver.find_elements_by_css_selector(sub_menu_css)
        menu_elements=[filter_element for filter_element in temp_elements if filter_element.text!='>']
        actual_menu_list=[item.text.strip() for item in menu_elements]
        if sub_menu!=None :
            menu_elements[actual_menu_list.index(sub_menu)].click()
            time.sleep(1)
            sub_menu_css="#iosmenu2 #iosmenu2o li[class='iosDIVULLI'] span[class='amMenuItem']"
            temp_elements=self.driver.find_elements_by_css_selector(sub_menu_css)
            sub_menu_elements=[filter_element for filter_element in temp_elements if filter_element.text!='>']
            actual_menu_list=[item.text.strip() for item in sub_menu_elements] 
            self.driver.find_element_by_css_selector("#iosmenu2o div[onclick^='ibi_iPadMenu.hide']").click()
            time.sleep(1)
        #print(actual_menu_list)
        mobile_utillity.UtillityMethods.asequal(self,actual_menu_list,expected_menu_list,msg)
        self.driver.find_element_by_css_selector("#iosmenu2 div[onclick='ibi_iPadMenu.hideMain()']").click()
        time.sleep(1)



''' <------------------------------ This class for mobile viewer page  ------------------------------>'''
        
class Mobile_Viewer_Active_Chart_Rollup(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Mobile_Viewer_Active_Chart_Rollup, self).__init__(driver)

    def select_chart_more_options_menu(self,popup_id,menu_navigation,**kwargs):
        '''
        :Param : popup_id='wall1'
        :Param : menu_navigation='Group By (X)->State' or 'Restore Original'
        :Param : kwargs['table_id']='ITableData1'
        :Usage : select_chart_more_options_menu('wall1','Group By (X)->State')  
        '''
        icon_css="#"+popup_id+" div[id^='wmenu'] .arChartMenuBar .arChartMenuBarContainer div[title='More Options'] img"
        self.driver.find_element_by_css_selector(icon_css).click()
        time.sleep(1)
        table_id=kwargs['table_id'] if 'table_id' in kwargs else 'ITableData0'
        table_index=str(table_id[-1])
        popup_index=str(popup_id[-1])
        item_index=0
        menu_items=menu_navigation.split('->')
        for item in menu_items :
            menu_item_css="div[id^='dt"+table_index+"_cpop"+popup_index+"'][id$='_"+str(item_index)+"'][style*='display: block']>table>tbody>tr>td>span[id^='set']"
            menu_item_elements=self.driver.find_elements_by_css_selector(menu_item_css)
            menu_items_text=[ele.text.strip() for ele in menu_item_elements]
            item_index=menu_items_text.index(item)
            menu_item_elements[item_index].click()
            time.sleep(2)
    
    def verify_chart_more_options_menu(self,popup_id,menu_navigation,expected_menu_items,msg,**kwargs):
        '''
        :Param : popup_id='wall1'
        :Param : menu_navigation=None or 'Group By (X)'
        :Param : expected_menu_items= ['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        :Param : msg='Step 02 : Verify char bar more options'
        :Param : kwargs['table_id']='ITableData1'
        :Usage : verify_chart_more_options_menu('wall1','Group By (X)',['√ Product', 'Category', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales'],'Step 02 : Verify char bar more options')  
        :Usage : verify_chart_more_options_menu('wall1',None,['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales'],'Step 02 : Verify char bar more options')  
        '''
        icon_css="#"+popup_id+" div[id^='wmenu'] .arChartMenuBar .arChartMenuBarContainer div[title='More Options'] img"
        self.driver.find_element_by_css_selector(icon_css).click()
        time.sleep(1)
        table_id=kwargs['table_id'] if 'table_id' in kwargs else 'ITableData0'
        table_index=str(table_id[-1])
        popup_index=str(popup_id[-1])
        item_index=0
        menu_navigation='temp_click' if menu_navigation==None else menu_navigation+'->temp_click'
        menu_items=menu_navigation.split('->')
        for item in menu_items :
            menu_item_css="div[id^='dt"+table_index+"_cpop"+popup_index+"'][id$='_"+str(item_index)+"'][style*='display: block']>table>tbody>tr"
            menu_item_elements=self.driver.find_elements_by_css_selector(menu_item_css)
            menu_menu_text=[ele.text.strip().replace('\n','').replace('►','').replace('>','') for ele in menu_item_elements]
            if item==menu_items[-1] :
                actual_menu_items=[ele.text.strip().replace('\n','').replace('►','').replace('>','') for ele in menu_item_elements if ele.text.strip()!='']
                mobile_utillity.UtillityMethods.asequal(self,actual_menu_items,expected_menu_items,msg)
            else :
                item_index=menu_menu_text.index(item)
                menu_item_elements[item_index].click()
    
    def click_chart_bar_icon(self,parent_id,icon_index):
        '''
        :Param : parent_id='wmenu1'
        :Param : icon_index=1 or 2 (icon index start from 1)
        :Usage : click_chart_bar_icon('wmenu1',2)
        '''
        icon_css="#"+parent_id+" .arChartMenuBar .arChartMenuBarContainer  div[onclick^='ibi'] img"
        icons=self.driver.find_elements_by_css_selector(icon_css)
        icons[int(icon_index)-1].click()
        time.sleep(2)