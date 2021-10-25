from common.lib import utillity, core_utility
from common.lib.core_utility import CoreUtillityMethods as coreutil_obj
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
import re, time
from common.lib.global_variables import Global_variables

class Active_Chart_Rollup(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Chart_Rollup, self).__init__(driver)

    def _validate_page(self, driver):
        print("Implement Page Loading wait")
        
    def click_chart_menu_bar_items(self, window_id, item_index):
        """
        :param: window_id='MAINTABLE_wbody1'
        :param: item_index=1 or 2 or 3 or ...
        :Usage click_chart_menu_bar_items(self, 'MAINTABLE_0', 1)
        """
        menu_items_css="#" + window_id + " .arChartMenuBar [onclick]"
        menu_items=self.driver.find_elements_by_css_selector(menu_items_css)
#         menu_items[item_index].click()
        coreutil_obj.python_left_click(self, menu_items[item_index])
        time.sleep(1)
        
    def create_new_item_(self, popup_id, select_path, parent_popup_index=0):
        Active_Chart_Rollup.click_chart_menu_bar_items(self, popup_id, 0)
        op_list=select_path.split('->')
        parent_popup_css = "[id^='dt"+str(parent_popup_index)+"'][style*='block']" 
        iter_count = 0
        for item_name in op_list:
            parent_popup_elements = self.driver.find_elements_by_css_selector(parent_popup_css)
            row_elements = parent_popup_elements[iter_count].find_elements_by_css_selector('table > tbody > tr>td[title="'+item_name+'"]')
            for row_element in row_elements:
                if item_name ==  row_element.text.strip():
                    coreutil_obj.move_to_element(self, row_elements[0], element_location='middle', xoffset=0, yoffset=0, mouse_move_duration=0.5)
                    coreutil_obj.left_click(self, row_element)
            iter_count += 0
            
    def create_new_item(self, chart_no, item_list, verify=False, popup_id='wall1',**kwargs):
        """
        **kwargs should contain 2 variables: 'expected_list', and 'msg'
        Usage: active_chart.create_new_item(0, 'New'), chart_no = first time its 0 , next time it should be 1
        Usage: create_new_item(0, 'New',False,'wall2')   
        ***************************
        Expected_main_menu_list=['New', 'Group By (X)', 'Add (Y)', 'Top', 'Chart/Rollup Tool', 'Restore Original']
        rollobj.create_new_item(0, 'Group By (X)->Product ID', verify_main_menu_list=Expected_main_menu_list, msg="Step 05a: Verify dropdown menu")
        ***************************     
        """
        actual_main_menu=[]
        actual_menu_list=[]
        index=list(popup_id)[-1]
        print(index)
        op_list=item_list.split('->')
        print(op_list)
        if chart_no==0:
            new_parent="0_cpop" + index + "_x__0"
        else:
            print("else part")
            new_parent="0_cpop" + index + "_0"
        print(new_parent)
        Active_Chart_Rollup.click_chart_menu_bar_items(self, popup_id, 0)
        var = "#dt" + new_parent + "  > table > tbody > tr"
        print('Table TR: ', var)
        menus=self.driver.find_elements_by_css_selector("#dt" + new_parent + "  > table > tbody > tr")
        print(len(menus))
        
        if 'verify_main_menu_list' in kwargs:
            for i in range(len(menus)):
                lineObjbj = re.match(r'(\S.*)?.*', menus[i].text.strip())
                actual_main_menu.append(lineObjbj.group(0))
            utillity.UtillityMethods.asequal(self,actual_main_menu, kwargs['verify_main_menu_list'], kwargs['msg']+" Verify dropdown menu")       
            
        for i in range(len(menus)):
            set_item="set" + new_parent + "_" + str(i) + "i_t"
            if self.driver.find_element_by_id(set_item).text == op_list[0]:
                set_item_obj=self.driver.find_element_by_id(set_item)
                coreutil_obj.python_left_click(self, set_item_obj)
