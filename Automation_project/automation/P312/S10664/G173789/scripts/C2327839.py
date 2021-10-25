'''
Created on Feb 13, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327839
Test_Case Name : Rename group value name gives error if using name used earlier in session
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2327839_TestClass(BaseTestCase):

    def test_C2327839(self):
        
        Test_Case_ID = "C2327839"
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
        
        """
        Step02: Add "Cost of Goods" and "Product,Category"
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", 45)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 45)
        
        """
        Step03: Right click "Product,Category" in query > Create Group
        Step04 :Multi select "Accessories, Camcorder and Computer"> Group
        """
        visual.right_click_on_field_under_query_tree('Product,Category', 1, 'Create Group...')
        visual.wait_for_number_of_element("#dynaGrpsValuesTree td",8)
        visual.slect_group_grid_values(['Accessories', 'Camcorder','Computers'])
        visual.wait_for_number_of_element("#dynaGrpsValuesTree [class*='selected']",3)
        visual.create_group_options('Group')
        
        """
        Step05: Select group value name > Rename and type "new name" and Hit "Enter" key
        Step06: Click OK
        """
        visual.wait_for_visible_text("#dynaGrpsValuesTree td", "AccessoriesandCamcorderandComputers",180)
        visual.slect_group_grid_values(['Accessories and Camcorder and Computers'])
        visual.wait_for_number_of_element("#dynaGrpsValuesTree [class*='selected']",1)
        visual.rename_group('new name')
        visual.wait_for_number_of_element("#dynaGrpsValuesTree td>img[src*='minus']",1)
        visual.exit_group_dialog('ok')
        
        """
        Step07: Verify preview updated
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 5, 120)     
        expected_xaxis_labels=['Media Player', 'Stereo Systems', 'Televisions', 'Video Production','new name']
        expected_yaxis_labels=['0','50M','100M','150M','200M','250M','300M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,5,tooltip, '07')        
        
        """
        Step08: Right click "PRODUCT_CATEGORY_1" in query > Edit Group
        Step09: Select group value name "new name" > Rename
        Step10: Enter the text "Accessories and Camcorder "
        Step11: Hit "Enter" key
        Step12: Verify Group value name updated
        Step13: Click OK
        """
        visual.right_click_on_field_under_query_tree('PRODUCT_CATEGORY_1', 1, 'Edit Group...')
        visual.wait_for_number_of_element("#dynaGrpsValuesTree td",9)
        visual.slect_group_grid_values(['new name'])
        visual.wait_for_number_of_element("#dynaGrpsValuesTree [class*='selected']",1)
        visual.rename_group('Accessories and Camcorder')
        visual.wait_for_visible_text("#dynaGrpsValuesTree td", "AccessoriesandCamcorder",180)
        group_names=['Accessories and Camcorder', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(group_names,"Step12: Verify Group names")
        visual.exit_group_dialog('ok')
        
        """
        Step14: Verify preview updated without showing any error
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 5, 120)     
        expected_xaxis_labels=['Accessories and Camcorder','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0','50M','100M','150M','200M','250M','300M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,5,tooltip, '14')        
        
        """
        Step15: Click Run and hover on first riser
        Step16: Verify tooltip information
        Step17: Dismiss run window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 5, 120)     
        expected_xaxis_labels=['Accessories and Camcorder', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0','50M','100M','150M','200M','250M','300M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,5,tooltip, '16')
        visual.take_run_window_snapshot(Test_Case_ID, '16')
        visual.switch_to_previous_window()
         
        """
        Step18: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
