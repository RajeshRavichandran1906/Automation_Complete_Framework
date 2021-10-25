'''
Created on JUL 10, 2017

@author: Prabhakaran

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204992
TestCase Name = AHTML:filter values in bar/line chart pop up menu are wrong(Project 96423)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_resultarea,visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2204992_TestClass(BaseTestCase):

    def test_C2204992(self):
        
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        
        """
            Step 01:Execute 96423.fex from repro and Expected Result
        """    
        utillobj.active_run_fex_api_login('96423.fex','S7074','mrid','mrpass')
        parent_css="#MAINTABLE_wbody0 div[title^='DEALER_COST'][style*='background-color']"
        resobj.wait_for_property(parent_css, 10)
        time.sleep(2)
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0 div[title='DEALER_COST = 49500']","Revenue by State","Step 01.1 : Verify Chart title")        
        
        x_axis=self.driver.find_elements_by_css_selector("#MAINTABLE_wbodyMain0 #Piet0 div[title][style*='Arial;'][style*='10pt']")
        expected_x_axis=['ENGLAND / JAGUAR', 'ENGLAND / JENSEN', 'ENGLAND / TRIUMPH', 'FRANCE / PEUGEOT', 'ITALY / ALFA ROMEO', 'ITALY / MASERATI', 'JAPAN / DATSUN', 'JAPAN / TOYOTA', 'W GERMANY / AUDI', 'W GERMANY / BMW']
        actual_x_axis=[xaxis.text.strip() for xaxis in x_axis]
        utillobj.asequal(actual_x_axis,expected_x_axis,'Step 01.2 : Verify X-Axis title')
        
        y_axis=self.driver.find_elements_by_css_selector("#MAINTABLE_wbodyMain0 #Piet0 [style*='Arial;'][style*='12pt']")
        expected_y_axis=['0','20 K','40 K','60 K']
        actual_y_axis=[yaxis.text.strip() for yaxis in y_axis]
        utillobj.asequal(actual_y_axis,expected_y_axis,'Step 01.3 : Verify Y-Axis title')

        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody0",10,'Step 01.4 : Verify number of char risers',custom_css="div[title^='DEALER_COST'][style*='background-color']")
        utillobj.verify_chart_color("MAINTABLE_wbody0",None, "Lochmara", "Step 01.5: Verify  bar color",custom_css="div[title='DEALER_COST = 49500']",attribute_type='background-color')
        
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelaneous_obj.verify_active_popup_chart_tooltip('MAINTABLE_wbody0','bar','DEALER_COST','DEALER_COST=18621','Lochmara','Step 01.8 : Verify tooltip ( DEALER_COST = 49500 )')
        
        """
            Step 02 : Select the last bar in chart
            it should display chart pop up menu
            "DEALER_COST=49500
            COUNTY=WGERMANY
            CAR=BMW
            MODEL=2002 2 DOOR"
        """
        riser=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 div[title='DEALER_COST = 49500'][style*='background']")
        riser.click()
        time.sleep(4)
        popup_menu=self.driver.find_elements_by_css_selector("div[id^='dt0_null_x'] tr[id^='t0_null_x'] span[id^='set0_null']")
        actual_popup_values=[popup.text.strip() for popup in popup_menu if popup.text!='']
        expected_popup_value=['DEALER_COST = 49500', 'COUNTRY=W GERMANY', 'CAR=BMW', 'MODEL=2002 2 DOOR']
        utillobj.asequal(actual_popup_values,expected_popup_value,"Step 02.1 : Verify Select the last bar in chart. it should display chart pop up menu ['DEALER_COST = 49500', 'COUNTRY=W GERMANY', 'CAR=BMW', 'MODEL=2002 2 DOOR']")
        
        utillobj.take_monitor_screenshot('C2204992_Actual_step02', image_type='actual', left=10, top=25, right=450, bottom=500)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
