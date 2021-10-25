'''
Created on Sep 20, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2073857
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea
from common.lib import utillity
import unittest,time
from selenium.common.exceptions import NoSuchElementException

class C2073857_TestClass(BaseTestCase):

    def test_C2073857(self):
        
        """Test Case Variables"""
        filter_val = '[title="Remove Filter"]'
        
        """
            Step 01: Execute the attached repro - act-137a.fex.
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj  = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        utillobj.active_run_fex_api_login("act-137a.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.1: Execute the act-137a.fex")
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report act-137a.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-137a.xlsx','Step 01.3: Expect to see the Active Report, displaying Packed decimal numbers for each of 5 Countries')
        
        
        def verify_riser_chart_X_labels(parent_id, expected_xval_list, msg):
            actual_val_list=[]
            
            parent="#" + parent_id + " svg > g"
            x=self.driver.find_elements_by_css_selector(parent + " text[class^='xaxis'][class*='labels']") 
            actual_val_list.extend([i.text for i in x])
            for label_x in expected_xval_list:
                if label_x[:4] in str(actual_val_list):
                    state= True
                else:
                    state=False
                    break
            utillobj.asequal(state, True, msg + " Verify the x-Axis labels.")       
        
        
        """
        Step 02: From the drop down control for Unit Sales, select Chart, then Column(Bar) and select Product for the Group By field.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Chart','Column','Product')

        miscelanousobj.verify_popup_appears('wall1', 'Unit Sales by Product','Step 02.1: Verify popup appears')
        time.sleep(3)
        miscelanousobj.move_active_popup('1', '600', '200')
        time.sleep(3)
        position = self.driver.find_element_by_css_selector('[id="win1"]').value_of_css_property('left')
        position_index = position[:-2]
        if int(position_index) > 0:
            print('Step 02.2: Expect to see the Bar Chart, positioned to the right of the Active Report - Passed')
        else:
            self.fail('Step 02.2: Expect to see the following Bar Chart, positioned to the right of the Active Report - Failed')

        """
        Step 03: Left click the Bar for Latte.
        """
        time.sleep(5)
        resultobj.create_lasso('wbody1_fmg','rect', 'riser!s0!g6!mbar')
        resultobj.select_or_verify_lasso_filter(verify=['1 point','Filter Chart','Exclude from Chart'],msg='Step 03: Expect to see the left-click options appear')
        
        """
        Step 04: Click the Exclude from Chart option.
        """
        time.sleep(5)
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        
        label_values=['Biscotti', 'Capucc', 'Coffee', 'Coffee', 'Croissant', 'Espresso', 'Mug', 'Scone', 'Thermos']
        
        
        
        verify_riser_chart_X_labels('wbody1_fmg', label_values, 'Step 04.1: Expect to see the Bar for Latte removed as well as the data for Latte removed from the report')
        expected_tooltip_list =['Unit Sales: 421K', 'X: Biscotti']
        miscelanousobj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mbar', expected_tooltip_list,'Step 04.1a: Expect to see the Bar for Latte removed as well as the data for Latte removed from the report')
        
        try:
            filter_icon = self.driver.find_element_by_css_selector(filter_val).is_displayed()
            utillobj.asequal(True,filter_icon,'Step 04.2: Expect to see the Filter icon appear at the top of the Bar Chart')
        except NoSuchElementException: 
            self.fail('Step 04.2: Expect to see the Filter icon appear at the top of the Bar Chart - Failed')
          
        
          
        """
        Step 05: Click the Filter icon at the top of the Bar Chart.
        """
        time.sleep(7)
        self.driver.find_element_by_css_selector(filter_val).click()
     
        time.sleep(5)
        label_values1=['Biscotti', 'Capucc', 'Coffee', 'Coffee', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        
        verify_riser_chart_X_labels('wbody1_fmg', label_values1, 'Step 05.1: Expect to see the Bar for Latte removed as well as the data for Latte removed from the report')
        
        expected_tooltip_list =['Unit Sales: 189K', 'X: Capuccino']
        miscelanousobj.verify_active_chart_tooltip('wall1', 'riser!s0!g1!mbar', expected_tooltip_list,'Step 05.1a: Expect to see the Bar for Latte removed as well as the data for Latte removed from the report')
        
        
        
        """
        Step 06: Exit the Active Report/Bar Chart screen. Execute the attached repro - act-137b.fex.
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("act-137b.fex", "S7215", 'mrid', 'mrpass')
        
        position_1 = self.driver.find_element_by_css_selector('[id="MAINTABLE_wbody0"]').value_of_css_property('left')
        position_index_1 = position_1[:-2]
        if int(position_index_1) == 0:
            print('Step 06.1: Expect to see the following Dashboard with an Active Report on the left - Passed')
        else:
            self.fail('Step 06.1: Expect to see the following Dashboard with an Active Report on the left - Failed')
            
        position_2 = self.driver.find_element_by_css_selector('[id="MAINTABLE_1"]').value_of_css_property('left')
        position_index_2 = position_2[:-2]
        if int(position_index_2) > 0:
            print('Step 06.2: Expect to see the following Dashboard with an Active Report on the left - Passed')
        else:
            self.fail('Step 06.2: Expect to see a Bar Chart on the right side - Failed')
        
        
            
        """
        Step 07: Left click the Bar for Food/Scone.
        """
        time.sleep(5)
        resultobj.create_lasso('MAINTABLE_wbody1_f','rect', 'riser!s0!g5!mbar')
        resultobj.select_or_verify_lasso_filter(verify=['1 point','Filter Chart','Exclude from Chart'],msg='Step 07: Expect to see the left-click options appear')
        
        """
        Step 08: Click the Exclude from Chart option.
        """
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(6)
       
        label_values2=['Coffee', 'Coffee', 'Coffee', 'Food/Bisc', 'Food/Croi', 'Gifts/Coff', 'Gifts/Coff', 'Gifts/Mug', 'Gifts/The']
        
        
        verify_riser_chart_X_labels('MAINTABLE_wbody1', label_values2, 'Step 08.1: Expect to see the Bar for Food/Scone removed as well as the data for Food/Scone removed from the report')
        
        
        expected_tooltip_list =['Sequence#, Gifts/Coffee Grinder: 863,014']
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody1', 'riser!s0!g5!mbar!', expected_tooltip_list,'Step 08.1a: Expect to see the Bar for Food/Scone restored')
        
        
        try:
            filter_icon = self.driver.find_element_by_css_selector(filter_val).is_displayed()
            utillobj.asequal(True,filter_icon,'Step 08.2: Expect to see the Filter icon appear at the top of the Bar Chart')
        except NoSuchElementException: 
            self.fail('Step 08.2: Expect to see the Filter icon appear at the top of the Bar Chart - Failed')
            
        """
        Step 09: Click the Filter icon at the top of the Bar Chart.
        """
        self.driver.find_element_by_css_selector(filter_val).click()
        time.sleep(6)
       
        
        label_values3=['Coffee/Ca', 'Coffee/Es', 'Coffee/Latte', 'Food/Bisc', 'Food/Croi', 'Food/Scone', 'Gifts/Coff', 'Gifts/Coff', 'Gifts/Mug', 'Gifts/The']
        
        
        verify_riser_chart_X_labels('MAINTABLE_wbody1', label_values3, 'Step 09: Expect to see the Bar for Food/Scone restored, as well as the data for Food/Scone on the report')
       
        expected_tooltip_list =['Sequence#, Food/Croissant: 1,481,273']
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody1', 'riser!s0!g4!mbar!', expected_tooltip_list,'Step 09.1a: Expect to see the Bar for Food/Scone restored')
        


if __name__ == "__main__":
    unittest.main()