'''
Created on December 18, 2017

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227790
TestCase Name = Report-Filter: Verify user can use Filter menu options under each column (Between, Not Between, Contains - 2, Omits - 2).)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2227790_TestClass(BaseTestCase):

    def test_C2227790(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
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
            Step 04:Select Category > Filter > Equals
            From the dropdown list select "Coffee".
            Click Highlight on the Filter menu.            
        """
          
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 0, 'Filter', option, 'Step 04.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 0, "Filter", "Equals")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 04.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Equals',value1='Coffee')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
          
        """
            Expect to see the same report with all values of Coffee highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 30, 'Step 04: Verify row is highlighted as expected.')
        time.sleep(2)
          
        """
            Step 05:Close the current Filter panel.
            Select Product ID > Filter > Not Equal
            From the dropdown list select "C142".
            Click Highlight on the Filter menu.         
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Filter', option, 'Step 05.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 1, "Filter", "Not equal")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 05.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Not equal',value1='C142')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
          
        """
            Expect to see all rows except those for Product ID C142 highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 46, 'Step 05.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
  
        """
            Step 06:Close the current Filter panel.
            Select Product > Filter > Greater Than
            From the dropdown list select "Espresso".
            Click Highlight on the Filter menu.      
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 2, 'Filter', option, 'Step 06.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 2, "Filter", "Greater than")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 06.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Greater than',value1='Espresso')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
          
        """
            Expect to see rows highlighted where Product is greater than Espresso, i.e. Latte & Scone but NOT Capuccino.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 22, 'Step 06.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
          
        """
            Step 07:Close the current Filter panel.
            Select Product > Filter > Greater Than or Equal to
            From the dropdown list select "Espresso".
            Click Highlight on the Filter menu.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 2, 'Filter', option, 'Step 07.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 2, "Filter", "Greater than or equal to")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 07.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Greater than or equal to',value1='Espresso')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
          
        """
            Expect to see rows highlighted where Product is greater than or Equal to Espresso. This report will now show Products Espresso, Latte and Scone highlighted.
        """
          
        miscelanousobj.verify_highlighted_rows('ITableData0', 33, 'Step 07.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
          
        """
            Step 08:Close the current Filter panel.
            Select State > Filter > Less Than
            From the dropdown list select "FL".
            Click Highlight on the Filter menu.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Filter', option, 'Step 08.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 3, "Filter", "Less than")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 08.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Less than',value1='FL')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
          
        """
            Expect to see rows highlighted where State is less than FL. This will include States CA and CT only.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 12, 'Step 08.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
          
        """
            Step 09:Close the current Filter panel.
            Select State > Filter > Less Than or equal to
            From the dropdown list select "FL".
            Click Highlight on the Filter menu.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Filter', option, 'Step 09.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 3, "Filter", "Less than or equal to")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 09.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Less than or equal to',value1='FL')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
          
        """
            Expect to see rows highlighted where State is less than or equal to FL. This will now show States CA, CT & FL highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 18, 'Step 09.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
         
        """
            Step 10:Close the current Filter panel.
            Select Unit Sales > Filter > Between
            From the first dropdown list select 15905.
            From the second dropdown list select 22482.
            Click Highlight on the Filter menu.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 4, 'Filter', option, 'Step 10.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 4, "Filter", "Between")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 10.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Between','large',value1='15905',value2='22482')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
         
        """
            Expect to see rows highlighted that have Unit Sales values between 15905 and 22482 inclusive highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 7, 'Step 10.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
         
        """
            Step 11:Close the current Filter panel.
            Select Unit Sales > Filter > Not Between
            From the first dropdown list select 12386.
            From the second dropdown list select 27409.
            Click Highlight on the Filter menu.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 4, 'Filter', option, 'Step 11.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 4, "Filter", "Not Between")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 11.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Not Between','large',value1='12386',value2='27409')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
         
        """
            Expect to see rows highlighted that have Unit Sales values that are not between 12386 and 27409 highlighted.
            This will include all rows less than 12386 and greater than 27409.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 36, 'Step 11.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
         
        """
            Step 12:Close the current Filter panel.
            Select Product ID > Filter > Contains
            Enter the value C142 into the text box.
            Click Highlight on the Filter menu.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Filter', option, 'Step 12.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 1, "Filter", "Contains")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 12.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Contains','large',value1='C142')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
         
        """
            Expect to see Product ID rows highlighted that contain the value C142.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 11, 'Step 12.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        
        """
            Step 13:Close the current Filter panel.
            Select Product ID > Filter > Contains (match case)
            Enter the value c141 into the text box. (lower case "c")
            Click Highlight on the Filter menu.
            Now change the "c" to "C". Click Highlight again.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Filter', option, 'Step 13.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 1, "Filter", "Contains (match case)")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 13.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Contains (match case)','large',value1='c141')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        filterselectionobj.create_filter(1,'Contains (match case)','large',value1='C141')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
         
        """
            Expect to see no rows highlighted because case must match exactly.
            Expect to see rows containing C141 because the case now matches.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 11, 'Step 13.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
         
        """
            Step 14:Close the current Filter panel.
            Select State > Filter > Omits
            Enter the value "T" into the text box.
            Click Highlight on the Filter menu.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Filter', option, 'Step 14.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 3, "Filter", "Omits")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 14.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Omits','large',value1='T')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
         
        """
            Expect to see State rows that do not have a "T" highlighted.
            Rows CT, TN & TX are NOT highlighted because they contain the letter "T" in any position.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 42, 'Step 14.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        
        """
            Step 15:Close the current Filter panel.
            Select State > Filter > Omits (match case)
            Enter a lower case "c" into the text box. 
            Click Highlight on the Filter menu.
            Now change the lower case "c" to an upper case "C". 
            Click Highlight again.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Filter', option, 'Step 15.1: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", 3, "Filter", "Omits (match case)")
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 15.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1,'Omits (match case)','large',value1='c')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        filterselectionobj.create_filter(1,'Omits (match case)','large',value1='C')
        time.sleep(4)
        filterselectionobj.filter_button_click('Highlight')
        
        """
            Expect to see all rows highlighted, as no State contains "c".
            Expect to see rows except CA & CT highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 45, 'Step 15.3: Verify row is highlighted as expected.')
        time.sleep(2)
        miscelanousobj.close_popup_dialog('1')
        time.sleep(4)
        
        """
            Step 16:Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main() 
        