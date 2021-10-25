'''
Created on July 26, 2019

@author: AA14564
Testcase Name : Testing URL to run PGX
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/5587443
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools.login import Login
from common.wftools.page_designer import Run
from common.wftools.chart import Chart

class C5587443_TestClass(BaseTestCase):

    def test_C5587443(self):
        
        """ TESTCASE OBJECT'S  """
        utillobj = utillity.UtillityMethods(self.driver)
        login = Login(self.driver)
        pd_run = Run(self.driver)
        chart = Chart(self.driver)
        
        """ TESTCASE VARIABLES  """
        SETUP_URL = login.create_setup_url().replace("home8206", "")
        URL_PATH = "{0}run/ibfs/WFC/Repository/Retail_Samples/InfoApps/Sales_Dashboard_Filtered".format(SETUP_URL)
        PAGE_CANVAS = ".pd-page-canvas"
        
        """ Step 1: Run Sales_Dashboard_Filtered page present in Retail_Samples > InfoApps folder using following API:
                    http://machine:port/alias/run/ibfs/WFC/Repository/Retail_Samples/InfoApps/Sales_Dashboard_Filtered
                    Verify that you see the signin page.
        """
        self.driver.get(URL_PATH)
        
        """ Step 2: Login as WF domain developer.
                    Verify the page runs with no issues.
        """
        login.login_page('mriddev', 'mrpassdev')
        ''' Verify Category Sales'''
        utillobj.synchronize_with_visble_text(PAGE_CANVAS, 'Category Sales', pd_run.home_page_long_timesleep)
        pd_run.switch_to_container_frame('Category Sales', timeout=pd_run.home_page_long_timesleep)
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 text[class*='legend-title']", pd_run.home_page_long_timesleep)
        chart.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['Product Category'], 'Step 01.00: Verify Category Sales labels.', same_group=True, custom_css="text[class*='legend-title']")
        pd_run.switch_to_default_page()
        
        ''' Verify Regional Sales Trend'''
        utillobj.synchronize_with_visble_text(PAGE_CANVAS, 'Regional Sales Trend', pd_run.home_page_long_timesleep)
        pd_run.switch_to_container_frame('Regional Sales Trend', timeout=pd_run.home_page_long_timesleep)
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 text[class^='xaxis'][class$='title']", pd_run.home_page_long_timesleep)
        chart.verify_x_axis_title_in_run_window(['Month'], msg='Step 01.01: Verify Regional Sales Trend.')
        pd_run.switch_to_default_page()
        
        ''' Verify Discount by Region '''
        utillobj.synchronize_with_visble_text(PAGE_CANVAS, 'Discount by Region', pd_run.home_page_long_timesleep)
        pd_run.switch_to_container_frame('Discount by Region', timeout=pd_run.home_page_long_timesleep)
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 text[class^='xaxis'][class$='title']", pd_run.home_page_long_timesleep)
        chart.verify_x_axis_title_in_run_window(['Sale Quarter'], msg='Step 01.02')
        pd_run.switch_to_default_page()
        
        ''' Verify Regional Profit by Category'''
        utillobj.synchronize_with_visble_text(PAGE_CANVAS, 'Regional Profit by Category', pd_run.home_page_long_timesleep)
        pd_run.switch_to_container_frame('Regional Profit by Category', timeout=pd_run.home_page_long_timesleep)
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 text[class^='yaxis'][class$='title']", pd_run.home_page_long_timesleep)
        chart.verify_x_axis_title_in_run_window(['Gross Profit'], x_or_y_axis_title_css="text[class^='yaxis'][class$='title']", msg='Step 01.03')
        pd_run.switch_to_default_page()
        
        ''' Verify Example of a Tab Container'''
        utillobj.synchronize_with_visble_text(PAGE_CANVAS, 'Example of a Tab Container', pd_run.home_page_long_timesleep)
        pd_run.switch_to_container_frame('Example of a Tab Container', timeout=pd_run.home_page_long_timesleep)
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 text[class*='legend-title']", pd_run.home_page_long_timesleep)
        chart.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['Store Business Region'], 'Step 01.04: Verify Example of a Tab Container.', same_group=True, custom_css="text[class*='legend-title']")
        pd_run.switch_to_default_page()
        
        ''' Verify Example of a Carousel Container'''
        utillobj.synchronize_with_visble_text(PAGE_CANVAS, 'Example of a Carousel Container', pd_run.home_page_long_timesleep)
        pd_run.switch_to_container_frame('Example of a Carousel Container', timeout=pd_run.home_page_long_timesleep)
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 [class$='title']", pd_run.home_page_long_timesleep)
        chart.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['Gross Profit'], 'Step 01.05: Verify Example of a Carousel Container.', same_group=True, custom_css="[class$='title']")
        pd_run.switch_to_default_page()
        
        ''' Verify page title'''
        actual_page = utillobj.validate_and_get_webdriver_object(".pd-page-title", 'Page title').text.strip()
        utillobj.asequal('Retail Sales Dashboard', actual_page, 'Step 01.06: Verify page title.')
        
        """ Step 3: Sign out WF. 
        """
        
if __name__=='__main__' :
    unittest.main()