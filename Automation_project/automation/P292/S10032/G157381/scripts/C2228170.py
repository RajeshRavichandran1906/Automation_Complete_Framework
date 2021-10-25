'''
Created on Dec 26, 2017

@author: BM13368
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2228170
TestCase Name : Verify simple Tagcloud chart (82xx)
TestSuite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2228170_TestClass(BaseTestCase):

    def test_C2228170(self):
        
        Test_Case_ID = "C2228170"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02:Select "Format" > "Chart Types" > "Other".
            Step 03:Verify the following window is displayed.
            Step 04:Select "HTML5" option.
            Step 05:Select "Tag Cloud" chart type.
            Step 06:Click "OK".
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbon_obj.select_other_chart_type('html5', 'html5_tagCloud', 4, ok_btn_click=True)
        """ 
           Step 07:Verify the following chart is displayed. 
        """
        parent_css="#TableChart_1 text[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 30)
        
        expected_text_list=['Group 4', 'Group 3', 'Group 2', 'Group 1', 'Group 0']
        ia_resultarea_obj.verify_tagcloud_chart_text("#TableChart_1", expected_text_list, "Step 03:01: Verify the tag cloud text")
        expected_text_color_dict={'Group 0':'persian_red','Group 1':'rajah_sandal','Group 2':'Cumulus1','Group 3':'pale_green1','Group 4':'elf_green'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#TableChart_1", expected_text_color_dict, "Step 03:02: Verify tag cloud chart text colors")
        
        """ 
            Step 08:Double click "LAST_NAME","CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
           
        """ 
            Step 09:Verify the following chart is displayed.
            Note: The position of labels is not important, and will vary between browsers. See Remi's comment in CHART-762.
        """
        parent_css="#TableChart_1 text[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 15)
        
        expected_text_list=['BANNING', 'CROSS', 'IRVING', 'SMITH', 'BLACKWOOD', 'ROMANS', 'MCCOY', 'JONES', 'MCKNIGHT', 'STEVENS', 'GREENSPAN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#TableChart_1", expected_text_list, "Step 03:01: Verify the tag cloud text")
        expected_text_color_dict={'BANNING':'bar_blue','CROSS':'bar_blue','IRVING':'bar_blue','SMITH':'bar_blue','BLACKWOOD':'bar_blue','ROMANS':'bar_blue','MCCOY':'bar_blue','MCKNIGHT':'bar_blue','STEVENS':'bar_blue','GREENSPAN':'bar_blue'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#TableChart_1", expected_text_color_dict, "Step 03:02: Verify tag cloud chart text colors")
        """ 
            Step 10:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 20)
            
        """ 
            Step 11:Verify the following chart is displayed.
        """
        expected_text_list=['BANNING', 'CROSS', 'IRVING', 'SMITH', 'BLACKWOOD', 'ROMANS', 'MCCOY', 'JONES', 'MCKNIGHT', 'STEVENS', 'GREENSPAN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#jschart_HOLD_0", expected_text_list, "Step 11:01: Verify the tag cloud text")
        expected_text_color_dict={'BANNING':'bar_blue','CROSS':'bar_blue','IRVING':'bar_blue','SMITH':'bar_blue','BLACKWOOD':'bar_blue','ROMANS':'bar_blue','MCCOY':'bar_blue','MCKNIGHT':'bar_blue','STEVENS':'bar_blue','GREENSPAN':'bar_blue'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#jschart_HOLD_0", expected_text_color_dict, "Step 11:02: Verify tag cloud chart text colors")
        """ 
            Step 12:Hover over "BANNING" and verify the tooltip displays "CURR_SAL" value.
        """
        expected_tooltip_list=['LAST_NAME:BANNING', 'CURR_SAL:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mtag!", expected_tooltip_list, "Step 11:03: Verify Alfa Romeo tooltip information")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)     
        """ 
            Step 13:Click "IA" > "Save" > "C2228170" > "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
             
        """ 
            Step 14:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        """ 
            Step 15:Run saved fex from bip using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228170.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        
        parent_css="#jschart_HOLD_0 text[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 60)
             
        """
            Step 16:Verify the following chart is displayed.
        """
        expected_text_list=['BANNING', 'CROSS', 'IRVING', 'SMITH', 'BLACKWOOD', 'ROMANS', 'MCCOY', 'JONES', 'MCKNIGHT', 'STEVENS', 'GREENSPAN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#jschart_HOLD_0", expected_text_list, "Step 16:01: Verify the tag cloud text")
        expected_text_color_dict={'BANNING':'bar_blue','CROSS':'bar_blue','IRVING':'bar_blue','SMITH':'bar_blue','BLACKWOOD':'bar_blue','ROMANS':'bar_blue','MCCOY':'bar_blue','MCKNIGHT':'bar_blue','STEVENS':'bar_blue','GREENSPAN':'bar_blue'}
        ia_resultarea_obj.verify_tagcloud_chart_text_color("#jschart_HOLD_0", expected_text_color_dict, "Step 16:02: Verify tag cloud chart text colors")
        
        """ 
            Step 17:Hover over "BANNING" and verify the tooltip displays "CURR_SAL" value.
        """ 
        expected_tooltip_list=['LAST_NAME:BANNING', 'CURR_SAL:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mtag!", expected_tooltip_list, "Step 17:01: Verify Alfa Romeo tooltip information")
            
        """ 
            Step 18:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4) 
           
        """ 
            Step 19:Restore the fex using API
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228170.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 text[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 60)
             
        """
            Step 20:Verify the following chart is displayed.
        """
        expected_text_list=['BANNING', 'CROSS', 'IRVING', 'SMITH', 'BLACKWOOD', 'ROMANS', 'MCCOY', 'JONES', 'MCKNIGHT', 'STEVENS', 'GREENSPAN']
        ia_resultarea_obj.verify_tagcloud_chart_text("#TableChart_1", expected_text_list, "Step 20:01: Verify the tag cloud text")
        utillobj.verify_chart_color("TableChart_1",'riser!s0!g6!mtag!', 'bar_blue',"Step 20:Verifytagcloud text color")

        """ 
            Step 21:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
    

if __name__ == "__main__":
    unittest.main()