#                 utillity.UtillityMethods.default_left_click(self, object_locator=set_item_obj, **kwargs)
                break
        time.sleep(3)
        if len(op_list) > 1:
            new_parent=new_parent + "_" + str(i)
            menus=self.driver.find_elements_by_css_selector("#dt" + new_parent + " span[id^='set']")
            #if self.browser=='Firefox' :
            if Global_variables.browser_name in ['chrome', 'firefox', 'ie', 'edge']:
                utillity.UtillityMethods.click_type_using_pyautogui(self, menus[0],move=True,**kwargs)
            else :
                hov1 = ActionChains(self.driver)
                hov1.move_to_element(menus[0]).perform()
            time.sleep(3) 
            for i in range(len(menus)):
                lineObjbj = re.match(r'(\S.*)?.*', menus[i].text)
                actual_menu_list.append(lineObjbj.group(1))
            position=actual_menu_list.index(op_list[1])
            cur_item_id="set" + new_parent + "_" + str(position) + "i_t"
            cur_item_obj=self.driver.find_element_by_id(cur_item_id)
            coreutil_obj.python_left_click(self, cur_item_obj)
#             utillity.UtillityMethods.default_left_click(self, object_locator=cur_item_obj, **kwargs)
            time.sleep(2)
            if verify==True:
                utillity.UtillityMethods.asequal(self,actual_menu_list, kwargs['expected_list'], kwargs['msg'])
            
    def select_advance_chart(self,popup_id, chart_name, chart_index=0):
        """
        :param: popup_id='wall1'
        :param: chart_name='bar'
        :Usage: select_advance_chart('wall1', 'bar')
        """
        index=list(popup_id)[-1]
        chart_ids={'bar':'chticon_'+index+'_'+str(chart_index)+'_bar1',
                    'stackedbar':'chticon_'+index+'_'+str(chart_index)+'_bar2',
                    'percentbar':'chticon_'+index+'_'+str(chart_index)+'_bar3',
                    'column':'chticon_'+index+'_'+str(chart_index)+'_column',
                    'stackedcolumn':'chticon_'+index+'_'+str(chart_index)+'_column2',
                    'percentcolumn':'chticon_'+index+'_'+str(chart_index)+'_column3',
                    'columndepth':'chticon_'+index+'_'+str(chart_index)+'_column4',
                    'stackeddepth':'chticon_'+index+'_'+str(chart_index)+'_column5',
                    'percentdepth':'chticon_'+index+'_'+str(chart_index)+'_column6',
                    '3Dcolumn':'chticon_'+index+'_'+str(chart_index)+'_bar3d',
                    'piebevel':'chticon_'+index+'_'+str(chart_index)+'_pie',
                    'piewithdepth':'chticon_'+index+'_'+str(chart_index)+'_pie2',
                    'line':'chticon_'+index+'_'+str(chart_index)+'_line',
                    'curvedline':'chticon_'+index+'_'+str(chart_index)+'_line1',
                    'strightline':'chticon_'+index+'_'+str(chart_index)+'_line2',
                    'curvedplusmarkers':'chticon_'+index+'_'+str(chart_index)+'_line3',
                    'strightplusmarkers':'chticon_'+index+'_'+str(chart_index)+'_line4',
                    'stepline':'chticon_'+index+'_'+str(chart_index)+'_line5',
                    'area':'chticon_'+index+'_'+str(chart_index)+'_area',
                    'stackedarea':'chticon_'+index+'_'+str(chart_index)+'_area2',
                    'percentarea':'chticon_'+index+'_'+str(chart_index)+'_area3',
                    'dountcylinder':'chticon_'+index+'_'+str(chart_index)+'_donut',
                    'dountwithDepth':'chticon_'+index+'_'+str(chart_index)+'_donut2',
                    'donutbevel':'chticon_'+index+'_'+str(chart_index)+'_donut3',
                    'scatter(xy_plot)':'chticon_'+index+'_'+str(chart_index)+'_scatter',
                    'bubble':'chticon_'+index+'_'+str(chart_index)+'_bubble',
                    'radarline':'chticon_'+index+'_'+str(chart_index)+'_radar',            
                    'heatmap':'chticon_'+index+'_'+str(chart_index)+'_heatmap',
                    'pyramid':'chticon_'+index+'_'+str(chart_index)+'_pyramid',
                    'funnel':'chticon_'+index+'_'+str(chart_index)+'_funnel',
                    'waterfall':'chticon_'+index+'_'+str(chart_index)+'_waterfall',
                    'histogram':'chticon_'+index+'_'+str(chart_index)+'_histogram',
                    'radarline':'chticon_'+index+'_'+str(chart_index)+'_radar'}

#         self.driver.find_element_by_css_selector("#" + popup_id + " #ttpanel_1_"+index+"_"+str(chart_index)).click()
        time.sleep(1)
        chart_roll_element = self.driver.find_element_by_css_selector("#" + popup_id + " #ttpanel_1_"+index+"_"+str(chart_index))
        coreutil_obj.python_left_click(self, chart_roll_element)
        time.sleep(1)
