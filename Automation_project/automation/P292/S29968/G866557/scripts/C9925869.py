'''
Created on Aug 26, 2019

@author: Vpriya

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/9925869
TestCase Name : Core JOIN functional workflow (Add/Delete/Save/Reopen) - Chart
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.lib.utillity import UtillityMethods
from common.wftools.designer import joining_data
from common.locators.designer_chart_locators import DesignerChart as dc_locators

class C9925869_TestClass(BaseTestCase):

    def test_C9925869(self):
        """
            CLASS OBJECTS 
        """
        designer_chart_obj=Designer_Chart(self.driver)
        utils=UtillityMethods(self.driver)
        joining_data_obj=joining_data.Joining_Data(self.driver)
        
        """
            TESTCASE CSS 
        """
        
        DATA_TAB_CSS ="[role='tablist'] .wb-data-tab-button"
        QUERY_BOX_CSS = ".wfc-bucket-display-box"
        RUN_PARENT_CSS = '#jschart_HOLD_0'
        
        
        """
            TESTCASE ID Variable 
        """
        JOIN_TYPES   = ['Inner', 'Left Outer', 'Right Outer', 'Full Outer']
        FIELDS_AFTER_JOINING = ["Product Dimension","Customer Dimension","Store Dimension"]
        X_AXIS_LABEL = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        Y_AXIS_LABEL = ['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        PREVIEW_LEGENDS = ['Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        X_AXIS_TITLE = ['Product Category']
        Y_AXIS_TITLE = ['Revenue']
        WARNING_MESSAGE = 'The source baseapp/dimensions/wf_retail_geography (T05) is in use. Do you still want to delete baseapp/dimensions/wf_retail_store (T04)?'
        
        """
        JOIN_1 variables
        """
        NODE_NAME_1           = ['wf_retail_product (T02)','Join 1','wf_retail_sales (T01)']
        JOIN_CONDITION_1      =  ['ID Product=ID Product']
        SAMPLE_DATA_FILE_NAME_1 =  "c9925869_step5"
        
        
        """
        JOIN_2 variables
        """
        NODE_NAME_2       = ['wf_retail_product (T02)','Join 1','wf_retail_sales (T01)','Join 2','wf_retail_store (T03)']
        JOIN_CONDITION_2  = ['ID Store=ID Store']
        SAMPLE_DATA_FILE_NAME_2 = "c9925869_step6"
        
        """
        JOIN_3 Variables
        """
        NODE_NAME_3 = ['wf_retail_product (T02)','Join 1','wf_retail_sales (T01)','Join 2','wf_retail_store (T03)','Join 3',
                                 'wf_retail_geography (T04)']
        
        JOIN_CONDITION_3 = ['T03.ID Geography=ID Geography']
        
        SAMPLE_DATA_FILE_NAME_3  = "c9925869_step7"
        
        """
        MULTIPLE_JOIN variables
        """
        MULTIPLE_JOIN_NODES = ['wf_retail_sales (T01)','Join 1','wf_retail_product (T02)',
                                 'wf_retail_customer (T03)','wf_retail_geography (T06)','wf_retail_store (T04)',
                                 'wf_retail_geography (T05)','Join 5','Join 2','Join 3','Join 4']
        
        MULTIPLE_JOIN_CONDITION = ['T03.ID Geography=ID Geography']
        MULTIPLE_JOIN_SAMPLE_DATA = "c9925869_step9"
        
        
        """
        STEP 1:Launch the API to create new Designer chart with wf_retail_sales master file as developer user:
  
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG728361%2F&master=baseapp%2Ffacts%2Fwf_retail_sales&tool=chart
  
        Designer chart created without error and Dimensions tree is empty.
          
        """
          
        designer_chart_obj.invoke_designer_chart_using_api("baseapp/facts/wf_retail_sales", mrid='mrid', mrpass='mrpass')
        utils.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS,designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_number_of_risers(".risers rect", 5, 5,"Step 01:01 Verify the number of risiers in preview")
        designer_chart_obj.verify_dimensions_field_is_empty("Step 01:02")
        utils.verify_object_visible(".chart-picker-box",True,"Step 01:03 verify the chart picker icon")
        utils.verify_object_visible(".pop-top",False,"Step 01:04 Verify the chart opens without any error")
        designer_chart_obj.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'],msg="Step 01:05")
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '40', '80', '120', '160', '200'],msg="Step 01:06")
        designer_chart_obj.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'],msg="Step 01:07")
          
        """
        Step 2:Select Data tab in designer.
        Data canvas visible without error.
        """
        utils.synchronize_with_visble_text(DATA_TAB_CSS,"Data",designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.select_tab_button("Data")
        joining_data_obj.switch_to_frame()
        utils.synchronize_until_element_is_visible(".wcx-grid-body-row-cell",designer_chart_obj.chart_long_timesleep)
        utils.verify_object_visible(".pop-top",False,"Step 02:01 Verify the data opens without any error")
        joining_data_obj.canvas(['wf_retail_sales']).verify_node_available("02.01")
        joining_data_obj.canvas(['wf_retail_sales'],"c9925869_step2").verify_canvas_image("Step 02:03 Data canvas visible without error.")
  
        """
        Step 3:From the database tree single click on "< facts" to move up a level in the database tree.
        """
        joining_data_obj.resource_tree(['wf_retail_sales','facts']).back_to()
          
        """
        Step 4:From the database tree single click on dimensions folder to drill down to the files there.
        """
        joining_data_obj.resource_tree(['dimensions']).click()
          
        """
        Step 5:Drag and drop wf_retail_product onto wf_retail_sales.
        """
        """
        Step 05:01 Join 1 created without error.
        """
        joining_data_obj.resource_tree(['wf_retail_product']).drag_to_canvas('wf_retail_sales')
        joining_data_obj.canvas(NODE_NAME_1,'c9925869_step5_01').verify_canvas_image("Step 05:01 Join 1 created without error.")
        joining_data_obj.canvas(NODE_NAME_1).verify_node_available("05:02")
        joining_data_obj.configure().verify_join_types(JOIN_TYPES,"05.03")
        joining_data_obj.configure().verify_conditions(JOIN_CONDITION_1,"05.05")
        joining_data_obj.configure().verify_configure_image("c9925869_step5_06.png","Step:05:06")
        #joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_1).create_data_set()
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_1).verify_data_set("05.07")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_1).verify_header_numeric_icons([1,4,5,6,7,8],"Step 05.08")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_1).verify_header_alpha_icons([11,12,13,15,16],"Step 05.09")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_1).verify_header_key_icons([2,3], "Step 05.10")
          
          
        """
        Step 6:Drag and drop wf_retail_store onto wf_retail_sales.
        """
        """
        Step 06:01 Join 2 created without error.
        """
        joining_data_obj.resource_tree(['wf_retail_store']).drag_to_canvas('wf_retail_sales (T01)')
        joining_data_obj.canvas(NODE_NAME_2,'c9925869_step6_01').verify_canvas_image("Step 06:01 Join 2 created without error")
        joining_data_obj.canvas(NODE_NAME_2).verify_node_available("06:02")
        joining_data_obj.configure().verify_join_types(JOIN_TYPES,"06.03")
        joining_data_obj.configure().verify_conditions(JOIN_CONDITION_2,"06.05")
        time.sleep(5)
        #joining_data_obj.configure().verify_configure_image("c9925869_step6_06.png","Step:06:06")
        #joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_2).create_data_set()
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_2).verify_data_set("06.07")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_2).verify_header_numeric_icons([1,4,5,6,7,8],"Step 06.08")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_2).verify_header_alpha_icons([11,12,13],"Step 06.09")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_2).verify_header_key_icons([2,3], "Step 06.10")
          
        """
        Step 7:Drag and drop wf_retail_geography onto the Join 2 icon.
        """
        joining_data_obj.resource_tree(['wf_retail_geography']).drag_to_canvas('Join 2')
          
        """
        Step 07.01:Join 3 created without error.
        """
        joining_data_obj.canvas(NODE_NAME_3,'c9925869_step7_01').verify_canvas_image("Step 07.01:Join 3 created without error.")
        joining_data_obj.canvas(NODE_NAME_3).verify_node_available("07:02")
        joining_data_obj.configure().verify_join_types(JOIN_TYPES,"07.03")
        joining_data_obj.configure().verify_conditions(JOIN_CONDITION_3,"07.05")
        joining_data_obj.configure().verify_configure_image("c9925869_step7_06.png","Step:07:06")
        #joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_3).create_data_set()
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_3).verify_data_set("07.07")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_3).verify_header_numeric_icons([1,3,6],"Step 07.08")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_3).verify_header_alpha_icons([12,13,14],"Step 07.09")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_3).verify_header_key_icons([2,4], "Step 07.10")
          
        """
        Step 8:Right click Join 2 and select Delete.
        """
        joining_data_obj.canvas(['Join 2']).select_option_from_right_click("Delete")
        time.sleep(6)
          
        """
        Step 08:01Join 2, Join 3, wf_retail_store and wf_retail_geography pills are deleted. The sample data frame is no longer present.
        """
        joining_data_obj.canvas(NODE_NAME_1).verify_node_available("08:01")
        joining_data_obj.canvas(NODE_NAME_1,'c9925869_step8_02').verify_canvas_image("Step 8:01 join canvas")
        joining_data_obj.sample_data(SAMPLE_DATA_FILE_NAME_3).verify_sample_data_frame_visiblity(False,"Step 8:02")
          
  
        """
        Step 9: Drag and drop wf_retail_customer onto wf_retail_sales;
        Drag and drop wf_retail_store onto wf_retail_sales;
        Drag and drop wf_retail_geography onto Join 3 icon;
        Drag and drop wf_retail_geography onto Join 2 icon.
        """
        joining_data_obj.resource_tree(['wf_retail_customer']).drag_to_canvas('wf_retail_sales (T01)')
        joining_data_obj.resource_tree(['wf_retail_store']).drag_to_canvas('wf_retail_sales (T01)')
        joining_data_obj.resource_tree(['wf_retail_geography']).drag_to_canvas('Join 3')
        joining_data_obj.resource_tree(['wf_retail_geography']).drag_to_canvas('Join 2')
          
        """
        Step 09:01 Joins created without error and the sample data frame was restored
        """
        joining_data_obj.canvas(MULTIPLE_JOIN_NODES,'c9925869_step9_01').verify_canvas_image(" step 09:01 Joins created without error and the sample data frame was restored.")
        joining_data_obj.canvas(MULTIPLE_JOIN_NODES,'c9925869_step9_01').verify_node_available("09:02")
        joining_data_obj.configure().verify_join_types(JOIN_TYPES,"09.03")
        joining_data_obj.configure().verify_conditions(MULTIPLE_JOIN_CONDITION,"09.05")
        joining_data_obj.configure().verify_configure_image("c9925869_step9_06","Step:09:06")
        joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).verify_sample_data_frame_visiblity(True , "Step:09:07")
        #joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).create_data_set()
        joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).verify_data_set("Step:09:08")
        joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).verify_header_numeric_icons([1,3,6],"Step 09.09")
        joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).verify_header_alpha_icons([20],"Step 09.10")
        joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).verify_header_key_icons([2,4],"Step 09.11")
        joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).verify_geo_location_icons([15,18],"Step 09:12")
        joining_data_obj.switch_to_default_content()
        
        """
        Step 10:Click Chart 1 tab.
        """
        """
        Step 10:01 Product, Customer and Store folders available in Dimension and Measures Fields tree.
        """
        designer_chart_obj.select_tab_button("Chart 1")
        utils.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS,designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_fields_in_dimensions(FIELDS_AFTER_JOINING,"Step 10.01 product customer filed sin dimensions",compare_type='asin')
        designer_chart_obj.verify_fields_in_measures(FIELDS_AFTER_JOINING,"Step 10.02 product customer fileds in Measures",compare_type='asin',field_path='Product Dimension')
          
        """
        Step 11:Expand Customer Dimension and Store Dimension.
        Geography Dimension node is available.
        """
        designer_chart_obj.verify_fields_in_dimensions(['Geography Dimension'],"Step 11:",compare_type='asin',
                                                       field_path="Customer Dimension->Geography Dimension")
        designer_chart_obj.verify_fields_in_dimensions(['Geography Dimension'],"Step 11:",compare_type='asin',
                                                       field_path="Store Dimension->Geography Dimension")
          
        """
        Step 12:Add Revenue field to Vertical bucket,
        Product Category to Horizontal bucket,
        Drag and drop "Business Region" to Color bucket present under Store > Geography.
        """
        designer_chart_obj.double_click_on_measures_field("Revenue")
        designer_chart_obj.wait_for_visible_text(QUERY_BOX_CSS, "Revenue", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_dimension_field("Product Dimension->Product,Category")
        designer_chart_obj.wait_for_visible_text(QUERY_BOX_CSS, "Product,Category", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.drag_and_drop_click_on_dimension_field_to_bucket_container('Store Dimension->Geography Dimension->Business,Region','Color')
        designer_chart_obj.wait_for_visible_text(QUERY_BOX_CSS, "Business,Region", designer_chart_obj.chart_medium_timesleep)
          
        """
        Step 12:01Live preview updated without error.
        """
        time.sleep(1)
        designer_chart_obj.verify_x_axis_label_in_preview(X_AXIS_LABEL,msg="Step:12.01 xaxis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Y_AXIS_LABEL,msg="Step:12.02 yaxislabel")
        designer_chart_obj.verify_number_of_risers("rect", 4, 7, msg="Step:12:03")
        designer_chart_obj.verify_x_axis_title_in_preview(X_AXIS_TITLE,msg="step:12:04 x-axis title")
        designer_chart_obj.verify_y_axis_title_in_preview(Y_AXIS_TITLE,msg="Step:12:05 y axis title")
        designer_chart_obj.verify_legends_in_preview(PREVIEW_LEGENDS,msg="Step:12:06 verify legends in preview")
  
        """
        Step 13:Click Save and enter "c9925869" in Title and click Save button.
        """
        designer_chart_obj.save_designer_chart_from_toolbar("c9925869")
           
 
        """
        Step 14:Run the chart using API:
         
        http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S29835%252FG728361%252F&BIP_item=c9925869.fex.
         
        Chart runs successfully.
        """
        designer_chart_obj.api_logout()
        designer_chart_obj.run_designer_chart_using_api("c9925869")
        designer_chart_obj.wait_for_visible_text("text[class^='xaxis'][class$='title']",'Product Category',designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_title_in_preview(X_AXIS_TITLE, parent_css=RUN_PARENT_CSS,msg="Step14.1")
        designer_chart_obj.verify_y_axis_title_in_preview(Y_AXIS_TITLE,parent_css=RUN_PARENT_CSS,msg="Step:14:02 y axis title")
        designer_chart_obj.verify_legends_in_preview(PREVIEW_LEGENDS,parent_css=RUN_PARENT_CSS,msg="Step:14:03 verify legends in preview")
        designer_chart_obj.verify_x_axis_label_in_preview(X_AXIS_LABEL,parent_css=RUN_PARENT_CSS,msg="Step:14.04 xaxis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Y_AXIS_LABEL,parent_css=RUN_PARENT_CSS,msg="Step:14.05 yaxislabel")
        designer_chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 4, 7,msg="Step:14.06")
          
        """
        Step 15:Restore saved c9925869 chart using API:
        
        http://domain:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG728361%2Fc9925869.fex
        
        Chart restored without error and Product, Customer and Store folders available in both Dimensions and Measures Fields.
        """
        
        designer_chart_obj.api_logout()
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c9925869')
        designer_chart_obj.wait_for_visible_text("text[class^='xaxis'][class$='title']",'Product Category',designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(X_AXIS_LABEL,msg="Step:15.01 xaxis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Y_AXIS_LABEL,msg="Step:15.02 yaxislabel")
        designer_chart_obj.verify_number_of_risers("rect", 4, 7, msg="Step:15:03")
        designer_chart_obj.verify_x_axis_title_in_preview(X_AXIS_TITLE,msg="step:15:04 x-axis title")
        designer_chart_obj.verify_y_axis_title_in_preview(Y_AXIS_TITLE,msg="Step:15:05 y axis title")
        designer_chart_obj.verify_legends_in_preview(PREVIEW_LEGENDS,msg="Step:15:06 verify legends in preview")

        """
        Step 16:Select Data tab present at bottom left corner.
        """
        """
        Step 16:01 Created joins present in the same position.
        """
        designer_chart_obj.select_tab_button("Data")
        joining_data_obj.switch_to_frame()
        utils.synchronize_with_number_of_element(".wcx-graph-node",11,designer_chart_obj.chart_long_timesleep)
        utils.verify_object_visible(".pop-top",False,"Step 02:01 Verify the data opens without any error")
        joining_data_obj.canvas(MULTIPLE_JOIN_NODES,'c9925869_step9_01').verify_canvas_image(" step 16:01 Joins created without error and the sample data frame was restored.")
        joining_data_obj.canvas(MULTIPLE_JOIN_NODES,'c9925869_step9_01').verify_node_available("16:02")
        joining_data_obj.sample_data(MULTIPLE_JOIN_SAMPLE_DATA).verify_sample_data_frame_visiblity(True , "Step:16:03")
        

        """
        Step 17:Right click Join 2 and select Delete.
        wf_retail_customer and its related wf_retail_geography nodes are deleted.
        """
        joining_data_obj.canvas(['Join 2']).select_option_from_right_click("Delete")
        time.sleep(2)
        joining_data_obj.canvas(['Join 2'],'c9925869_step17_01').verify_canvas_image("Step 17:wf_retail_customer and its related wf_retail_geography nodes are deleted.")

        """
        Step 18:Right click Join 3 and select Delete.
        A warning message pops up that the Join is in use by the query.
        """
        joining_data_obj.canvas(['Join 3']).select_option_from_right_click("Delete")
        joining_data_obj.canvas().verify_warning_dialog_content(WARNING_MESSAGE,"Step 18:02")

        """
        Step 19:Select Cancel from the warning box
        
        Select "c9925869" tab below the data prep canvas.
        """
        joining_data_obj.canvas().select_button_in_warning_dialog("Cancel")
        joining_data_obj.switch_to_default_content()
        designer_chart_obj.select_tab_button("c9925869")
        designer_chart_obj.wait_for_visible_text("text[class^='xaxis'][class$='title']",'Product Category',designer_chart_obj.chart_medium_timesleep)
        
        """
        Hover over Business Region in the Color Bucket and click on the "x" at the right edge to remove this from the bucket.
        
        Live preview updated.
        """
        
        designer_chart_obj.remove_query_bucket_field('Color',"Business,Region")
        time.sleep(2)
        designer_chart_obj.wait_for_visible_text("text[class^='xaxis'][class$='title']",'Product Category',designer_chart_obj.chart_medium_timesleep)

        """
        Step 20:Select Data tab present at bottom left corner.
        
        Right click Join 3 and select Delete.

        Join 3 and its related nodes are deleted.
        """
        designer_chart_obj.select_tab_button("Data")
        joining_data_obj.switch_to_frame()
        utils.synchronize_with_number_of_element(".wcx-graph-node",7,designer_chart_obj.chart_long_timesleep)
        joining_data_obj.canvas(['Join 3']).select_option_from_right_click("Delete")
        

        """
        Step 21:Select "c9925869" tab below the data prep canvas.
        
        Only Product node visible in both Dimensions and Measures tree.
        """
        joining_data_obj.switch_to_default_content()
        designer_chart_obj.select_tab_button("c9925869")
        designer_chart_obj.wait_for_visible_text("text[class^='xaxis'][class$='title']",'Product Category',designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_fields_in_dimensions(['Customer Dimension'],"Step 21.01 customer filed is not dimensions",compare_type='asnotin')
        designer_chart_obj.verify_fields_in_measures(['Customer Dimension'],"Step 21.02  customer filed is not in Measures",compare_type='asnotin')
        designer_chart_obj.verify_fields_in_measures(['Geography Dimension'],"Step 21.03  Geography filed is not in Measures",compare_type='asnotin')
        designer_chart_obj.verify_fields_in_dimensions(['Geography Dimension'],"Step 21.04  Geography filed is not in Dimension",compare_type='asnotin')
        
        """
        Step 22:Click Application menu and click Save as, enter "c9925869_1" in Title and click Save as.
        """
        
        designer_chart_obj.save_as_from_application_menu("c9925869_1")
     
        """
        Step 23:Run c9925869_1 chart using API:
        http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S29835%252FG728361%252F&BIP_item=c9925869_1.fex.
        Chart runs successfully.
        """
        designer_chart_obj.api_logout()
        designer_chart_obj.run_designer_chart_using_api("c9925869_1")
        designer_chart_obj.wait_for_visible_text("text[class^='xaxis'][class$='title']",'Product Category',designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_title_in_preview(X_AXIS_TITLE, parent_css=RUN_PARENT_CSS,msg="Step 23.1")
        designer_chart_obj.verify_y_axis_title_in_preview(Y_AXIS_TITLE,parent_css=RUN_PARENT_CSS,msg="Step:23:02 y axis title")
        designer_chart_obj.verify_x_axis_label_in_preview(X_AXIS_LABEL,parent_css=RUN_PARENT_CSS,msg="Step:23.04 xaxis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Y_AXIS_LABEL,parent_css=RUN_PARENT_CSS,msg="Step:23.05 yaxislabel")
        designer_chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 7,msg="Step:23.06")
        
        
        """
        Step 24:Restore saved c9925869_1 chart using API:
        http://domain:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG728361%2Fc9925869_1.fex
        Chart restored without error and Product node available in both Dimensions and Measures Fields.
        """
        
        designer_chart_obj.api_logout()
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c9925869_1')
        designer_chart_obj.wait_for_visible_text("text[class^='xaxis'][class$='title']",'Product Category',designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(X_AXIS_LABEL,msg="Step:24.01 xaxis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Y_AXIS_LABEL,msg="Step:24.02 yaxislabel")
        designer_chart_obj.verify_number_of_risers("rect", 1, 7, msg="Step:24:03")
        designer_chart_obj.verify_x_axis_title_in_preview(X_AXIS_TITLE,msg="step:24:04 x-axis title")
        designer_chart_obj.verify_y_axis_title_in_preview(Y_AXIS_TITLE,msg="Step:24:05 y axis title")

        """
        Step 25:Select the Data tab to open the data prep canvas.
        Join 1 available in the data prep canvas.
        """
        designer_chart_obj.select_tab_button("Data")
        joining_data_obj.switch_to_frame()
        utils.synchronize_with_number_of_element(".wcx-graph-node",3,designer_chart_obj.chart_long_timesleep)
        joining_data_obj.canvas().verify_node_available("Step:25")
        time.sleep(2)
        joining_data_obj.switch_to_default_content()

        """
        Step 26:Log out WF using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

        
if __name__ == '__main__':
    unittest.main()