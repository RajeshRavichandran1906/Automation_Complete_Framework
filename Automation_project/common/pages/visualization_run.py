from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.base import BasePage
import time


class Visualization_Run(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Visualization_Run, self).__init__(driver)

    def _validate_page(self, driver):
#         self.shortwait.until(EC.element_to_be_clickable((BueiCalculationLocators.cancelbtn)))

        ''' Filter Prompt '''
    
    def select_run_menu_options(self, menu_option_button_name=None, parent_css='#MAINTABLE_menuContainer1', toggle_button_click='yes'):
        '''
        Desc: This function is used to click the run menu options buttons.
        
        :param menu_opt: show_report, reset, remove_filter
        Syntax:select_run_menu_option('MAINTABLE_menuContainer1',"reset")
        
        toggle default is yes, if  you want to not to click toggle use toggle="no" as last default param
        :author: Niranjan
        '''
        button_name={'toggle' : 'toggle', 'show_report_css' : 'show', 'reset' : 'reset', 'remove_filter' : 'remove'}
        if toggle_button_click=='yes':
            toggle_button_css=parent_css + " div[onclick*='" + button_name['toggle'] + "'] img"
            self.driver.find_element_by_css_selector(toggle_button_css).click()
        time.sleep(1)
        if menu_option_button_name != None:
            any_button_css = parent_css + " [onclick*='" + button_name[menu_option_button_name] + "'] img"
            self.driver.find_element_by_css_selector(any_button_css).click()
            time.sleep(1)
    
    def create_visualization_tabular_report(self, table_css, file_name):
        '''
        Desc:-This function is used to create ahtml report in run time.
        '''
        utillityobject.create_table_data(self, table_css, file_name)
    
    def verify_visualization_tabular_report(self, table_css, file_name, msg):
        '''
        Desc:-This function is used to verify ahtml report in run time.
        '''
        status = utillityobject.verify_table_data(self, table_css, file_name)
        utillityobject.asequal(self, len(status), 1, msg+ ' Row,Column -'+ str(status))
    
    def create_table_data_set(self,table_css,file_name):
        ''' 
        Desc: This is used to create table data set of a standard html table.   
        @param: table_css= Need to provide the full parent path. means till: table > tbody > tr
        @param: file_name: "test.xlsx" 
        '''
        utillityobject.create_table_data(self, table_css, file_name)
         
    
    def verify_table_data_set(self,table_css,file_name,msg):
        '''
        Desc: This is used to verify table data set of a standard html table.
        @param: table_css= Need to provide the full parent path. means till: table > tbody > tr
        '''
        x= utillityobject.verify_table_data(self, table_css, file_name)
        utillityobject.asequal(self,len(x),1,msg+ ' Row,Column -'+ str(x))
        
                    
    """========================================Old functions==============================================="""              
#Function 32: Change filter prompt values
    def change_filter_prompt_checkBoxValue(self,prompt_num,prompt_value_num,*args):
        """

        :param prompt_num: 1, 2, 3 (1 -> indicates first filter prompt number in "runtime")
               prompt_num: 0, 1, 2 (0 -> indicates first filter prompt number in "preview") 
        :param prompt_value_num: 0 or 1 or 2.. (0 -> incidates first prompt value checkbox, 1 -> incidates second prompt value checkbox in "preview"and "runtime")
        :author: Sindhuja Date: June 01
        """

        if 'preview' in args:
            previewPrompt = self.driver.find_element_by_xpath("//input[@id='checkboxLOBJC20"+prompt_num+"_"+prompt_value_num+"']")
            previewPrompt.click()
        if 'runtime' in args:
            runtimePrompt = self.driver.find_element_by_xpath("//input[contains(@id,'checkboxPROMPT_"+prompt_num+"_"+prompt_value_num+"')]")
            runtimePrompt.click()  
        
# Function 19: Verify Filter Prompt title and values in runtime
    def verification_filter_prompt_runtime(self,promptNum,values, text):
        """
            :param promptNum = filter prompt number (11 -> represents first filter, 22 -> second filter , 33 -> third filter)
            eg: (ia.verification_filter_prompt_runtime("11","Product,Category", "Step 10: Verify Quer Pane"))
            values = Product,Category or Accessories or [All] (filter prompt title and values)
            @author = Sindhuja
            """
        filterPrompt=self.driver.find_element_by_xpath("//div[@id='LOBJPrompt_"+promptNum+"']")
        runtimeFilterPrompt=filterPrompt.text
        utillityobject.asin(self, values, runtimeFilterPrompt, text)
        
        ''' Run Menu Options'''
        
#Function 27 : Click run menu icon and options
    def select_run_menu_option(self, parent_id, menu_opt, toggle='yes'):#Need to delete
        """
        :param menu_opt: show_report, reset, remove_filter
        Syntax:select_run_menu_option('MAINTABLE_menuContainer1',"reset")
        
        toggle default is yes, if  you want to not to click toggle use toggle="no" as last default param
        :author: Niranjan
        """
        toggle_css="#" + parent_id + " div[onclick^='toggle'] img"
        remove_filter_css="#" + parent_id + " span[onclick*='remove'] img"
        reset_css="#" + parent_id + " span[onclick*='reset'] img"
        show_report_css="#" + parent_id + " span[onclick*='show'] img"
        if toggle=='yes':
            self.driver.find_element_by_css_selector(toggle_css).click()
        
        if menu_opt=='show_report':
            self.driver.find_element_by_css_selector(show_report_css).click()
        if menu_opt=='reset':
            self.driver.find_element_by_css_selector(reset_css).click()
        if menu_opt=='remove_filter':
            self.driver.find_element_by_css_selector(remove_filter_css).click()
            
    def verify_visualization_row_column_header_labels(self,parent_id,matrix_type,expected_header,expected_label,msg):
        """
        :param parent_id: MAINTABLE_wbody1
        :param matrix_type: 'Rows' or 'columns'
        :param expected_rowheader: 'Product Category'
        :param expected_rowlabel: ['Hazelnut', 'B141', 'French Roast', 'B142', 'Kona', 'B144', 'Scone', 'F101', 'Biscotti']
        :param msg: "Step 10"
        Usage: verify_matrix_marker_row_header_labels('MAINTABLE_wbody1','Product Category', ['Hazelnut', 'B141', 'French Roast', 'B142', 'Kona', 'B144', 'Scone', 'F101', 'Biscotti'], "Step 04:")
        @author: Niranjan
        """
        actual_val_list=[]
        
        if matrix_type == 'Rows':
            header_css="#" + parent_id + " g.scrollRowTitle"
            label_css="#" + parent_id + " g.scrollRowLbl > g text"
        else:
            header_css="#" + parent_id + " g.scrollColTitle"
            label_css="#" + parent_id + " g.scrollColLbl > g text"

        actual_rowheader=self.driver.find_element_by_css_selector(header_css).text.strip()
        utillityobject.asequal(self, expected_header, actual_rowheader, msg + " Verify Header tile for " + matrix_type)
        actual_val_list.extend([x for x in [el.text.strip() for el in self.driver.find_elements_by_css_selector(label_css)] if x!=''])
        for label_x in expected_label:
            if label_x in actual_val_list:
                state= True
            else:
                state=False
                break
        utillityobject.asequal(self,state, True, msg + " Verify Header labels for " + matrix_type) 