#         chart_temp_obj=self.driver.find_element_by_id(chart_ids['bar'])
# #         chart_temp_obj.click()
#         coreutil_obj.python_left_click(self, chart_temp_obj)
#         time.sleep(1)
        chart_elem = self.driver.find_element_by_id(chart_ids[chart_name])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", chart_elem)
        chart_elem.click()
#         coreutil_obj.python_left_click(self, chart_elem)
        time.sleep(3)
        ok_element = self.driver.find_element_by_css_selector("#" + popup_id + " td[onclick*=dochart]")
#         self.driver.execute_script("arguments[0].click();", ok_element)
        ok_element.click()
#         coreutil_obj.python_left_click(self, ok_element)
        time.sleep(1)
        
    def verify_arChartMenu(self,window_id,msg):
        """
        :param self: Current object 
        :param window_id: wall1 or wall2 
        :param menus: default value is ['', 'Column']
        :return: 
        """
        menus=['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart','Aggregation']
        css= "#"+window_id+" .arChartMenuBarContainer div[title]"
        actual = []
        elm = self.driver.find_elements_by_css_selector(css)
        for x in range(0,len(elm)):
            actual.append(elm[x].get_attribute("title"))
        actual.append(self.driver.find_element_by_css_selector("#"+window_id+" #SUM_"+window_id[-1]+" [title]").get_attribute("title"))
        utillity.UtillityMethods.asequal(self,menus, actual, msg)
        s = self.driver.find_element_by_css_selector("#"+window_id+" #LINKIMG"+window_id[-1]+"_-1").is_displayed()
        utillity.UtillityMethods.asequal(self,True, s, msg+ "Freeze icon")
        
    def click_pivot_menu_bar_items(self, popup_id, item_index):
        """
        Syntax: click_pivot_menu_bar_items('wall1', 2)
        @author = Niranjan 
        """
        
        menu_items_css="#" + popup_id + " .arChartMenuBar img"
        menu_items=self.driver.find_elements_by_css_selector(menu_items_css)
        utillity.UtillityMethods.default_click(self, menu_items[item_index], click_option=0)
        time.sleep(2)

    def select_chartmenubar_option(self, popup_id, popup_instance, item_list, elem_index=9, **kwargs):
        """ 
        Usage:  select_chartmenubar_option('wall1', 0, 'Avg')
                select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->DEALER_COST', 0, custom_css='cpop')
                select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->DEALER_COST', 0, custom_css='cpop', verify=True, expected_list=['Unit Sales', 'Dollar Sales'])
                select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->DEALER_COST', 0, custom_css='cpop', checked_list_item=['Unit Sales', 'Dollar Sales'])
                select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->DEALER_COST', 0, custom_css='cpop', verify=True, expected_list=['Unit Sales', 'Dollar Sales'],
                                            checked_list_item=['Unit Sales', 'Dollar Sales'])
        """
        op_list=item_list.split('->')
        custom_css=kwargs['custom_css'] if 'custom_css' in kwargs else "SUM_"
        Active_Chart_Rollup.click_pivot_menu_bar_items(self, popup_id, elem_index)
        if popup_instance==0:
            parent_css="0_"+custom_css+"'][id$='_x__0'][style*='block'] > table"
        else:
            parent_css="0_"+custom_css+"'][id$='_0'][style*='block'] > table"
        x=self.driver.find_elements_by_css_selector("[id^='dt" + parent_css + " span[id ^='set']")
        for i in range(len(x)):
            if op_list[0]=='':
                break
            if x[i].text == op_list[0]:
                utillity.UtillityMethods.click_on_screen(self, x[i], 'middle', click_type=0, **kwargs)
                break
        time.sleep(1)
        if len(op_list) > 1:
            if popup_instance==0:
#                 new_parent="0_"+custom_css+"'][id$='_x__0_" + str(i) + "'][style*='block'] "
                new_parent="0_"+custom_css+"'][style*='block']"
            else:
