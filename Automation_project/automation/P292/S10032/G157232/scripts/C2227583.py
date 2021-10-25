'''
Created on Dec 6, 2017

@author: Robert
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227583
TestCase Name : Report with Page Break, Line Break, Subtotal, Sub Header and Footer  
'''
import unittest, time,pyautogui
from common.lib import utillity, core_utility
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver import ActionChains

class C2227583_TestClass(BaseTestCase):

    def test_C2227583(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2227583'
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(self.driver)      
          
        '''    Step 1. Launch IA Report mode:    '''
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.chart_long_timesleep)
          
        '''    Step 2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".    '''
        metaobj.datatree_field_click('COUNTRY', 2, 0)
        parent_css="#TableChart_1"
        utillobj.synchronize_with_visble_text(parent_css, 'COUNTRY', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('CAR', 2, 0)
        utillobj.synchronize_with_visble_text(parent_css, 'CAR', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('DEALER_COST', 2, 0)
        utillobj.synchronize_with_visble_text(parent_css, 'DEALER_COST', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('RETAIL_COST', 2, 0)
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COST', metaobj.chart_long_timesleep)
           
        '''    Step 3. Verify the following report is displayed.    '''
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 8, 20)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03.00: Verify the following report is displayed")
#         ia_resultarea_obj.create_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx")
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 03.01: Verify report dataset')
           
        '''    Step 4. Select "COUNTRY" in Query pane.    '''
           
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(4)
           
        '''    Step 5. Select "Page Break" (Break Grouping).    '''
        '''    Step 6. Select "Home" (dropdown) > "PDF".   '''
        vis_ribbon_obj.switch_ia_tab('Field')
        vis_ribbon_obj.select_ribbon_item('Field','page_break_icon')
        time.sleep(4)
        ia_ribbon_obj.select_or_verify_output_type(launch_point='Home',selected_format='HTML',item_select_path='PDF')
   
        '''    Step 7. Verify "Live Preview" updated.    '''
        time.sleep(3)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 14, 4, Test_Case_ID+"_Ds02.xlsx", 'Step 07.00: Verify report dataset after page break')
           
        '''    Step 8. Click "Run".    '''
        '''    Step 9. Verify that 5 pages of PDF report is displayed, Scroll down and verify each page of report    '''
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
          
        '''    Step 10. Dismiss the "Run" output window    '''
        '''    Step 11. Click "IA" > "Save" > Enter Title = "C2227583" > Click "Save".    '''
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(5)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
  
        '''    Step 12. Select "Field - COUNTRY" > De-select "Page Break".    '''
        '''    Step 13. Click "Line Break".    '''
        '''    Step 14. Verify "Live Preview" updated.    '''
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(4)
        vis_ribbon_obj.switch_ia_tab('Field')
        vis_ribbon_obj.select_ribbon_item('Field','page_break_icon')
        time.sleep(5)
        vis_ribbon_obj.select_ribbon_item("Field", "line_break")
          
        linecss="#TableChart_1 div[style*='border-top:1pt']"
        utillobj.synchronize_with_number_of_element(linecss, 5, 15)
        utillobj.verify_object_visible(linecss, True, 'Step 14.00: Verify Live preview with Line break.')
        time.sleep(3)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 14.01: Verify report dataset after line break')
          
        '''    Step 15. Click "Run".    '''
        '''    Step 16. Verify the "Line Break" applied in Run mode.    '''
        '''    Step 17. Dismiss the "Run" output window    '''
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
          
        '''    Step 18. Select "Field - COUNTRY" > De-select "Line Break".    '''
        '''    Step 19. Click "Subtotal" (dropdown) > "Simple".    '''
        '''    Step 20. Verify "Live Preview" updated.    '''
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(5)
        vis_ribbon_obj.switch_ia_tab('Field')
        vis_ribbon_obj.select_ribbon_item("Field", "line_break")
        time.sleep(5) 
        vis_ribbon_obj.select_ribbon_item("Field", "subtotal", opt='Simple')
        time.sleep(5)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 15, 4, Test_Case_ID+"_Ds03.xlsx", 'Step 20.01: Verify report dataset after simple subtotal applied')
          
        '''    Step 21. Click "Run".    '''
        '''    Step 22. Verify the "Subtotal - Simple" applied in Run mode.    '''
        '''    Step 23. Dismiss the "Run" output window    '''
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
          
        '''    Step 24. Select "Field - COUNTRY" > De-select "Subtotal".    '''
        '''    Step 25. Click "Sub Header".    '''
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(8)
        vis_ribbon_obj.switch_ia_tab('Field')
        vis_ribbon_obj.select_ribbon_item("Field", "subtotal_icon")
        time.sleep(4)
          
        '''vis_ribbon_obj.select_ribbon_item("Field", "sub_header")'''
          
        '''    Step 26. Enter "This is for Sub Header". Center, Bold,Font color = Blue and Background = Yellow.    '''
        '''    Step 27. Click "Sub Footer" in the popup window.    '''
        '''    Step 28. Enter "This is for Sub Footer". Right justify, Font color = Red and Background = Cyan,Bold.    '''
        '''    Step 29. Click "OK".    ''' 
        ia_stylingobj.create_sub_header_footer('sub_header', 'This is for Sub Header', bold=True, center_justify=True, text_color='blue', background_color='yellow', btn_apply=True)
        time.sleep(4)
        pagefooting=self.driver.find_element_by_css_selector('#pgFting')
        core_utilobj.left_click(pagefooting)
        time.sleep(4)
        browser = utillobj.parseinitfile('browser')
        if browser == 'IE':     
            action=ActionChains(self.driver)
            time.sleep(1)
            action.send_keys('This is for Sub Footer').perform()
            time.sleep(1)
            del action
        else:
            parent_css="#Editor"
            utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
            self.driver.switch_to.frame(self.driver.find_element_by_id("Editor"))
            time.sleep(8)
            el = self.driver.find_element_by_css_selector('html>body').click()
            time.sleep(1)
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('a')
            pyautogui.keyUp('a')
            pyautogui.keyUp('ctrl')
            time.sleep(1)
            pyautogui.press('delete')
            time.sleep(1)
            el = self.driver.find_element_by_css_selector('html>body')
            el.send_keys('This is for Sub Footer') 
            time.sleep(5)
            core_utilobj.switch_to_default_content()
        utillobj.synchronize_with_number_of_element("#subheaderDlg #Bold img", 1, metaobj.home_page_medium_timesleep)
        ia_stylingobj.set_header_footer_style(bold=True, right_justify=True, text_color='red', background_color='cyan')
        time.sleep(3)
        core_utilobj.left_click(self.driver.find_element_by_id("okBtn"))
        time.sleep(5)
         
        '''  Step 30. Verify "Live Preview" updated. '''
        ia_resultarea_obj.verify_report_header_footer_property('TableChart_1', 1,cell_no=1,font_color='blue', bg_color='yellow', text_value='This is for Sub Header', font_name='Arial', msg='Step 30.01: Verify Subheader styling')
        ia_resultarea_obj.verify_report_header_footer_property('TableChart_1', 2, cell_no=2, font_color='red', bg_color='cyan', text_value='This is for Sub Footer', font_name='Arial', msg='Step 30.02: Verify Subfooter styling')
         
        '''    Step 31. Click "Run".    '''
        '''    Step 32. Verify the "Sub Header", "Sub Footer" and Styling applied in Run mode.    '''
        '''    Step 33. Dismiss the "Run" output window    '''
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
       
        '''    Step 34. Click field "COUNTRY" on Preview > Select "Page-Break", "Line-Break" and "Subtotal" in the Field Tab ribbon    '''
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(5)
        vis_ribbon_obj.switch_ia_tab('Field')
        time.sleep(5)
        vis_ribbon_obj.select_ribbon_item('Field','page_break_icon')
        time.sleep(3)
        vis_ribbon_obj.select_ribbon_item("Field", "line_break")
        time.sleep(3)
        vis_ribbon_obj.select_ribbon_item("Field", "subtotal_icon")
        time.sleep(5)
        
        '''    Step 35. Click "IA" > Save    '''
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        '''    Step 36. Logout:    '''
        '''    Step 37. Reopen saved FEX:    '''
        '''    Step 38. Click field "COUNTRY" on Preview > Verify options in the Field Tab ribbon    '''
        ''''    Step 39. Logout:    '''
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.chart_long_timesleep)
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(4)
        vis_ribbon_obj.switch_ia_tab('Field')
        time.sleep(5)
        pagebrk_chkd= "div[id='FieldPageBreak'][class*=button-checked]"
        linebrk_chkd=" div[id='FieldLineBreak'][class*=button-checked]"
        subtotal_chkd="div[id='FieldRecompute'][class*=button-checked]"
        utillobj.verify_object_visible(pagebrk_chkd, True,msg='Step 38.00: Verify the options(pagebreak) are checked in Field tab')
        utillobj.verify_object_visible(linebrk_chkd, True,msg='Step 38.01: Verify the options(linebreak) are checked in Field tab')
        utillobj.verify_object_visible(subtotal_chkd, True,msg='Step 38.02: Verify the options(subtotal) are checked in Field tab')
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()