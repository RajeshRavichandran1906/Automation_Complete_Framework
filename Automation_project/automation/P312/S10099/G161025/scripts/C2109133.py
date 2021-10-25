'''
Created on June17, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109133&group_by=cases:section_id&group_id=147037&group_order=asc
TestCase Name : IA-4248:BUE: Toottip doesn't go away after selecting filter (cache?)
'''
import unittest, time
from selenium.webdriver.common.by import By
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, core_metadata

class C2109133_TestClass(BaseTestCase):

    def test_C2109133(self):
         
        """
        TESTCASE OBJECTS
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_metaobj = core_metadata.CoreMetaData(self.driver)
        core_utils  = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109133'
        
        """
        Step 01: Launch the IA API with Customer_Data (Folder - S8404 and Master - customer_data) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/Customer_Data&item=IBFS%3A%2FWFC%2FRepository%2FS404%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/customer_data','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click "Transactions" and "Sales Region"
        """
        metaobj.datatree_field_click('Measure Groups->Sheet1->Transactions', 2, 1)
        time.sleep(5)
        core_metaobj.collapse_data_field_section('Measure Groups')
        time.sleep(5)
        metaobj.datatree_field_click('Dimensions->Sheet1->Sales->Sales Region', 2, 1)
        time.sleep(5)
        
        """
        Step 03: Verify label values.
        """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step 03.01: Verify the total number of risers displayed on live preview Chart')
        expected_xval_list=['Canada', 'Central', 'Eastern', 'Southern', 'Western']
        expected_yval_list=['0', '400', '800', '1,200', '1,600', '2,000']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 03.03: Verify first bar color")
        xaxis_value="Sales Region"
        yaxis_value="Transactions"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 03.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 03.05: Verify Y-Axis Title")
        
        """
        Step 04: Verify query pane
        """
        metaobj.verify_query_pane_field("Horizontal Axis", "Sales Region", 1, "Step 04.01: ")
        metaobj.verify_query_pane_field('Vertical Axis', "Transactions", 1, "Step 04.02: ")
        
        """
        Step 05: Verify all bar riser values
        """
        expected_tooltip=['Sales Region:Canada', 'Transactions:334', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sales Branch']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 05.01: verify the default tooltip values")
        
        """
        Step 06:  Lasso select 2 columns (Canada and Central) in preview > Filter
        """
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g1!mbar!')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 50).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(1)
        parent_css="#qbFilterBox table>tbody>tr img"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_filter_pane_field("Sales Region", 1,"Step 06.01: verify query added to filter pane")
        
        
        """
        Step 07: Verify tooltip values
        """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 07.01: Verify the total number of risers displayed on live preview Chart')
        expected_tooltip=['Sales Region:Canada', 'Transactions:334', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sales Branch']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 07.02: verify the default tooltip values")
        expected_tooltip=['Sales Region:Central', 'Transactions:1634', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sales Branch']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 07.03: verify the default tooltip values")
        
        """
        Step 08: Click run in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)     
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """
        Step 09: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 09.01: Verify the total number of risers displayed on Run Chart')
#         time.sleep(15)
#         utillobj.take_screenshot(driver.find_element_by_css_selector(" #orgdiv0"),'C2109133_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        x_val_list=['Canada', 'Central']
        y_val_list=['0', '400', '800', '1,200', '1,600', '2,000']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 09.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 09.03: Verify first bar color")
        xaxis_value="Sales Region"
        yaxis_value="Transactions"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09.05: Verify Y-Axis Title")
        expected_tooltip=['Sales Region:Central', 'Transactions:1634', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sales Branch']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 09.06: verify the default tooltip values")
        
        """
        Step 10: Close the output window.
        """
        core_utils.switch_to_previous_window()
        elem1=(By.ID, 'applicationButton')
        resultobj._validate_page(elem1)
        
        """
        Step 11: Click "Save" in the toolbar > Type C2109133 > Click "Save" in the Save As dialog
        """
        time.sleep(2)  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step 12: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()