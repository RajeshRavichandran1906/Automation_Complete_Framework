'''
Created on Oct 11, 2017

@author: BM13368
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea
from selenium.webdriver.common.by import By

class C2316727_TestClass(BaseTestCase):


    def test_C2316727(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2316727'
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        
        """ Step 1: Invoke IA Chart tool with wf_retail
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_1', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        """
            Step 02 : Expand Customer > Full,Name
            Step 03 : Right click Age > Create Bins > leave defaults > OK
        """
        metadataobj.datatree_field_click('Age', 1, 0, 'Create Bins...')
        metadataobj.create_bin('AGE_BIN_1', 'OK')
        """
            Step 04 : Drag bin to Horizontal Axis
        """
        metadataobj.datatree_field_click("AGE_BIN_1",1,0,'Add To Query','Horizontal Axis')
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
        time.sleep(2)
        
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
        time.sleep(2)
        """
            Verification : Verify query-pane whether CNT.Revenue is added underneath Measure
        """
        metadataobj.verify_query_pane_field('Measure', 'CNT.Revenue', 1, "Step 07::00: Verify CNT.Revenue is visible underneath Measure")
        """
            Verification : Verify live preview pie chart 
        """
        parent_css="#TableChart_1 text[class^='pieLabel!g']"
        resultobj.wait_for_property(parent_css, 1)
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
        resultobj.wait_for_property(parent_css, 1)
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 08:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue", "Step 08:02: Verify pie chart color")
        resultobj.verify_riser_pie_labels_and_legends('TableChart_1', ['CNT Revenue'],"'Step 08:03: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        metadataobj.verify_query_pane_field('Measure', 'CNT.Revenue', 1, "Step 08::04: Verify CNT.Revenue is visible underneath Measure")
        
        """
            Step 09 : Double click Bin in data pane (cannot be done now because of IA-7034, so instead drag the bin to the color bucket)
        """
        metadataobj.datatree_field_click("AGE_BIN_1",2,0)
        parent_css="#TableChart_1 text[class^='pieLabel!g']"
        resultobj.wait_for_property(parent_css, 1)
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
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='pieLabel!g']"
        resultobj.wait_for_property(parent_css, 1)
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
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)     
        utillobj.infoassist_api_logout()
        time.sleep(3)

      

if __name__ == "__main__":
    unittest.main()