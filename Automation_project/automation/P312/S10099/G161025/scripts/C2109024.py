'''
Created on June16, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109024&group_by=cases:section_id&group_id=147037&group_order=asc
TestCase Name : IA-4319:Lasso on date field doesn't work at design time
'''
import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, active_miscelaneous
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from common.wftools.visualization import Visualization

class C2109024_TestClass(BaseTestCase):

    def test_C2109024(self):
       
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109024'
        visual = Visualization(self.driver)
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
       
        """
        Step 01: Launch the IA API with Employee (Folder - S8404 and Master - employee) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/EMPLOYEE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        visual.invoke_visualization_using_api('ibisamp/employee')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
      
        """
        Step 02: Double click CURR_SAL & HIRE_DATE
        """
        visual.double_click_on_datetree_item('CURR_SAL', 1)
        parent_css="#queryTreeWindow"
        visual.wait_for_visible_text(parent_css, 'CURR_SAL')
        visual.double_click_on_datetree_item('HIRE_DATE', 1)
        visual.wait_for_visible_text(parent_css, 'HIRE_DATE')
        
        """
        Step 03: Verify label values.
        """
        elem=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 text[class^='xaxis'][class$='title']")
        utillobj._validate_page(elem)
        time.sleep(3)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 9, 'Step 03.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['80/06/02', '81/07/01', '81/11/02', '82/01/04', '82/02/02', '82/04/01', '82/05/01', '82/07/01', '82/08/01']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K']
        
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.03: Verify first bar color")
        xaxis_value="HIRE_DATE"
        yaxis_value="CURR_SAL"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03.05: Verify Y-Axis Title")       
        
        """
        Step 04: Verify query pane
        """
        metaobj.verify_query_pane_field('Horizontal Axis','HIRE_DATE',1,"Step 04.01")
        metaobj.verify_query_pane_field('Vertical Axis', 'CURR_SAL',1,"Step 04.02")
        
        """
        Step 05:  lasso the 2 bars from 1982(82/02/02 and 82/04/01)> filter chart
        """
        time.sleep(8)
        
        resultobj.create_lasso('MAINTABLE_wbody1', 'rect','riser!s0!g4!mbar',target_tag='rect', target_riser='riser!s0!g5!mbar')
        time.sleep(2)
        miscelanousobj.select_active_lasso_menu('Filter Chart')
        
        time.sleep(8)
        """
        Step 06: Verify query added to filter pane.
        """
        elem=(By.CSS_SELECTOR,'#qbFilterBox table>tbody>tr img')
        utillobj._validate_page(elem)
        metaobj.verify_filter_pane_field('HIRE_DATE',1,"Step 06.01: Verify query added to filter pane.")
        
        """
        Step 07: verify bar riser values in preview
        """
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css, 2)
        expected_xval_list=['82/02/02', '82/04/01']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07.01: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 07.02: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.03: Verify bar color") 
        time.sleep(8)
        a=['HIRE_DATE:82/02/02', 'CURR_SAL:$16,100.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',a,"Step 07.04: verify bar riser values in preview")
        
        """
        Step 08: Right click HIRE_DATE in filter pane > Edit
        """
        time.sleep(4)
        metaobj.filter_tree_field_click('HIRE_DATE', 1, 1, 'Edit...')
        time.sleep(8)
        
        """
        Steo 09: Verify filter dialog (82/02/02 and 82/04/01 values only to be checked)
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        utillobj._validate_page(elem)
        
        l= ['82/02/02', '82/04/01']        
        metaobj.select_or_verify_visualization_filter_values(l, verify="true", Ok_button=True)
         
        """
        Step 10: Click run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()       
         
        """
        Step 11: Verify output
        """
        raiser="div[id*='ibi$container$inner$HBOX_1']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(8)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 11.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['82/02/02', '82/04/01']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11.02: X and Y axis Scales Values has changed or NOT')
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.03: Verify bar color")
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', ['HIRE_DATE:82/02/02', 'CURR_SAL:$16,100.00', 'Filter Chart', 'Exclude from Chart'],"Step 11.04: Verify Output has two bars")

        """
        Step 12: Close the output window.
        """
        visual.switch_to_previous_window()

        """
        Step 13: Click "Save" in the toolbar > Type C2109024 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
         
        """
        Step 14: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
         
if __name__ == '__main__':
    unittest.main()