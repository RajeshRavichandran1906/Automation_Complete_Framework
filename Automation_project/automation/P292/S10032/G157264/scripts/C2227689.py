'''
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2227689

'''

import unittest, time
from common.wftools import visualization
from selenium.webdriver.common import keys
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.pages import visualization_ribbon,visualization_resultarea,ia_styling
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2227689_TestClass(BaseTestCase):
    
    def test_C2227689(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227689'
        expected_xval_list = ['2011', '2012', '2013', '2014', '2015', '2016'] 
#         expected_xval_list=['2016', '2017', '2018', '2019', '2020', '2021']
        expected_yval_list=['0', '0.4B', '0.8B', '1.2B','1.6B', '2B', '2.4B']
        oLegends=['Cost of Goods Local Currency','Cost of Goods']
        
        """
            CLASS & OBJECTS
        """
        driver = self.driver #Driver reference object created
        ia_styobj = ia_styling.IA_Style(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        vis_obj = visualization.Visualization(self.driver)
        coreutillobj = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """    
            STEP 01 : Launch the IA API with wf_retail_lite, Visualization mode:
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    
            STEP 02 : Drag "Cost of Goods,Local Currency" to Vertical Axis.    
        """
        vis_obj.drag_field_from_data_tree_to_query_pane("Cost of Goods,Local Currency", 1, 'Vertical Axis')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", 'Cost of Goods Local Currency', 80, 2)
        
        """    
            STEP 03 : Drag "Cost of Goods" to Vertical Axis.    
        """
        vis_obj.drag_field_from_data_tree_to_query_pane("Cost of Goods", 1, 'Cost of Goods,Local Currency')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='legend-labels!s1!']", 'Cost of Goods', 80, 2)
        
        if Global_variables.browser_name == 'ie' : 
            canvas_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f")
            coreutillobj.python_left_click(canvas_obj, 'top_left')
            time.sleep(5)
            
        """    
            STEP 04 : Drag "Sale,Year" to Horizontal Axis.    
        """
        vis_obj.drag_field_from_data_tree_to_query_pane("Sale,Year", 1, 'Horizontal Axis')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'Sale Year', 80, 2)
        
        """    
            STEP 05 : Select "Format" > "Report" > "Header & Footer" (dropdown) > "Page Header".    
        """
        ribbonobj.select_ribbon_item('Format','Header_footer', opt='Page Header')
        
        """    
            STEP 06 : Type "Test for Page Header".    
            STEP 07 : Change to Bold, Center, Font color = Blue (RGB = (0,128,192)), Size = 14 > Click "Apply".
        """
        if Global_variables.browser_name=='firefox':
            self.create_header_footer('frame', 'Page Header', 'Test for Page Header', font_size='14', bold=True, center_justify=True, text_color='light_blue1', btn_apply=True)
        else:
            ia_styobj.create_header_footer('frame', 'Page Header', 'Test for Page Header', font_size='14', bold=True, center_justify=True, text_color='light_blue1', btn_apply=True)
        utillobj.synchronize_with_visble_text("#MAINTABLE_1 foreignObject[class='title'] span", 'Test for Page Header', 190, 2)
         
        """    
            STEP 08 : Verify the Header styling has been applied on the canvas.    
        """
        oHead=driver.find_element_by_css_selector("#MAINTABLE_1 foreignObject[class='title'] span").text.strip()
        utillobj.asequal("Test for Page Header",oHead, "step 08a: Verify Header styling has been applied on the canvas")
        
        """    
            STEP 09 : Click "Page Footer" on "Header & Footer" window.  
            STEP 10 : Type "Test for Page Footer".
            STEP 11 : Change to Bold, Font color = Red (RGB = (255, 0, 0)), Size = 14 > Click "Apply".
            STEP 12 : Click "OK".
        """
        if Global_variables.browser_name =='firefox':
            self.create_header_footer('frame', 'Page Footer', 'Test for Page Footer', font_size='14', bold=True, text_color='red', btn_apply=True, btn_ok=True)
        else:
            ia_styobj.create_header_footer('frame', 'Page Footer', 'Test for Page Footer', font_size='14', bold=True, text_color='red', btn_apply=True, btn_ok=True)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1 foreignObject:not(.title)", 'Test for Page Footer', 40, 2)
       
        """    
            STEP 13 : Verify the following is displayed.    
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 13.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 13.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 13.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 13.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 13.06: Verify first bar color")
        resultobj.verify_header_footer_text("title", font_color='light_blue', bold=True, msg='Step 13.07: ')
        resultobj.verify_header_footer_text("footnote", font_color='red', bold=True, msg='Step 13.08: ')
        oHead=driver.find_element_by_css_selector("#MAINTABLE_1 foreignObject[class='title'] span").text.strip()
        utillobj.asequal("Test for Page Header",oHead, "Step 13.09: Verify Header styling has been applied on the canvas")
        ofooter=driver.find_element_by_css_selector("#MAINTABLE_wbody1 foreignObject:not(.title)").text.strip()
        utillobj.asequal("Test for Page Footer",ofooter, "Step 13.10: Verify page footer text display on the canvas")
        
        """    
            STEP 14 : Click "Run".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'Sale Year', 180, 2)
        
        """    
            STEP 15 : Verify the following is displayed.    
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 15.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 15.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 15.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 15.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 15.06: Verify first bar color")
        resultobj.verify_header_footer_text("title", font_color='light_blue', bold=True, msg='Step 15.07:')
        resultobj.verify_header_footer_text("footnote", font_color='red', bold=True, msg='Step 15.08:')
        oHead=driver.find_element_by_css_selector("#MAINTABLE_1 foreignObject[class='title'] span").text.strip()
        utillobj.asequal("Test for Page Header",oHead, "Step 15.09: Verify Header styling has been applied on the canvas")
        ofooter=driver.find_element_by_css_selector("#MAINTABLE_wbody1 foreignObject:not(.title)").text.strip()
        utillobj.asequal("Test for Page Footer",ofooter, "Step 15.10: Verify page footer text display on the canvas")
        
        """    
            STEP 16 : Dismiss the "Run" window.    
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """    
            STEP 17 : Click "IA" > "Save" > "C2160093" > "Save".    
        """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
            STEP 18. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        utillobj.infoassist_api_logout()
        
        """    
            STEP 19 : Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160093.fex&tool=idis    
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'Sale Year', 180, 2)
        
        """    
            STEP 20 : Verify the following is displayed.    
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 20.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 20.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 20.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 20.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 20.06: Verify first bar color")
        resultobj.verify_header_footer_text("title", font_color='light_blue', bold=True, msg='Step 20.07:')
        resultobj.verify_header_footer_text("footnote", font_color='red', bold=True, msg='Step 20.08:')
        oHead=driver.find_element_by_css_selector("#MAINTABLE_1 foreignObject[class='title'] span").text.strip()
        utillobj.asequal("Test for Page Header",oHead, "step 20.09: Verify Header styling has been applied on the canvas")
        ofooter=driver.find_element_by_css_selector("#MAINTABLE_wbody1 foreignObject:not(.title)").text.strip()
        utillobj.asequal("Test for Page Footer",ofooter, "step 20.10: Verify page footer text display on the canvas")
        
        """    
            STEP 21 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
    def create_header_footer(self, launch_point, heading_type, input_text,**kwargs): 
    
        if launch_point =='ribbon':
            visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
            visual_ribbonobj.select_ribbon_item('Home', 'header_footer', opt=heading_type)
        else:
            ids={'Report Header':'rptHding','Page Header':'pgHding','Page Footer':'pgFting','Report Footer':'rptFting'}
            btn_css="#" + ids[heading_type] + " img"
            btn_css_obj=self.driver.find_element_by_css_selector(btn_css)
            core_utility.CoreUtillityMethods.left_click(self, btn_css_obj)
            
        utillity.UtillityMethods.synchronize_with_number_of_element(self, '#subheaderDlg #okBtn', 1, 40)
        utillity.UtillityMethods.switch_to_frame(self,frame_css="#Editor")
        time.sleep(5)
        el = self.driver.find_element_by_css_selector('html>body')
        core_utility.CoreUtillityMethods.left_click(self, el)
        time.sleep(1)
        el.send_keys(keys.Keys.CONTROL, 'a')
        time.sleep(1)
        el.send_keys(keys.Keys.DELETE)
        time.sleep(1)
        el = self.driver.find_element_by_css_selector('html>body')
        el.send_keys(input_text)
        time.sleep(3)
        utillity.UtillityMethods.switch_to_default_content(self)

        time.sleep(2)
        self.set_header_footer_style(**kwargs)
        if 'btn_apply' in kwargs:
            self.driver.find_element_by_id("applyBtn").click()
            time.sleep(1)
        if 'btn_ok' in kwargs:
            self.driver.find_element_by_id("okBtn").click()
            time.sleep(1)
        if 'btn_cancle' in kwargs:
            self.driver.find_element_by_id("cancelBtn").click()
            time.sleep(1)
        if 'btn_reset' in kwargs:
            self.driver.find_element_by_id("resetBtn").click()
            time.sleep(1)
           
    def set_header_footer_style(self, **kwargs):
        
        if 'font_size' in kwargs:
            font_size_ele=self.driver.find_element_by_css_selector("#subheaderDlg  div[id*=FontSize] div[id^='BiButton']")
            utillity.UtillityMethods.select_any_combobox_item(self, font_size_ele, kwargs["font_size"])
        if 'bold' in kwargs:
            el = self.driver.find_element_by_css_selector('html>body')
            core_utility.CoreUtillityMethods.left_click(self, el)
            time.sleep(1)
            el.send_keys(keys.Keys.CONTROL, 'a')
            time.sleep(1)
            bold_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Bold img")
            core_utility.CoreUtillityMethods.left_click(self, bold_obj)
            time.sleep(1)
        if 'center_justify' in kwargs:
            el = self.driver.find_element_by_css_selector('html>body')
            core_utility.CoreUtillityMethods.left_click(self, el)
            time.sleep(1)
            el.send_keys(keys.Keys.CONTROL, 'a')
            time.sleep(1)
            center_justify_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Center img")
            core_utility.CoreUtillityMethods.left_click(self, center_justify_obj)
            time.sleep(1)
        if 'text_color' in kwargs:
            text_color_obj=self.driver.find_element_by_css_selector("#subheaderDlg #Color img")
            utillity.UtillityMethods.default_left_click(self, object_locator=text_color_obj, **kwargs)
            color_dialog_popup_css="div[id*='ColorPicker'] div[class*='window-active']"
            ok_btn_css=color_dialog_popup_css+" #BiColorPickerOkBtn"
            utillity.UtillityMethods.synchronize_with_number_of_element(self, ok_btn_css, 1, 25)
            ia_styling.IA_Style.set_color(self,kwargs['text_color'])
        
    
if __name__ == '__main__':
    unittest.main()