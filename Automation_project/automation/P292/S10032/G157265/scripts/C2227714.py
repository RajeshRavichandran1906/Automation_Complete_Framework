'''
Created on Jun 19, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227714
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon

class C2227714_TestClass(BaseTestCase):

    def test_C2227714(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227714'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01 : Launch the IA API with wf_retail_lite, Visualization mode:
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", 'Drop Measures', 160)
        
        """
            Step 02 : Select Change > Grid in the Home Tab ribbon
            Step 03 : Verify Preview
        """
        ribbonobj.change_chart_type('grid')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1", 'Drag fields', 30)
        resultobj.verify_panel_caption_label(0, 'Grid1', "Step02: Verify Grid1 is displayed")
         
        """
            Step 04 : Add fields "Store,Country", "Product,Category", and "Revenue"
        """    
        metaobj.datatree_field_click("Store,Country", 2, 1)       
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Store Country', 30)
        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Product Category', 30)
        
        metaobj.datatree_field_click("Revenue",2,1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f", 'Revenue', 30)
        
        """
            Step05: Drag and drop "Store,Country" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("Store,Country", 1) 
        utillobj.synchronize_with_visble_text("#avFilterOkBtn", 'OK', 30)
         
        """
            Step 06 : De-select [All] to de-select all values
            Step 07 : Check off values: Brazil, Canada, China, United States > click OK        
        """
        if Global_variables.browser_name == 'chrome':
            self.select_or_verify_visualization_filter_values(['[All]','Brazil','Canada'])
            time.sleep(2)
            self.select_or_verify_visualization_filter_values(['United States'] ,scroll_down=True)
            metaobj.create_visualization_filters('alpha')
        else:
            l=['[All]','Brazil','Canada','United States']
            metaobj.create_visualization_filters('alpha',['GridItems',l])
        utillobj.synchronize_with_visble_text("#ar_Prompt_1", 'Store,Country', 30)
        propertyobj.select_or_verify_show_prompt_item('1', 'China')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f .rowLabels", 'China', 60)
        
        """
            Step 08 : Verify Preview
        """
        metaobj.verify_query_pane_field('Grid1',"Rows",1,"Step08: Verify Grid1")
        metaobj.verify_query_pane_field('Store,Country',"Product,Category",1,"Step08: Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step08: Verify Revenue in measure")
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=False,msg="Step08: Verify All unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Brazil',verify=True, verify_type=True,msg="Step08: Verify Brazil checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Canada',verify=True, verify_type=True,msg="Step08: Verify Canada checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'China',verify=True, verify_type=True,msg="Step08: Verify China checked in prompt")
        rise=len(self.driver.find_elements_by_css_selector("#TableChart_1 rect[class^='riser']"))
        utillobj.asequal(rise,28,"Step08: Verify Grid1 risers")
         
        """
            Step 09 : Select Insert > Chart in the Home Tab
        """
        ribbonobj.select_ribbon_item('Home', 'Insert',opt='Chart')
        utillobj.synchronize_with_visble_text("#pfjTableChart_2", 'Drop Measures', 120)
       
        resultobj.verify_panel_caption_label(0, 'Bar Stacked1', "Step10: Verify Bar Stacked1 is displayed")
        resultobj.verify_panel_caption_label(1, 'Grid1', "Step10: Verify Grid1 is displayed")
        
        """
            Step 10  : Step 10 : Add fields "Store,Country", "Product,Category", and "Cost of Goods"
        """
        metaobj.datatree_field_click("Store,Country", 2, 1)       
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f text.xaxisOrdinal-title", 'Store Country', 30)
        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f text.xaxisOrdinal-title", 'Store Country : Product Category', 30)
       
        metaobj.datatree_field_click("Cost of Goods",2,1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f text.yaxis-title", 'Cost of Goods', 30)
        
        """
            Step 11 : Verify Preview
        """  
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step11:d(i) Verify Y-Axis Title")
        expected_xval_list=['Brazil: Accessories','Brazil: Camcorder', 'Brazil: Computers']
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 28, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step11.c: Verify first bar color")
        heading = ['Store C...', 'Product C...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step11: Verify column titles')
        row_val=['Brazil','Accessories', '$3,174,057.03']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step11: verify grid 1st row value')
         
        """
            Step 12 : Drag and drop "Product,Category" into the Filter pane
            Step 13 : De-select [All] to de-select all values
            Step 14 : Check off values: Computers, Media Player, and Televisions > click OK
        """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        utillobj.synchronize_with_visble_text("#avFilterOkBtn", 'OK', 30) 
       
        l=['[All]','Computers', 'Media Player','Televisions']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        utillobj.synchronize_with_visble_text("#ar_Prompt_2", 'Product,Category', 30, pause_time=2)
         
        """
            Step 15 : Verify Preview
        """
        propertyobj.select_or_verify_show_prompt_item('2', '[All]',verify=True, verify_type=False,msg="Step15: Verify All unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Computers',verify=True, scroll_down=True,verify_type=True,msg="Step15: Verify Computers checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Media Player',verify=True,scroll_down=True, verify_type=True,msg="Step15: Verify Media Player checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Televisions',verify=True,scroll_down=True, verify_type=True,msg="Step15: Verify Televisions checked in prompt")
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step15:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step15:d(i) Verify Y-Axis Title")
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step15.c: Verify first bar color")
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step15: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step15: verify grid 1st row value')
     
        """
            Step16 : Click "New" in the toolbar > select "Build a Visualization" > select wf_retail_lite
        """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        ribbonobj.select_item_in_splash_options('Build a Visualization')
        utillobj.synchronize_with_visble_text("#TableChart_1", 'Drop Measures', 160)
        
        """
            Step17 : Add fields "Cost of Goods" and "Product,Subcategory"
        """
        metaobj.datatree_field_click("Cost of Goods",2,1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text.yaxis-title", 'Cost of Goods', 30)
        
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text.xaxisOrdinal-title", 'Product Subcategory', 30)

        """
            Step18 : Drag and drop "Product,Category" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        utillobj.synchronize_with_visble_text("#avFilterOkBtn", 'OK', 30) 
         
        """
            Step19 : De-select [All] to de-select all values
            Step20 : Check off values: Computers and Televisions > click OK        
        """
        l=['[All]','Computers','Televisions']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        utillobj.synchronize_with_visble_text("#ar_Prompt_1", 'Product,Category', 30, pause_time=2)
 
        """
            Step21 : Verify Preview
        """  
        xaxis_value="Product Subcategory"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step21:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", "Cost of Goods", "Step21:d(i) Verify Y-Axis Title")
        expected_xval_list=['CRT TV','Flat Panel TV','Portable TV','Smartphone','Tablet']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step21.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar", "bar_blue", "Step21.c: Verify first bar color")

        """
            Step22 : Click the switch "Reports" shortcut in the lower right corner
            Step23 : Select "Visual1" > Verify Preview
        """        
        self.driver.find_element_by_css_selector("#sbpSwitchReport div[id^='BiComponent']").click()
        utillobj.select_or_verify_bipop_menu('Visual1')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f text.yaxis-title", 'Cost of Goods', 120, pause_time=5)
        
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step23:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step23:d(i) Verify Y-Axis Title")
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step23:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step23.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step23.c: Verify first bar color")
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step23: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step23: verify grid 1st row value')
        
        """
            Step24 : Click the switch "Reports" shortcut in the lower right corner > Select "Visual2" > Verify Preview
        """
        self.driver.find_element_by_css_selector("#sbpSwitchReport div[id^='BiComponent']").click()
        utillobj.select_or_verify_bipop_menu('Visual2')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text.xaxisOrdinal-title", 'Product Subcategory', 120, pause_time=5)
       
        xaxis_value="Product Subcategory"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step24:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", "Cost of Goods", "Step24:d(i) Verify Y-Axis Title")
        expected_xval_list=['CRT TV','Flat Panel TV','Portable TV','Smartphone','Tablet']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step24:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step24.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar", "bar_blue", "Step24.c: Verify first bar color")
       
        """
            Step25 : Click the switch "Reports" shortcut in the lower right corner > Select "Visual1" > Verify Preview
        """
        self.driver.find_element_by_css_selector("#sbpSwitchReport div[id^='BiComponent']").click()
        utillobj.select_or_verify_bipop_menu('Visual1')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f text.yaxis-title", 'Cost of Goods', 120, pause_time=5)
        
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step25:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step25:d(i) Verify Y-Axis Title")
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step26:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step25.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step25.c: Verify first bar color")
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step25: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step25: verify grid 1st row value')
        
        """
            Step 26 : Click Run > Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f text.yaxis-title", 'Cost of Goods', 120, pause_time=5)
        
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2_f", xaxis_value, "Step26:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2_f", "Cost of Goods", "Step26:d(i) Verify Y-Axis Title")
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2_f", expected_xval_list, expected_yval_list, "Step26:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2_f", 1, 12, 'Step26.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2_f", "riser!s0!g1!mbar", "bar_blue", "Step26.c: Verify first bar color")
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1_f',heading, 'Step26: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1_f',row_val,'Step26: verify grid 1st row value')
                     
        """
            Step 27 : Close
            Step 08 : Click Save in the toolbar
            Step 09 : Save as "C2158150" > Click Save
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 29 : Click "IA" > "Close"
        """
        ribbonobj.select_tool_menu_item('menu_close')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text.xaxisOrdinal-title", 'Product Subcategory', 120, pause_time=5)
        
        """
            Step 30 : Click "Save" > "C2158288_Visual2" > click Save
        """        
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+'_Visual2')
                  
        """
            Step 31 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.wf_logout()
          
        """
            Step 32 : Reopen fex using IA API:
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f text.yaxis-title", 'Cost of Goods', 180,  pause_time=5)
          
        """
            Step 33 : Verify the following is displayed.
        """
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step33:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step33:d(i) Verify Y-Axis Title")
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step33:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step33.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step33.c: Verify first bar color")
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step33: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step33: verify grid 1st row value')
        
        """
            Step 34 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        
    def select_or_verify_visualization_filter_values(self, item_list, **kwargs):
        utillobj = utillity.UtillityMethods(self.driver)
        if 'msg' in kwargs:
            kwargs['msg'] =  kwargs['msg']
        else:
            kwargs['msg'] = 'Step X:'
        for item in item_list:
            flag = 0
            checkbox_item_css="div[id$='ValuesBox']  div[id^='CheckBoxItem']"
            while flag < 200:
                elem=self.driver.find_elements_by_css_selector(checkbox_item_css)
                elem_list=[el.text.strip() for el in elem]
                if item in elem_list:
                    if 'verify' in kwargs: 
                        status=elem[elem_list.index(item)].find_element_by_css_selector("input").get_attribute("checked")
                        if status == 'true':
                            utillobj.asequal(self, status, kwargs['verify'], kwargs['msg']+" verify " + item + " is checked in filter box.")
                        else:
                            utillobj.asequal(self, status, kwargs['verify'], kwargs['msg']+" verify " + item + " is Unchecked in filter box.")
                    else:
                        val_obj=elem[elem_list.index(item)].find_element_by_css_selector("input")
                        if 'scroll_down' in kwargs:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", val_obj)
                        time.sleep(4)
                        utillobj.default_left_click(self,object_locator=val_obj,action_move=True, **kwargs)
                    flag = 200
                else:
                    for i in range(8):
                        self.driver.find_element_by_css_selector("div[id$='ValuesBox'] [class*='scroll-bar-vertical'] [class*='scroll-bar-inc-button']").click()
                    flag = flag + 8
                    time.sleep(1)
            try:
                if flag > 200:
                    raise ValueError(item + "does not exist in filter grid")
            except ValueError as err:
                print(err.args)
        
        if 'Ok_button' in kwargs:
            self.driver.find_element_by_id("avFilterOkBtn").click()
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()