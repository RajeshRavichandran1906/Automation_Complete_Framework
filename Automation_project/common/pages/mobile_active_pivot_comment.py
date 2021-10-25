from common.lib import mobile_utillity
from common.lib.mobile_base import BasePage
import time,re


class Active_Pivot_Comment(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Pivot_Comment, self).__init__(driver)

    def _validate_page(self, driver):
        print("Implement Page Loading wait")

    def veryfy_pivot_table_title(self,parent_id, expected_title, msg):
        """
        Syntax: veryfy_pivot_table_title('piv1', 'StateBYCategory,ProductID', 'Step 10: Veryfy filter row.')
        @author = Niranjan 
        """
        pivot_title_table= "#" + parent_id + " tbody > tr:nth-child(1) > td > table[border='1']>tbody>tr>td>div"
        actual_title=self.driver.find_element_by_css_selector(pivot_title_table).text.strip()
        #print(actual_title)
        mobile_utillity.UtillityMethods.asequal(self, expected_title, actual_title, msg)
        
    def verify_Pivot_Tool_Bar(self,parent_id,expected_list,msg,original_view=False,**kwargs):
        
        '''
        :param : parent_id='iosfullscreenbot' or 'wmenu1'
        :param : exptected_list=['More Options','Freeze icon','Aggregation']
        :param : original_view=True (When chart is displaying in original view) else original_view=Fals
        :param : **kwargs=default_aggregaion_text='Count' (Should be pass default aggregaion text when Aggregation is listed in exptected list)
        :usage1: .verify_Pivot_Tool_Bar('wmenu1',['More Options','Freeze icon','Aggregation'],'Step 03.3 : Verify the active pivot toolbar)
        :usage2: .verify_Pivot_Tool_Bar('wmenu1',['More Options','Freeze icon','Aggregation'],'Step 03.3 : Verify the active pivot toolbar, displayed at the bottom of the Pivot tab in full screen view',original_view=True,verify_position=True) 
        '''
        
        actual_list=[]
        icons_css="#"+parent_id +" .arPivotMenuBar table>tbody>tr>td div[onclick] img" if original_view==True else "#"+parent_id+" [id^='iosfullscreenbot'] table>tbody>tr>td div[onclick] img"
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
                parent_css="#"+parent_id+" .arPivotMenuBar div[title='More Options'] img"
            more=self.driver.find_element_by_css_selector(parent_css)
            if more.is_displayed() :
                actual_list.append('More Options')
        except : pass 
        
        '------ Freeze Icon -----'
        try :
            if original_view==False :
                parent_css="#"+parent_id+" [id^='LINKIMG'] img"
            else :
                parent_css="#"+parent_id+" .arPivotMenuBar [id^='LINKIMG'] img"
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
                parent_css="#"+parent_id+" .arPivotMenuBar [id^='SUM'] img"
                text_css="#"+parent_id+" .arPivotMenuBar [id^='SUM'] td[class^='tabPagingText']"
            aggregation=self.driver.find_element_by_css_selector(parent_css)
            actual_agg_text=self.driver.find_element_by_css_selector(text_css).text.strip()
            exptected_agg_text=exptected_agg_text=kwargs['default_aggregaion_text'] if 'default_aggregaion_text' in kwargs else 'Sum'
            if aggregation.is_displayed()==True and actual_agg_text==exptected_agg_text :
                actual_list.append('Aggregation')
        except : pass
        #print(actual_list)
        
        if 'verify_position' in kwargs :
            if original_view==True :
                postion=self.driver.find_element_by_css_selector("#"+parent_id+" .arPivotMenuBar")
                if postion.location['x']==0 and postion.location['y']>=0 and postion.location['y']<=30  :
                    status=True
                else :
                    status=False
                #print(postion.location)
                mobile_utillity.UtillityMethods.asequal(self,True,status,'Step X : Verify the chart toolbars in the top of the report in original view')
            else :
                postion1=self.driver.find_element_by_css_selector("#"+parent_id+" [id^='iosfullscreenbot']>table")
                if postion1.location['x']==0 and postion1.location['y']!=0 :
                    status1=True
                else :
                    status1=False
                #print(postion1.location)
                mobile_utillity.UtillityMethods.asequal(self,True,status1,'Step X : Verify the chart toolbars in bottom of the report in fullscreen view')    
            
        status=True if actual_list==expected_list and len(actual_list)==total_icons else False
        mobile_utillity.UtillityMethods.asequal(self,True,status,msg)    
    
    
    def select_pivot_menu(self,parent_id,navigate_patten,original_view=False):
        '''
        :param : parent_id='iosfullscreenbot' or wmenu1
        :param : navigate_patten='Add (Y)->Product' or New
        :param : original_view=True (When repor is displaying in original view ) else original_view=False
        :usage : select_pivot_menu('iosfullscreenbot','Original View')
        '''
        
        if original_view==True :
            menu_css="#"+ parent_id +" .arPivotMenuBarContainer div[title='More Options'] img"
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
            
    def verify_pivot_menu(self,parent_id,sub_menu,expected_menu_list,msg,original_view=False): 
        '''
        :param : parent_id='iosfullscreenbot' or wmenu1
        :param : sub_menu='Add (Y)' or None (When do no verify sub menus)
        :param : expected_menu_list = ['New', 'Original View', 'Group By (X)', 'Add (Y)', 'Restore Original']
        :param : original_view=True (When repor is displaying in original view ) else original_view=False
        :usage : verify_pivot_menu('wmenu1',None,['New', 'Fullscreen', 'Group By (X)', 'Add (Y)', 'Pivot Tool'],'Step 03.6 : Verify the pivot menu options are displaying properly in original view',original_view=True)
        '''
        if original_view==True :
            menu_css="#"+ parent_id +" .arPivotMenuBarContainer div[title='More Options'] img"
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
        


class Mobile_Viewr_Active_Pivot_Comment(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Mobile_Viewr_Active_Pivot_Comment, self).__init__(driver)
    
    def select_pivot_menu_options_menu(self,popup_id,menu_navigation,**kwargs):
        '''
        :Param : popup_id='wall1'
        :Param : menu_navigation='Group By (X)->State' or 'Restore Original'
        :Param : kwargs['table_id']='ITableData1'
        :Usage : select_pivot_menu_options_menu('wall1','Group By (X)->State')  
        '''
        icon_css="#"+popup_id+" .arPivotMenuBar .arPivotMenuBarContainer div[title='More Options'] img"
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
    
    def verify_pivot_menu_options_menu(self,popup_id,menu_navigation,expected_menu_items,msg,**kwargs):
        '''
        :Param : popup_id='wall1'
        :Param : menu_navigation=None or 'Group By (X)'
        :Param : expected_menu_items= ['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        :Param : msg='Step 02 : Verify char bar more options'
        :Param : kwargs['table_id']='ITableData1'
        :Usage : verify_pivot_menu_options_menu('wall1','Group By (X)',['√ Product', 'Category', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales'],'Step 02 : Verify char bar more options')  
        :Usage : verify_pivot_menu_options_menu('wall1',None,['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales'],'Step 02 : Verify char bar more options')  
        '''
        icon_css="#"+popup_id+" .arPivotMenuBar .arPivotMenuBarContainer div[title='More Options'] img"
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