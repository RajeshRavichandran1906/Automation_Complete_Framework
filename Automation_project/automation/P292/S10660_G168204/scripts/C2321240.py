'''
Created on Oct 25, 2017

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2321240
Test_Case_Name : New Bucketized TagCloud Chart

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon, ia_resultarea

class C2321240_TestClass(BaseTestCase):


    def test_C2321240(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2321240'
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        runtime_chart_css="jschart_HOLD_0"
        preview_chart_css="TableChart_1"
        preview_default_tagcloud_chart_css="#TableChart_1 text[class*='riser']"
        runtime_default_tagcloud_chart_css="#jschart_HOLD_0 text[class*='riser']"
        
        """
            Step 01 : Invoke IA Chart tool with wf_retail
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10660_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02: Format > Chart Type > Other > HTML5 > TagCloud Chart
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'html5_tagCloud', 4, ok_btn_click=True)
        
        """
            Verification : Step 02:00: Expect to see the following TagCloud Chart Preview.
        """
        utillobj.synchronize_with_number_of_element(preview_default_tagcloud_chart_css,5, 50)
        expected_text_list=['Group 4', 'Group 3', 'Group 2', 'Group 1', 'Group 0']
        ia_resultarea_obj.verify_tagcloud_chart_text("#"+preview_chart_css, expected_text_list, "Step 02:01: Verify the tag cloud text")
        expected_text_color_dict={'Group 0':'persian_red','Group 1':'rajah_sandal','Group 2':'Cumulus1','Group 3':'pale_green1','Group 4':'elf_green'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#"+preview_chart_css, expected_text_color_dict, "Step 02:02: Verify tag cloud chart text colors")
        
        """
            Step 03: Add Car to the Horizontal axis bucket.
            Add Dealer_Cost and to the Vertical axis bucket.
        """
        metadataobj.datatree_field_click("CAR",1,1,'Add To Query','Detail')
        utillobj.synchronize_with_number_of_element(preview_default_tagcloud_chart_css, 10, 55)
        
        metadataobj.datatree_field_click("DEALER_COST",1,1,'Add To Query','Size')
        utillobj.synchronize_with_visble_text("#queryTreeColumn tr:nth-child(6)", "DEALER_COST", 40)
        
        """
            Expect to see the following TagCloud Chart Preview.
        """
        expected_text_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOYOTA', 'DATSUN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#"+preview_chart_css, expected_text_list, "Step 03:01: Verify the tag cloud text")
        expected_text_color_dict={'ALFA ROMEO':'bar_blue','AUDI':'bar_blue','BMW':'bar_blue','DATSUN':'bar_blue','JAGUAR':'bar_blue','JENSEN':'bar_blue','MASERATI':'bar_blue','PEUGEOT':'bar_blue','TOYOTA':'bar_blue','TRIUMPH':'bar_blue'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#"+preview_chart_css, expected_text_color_dict, "Step 03:02: Verify tag cloud chart text colors")
        
        """
            Step 04: Click the Run button.
            Hover over the 'O' in Alfa Romeo.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 60)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element(runtime_default_tagcloud_chart_css, 10, 55)
        expected_text_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOYOTA', 'DATSUN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#"+runtime_chart_css, expected_text_list, "Step 04:01: Verify the tag cloud text")
        expected_text_color_dict={'ALFA ROMEO':'bar_blue','AUDI':'bar_blue','BMW':'bar_blue','DATSUN':'bar_blue','JAGUAR':'bar_blue','JENSEN':'bar_blue','MASERATI':'bar_blue','PEUGEOT':'bar_blue','TOYOTA':'bar_blue','TRIUMPH':'bar_blue'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#"+runtime_chart_css, expected_text_color_dict, "Step 04:02: Verify tag cloud chart text colors")
        
        """
            Expect to see the following HTML5 TagCloud Chart, including Tool tip information.
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235']
        resultobj.verify_default_tooltip_values(runtime_chart_css, "riser!s0!g0!mtag!", expected_tooltip_list, "Step 4:03: Verify Alfa Romeo tooltip information")
        utillobj.switch_to_default_content(pause=1)
        
        """
            Step 05: Add Retail_Cost to the Color By bucket.
            Click the Run button.
        """
        metadataobj.datatree_field_click("RETAIL_COST",1,1,'Add To Query','Color')
        utillobj.synchronize_with_visble_text("#queryTreeColumn tr:nth-child(8)", "RETAIL_COST", 35)
        
        metadataobj.verify_query_pane_field('Color', 'RETAIL_COST', 1, "Step 05::01: Verify Query Pane that CAR added under Color Bucket")
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 60)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element(runtime_default_tagcloud_chart_css, 10, 55)
        
        """
            Expect to see the following TagCloud Chart, now with the chart reflecting colors using the Color By bucket.
            Also expect to see the Tool tip information for Retail_Cost.
        """
        expected_text_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOYOTA', 'DATSUN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#"+runtime_chart_css, expected_text_list, "Step 05:02: Verify the tag cloud text")
        expected_text_color_dict={'ALFA ROMEO':'macaroni_and_cheese','AUDI':'cinnabar2','BMW':'elf_green','DATSUN':'persian_red','JAGUAR':'rajah_sandal2','JENSEN':'rajah_sandal1','MASERATI':'cumulus1','PEUGEOT':'cinnabar','TOYOTA':'persian_red2','TRIUMPH':'cinnabar1'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#"+runtime_chart_css, expected_text_color_dict, "Step 05:03: Verify tag cloud chart text colors")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'RETAIL_COST:19,565']
        resultobj.verify_default_tooltip_values(runtime_chart_css, "riser!s0!g0!mtag!", expected_tooltip_list, "Step 05:04: Verify tooltip information contains Retail_Cost")
        
        """
            Step 06: Add Country to the Tool Tip bucket.
            Click the Run button.
            Hover over the lower area for Jaguar.
        """
        utillobj.switch_to_default_content(pause=1)
        
        metadataobj.datatree_field_click("COUNTRY",1,1,'Add To Query','Tooltip')
        utillobj.synchronize_with_visble_text("#queryTreeColumn tr:nth-child(10)", "FST.COUNTRY", 35)
        
        metadataobj.verify_query_pane_field('Tooltip', 'FST.COUNTRY', 1, "Step 06::01: Verify Query Pane that COUNTRY added under Tooltip Bucket")
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 60)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element(runtime_default_tagcloud_chart_css, 10, 55)
        
        expected_text_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOYOTA', 'DATSUN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#"+runtime_chart_css, expected_text_list, "Step 06:02: Verify the tag cloud text")
        expected_text_color_dict={'ALFA ROMEO':'macaroni_and_cheese','AUDI':'cinnabar2','BMW':'elf_green','DATSUN':'persian_red','JAGUAR':'rajah_sandal2','JENSEN':'rajah_sandal1','MASERATI':'cumulus1','PEUGEOT':'cinnabar','TOYOTA':'persian_red2','TRIUMPH':'cinnabar1'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#"+runtime_chart_css, expected_text_color_dict, "Step 06:03: Verify tag cloud chart text colors")
        
        """
            Expect to see the following TagCloud Chart, now with additional Tool tip information for Country.
        """
        expected_tooltip_list=['CAR:JAGUAR', 'DEALER_COST:18,621', 'RETAIL_COST:22,369', 'COUNTRY:ENGLAND']
        resultobj.verify_default_tooltip_values(runtime_chart_css, "riser!s0!g4!mtag!", expected_tooltip_list, "Step 06:04: Hover lower area for JAGUAR and verify tooltip information")
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 07: Save with name C2321240 and close.
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
            Step 08: Restore using IA API:
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%C2321240.fex
            Expect to see the regenerated TagCloud Chart.
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element(preview_default_tagcloud_chart_css, 10, 55)
        
        expected_text_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOYOTA', 'DATSUN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#"+preview_chart_css, expected_text_list, "Step 08:01: Verify the tag cloud text")
        expected_text_color_dict={'ALFA ROMEO':'macaroni_and_cheese','AUDI':'cinnabar2','BMW':'elf_green','DATSUN':'persian_red','JAGUAR':'rajah_sandal2','JENSEN':'rajah_sandal1','MASERATI':'cumulus1','PEUGEOT':'cinnabar','TOYOTA':'persian_red2','TRIUMPH':'cinnabar1'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#"+preview_chart_css, expected_text_color_dict, "Step 08:02: Verify tag cloud chart text colors")


if __name__ == "__main__":
    unittest.main()