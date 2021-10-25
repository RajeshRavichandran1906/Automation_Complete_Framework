'''
Created on Sep 20, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2068113
'''
import unittest,re,time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.support.color import Color



class C2068113_TestClass(BaseTestCase):

    def test_C2068113(self):

        """
            Step 01: Execute the attached repro - ACT-379-default.fex.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 02: Execute the attached repro - ACT-379.fex.
        """

        utillobj.active_run_fex_api_login('ACT-379.fex','S7215','mrid','mrpass')  
        time.sleep(6)    
        active_misobj.verify_page_summary('0','4317of4317records,Page1of76', 'Step 02.1: Verify Page summary')
        columns1 = ['Sequence#', 'Category', 'Product ID', 'Product', 'Region', 'State', 'City', 'Store ID', 'Date', 'Unit Sales', 'Dollar Sales', 'Budget Units', 'Budget Dollars']
        active_misobj.verify_column_heading('ITableData0', columns1, 'Step 02.2: Verify column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT-379-default.xlsx', 'Step 02.3: Verify data set')
    

    
        #1.Heading area is green, text is blue.
        
        expected_color=utillobj.color_picker('green', 'rgba')
        heading_color = self.driver.find_element(By.CSS_SELECTOR,'[class="arGridBar"]').value_of_css_property('background-color')
        heading_color = Color.from_string(heading_color).rgba
        
        utillobj.asin(heading_color,expected_color,'Step 02.a: Expect to see Heading area is green') 
         
        expected_color_text=utillobj.color_picker('blue', 'rgba')
        time.sleep(3)
        
        text = "table[id='IWindowBody0'] .arGridBar table td:nth-child(2)"
        heading_text_color = self.driver.find_elements(By.CSS_SELECTOR,text)
        heading_text = heading_text_color[1].value_of_css_property('color')
        heading_text = Color.from_string(heading_text).rgba
        
        utillobj.asin(heading_text,expected_color_text,'Step 02.b: Expect to see Heading text is blue')
        
        #2 - Heading size has increased(size 16) from default.
        
        heading_font = heading_text_color[1].value_of_css_property('font-size')
        utillobj.as_GE(int(heading_font[:2]),16,'Step 02.c: Expect to see Heading size has increased(size 16) from default')
        
        #3 - Heading font is Comic Sans MS.
        
        heading = self.driver.find_element_by_css_selector("table[id='IWindowBody0'] .arGridBar table table tr > td:nth-child(2)").value_of_css_property('font-family')
       
        utillobj.asin("comic sans ms",heading.lower(), 'Step 02.d : Expect to see Heading font is Comic Sans MS.')
        
        #4. Report is orange text on white background.
        
        report = '[id="ITableData0"]  td[id*="I0r"]'
        expected_color_report=utillobj.color_picker('flush_orange', 'rgba')
        
        report_text = self.driver.find_elements(By.CSS_SELECTOR, report)
        
        for i in range(len(report_text)):
            color=report_text[i].value_of_css_property('color')
            color1=report_text[i].value_of_css_property('background-color')
            
            report_text_size=report_text[i].value_of_css_property('font-size')
            #report_font=report_text[i].value_of_css_property('font-family')
            break
        
        color = Color.from_string(color).rgba
        color1 = Color.from_string(color1).rgba
    
       
        
        utillobj.asin(color,expected_color_report,'Step 02.e: Expect to see Report is orange text')
        
        
 
        utillobj.asequal(color1,'rgba(0, 0, 0, 0)','Step 02.f: Expect to see Report on white background.')
        
        
        #5.Report size has decreased(size 7) from default.
        utillobj.as_GE(int(report_text_size[:1]),9,'Step 02.g: Expect to see Heading size has decreased(size 7) from default')
        
        
        

if __name__ == "__main__":
    unittest.main()