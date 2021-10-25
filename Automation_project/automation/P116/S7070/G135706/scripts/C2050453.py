'''
Created on Aug 22, 2016
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050453
TestCase Name = IA:ActiveDash:AHTML:Filter_TextBx:Default Font is too small (118115)
'''
import unittest, time, keyboard
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run

class C2050453_TestClass(BaseTestCase):

    def test_C2050453(self):
        """Test case Variable"""
    
        """
            Step 01a:    Create a Document/Dashboard with Car master file.
            Step 01b:    From home tab change the format to Active Report
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        
        utillobj.infoassist_api_login('document','ibisamp/car','P116/S7070', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 60)
        
        """
            Step 02a    Select Country, Bodytype and Car fields fields.
        """
        metaobj.datatree_field_click("COUNTRY",2,1)
        time.sleep(3)
        metaobj.datatree_field_click("BODYTYPE",2,1)
        time.sleep(3)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(3)
        
        list1 = ['COUNTRY', 'BODYTYPE', 'CAR']
        run_data = []
        col1 = self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x'][class$='003']")
        for r in range(0, len(col1)):
            run_data.append(col1[r].text)
        text = 'Step 02a: Verify column titles on preview'
        utillity.UtillityMethods.asequal(self,list1, run_data, text)
        ribbonobj.repositioning_document_component('2.5', '2.5')
        
        '''
        Step 03a    From insert tab select dropdown, listbox and textbox. Move each box to the right of the report.
        '''
        'DropDown Box'
        ribbonobj.select_ribbon_item("Insert", "drop_down")
        ribbonobj.repositioning_document_component('1.0', '1.0')
        expected_dd_list=['Option 1']
        actual_dd_text = driver.find_element_by_id("Prompt_1").text
        dd_verify=actual_dd_text.strip().split('\n') == expected_dd_list
        utillity.UtillityMethods.asequal(self,True, dd_verify, 'Step 3.a Verifying Drop down added on preview canvas')
        
        'List Box'
        ribbonobj.select_ribbon_item("Insert", "List")
        ribbonobj.repositioning_document_component('2.5', '1.0')
        
        expected_list_text=['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        actual_list_text = driver.find_element_by_id("Prompt_2").text
        list_verify=actual_list_text.strip().split('\n') == expected_list_text
        utillity.UtillityMethods.asequal(self,True, list_verify, 'Step 3.b Verifying List Box added on preview canvas')
        
        'Text Box'
        ribbonobj.select_ribbon_item("Insert", "Text")
        ribbonobj.repositioning_document_component('4.5', '1.0')
        actual_text = driver.find_element_by_css_selector("#Prompt_3").is_displayed()
        utillity.UtillityMethods.asequal(self,True, actual_text, 'Step 3.c Verifying text Box added on preview canvas')     
        
        """
        Step 04a    From dropdown(Combo box) right click and select properties then Active Dashboard Properties opened
        """
        
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        time.sleep(5)
        
        """
        Step 05a    Select Report1 for report, select Bodytype for field and select Equal To for Condition.
        Verify that Include All box is checked and click ok.
        """
        source={'select_field':'BODYTYPE', 'select_condition':'Equal to', 'includeall':True}
        resultobj.customize_active_dashboard_properties(source=source)
        time.sleep(3)
        
        """
        Step 06a    For Text box repeat the above Properties actions (Step5)
        Step 05a    Select Report1 for report, select Bodytype for field and select Equal To for Condition.
        Verify that Include All box is checked and click ok.
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_3', 'Properties')
        time.sleep(5)
        
        source={'select_field':'BODYTYPE', 'select_condition':'Equal to', 'includeall':True}
        resultobj.customize_active_dashboard_properties(source=source)
        time.sleep(3)
        
        """
        Step 07.a    From list box right click and select properties then Active Dashboard Properties opened
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties')
        time.sleep(5)
        
        """
        Step 08.a   Select Report1 for report, select Car for field and select Equal To for condition.
                    Verify that the Include All box is checked and click ok.
        """
        source={'select_field':'CAR', 'select_condition':'Equal to', 'includeall':True}
        resultobj.customize_active_dashboard_properties(source=source)
        
        'DropDown Properties'
        
        expected_dd_list=['[All]']
        actual_dd_text = driver.find_element_by_id("Prompt_1").text
        dd_verify=actual_dd_text.strip().split('\n') == expected_dd_list
        utillity.UtillityMethods.asequal(self,True, dd_verify, 'Step 8.b Verifying Drop down values on preview canvas')
        
        'List Box Properties'
        
        actual_list_text = driver.find_element_by_id("Prompt_2").text
        expected_list_text=['[All]', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        list_verify=actual_list_text.strip().split('\n') == expected_list_text
        utillity.UtillityMethods.asequal(self,True, list_verify, 'Step 8.c Verifying List Box values on preview canvas')
       
        
        'TextBox Properties'
        actual_text = driver.find_element_by_id("Prompt_3").text
        text_verify=bool(actual_text)
        utillity.UtillityMethods.asequal(self,True, text_verify, 'Step 8.d Verifying text Box added is blank on preview canvas')
       
        """
        Step 09.a   Click run and in text box type SEDAN.Hit enter to apply the filter.
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame()
        
        element=self.driver.find_element_by_css_selector('#PROMPT_3_cs input')
        exec("element.clear()")
        exec("element.send_keys('SEDAN')")
        keyboard.send('enter')
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '8of13records,Page1of1', 'Step 09.a: Verify the Run Report Heading')
        column_list=['COUNTRY', 'BODYTYPE', 'CAR']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 09.b: Verify the Run Report column heading')
        utillobj.verify_data_set('ITableData0','I0r','C2050453_Ds_01.xlsx',"Step 09.b: Verify entire Data set in Run Report on Page 1")
        
        'DropDown Properties'
        expected_dd_list=['[All]', 'CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN']
        
        actual_dd_text = driver.find_element_by_id("combobox_dPROMPT_1").text
        dd_verify=actual_dd_text.strip().split('\n') == expected_dd_list
        utillity.UtillityMethods.asequal(self,True, dd_verify, 'Step 9.c Verifying Drop down values on Run Report')
        
        'List Box Properties'
        
        expected_list_text=['[All]', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        actual_list_text = driver.find_element_by_id("list_dPROMPT_2").text
        list_verify=actual_list_text.strip().split('\n') == expected_list_text
        utillity.UtillityMethods.asequal(self,True, list_verify, 'Step 9.d Verifying List Box values on Run Report')
        
        'TextBox Properties'
        actual_dd_text = driver.find_element_by_css_selector("#textinputPROMPT_3 input").get_attribute('value')
        utillity.UtillityMethods.asequal(self,actual_dd_text, 'SEDAN', 'Step 9.e Verifying text Box added is blank Run Report')
        
        #Expect to see that the font size in the Text Box is the same as the values in the List Box
        listbox_font=driver.find_element_by_css_selector("#list_tdPROMPT_2_0>div").value_of_css_property("font-size")
        textbox_font=driver.find_element_by_css_selector("#textinputPROMPT_3 > input[type='text']").value_of_css_property("font-size")
        verify_font =  listbox_font == textbox_font
        utillity.UtillityMethods.asequal(self,True, verify_font, 'Step 9.f Verifying font size in the Text Box is the same as the values in the List Box')
        driver.switch_to_default_content()
       
                
if __name__ == '__main__':
    unittest.main()

