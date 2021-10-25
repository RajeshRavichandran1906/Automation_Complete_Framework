'''
Created on Sep 16, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2058833
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,re
from selenium.webdriver.support.color import Color
import time

class C2058833_TestClass(BaseTestCase):

    def test_C2058833(self):
        
        """
            Step 01: Execute the attached repro ACT-485-default.fex

            Click the drop down for Country, select Filter, then Equals.

        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("ACT-485-default.fex", "S7215", 'mrid', 'mrpass')
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the ACT-485t.fex")
        column_list=['COUNTRY','CAR','MODEL','BODYTYPE','RETAIL_COST','DEALER_COST']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report ACT-485t.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act485t.xlsx','Step 01.3: Verify data set')
        
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        time.sleep(6)
        
        box="#fboxi0 .arFilterItemDrowpDown"
        val2=self.driver.find_element_by_css_selector(box).value_of_css_property("font-size") 
        
        utillobj.asequal(val2,'11px','Step 01.1: Expect to see the Filter Box with the expanded font size of 16px')
        
        utillobj.infoassist_api_logout()
        
        """
        Step 02: Execute the attached repro act-485-10px.fex
 
        Click the drop down for Country, select Filter, then Equals.
 
        """
        #Expect to see the Filter Box with the font size of 10px, with White text on Green background, as a result of the inserted json code.

        #The json code only changes the line showing COUNTRY and the value boxes.
        #The Operator and Condition line below remains the same size.
         
        utillobj.active_run_fex_api_login("act-485-10px.fex", "S7215", 'mrid', 'mrpass')
        time.sleep(6)
         
             
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        expected_color=utillobj.color_picker('green', 'rgba')
        expected_color_text=utillobj.color_picker('white', 'rgba')
             
        filter_buttons_css="#wall1 .arFilterButton"
         
        filter_buttons=self.driver.find_elements_by_css_selector(filter_buttons_css)
        
        for i in range(len(filter_buttons)):
            color = filter_buttons[i].value_of_css_property('background-color')
            color_text = filter_buttons[i].value_of_css_property('color')
            color= Color.from_string(color).rgba
            color_text= Color.from_string(color_text).rgba
            if color not in expected_color:
                break  
         
        box="#fboxi0 .arFilterItemDrowpDown"
        val2=self.driver.find_element_by_css_selector(box).value_of_css_property("font-size")  
        utillobj.asequal(val2,'10px','Step 02.1: Expect to see the Filter Box with the expanded font size of 16px')
        utillobj.asin(color,expected_color,'Step 02.2: Expect to see Green background, as a result of the inserted json code')
        
        utillobj.asin(color_text,expected_color_text,'Step 02.3: Expect to see black text on Green background, as a result of the inserted json code')
        utillobj.infoassist_api_logout()
         
        """Step 03: Execute the attached repro act-485-18px.fex
        act-485-18px
 
        Click the drop down for Country, select Filter, then Equals."""
            
        #Expect to see the Filter Box with the much larger font size of 18px, with White text on Green background, as a result of the inserted json code.

        #Again, the json code only changes the line showing COUNTRY and the value boxes.
        #The Operator and Condition line below remains the same size.
        
        utillobj.active_run_fex_api_login("act-485-18px.fex", "S7215", 'mrid', 'mrpass')
        time.sleep(6)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        expected_color=utillobj.color_picker('green', 'rgba')
        expected_color_text=utillobj.color_picker('white', 'rgba')
             
        filter_buttons_css="#wall1 .arFilterButton"
         
        filter_buttons=self.driver.find_elements_by_css_selector(filter_buttons_css)
        
        for i in range(len(filter_buttons)):
            color = filter_buttons[i].value_of_css_property('background-color')
            color_text = filter_buttons[i].value_of_css_property('color')
            color= Color.from_string(color).rgba
            color_text= Color.from_string(color_text).rgba
            if color not in expected_color:
                break  
         
        box="#fboxi0 .arFilterItemDrowpDown"
        val2=self.driver.find_element_by_css_selector(box).value_of_css_property("font-size") 
        
        utillobj.asequal(val2,'18px','Step 03.1: Expect to see the Filter Box with the expanded font size of 16px')
        utillobj.asin(color,expected_color,'Step 03.2: Expect to see Green background, as a result of the inserted json code')
        
        utillobj.asin(color_text,expected_color_text,'Step 03.3: Expect to see black text on Green background, as a result of the inserted json code')
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()