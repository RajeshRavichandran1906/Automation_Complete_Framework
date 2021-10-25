'''
Created on Jan 18, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251701
Test_Case Name : AHTML/AFLEX Add ShowTitle option for filter controls(ACT-368).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_run, active_miscelaneous
from common.lib import utillity

class C2251701_TestClass(BaseTestCase):

    def test_C2251701(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251701'
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01 : Execute the attached repro act-368.fex Expand the window to maximum .
        """
        utillobj.active_run_fex_api_login('act-368.fex', 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'COUNTRY', 30)
        
        """
            Step 01.1 : Expect to see the following Document with Active Report and the following Dashboard filtering controls List Box(heading ListBox), Check Box(heading Checkbox), Radio Button(heading Radio) & Combo Box(heading Combo).
            Notice that all 4 filter controls have a blue box above, that describes the Filter type. From left to right, they are: ListBox, Checkbox, Radio & Combo.
        """
        #iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_01.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_01.xlsx', 'Step 01.1 : Verify Activr Report displays')
        active.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.2 : Verify report page summary')
        
        """
        Step 01.3 : Verify the following Dashboard filtering controls List Box(heading ListBox), Check Box(heading Checkbox), Radio Button(heading Radio) & Combo Box(heading Combo).
        """
        actual_control_names=[control.text.strip() for control in self.driver.find_elements_by_css_selector("#allLayoutObjects div[id^='LOBJPrompt'] div[class='arFilterButton'] span")]
        utillobj.asequal(['ListBox', 'CheckBox', 'Radio', 'Combo'], actual_control_names, 'Step 01.3 : Verify the following Dashboard filtering controls List Box(heading ListBox), Check Box(heading Checkbox), Radio Button(heading Radio) & Combo Box(heading Combo).')
        
        """
           Step 01.4 Notice that all 4 filter controls have a blue box abov
        """
        control_elements=self.driver.find_elements_by_css_selector("#allLayoutObjects div[id^='LOBJPrompt'] div[class='arFilterButton']")
        for count, control in enumerate(control_elements) :
            actual_color_style=control.value_of_css_property('background-image')
            utillobj.asin('rgb(45, 102, 182) 45%', actual_color_style, 'Step 01.4 : Verify Control ' + str(count) + ' color')
             
        """
            Step 01.5 : Verify listbox, checkbox and radio control values 
        """
        actual_listbox_values=[listbox.text.strip() for listbox in self.driver.find_elements_by_css_selector("#allLayoutObjects #PROMPT_1_cs #list_dPROMPT_1>table>tbody>tr>td>div")]
        actual_checkbox_values=[checkbox.text.strip() for checkbox in self.driver.find_elements_by_css_selector("#allLayoutObjects #PROMPT_2_cs #checkbox_dPROMPT_2>table>tbody>tr>td>label")]
        actual_radiobox_values=[radiobox.text.strip() for radiobox in self.driver.find_elements_by_css_selector("#allLayoutObjects #PROMPT_3_cs #radiobutton_dPROMPT_3>table>tbody>tr>td label")]
        expected_list_values=['[All]', '2,626', '2,886', '4,292', '4,631', '4,915', '5,063', '5,660', '5,800', '6,000', '7,427', '8,300', '8,400', '10,000', '11,000', '11,194', '14,940', '25,000'] 
        status=True if actual_listbox_values==actual_checkbox_values==actual_radiobox_values==expected_list_values else False
        utillobj.asequal(status, True, 'Step 01.5 : Verify All control values')
        
        """
            Step 01.6 : Verify combo control selected value 
        """
        utillobj.verify_dropdown_value('#combobox_dsPROMPT_4 ',expected_default_selected_value="[All]", default_selection_msg='Step 01.6 : Verify combo control selected value')
        
if __name__ == '__main__':
    unittest.main()