'''
Created on Mar 15, 2017

@author: Magesh

Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227561
TestCase Name = Verify restore Compute field in Chart mode
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata, visualization_resultarea, define_compute
from common.lib import utillity
import unittest,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class C2227561_TestClass(BaseTestCase):

    def test_C2227561(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        def_comp = define_compute.Define_Compute(self.driver)
        
        Test_Case_ID = "C2227561"
        
        """
        Step 01: Launch IA Chart mode: 
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """ 
        utillobj.infoassist_api_login('chart', 'baseapp/wf_retail_lite', 'P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
              
        """
        Step 02: Double click "Revenue","Product,Category".
        """
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css1="#TableChart_1 svg g text[class='yaxis-title']"
        utillobj.synchronize_with_number_of_element(parent_css1, 1, 30)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02:d(iii): _")
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 02a: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar", "bar_blue1", "Step 02.c(i) Verify first bar color")
         
        """
        Step 03: Select "Data" > "Summary (Compute)".
        Step 04: Enter "Field" = "NewRevenue".
        Step 05: Double click "Revenue".
        """
        def_comp.invoke_define_compute_dialog('Compute')
        time.sleep(2)
        parent_css="#defineMetaData"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        def_comp.enter_define_compute_parameter('NewRevenue', 'D12.2', 'Revenue', 1)
         
        """
        Step 06: Enter "+ 9999999" into the textbox.
        Step 07: Click "OK".
        """
        time.sleep(3)
        def_comp.select_calculation_btns('plus')
        def_comp.select_calculation_btns('nine')
        def_comp.select_calculation_btns('nine')
        def_comp.select_calculation_btns('nine')
        def_comp.select_calculation_btns('nine')
        def_comp.select_calculation_btns('nine')
        def_comp.select_calculation_btns('nine')
        def_comp.select_calculation_btns('nine')
        time.sleep(2)
        def_comp.close_define_compute_dialog('ok')
        time.sleep(2)
         
        """
        Step 08: Verify the following chart is displayed.
        """
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 08: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 08: Verify chart_XY_labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 08: Verify the total number of risers displayed on Run Chart')
        resultobj.verify_riser_legends("TableChart_1", ['Revenue','NewRevenue'], "Step 08: Verify legend Title")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar", "bar_blue1", "Step 08: Verify bar color")
         
        """
        Step 09: Click Run:
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
         
        """
        Step 10: Verify the following chart is displayed.
        """
        frame_obj=driver.find_element_by_css_selector('[id^=ReportIframe-]')
        x_fr=frame_obj.location['x']
        y_fr=frame_obj.location['y']
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        parent_css="#jschart_HOLD_0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 10: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 10: Verify chart_XY_labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 14, 'Step 10: Verify the total number of risers displayed on Run Chart')
        resultobj.verify_riser_legends("jschart_HOLD_0", ['Revenue','NewRevenue'], "Step 10: Verify legend Title")
        expected_tooltip=['Product Category:Stereo Systems', 'Revenue:$291,294,933.52']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g4!mbar",expected_tooltip, "Step 10: verify the default tooltip values", x_offset=x_fr,y_offset=y_fr-7)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mbar", "bar_blue1", "Step 10: Verify bar color")
        driver.switch_to_default_content()
        
        """
        Step 11: Highlight "NewRevenue" > Right mouse click > "Edit Compute".
        Step 12: Enter "Field" = "NewRevenue_1".
        Step 13: Click "OK".
        """
        time.sleep(6)
        metaobj.querytree_field_click('NewRevenue',1,0)
        time.sleep(3)
        metaobj.querytree_field_click('NewRevenue',1,1,'Edit Compute')
        parent_css="#defineMetaData"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        time.sleep(5)
        field_name = driver.find_element_by_css_selector("div[id^='BiVBox'] input[id='fname']") 
        utillobj.set_text_field_using_actionchains(field_name,'NewRevenue_1')
        time.sleep(3)
        def_comp.close_define_compute_dialog('ok')
        time.sleep(2)
        
        """
        Step 14: Verify the following chart is displayed.
        """
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 14: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 14: Verify chart_XY_labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 14: Verify the total number of risers displayed on Run Chart')
        resultobj.verify_riser_legends("TableChart_1", ['Revenue','NewRevenue_1'], "Step 14: Verify legend Title")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar", "bar_blue1", "Step 14: Verify bar color")
        
        """
        Step 15: Click "IA" > "Save".
        Step 16: Enter Title = "C2227561".
        Step 17: Click "Save".
        """
        time.sleep(5)
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
        
        """
        Step 19: Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227561.fex&tool=Chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        
        """
        Step 20: Verify Chart on "Live Preview".
        """
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 20: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 20: Verify chart_XY_labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 20: Verify the total number of risers displayed on Run Chart')
        resultobj.verify_riser_legends("TableChart_1", ['Revenue','NewRevenue_1'], "Step 20: Verify legend Title")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar", "bar_blue1", "Step 20: Verify bar color")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,'C2227561_Actual_step20', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 21: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
                   
if __name__ == "__main__":
    unittest.main()