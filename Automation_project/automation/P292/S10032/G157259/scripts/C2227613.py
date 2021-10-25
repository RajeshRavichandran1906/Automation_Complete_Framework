'''
Created on May 16, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227613
TestCase Name = Lasso Filter with Grid
'''

import unittest,time
from common.lib import utillity
from common.wftools.visualization import Visualization
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_run, ia_run
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227613_TestClass(BaseTestCase):

    def test_C2227613(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227613'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        visual = Visualization(self.driver)
        
        """
        Step 02: Click "Change" in the Home Tab > Select "Scatter" chart type
        """
        ribbonobj.change_chart_type("grid")
         
        """
        Step 03: Double-click "Cost of Goods " and "Product,Category"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        heading = ['Product Category', 'Cost of Goods',]
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 03.1: Verify column titles')
        row_val=['Accessories', '$89,753,898.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 03.2: verify grid 1st row value')
        
        """
        Step 04:  Lasso "Cost of Goods" values for Camcorder, Computer, and Media Player > Select "Filter Chart"
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g0!mcellFill!r1!c0!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        visual.create_lasso_using_action_chain("rect[class*='riser!s0!g0!mcellFill!r1!c0!']", "rect[class*='riser!s0!g0!mcellFill!r3!c0!']")
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(5)
        
        """
        Step 05: Verify Preview
        """
        metaobj.verify_filter_pane_field('Product,Category',1,"Step05.a:")
        time.sleep(8)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        heading = ['Product Category', 'Cost of Goods',]
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 05.1: Verify column titles')
        row_val=['Camcorder', '$104,866,857.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 05.2: verify grid 1st row value')
        
        """
        Step 06: Click Run > Verify output
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        chart_type_css="rect[class*='riser!s0!g0!mcellFill!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        time.sleep(5)
        heading = ['Product Category', 'Cost of Goods',]
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 06.1: Verify column titles')
        row_val=['Camcorder', '$104,866,857.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 06.2: verify grid 1st row value')
        
        """
        Step 07: Expand the runtime menu in the lower right corner > select show data grid icon
        """
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        time.sleep(6)
        
        """
        Step 08: Verify output
        """
        time.sleep(5)
#         iarunobj.create_table_data_set('#MAINTABLE_wbody2 table table', "C2227613.xlsx")
        iarunobj.verify_table_data_set('#MAINTABLE_wbody2 table table', "C2227613.xlsx", 'Step 08: verify grid')
        
        """
        Step 09: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 10: Click "Save" > Save as "C2167765" > click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 12: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 13: Verify Preview 
        """
        time.sleep(8)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step13.a:")
        heading = ['Product Category', 'Cost of Goods',]
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 13.1: Verify column titles')
        row_val=['Camcorder', '$104,866,857.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 13.2: verify grid 1st row value')
        
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()