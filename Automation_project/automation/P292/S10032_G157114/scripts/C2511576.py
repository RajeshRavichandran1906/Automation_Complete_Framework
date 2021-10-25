'''
Created on December 18, 2017

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227787
TestCase Name = Report-Filter: Verify user can use Filter menu options under each column (Between, Not Between, Contains - 2, Omits - 2).)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2511576_TestClass(BaseTestCase):

    def test_C2511576(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        Test_Case_ID = "C2511576"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
           
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")      
          
        """
             Step 03 : Verify the report is generated.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
          
        """
            Step 04 : Select State > Filter > Between
            Select GA from the first value box and MA from the second value box. Click Filte
            Click the Filter button.
            Verify Filter selection pop up is opened.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Filter', option, 'Step 04.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 3, "Filter", "Between")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 04.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Between',value1='GA',value2='MA')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
          
        """
             Verify that report returns 29 of 107 records and that all are between the State values of "GA" and "MA".
        """
          
        miscelanousobj.verify_page_summary('0','29of107records,Page1of1', 'Step 04.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227787_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx", 'Step 04.4: Verify that report returns 29 of 107 records')
        time.sleep(4)
          
        """
            Step 05: Close Filter selection pop up\Verify report is restored in original format.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 05.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 05.2: verify report data")
         
        """
            Step 06: Select Unit Sales > Filter > Not Between
            Select 12386 from the first value box and 48941 from the second value box. 
            Click the Filter button.
            Verify Filter selection pop up is opened.
            Verify the Unit Sales value Filter selection menu appears.
              
        """
          
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 4, 'Filter', option, 'Step 06.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 4, "Filter", "Not Between")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 06.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Not Between','large',value1='12386',value2='48941')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
          
        """
             Verify that report returns 19 of 107 records all not Between values 12386 and 48941.
        """
          
        miscelanousobj.verify_page_summary('0','19of107records,Page1of1', 'Step 06.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227787_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx', 'Step 06.4: Verify that report returns 55 of 107 records, all Less Than 15905.')
        time.sleep(4)
          
        """
            Step 07: Close Filter selection pop up\Verify report is restored in original format.
        """          
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 07.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 07.2: verify report data")
         
        """
            Step 08: Select Product > Filter > Contains
            Enter the string "is" (lower case) in the text box.
            Click Filter.            
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 2, 'Filter', option, 'Step 08.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 2, "Filter", "Contains")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 08.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Contains','large',value1='is')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)         
         
        """
             Verify that report returns 22 of 107 records.Both Biscotti and Croissant contain the string "is".
        """
        miscelanousobj.verify_page_summary('0','22of107records,Page1of1', 'Step 08.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227787_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx', 'Step 08.4: Verify that report returns 22 of 107 records, Both Biscotti and Croissant contain the string "is"')
        time.sleep(4)
         
        """
            Step 09: Close Filter selection pop up\Verify report is restored in original format.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(3)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 09.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 09:2: verify report data")
        
        """
            Step 10: Select Product > Filter > Contains (match case)
            Enter the string "Is" (mixed case) in the text box.
            Click Filter.           
        """
        
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 2, 'Filter', option, 'Step 10.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 2, "Filter", "Contains (match case)")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 10.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Contains (match case)','large',value1='Is')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """
        Verify report returns 0 records because no Product contains the exact case match string "Is".
        """
        miscelanousobj.verify_page_summary('0','0of107records,Page1of1', 'Step 10.3: Verify the page summary')
        time.sleep(4)
        
        """
            Step 11: Change the value in the Text Box to "is" (lower case)
            Verify that report returns 22 of 107 records.
                Both Biscotti and Croissant contain the string "is".         
        """        
        filterselectionobj.create_filter(1,'Contains (match case)','large',value1='is')
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','22of107records,Page1of1', 'Step 11.1: Verify the page summary')
        time.sleep(4)
        
        """
            Step 12: Close Filter selection pop up.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        
        """
            Step 13:Select Product ID > Filter > Omits 
            Enter the string "C" (upper case) in the text box.
            Click Filter.
            Verify that report returns 77 of 107 records.
            Only Product IDs not starting with "C" appear, showing "F" and "G" starting values.      
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Filter', option, 'Step 13.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 1, "Filter", "Omits")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 13.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Omits','large',value1='C')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """
        Verify that report returns 77 of 107 records.
            Only Product IDs not starting with "C" appear, showing "F" and "G" starting values. 
        """
        
        miscelanousobj.verify_page_summary('0','77of107records,Page1of2', 'Step 13.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227787_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx', 'Step 13.4: Verify that report returns 22 of 107 records, Both Biscotti and Croissant contain the string "is"')
        time.sleep(4)
        
        """
            Step 14: Close Filter selection pop up.Verify report is restored in original format.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 14.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 14.2: verify report data")
        
        """
            Step 15:Select Product ID > Filter > Omits (match case)
            Enter the string "c141" (mixed case) in the text box.Click Filter.     
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Filter', option, 'Step 15.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 1, "Filter", "Omits (match case)")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 15.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Omits (match case)','large',value1='c141')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """
        Verify that report returns 107 of 107 records.
        There are no records to Omit that have exact value "c141".The original report appears.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 15.3: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "'Step 15.4: Verify that report returns 107 of 107 records.")
        
        """
            Step 16:Change the value in the Text Box to "C141" (upper case "C").Click Filter.
               
        """
        filterselectionobj.create_filter(1,'Omits (match case)','large',value1='C141')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """
        Verify that report returns 96 of 107 records. Only records that have exact value "C141" are Omitted.
        """
        miscelanousobj.verify_page_summary('0','96of107records,Page1of2', 'Step 16.1: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227787_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds06.xlsx', 'Step 16.2: Verify that report returns 96 of 107 records. Only records that have exact value "C141" are Omitted.')
        time.sleep(4)
        
        """
            Step 17:Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp            
        """
        
if __name__=='__main__' :
    unittest.main()