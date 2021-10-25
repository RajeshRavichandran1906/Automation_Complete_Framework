from common.lib import mobile_utillity
from common.lib.mobile_base import BasePage
import time

class Active_Filter_Selection(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Filter_Selection, self).__init__(driver)

    def _validate_page(self, driver):
        print("Implement Page Loading wait")
    
    def verify_filter_buttons(self,parent_id,expected_btn_list, msg):
        
        """
        :Usage: verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], 'Step 10: Veryfy All buttons Present.')
        @author = Prabhakaran 
        """
        filter_buttons_css="#"+parent_id+" .arFilterButton"
        filter_buttons=self.driver.find_elements_by_css_selector(filter_buttons_css)        
        actual_btn_list=[btn.text.strip() for btn in filter_buttons if btn.is_displayed()]
        #print(actual_btn_list)
        mobile_utillity.UtillityMethods.asequal(self, expected_btn_list, actual_btn_list, msg)
        
    def verify_filter_selection(self,parent_id,msg,*args):
        
        '''
        :param: parent_id='iosTabs0' or wall1
        :param: args(expected_values)=
        '''
        parent_css="#"+parent_id+" tr[class='arFilterItem']"
        filter_selection=self.driver.find_elements_by_css_selector(parent_css)
        verification_status=None
        for i in range(len(args)) :
            actual_list=filter_selection[i].text.strip().split('\n')
            #print(actual_list)
            if actual_list==args[i] :
                verification_status=True
            else :
                verification_status=False
                break
        mobile_utillity.UtillityMethods.asequal(self,True,verification_status,msg)
            


''' <----------------------------------------- This is separate filter selection class for mobile viewer -----------------------------------------> '''
        
