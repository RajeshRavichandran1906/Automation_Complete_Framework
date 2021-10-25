'''
Created on December 18, 2017

@author: PM14587
Testcase Name : Verify SET Command for Decimal Notation
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2313004
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_ribbon,ia_run
from common.lib import utillity

class C2313004_TestClass(BaseTestCase):

    def test_C2313004(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2313004'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon= ia_ribbon.IA_Ribbon(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        
        """
            Step 01 : Launch Report Mode: http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('Report','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
         
        """
            Step 02 : Add fields 'Product,Category' and 'Product,Subcategory'
        """
        metaobj.datatree_field_click('Product,Category',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='Product,Category')
        
        metaobj.datatree_field_click('Product,Subcategory',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='Product,Subcategory')
        
        """
            Step 03 :Add field 'Cost of Goods'
        """
        metaobj.datatree_field_click('Cost of Goods',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='Cost of Goods')
        time.sleep(2)
        
        
        """
            Step 04 : Verify Preview
        """
        iaresult.verify_row_total_report_titles_on_preview(3,6,'TableChart_1',['ProductCategory', 'ProductSubcategory', 'Cost of Goods'],'Step 04.1 : Verify Preview')
        preview_data=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[8]
        utillobj.asequal('$2,052,711.00',preview_data.text.strip(),'Step 04.2 : Verify Live Preview data')
        
        """
            Step 05 : Click on the 'Procedure Settings' button in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
         
        """
            Step 06 : Verify default settings
            Step 06.1 : Verify default Unchecked values 
        """
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 06.1 : Verify '+row+' is not selected as default')
         
        """
             Step 06.2 : Verify default checked values
        """
        checked_row=['HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 06.2 : Verify '+row+' is selected as default')
         
        """
            Step 06.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 06.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
         
        """
            Step 06.4 : Verify "Missing Value" default value
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 06.4 : Verify Missing Value default value')
         
        """
            Step 06.5 : Verify Decimal Notation ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 06.5 : Verify Decimal Notation ON is not selected',1)
        iaribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 06.5 : Verify Decimal Notation OFF is selected',2)
             
        """
            Step 06.6 : Verify HTML Encode ON and OFF status 
        """
        for row in ['HTML Encode', 'Empty Report'] :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 06.6 : Verify '+row+' ON is selected',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 06.6 : Verify '+row+' OFF is not selected',2)
        
        """
            Step 07 : Check off 'Decimal Notation' > Select 'On' radio button
        """
        iaribbon.procedure_setting_dialog_input('Decimal Notation','checkbox','unchecked')
        iaribbon.procedure_setting_dialog_input('Decimal Notation','radiobutton','unchecked')

        """
            Step 08 : Click OK
        """
        iaribbon.procedure_setting_dialog_dismiss('OK') 
        time.sleep(6)
        
        """
            Step 09 : Verify placement of the period and comma for the 'Cost of Goods' column in Preview
        """
        iaresult.verify_row_total_report_titles_on_preview(3,6,'TableChart_1',['ProductCategory', 'ProductSubcategory', 'Cost of Goods'],'Step 09.1 : Verify Preview')
        preview_data=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[8]
        utillobj.asequal('$2.052.711,00',preview_data.text.strip(),"Step 09.2 : Verify placement of the period and comma for the 'Cost of Goods' column in Preview")
        
        """
            Step 10 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("table[summary] tr:nth-child(1)>td:nth-child(3)", 1,20,string_value='Cost of Goods')
         
        """
            Step 10.1 :  Verify output
        """
        #iarun.create_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx')
        iarun.verify_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx',"Step 10.1 :  Verify output")
        utillobj.switch_to_default_content(3)
        
        """
            Step 11 : Click 'Save' in the toolbar > Save as > C2313004 > Click 'Save'
        """
        utillobj.switch_to_default_content(3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 12 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 13 : Restore saved Fex : http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Public/C2313004.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 1,30,string_value='Product')
        time.sleep(2)
        
        """
            Step 14 : Verify Live Preview
        """
        iaresult.verify_row_total_report_titles_on_preview(3,6,'TableChart_1',['ProductCategory', 'ProductSubcategory', 'Cost of Goods'],'Step 14.1 : Verify Preview')
        preview_data=self.driver.find_elements_by_css_selector("#TableChart_1 div[class^='x']")[8]
        utillobj.asequal('$2.052.711,00',preview_data.text.strip(),"Step 14.2 : Verify placement of the period and comma for the 'Cost of Goods' column in Preview")
        
        """
            Step 15 : Click "Chart" in the Home Tab ribbon
        """
        ribbonobj.select_ribbon_item('Home','chart')
        resultobj.wait_for_property("#TableChart_1 text[class='yaxis-title']", 1,20,string_value='Cost of Goods')
        
        """
            Step 16 : Click on the 'Procedure Settings' button in the toolbar > Verify 'Decimal Notation' setting is NOT carried over.
            Step 16.1 : Verify default Unchecked values for chart
        """
        ribbonobj.select_top_toolbar_item('toolbar_showfex_setting')
        time.sleep(3)
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 16.1 : Verify '+row+' is not selected as default')
         
        """
             Step 16.2 : Verify default checked values
        """
        checked_row=['HTML Encode','Empty Report']
        for row in checked_row :
            iaribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 16.2 : Verify '+row+' is selected as default')
         
        """
            Step 16.3 : Verify default combobox values
        """
        combobox_row=['Collation Sequence','Summary Lines']
        expected_chombobox_values=['Code Page','New']
        for i in range(len(combobox_row)) :
            iaribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 16.3 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
         
        """
            Step 16.4 : Verify "Missing Value" default value for chart
        """
        iaribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 16.4 : Verify Missing Value default value for chart')
             
        """
            Step 16.5 : Verify 'Decimal Notation','HTML Encode' ON and OFF status 
        """
        for row in ['Decimal Notation','HTML Encode'] :
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 06.6 : Verify '+row+' ON is not selected',1)
            iaribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 06.6 : Verify '+row+' OFF is selected',2)
        
        """
            Step 16.6 : Verify Empty Report ON and OFF status 
        """
        iaribbon.procedure_setting_dialogverify('Empty Report','radiobutton','checked','Step 16.5 : Verify Empty Report ON is selected',1)
        iaribbon.procedure_setting_dialogverify('Empty Report','radiobutton','unchecked','Step 16.5 : Verify Empty Report OFF is not selected',2)
        
        """
            Step 17 : Click Cancel
        """
        iaribbon.procedure_setting_dialog_dismiss('Cancel') 
        
        """
            Step 17.1 : Verify chart output
        """
        resultobj.verify_xaxis_title('TableChart_1','Product Category : Product Subcategory', 'Step 17.1 : Verify X-Axis title')
        resultobj.verify_yaxis_title('TableChart_1','Cost of Goods', 'Step 17.2 : Verify Y-Axis title')
        expected_xaix_labels=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xaix_labels, expected_yaxis_labels, 'Step 17.3 :', 15)
        resultobj.verify_number_of_riser('TableChart_1',1, 21, 'Step 17.4 : Verify number of chart risers')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g8!mbar!', 'bar_blue', 'Step 17.5 : Verify chart color')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_17', 'actual')
        
        """
            Step 18 : Click 'Save' in the toolbar > Save as > C2313004_1 > Click 'Save'
        """
        utillobj.switch_to_default_content(3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+'_1')
        
        """
            Step 18 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 20 : Restore saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Public/C2313004_1.fex&tool=Chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID+'_1', 'Chart', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1 text[class='yaxis-title']", 1,20,string_value='Cost of Goods')
        time.sleep(2)
        
        """
            Step 21 : Verify Chart in Live Preview
        """
        resultobj.verify_xaxis_title('TableChart_1','Product Category : Product Subcategory', 'Step 21.1 : Verify X-Axis title')
        resultobj.verify_yaxis_title('TableChart_1','Cost of Goods', 'Step 21.2 : Verify Y-Axis title')
        expected_xaix_labels=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xaix_labels, expected_yaxis_labels, 'Step 21.3 :', 15)
        resultobj.verify_number_of_riser('TableChart_1',1, 21, 'Step 21.4 : Verify number of chart risers')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g8!mbar!', 'bar_blue', 'Step 21.5 : Verify chart color')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_21', 'actual')
        
        """
            Step 22 : Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
     
if __name__=='__main__' :
    unittest.main()