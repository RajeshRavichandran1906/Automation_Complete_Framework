'''
Created on Nov 28, 2017

@author: PM14587
Testcase Name : Verify InfoMini request with Chart mode 
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2230759
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run,ia_resultarea,active_miscelaneous
from common.lib import utillity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class C2230759_TestClass(BaseTestCase):

    def test_C2230759(self):
        
        """   
            TESTCASE VARIABLES 
        """
        
        Test_Case_ID = 'C2230759'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active_mis=active_miscelaneous.Active_Miscelaneous(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        
        """
            Step 01 : Reopen FEX created in precondition test case (C2231637): http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231637a.fex&tool=report
        """
        utillobj.infoassist_api_edit('C2231637', 'report', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
        
        """
            Step 02 : Click "Document" in the Home Tab Ribbon
        """
        ribbonobj.select_ribbon_item('Home','Document')
        resultobj.wait_for_property("#canvasFrame #TableChart_1", 1,60)
        
        """
            Step 03 : Verify Document Canvas
        """
        iaresult.verify_across_report_data_set('canvasFrame #TableChart_1',3,5,7,5,Test_Case_ID+'_DataSet_01.xlsx','Step 3.1 : Verify Document Canvas')
        
        """
            Step 04 : Click on the component on Canvas
        """
        canvas_table=self.driver.find_element_by_css_selector("#canvasContainer #TableChart_1")
        utillobj.click_on_screen(canvas_table, coordinate_type='middle', click_type=0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        
        """
            Step 05 : Verify Query pane and Canvas
        """
        expected_fields=['Sum','Parameter1', 'Revenue', 'Cost of Goods', 'Gross Profit', 'By', 'Parameter2', 'Product,Category', 'Product,Subcategory', 'Across', 'Store,Business,Region','Coordinated']
        position=1
        for field in expected_fields :
            metaobj.verify_query_pane_field('Report1 (wf_retail_lite)',field,position,'Step 5.'+str(position))
            position+=1
        iaresult.verify_across_report_data_set('canvasFrame #TableChart_1',3,5,7,5,Test_Case_ID+'_DataSet_01.xlsx','Step 5.13 : Verify Canvas report')
        
        """
            Step 06 : Click "IA" > Save As > "C2230759" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 07 : Logout:
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
            Step 08 : Reopen FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2230759.fex&tool=document
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#canvasFrame #TableChart_1", 1,60)
        time.sleep(3)
        
        """
            Step 09 : Click on the component on Canvas
        """
        canvas_table=self.driver.find_element_by_css_selector("#canvasContainer #TableChart_1")
        utillobj.click_on_screen(canvas_table, coordinate_type='middle', click_type=0)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        
        """
            Step 10 : Verify Query pane and Canvas
        """
        expected_fields=['Sum','Parameter1', 'Revenue', 'Cost of Goods', 'Gross Profit', 'By', 'Parameter2', 'Product,Category', 'Product,Subcategory', 'Across', 'Store,Business,Region','Coordinated']
        position=1
        for field in expected_fields :
            metaobj.verify_query_pane_field('Report1 (wf_retail_lite)',field,position,'Step 10.'+str(position))
            position+=1
        iaresult.verify_across_report_data_set('canvasFrame #TableChart_1',3,5,7,5,Test_Case_ID+'_DataSet_01.xlsx','Step 10.13 : Verify Canvas report')
        
        """
            Step 11 : Click Run > Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#promptPanel label[class='autop-title']",1,20,string_value='Filter Values')
        
        actual_field1=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter1']").text.strip().replace('\n',' ')
        actual_field2=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter2']").text.strip().replace('\n',' ')
        
        expected_paramter1="Parameter1 Revenue Revenue Cost of Goods Gross Profit" if browser=='Firefox' else "Parameter1 Revenue"
        expected_paramter2="Parameter2 Product Category Product Category Product Subcategory" if browser=='Firefox' else "Parameter2 Product Category"
        
        utillobj.asequal(actual_field1,expected_paramter1,'Step 11.1 : Verify default amper value for Paramater1')
        utillobj.asequal(actual_field2,expected_paramter2,'Step 11.2 : Verify default amper value for Paramater2')
        
        """
            Step 12 : Click Submit button > Verify output
        """
        iarun.select_amper_menu('Run')
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        resultobj.wait_for_property("#ITableData0>tbody>tr:nth-child(1)>td:nth-child(2) span",1,20,string_value='EMEA')
        iarun.verify_table_data_set("#ITableData0",Test_Case_ID+'_DataSet_02.xlsx','Step 12.1 : Verify output report')
        active_mis.verify_page_summary(0,'7of7records,Page1of1','Step 12.2 : Verify report page summary')
        
        """
            Step 013 : Logout:
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()