'''
Created on May 16, 2019

@author: varun
Testcase Name : Mixed case search, across Fields, Variables
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261854
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from selenium.webdriver.common.keys import Keys
from common.locators.designer_chart_locators import DesignerChart as dc_locators

class C8261854_TestClass(BaseTestCase):
    
    def test_C8261854(self):
        
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        
        """
        Test case variables
        """
        dimensions_list = ['Product,Category', 'Product,Subcategory', 'ID Product', 'Product,Cost', 'Product,Description', 'Product Name', 'Product,Weight', 'Product,Weight,Units']
        pro_dimensions_list = ['Product,Category', 'Product,Subcategory', 'ID Product', 'Product,Cost', 'Product,Description', 'Product Name', 'Product,Weight', 'Product,Weight,Units', 'Store,State,Province,Capital']
        
        """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        
        """
        Step 2: Enter ProD in the search box
        """
        designer_chart_obj.enter_text_in_search_fields(text_to_search='ProD')
        designer_chart_obj.verify_fields_in_dimensions(dimensions_list, "Step 2.1: Verify the dimensions list")
        
        """
        Step 3: Click on the Variables tab
        """
        designer_chart_obj.select_fields_or_variables_in_datapane('Variables')
        designer_chart_obj.verify_variables_list(['Product Filter'], 'Step 3.1: Verify the variables list')
        
        """
        Step 4: Remove the D from the search so it is now Pro
        Notice Store Name is displayed because its name is actually STORE_PROMPT which contains string PRO
        """
        designer_chart_obj.enter_text_in_search_fields(send_keys=Keys.BACK_SPACE)
        designer_chart_obj.wait_for_number_of_element(dc_locators.VARIABLES_CSS, 2, designer_chart_obj.chart_short_timesleep)
        designer_chart_obj.verify_variables_list(['Product Filter', 'Store Name'], 'Step 4.1: Verify the variables list')
        
        """
        Step 5: Click on the Fields tab
        Notice more fields are listed as they contain string PRO but not PROD
        """
        designer_chart_obj.select_fields_or_variables_in_datapane('Fields')
        designer_chart_obj.verify_fields_in_dimensions(pro_dimensions_list, "Step 5.1: Verify the dimensions list", compare_type='asin')
        designer_chart_obj.verify_fields_in_measures(['Gross Profit,Local Currency', 'Gross Profit'], 'Step 5.2: Verify the Measures field')
        
        """
        Step 6: Sign out using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        
if __name__ == '__main__':
    unittest.main()