#                 new_parent="0_"+custom_css+"'][id$='_0_" + str(i) + "'][style*='block']"
                new_parent="0_"+custom_css+"'][style*='block']"
            new_css="[id^='dt" + parent_css + " div[id^='dt" + new_parent + " span[id^='set']"
            menus=self.driver.find_elements_by_css_selector(new_css)
            for i in range(len(menus)):
                if menus[i].text == op_list[1]:                    
                    utillity.UtillityMethods.click_type_using_pyautogui(self, obj_locator=menus[0])
                    time.sleep(2)
                    utillity.UtillityMethods.default_left_click(self, object_locator=menus[i], **kwargs)
                    break
            time.sleep(2)
        if 'verify' in kwargs:
            if op_list[0]=='':
                new_parent = parent_css
            elif popup_instance==0:
                new_parent="0_"+custom_css+"'][id$='_x__0_" + str(i) + "'][style*='block']"
            else:
                new_parent="0_"+custom_css+"'][id$='_0_" + str(i) + "'][style*='block']"
            menus=self.driver.find_elements_by_css_selector("[id^='dt" + new_parent + " span[id^='set']")
            actual_list=[]
            for i in range(len(menus)):
                if menus[i].is_displayed():
                    actual_list.append(menus[i].text)
            utillity.UtillityMethods.asequal(self, actual_list, kwargs['expected_list'],kwargs['msg']+" Verify menulist")
        if 'checked_list_item' in kwargs:
            if popup_instance==0:
                new_parent="0_"+custom_css+"'][id$='_x__0_" + str(i) + "'][style*='block']"
            else:
                new_parent="0_"+custom_css+"'][id$='_0_" + str(i) + "'][style*='block']"
            menus_checked_elem=self.driver.find_elements_by_css_selector("[id^='dt" + new_parent + " [id^='t0_"+custom_css+"']")
            actual_checked_list=[]
            for el in menus_checked_elem:
                try:
                    el.find_element_by_css_selector("td:nth-child(1) span[style*='symbol']")
                    actual_checked_list.append(el.find_element_by_css_selector("td:nth-child(2)").text.strip())
                except:
                    pass
            utillity.UtillityMethods.asequal(self, actual_checked_list, kwargs['checked_list_item'],kwargs['msg']+" Verify menulist")
    
    def select_aggregate_function(self, popup_id, popup_instance, function_name, elem_index=9, verify=True, **kwargs):
        """
        Syntax: select_aggregate_function('wall1', 0, 'Avg')
        Syntax: select_aggregate_function('wall1', 1, 'Avg')
        Params: popup_instance :- If you are invoking this function freshly then use 0, else nonzero.
        @author = Niranjan 
        """
        Active_Chart_Rollup.select_chartmenubar_option(self, popup_id, popup_instance, function_name, elem_index, **kwargs)
        selected_function_css="#" + popup_id + " .arChartMenuBar [id^='SUM_']"
        actual_function_name=self.driver.find_element_by_css_selector(selected_function_css).text.strip()
        if verify==True:
            utillity.UtillityMethods.asequal(self, function_name, actual_function_name, "Step X: Verify " + function_name + " is displaying now.")
        else:
            utillity.UtillityMethods.as_not_equal(self, function_name, actual_function_name, "Step X: Verify " + function_name + " is not displaying.")
            
    def verify_advanced_chart_items(self, item_list, comparison_type, msg):
        """
        Description: This function is used to verify chart items in the advanced chart menu, it has options 
                    to compare asin, asnotin and asequal
        usage: verify_advanced_chart_items(['Bar'], 'asin', 'Step 3.1: Verify bar under the advanced chart menu') 
        """
        items_css = "#wall1 div[id^='chticon'] svg text[class='title']"
        elements =utillity.UtillityMethods.validate_and_get_webdriver_objects(self, items_css, "advanced_menu_items")
        observed_items_text = [element.text.strip() for element in elements]
        if comparison_type == 'asin':
            for item in item_list:
                utillity.UtillityMethods.asin(self, item, observed_items_text,  msg+" displays "+item)
        elif comparison_type=='asnotin':
            for item in item_list:
                utillity.UtillityMethods.as_notin(self, item, observed_items_text, msg+" doesn't display "+item)
        else:
            utillity.UtillityMethods.as_List_equal(self, item_list, observed_items_text, msg)
        
    def click_chart_rollup_tool_items(self, tab_name):
        """
        Description: Click the item in the chart rollup menubar
        usage: click_chart_rollup_tool_items('Charts')
        """
        items_css = "#charttoolt1 [id^='ttpanel_']"
        elements = utillity.UtillityMethods.validate_and_get_webdriver_objects(self, items_css, 'menu_items')
        for element in elements:
            if element.text.strip() == tab_name:
                core_utility.CoreUtillityMethods.python_left_click(self, element)