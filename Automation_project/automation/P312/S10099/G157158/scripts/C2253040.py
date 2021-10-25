'''
Created on Feb 17, 2018
@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253040
Test_Case Name : 2 hierarchical dimensions in vis, drilldown on second changes first in query at design
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.lib import utillity

class C2253040_TestClass(BaseTestCase):

    def test_C2253040(self):
        
        Test_Case_ID = "C2253040"
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"  
        wait_time_in_sec=120
        visual = visualization.Visualization(self.driver)
#         vis_res_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        util_obj= utillity.UtillityMethods(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label',xyz_axis_label_length=4)
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step1:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step02: Add Cost of Goods(Vertical axis) and Product,Category(horizontal-axis).
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", 45)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 45)
        visual.double_click_on_datetree_item('Product,Subcategory', 1)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f text[class*='xaxisOrdinal']", 22, 45)
        
        """
        Step03: Verify axis label values
        Step04: Verify query pane
        Step05:Verify Accessories (Product Subcategory:Cost of Goods)
 
            Charger: $2,052,711.00
            Headphones: $51,663,564.00
            Universal Remote Controls: $36,037,623.00
         
        """
         
        no_of_riser=21
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['Product Category : Product Subcategory']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Cont...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Sys...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M']
        Media_Player_riser="riser!s0!g3!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Camcorder', 'Product Subcategory:Handheld', 'Cost of Goods:$20,576,916.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riser,Media_Player_riser_riser_tooltip, '03.1')  
          
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Cost of Goods', 1, "Step04.1: Verify Cost of Goods in Query Pane")  
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', 1, "Step04.2: Verify Product,Category in Query Pane") 
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Subcategory', 2, "Step04.3: Verify Product,Category in Query Pane")  
          
#         Accessories_Charger_riser="riser!s0!g0!mbar!"
#         Accessories_Charger_riser_tooltip=['Product Category:Accessories', 'Product Subcategory:Charger', 'Cost of Goods:$2,052,711.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
#         Accessories_Universal_Remote_riser="riser!s0!g2!mbar!"
#         Accessories_Universal_Remote_riser_tooltip=['Product Category:Accessories', 'Product Subcategory:Universal Remote Controls', 'Cost of Goods:$36,037,623.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
#         visual.verify_tooltip(Accessories_Charger_riser,Accessories_Charger_riser_tooltip,msg='Step05.1 Verify Accessories_riser tooltip')
#         visual.verify_tooltip(Accessories_Universal_Remote_riser,Accessories_Universal_Remote_riser_tooltip,msg='Step05.3 Verify Computers_riser tooltip')
        
        Accessories_Headphones_riser="riser!s0!g1!mbar!"
        Accessories_Headphones_riser_tooltip=['Product Category:Accessories', 'Product Subcategory:Headphones', 'Cost of Goods:$51,663,564.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        visual.verify_tooltip(Accessories_Headphones_riser,Accessories_Headphones_riser_tooltip,msg='Step05.2 Verify Camcorder_riser tooltip')
                       
        """
        Step06:Hover over 3rd bar from left (Accessories:Universal Remote) > Drill Down > Model
        """
        
        Accessories_Universal_Remote_riser="riser!s0!g2!mbar!"
        visual.select_tooltip(Accessories_Universal_Remote_riser,'Drill down to->Model')
        util_obj.wait_for_page_loads(10)
        
               
        """
        Step07:Verify query added to filter pane
        """
        
        visual.verify_field_in_filterbox('PRODUCT_CATEGORY and PRODUCT_SUBCATEG', 1, "Step07: Verify PRODUCT_CATEGORY and PRODUCT_SUBCATEG added to Filter pane")    
        
        """
        Step08:Verify subcategory drill down to Model
        """
        no_of_risera=4
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_risera, wait_time_in_sec) 
        x_title=['Product Category : Model']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories : Logitech 1100', 'Accessories : Logitech 900', 'Accessories : Niles Audio RCAHT2', 'Accessories : Niles Audio RCATT2']
        expected_yaxis_labels=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        Camcorder_riser="riser!s0!g0!mbar!"
        Camcorder_riser_tooltip=['Product Category:Accessories', 'Model:Logitech 1100', 'Cost of Goods:$7,783,440.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Camcorder_riser,no_of_risera,Camcorder_riser_tooltip, '08.1') 
        
        
        """
        Step09:Verify each bar riser value in preview
        """
#         Accessories_Logitech_1100_riser="riser!s0!g0!mbar!"
#         Accessories_Logitech_1100_riser_tooltip=['Product Category:Accessories', 'Model:Logitech 1100', 'Cost of Goods:$7,783,440.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
#         Accessories_NilesAudioRCAHT2_riser="riser!s0!g2!mbar!"
#         Accessories_NilesAudioRCAHT2_riser_tooltip=['Product Category:Accessories', 'Model:Niles Audio RCAHT2', 'Cost of Goods:$9,450,756.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
#         Accessories_NilesAudioRCATT21_riser="riser!s0!g2!mbar!"
#         Accessories_NilesAudioRCATT21_riser_tooltip=['Product Category:Accessories', 'Model:Niles Audio RCAHT2', 'Cost of Goods:$9,450,756.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
#         visual.verify_tooltip(Accessories_Logitech_1100_riser,Accessories_Logitech_1100_riser_tooltip,msg='Step09.1 Verify Accessories_Logitech_1100_riser tooltip')
#         visual.verify_tooltip(Accessories_NilesAudioRCAHT2_riser,Accessories_NilesAudioRCAHT2_riser_tooltip,msg='Step05.3 Verify Accessories_NilesAudioRCAHT2_riser tooltip')
#         visual.verify_tooltip(Accessories_NilesAudioRCATT21_riser,Accessories_NilesAudioRCATT21_riser_tooltip,msg='Step05.3 Verify Accessories_NilesAudioRCATT21_riser_tooltip')
        Accessories_Logitech_900_riser="riser!s0!g1!mbar!"
        Accessories_Logitech_900_riser_riser_tooltip=['Product Category:Accessories', 'Model:Logitech 900', 'Cost of Goods:$10,017,859.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
        visual.verify_tooltip(Accessories_Logitech_900_riser,Accessories_Logitech_900_riser_riser_tooltip,msg='Step09.2 Verify Accessories_Logitech_900_riser tooltip')
        
        
        """
        Step10:Click Run in the toolbar
        Step11:Verify ouput
        Step12:Close the output window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_risera, wait_time_in_sec) 
        x_title=['Product Category : Model']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories : Logitech 1100', 'Accessories : Logitech 900', 'Accessories : Niles Audio RCAHT2', 'Accessories : Niles Audio RCATT2']
        expected_yaxis_labels=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        Camcorder_riser="riser!s0!g0!mbar!"
        Camcorder_riser_tooltip=['Product Category:Accessories', 'Model:Logitech 1100', 'Cost of Goods:$7,783,440.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Camcorder_riser,no_of_risera,Camcorder_riser_tooltip, '10.1') 
#         visual.take_run_window_snapshot(Test_Case_ID, '12')
        visual.switch_to_previous_window()
        """
        Step13:Click "Save" in the toolbar > Type C2141631 > Click "Save" in the Save As dialog
        Step14:Logout of the IA API using the following URL. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()
        
        
       
        