from common.lib import utillity
from common.lib.base import BasePage
from common.locators.visualization_metadata_locators import VisualizationMetadataLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import re
import time


class Active_Tools(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Active_Tools, self).__init__(driver)

    def _validate_page(self, driver):
        print("Implement Page Loading wait")
        
    def pivot_tool_drag_drop_items(self, table_id, from_column, item_name, item_position, to_column, to_row_num, **kwargs):
        """
        Params: table_id='pivottoolt1'
        Params: from_column='Columns' or 'Group By' or 'Across' or 'Measure'
        Params: item_name='State'
        Params: item_position=1,2.. (represents no. of duplicates, if same column twice then 2)
        Params: to_column='Group By' or 'Across' or 'Measure'
        Params: to_row_num=0,1..(0 when Drag Column Here is there)
        Syntax: pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'State', 1, 'Group By', 0)
        Syntax: pivot_tool_drag_drop_items('gridtoolt1', 'Column Order', 'D10.2 Unit Price', 1, 'Column Order', 1)
        @Author: Nasir 
        """
        if from_column == 'Columns' or from_column == 'Column Order':
            fcol=1
        elif from_column == 'Group By':
            fcol=2
        elif from_column == 'Across':
            fcol=3
        elif from_column == 'Measure':
            fcol=4
        else:
            print("Specified " + from_column + " does not exist")
        strcolumn_name = "//*[@id='" + table_id + "']/tbody/tr[1]/td[" + str(fcol) + "]//div[normalize-space(text())='" + item_name + "']"
        pos = item_position-1

        # **** To drag the column name on the specified column ***
        strcolumn_name_pos = self.driver.find_elements_by_xpath(strcolumn_name)
        draggable = strcolumn_name_pos[pos]

        # **** To drop the column name on the specified column ***
        if to_column == 'Group By':
            tcol=2
            trow_id = 'ptg_0_'
        elif to_column == 'Across':
            tcol=3
            trow_id = 'pta_0_'
        elif to_column == 'Measure':
            tcol=4
            trow_id = 'ptm_0_'
        elif to_column == 'Column Order':
            tcol=1
            trow_id='gtc_0_'
        else:
            print("Specified " + to_column + " does not exist")

        # verifying the row
        if to_row_num == 0:
            destination_elem = "//*[@id='" + table_id + "']/tbody/tr[1]/td[" + str(tcol) + "]//span[text()[contains(.,'Drag Column Here')]]"
            droppable = self.driver.find_element_by_xpath(destination_elem)
        else:
            destination_elem = "#" + table_id + " > tbody > tr:nth-child(1) > td:nth-child(" + str(tcol) + ") td[id='" + trow_id + str(to_row_num) + "_2']"
            droppable = self.driver.find_element_by_css_selector(destination_elem)
        if self.browser == 'Firefox':
            if 'browser_height' in kwargs:
                utillity.UtillityMethods.drag_to_using_pyautogui(self, draggable, droppable, kwargs['sx_offset'], kwargs['sy_offset'], kwargs['tx_offset'], kwargs['ty_offset'], browser_height=kwargs['browser_height'])
            else:
                utillity.UtillityMethods.drag_to_using_pyautogui(self, draggable, droppable, 0, -7, 0, -7)
        else:
            dragdrop = ActionChains(self.driver).drag_and_drop(draggable, droppable)
            dragdrop.perform()
        time.sleep(2)
        

    def pivot_tool_close(self, table_id, btn_type):
        """
        Params: table_id='pivottoolt1'
        Params: btn_type='Ok' or 'Cancel'
        Syntax: pivot_tool_close('pivottoolt1', 'Ok')
        @Author: Nasir 
        """
        # **** To check the buttons Ok/Cancel ***
        if btn_type == 'Ok':
            Ok_btn = "#" + table_id + " > tbody > tr:nth-child(2) td[onclick*='Pt_dopivot']"
            self.driver.find_element_by_css_selector(Ok_btn).click()
        elif btn_type == 'Cancel':
            Cancel_btn = "#" + table_id + " > tbody > tr:nth-child(2) td[onclick*='closewin']"
            self.driver.find_element_by_css_selector(Cancel_btn).click()
        else:
            print("Specified " + btn_type + " does not exist")
        time.sleep(2)

    def grid_tool_select_aggregate_function(self, table_id, item_name, item_position, function_name, **kwargs):
        """
        Params: table_id='gridtoolt1'
        Params: item_name='State'
        Params: item_position=1,2..
        Params: function_name='Avg' or 'Sum' or 'Count'
        params: expected_aggregation_list=['Avg', 'Sum', 'Count']
        Syntax: grid_tool_select_aggregate_function('gridtoolt1', 'State', 1, 'Avg')
        Syntax: grid_tool_select_aggregate_function('gridtoolt1', 'State', 1, 'Avg', ['Avg', 'Sum', 'Count'])
        @Author: Nasir & Niranjan
        """
        pos = item_position-1
        strcolumn_name = "//*[@id='" + table_id + "']/tbody/tr[1]/td[1]//div[normalize-space(text())='" + item_name + "']"
        strcolumn_sum = strcolumn_name + "/../../child::td//div[@title='Select Calculation Type']"
        strcolumn_sum_pos = self.driver.find_elements_by_xpath(strcolumn_sum)
        strid = strcolumn_sum_pos[pos].get_attribute("id")
        strmenu_id = "dt0_" + strid + "_x__0"    
        strcolumn_sum_pos[pos].click()
        time.sleep(1)
        if 'expected_aggregation_list' in kwargs:
            actual_aggregation_list=[]
            aggregation_list=self.driver.find_elements_by_css_selector("#" + strmenu_id + " tr")
            for fun in aggregation_list:
                actual_aggregation_list.append(fun.text.strip())
            utillity.UtillityMethods.asequal(self, kwargs['expected_aggregation_list'], actual_aggregation_list, "Step X : Verify the list.")
        func_name=self.driver.find_element_by_xpath("//*[@id='" + strmenu_id + "']//span[text()[contains(.,'" + function_name + "')]]")
        if self.browser=='Firefox':
            if 'browser_height' in kwargs:
                utillity.UtillityMethods.click_type_using_pyautogui(self, func_name, kwargs['x_offset'], kwargs['y_offset'], browser_height=kwargs['browser_height'],leftClick=True)
            else:
                utillity.UtillityMethods.click_type_using_pyautogui(self, func_name,0,-7, leftClick=True)
        else:
            func_name.click()
        time.sleep(2)
        selected_aggregation_xpath = "//*[@id='" + table_id + "']/tbody/tr[1]/td[1]//div[normalize-space(text())='" + item_name + "']/../../td[3]"
        actual_aggregation_value=self.driver.find_element_by_xpath(selected_aggregation_xpath).text
        utillity.UtillityMethods.asequal(self, function_name, actual_aggregation_value, "Step X : Verify the aggregation " + function_name + " value sected.")
    
    def grid_tool_drag_drop_items(self, table_id, item_name, item_occurrence, to_row_num, **kwargs):
        """
        Params: table_id='gridtoolt1'
        Params: item_name='State'
        Params: item_position=1,2..
        Params: to_row_num=0,1..
        Syntax: grid_tool_drag_drop_items('gridtoolt1', 'State', 1, 0)
        @Author: Nasir 
        """
        pos = item_occurrence-1
        strcolumn_name = "//*[@id='" + table_id + "']/tbody/tr[1]/td[1]//div[normalize-space(text())='" + item_name + "']"

        strcolumn_name_pos = self.driver.find_elements_by_xpath(strcolumn_name)
        draggable = strcolumn_name_pos[pos]
        if to_row_num == 0:
            destination_elem = "//*[@id='gridtoolt1']/tbody/tr[1]/td[2]//span[text()[contains(.,'Drag Column Here')]]"
            droppable = self.driver.find_element_by_xpath(destination_elem)
        else:
            destination_elem = "#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) td[id='gts_0_" + str(to_row_num) + "_2']"
            droppable = self.driver.find_element_by_css_selector(destination_elem)
        if self.browser == 'Firefox':
            if 'browser_height' in kwargs:
                utillity.UtillityMethods.drag_to_using_pyautogui(self, draggable, droppable, kwargs['sx_offset'], kwargs['sy_offset'], kwargs['tx_offset'], kwargs['ty_offset'], browser_height=kwargs['browser_height'])
            else:
                utillity.UtillityMethods.drag_to_using_pyautogui(self, draggable, droppable, 0, -7, 0, -7)
        else:
            dragdrop = ActionChains(self.driver).drag_and_drop(draggable, droppable)
            dragdrop.perform()
        time.sleep(2)

    def grid_tool_select_group_checkbox(self, table_id):
        """
        Params: table_id='gridtoolt1'
        Syntax: grid_tool_select_group_checkbox('gridtoolt1')
        @Author: Nasir 
        """
        checkbox = "#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) div[onclick*='toggleSortGroup']"
        self.driver.find_element_by_css_selector(checkbox).click()
        time.sleep(1)
        
    def grid_tool_close(self, table_id, btn_type):
        """
        Params: table_id='gridtoolt1'
        Params: btn_type='Ok' or 'Cancel'
        Syntax: grid_tool_close('gridtoolt1', 'Ok')
        @Author: Nasir 
        """
        # **** To check the buttons Ok/Cancel ***
        if btn_type == 'Ok':
            Ok_btn = "#" + table_id + " > tbody > tr:nth-child(2) td[onclick*='Gt_dogrid']"
            self.driver.find_element_by_css_selector(Ok_btn).click()
        elif btn_type == 'Cancel':
            Cancel_btn = "#" + table_id + " > tbody > tr:nth-child(2) td[onclick*='closewin']"
            self.driver.find_element_by_css_selector(Cancel_btn).click()
        else:
            print("Specified " + btn_type + " does not exist")
        time.sleep(2)

    def pivot_tool_verify_columns(self, table_id, colnum, expected_list, msg):
        """
        Params: table_id='pivottoolt1'
        Params: colnum=1,2,3,4
        Params: expected_list=['Columns', 'Region', 'Category', 'Dollar Sales', 'Unit Sales'] OR ['Across', 'Drag Column Here'], OR ['Measure', 'Sum:', 'Dollar Sales']
        Syntax: pivot_tool_verify_columns('pivottoolt1', 1,['Columns', 'Region', 'Category', 'Dollar Sales', 'Unit Sales'], 'Step 10: xxxx')
        @Author: Niranjan 
        """
        col_css="table[id='" + table_id + "'] >  tbody > tr:nth-child(1) > td:nth-child(" + str(colnum) + ")"
        actual_list=[el.strip() for el in self.driver.find_element_by_css_selector(col_css).text.split("\n") if bool(re.match('\S', el))]
        utillity.UtillityMethods.asequal(self, expected_list, actual_list, msg)
    
    def pivot_tool_delete_column_items(self, table_id, colnum, delete_btn_index):
        """
        Params: table_id='pivottoolt1'
        Params: colnum=1,2,3,4
        Params: delete_btn_index=0,1,2...
        Syntax: pivot_tool_delete_column_items('pivottoolt1', 4,0)
        @Author: Niranjan 
        """
        delete_css="table[id='" + table_id + "'] >  tbody > tr:nth-child(1) > td:nth-child(" + str(colnum) + ") div[title='Delete']"
        delete_btns=self.driver.find_elements_by_css_selector(delete_css)
        delete_btns[delete_btn_index].click()
        time.sleep(1)
 
    def grid_tool_show_hide_column(self, table_id, item_name, item_index, change_hide):
        """
        Params: table_id='gridtoolt1'
        Params: item_name='SEATS'
        Params: item_position=1,2..
        Params: change_hide='Hide Column' or 'Show Column'
        Syntax: grid_tool_select_change_hide_column('gridtoolt1', 'SEATS', 1, 'Hide Column')
        @Author: Nasir 
        """
        pos = item_index-1
        strcolumn_name = "//*[@id='" + table_id + "']/tbody/tr[1]/td[1]//div[normalize-space(text())='" + item_name + "']"
        strcolumn_column = strcolumn_name + "/../../child::td//div[@title='" + change_hide + "']"
        strcolumn_sum_pos = self.driver.find_elements_by_xpath(strcolumn_column)
        strcolumn_sum_pos[pos].click()

    def verify_grid_tool_show_hide_column(self, table_id, item_name, item_index, change_show_hide,msg):
        """
        Params: table_id='gridtoolt1'
        Params: item_name='SEATS'
        Params: item_position=1,2..
        Params: change_show_hide='Hide Column' or 'Show Column'
        Syntax: verify_grid_tool_show_hide_column('gridtoolt1', 'Unit Sales',1,'Show Column', "Step 03: Verify that Unit Sales is checked")
        verify_grid_tool_show_hide_column('gridtoolt1', 'Unit Sales',1,'Hide Column', "Step 06: Verify that Unit Sales is unchecked")
        @Author: Sindhuja 
        """
        pos = item_index-1
        strcolumn_name = "//*[@id='" + table_id + "']/tbody/tr[1]/td[1]//div[normalize-space(text())='" + item_name + "']"
        strcolumn_column = strcolumn_name + "/../../child::td//div[@title='" + change_show_hide + "']"
        strcolumn_sum_pos = self.driver.find_elements_by_xpath(strcolumn_column)
        try: 
            value=strcolumn_sum_pos[pos].is_displayed()
            utillity.UtillityMethods.asequal(self,True,value,msg)
        except NoSuchElementException:
            value=False
            utillity.UtillityMethods.asequal(self,True,value,msg)
        
        
        
    def grid_tool_delete_item(self, table_id, rownum):
        """
        Params: table_id='gridtoolt1'
        Params: rownum=1,2..
        Syntax: grid_tool_delete_item('gridtoolt1', 2)
        @Author: Niranjan 
        """
        delete_css="#" + table_id + " > tbody > tr:nth-child(1) > td:nth-child(2) div[title='Delete']"
        delete_btns=self.driver.find_elements_by_css_selector(delete_css)
        delete_btns[rownum-1].click()
        time.sleep(1)

    def grid_tool_sort_item(self, rownum):
        """
        Params: table_id='gridtoolt1'
        Params: rownum=1,2..
        Syntax: grid_tool_sort_item('gridtoolt1', 2)
        @Author: Niranjan 
        """
        sort_css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) div[title='Select Sort Order']" 
        sort_btns=self.driver.find_elements_by_css_selector(sort_css)
        sort_btns[rownum-1].click()
        time.sleep(1)   
        
    def grid_tool_verify_columns(self, table_id, colnum, expected_list, msg):
        """
        Params: table_id='gridtoolt1'
        Params: colnum=1,2
        Params: expected_list=['Columns', 'Region', 'Category', 'Dollar Sales', 'Unit Sales'] OR ['Across', 'Drag Column Here'], OR ['Measure', 'Sum:', 'Dollar Sales']
        Syntax: grid_tool_verify_columns('gridtoolt1', 2, ['Sort Order', 'Region', 'Category', 'Dollar Sales', 'Unit Sales'], 'Step 10: xxxx')
        @Author: Niranjan 
        """
        col_css="table[id='" + table_id + "'] >  tbody > tr:nth-child(1) > td:nth-child(" + str(colnum) + ")"
        actual_list=(self.driver.find_element_by_css_selector(col_css).text).split('\n')
        utillity.UtillityMethods.asequal(self, expected_list, actual_list, msg)
        
    def chart_rollup_tool_drag_drop_items(self, table_id, from_column, item_name, item_position, to_column, to_row_num, **kwargs):
        """
        Params: table_id='charttoolt1'
        Params: from_column='Columns' or 'Group By' or 'Across' or 'Measure'
        Params: item_name='State'
        Params: item_position=1,2..
        Params: to_column='Group By' or 'Across' or 'Measure'
        Params: to_row_num=0,1..
        Syntax: toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Category', 1, 'Group By', 0)
        Syntax: toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)
        Syntax: pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'State', 1, 'Group By', 0)
        @Author: Nasir 
        """
        if from_column == 'Columns':
            fcol=1
        elif from_column == 'Group By':
            fcol=2
