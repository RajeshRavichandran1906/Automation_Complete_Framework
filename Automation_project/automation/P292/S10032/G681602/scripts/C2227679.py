'''
Created on Apr 7, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227679
Test case Name =  Change Filter Sort order from the Filter dialog
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.lib import core_utility


class C2227679_TestClass(BaseTestCase):

    def test_C2227679(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227679'
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        data_list = ["Gross Profit","Product,Subcategory"] 
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(elem1, 1, resultobj.chart_long_timesleep)
    
        """
        Step 02: Double-click "Gross Profit", located under Sales Measures
        Step 03: Double-click "Product,Subcategory", located under Product Dimension
        """
        for item in data_list:
            metaobj.datatree_field_click(item,2,1)
            utillobj.synchronize_with_visble_text("#queryTreeColumn", item, metaobj.chart_medium_timesleep)
            
        """
        Step04: Drag and drop "Product,Subcategory" to the Filter pane
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Subcategory", 1)
        
        """
        Step05: Select Sort "Descending"
        Step06: Verify Filter dialog
        Step07: Click OK
        """ 
        utillobj.synchronize_with_number_of_element('#avFilterOkBtn', 1, resultobj.chart_medium_timesleep)
        elem = utillobj.validate_and_get_webdriver_object("#avfSortValuesComboBox", 'combo-box')
        combo=['Ascending','Descending']
        utillobj.select_any_combobox_item(elem,'Descending',verify=True,expected_combobox_list=combo, msg="Step05: Verify list of Sort functions")
        item_list=['[All]']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', msg = 'step06.a: Verify dialog')
        elem = utillobj.validate_and_get_webdriver_object("#avfSortValuesComboBox div", 'sort-combo-box')
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Descending',"Step06.b: Verify Sort in Filter dialog")
        expected_value_list=['[All]', 'iPod Docking Station', 'Video Editing', 'Universal Remote Controls']
        metaobj.verify_filter_dialog_item_list(expected_value_list, "Step06.c:")
        metaobj.create_visualization_filters('alpha')
        
        """
        Step08: Verify Filter Prompt Sort order
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        menu_list_items=['[All]', 'iPod Docking Station', 'Video Editing', 'Universal Remote Controls', 'Tablet', 'Streaming', 'Standard', 'Speaker Kits', 'Smartphone', 'Receivers', 'Professional', 'Portable TV', 'Home Theater Systems', 'Headphones', 'Handheld', 'Flat Panel TV', 'DVD Players - Portable', 'DVD Players', 'Charger', 'CRT TV', 'Boom Box', 'Blu Ray']
        utillobj.synchronize_with_number_of_element("div[id*='Prompt_1'] table[style*=hidden] tr", 22, resultobj.chart_medium_timesleep)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', menu_list=menu_list_items, msg="Step08.a: Verify prompt menu list")
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step08.b: Verify [All] is checked in filter prompt")
        
        """
        Step09: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_util_obj.switch_to_new_window()
        
        """
        Step 10: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7) 
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step10.e: Verify [All] is checked in filter prompt")
        
        """
        Step 11: Close output window
        """
        core_util_obj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, resultobj.chart_medium_timesleep)
        
        """
        Step12: Click Save in the toolbar
        Step13: Save as "C2158165" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
             
        """
        Step15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
             
        """
        Step 16: Verify Canvas
        """
        utillobj.synchronize_with_number_of_element('#MAINTABLE_wbody1', 1, resultobj.chart_long_timesleep)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.verify_filter_pane_field('Product,Subcategory',1,"Step16:")
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 1.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        bar=['Product Subcategory:Blu Ray', 'Gross Profit:$51,771,195.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16.d: Verify bar value")
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step16.e: Verify [All] is checked in filter prompt")
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()