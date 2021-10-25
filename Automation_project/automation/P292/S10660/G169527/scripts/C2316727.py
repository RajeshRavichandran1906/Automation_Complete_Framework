'''
Created on Oct 11, 2017

@author: BM13368
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, metadata

class C2316727_TestClass(BaseTestCase):


    def test_C2316727(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2316727'
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj1=metadata.MetaData(self.driver)
        
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        
        """ Step 1: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=baseapp/wf_retail
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 85)
        
        """
            Step 02 : Expand Customer > Full,Name
            Step 03 : Right click Age > Create Bins > leave defaults > OK
        """
        metadataobj.datatree_field_click('Age', 1, 0, 'Create Bins...')
        metadataobj.create_bin('AGE_BIN_1', 'OK')
        time.sleep(4)
        
        """
            Step 04 : Drag bin to Horizontal Axis
        """
        
        metaobj1.collapse_data_field_section("Customer")
        metadataobj.drag_drop_data_tree_items_to_query_tree("Dimensions->AGE_BIN_1", 1, 'Horizontal Axis', 0)
        time.sleep(2)
        
        """
            Verify Querypane field
        """
        metadataobj.verify_query_pane_field('Horizontal Axis', 'AGE_BIN_1', 1, "Step 04::01: Verify AGE_BIN_1 is added under Horizontal Axis")
        """
            Verify live preview chart
        """
        time.sleep(2)
        resultobj.verify_xaxis_title("TableChart_1", 'AGE_BIN_1', "Step 04:02 : Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1",1,9, 'Step 04:03 : Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=[]
        expected_xval_list=['0','10','20','30','40','50','60','70','80']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 01:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 01:05: Verify first bar color")
        """
            Step 05 : Change chart type to Pie
        """
        ribbonobj.select_ribbon_item('Format', 'Pie')
        time.sleep(5)
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 05:02: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue", "Step 05:03: Verify pie chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge!", "dark_green", "Step 05:03: Verify second pie chart slice color")
        expected_label_list=['AGE_BIN_1', '0', '10', '20', '30', '40', '50', '60', '70', '80']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 05:04: Verify pie chart Legends')
        """
            Step 06 : Double click Revenue 
        """
        metadataobj.datatree_field_click("Revenue", 2, 0)
        time.sleep(4)
        
        """
            Step 07 : Right click Revenue in query > More > Aggregation > Count
        """
        metadataobj.querytree_field_click('Revenue', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(2) 
        utillobj.select_or_verify_bipop_menu('Count')
        time.sleep(5)
        """
            Verification : Verify query-pane whether CNT.Revenue is added underneath Measure
        """
        metadataobj.verify_query_pane_field('Measure', 'CNT.Revenue', 1, "Step 07::00: Verify CNT.Revenue is visible underneath Measure")
        """
            Verification : Verify live preview pie chart 
        """
        parent_css="#TableChart_1 text[class^='pieLabel!g']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 07:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue", "Step 07:02: Verify pie chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge!", "dark_green", "Step 07:03: Verify second pie chart slice color")
        expected_label_list=['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 07:04: Verify pie chart Legends')
        resultobj.verify_riser_pie_labels_and_legends('TableChart_1', ['CNT Revenue'],"'Step 07:05: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        
        
        """
            Step 08 : Right click Bin in Color bucket > Delete 
        """
        metadataobj.querytree_field_click("AGE_BIN_1", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Delete')
        time.sleep(2)
        metadataobj.verify_query_pane_field_available('Measure', 'AGE_BIN_1', 'Size', 'Step 08:Verify Query field is not available under Color bucket', availability=False)
        """
            Verification : Verify the pie chart
        """
        parent_css="#TableChart_1 text[class^='pieLabel!g']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 08:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue", "Step 08:02: Verify pie chart color")
        resultobj.verify_riser_pie_labels_and_legends('TableChart_1', ['CNT Revenue'],"'Step 08:03: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        metadataobj.verify_query_pane_field('Measure', 'CNT.Revenue', 1, "Step 08::04: Verify CNT.Revenue is visible underneath Measure")
        
        """
            Step 09 : Double click Bin in data pane (cannot be done now because of IA-7034, so instead drag the bin to the color bucket)
        """
        metaobj1.collapse_data_field_section("Measures")
        time.sleep(3)
        metadataobj.datatree_field_click("Dimensions->AGE_BIN_1",2,0)
        parent_css="#TableChart_1 text[class^='pieLabel!g']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 09:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue", "Step 09:02: Verify pie chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge!", "dark_green", "Step 09:03: Verify second pie chart slice color")
        expected_label_list=['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 09:04: Verify pie chart Legends')
        resultobj.verify_riser_pie_labels_and_legends('TableChart_1', ['CNT Revenue'],"'Step 09:05: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
         
        """
            Step 10 : Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='pieLabel!g']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 10:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue", "Step 10:02: Verify pie chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mwedge!", "dark_green", "Step 10:03: Verify second pie chart slice color")
        expected_label_list=['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        resultobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step 10:04: Verify pie chart Legends')
        resultobj.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['CNT Revenue'],"'Step 10:05: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        expected_tooltip_list=['AGE_BIN_1:60', 'CNT Revenue:476974  (19.17%)']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s5!g0!mwedge!", expected_tooltip_list, "Step  10:06: Verify pie slice tooltip value")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        
        """
        Step 11: Click Save in the toolbar > Save as "C2316727" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
        Step12 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 13:Run from bip
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2316727.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_1", 'mrid', 'mrpass')
        parent_css="#jschart_HOLD_0 text[class^='pieLabel!g']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 13:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue", "Step 13:02: Verify pie chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mwedge!", "dark_green", "Step 13:03: Verify second pie chart slice color")
        expected_label_list=['AGE_BIN_1', '10', '20', '30', '40', '50', '60', '70']
        resultobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step 13:04: Verify pie chart Legends')
        resultobj.verify_riser_pie_labels_and_legends('jschart_HOLD_0', ['CNT Revenue'],"'Step 13:05: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        

if __name__ == "__main__":
    unittest.main()