#         elif from_column == 'Across':
#             fcol=3
        elif from_column == 'Measure':
            fcol=3
        else:
            print("Specified " + from_column + " does not exist")
        strcolumn_name = "//*[@id='" + table_id + "']//tbody/tr[1]/td[" + str(fcol) + "]//div[normalize-space(text())='" + item_name + "']"
        pos = item_position-1

        # **** To drag the column name on the specified column ***
        strcolumn_name_pos = self.driver.find_elements_by_xpath(strcolumn_name)
        draggable = strcolumn_name_pos[pos]

        # **** To drop the column name on the specified column ***
        if to_column == 'Group By':
            tcol=2
            trow_id = 'ctg_0_'
#         elif to_column == 'Across':
#             tcol=3
#             trow_id = 'pta_0_'
        elif to_column == 'Measure':
            tcol=3
            trow_id = 'ctm_0_'
        else:
            print("Specified " + to_column + " does not exist")

        # verifying the row
        if to_row_num == 0:
            destination_elem = "//*[@id='" + table_id + "']//tbody/tr[1]/td[" + str(tcol) + "]//span[text()[contains(.,'Drag Column Here')]]"
            droppable = self.driver.find_element_by_xpath(destination_elem)
        else:
            destination_elem = "#" + table_id + " tbody > tr:nth-child(1) > td:nth-child(" + str(tcol) + ") td[id='" + trow_id + str(to_row_num) + "_2']"
            droppable = self.driver.find_element_by_css_selector(destination_elem)
        if self.browser == 'Firefox':
            if 'browser_height' in kwargs:
                utillity.UtillityMethods.drag_to_using_pyautogui(self, draggable, droppable, kwargs['sx_offset'], kwargs['sy_offset'], kwargs['tx_offset'], kwargs['ty_offset'], browser_height=kwargs['browser_height'])
            else:
                utillity.UtillityMethods.drag_to_using_pyautogui(self, draggable, droppable, 0, -12, 0, -12)
        else:
            dragdrop = ActionChains(self.driver).drag_and_drop(draggable, droppable)
            dragdrop.perform()
        time.sleep(2)
        
    def chart_rollup_tool_verify_columns(self, table_id, panel_id,colnum, expected_list, msg):
        """
        Params: table_id='charttoolt1'
        Params: panel_id='tpanel_0_1_0'
        Params: colnum=1,2,3
        Params: expected_list=['Columns', 'Region', 'Category', 'Dollar Sales', 'Unit Sales'] OR ['Across', 'Drag Column Here'], OR ['Measure', 'Sum:', 'Dollar Sales']
        Syntax: pivot_tool_verify_columns('pivottoolt1', 1,['Columns', 'Region', 'Category', 'Dollar Sales', 'Unit Sales'], 'Step 10: xxxx')
        @Author: Niranjan 
        """
        col_css="#"+table_id+" #"+panel_id+" > table > tbody > tr > td:nth-child(" + str(colnum) + ")"
        actual_list=[el.strip() for el in self.driver.find_element_by_css_selector(col_css).text.split("\n") if bool(re.match('\S', el))]
        utillity.UtillityMethods.asequal(self, expected_list, actual_list, msg)
        
    def chart_rollup_tool_delete_column_items(self, table_id, colnum, delete_btn_index):
        """
        Params: table_id='charttoolt1'
        Params: colnum=1,2,3
        Params: delete_btn_index=0,1,2...
        Syntax: chart_rollup_tool_delete_column_items('charttoolt1',3,0)
        @Author: Niranjan 
        """
        delete_css="table[id='" + table_id + "'] tbody > tr:nth-child(1) > td:nth-child(" + str(colnum) + ") div[title='Delete']"
        delete_btns=self.driver.find_elements_by_css_selector(delete_css)
        delete_btns[delete_btn_index].click()
        time.sleep(1)
        
    def chart_rollup_tool_close(self, table_id, btn_type):
        """
        Params: table_id='charttoolt1'
        Params: btn_type='Ok' or 'Cancel'
        Syntax: chart_rollup_tool_close('charttoolt1', 'Ok')
        @Author: Nasir 
        """
        # **** To check the buttons Ok/Cancel ***
        if btn_type == 'Ok':
            Ok_btn = "#" + table_id + " > tbody > tr:nth-child(2) td[onclick*='Ct_dochart']"
            self.driver.find_element_by_css_selector(Ok_btn).click()
        elif btn_type == 'Cancel':
            Cancel_btn = "#" + table_id + " > tbody > tr:nth-child(2) td[onclick*='closewin']"
            self.driver.find_element_by_css_selector(Cancel_btn).click()
        else:
            print("Specified " + btn_type + " does not exist")
        time.sleep(2)
        
