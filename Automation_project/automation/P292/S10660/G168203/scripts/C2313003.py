'''
Created on December 20, 2017

@author: PM14587
Testcase Name : Verify SET Command for Missing Value with multiple queries
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2313003
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_ribbon
from common.lib import utillity

class C2313003_TestClass(BaseTestCase):

    def test_C2313003(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2313003'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon= ia_ribbon.IA_Ribbon(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01 : Launch Report Mode, http://machine:port/ibi_apps/ia?tool=Report&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login_with_masterfile_promt('Report','mrid', 'mrpass')
        resultobj.wait_for_property("#dlgIbfsOpenFile7 #IbfsOpenFileDialog7_btnOK", 1,10,string_value='Open')
        
        """
            Step 02 : Select Car master from master file selection window
            Step 03 : Click oprn
        """
        utillobj.ibfs_save_as('car.mas',save_folder='ibisamp')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,30,string_value='Sum')
        time.sleep(3)
         
        """
            Step 04 : Add fields CAR, SALES 
        """
        metaobj.datatree_field_click('CAR',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='CAR')
        
        metaobj.datatree_field_click('SALES',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='SALES')
        
        """
            Step 05 : Drag COUNTRY into the Across bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Across', 0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(7)", 1,20,string_value='COUNTRY')
        time.sleep(3)
         
        """
            Step 06 : Click on the 'Procedure Settings' button in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
        
        """
            Step 07 : Verify default settings
            Step 07.1 : Verify default Unchecked values 
        """
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 07.1 : Verify '+row+' is not selected as default')
        
        """
             Step 07.2 : Verify default checked values
        """
        checked_row=['HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 07.2 : Verify '+row+' is selected as default')
        
        """
            Step 07.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 07.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        """
            Step 07.4 : Verify "Missing Value" default value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 07.4 : Verify Missing Value default value')
        
        """
            Step 07.5 : Verify Decimal Notation ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 07.5 : Verify Decimal Notation ON is not selected',1)
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 07.5 : Verify Decimal Notation OFF is selected',2)
            
        """
            Step 07.6 : Verify HTML Encode ON and OFF status 
        """
        for row in ['HTML Encode', 'Empty Report'] :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 07.6 : Verify '+row+' ON is selected',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 07.6 : Verify '+row+' OFF is not selected',2)
    
        """
            Step 08 : Check off 'Missing Value' > Type N/A > Click OK
        """
        iaribbon.procedure_setting_dialog_input('Missing Value','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Missing Value','textbox','N/A')
        iaribbon.procedure_setting_dialog_dismiss('OK') 
        time.sleep(4)
        
        """
            Step 09 : Verify Preview
        """
        #iaresult.create_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 09.1 : Verify preview')
        
        """
            Step 10 : Click 'New' button in the toolbar > Select 'Build a Chart' > Select carolap > Open
        """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        ribbonobj.select_item_in_splash_options('Build a Chart')
        resultobj.wait_for_property("#dlgIbfsOpenFile7 #IbfsOpenFileDialog7_btnOK", 1,10,string_value='Open')
        utillobj.ibfs_save_as('carolap.mas',save_folder='ibisamp')
        resultobj.wait_for_property(" #TableChart_1 text[class='legend-labels!s0!']", 1,10,string_value='Series 0')
        time.sleep(2)
        
        """
            Step 11 : Click the '2 Reports' shortcut in the Status Bar > Select Report1
        """
        ribbonobj.switch_to_report_panel('Report1')
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 1,15,string_value='COUNTRY')
        time.sleep(2)
        
        """
            Step 12 : Verify Report Live Preview is displayed
        """
        iaresult.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 12.1 : Verify Report Live Preview is displayed')
        
        """
            Step 13 : Save the Report fex: Click 'Save' in the toolbar > Save as > C2313003 > Click 'Save'
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 14 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 15 : Restore saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10660/C2313003.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 1,60,string_value='COUNTRY')
        time.sleep(3)
        
        """
            Step 16 : Verify Live Preview
        """
        iaresult.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+'_DataSet_01.xlsx','Step 12.1 : Verify Report Live Preview')
        
        """
            Step 17 : Click on the 'Procedure Settings' button in the toolbar > Verify selection is displayed after restore.
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
        
        """
            Step 17.1 : Verify default Unchecked values 
        """
        unchecked_row=['Collation Sequence','Summary Lines','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 17.1 : Verify '+row+' is not selected as default')
        
        """
             Step 17.2 : Verify default checked values
        """
        checked_row=['Missing Value','HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 17.2 : Verify '+row+' is selected as default')
        
        """
            Step 17.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 17.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        """
            Step 17.4 : Verify "Missing Value" default value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','N/A','Step 17.4 : Verify Missing Value value')
        
        """
            Step 17.5 : Verify Decimal Notation ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 17.5 : Verify Decimal Notation ON is not selected',1)
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 15.5 : Verify Decimal Notation OFF is selected',2)
            
        """
            Step 17.6 : Verify HTML Encode ON and OFF status 
        """
        for row in ['HTML Encode', 'Empty Report'] :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 17.6 : Verify '+row+' ON is selected',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 17.6 : Verify '+row+' OFF is not selected',2)
    
        """
            Step 18 : Click Cancel
        """
        iaribbon.procedure_setting_dialog_dismiss('Cancel')
         
        """
            Step 19 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()