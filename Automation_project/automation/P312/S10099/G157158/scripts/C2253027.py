'''
Created on Feb 21, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2253027
TestCase Name: Drilldown is available when should not be at run time and results in COUNT
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata

class C2253027_TestClass(BaseTestCase):

    def test_C2253027(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253027'
        visual = visualization.Visualization(self.driver)
        core_metaobj = core_metadata.CoreMetaData(self.driver)
        position=1
        
        def verify_bar_chart(x_label, y_label, max_num, legend_list, riser_css, stepno, tooltip_list=None):
            visual.verify_rows_label(x_label, msg='Step '+stepno+'.1'+' Verify x_axis title')
            visual.verify_column_label(y_label, msg='Step '+stepno+'.2'+' Verify y_axis title')
            visual.verify_number_of_circles('#MAINTABLE_wbody1_f', position, max_num, msg='Step '+stepno+'.3'+' Verify number of circles')
            visual.verify_legends(legend_list, '#MAINTABLE_wbody1_f', msg='Step '+stepno+'.4'+' Verify number of circles')
            if tooltip_list!=None:
                visual.verify_tooltip(riser_css, tooltip_list, move_to_tooltip=True,msg='Step '+stepno+'.5'+' Verify tooltip')
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
        
        """
        Step 02 : Change > Matrix Marker
        """
        visual.change_chart_type('matrix_marker')
         
        """
        Step 03 : Double click Gross Profit (adds to Size).
        """
        visual.double_click_on_datetree_item('Gross Profit', position)
        element_css="#MAINTABLE_wbody1_f svg circle[class^='riser!']"
        visual.wait_for_number_of_element(element_css, expected_number=position)
         
        """
        Step 04 : Drag Product,Category to Rows.
        """
        visual.drag_field_from_data_tree_to_query_pane('Product,Category', position, 'Rows', position)
        element_css="#MAINTABLE_wbody1_f svg circle[class^='riser!']"
        visual.wait_for_number_of_element(element_css, expected_number=7)
         
        """
        Step 05 : Drag Store,Business,Region to Columns.
        """
        visual.drag_field_from_data_tree_to_query_pane('Store,Business,Region', position, 'Columns', position)
        element_css="#MAINTABLE_wbody1_f svg circle[class^='riser!']"
        visual.wait_for_number_of_element(element_css, expected_number=28)
         
        """
        Step 06 : Drag Quantity,Sold to Color bucket.
        """
        visual.drag_field_from_data_tree_to_query_pane('Quantity,Sold', position, 'Color', position)
        element_css="#MAINTABLE_wbody1_f rect[class='legendColorScale']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
         
        """
        Step 07 : Verify query pane
        """
        visual.verify_field_listed_under_querytree('Size', 'Gross Profit', position, msg='Step 7.1')
        visual.verify_field_listed_under_querytree('Rows', 'Product,Category', position, msg='Step 7.2')
        visual.verify_field_listed_under_querytree('Columns', 'Store,Business,Region', position, msg='Step 7.3')
        visual.verify_field_listed_under_querytree('Color', 'Quantity,Sold', position, msg='Step 7.4')
        
        """
        Step 08 : Hover on EMEA:Computers and verify tooltip
        """
        x_label=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_label=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America', 'Quantity Sold', '0K', '159.2K', '318.4K', '477.5K', '636.6K']
        legend_list=['Quantity Sold', '0K', '159.2K', '318.4K', '477.5K', '636.6K', 'Gross Profit', '49.2M', '24.6M', '0M']
        riser_css=['riser!s0!g0!mmarker!r2!c0!', 'riser!s0!g0!mmarker!r4!c1!', 'riser!s0!g0!mmarker!r0!c2!', 'riser!s0!g0!mmarker!r6!c3!']
        tooltip=['Product Category:Computers', 'Store Business Region:EMEA', 'Gross Profit:$12,147,362.23', 'Quantity Sold:129,078', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        verify_bar_chart(x_label, y_label, 30, legend_list, riser_css[0], '8', tooltip_list=tooltip)
        
        """
        Step 09 : Hover on NorthAmerica:StereoSystems and verify tooltip
        """
        tooltip=['Product Category:Stereo Systems', 'Store Business Region:North America', 'Gross Profit:$49,228,757.29', 'Quantity Sold:636,612', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        verify_bar_chart(x_label, y_label, 30, legend_list, riser_css[1], '9', tooltip_list=tooltip)
        
        """
        Step 10 : Hover on Oceania:Accessories and verify tooltip
        """
        tooltip=['Product Category:Accessories', 'Store Business Region:Oceania', 'Gross Profit:$48,343.30', 'Quantity Sold:592', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        verify_bar_chart(x_label, y_label, 30, legend_list, riser_css[2], '10', tooltip_list=tooltip)
        
        """
        Step 11 : Hover on SouthAmerica:VideoProduction and verify tooltip
        """
        tooltip=['Product Category:Video Production', 'Store Business Region:South America', 'Gross Profit:$460,856.91', 'Quantity Sold:5,228', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        verify_bar_chart(x_label, y_label, 30, legend_list, riser_css[3], '11', tooltip_list=tooltip)
        
        """
        Step 12 : Drag Store,Type to filter, set to no prompt and equal store front
        """
        core_metaobj.collapse_data_field_section('Filters and Variables')
        visual.drag_and_drop_from_data_tree_to_filter('Store Type', position)
        visual.wait_for_number_of_element("#avFilterOkBtn", expected_number=1)
        
        """
        Step 13 : Verify filter dialog (show prompt - unchecked and storefront- checked)
        Step 14 : Click ok in filter dialog
        """
        visual.deselect_filter_show_prompt_checkbox('alpha',['[All]','Store Front'])
        item_list=['[All]','Store Front']
        visual.select_filter_field_values(item_list, Ok_button=True)
        element_css="#MAINTABLE_wbody1_f svg circle[class^='riser!']"
        visual.wait_for_number_of_element(element_css, expected_number=28)
        
        """
        Step 15 : Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('Store Type', position, msg='Step 15.1')
        
        """
        Step 16 : Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        element_css="#MAINTABLE_wbody1_f svg circle[class^='riser!']"
        visual.wait_for_number_of_element(element_css, expected_number=28)
        
        """
        Step 17 : Hover over the greenest spot (Stereo System, EMEA) > Drilldown > Product Subcategory.
        """
        visual.select_tooltip('riser!s0!g0!mmarker!r4!c0!', 'Drill down to->Product Subcategory')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g circle[class^='riser!']", expected_number=5)
        
        """
        Step 18 : Verify product category changed to product subcategory in row title
        """
        x_label=['Product Subcategory', 'Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        y_label=['Store Business Region', 'EMEA', 'Quantity Sold', '6.2K', '44.5K', '82.7K', '120.9K', '159K']
        legend_list=['Quantity Sold', '6.2K', '44.5K', '82.7K', '120.9K', '159K', 'Gross Profit', '11.1M', '5.8M', '0.4M']
        riser_css='riser!s0!g0!mmarker!r2!c0!'
        tooltip=['Product Subcategory:Receivers', 'Store Business Region:EMEA', 'Gross Profit:$6,625,788.09', 'Quantity Sold:60,204', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Category', 'Drill down to']
        verify_bar_chart(x_label, y_label, 30, legend_list, riser_css, '18', tooltip_list=tooltip)
        
        """
        Step 19 : Hover over greenest spot (Home Theater System, EMEA) > Drilldown > Model.
        """
        visual.select_tooltip('riser!s0!g0!mmarker!r1!c0!', 'Drill down to->Model')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g circle[class^='riser!']", expected_number=8)
         
        """
        Step 20 : Verify product subcategory changed to Model in row title
        Step 21 : Hover over greenest spot (Samsung HT-Z120, EMEA)
        Step 22 : Verify model display 'Drillup' in the tooltip 
        """       
        x_label=['Model', 'LG MDD72', 'LG XD63', 'Panasonic', 'Panasonic SC-PT160', 'Pioneer HTZ-170', 'Samsung HT-Z120', 'Sharp HT-CN550', 'Sony DAV-DZ30']
        y_label=['Store Business Region', 'EMEA', 'Quantity Sold', '19,413', '19,676.3', '19,939.5', '20,202.8', '20,466']
        legend_list=['Quantity Sold', '19,413', '19,676.3', '19,939.5', '20,202.8', '20,466', 'Gross Profit', '1,753.2K', '1,329.3K', '905.4K']
        riser_css='riser!s0!g0!mmarker!r5!c0!'
        tooltip=['Model:Samsung HT-Z120', 'Store Business Region:EMEA', 'Gross Profit:$1,376,888.70', 'Quantity Sold:20,466', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory', 'Drill down to Store Business Sub Region']
        verify_bar_chart(x_label, y_label, 30, legend_list, riser_css, '20', tooltip_list=tooltip)
        
        """
        Step 23 : Click drillup
        """
        visual.select_tooltip('riser!s0!g0!mmarker!r5!c0!', 'Drill up to Product Subcategory')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g circle[class^='riser!']", expected_number=5)
        
        """
        Step 24 : Verify output 
        """
        x_label=['Product Subcategory', 'Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        y_label=['Store Business Region', 'EMEA', 'Quantity Sold', '6.2K', '44.5K', '82.7K', '120.9K', '159K']
        legend_list=['Quantity Sold', '6.2K', '44.5K', '82.7K', '120.9K', '159K', 'Gross Profit', '11.1M', '5.8M', '0.4M']
        riser_css='riser!s0!g0!mmarker!r2!c0!'
        verify_bar_chart(x_label, y_label, 30, legend_list, riser_css, '24')
        
        visual.switch_to_previous_window()
        element_css="#MAINTABLE_wbody1_f svg circle[class^='riser!']"
        visual.wait_for_number_of_element(element_css, expected_number=28)
        
        """
        Step 25 : Click "Save" in the toolbar > Type C2141381 > Click "Save" in the Save As dialog
                    Save the fex with the same name as this test case
        """
        
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        
if __name__ == '__main__':
    unittest.main() 