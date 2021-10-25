'''
Created on Aug 31, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050538
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, active_tools, visualization_resultarea
from common.lib import utillity
import unittest
import time, re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class C2050538_TestClass(BaseTestCase):

    def test_C2050538(self):
        
        """Test case variables"""
        country_field='[id="popid0_0"]'
        car_field = '[id="popid0_1"]'
        model_field='[id="popid0_2"]'
        retail_cost_field='[id="popid0_3"]'
        dealer_cost_field='[id="popid0_4"]'
        sales_filed='[id="popid0_5"]'
        columns1=['COUNTRY','CAR','MODEL','RETAIL_COST','DEALER_COST','SALES']
        HTML_column=['COUNTRY','CAR','MODEL','RETAIL_COST','DEALER_COST','SALES']
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj=active_filter_selection.Active_Filter_Selection(self.driver)
        toolsobj = active_tools.Active_Tools(self.driver)
        result_obj=visualization_resultarea.Visualization_Resultarea(self.driver)
        
        def report_checkpoint(msg):
            miscelanousobj.verify_page_summary(1, '10of10records,Page1of1', msg + ".a: Verify the Run Report Heading")
            column_list=['CAR', 'RETAIL_COST']
            miscelanousobj.verify_column_heading('ITableData1', column_list, msg + ".b: Verify the Run Report column heading")
#             utillobj.create_data_set('ITableData1','I1r','C2050538_Ds10.xlsx')
            utillobj.verify_data_set('ITableData1','I1r','C2050538_Ds10.xlsx', msg + ".c: Verify entire Data set in Run Report on Page 1") 
            time.sleep(2)
        def verify_tabs(tabs_text,msg):
            otab_val=driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr").text
            ocheck=otab_val.strip().split("\n")==tabs_text
            utillity.UtillityMethods.asequal(self,True, ocheck, msg + ": verifying Report and Chart Tabs displayed on top of the Run Report")
        
#             
        """
            Step 01: Execute the AR-RP-219.fex
        """
           
            
        utillobj.active_run_fex_api_login("AR-RP-219.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the AR-RP-219.fex and verify page summary")
        columns=['COUNTRY','CAR','MODEL','RETAIL_COST','DEALER_COST','SALES']
        miscelanousobj.verify_column_heading("ITableData0", columns, 'Step 01.2: Verify all columns listed on the report AR-RP-219.fex')
#         utillobj.create_data_set('ITableData0','I0r','AR-RP-219.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 01.3: Verify AR-RP-219.fex data', desired_no_of_rows=5)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,car_field).click()
                 
        try:
            value = ""
            prompt = self.driver.find_element(By.CSS_SELECTOR,'[id="popid0_1"]').text
               
        except NoSuchElementException:
            prompt=False
        utillobj.asequal(value,prompt,"Step 01.4: Expect to see no options appear") 
           
        utillobj.infoassist_api_logout()
          
                 
        """
        Step 02: Execute Fex AR-RP-219a. CALC option functionality test.
        Select the Country field and click the Active drop-down arrow.
        Select Count Distinct for the CALC option to make sure the functionality is available.
        """
        utillobj.active_run_fex_api_login("AR-RP-219a.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
          
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
          
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 02: Execute the AR-RP-219a.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 02.1: Verify all columns listed on the report AR-RP-219a.fex')
            
        self.driver.find_element(By.CSS_SELECTOR,country_field).click()
                
        try:
            calc=self.driver.find_element(By.CSS_SELECTOR,'#set0_0_0_0i_t').text
        except NoSuchElementException:
            calc=False
        utillobj.asequal('Calculate',calc,"Step 02.2: Expect to see only the CALC option appear when the Country field drop-down arrow is selected")     
        miscelanousobj.select_menu_items('ITableData0', 0, 'Calculate','Count')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        utillobj.synchronize_with_visble_text(parent_css, 'TotalCnt18', 30, 1)
         
          
        miscelanousobj.verify_calculated_value(2, 1, 'Total Cnt 18', True, 'Step 02.3: Expect to see a Count Distinct value for Country')
          
        utillobj.infoassist_api_logout()
          
              
             
        """
        Step 03: Execute Fex AR-RP-219b. CHART option functionality test.
        Select the Retail_Cost field and click the Active drop-down arrow.
        Select Pie for the chart and CAR for the Group By field.
        """
        utillobj.active_run_fex_api_login("AR-RP-219b.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 03.1: Execute the AR-RP-219b.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 03.2: Verify all columns listed on the report AR-RP-219b.fex')
         
        self.driver.find_element(By.CSS_SELECTOR,retail_cost_field).click()
        chart_option=False
         
        temp_str_value=driver.find_element_by_css_selector("#pt0_3_0 #dt0_3_0 table").text.strip().replace(' ','').split('\n')
        if 'Chart' in temp_str_value:
            chart_option=True
        utillobj.asequal(True ,chart_option,"Step 03.3: Expect to see only the CHART option appear when the Retail_Cost field drop-down arrow is selected")
              
        miscelanousobj.select_menu_items('ITableData0', 3, 'Chart','Pie','CAR')
        parent_css="[id^='wall1'] td[class*='arWindowBar']"
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COSTBYCAR', 30, 1)
         
         
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2050538_Actual_Step03', image_type='actual')
         
        miscelanousobj.verify_active_popup_chart_tooltip('wall1', 'pie', 'BMW', 'BMW=58762(33.9%)', 'deep_magenta', 'Step 03.4: Verify tooltip and color')
         
        utillobj.infoassist_api_logout()
         
                  
        """
        Step 04: Execute Fex AR-RP-219c. COMMENTS option functionality test.
        Select the Car field and click the Active drop-down arrow.
        Select the Expand option.
        Select Car and Expand again.
        """
        utillobj.active_run_fex_api_login("AR-RP-219c.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 04.1: Execute the AR-RP-219c.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 04.2: Verify all columns listed on the report AR-RP-219c.fex')
         
        self.driver.find_element(By.CSS_SELECTOR,car_field).click()
         
        try:
            chart_option=self.driver.find_element(By.CSS_SELECTOR,'#set0_1_0_1i_t').text
        except NoSuchElementException:
            chart_option=False
        utillobj.asequal('Comments',chart_option,"Step 04.3: Expect to see only the COMMENTS option appear when the Car field drop-down arrow is selected")
         
        expected_menu_list = ['Expand','Hide Indicator']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Comments', expected_menu_list, 'Step 04.4: Expect to see the Expand option appear.')
         
        miscelanousobj.select_menu_items('ITableData0', 1, 'Comments','Expand')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,car_field).click()
 
        self.driver.find_element(By.CSS_SELECTOR,'#set0_1_0_1i_t').click()
 
        selected = self.driver.find_element(By.XPATH,"//td[@id='et0_1_0_1_0i_t']/span/span").text
        status=False
        if ord(selected)== 8730 or 214:
            status=True
        else:
            status=False
        utillobj.asequal(status,True,"'Step 04.5: Expect top see the Expand option with the selection tag")
 
        utillobj.infoassist_api_logout()
 
              
        """
        Step 05: Execute Fex AR-RP-219d. EXPORT option functionality test.
        Select the Model field and click the Active drop-down arrow.
        Select HTML for the output and ALL RECORDS.
        """
              
        utillobj.active_run_fex_api_login("AR-RP-219d.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
 
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
 
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 05.1: Execute the AR-RP-219d.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 05.2: Verify all columns listed on the report AR-RP-219d.fex')
 
        self.driver.find_element(By.CSS_SELECTOR,model_field).click()
 
        try:
            export=self.driver.find_element(By.CSS_SELECTOR,'#set0_2_0_1i_t').text
        except NoSuchElementException:
            export=False
        utillobj.asequal('Export',export,'Step 05.3: Expect to see only the EXPORT option appear when the MODEL field drop-down arrow is selected')
        time.sleep(3)
        miscelanousobj.verify_menu_items('ITableData0', 2, 'Export->HTML', 'All records', 'Step 05.4: Expect to see output format selection for HTML and the All Records option', all_items='no')
 
        miscelanousobj.select_menu_items('ITableData0', 2, 'Export','HTML','All records')
 
        utillobj.switch_to_window(1)
        time.sleep(9)
        miscelanousobj.verify_column_heading("ITableData0", HTML_column, 'Step 05.4: Verify all columns listed on the HTML report')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2050538_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050538_Ds01.xlsx', 'Step 05.5: Expect to see a basic HTML report in a new window', desired_no_of_rows=7)
  
        self.driver.close()
 
        utillobj.switch_to_window(0)
 
        utillobj.infoassist_api_logout()
 
              
        """
        STep 06: Execute Fex AR-RP-219e. FILTER option functionality test.
        Select the Retail_Cost field and click the Active drop-down arrow.
        Select Filter, then Greater Than, then select 9,495 as the value. Click the Filter button.
        """
        utillobj.active_run_fex_api_login("AR-RP-219e.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
 
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
 
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 06.1: Execute the AR-RP-219e.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 06.2: Verify all columns listed on the report AR-RP-219e.fex')
  
        self.driver.find_element(By.CSS_SELECTOR,retail_cost_field).click()
 
        try:
            filter_option=self.driver.find_element(By.CSS_SELECTOR,'#set0_3_0_0i_t').text
        except NoSuchElementException:
            filter_option=False
        utillobj.asequal('Filter',filter_option,'Step 06.3: Expect to see only the FILTER option appear when the Retail_Cost field drop-down arrow is selected')
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Greater than')
        parent_css="[id^='wall1'] td[class*='arWindowBar']"
        utillobj.synchronize_with_visble_text(parent_css, 'FilterSelection', 30, 1)
         
         
        filterselectionobj.create_filter(1, 'Greater than', value1='9,495')
        time.sleep(3) 
        filter_box=['RETAIL_COST','Greater than','9,495']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 06.4: Expect to see the Filter selection and value panel appear',filter_box)
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        parent_css="#ITableData0 tr:nth-child(4) td:nth-child(1)"
        utillobj.synchronize_with_visble_text(parent_css, 'ITALY', 30, 1)
         
         
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2050538_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050538_Ds02.xlsx', 'Step 06.5: Expect to see a the report displaying only Retail_Cost rows that are Greater than 9,495', desired_no_of_rows=5)
 
        utillobj.infoassist_api_logout()
 
                  
        """
        Step 07: Execute Fex AR-RP-219f. FREEZE option functionality test.
        Select the Dealer_Cost field and click the Active drop-down arrow.
        """    
        utillobj.active_run_fex_api_login("AR-RP-219f.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
 
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
 
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 07.1: Execute the AR-RP-219f.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 07.2: Verify all columns listed on the report AR-RP-219f.fex')
 
        self.driver.find_element(By.CSS_SELECTOR,dealer_cost_field).click()
 
              
        try:
            dealer_value=self.driver.find_element(By.CSS_SELECTOR,'#set0_4_0_0i_t').text
        except NoSuchElementException:
            dealer_value=False
        utillobj.asequal('',dealer_value,'Step 07.3: Expect to see no options appear when any field drop-down arrow is selected')
    
        utillobj.infoassist_api_logout()
 
          
          
        """
        Step 08: Execute Fex AR-RP-219g. HIDE option functionality test.
        Select the Sales field and click the Active drop-down arrow.
        Click the Hide option.
        """
        utillobj.active_run_fex_api_login("AR-RP-219g.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
 
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
 
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 08.1: Execute the AR-RP-219g.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 08.2: Verify all columns listed on the report AR-RP-219g.fex')
  
        self.driver.find_element(By.CSS_SELECTOR,sales_filed).click()
        time.sleep(2)     
        try:
            sales_value=self.driver.find_element(By.CSS_SELECTOR,'#set0_5_0_1i_t').text
        except NoSuchElementException:
            sales_value=False
        utillobj.asequal('Hide Column',sales_value,'Step 08.3: Expect to see only the Hide option appear when the Sales field drop-down arrow is selected')
        time.sleep(3)     
        miscelanousobj.select_menu_items('ITableData0', 5, 'Hide Column')
        parent_css="#ITableData0 .arGridColumnHeading td[id^='TCOL_0_C']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 30, 1)
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2050538_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050538_Ds03.xlsx','Step 08.4: Expect to see a the report with the Sales column now hidden')            
             
        utillobj.infoassist_api_logout()
         
              
        """
        Step 09: Execute Fex AR-RP-219h. PAGINATION option functionality test.
        Select the Country field and click the Active drop-down arrow.
        Select 10 Records from the Pagination selection panel.
        """
        utillobj.active_run_fex_api_login("AR-RP-219h.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 09.1: Execute the AR-RP-219h.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 09.2: Verify all columns listed on the report AR-RP-219h.fex')
         
        self.driver.find_element(By.CSS_SELECTOR,country_field).click()
        time.sleep(2)
              
        try:
            pagination=self.driver.find_element(By.CSS_SELECTOR,'#set0_0_0_1i_t').text
        except NoSuchElementException:
            pagination=False
        utillobj.asequal('Show Records',pagination,'Step 09.3: Expect to see only the Pagination option appear when the Country field drop-down arrow is selected')
         
        option_list=['Default','5 Records','10 Records','15 Records','Show All']
        miscelanousobj.verify_menu_items('ITableData0', 0, 'Show Records', option_list, 'Step 09.4: Expect to see all options')
          
        miscelanousobj.select_menu_items('ITableData0', 0, 'Show Records','10 Records')
        parent_css="#ITableData0 tr[id^='I0r']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 30, 1)
         
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2050538_Ds04_page1.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050538_Ds04_page1.xlsx','Step 09.5: Expect to see the first 10 of 18 records on Page 1')
        time.sleep(2) 
        miscelanousobj.navigate_page('last_page')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        utillobj.synchronize_with_visble_text(parent_css, 'JAPAN', 30, 1)
         
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2050538_Ds04_page2.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050538_Ds04_page2.xlsx','Step 09.6: Expect to see the last 8 records on Page 2')
         
        utillobj.infoassist_api_logout()
         
              
        """
        Step 10: Execute Fex AR-RP-219i. PIVOT option functionality test.
        Select the Retail_Cost field and click the Active drop-down arrow.
        Select Country as the Group By field and CAR as the Across field.
        """
        utillobj.active_run_fex_api_login("AR-RP-219i.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 10.1: Execute the AR-RP-219i.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 10.2: Verify all columns listed on the report AR-RP-219i.fex')
        time.sleep(2)  
        self.driver.find_element(By.CSS_SELECTOR,retail_cost_field).click()
        time.sleep(3) 
        try:
            pivot=self.driver.find_element(By.CSS_SELECTOR,'#set0_3_0_0i_t').text
        except NoSuchElementException:
            pivot=False
        utillobj.asequal('Pivot (Cross Tab)',pivot,'Step 10.3: Expect to see only the Pivot option appear when the Retail_Cost field drop-down arrow is selected')
          
        pivot_menu=['Group By(undefined)', 'COUNTRY', 'CAR', 'MODEL', 'RETAIL_COST', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Pivot (Cross Tab)', pivot_menu, 'Step 10.4: Expect to see the Group By panel appear')
        time.sleep(2)  
        across_menu=['Across', 'CAR', 'MODEL', 'RETAIL_COST', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Pivot (Cross Tab)->COUNTRY', across_menu, 'Step 10.5: Expect to see the Across panel appear')
        time.sleep(3)  
        miscelanousobj.select_menu_items('ITableData0', 3, 'Pivot (Cross Tab)','COUNTRY','CAR')
        parent_css="[id^='wall1'] td[class*='arWindowBar']"
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COSTBYCAR,COUNTRY', 30, 1)
         
#         utillobj.create_pivot_data_set('piv1', 'C2050538_Ds05.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2050538_Ds05.xlsx','Step 10.6: Expect to see the Pivot Table')
           
        utillobj.infoassist_api_logout()
         
             
            
        """
        Step 11: Execute Fex AR-RP-219j. PRINT option functionality test.
        Select the Dealer_Cost field and click the Active drop-down arrow.
        Select Print, then select All Records.
        """
        utillobj.active_run_fex_api_login("AR-RP-219j.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 11.1: Execute the AR-RP-219j.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 11.2: Verify all columns listed on the report AR-RP-219j.fex')
           
        self.driver.find_element(By.CSS_SELECTOR,dealer_cost_field).click()
        time.sleep(3)
        try:
            print_option=self.driver.find_element(By.CSS_SELECTOR,'#set0_4_0_1i_t').text
        except NoSuchElementException:
            print_option=False
        utillobj.asequal('Print',print_option,'Step 11.3: Expect to see only the Print option appear when the Dealer_Cost field drop-down arrow is selected') 
        record_values=['All records','Filtered only']
        miscelanousobj.verify_menu_items('ITableData0', 4, 'Print', record_values, 'Step 11.4: Expect to see the Record Selection panel')
        miscelanousobj.select_menu_items('ITableData0', 4, 'Print','All records')
         
        utillobj.verify_print_dialog_and_click('Step 11.5: Printer Dialog Opened')
         
        utillobj.infoassist_api_logout()
         
            
            
        """
        Step 12: Execute Fex AR-RP-219k. RESTORE option functionality test.
        Select the Sales field, select Filter, then Not Equal and lastly select value 0 from the drop-down, then click the Filter button.
        Select the Sales field again and select Restore.
        """
        utillobj.active_run_fex_api_login("AR-RP-219k.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 12.1: Execute the AR-RP-219k.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 12.2: Verify all columns listed on the report AR-RP-219k.fex')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 12.3: Verify AR-RP-219.fex data', desired_no_of_rows=5)
         
        utillobj.infoassist_api_logout()
         
             
              
        """
        Step 13: Execute Fex AR-RP-219l. ROLLUP option functionality test.
        Select the Retail_Cost field and click the Active drop-down arrow.
        Select the Country field as the Rollup Group By field.
        """
        utillobj.active_run_fex_api_login("AR-RP-219l.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 13.1: Execute the AR-RP-219l.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 13.2: Verify all columns listed on the report AR-RP-219l.fex')
          
        self.driver.find_element(By.CSS_SELECTOR,retail_cost_field).click()
        time.sleep(1) 
        try:
            rollup_option=self.driver.find_element(By.CSS_SELECTOR,'#set0_3_0_0i_t').text
        except NoSuchElementException:
            rollup_option=False
        utillobj.asequal('Rollup',rollup_option,'Step 13.3: Expect to see only the Rollup option appear when the Retail_Cost field drop-down arrow is selected')
        time.sleep(1)
        rollup_menu=['Group By (X)(undefined)', 'COUNTRY', 'CAR', 'MODEL', 'RETAIL_COST', 'DEALER_COST', 'SALES']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Rollup', rollup_menu, 'Step 13.4: Expect to see the Rollup field selection panel')
        time.sleep(1) 
        miscelanousobj.select_menu_items('ITableData0', 3, 'Rollup','COUNTRY')
        parent_css="[id^='wall1'] td[class*='arWindowBar']"
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COSTBYCOUNTRY', 30, 1)
         
        rollup_column=['COUNTRY','RETAIL_COST']
        miscelanousobj.verify_column_heading("ITableData1", rollup_column, 'Step 13.5: Verify rollup columns')
        time.sleep(1)
#         utillobj.create_data_set('ITableData1', 'I1r', 'C2050538_Ds06.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', 'C2050538_Ds06.xlsx','Step 13.6: Expect to see the Rollup report')
              
        utillobj.infoassist_api_logout()
         
              
        """
        Step 14: Execute Fex AR-RP-219m. SAVECHANGES option functionality test.
        Select the Dealer_Cost field and click the Active drop-down arrow.
        Select Save Changes.
        """
              
        utillobj.active_run_fex_api_login("AR-RP-219m.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 14.1: Execute the AR-RP-219m.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 14.2: Verify all columns listed on the report AR-RP-219m.fex')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 14.3: Verify AR-RP-219.fex data', desired_no_of_rows=5)
        time.sleep(1)
        utillobj.infoassist_api_logout()
        time.sleep(3)
              
        """
        Step 15: Execute Fex AR-RP-219n. SENDEMAIL option functionality test.
        Select the Sales field and click the Active drop-down arrow.
        Select Send as E-mail.
        """
        utillobj.active_run_fex_api_login("AR-RP-219n.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 15.1: Execute the AR-RP-219n.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 15.2: Verify all columns listed on the report AR-RP-219n.fex')
        time.sleep(3)
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 15.3: Verify AR-RP-219.fex data', desired_no_of_rows=5)
         
        utillobj.infoassist_api_logout()
         
              
        """
        Step 16: Execute Fex AR-RP-219o. SORT option functionality test.
        Click Sort Descending option.
        """
        utillobj.active_run_fex_api_login("AR-RP-219o.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 16.1: Execute the AR-RP-219o.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 16.2: Verify all columns listed on the report AR-RP-219o.fex')
          
        self.driver.find_element(By.CSS_SELECTOR,country_field).click()
        time.sleep(2) 
        sort_list=[]
        country_dropdown=self.driver.find_elements(By.CSS_SELECTOR,'[id*=set0_0_0_]')
        for i in range(len(country_dropdown)):
            sort_list.append(country_dropdown[i].text)
        country_dropdown_value=[x for x in sort_list if x]
        time.sleep(2) 
        utillobj.asequal(['Sort Ascending', 'Sort Descending'],country_dropdown_value,'Step 16.3: Expect to see only the Sort Ascending & Sort Descending options available')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Descending')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        utillobj.synchronize_with_visble_text(parent_css, 'WGERMANY', 30, 1)
         
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2050538_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050538_Ds07.xlsx', 'Step 16.4: Expect to see the report re-sorted in Descending COUNTRY order')
         
        utillobj.infoassist_api_logout()
         
             
        """
        Step 17: Execute Fex AR-RP-219p. TOOLS option functionality test.
        This will provide menu options for: Grid Tool, Chart/Rollup Tool & Pivot Tool.
        Click the Active drop-down for RETAIL_COST.
        Select the first option - Grid Tool
        Drag the Car field above the Country field to re-order the report, then click OK.
        Click the Active drop-down again and select Restore Original.
        """
        utillobj.active_run_fex_api_login("AR-RP-219p.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
         
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
         
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 17.1: Execute the AR-RP-219p.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 17.2: Verify all columns listed on the report AR-RP-219p.fex')
         
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 17.2.1: Verify AR-RP-219.fex data', desired_no_of_rows=5)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,retail_cost_field).click()
        retail_dropdown=[]
        retail_cost_option=self.driver.find_elements(By.CSS_SELECTOR,'[id*="set0_3_0_"]')
        for i in range(len(retail_cost_option)):
            retail_dropdown.append(retail_cost_option[i].text)
        retail_dropdown_value=[x for x in retail_dropdown if x]
        utillobj.asequal(['Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Restore Original'],retail_dropdown_value,'Step 17.3: Expect to see only the Grid Tool, Chart/Rollup Tool, Pivot Tool & Restore options available')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        parent_css="[id^='wall1'] td[class*='arWindowBar']"
        utillobj.synchronize_with_visble_text(parent_css, 'GridTool', 30, 1)
         
        miscelanousobj.verify_popup_appears('wall1', 'Grid Tool', 'Step 17.4: Expect to see the Grid Menu appears')
        time.sleep(2)
        toolsobj.pivot_tool_drag_drop_items('gridtoolt1', 'Column Order', 'COUNTRY', 0, 'Column Order', 2)
        time.sleep(1)
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        utillobj.synchronize_with_visble_text(parent_css, 'JAGUAR', 30, 1)
         
        columns2=['CAR','COUNTRY','MODEL','RETAIL_COST','DEALER_COST','SALES']
        miscelanousobj.verify_column_heading("ITableData0", columns2, 'Step 17.5: Verify columns')
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2050538_Ds08.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050538_Ds08.xlsx','Step 17.6: Expect to see the report still in Country sequence but with Car in column 1 and Country in column 2')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 3, 'Restore Original')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        utillobj.synchronize_with_visble_text(parent_css, 'ENGLAND', 30, 1)
         
             
        """Click the Active drop-down for RETAIL_COST field and select the second option - Chart/Rollup Tool
        Drag RETAIL_COST to the Measure and CAR to the Group By, then click OK."""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Chart/Rollup Tool')
        parent_css="[id^='wall1'] td[class*='arWindowBar']"
        utillobj.synchronize_with_visble_text(parent_css, 'Chart/RollupTool', 30, 1)
         
        miscelanousobj.verify_popup_appears('wall1', 'Chart/Rollup Tool', 'Step 17.7: Expect to see the Chart/Rollup Tool appear')
        time.sleep(1)
        toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'RETAIL_COST', 1, 'Measure', 0)
        time.sleep(2)
        toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'CAR', 1, 'Group By', 0)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[contains(text(),'Ok')]").click()
         
        element1 = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element1, 'C2050538_Actual_Step17', image_type='actual')
         
        miscelanousobj.verify_active_popup_chart_tooltip('wall2', 'bar', 'RETAIL_COST', 'RETAIL_COST=19565', 'Lochmara', 'Step 17.8: Expect to see a Bar Chart with 10 columns, one for each CAR value')
        self.driver.find_element(By.CSS_SELECTOR,'[onclick="closewin(2)"]').click()
        time.sleep(3)
             
        """Click the Active drop-down for RETAIL_COST field and select the third option - Pivot Tool
        Drag DEALER_COST to the Measure, COUNTRY to Across and CAR to Group By, then click OK."""
        miscelanousobj.select_menu_items('ITableData0', 3, 'Pivot Tool')
        parent_css="[id^='wall1'] td[class*='arWindowBar']"
        utillobj.synchronize_with_visble_text(parent_css, 'PivotTool', 30, 1)
         
        time.sleep(2)
        miscelanousobj.verify_popup_appears('wall1', 'Pivot Tool', 'Step 17.9: Expect to see the Pivot Tool appear')
        time.sleep(1)
        toolsobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'DEALER_COST', 1, 'Measure', 0)
        time.sleep(1)
        toolsobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'COUNTRY', 1, 'Across', 0)
        time.sleep(1)
        toolsobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'CAR', 1, 'Group By', 0)
        time.sleep(1)
        toolsobj.pivot_tool_close('pivottoolt1', 'Ok')
        time.sleep(2)
#         utillobj.create_pivot_data_set('piv2', 'C2050538_Ds09.xlsx')
        utillobj.verify_pivot_data_set('piv2', 'C2050538_Ds09.xlsx', 'Step 17.10: Expect to see a grid report with summed Dealer_Costs')
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
            
            
        """ Step 18: Execute Fex AR-RP-219q. VISUALIZE option functionality test. Test is valid for numeric fields only.
                    Click the Active drop-down for MODEL(alphanumeric).
                    For the SALES column, click the Active drop-down. Select Visualize.
                    Expect to see no options, Visualize is only enabled for numeric fields.
                    Expect to see only the Visualize option available.
                    Expect to see a new column appear with horizontal bars, representing the relative values of each SALES value.
        """
        utillobj.active_run_fex_api_login("AR-RP-219q.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 18.1: Execute the AR-RP-219q.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 18.2: Verify all columns listed on the report AR-RP-219q.fex')
        
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 18.2.1: Verify AR-RP-219.fex data', desired_no_of_rows=5)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,model_field).click()
        
        temp_str_value=driver.find_element_by_css_selector("#pt0_2_0 #dt0_2_0 table").text.strip().replace('\n','')
        actual=re.sub(' ','',temp_str_value)
        utillobj.asequal(actual, '', 'Step 18.3: Expect to see no options appear')
        time.sleep(1) 
        driver.find_element(By.CSS_SELECTOR,sales_filed).click()
        time.sleep(2)
        temp_str_value=driver.find_element_by_css_selector("#pt0_5_0 #dt0_5_0 table").text.strip().replace('\n','')
        acutal=re.sub(' ','',temp_str_value)
        utillobj.asequal(acutal, 'Visualize', 'Step 18.4: Expect to see Visualize')
        time.sleep(1)
        miscelanousobj.select_menu_items('ITableData0', 5, 'Visualize')
        parent_css="#ITableData0 tr:nth-child(1) td:nth-child(7)"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 5, 'black', 'Step 18.5: Verify visualization added', background=True,custom_opt='True')
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
            
            
            
        """ Step 19: Execute Fex AR-RP-219r. WINDOW option functionality test. 
                    Click the Active drop-down for COUNTRY.
                    Select the Window option, then click the Tabs option.
                    For the RETAIL_COST field, click the drop-down and select Rollup, then CAR as the Group By field.
                    Click the Report tab at the top.
                    Click the Chart tab at the top.
                    Expect to see only the Window and the Rollup options available.
                    Expect to see the report refreshed, with a REPORT tab button at the top.
                    Expect to see a 10 line Rollup Report appear and at the top see a Chart icon appear next to the Report icon.
                    Expect to see the original Report.
                    Expect to see the Rollup Report once again.
        """
        utillobj.active_run_fex_api_login("AR-RP-219r.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 19.1: Execute the AR-RP-219r.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 19.2: Verify all columns listed on the report AR-RP-219r.fex')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 19.2.1: Verify AR-RP-219.fex data', desired_no_of_rows=5)
        time.sleep(2)
        status=False
        driver.find_element(By.CSS_SELECTOR,retail_cost_field).click()
        time.sleep(1)
        temp_str_value=driver.find_element_by_css_selector("#pt0_3_0 #dt0_3_0 table").text.strip().replace(' ','').split('\n')
        if 'Rollup' in temp_str_value:
            if 'Window' in temp_str_value:
                status=True
        utillobj.asequal(status, True, 'Step 19.3: Expect to see Rollup and Window option available')
        time.sleep(1)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Window', 'Tabs')
        parent_css="#MAINTABLE_wmenu0"
        utillobj.synchronize_with_visble_text(parent_css, 'Report', 30, 1)
        
        time.sleep(2)
        otab1=driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr>#tab_0").text
        otab=otab1.strip()=='Report'
        utillity.UtillityMethods.asequal(self,True, otab, 'step 19.4: Verify Active Report appear with a Tab Window control at the top')
        time.sleep(2)
        miscelanousobj.select_menu_items("ITableData0", 3, "Rollup","CAR")
        parent_css="#MAINTABLE_wmenu0"
        utillobj.synchronize_with_visble_text(parent_css, 'ReportChart', 30, 1)
        
        time.sleep(2)
        tabs=['Report ', 'Chart']
        verify_tabs(tabs, "Step 19.5")
        time.sleep(5)
        report_checkpoint("Step 19.6")
        miscelanousobj.navigate_tabbed_report(0,1)
        time.sleep(4)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, 1)
        
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 19.7: Execute the AR-RP-219r.fex")
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 19.8: Verify all columns listed on the report AR-RP-219r.fex')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-219.xlsx','Step 19.9: Verify AR-RP-219.fex data', desired_no_of_rows=5)
        time.sleep(2)
        miscelanousobj.navigate_tabbed_report(0,2)
        parent_css="#MAINTABLE_wmenu0"
        utillobj.synchronize_with_visble_text(parent_css, 'ReportChart', 30, 1)
        
        time.sleep(2)
        tabs=['Report ', 'Chart']
        verify_tabs(tabs, "Step 19.10")
        time.sleep(5)

        
        

if __name__ == "__main__":
    unittest.main()