class Mobile_Viewer_Active_Filter_Selection(BasePage):
    
    def __init__(self, driver):
        super(Mobile_Viewer_Active_Filter_Selection, self).__init__(driver)
        self.test=mobile_utillity.UtillityMethods.parseinitfile(self,'test')
    
    def select_filter_button(self,filter_popup_index,button_name,**kwargs):
        '''
        :Param : filter_popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : button_name ='Operator: AND' or 'Add Condition' or 'Filter' or 'Highlight' or 'Clear All'
        :Param : kwargs['verify'] = ['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All']
        :Usage1 : select_mv_filter_button(1,'Filter')
        :Usage2 : select_mv_filter_button(1,'Filter',verify=['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'],msg='Step 02.1 : Verify filter buttons')
        ''' 
        btns_css='#wall'+str(filter_popup_index)+' #FiltTable'+str(filter_popup_index)+" .arFilterButton"    
        filter_buttons=self.driver.find_elements_by_css_selector(btns_css)
        buttons=[btn.text.strip() for btn in filter_buttons]
        if 'verify' in kwargs :
            mobile_utillity.UtillityMethods.asequal(self,buttons,kwargs['verify'],kwargs['msg'])
        if button_name=='Add Condition' :
            filter_buttons[buttons.index(button_name)].find_element_by_css_selector("div[onclick^='ibiMenu.Showmenu']").click()
        else :
            filter_buttons[buttons.index(button_name)].click()
        time.sleep(2)
    
    def select_filter_condition(self,popup_index,row_num,condition_name,**kwargs):
        '''
        :Param : filter_popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : row_num : 1 or 2 (Row number alwasy start from 1) row num is position of filed name in filter popup window
        :Param : condition_name ='Equals' or 'Not Equal'
        :Usage : act_filter.select_mv_filter_condition(2,1,'Equals')
        '''
        table_id=kwargs['table_id'] if 'table_id' in kwargs else 'ITableData0'
        table_index=table_id[-1]
        icon_css="#FiltTable"+str(popup_index)+" .arFilterItem div[id='ft"+str(popup_index)+"_"+str(row_num-1)+"']>div[onclick^='ibiMenu'] img"
        conditions_css="#dt"+str(table_index)+"_ft"+str(popup_index)+"_"+str(row_num-1)+"_x__0 span[id^='set']"
        self.driver.find_element_by_css_selector(icon_css).click()
        time.sleep(1)
        condition_elements=self.driver.find_elements_by_css_selector(conditions_css)
        conditions=[opt.text.strip() for opt in condition_elements]
        #print(conditions)
        expected_condtions=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        mobile_utillity.UtillityMethods.asequal(self,conditions,expected_condtions,'Step X : Verify all filter conditions')
        condition_elements[conditions.index(condition_name)].click()
        time.sleep(1)
        condtion=self.driver.find_elements_by_css_selector("#FiltTable"+str(popup_index)+" .arFilterItem")
        value=condtion[row_num-1].find_element_by_css_selector("td:nth-child(3) .arFilterItemDrowpDown").text.strip()
        mobile_utillity.UtillityMethods.asequal(self,value,condition_name,"Step X : Verify "+condition_name+" is selected")
        
    def add_condition_field(self,popup_index,condition_feild,table_id='ITableData0'):
        '''
        :Param : filter_popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : condition_feild ='State' or 'Product'
        :Usage : act_filter.add_mv_condition_field(2,'Product ID')
        '''
        
        self.select_filter_button(popup_index,'Add Condition')
        table_index=str(table_id[-1])
        feild_css="#dt"+table_index+"_filtop0_0 td[title='"+condition_feild+"']"
        self.driver.find_element_by_css_selector(feild_css).click()
        time.sleep(2)
    
    def select_filter_value(self,popup_index,row_num,value,**kwargs):
        '''
        :Param : popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : row_num : 1 or 2 (Row number alwasy start from 1) row num is position of condition filed name in filter popup window
        :Param : value ='CA' (if you want to select only one value);  value=['CA','CT','WA'] (if you want to select multiple values)
        :Param : filter_values_type='small' ( if filter value list small) ; filter_values_type='large' (if filter value list large set of data)
        :Param : table_id='ITableData0' or 'ITableData1'
        :Param : kwargs['value2'] ='CA' ( This keyword arguments should be pass when filter condition is 'Between' or 'Not Between'
        :Usage 1 : mv_filter.select_filter_value(1,1,['CA','CT','WA'],'small')
        :Usage 2 : mv_filter.select_filter_condition(1,3,'Omits')
        :Usage 3 : mv_filter.select_filter_value(1,4,'Coffee',value2='Gifts')
        :Usage 5 : mv_filter.select_filter_value(1,4,'Coffee','large',value2='Gift')
        '''
        table_id=kwargs['table_id'] if 'table_id' in kwargs else 'ITableData0'
        filter_values_type=kwargs['filter_values_type'] if 'filter_values_type' in kwargs else 'small'
        condtion_elements=self.driver.find_elements_by_css_selector("#FiltTable"+str(popup_index)+" .arFilterItem")
        condition_value=condtion_elements[row_num-1].find_element_by_css_selector("td:nth-child(3) .arFilterItemDrowpDown").text.strip()
        if condition_value in ['Contains', 'Contains (match case)', 'Omits', 'Omits (match case)'] :
            inputbox_css="#fboxi"+str(row_num-1)+" input[name^='"+str(row_num-1)+"filtPatt']"
            self.driver.find_element_by_css_selector(inputbox_css).send_keys(value)
            time.sleep(1)
        elif condition_value in ['Between', 'Not Between'] :
            self.select_between_condition_filter_value(popup_index, row_num, value,**kwargs)
        else :
            table_index=table_id[-1]
            icon_css="#FiltTable"+str(popup_index)+" .arFilterItem div[id='ftp"+str(popup_index)+"_1_"+str(row_num-1)+"']>div[onclick^='ibiMenu'] img"
            self.driver.find_element_by_css_selector(icon_css).click()
            time.sleep(1)
            if filter_values_type=='small' :
                small_filter_values_css="#dt"+str(table_index)+"_ftp"+str(popup_index)+"_1_"+str(row_num-1)+"_x__0 table>tbody>tr span[id^='set']"
                filter_value_elements=self.driver.find_elements_by_css_selector(small_filter_values_css)
                filter_values=[value.text.strip() for value in filter_value_elements]
                if type(value) is list : 
                    for v in value :
                        filter_value_elements[filter_values.index(v)].click()
                        time.sleep(1)
                else :
                    filter_value_elements[filter_values.index(value)].click()
            else :
                pass
            time.sleep(1)
            value_css="#FiltTable"+str(popup_index)+" .arFilterItem #fboxi"+str(row_num-1)+" .arFilterItemDrowpDown"
            actual_selected_value=self.driver.find_element_by_css_selector(value_css).text.strip()
            expect_selected_value="*"+value[0] if type(value) is list else value
            mobile_utillity.UtillityMethods.asequal(self,actual_selected_value,expect_selected_value,'Step X : Verify filter values are selected')
    
    def select_between_condition_filter_value(self,popup_index,row_num,value1,value2,**kwargs):
        '''
        :Param : popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : row_num : 1 or 2 (Row number alwasy start from 1) row num is position of condition filed name in filter popup window
        :Param : value1 ='CA' 
        :Param : value2 ='CT' 
        :Param : filter_values_type='small' ( if filter value list small) ; filter_values_type='large' (if filter value list large set of data)
        :Param : table_id='ITableData0' or 'ITableData1'
        :Usage : mv_filter.select_filter_value(1,4,'Coffee','Gift','small')
        '''
        
        table_id=kwargs['table_id'] if 'table_id' in kwargs else 'ITableData0'
        filter_values_type=kwargs['filter_values_type'] if 'filter_values_type' in kwargs else 'small'
        table_index=table_id[-1]
        for i in range(1,3) :
            value=value1 if i==1 else value2
            icon_css="#FiltTable"+str(popup_index)+" .arFilterItem div[id='ftp"+str(popup_index)+"_"+str(i)+"_"+str(row_num-1)+"']>div[onclick^='ibiMenu'] img"
            self.driver.find_element_by_css_selector(icon_css).click()
            time.sleep(1)
            if filter_values_type=='small' :
                small_filter_values_css="#dt"+str(table_index)+"_ftp"+str(popup_index)+"_"+str(i)+"_"+str(row_num-1)+"_x__0 table>tbody>tr span[id^='set']"
                filter_value_elements=self.driver.find_elements_by_css_selector(small_filter_values_css)
                filter_values=[value.text.strip() for value in filter_value_elements]
                filter_value_elements[filter_values.index(value)].click()
            else :
                pass
            time.sleep(1)
            if i==1 :
                value_css="#FiltTable"+str(popup_index)+" .arFilterItem #fboxi"+str(row_num-1)+" .arFilterItemDrowpDown"
                expect_selected_value=value1
            else :
                value_css="#FiltTable"+str(popup_index)+" .arFilterItem #fbox2i"+str(row_num-1)+" .arFilterItemDrowpDown"
                expect_selected_value=value2
            actual_selected_value=self.driver.find_element_by_css_selector(value_css).text.strip()
            mobile_utillity.UtillityMethods.asequal(self,actual_selected_value,expect_selected_value,'Step X : Verify filter value is selected')
    
    
    def verify_filter_selection_row(self,popup_index,row_num,expected_list,msg):
        '''
        :Param : popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : row_num : 1 or 2 (Row number alwasy start from 1) row num is position of condition filed name in filter popup window
        :Param : expected_list = ['Category', 'Not Between', '[', 'Coffee', 'Gifts']
        :Param : msg = 'Verify filter selection values'
        :Usage : mv_filter.verify_filter_selection_row(1,1,['Sate', 'Equals', '*CA'],'Step 01.1 : Verify filter selection values')
        '''
        filter_selection_css="#FiltTable"+str(popup_index)+" .arFilterItem:nth-child("+str(row_num+1)+")"
        filter_delete_icon=self.driver.find_element_by_css_selector(filter_selection_css+" div[onclick*='ibiFilter.clearFilter'] img")
        filter_selection=self.driver.find_element_by_css_selector(filter_selection_css)
        actual_list=filter_selection.text.strip().split('\n')
        #print(actual_list)
        status= True if actual_list==expected_list and filter_delete_icon.is_displayed()==True else False
        mobile_utillity.UtillityMethods.asequal(self,True,status,msg)
           
    def verify_multiple_verify_filter_selection_rows(self,popup_index,msg,*expected_list_arg):
        '''
        :Param  : :Param : popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param  : msg ='Step 03.1 : Verify all filter selection values'
        :Param  : *expected_list_arg = ['State', 'Equals', '*CA'],['Product ID', 'Greater than', 'G110'],['Product', 'Omits'],['Category', 'Not Between', '[', 'Coffee', 'Gifts']
        :Usage1 : verify_multiple_verify_filter_selection_rows(1,'Step 02 : Verify all filter',['State', 'Equals', '*CA'],['Product ID', 'Greater than', 'G110'],['Product', 'Omits'],['Category', 'Not Between', '[', 'Coffee', 'Gifts'])
        :Usage2 : verify_multiple_verify_filter_selection_rows(1,'Step 02 : Verify all filter',['State', 'Equals', '*CA'],['Product ID', 'Greater than', 'G110'])
        ''' 
        row_num=1
        for expected_list in expected_list_arg :
            self.verify_filter_selection_row(popup_index, row_num, expected_list, msg)
            row_num=row_num+1
    
    def verify_filter_values(self,popup_index,row_num,expected_values,msg,**kwargs):
        '''
        :Param : popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : row_num : 1 or 2 (Row number alwasy start from 1) row num is position of condition filed name in filter popup window
        :Param : expected_values=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', '√ Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        :Param : expected_values2=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'] ( expected_values2 should be pass if filter condition is between or Not between )
        :Usage1 : mv_filter.verify_filter_values(1,1,['CA', '√ CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA'],'Step 02 : Verify filter value',expected_values2=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA'],msg2='Step 02 : Verify filter value)
        '''
        table_id=kwargs['table_id'] if 'table_id' in kwargs else 'ITableData0'
        filter_values_type=kwargs['filter_values_type'] if 'filter_values_type' in kwargs else 'small'
        table_index=table_id[-1]
        icon_css="#FiltTable"+str(popup_index)+" .arFilterItem div[id='ftp"+str(popup_index)+"_1_"+str(row_num-1)+"']>div[onclick^='ibiMenu'] img"
        self.driver.find_element_by_css_selector(icon_css).click()
        time.sleep(1)
        if filter_values_type=='small' :
            small_filter_values_css="#dt"+str(table_index)+"_ftp"+str(popup_index)+"_1_"+str(row_num-1)+"_x__0 table>tbody>tr"
            filter_value_elements=self.driver.find_elements_by_css_selector(small_filter_values_css)
            actual_filter_values=[value.text.strip() for value in filter_value_elements]
            #print(actual_filter_values)
            mobile_utillity.UtillityMethods.asequal(self,actual_filter_values,expected_values,msg)
            if 'expected_values2' in kwargs :
                icon_css2="#FiltTable"+str(popup_index)+" .arFilterItem div[id='ftp"+str(popup_index)+"_2_"+str(row_num-1)+"']>div[onclick^='ibiMenu'] img"
                self.driver.find_element_by_css_selector(icon_css2).click()
                time.sleep(2)
                small_filter_values_css2="#dt"+str(table_index)+"_ftp"+str(popup_index)+"_2_"+str(row_num-1)+"_x__0 table>tbody>tr"
                filter_value_elements2=self.driver.find_elements_by_css_selector(small_filter_values_css2)
                actual_filter_values2=[value.text.strip() for value in filter_value_elements2]
                #print(actual_filter_values2)
                mobile_utillity.UtillityMethods.asequal(self,actual_filter_values2,kwargs['expected_values2'],kwargs['msg2'])
        else :
            pass
    
    def verify_filter_buttons(self,filter_popup_index,expected_buttons,msg):
        '''
        :Param : filter_popup_index= 1 or 2 or 3 (index should get from popup id.for example popup id is "#wall1". Now index is 1)
        :Param : expected_buttons =['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All']
        :Usage : verify_filter_buttons(1,['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'],'Step 02.1 : Verify filter buttons')
        ''' 
        btns_css='#wall'+str(filter_popup_index)+' #FiltTable'+str(filter_popup_index)+" .arFilterButton"    
        filter_buttons=self.driver.find_elements_by_css_selector(btns_css)
        buttons=[btn.text.strip() for btn in filter_buttons]
        mobile_utillity.UtillityMethods.asequal(self,buttons,expected_buttons,msg)
        