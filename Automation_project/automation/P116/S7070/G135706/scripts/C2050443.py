'''
Created on Aug 16, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050443
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,visualization_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


class C2050443_TestClass(BaseTestCase):

    def test_C2050443(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050443'
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultareaobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        
        """    
        Step 01: Right click on folder created in IA and select New >report and select GGSALES master file.
        """
        utillobj.infoassist_api_login('report','ibisamp/ggsales','P116/S7070', 'mrid', 'mrpass')
        """
        Step 02: On the Format tab, in the Output Types group, click Active report.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        """
        Step 03: On the Home Tab, select Theme and select ENIADefault_combine.sty
        """
        time.sleep(3)
        ribbonobj.select_theme('Legacy Templates', 'ENIADefault_combine.sty')
        
        """
        Step 04: Select Category, Product_Id & Product as Dimensions and Unit Sales, Dollar sales as Measures.
        """
        metaobj.datatree_field_click('Category', 1, 1,'Sort')
        metaobj.datatree_field_click('Product ID', 1, 1,'Sort')
        metaobj.datatree_field_click('Product', 1, 1,'Sort')
        metaobj.datatree_field_click('Unit Sales', 1, 1,'Sum')
        metaobj.datatree_field_click('Dollar Sales', 1, 1,'Sum')
        
        columns=['Category','Product ID','Product','Unit Sales','Dollar Sales']
        resultareaobj.verify_report_titles_on_preview(5, 5,'TableChart_1',columns, 'Step 04: Verify preview pane')
        
        """
        Step 05: Select Format tab --> Navigation --> select Table of content option
        """
        ribbonobj.select_ribbon_item("Format", "table_of_contents")
        
        """
        Step 06: Run the report
        """
        value=utillobj.parseinitfile("browser")
        if value=='IE':
            ribbonobj.select_top_toolbar_item('toolbar_run')
            time.sleep(10)
            self.driver.switch_to_frame(self.driver.find_element(By.CSS_SELECTOR,"[id*='ReportIframe']"))
        else:
            ribbonobj.select_top_toolbar_item('toolbar_run')
            time.sleep(10)
            self.driver.switch_to_frame(self.driver.find_element(By.CSS_SELECTOR,"[id*='ReportIframe']"))
        time.sleep(10)
        
        try:
            content=self.driver.find_element(By.CSS_SELECTOR,"[id='MAINTABLE_filter0']").is_displayed()
            utillobj.asequal(True,content,"Step 06: Verify report contain Table of content box")
        except NoSuchElementException:
            print("Step 06.3: Verify report contain Table of content box - Failed")
            
        """
        Step 07: In table of content query plane select coffee
        """
        time.sleep(5)
        try:
            selected = self.driver.find_element(By.XPATH,"//tr[@class='arByTocItemSelected']/td/table/tbody/tr/td[3]/span[contains(text(),'Coffee')]").is_displayed()
            utillobj.asequal(True,selected,"Step 07.1: Verify Coffee value highlighted")
        except NoSuchElementException:
            print("Step 07.1: Verify Coffee value highlighted-Failed")
        
        self.driver.find_element(By.CSS_SELECTOR,'[id="XFD_0_0"]').click()
        time.sleep(10)
        actual_value=['+', '+', '+']
        values=[]
        #x=self.driver.find_elements(By.XPATH,'//*[contains(@style,"white-space")]//*[contains(@onclick,"FD_0_0")]')    
        for i in range(0,3):
                x='[id*="_0\:'+str(i)+'"] [class="arByTocItem"]'
                values.append(self.driver.find_element_by_css_selector(x).text.strip())
        utillobj.asequal(actual_value,values,"Step 07.2: verify coffee get expanded")
        
        
        """
        Step 08: Select coffee sub field C141
        """
        
        self.driver.find_element(By.XPATH,"//span[contains(text(),'C141')]").click()
        time.sleep(5)
        try:
            value_selected=self.driver.find_element(By.XPATH,"//tr[@class='arByTocItemSelected']").is_displayed()
            utillobj.asequal(True,value_selected,"Step 08: Verify C141 value highlighted ")
        except NoSuchElementException:
            print("Step 08: Verify C141 value highlighted -Failed")
        
        """
        Step 09: Select Espresso in C141 sub field
        """
        self.driver.find_element(By.XPATH,"//td[@id='XFD_0_0:0']").click()
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Espresso')]").click()
        time.sleep(5)
        try:
            selected_value2=self.driver.find_element(By.CSS_SELECTOR,'[class="arByTocItemSelected"]').is_displayed()
            utillobj.asequal(True,selected_value2,"Step 09: Verify Expresso value highlighted ")
        except NoSuchElementException:
            print("Step 09: Verify Expresso value highlighted -Failed")
            
        self.driver.switch_to_default_content()
        
        
if __name__ == '__main__':
    unittest.main()   
            
            
            
            
            
            
            
            
            
            