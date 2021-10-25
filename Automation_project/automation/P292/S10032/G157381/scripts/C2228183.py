'''
Created on 28-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228183
TestCase Name = Verify AlphaNumeric Axes in Matrix Chart
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon

class C2228183_TestClass(BaseTestCase):

    def test_C2228183(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2228183"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        def verify_chart(total_circle, xlabel, ylabel, step_num, expected_legend_list, tooltip=None, parent_id='jschart_HOLD_0'):
            x_title_obj = driver.find_elements_by_css_selector("#"+parent_id+" text[class^='xaxis'][class$='title']")
            x_title_text = [elem.text.strip() for elem in x_title_obj]
            utillobj.as_List_equal(['Brand', 'Sale Year/Quarter'], x_title_text, "Step "+step_num+".1: Verify X-Axis Title.")
            resultobj.verify_number_of_circle(parent_id, 1, int(total_circle), "Step "+step_num+".2: Verify chat with expected circle.")
            msg = "Step "+step_num+".3: Verify X-Axis title."
            resultobj.verify_riser_chart_XY_labels(parent_id, xlabel, ylabel, msg, x_custom_css="svg > g text[class^='xaxisOrdinal']", y_custom_css="svg > g text[class^='yaxisOrdinal']")
            resultobj.verify_riser_legends(parent_id, expected_legend_list, "Step "+step_num+".4: Verify chart lagend.")
            time.sleep(0.5)
            if tooltip != None:
                resultobj.verify_default_tooltip_values(parent_id, 'riser!s0!g112!mmarker!', tooltip, "Step "+step_num+".5: Verify chat tooltip.")
            
            
        """ Step 1: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 [class^='riser']",26,65)
         
        """ Step 2: Select Format > Scatter Chart.
        """
        vis_ribbonobj.select_ribbon_item('Format', 'Scatter')
        utillobj.synchronize_with_number_of_element("#TableChart_1 path",27,15)
         
        """ Step 3: Drag Brand (Model Attributes) to Vertical Axis.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Brand', 1, 'Vertical Axis', 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title']", 'Brand', 25) 
         
        """ Step 4: Verify Brand is added to vertical Axis.
        """
        metaobj.verify_query_pane_field('Vertical Axis', 'Brand', 1, "Step 4")
        resultobj.verify_xaxis_title('TableChart_1', 'Brand', "Step 4.1: Verify Brand is added to vertical Axis.")
        resultobj.verify_number_of_circle('TableChart_1', 1, 31, "Step 4.2: Verify Brand is added to vertical Axis with expected circle.")
        expected_yval_list = ['Audio Technica', 'Audiovox', 'BOSE', 'Canon', 'Denon', 'GPX', 'Grado', 'Harman Kardon', 'JVC', 'LG', 'Logitech', 'Magnavox', 'Niles Audio', 'Onkyo', 'Panasonic', 'Philips', 'Pioneer', 'Polaroid', 'Polk Audio', 'Roku', 'Samsung', 'Sanyo', 'Sennheiser', 'Sharp', 'Sony', 'SuperSonic', 'Thomson Grass Valley', 'Tivax', 'Toshiba', 'Yamaha']
        msg = "Step 4.3: Verify Y-Axis title."
        resultobj.verify_riser_chart_XY_labels('TableChart_1', [], expected_yval_list, msg, y_custom_css="svg > g text[class^='yaxisOrdinal']")
        time.sleep(0.5)
         
        """ Step 5: Drag Brand from Vertical Axis to Horizontal Axis.
        """
        elem = driver.find_element_by_css_selector("#queryTreeColumn table tr:nth-child(7) img[src*='16.png']")
        utillobj.click_on_screen(elem, 'middle', click_type=2)
        time.sleep(2)
        metaobj.drag_and_drop_query_items('Brand', 'Horizontal Axis')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table tr:nth-child(8)", 'Brand', 25)
         
        """ Step 6: Verify Brand displays as Brand under Horizontal Axis.
        """
        metaobj.verify_query_pane_field('Horizontal Axis', 'Brand', 1, "Step 5:")
        resultobj.verify_xaxis_title('TableChart_1', 'Brand', "Step 5.1: Verify Brand is added to vertical Axis.")
        resultobj.verify_number_of_circle('TableChart_1', 1, 31, "Step 5.2: Verify Brand is added to vertical Axis with expected circle.")
        expected_xval_list = ['Audio Technica', 'Audiovox', 'BOSE', 'Canon', 'Denon', 'GPX', 'Grado', 'Harman Kardon', 'JVC', 'LG', 'Logitech', 'Magnavox', 'Niles Audio', 'Onkyo', 'Panasonic', 'Philips', 'Pioneer', 'Polaroid', 'Polk Audio', 'Roku', 'Samsung', 'Sanyo', 'Sennheiser', 'Sharp', 'Sony', 'SuperSonic', 'Thomson Grass Valley', 'Tivax', 'Toshiba', 'Yamaha']
        msg = "Step 5.3: Verify X-Axis title."
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, [], msg, x_axis_label_length=2, y_custom_css="svg > g text[class^='xaxisOrdinal']")
         
        """ Step 7: Drag Sale,Year/Quarter to Vertical Axis.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Year/Quarter', 1, 'Vertical Axis', 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title']",'Brand',25)
         
        """ Step 8: Drag Model to Detail.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Model', 1, 'Detail', 0)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table tr:nth-child(13)",'Model',25)
         
        """ Step 9: Drag Product,Category to Color BY.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Color', 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='legend-title']",'Product Category',25)
         
        """ Step 10: Drag Gross Profit to Size.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit', 1, 'Size', 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='sizeLegend-title']",'Gross Profit',25)
         
        """ Step 11: Verify the following chart displays in preview.
        """
        xlabel = ['Audio Technica', 'Canon', 'Denon', 'Grado', 'JVC', 'Logitech', 'Niles Audio', 'Panasonic', 'Pioneer', 'Samsung', 'Sanyo', 'Sennheiser', 'Sony', 'Brand', 'Sale Year/Quarter']
        ylabel = ['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        verify_chart(505, xlabel, ylabel, '11', ['Product Category', 'Accessories', 'Camcorder', 'Gross Profit', '577.8K', '291K', '4.3K'], parent_id='TableChart_1')
         
        """ Step 12: Run.
        """
        vis_ribbonobj.select_top_toolbar_item('toolbar_run')
         
        """ Step 13: Verify the following chart displays.
        """
        utillobj.switch_to_frame(pause=2)
        xlabel=['Audio Technica', 'AudioVox', 'Audiovox', 'BOSE', 'Canon', 'Denon', 'GPX', 'Grado', 'Harman Kardon', 'JVC', 'LG', 'Logitech', 'Magnavox', 'Niles Audio', 'Onkyo', 'Panasonic', 'Philips', 'Pioneer', 'Polaroid', 'Polk Audio', 'Roku', 'Samsung', 'Sanyo', 'Sennheiser', 'Sharp', 'Sony', 'SuperSonic', 'Thomson Grass Valley', 'Tivax', 'Toshiba', 'Yamaha', 'Brand', 'Sale Year/Quarter']
        ylabel=['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '722.3K', '361.2K', '0K']
        actual_tooltip=['Brand:Audio Technica', 'Sale Year/Quarter:2013 Q1', 'Gross Profit:$54,401.91', 'Product Category:Accessories', 'Model:Audio Technica ATHW5000']
        verify_chart(2580, xlabel, ylabel, '13', expected_legend_list, tooltip=actual_tooltip)
        utillobj.switch_to_default_content(pause=2)
         
        """ Step 14: Click Save in the toolbar > Save as "C2228183" > Click Save
        """
        vis_ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ Step 15: Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#jschart_HOLD_0 [class='xaxisOrdinal-title']",2,25)
        
        """ Step 16: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228183.fex
            Step 17:Verify the following chart displays.
        """
        xlabel=['Audio Technica', 'AudioVox', 'Audiovox', 'BOSE', 'Canon', 'Denon', 'GPX', 'Grado', 'Harman Kardon', 'JVC', 'LG', 'Logitech', 'Magnavox', 'Niles Audio', 'Onkyo', 'Panasonic', 'Philips', 'Pioneer', 'Polaroid', 'Polk Audio', 'Roku', 'Samsung', 'Sanyo', 'Sennheiser', 'Sharp', 'Sony', 'SuperSonic', 'Thomson Grass Valley', 'Tivax', 'Toshiba', 'Yamaha', 'Brand', 'Sale Year/Quarter']
        ylabel=['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '722.3K', '361.2K', '0K']
        actual_tooltip=['Brand:Audio Technica', 'Sale Year/Quarter:2013 Q1', 'Gross Profit:$54,401.91', 'Product Category:Accessories', 'Model:Audio Technica ATHW5000']
        verify_chart(2580, xlabel, ylabel, '16', expected_legend_list)
        elem = driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(elem, Test_Case_ID+"_Actual_Step_16")
        time.sleep(3)
        
        """
        Step 18 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
        
if __name__ == '__main__':
    unittest.main()