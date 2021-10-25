'''
Created on Nov 28, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2349140
TestCase Name = Verify Hold with Chart mode
'''
import unittest
import time, re
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2349140_TestClass(BaseTestCase):

    def test_C2349140(self):
        
        Test_Case_ID = "C2349140"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)       
        
        """ 
            Step 01Launch IA Chart mode:
            http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(15)
  
        """
            Step 02:Double-click "Product,Category", "Cost of Goods", and "Revenue" 
        """        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Revenue", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Revenue', with_regular_exprestion=True,expire_time=50)
        time.sleep(5)
        resobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 02.1: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.2: Verify XY Label')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 02.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 02.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 02.5: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 02.6: Verify the total number of risers displayed on preview')
        
        """
            Step 03:Verify "File" option is disabled in the Home Tab ribbon for default format HTML5
        """
        css="#HomeDestFile"       
        status = bool(self.driver.find_element_by_css_selector(css).get_attribute("disabled"))
        utillobj.asequal(True, status, "Step 03: Verify file option is disabled in the Home tab")
        
        """
            Step 04:Click the HTML5 format button > Select HTML
        """
        ribbonobj.change_output_format_type('charthtml')
        parent_css="div[id*='LayoutChartObjectDrawLayer']"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        ele=driver.find_element_by_css_selector("div[id*='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2) 

        """
            Step 05:Verify "File" becomes enabled
        """
        css="#HomeDestFile"       
        status = bool(self.driver.find_element_by_css_selector(css).get_attribute("disabled"))
        utillobj.asequal(False, status, "Step 05: Verify file option is enabled in the Home tab")
 
        """
            Step 06:Click "File" 
        """
        ribbonobj.select_ribbon_item('Home', 'File')
  
        """
            Step 07:Click "Save" in the File dialog
         
        """
        utillobj.expand_domain_folders_in_open_dialog('foccache')
        utillobj.ibfs_save_as("File1")
  
        """
            Step 08:Verify Chart
        """
        parent_css="div[id*='LayoutChartObjectDrawLayer']"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        ele=driver.find_element_by_css_selector("div[id*='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_08', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2) 
         
        """
            Step 09:Click "Save" > Save As "C2349140" > Click "Save" 
        """
        time.sleep(6)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
  
        """
            Step 10:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
  
        """
            Step 11:Reopen saved FEX:
                    http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235511.fex&tool=Chart
        """
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        parent_css="div[id*='LayoutChartObjectDrawLayer']"
        resobj.wait_for_property(parent_css, 1)
        """
            Step 12:Verify successful restore
        """
        time.sleep(5)
        ele=driver.find_element_by_css_selector("div[id*='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2) 

        """
            Step 13:Click Run > Verify message displayed
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_css="div[class='errorMain']"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(2)
        actual_data=driver.find_element_by_css_selector("div[class*='errorMain']").text.strip().split('\n')
        expected_data=['No output was returned']
        utillobj.asequal(actual_data, expected_data, 'Step 13.1: Expect to see just the HOLD output, no Active output.')
        time.sleep(2)
        actual_hold_data=driver.find_element_by_css_selector("div[class='errorDetail']").text.strip().replace('\n', '')
        hold_data = re.sub(' ', '', actual_hold_data)
        expected_hold_data = 'Possiblecauses:-OutputwasdirectedtoadestinationsuchasafileorprinterDetail:0NUMBEROFRECORDSINGRAPH=7PLOTPOINTS=7PNGFILESAVED...'
        utillobj.asequal(hold_data, expected_hold_data, 'Step 13.2: All requests should give0 NUMBER OF RECORDS IN GRAPH =7 PLOT POINTS=7PNG FILE SAVED...')
        
        """
            Step 14:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
 
if __name__ == '__main__':
    unittest.main()
