'''
Created on Feb, 09 2018

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349081
Test_Case Name : Change name of Group field used in Filter

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2349081_TestClass(BaseTestCase):

    def test_C2349081(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349081'
        visual=Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num,color='lochmara'):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.6:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", color,  msg='Step' + step_num + '.7:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.8:'+' Verify riser tooltip')
                   
        """
        Step 01:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/ia?tool=idis&master=baseapp/WF_RETAIL&item=IBFS%3A%2FWFC%2FRepository%2FS10664
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite') 
             
        """ 
        Step02: Double click "Cost of Goods" and "Product, Category"
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", 45)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 45)
        
        """
        Step03: Lasso "Accessories, Camcorder, Computers" >
        Step04: Click "Group Product, Category Selection"
        Step05: Verify group created
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g2!mbar!']")
        visual.create_lasso(source_element, target_element)
        visual.select_lasso_tooltip('Group Product,Category Selection')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f [class*='xaxisOrdinal-labels!g0']", "AccessoriesandCamcorderandComputers")
        
        """
        Step06 : Drag and drop "PRODUCT_CATEGORY_1" into Filter pane
        Step07: Click OK
        """       
        visual.right_click_on_datetree_item('Dimensions->PRODUCT_CATEGORY_1', 1, 'Filter') 
        visual.wait_for_number_of_element("#avFilterOkBtn",1)
        visual.close_filter_dialog('ok')
        
        """
        Step08: Right-click "PRODUCT_CATEGORY_1" in the Data pane > Edit Group...
        Step09: Change name to 'TEST1' and select 'Show Other'
        Step10: Click OK
        """
        visual.wait_for_visible_text("#qbFilterBox td", "PRODUCT_CATEGORY_1")
        visual.right_click_on_datetree_item('Dimensions->PRODUCT_CATEGORY_1', 1, 'Edit Group...')
        visual.enter_field_text_group('TEST1')
        visual.create_group_options('Show Other')
        visual.exit_group_dialog('ok')
        
        """
        Step11: Verify following chart displayed
        Data pane, Filter pane and prompt updated with 'TEST1' name
        """
        expected_xaxis_labels=['Accessories and Camcorder and Computers', 'Other']
        expected_yaxis_labels=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        riser="riser!s0!g0!mbar"
        tooltip=['TEST1:Accessories and Camcorder and Computers', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['TEST1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser, 2,tooltip, '11.1')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'TEST1', 1, 'Step11.2: Verify TEST1 in querytree')
        visual.verify_field_listed_under_datatree('Dimensions',"TEST1",6,"Step11.3: Verify TEST1 in datatree")
        visual.verify_field_in_filterbox('TEST1', 1,"Step11.4: Verify TEST1 in filter box")
        visual.verify_prompt_title('TEST1')
        
        """
        Step12: Click IA > Save as "C2349080" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step13: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step14: Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349080.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f [class*='xaxisOrdinal-labels!g0']", "AccessoriesandCamcorderandComputers")
        
        """
        Step15: Click on Accessories and Camcorder and Computers riser > Ungroup Accessories and Camcor...
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class*='riser!s0!g0!mbar']")
        visual.select_chart_component(source_element)
        visual.select_lasso_tooltip('Ungroup Accessories and Camcorder...')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f [class*='xaxisOrdinal-labels!g0']", "Accessories")
        
        """
        Step16: Verify preview ,filter prompt updated
        Expected to see ungrouped both "Accessories and Camcorder and Computers" and Others group values
        """
        expected_xaxis_labels=['Accessories', 'Camcorder' ,'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        riser="riser!s0!g0!mbar"
        tooltip=['TEST1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['TEST1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser, 7,tooltip, '16.1')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'TEST1', 1, 'Step16.2: Verify TEST1 in querytree')
        visual.verify_field_listed_under_datatree('Dimensions',"TEST1",6,"Step16.3: Verify TEST1 in datatree")
        visual.verify_field_in_filterbox('TEST1', 1,"Step16.4: Verify TEST1 in filter box")
        visual.verify_prompt_title('TEST1')
        
        """
        Step17: Right click on "TEST1" in filter pane > Edit
        Step18: Verify filter dialog updated same
        """
        visual.right_click_on_field_in_filterbox('TEST1', 1, 'Edit...')
        visual.wait_for_number_of_element("#avFilterOkBtn",1)
        visual.verify_filter_field_values(['Accessories', 'Camcorder' ,'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production'],'true')
        visual.close_filter_dialog('ok')
                        
        """
        Step19 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        
        
if __name__ == '__main__':
    unittest.main()