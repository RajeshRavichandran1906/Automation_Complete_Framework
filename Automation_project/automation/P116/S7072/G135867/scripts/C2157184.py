'''
Created on Aug 04, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2157184
TestCase Name = This test verifies that margins may be added to an Active Report.
Keywords used by InfoAssist are: TOPMARGIN, BOTTOMMARGIN, LEFTMARGIN & RIGHTMARGIN.
There will be tests for default(no settings), 4 preset margin configurations and for user defined Custom margins.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
import re

class C2157184_TestClass(BaseTestCase):

    def test_C2157184(self):
        def run_chart_checkpoint(msg,x=0,y=0):
            time.sleep(5)
            resultobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 20, msg + 'run a: Verify the total number of risers displayed on Run Chart')
            legends = ['Unit Sales', 'Dollar Sales']
            msg1= msg + "run b: Verify the Legends - Unit Sales, Dollar Sales displayed on Run chart"
            resultobj.verify_riser_legends("MAINTABLE_wbody0_f", legends, msg1)
            expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone', 'Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug', 'Gifts : Thermos']
            expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
            resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, msg + 'run c: X annd Y axis Scales Values has changed or NOT')
            utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "bar_blue", msg + ".c(i) Verify first bar color")
            utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s1!g1!mbar!", "pale_green", msg + ".c(ii) Verify second bar color")
            driver.switch_to_default_content()
            time.sleep(1)
            element = self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
            utillobj.take_screenshot(element, 'C2157184_Actual_' + msg + 'run', image_type='actual',x=2, y=2, w=-2, h=-2)
            utillobj.switch_to_frame(pause=2)
            time.sleep(1)
#             a=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063']    
#             b=['Category:Gifts', 'Product:Mug', 'Dollar Sales:4522521']
#             resultobj.verify_chart_tooltip_values(0, "riser!s0!g2!mbar!", a, msg + "run .d: Verify Category, Product and Unit Sales value from Top",x_offset=x,y_offset=y)
#             time.sleep(2)
#             resultobj.verify_chart_tooltip_values(0, "riser!s1!g8!mbar!", b, msg + "run .e: Verify Category, Product and Dollar Sales value from Bottom",x_offset=x,y_offset=y)
            time.sleep(2)
            
            expected_list = ['More Options', 'Advanced Chart', 'Original Chart']     
            x = driver.find_elements_by_css_selector("#MAINTABLE_wmenu0>table td:nth-child(1)>table>tbody>tr>td>div")
            Actual_list=[]
            for i in range(len(x)):
                lineObjbj = re.match(r'(\S.*)?.*', x[i].get_attribute("title"))
                Actual_list.append(lineObjbj.group(1))
            utillity.UtillityMethods.asequal(self,Actual_list, expected_list, msg + 'run.f(i): Verifying the Menu Bar icons on Run chart')
            s = driver.find_element_by_css_selector(".tabPagingText1 > div > table > tbody > tr > td[title='Aggregation']").is_displayed()
            utillity.UtillityMethods.asequal(self,True, s, msg + "run.f(ii): verify Aggregation icon")
            time.sleep(2)
            
        """
            Step 01a:    Start an InfoAssist session, create a new Chart and select the ggsales file.
            Step 01b:    Change the output Format to AHTML.
            Step 01c:    Select Category & Product for the Dimensions and Unit Sales & Dollar Sales as the Measures
            Step 01d:    Select Run button"""
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P116/S7072', 'mrid', 'mrpass')
        
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        
        browser = utillobj.parseinitfile('browser')
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        '''driver.find_element_by_id("HomeFormatType").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#menu_ahtml_btn img").click()
        time.sleep(4)'''
        metaobj.datatree_field_click("Category",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Product",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Dollar Sales",2,1)
        time.sleep(15)
        '''
        VP:::: Verifying the X axis label on Preview chart
        '''
        xaxis = self.driver.find_element_by_xpath("//*[contains(@class,'xaxis')and contains(@class,'title')]")
        utillity.UtillityMethods.asequal(self,xaxis.text, 'Category : Product', "Step 1.a Verify X Label on preview Chart")
        legends = ['Unit Sales', 'Dollar Sales']
        msg1="Step 1.b Verify the Legends - Unit Sales, Dollar Sales displayed on Preview chart"
        resultobj.verify_riser_legends("TableChart_1", legends, msg1)
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 1.c(i) Verify first bar color")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s1!g1!mbar!", "bar_green", "Step 1.c(ii) Verify second bar color")
        x_labels=['Coffee : Capuccino', 'Coffee : Espresso']
        y_labels=['0', '0.5M','1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels("pfjTableChart_1", x_labels, y_labels, "Step 1.d: ")
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)                 
        run_chart_checkpoint("Step01",x_fr,y_fr-8)
        
        """Step 02:Click the Layout tab at the top, then select Margins.
        Click the first option - Normal (pixels all around).
        Click the Run button. """
        utillobj.switch_to_default_content(pause=2)
        time.sleep(4)
        ribbonobj.select_ribbon_item('Layout', 'Margins', opt='Normal (pixels all round)')
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_run')    
        time.sleep(10)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        run_chart_checkpoint("Step02",x_fr,y_fr-8)
        utillobj.switch_to_default_content(pause=2)
        
        """Step 03: Check the code for the first option by clicking the View Code button at the top.
        Scroll to the bottom of the procedure."""
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'LEFTMARGIN=2.54, TOPMARGIN=2.54, RIGHTMARGIN=2.54, BOTTOMMARGIN=2.54'
        vp_text = 'Step 3. Verify the following code - LEFTMARGIN=2.54 (all in pixels)1, TOPMARGIN=2.54, RIGHTMARGIN=1,RIGHTMARGIN=2.54..BOTTOMMARGIN=2.54'
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        driver.switch_to_default_content()
        time.sleep(2)
                
        """
            Step 04 :Click the OK button on the Current Focexec Content screen.
            Click the Layout tab at the top, then select Margins.
            Click the second option - Narrow (pixels around).
            Click the Run button. """
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.default_click(close_fexcode_btn)
#         if browser == 'Firefox':
#             utillity.UtillityMethods.click_type_using_pyautogui(self, close_fexcode_btn, 0, -7, leftClick=True)
#         else:
#             close_fexcode_btn.click()        
        time.sleep(4)
        #driver.find_element_by_css_selector("#showFexOKBtn img").click()
        time.sleep(4)
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Narrow (pixels round)")
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        run_chart_checkpoint("Step04",x_fr,y_fr-8)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'LEFTMARGIN=1.27, TOPMARGIN=1.27, RIGHTMARGIN=1.27, BOTTOMMARGIN=1.27'
        vp_text = 'Step 4 VP.8. Verify the following code - LEFTMARGIN=1.27 (all in pixels), TOPMARGIN=1.27, RIGHTMARGIN=1.27,RIGHTMARGIN=1.27.BOTTOMMARGIN=1.27'
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
       
        """Step 05 : Click the OK button on the Current Focexec Content screen.
        Click the Layout tab at the top, then select Margins.
        Click the third option - Moderate (pixels left/right).
        Click the Run button. """
        time.sleep(4)
        driver.switch_to_default_content()
        #driver.find_element_by_css_selector("#showFexOKBtn img").click()
        time.sleep(2)
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.default_click(close_fexcode_btn)
#         if browser == 'Firefox':
#             utillity.UtillityMethods.click_type_using_pyautogui(self, close_fexcode_btn, 0, -7, leftClick=True)
#         else:
#             close_fexcode_btn.click()        
        time.sleep(4)
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Moderate (pixels left/right)")
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        run_chart_checkpoint("Step05",x_fr,y_fr-8)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'LEFTMARGIN=1.27, RIGHTMARGIN=1.27'
        vp_text = 'Step 5 VP.8. Verify the following code - LEFTMARGIN=1.27 (all in pixels), TOPMARGIN=1.27, RIGHTMARGIN=1.27,RIGHTMARGIN=1.27.BOTTOMMARGIN=1.27'
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        
        """Step 06: Click the OK button on the Current Focexec Content screen.
        Click the Layout tab at the top, then select Margins.
        Click the fourth option - Wide (pixels left/right).
        Click the Run button. """
        time.sleep(4)
        utillobj.switch_to_default_content(pause=2)
        #driver.find_element_by_css_selector("#showFexOKBtn img").click()
        time.sleep(2)
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.default_click(close_fexcode_btn)
#         if browser == 'Firefox':
#             utillity.UtillityMethods.click_type_using_pyautogui(self, close_fexcode_btn, 0, -7, leftClick=True)
#         else:
#             close_fexcode_btn.click()        
        time.sleep(4)
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Wide (pixels left/right)")
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        run_chart_checkpoint("Step06",x_fr,y_fr-8)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2) 
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'LEFTMARGIN=3.81, RIGHTMARGIN=3.81'
        vp_text = 'Step 6 VP.8. Verify the following code - LEFTMARGIN=3.81 (all in pixels),  RIGHTMARGIN=3.81,RIGHTMARGIN=3.81'
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        
        
        """Step 07: Click the OK button on the Current Focexec Content screen.
        Click the Layout tab at the top, then select Margins.
        Click the fifth option - Custom"""
        time.sleep(4)
        driver.switch_to_default_content()
        #driver.find_element_by_css_selector("#showFexOKBtn img").click()
        time.sleep(4)
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.default_click(close_fexcode_btn)
#         if browser == 'Firefox':
#             utillity.UtillityMethods.click_type_using_pyautogui(self, close_fexcode_btn, 0, -7, leftClick=True)
#         else:
#             close_fexcode_btn.click()        
        time.sleep(4)
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Custom")
        time.sleep(8)
        input_top = driver.find_element_by_css_selector("#qbMarginsDlg #topMargin")
        otop = input_top.get_attribute("value")
        input_bottom = driver.find_element_by_css_selector("#qbMarginsDlg #bottomMargin")
        obottom = input_bottom.get_attribute("value")
        input_left = driver.find_element_by_css_selector("#qbMarginsDlg #leftMargin")
        oleft = input_left.get_attribute("value")
        input_right = driver.find_element_by_css_selector("#qbMarginsDlg #rightMargin")
        oright = input_right.get_attribute("value")
        vp_text1 = 'Step 07a: Notice that the last set of values selected, still appear, 3.81 inch for the Left and Right positions'
        vp_text2 = 'Step 07b: Notice that the last set of values selected, still appear, 0 inch for the top and bottom positions'
        vp1=oleft == oright == '3.81'
        utillity.UtillityMethods.asequal(self,True, vp1, vp_text1)
        vp2=otop == obottom == '0.0'
        utillity.UtillityMethods.asequal(self,True, vp2, vp_text2)
        
        """Step 08: Enter 50 pixels for all Margin settings.
        Click the OK button.
        Click the Run button"""
        input_top.clear()
        input_top.send_keys('50')
        time.sleep(3)
        input_bottom.clear()
        input_bottom.send_keys('50')
        time.sleep(3)
        input_left.clear()
        input_left.send_keys('50')
        time.sleep(3)
        input_right.clear()
        input_right.send_keys('50')
        time.sleep(3)
        driver.find_element_by_css_selector("#qbMarginsDlg #marginApplyBtn").click()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        run_chart_checkpoint("Step08",x_fr,y_fr-8)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2) 
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'LEFTMARGIN=50, TOPMARGIN=50, RIGHTMARGIN=50, BOTTOMMARGIN=50'
        vp_text = 'Step 8 VP.8. Verify the following code - LEFTMARGIN=3.81 (all in pixels),  RIGHTMARGIN=3.81,RIGHTMARGIN=3.81'
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text) 
        time.sleep(4)
        driver.switch_to.default_content()
        time.sleep(2)  
        #driver.find_element_by_css_selector("#showFexOKBtn img").click()
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.default_click(close_fexcode_btn)
#         if browser == 'Firefox':
#             utillity.UtillityMethods.click_type_using_pyautogui(self, close_fexcode_btn, 0, -7, leftClick=True)
#         else:
#             close_fexcode_btn.click()        
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("C2157184")
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()
