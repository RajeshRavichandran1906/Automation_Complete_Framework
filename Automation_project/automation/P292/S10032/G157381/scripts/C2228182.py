'''
Created on May 18, 2018

@author: BM13368
Test Case ID : http://172.19.2.180/testrail/index.php?/cases/view/2228182&group_by=cases:section_id&group_order=asc&group_id=157381 
Test Case Name : Verify Matrix chart workflow, preview & run
'''
import unittest, time, keyboard
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, ia_ribbon, metadata, visualization_resultarea

class C2228182_TestClass(BaseTestCase):

    def test_C2228182(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2228182"
        utillobj = utillity.UtillityMethods(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj=metadata.MetaData(self.driver)
        resultobj=visualization_resultarea.Visualization_Resultarea(self.driver)
    
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 text", 16, 65)    
             
        """ 
            Step 02:Select Format > Scatter (from Chart Types group).
        """ 
        vis_ribbonobj.select_ribbon_item("Format", "Scatter")
        
        """ 
            Step 03:Double click Gross Profit (to add to Vertical Axis bucket).
        """ 
        metadataobj.double_click_on_data_filed("Measure Groups->Sales->Gross Profit", 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", "Gross Profit", 15)  
        """ 
            Step 04:Drag Discount to Horizontal Axis bucket.
        """ 
        metaobj.drag_drop_data_tree_items_to_query_tree("Discount", 1, "Horizontal Axis", 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisNumeric-title']", "Discount", 15)
             
        """ 
            Step 05:Double click Model (to add to Detail bucket).
        """ 
        metadataobj.double_click_on_data_filed("Dimensions->Product->Product->Model", 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 [class*='riser']", 157, 25)
            
        """ 
            Step 06:Drag Product,Category to Color bucket.
        """ 
        metaobj.drag_drop_data_tree_items_to_query_tree("Product,Category", 1, "Color", 0)
        time.sleep(3)
        metaobj.verify_query_pane_field('Color BY', 'Product,Category', 1, "Step 06::01: Verify Product Category is visible underneath Color bucket")
           
        """ 
            Step 07:Drag Quantity,Sold to Size bucket.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("Quantity,Sold", 1, "Size", 0)
        metaobj.verify_query_pane_field('Size', 'Quantity,Sold', 1, "Step 07::01: Verify Quantity Sold is visible underneath Size bucket")    
            
        """   
            Step 08:Drag Store,Business,Region to Matrix > Columns bucket
        """  
        metadataobj.collapse_data_field_section("Measure Groups")  
        metaobj.drag_drop_data_tree_items_to_query_tree("Store,Business,Region", 1, "Columns", 0)
        metaobj.verify_query_pane_field('Columns', "Store,Business,Region", 1, "Step 08::01: Verify Store, Business, Region is added underneath Columns bucket")
           
        """ 
            Step 09:Drag Store,Business,Region to filter pane>Get Values>All>Select EMEA & North America>Move to right pane of filter>OK>OK
        """ 
        metaobj.drag_drop_data_tree_items_to_filter("Store,Business,Region", 1)
        ia_ribbonobj.create_constant_filter_condition('All',['EMEA', 'North America'])
        
        """
            Verify the created scatter chart in the preview
        """
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 09:01")
        resultobj.verify_number_of_circle("TableChart_1", 1, 315, 'Step 09:02: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("TableChart_1", "Discount","Step 09:03:Verify xaxis title")
        resultobj.verify_yaxis_title("TableChart_1", "Gross Profit", "Step 09:04:Verify yaxis title")
        expected_xval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K', '', '0', '50K', '100K', '150K']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 09:05: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '31K', '15.5K', '0K']
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 09:06:Verify legends")
        utillobj.verify_chart_color("TableChart_1", 'riser!s4!g12!mmarker!r0!c1!', "brick_red", "Step 09:07: Verify the scatter color", custom_css="circle[class='riser!s4!g12!mmarker!r0!c1!']")
        
        """ 
            Step 10:Click Run.
        """ 
        vis_ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 [class='yaxis-title']", "Gross Profit", 30)
             
        """ 
            Step 11:Verify chart displays just EMEA and North America.
        """ 
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        resultobj.verify_visualization_row_column_header_labels('jschart_HOLD_0','columns',expected_header,expected_label,"Step 10:01")
        resultobj.verify_number_of_circle("jschart_HOLD_0", 1, 315, 'Step 10:02: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("jschart_HOLD_0", "Discount","Step 10:03:Verify xaxis title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", "Gross Profit", "Step 10:04:Verify yaxis title")
        expected_xval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K', '', '0', '50K', '100K', '150K']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 10:05: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '31K', '15.5K', '0K']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 09:06:Verify legends")
        utillobj.verify_chart_color("jschart_HOLD_0", 'riser!s4!g12!mmarker!r0!c1!', "brick_red", "Step 10:07: Verify the scatter color", custom_css="circle[class='riser!s4!g12!mmarker!r0!c1!']")
        utillobj.switch_to_default_content(pause=1)
            
        """ 
            Step 12:Click Save in the toolbar > Save as "C2228182" > Click Save.
        """ 
        vis_ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
           
        """   
            Step 13:Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5) 
             
        """ 
            Step 14:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228182.fex
        """ 
        utillobj.infoassist_api_edit(Test_Case_ID, 'Chart', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisNumeric-title']", "Discount", 75)
             
        """ 
            Step 15:Drag "Transaction Date,Component" > "Sale,Year/Quarter" to Matrix Rows bucket
        """ 
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Year/Quarter", 1, "Rows", 0)
        time.sleep(3)
        metaobj.verify_query_pane_field('Rows', 'Sale,Year/Quarter', 1, "Step 15::01: Verify Sale,Year/Quarter is added underneath Rows bucket")
        
        """ 
            Verify preview chart
        """
        expected_header="Store Business Region"
        expected_label=['EMEA','North America']
        expected_header1="Sale Year/Quarter"
        row_header=self.driver.find_element_by_css_selector("#TableChart_1 [class^='rowHeader']").text.strip()
        utillobj.asequal(row_header,expected_header1, "Step 15:01:Verify row header value")
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 15:02")
        resultobj.verify_number_of_circle("TableChart_1", 1, 501, 'Step 15:03: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("TableChart_1", "Discount","Step 15:04:Verify xaxis title")
        resultobj.verify_yaxis_title("TableChart_1", "Gross Profit", "Step 15:05:Verify yaxis title")
        expected_xval_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '', '0', '1,000', '2,000', '3,000']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '', '0', '10K', '20K', '30K', '40K', '50K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 15:06: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '597', '299', '1']
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 15:07: Verify legend values")
        utillobj.verify_chart_color("TableChart_1", 'riser!s4!g12!mmarker!r0!c1!', "brick_red", "Step 15:08: Verify the scatter color", custom_css="circle[class='riser!s4!g12!mmarker!r0!c1!']")
        
        """
            Step 16 :Step 16:Select Home ribbon, type 150 in the Records inbox (do not use a value from the dropdown) > click ENTER.
        """
        vis_ribbonobj.switch_ia_tab('Home')
        time.sleep(2)
        element=self.driver.find_element_by_css_selector("#HomeRecordLimit input[id^='BiTextField']")
        exec("element.clear()")
        exec("element.send_keys('150')")
        keyboard.send('enter')
        utillobj.synchronize_with_number_of_element("#TableChart_1 [class^='riser']", 150, 35)
             
        """ 
            Step 17:Right click Sale,Year/Quarter>Sort>Descending.
        """ 
        metaobj.querytree_field_click("Sale,Year/Quarter", 1, 1, 'Sort')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Sort')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Descending')
        time.sleep(0.5)
        utillobj.synchronize_with_number_of_element("#TableChart_1 circle[class^='riser']", 5143, 35)
        
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header1="Sale Year/Quarter"
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 17:01")
        row_header=self.driver.find_element_by_css_selector("#TableChart_1 [class^='rowHeader']").text.strip()
        utillobj.asequal(row_header,expected_header1, "Step 17:02:Verify row header value")
        resultobj.verify_number_of_circle("TableChart_1", 1, 5144, 'Step 17:03: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("TableChart_1", "Discount","Step 17:04:Verify xaxis title")
        resultobj.verify_yaxis_title("TableChart_1", "Gross Profit", "Step 17:05:Verify yaxis title")
        expected_xval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '', '0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 17:06: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '4,160', '2,090.5', '21']
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 17:07: Verify legend values")
        utillobj.verify_chart_color("TableChart_1", 'riser!s4!g10!mmarker!r0!c0!', "brick_red", "Step 17:08: Verify the scatter color", custom_css="circle[class='riser!s4!g10!mmarker!r0!c0!']")
        expected_datalabel=['2016 Q4']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 17:09 Verify row labels", custom_css=".chartPanel text[class^='rowLabel']", data_label_length=7)
         
          
        """ 
            Step 18:Click Run.
        """ 
        vis_ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 [class='yaxis-title']", "Gross Profit", 30)
             
        """ 
            Step 19:Verify the following chart displays.
        """
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header1="Sale Year/Quarter"
        resultobj.verify_visualization_row_column_header_labels('jschart_HOLD_0','columns',expected_header,expected_label,"Step 19:01")
        row_header=self.driver.find_element_by_css_selector("#jschart_HOLD_0 [class^='rowHeader']").text.strip()
        utillobj.asequal(row_header,expected_header1, "Step 19:02:Verify row header value")
        resultobj.verify_number_of_circle("jschart_HOLD_0", 1, 5144, 'Step 19:03: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("jschart_HOLD_0", "Discount","Step 19:04:Verify xaxis title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", "Gross Profit", "Step 19:05:Verify yaxis title")
        expected_xval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '', '0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '', '0', '100K', '200K', '300K', '400K', '', '0', '100K', '200K', '300K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 19:06: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '4,288']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 19:07: Verify legend values")
        utillobj.verify_chart_color("jschart_HOLD_0", 'riser!s4!g12!mmarker!r0!c1!', "brick_red", "Step 19:08: Verify the scatter color", custom_css="circle[class='riser!s4!g12!mmarker!r0!c1!']")
        expected_datalabel=['2016 Q4', '2016 Q3', '2016 Q2', '2016 Q1', '2015 Q4', '2015 Q3', '2015 Q2']
        resultobj.verify_data_labels("jschart_HOLD_0", expected_datalabel, "Step 19:09 Verify row labels", custom_css=".chartPanel text[class^='rowLabel']", data_label_length=7)
        utillobj.switch_to_default_content(pause=2)
            
        """   
            Step 20:Right click "Model" from Query pane > Delete.
        """ 
        metaobj.querytree_field_click("Model", 1, 1, 'Delete')
        time.sleep(3)
        metaobj.verify_field_available_in_query_pane('Size', 'Model', 'Color BY', "Step 20:01:Verify Model is feld is deleted", availability=False)
        resultobj.verify_number_of_circle("TableChart_1", 1, 151, 'Step 20:05: Verify number of Circle displayed')
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header1="Sale Year/Quarter"
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 20:06")
        row_header=self.driver.find_element_by_css_selector("#TableChart_1 [class^='rowHeader']").text.strip()
        utillobj.asequal(row_header,expected_header1, "Step 20:07:Verify row header value")
        
        """ 
            Step 21:Double click Store > "Store,City" (to add to Detail bucket).
        """
        metadataobj.collapse_data_field_section("Sales_Related") 
        metadataobj.double_click_on_data_filed("Dimensions->Store->Store->Store,City", 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table tr:nth-child(16)", "Store,City", 15)
           
        """ 
            Step 22:Double click Query Variables/Store Front (to add to filter pane with Is True).
        """ 
        metadataobj.double_click_on_data_filed("Filters and Variables->Store Front", 1)
        utillobj.synchronize_with_visble_text("#qbFilterBox div>table>tbody>tr:nth-child(2)", "Store Front Is true", 20)
        metaobj.verify_filter_pane_field('Store Front Is true', 2, "Step 22: Verify the filter pane")
             
        """ 
            Step 23:Select Home ribbon > Records dropdown > 500.
        """
        vis_ribbonobj.switch_ia_tab('Home')
        time.sleep(2)
        element=self.driver.find_element_by_css_selector("#HomeRecordLimit input[id^='BiTextField']")
        exec("element.clear()")
        exec("element.send_keys('500')")
        keyboard.send('enter')
        utillobj.synchronize_with_number_of_element("#TableChart_1 circle[class^='riser']", 500, 35)
              
        """ 
            Step 24:Verify the following chart displays.
        """
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header1="Sale Year/Quarter"
        row_header=self.driver.find_element_by_css_selector("#TableChart_1 [class^='rowHeader']").text.strip()
        utillobj.asequal(row_header,expected_header1, "Step 24:01:Verify row header value")
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 24:02")
        resultobj.verify_number_of_circle("TableChart_1", 1, 501, 'Step 24:03: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("TableChart_1", "Discount","Step 24:04:Verify xaxis title")
        resultobj.verify_yaxis_title("TableChart_1", "Gross Profit", "Step 24:05:Verify yaxis title")
        expected_xval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '', '0', '5K', '10K', '15K']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 24:06: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '3,096', '1,5550', '4']
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 24:07: Verify legend values")
        utillobj.verify_chart_color("TableChart_1", 'riser!s4!g14!mmarker!r0!c1!', "brick_red", "Step 24:08: Verify the scatter color", custom_css="circle[class='riser!s4!g14!mmarker!r0!c1!']")
        expected_datalabel=['2016 Q4']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 24:09 Verify row labels", custom_css=".chartPanel text[class^='rowLabel']") 
            
        """ 
            Step 25:Run.
        """ 
        vis_ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
            
        """ 
            Step 26:Verify the following chart displays.
        """ 
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header1="Sale Year/Quarter"
        row_header=self.driver.find_element_by_css_selector("#jschart_HOLD_0 [class^='rowHeader']").text.strip()
        utillobj.asequal(row_header,expected_header1, "Step 24:01:Verify row header value")
        resultobj.verify_visualization_row_column_header_labels('jschart_HOLD_0','columns',expected_header,expected_label,"Step 26:02")
        resultobj.verify_number_of_circle("jschart_HOLD_0", 1, 6234, 'Step 26:03: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("jschart_HOLD_0", "Discount","Step 26:04:Verify xaxis title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", "Gross Profit", "Step 26:05:Verify yaxis title")
        expected_xval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '', '0', '5K', '10K', '15K', '20K']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K', '', '0', '40K', '80K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 26:06: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '3,096']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 26:07: Verify legend values")
        utillobj.verify_chart_color("jschart_HOLD_0", 'riser!s4!g14!mmarker!r0!c1!', "brick_red", "Step 26:08: Verify the scatter color", custom_css="circle[class='riser!s4!g14!mmarker!r0!c1!']")
        expected_datalabel=['2016 Q4', '2016 Q3', '2016 Q2', '2016 Q1', '2015 Q4', '2015 Q3', '2015 Q2']
        resultobj.verify_data_labels("jschart_HOLD_0", expected_datalabel, "Step 26:09 Verify row labels", custom_css=".chartPanel text[class^='rowLabel']", data_label_length=7)
        utillobj.switch_to_default_content(pause=2)
            
        """ 
            Step 27:Click Save > click Ok.
        """ 
        vis_ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
             
        """ 
            Step 28:Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        utillobj.infoassist_api_logout()
        time.sleep(3)
             
        """ 
            Step 29:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228182.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisNumeric-title']", "Discount", 75)
        
        """    
            Step 30:Verify chart restores without error.
        """
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header1="Sale Year/Quarter"
        row_header=self.driver.find_element_by_css_selector("#TableChart_1 [class^='rowHeader']").text.strip()
        utillobj.asequal(row_header,expected_header1, "Step 30:01:Verify row header value")
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 30:02")
        resultobj.verify_number_of_circle("TableChart_1", 1, 501, 'Step 30:03: Verify number of Circle displayed')
        resultobj.verify_xaxis_title("TableChart_1", "Discount","Step 30:04:Verify xaxis title")
        resultobj.verify_yaxis_title("TableChart_1", "Gross Profit", "Step 30:05:Verify yaxis title")
        expected_xval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '', '0', '5K', '10K', '15K']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 30:06: Verify X and Y axis labels')
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Quantity Sold', '3,096', '1,5550', '4']
        resultobj.verify_riser_legends("TableChart_1", expected_legend_list, "Step 30:07: Verify legend values")
        utillobj.verify_chart_color("TableChart_1", 'riser!s4!g14!mmarker!r0!c1!', "brick_red", "Step 30:08: Verify the scatter color", custom_css="circle[class='riser!s4!g14!mmarker!r0!c1!']")
        expected_datalabel=['2016 Q4']
        resultobj.verify_data_labels("TableChart_1", expected_datalabel, "Step 30:09 Verify row labels", custom_css=".chartPanel text[class^='rowLabel']") 
            
        """ 
            Step 31:Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()