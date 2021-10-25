'''
Created on May 28, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2204946
TestCase_Name : Verify Active chart engine is set to JSCHART
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon, active_miscelaneous, wf_mainpage

class C2318047_TestClass(BaseTestCase):

    def test_C2318047(self):
        
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        miscelaneousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        wfmain_page_obj=wf_mainpage.Wf_Mainpage(self.driver)
        
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        fex_name="Chart_Engine"
        
        """
            Step 01:Sign in to WebFOCUS
            http://machine:port/{alias}
            Step 02:Execute the following URL:
            http://machine:port/{alias}/ia?tool=chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FS10670
            Change the Output type to Active Report.
        """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
          
        ribbonobj.switch_ia_tab("Home")
        ia_ribbonobj.select_or_verify_output_type(launch_point='Home', item_select_path='Active Report')  
               
        """ 
            Step 03:Add Category and Product fields to Horizontal Axis 
            and add Unit Sales field to Vertical Axis
        """
        metadataobj.datatree_field_click("Category",2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title']", "Category", 15)
          
        metadataobj.datatree_field_click("Product",2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", "Category : Product", 15) 
          
        metadataobj.datatree_field_click("Unit Sales",2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", "Unit Sales", 15)
          
        resultobj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 3:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'Category : Product', "Step 3:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 3:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 3:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 3:05: Verify first bar color")
              
        """ 
            Step 04:Run the chart
            Verify the chart is displayed properly
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 4:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", 'Category : Product', "Step 4:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 4:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, 'Step 4:04: X and Y axis labels')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 4:05: Verify first bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 4:06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 4:07: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 4:08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 4:09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=1)
             
        """ 
            Step 05:Save the chart as Chart_Engine.fex
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(2)
        utillobj.ibfs_save_as(fex_name)
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(3)
             
        """ 
            Step 06:Now edit the saved fex from Text editor
            Verify from the source code whether below
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        time.sleep(10)
        wfmain_page_obj.select_repository_folder_item_context_menu('Chart_Engine', 'Edit with text editor', folder_path='P116->S7074')
        utillobj.switch_to_window(1, pause=1)
        utillobj.synchronize_with_number_of_element("#bipEditor #toolbar_button_new", 1, 60)
        text_elem=self.driver.find_element_by_css_selector("#bipEditorArea").get_attribute("value").strip('\n')
        expected_value="ARGRAPHENGINE=JSCHART"
        utillobj.asin(expected_value, text_elem, "Step 06:Verify from the source code whether which has ARGRAPHENGINE=JSCHART in editor")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()