'''
Created on Nov 28, 2017

@author: PM14587
Testcase Name : Verify InfoMini request with Chart mode 
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2231281
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run
from common.lib import utillity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class C2231281_TestClass(BaseTestCase):

    def test_C2231281(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2231281'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """
            Step 01 : Launch IA Report mode with wf_retail_lite: http://machine:port/ibi_apps/ia?tool=report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Matrix')
        time.sleep(3)
#         
        """
            Step 02 : Right-click Vertical Axis > New Parameter
        """
        metaobj.querytree_field_click('Vertical Axis',1,1,'New Parameter')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(7)", 1,40,string_value='Parameter1')
          
        """
            Step 03 : Drag and drop "Revenue", "Cost of Goods", and "Gross Profit" under Parameter1 in Vertical Axis
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit',1,'Parameter1',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,40,string_value='Gross Profit')
        metaobj.drag_drop_data_tree_items_to_query_tree('Cost of Goods',1,'Parameter1',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,40,string_value='Cost of Goods')
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue',1,'Parameter1',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,40,string_value='Revenue')
        time.sleep(2)
          
        """
            Step 04 : Right-click Horizontal Axis > New Parameter
        """
        metaobj.querytree_field_click('Horizontal Axis',1,1,'New Parameter')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(12)", 1,40,string_value='Parameter2')
          
        """
            Step 05 : Drag and drop "Product,Category" and "Product,Subcategory" under Parameter1 in Horizontal Axis
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Subcategory',1,'Parameter2',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(13)", 1,40,string_value='Product,Subcategory')
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category',1,'Parameter2',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(13)", 1,40,string_value='Product,Category')
        time.sleep(2)
         
        """
            Step 06 : Drag and drop "Store,Business,Region" to Matrix > Columns
        """
        metaobj.datatree_field_click('Store,Business,Region', 1, 0, 'Add To Query', 'Columns')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,40,string_value='Store,Business,Region')
        time.sleep(2)
          
        """
            Step 07 : Drag and drop "Customer,Business,Region" to the Color bucket
        """
        metaobj.datatree_field_click('Customer,Business,Region', 1, 0, 'Add To Query', 'Color')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(18)", 1,40,string_value='Customer,Business,Region')
        time.sleep(2)
         
        """
            Step 08 : Verify Query pane and Preview
        """
        utillobj.verify_element_text("#pfjTableChart_1 text[class='colHeader-label!']",'Store Business Region','Step 08.1 : Verify vertical title')
        expected_xaxis_label=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yaxis_label=['0','30M','60M','90M','120M','150M']
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xaxis_label, expected_yaxis_label,'Step 08.2 :')
        resultobj.verify_yaxis_title('pfjTableChart_1','Revenue','Step 08.3 : Verit Y-Axis title')
        resultobj.verify_data_labels('pfjTableChart_1',['Product Category','Product Category','Product Category','Product Category'],'Step 08.4 : Verify X-Axis titles',custom_css="svg > g text[class='xaxisOrdinal-title']")
        resultobj.verify_data_labels('pfjTableChart_1',['EMEA','North America','Oceania','South America'],'Step 08.5 : Verify chart column labels',custom_css="svg > g text[class^='colLabel!']")
        resultobj.verify_number_of_riser('pfjTableChart_1',1,49,'Step 08.6 : Verify number of risers')
        resultobj.verify_riser_legends('pfjTableChart_1',['Customer Business Region','EMEA','North America','Oceania','South America'],'Step 08.7 : Verify legend text')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s0!g3!mbar!r0!c1!','bar_blue1','Step 08.8 : Verify riser color')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s1!g3!mbar!r0!c1!','bar_green','Step 08.9 : Verify riser color')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_08','actual')
        
        """
            Step 09 : Drag and drop "Customer,Country" to Matrix > Rows
        """
        metaobj.datatree_field_click('Customer,Country', 1, 0, 'Add To Query', 'Rows')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,40,string_value='Customer,Country')
        time.sleep(2)
        
        """
            Step 10 : Right-click "Customer,Country" in Matrix Rows > Select "Create Group..."
        """
        metaobj.querytree_field_click('Customer,Country',1,1,'Create Group...')
         
        """
            Step 11 : Multi-select values "Canada" and "United States" > Click "Group"
            Step 12 : Click OK
        """
        metaobj.create_large_ia_group('Group', ['Canada','United States'],42,close_button='ok')
        resultobj.wait_for_property("#pfjTableChart_1 text[class='rowHeader-label!']",1,30,string_value='COUNTRY_NAME_1')
        time.sleep(2)

        """
            Step 13 : Verify Query pane and Preview
        """
        expected_fields=['Matrix', 'Rows', 'COUNTRY_NAME_1', 'Columns', 'Store,Business,Region', 'Axis', 'Vertical Axis', 'Parameter1', 'Revenue', 'Cost of Goods', 'Gross Profit', 'Horizontal Axis', 'Parameter2', 'Product,Category', 'Product,Subcategory', 'Marker', 'Color BY', 'Customer,Business,Region', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        position=1
        for field in expected_fields :
            metaobj.verify_query_pane_field('Chart (wf_retail_lite)',field,position,'Step 13.'+str(position))
            position+=1
        utillobj.verify_element_text("#pfjTableChart_1 text[class='colHeader-label!']",'Store Business Region','Step 13.23 : Verify vertical title')
        utillobj.verify_element_text("#pfjTableChart_1 text[class='rowHeader-label!']",'COUNTRY_NAME_1','Step 13.24 : Verify Row header label')
        expected_xaxis_label=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yaxis_label=['0','30M','60M','90M','120M','150M']
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xaxis_label, expected_yaxis_label,'Step 13.25 :',y_custom_css="g[class='scrollRowAxis'] g:nth-child(1) text[class^='yaxis-labels']")
        resultobj.verify_data_labels('pfjTableChart_1',['Product Category','Product Category','Product Category','Product Category'],'Step 13.26 : Verify X-Axis titles',custom_css="svg > g text[class='xaxisOrdinal-title']")
        resultobj.verify_data_labels('pfjTableChart_1',['Revenue','Revenue','Revenue','Revenue','Revenue'],'Step 13.27 : Verify Y-Axis titles',custom_css="svg > g text[class='yaxis-title']",data_label_length=7)
        resultobj.verify_data_labels('pfjTableChart_1',['EMEA','North America','Oceania','South America'],'Step 13.28 : Verify column labels',custom_css="svg > g text[class^='colLabel!']")
        resultobj.verify_data_labels('pfjTableChart_1',['Argentina','Australia','Austria','Belgium','Brazil'],'Step 13.29 : Verify Row labels',custom_css="svg > g text[class^='rowLabel!']",data_label_length=6)
        resultobj.verify_riser_legends('pfjTableChart_1',['Customer Business Region','EMEA','North America','Oceania','South America'],'Step 13.30 : Verify legend text')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_13','actual')
        
        """
            Step 14 : Click IA > Save As > "C2231281" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 15 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
         
        """
            Step 16 : Reopen FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2223569.fex&tool=report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#pfjTableChart_1 text[class='rowHeader-label!']", 1,60,string_value='COUNTRY_NAME_1')
        time.sleep(3)
         
        """
            Step 17 : Verify Query pane and Preview
        """
        expected_fields=['Matrix', 'Rows', 'COUNTRY_NAME_1', 'Columns', 'Store,Business,Region', 'Axis', 'Vertical Axis', 'Parameter1', 'Revenue', 'Cost of Goods', 'Gross Profit', 'Horizontal Axis', 'Parameter2', 'Product,Category', 'Product,Subcategory', 'Marker', 'Color BY', 'Customer,Business,Region', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        position=1
        for field in expected_fields :
            metaobj.verify_query_pane_field('Chart (wf_retail_lite)',field,position,'Step 17.'+str(position))
            position+=1
        utillobj.verify_element_text("#pfjTableChart_1 text[class='colHeader-label!']",'Store Business Region','Step 17.23 : Verify vertical title')
        utillobj.verify_element_text("#pfjTableChart_1 text[class='rowHeader-label!']",'COUNTRY_NAME_1','Step 17.24 : Verify Row header label')
        expected_xaxis_label=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production','Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yaxis_label=['0','30M','60M','90M','120M','150M']
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xaxis_label, expected_yaxis_label,'Step 17.25 :',y_custom_css="g[class='scrollRowAxis'] g:nth-child(1) text[class^='yaxis-labels']")
        resultobj.verify_data_labels('pfjTableChart_1',['Product Category','Product Category','Product Category','Product Category'],'Step 17.4 : Verify X-Axis titles',custom_css="svg > g text[class='xaxisOrdinal-title']")
        resultobj.verify_data_labels('pfjTableChart_1',['Revenue','Revenue','Revenue','Revenue','Revenue'],'Step 17.26 : Verify Y-Axis titles',custom_css="svg > g text[class='yaxis-title']",data_label_length=7)
        resultobj.verify_data_labels('pfjTableChart_1',['EMEA','North America','Oceania','South America'],'Step 17.27 : Verify column labels',custom_css="svg > g text[class^='colLabel!']")
        resultobj.verify_data_labels('pfjTableChart_1',['Argentina','Australia','Austria','Belgium','Brazil'],'Step 17.28 : Verify Row labels',custom_css="svg > g text[class^='rowLabel!']",data_label_length=6)
        resultobj.verify_riser_legends('pfjTableChart_1',['Customer Business Region','EMEA','North America','Oceania','South America'],'Step 17.30 : Verify legend text')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_17','actual')
         
        """
            Step 18 : Click Run
            Step 19 : Verify Auto Prompt for Parameterized fields
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#promptPanel label[class='autop-title']",1,20,string_value='Filter Values')
        
        actual_field1=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter1']:not(select)").text.strip().replace('\n',' ')
        actual_field2=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter2']:not(select)").text.strip().replace('\n',' ')
        expected_paramter1="Parameter1 Revenue Revenue Cost of Goods Gross Profit" if browser=='Firefox' else "Parameter1 Revenue"
        expected_paramter2="Parameter2 Product Category Product Category Product Subcategory" if browser=='Firefox' else "Parameter2 Product Category"
        
        utillobj.asequal(actual_field1,expected_paramter1,'Step 11.1 : Verify default amper value for Paramater1')
        utillobj.asequal(actual_field2,expected_paramter2,'Step 11.2 : Verify default amper value for Paramater2')
        
        """
            Step 20 : Click on the "Revenue" dropdown > Select "Cost of Goods"
        """
        iarun.select_amper_value('Parameter1',['Cost of Goods'],False,verify_small_value_list=['Revenue', 'Cost of Goods', 'Gross Profit'])
        
        """
            Step 21 : Click on the "Product,Category" dropdown > Select "Product,Subcategory"
        """
        iarun.select_amper_value('Parameter2',['Product Subcategory'],False,verify_small_value_list=['Product Category', 'Product Subcategory'])
        
        """
            Step 22 : Click the Submit button
        """
        iarun.select_amper_menu('Run')
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        resultobj.wait_for_property("#jschart_HOLD_0 g>text[class='yaxis-title']",1,30,string_value='Cost of Goods')
        
        """
            Step 23 : Step 23 : Verify output
        """
        utillobj.verify_element_text("#jschart_HOLD_0 text[class='colHeader-label!']",'Store Business Region','Step 23.1 : Verify vertical title')
        utillobj.verify_element_text("#jschart_HOLD_0 text[class='rowHeader-label!']",'COUNTRY_NAME_1','Step 23.2 : Verify Row header label')
        expected_xaxis_label=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Contr...', 'Video Editing', 'iPod Docking Station']
        expected_yaxis_label=['0','16M','32M','48M','64M','80M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xaxis_label, expected_yaxis_label,'Step 23.3 :',y_custom_css="g[class='scrollRowAxis'] g:nth-child(1) text[class^='yaxis-labels']")
        resultobj.verify_data_labels('jschart_HOLD_0',['Product Subcategory','Product Subcategory','Product Subcategory','Product Subcategory'],'Step 23.4 : Verify X-Axis titles',custom_css="svg > g text[class='xaxisOrdinal-title']")
        resultobj.verify_data_labels('jschart_HOLD_0',['Cost of Goods','Cost of Goods','Cost of Goods','Cost of Goods','Cost of Goods'],'Step 23.5 : Verify Y-Axis titles',custom_css="svg > g text[class='yaxis-title']",data_label_length=7)
        resultobj.verify_data_labels('jschart_HOLD_0',['EMEA','North America','Oceania','South America'],'Step 23.6 : Verify column labels',custom_css="svg > g text[class^='colLabel!']")
        resultobj.verify_data_labels('jschart_HOLD_0',['Argentina','Australia','Austria','Belgium','Brazil'],'Step 23.7 : Verify Row labels',custom_css="svg > g text[class^='rowLabel!']",data_label_length=6)
        resultobj.verify_riser_legends('jschart_HOLD_0',['Customer Business Region','EMEA','North America','Oceania','South America'],'Step 23.8 : Verify legend text')
        
        self.driver.switch_to_default_content()
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_23','actual')
        
        """
            Step 24 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()