'''
Created on Aug 03, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2157176
TestCase Name = AHTML: Add support for report margins via the Layout/Margin control of InfoAssist. 
'''
import unittest, time 
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity,core_utility
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.wftools.chart import Chart

class C2157176_TestClass(BaseTestCase):

    def test_C2157176(self):
        
        """ Class object """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        chart_obj = Chart(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        
        """
            Step 01a:    Start an InfoAssist session, create a new report and select the ggsales file.
            Step 01b:    Change the output Format to AHTML.
            Step 01c:    Select Category & Product for the Dimensions and Unit Sales & Dollar Sales as the Measures
            Step 01d:    Select Run button
        """
        utillobj.infoassist_api_login('report','ibisamp/ggsales','P116/S7072', 'mrid', 'mrpass')
        
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 60)
        
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        

        metaobj.datatree_field_click("Category",2,1)
        time.sleep(5)
        metaobj.datatree_field_click("Product",2,1)
        time.sleep(5)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Dollar Sales",2,1)
        time.sleep(5)
        
        list1 = ['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", list1, "Step 01.01: Verify column titles on preview")
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.02: Verify the Run Report Heading')
        column_list=['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.03: Verify the Run Report column heading')
        time.sleep(5)
        
        """
            Step 2.a Click the Layout tab at the top, then select Margins. Click the first option - Normal (1.0 inch all around).
            Step 2.b Click the Run button.
        """
        utillobj.switch_to_default_content(pause=2)
        time.sleep(1)
        ribbonobj.select_ribbon_item('Layout', 'Margins', opt='Normal (1.0 inch all round)')
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 02.01: Verify the Run Report Heading')
        column_list=['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02.02: Verify the Run Report column heading')
        expected_style = '72px;'
        divid = driver.find_element_by_id('MAINTABLE_all0')
        actual_style = divid.get_attribute("style")
        text = 'Step 02.03: Verify report has Normal (1.0 inch all around)'
        utillity.UtillityMethods.asin(self,expected_style, actual_style, text)
        chart_obj.switch_to_default_content()
        
        """
            Step 3. Check the code for the first option by clicking the View Code button at the top
        """
        chart_obj.select_item_in_top_toolbar('showfex')
        time.sleep(8)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        fex_code = driver.find_element_by_css_selector("body>div").text
        expected_code = 'LEFTMARGIN=1, TOPMARGIN=1, RIGHTMARGIN=1, BOTTOMMARGIN=1'
        vp_text = 'RIGHTMARGIN=1,BOTTOMMARGIN=1..in the fexex code'
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
                
        """
            Step 4.a Click the OK button on the Current Focexec Content screen.
            Step 4.b Click the Layout tab at the top, then select Margins.
            Step 4.c Click the second option - Narrow (.50 inch around).
            Step 4.d Click the Run button.
        """
        close_fexcode_btn = driver.find_element_by_css_selector("#showFexOKBtn")
        core_utils.left_click(close_fexcode_btn)       
        time.sleep(4)
        
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Narrow (.50 inch round)")
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 04.01: Verify the Run Report Heading')
        column_list=['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04.02: Verify the Run Report column heading')
        expected_style = '36px;'
        divid = driver.find_element_by_id('MAINTABLE_all0')
        actual_style = divid.get_attribute("style")
        text = 'Step 04.03: Verify report has Narrow (.50 inch round)'
        utillity.UtillityMethods.asin(self,expected_style, actual_style, text)
        
        """
            Step 5.a Click the Layout tab at the top, then select Margins.
            Step 5.b Click the third option - Moderate (.50 inch left/right).
            Step 5.c Click the Run button.
        """
        utillobj.switch_to_default_content(pause=2)
        
        time.sleep(2)
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Moderate (.50 inch left/right)")
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 05.01: Verify the Run Report Heading')
        column_list=['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05.02: Verify the Run Report column heading')
        expected_style = '36px;'
        top="margin-top"
        divid = driver.find_element_by_id('MAINTABLE_all0')
        actual_style = divid.get_attribute("style")
        text = 'Step 05.04: Verify report has Moderate (.50 inch left/right) and verify the report has no spacing at the top'
        utillity.UtillityMethods.as_notin(self,top, actual_style,"Step 05.03: Verify margin-top not present")
        utillity.UtillityMethods.asin(self,expected_style, actual_style, text)
        
        """
            Step 6.a Click the Layout tab at the top, then select Margins.
            Step 6.b Click the third option - Wide (1.50 inch left/right).
            Step 6.c Click the Run button.
        """
        
        utillobj.switch_to_default_content(pause=2)
        time.sleep(8)
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Wide (1.50 inch left/right)")
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 06.01: Verify the Run Report Heading')
        column_list=['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06.02: Verify the Run Report column heading')
        expected_style = '108px;'
        top="margin-top"
        divid = driver.find_element_by_id('MAINTABLE_all0')
        actual_style = divid.get_attribute("style")
        text = 'Step 06.04: Verify report has Wide (1.50 inch left/right) and verify the report has no spacing at the top'
        utillity.UtillityMethods.as_notin(self,top, actual_style,"Step 06.03: Verify margin-top not present")
        utillity.UtillityMethods.asin(self,expected_style, actual_style, text)
        utillobj.switch_to_default_content(pause=2)
        
        '''
        7.a Click the Layout tab at the top, then select Margins.
        7.b Click the fifth option - Custom
       '''
        ribbonobj.select_ribbon_item("Layout", "Margins", opt="Custom")

        input_top = driver.find_element_by_css_selector("#qbMarginsDlg #topMargin")
        otop = input_top.get_attribute("value")
        input_bottom = driver.find_element_by_css_selector("#qbMarginsDlg #bottomMargin")
        obottom = input_bottom.get_attribute("value")
        input_left = driver.find_element_by_css_selector("#qbMarginsDlg #leftMargin")
        oleft = input_left.get_attribute("value")
        input_right = driver.find_element_by_css_selector("#qbMarginsDlg #rightMargin")
        oright = input_right.get_attribute("value")
        vp_text1 = 'Step 07.01: Notice that the last set of values selected, still appear, 1.50 inch for the Left and Right positions'
        vp_text2 = 'Step 07.02: Notice that the last set of values selected, still appear, 0 inch for the top and bottom positions'
        vp1=oleft == oright == '1.5'
        utillity.UtillityMethods.asequal(self,True, vp1, vp_text1)
        vp2=otop == obottom == '0.0'
        utillity.UtillityMethods.asequal(self,True, vp2, vp_text2)
        
        '''
        8.a Enter 2.5 for all Margin settings.
        8.b Click the OK button
        8.c Click the Run button
       '''
        input_top.clear()
        input_top.send_keys('2.5')
        time.sleep(1)
        
        input_bottom.clear()
        input_bottom.send_keys('2.5')
        time.sleep(1)
        
        input_left.clear()
        input_left.send_keys('2.5')
        time.sleep(1)
    
        input_right.clear()
        input_right.send_keys('2.5')
        time.sleep(1)

        driver.find_element_by_css_selector("#qbMarginsDlg #marginApplyBtn").click()
        time.sleep(2)
        
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(8)
       
        utillobj.switch_to_frame(pause=2)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 08.01: Verify the Run Report Heading')
        column_list=['Category', 'Product', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 08.02: Verify the Run Report column heading')
        expected_style = '180px;'
        divid = driver.find_element_by_id('MAINTABLE_all0')
        actual_style = divid.get_attribute("style")
        text = 'Step 08.03: Verify report has hows 2.50 inches all around'
        utillity.UtillityMethods.asin(self,expected_style, actual_style, text)
        
        utillobj.switch_to_default_content(pause=2)
        
        time.sleep(2) 
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as("AR_RP_C2157176")
        time.sleep(6) 
        
if __name__ == '__main__':
    unittest.main()