'''
Created on Dec 15, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2355874
Test case Name =  Create Narrative Chart
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,wf_administration_console
from common.lib import utillity

class C2355874_TestClass(BaseTestCase):

    def test_C2355874(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2355874'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfadminconsoleobj = wf_administration_console.Wf_Administration_Console(self.driver)
        
        """PRECONDITION"""
        """Feature has to be enabled by administrator (admin console has to have the URL for the text server http://ibivmappsa.ibi.com:9080/yseop-manager/direct/savvy-kb/dialog.do)."""
       
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/signin'
        driver.get(setup_url)
        time.sleep(3)
        parent_css= "[id=SignonbtnLogin]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        time.sleep(3)
        utillobj.login_wf('mrid01', 'mrpass01')
        time.sleep(5)
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        admin_console_url = 'http://' + node + ':' + port + context + '/admin'
        driver.get(admin_console_url)
        time.sleep(8)
        parent_css= "#console_tree_Configuration_Settings .bi-tree-view-body-content"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        wfadminconsoleobj.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "Text Generation Server")
        
        url = 'http://ibivmappsa.ibi.com:9080/yseop-manager/direct/savvy-kb/dialog.do'
        text_input_css = driver.find_element_by_css_selector("input[id^='editIBI_TEXT_GENERATION_SERVER_URL'][class^='bi-text-field text-field']")
        utillobj.set_text_field_using_actionchains(text_input_css, url, keyboard_type=True)
        time.sleep(3)
        ok_btn=driver.find_element_by_css_selector("#_ReportingServerClientSaveButton")
        ok_btn.click()
        time.sleep(3)
        utillobj.verify_js_alert('Successfully Saved', 'Verify Alert')
        time.sleep(10)
        wfadminconsoleobj.select_or_verify_top_toolbar_links('clearcache')
        cache_dialog= "#ClearCacheDialog"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.click_dialog_button(cache_dialog, 'OK')
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """TESTCASE"""
        """
        Step 01: Use API call to create new chart with wf_retail:
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail','P292/S10117_chart_visual_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#TableChart_1 svg rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 25, 20)
        
        """
        Step 02: Double click Gross Profit & Product Category
        """
        metaobj.datatree_field_click("Gross Profit",2,1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 20)
        
        metaobj.datatree_field_click("Product,Category",2,1)
        time.sleep(4)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        
        """
        Step 03: Select Format tab > Features > Narrative
        """
        ribbonobj.select_ribbon_item('Format', 'Narrative')
        
        """
        Step 03.1: Text describing the chart appears at the top of the chart
        """
        time.sleep(3)
        parent_css="[class='narrativeText']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        actual_narrative_txt = driver.find_element_by_css_selector("[class='narrativeText-label']").text.strip()
        print(actual_narrative_txt)
        
        expected_narrative_txt1 = "Gross Profit"
        utillobj.asin(expected_narrative_txt1, actual_narrative_txt, "Step 03.1: Narrative Text describing the chart appears at the top of the chart in line1")
        
        expected_narrative_txt2 = "Product Category range of Accessories - Video Production."
        utillobj.asin(expected_narrative_txt2, actual_narrative_txt, "Step 03.2: Narrative Text describing the chart appears at the top of the chart in line1")
        
        expected_narrative_txt3 = "the Gross Profit overall"
        utillobj.asin(expected_narrative_txt3, actual_narrative_txt, "Step 03.3: Narrative Text describing the chart appears at the top of the chart in line2")
        
        expected_narrative_txt4 = "from 39,854,441 to 17,947,620."
        utillobj.asin(expected_narrative_txt4, actual_narrative_txt, "Step 03.4: Narrative Text describing the chart appears at the top of the chart in line2")
        
        expected_narrative_txt5 = "in Stereo Systems at 86,181,071."
        utillobj.asin(expected_narrative_txt5, actual_narrative_txt, "Step 03.5: Narrative Text describing the chart appears at the top of the chart in line3")
        
        expected_narrative_txt6 = "Gross Profit fell to 17,947,620, a 55%"
        utillobj.asin(expected_narrative_txt6, actual_narrative_txt, "Step 03.6: Narrative Text describing the chart appears at the top of the chart in line3")
        
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03:a(ii) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 03.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 03.c: Verify first bar color")
        time.sleep(5)

        """
        Step 04: Save chart with name C2355874 and close.
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(2)

        """
        Step 05: Run the chart with API call:
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2355874.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex",'S10117_chart_visual_1', 'mrid', 'mrpass')
        time.sleep(6)
        parent_css= "#jschart_HOLD_0 svg rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        
        """verify run window"""
        time.sleep(3)
        parent_css="[class='narrativeText']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        actual_narrative_txt = driver.find_element_by_css_selector("[class='narrativeText-label']").text.strip()
        print(actual_narrative_txt)
        
        expected_narrative_txt1 = "Gross Profit"
        utillobj.asin(expected_narrative_txt1, actual_narrative_txt, "Step 05.1: Narrative Text describing the chart appears at the top of the chart in line1")
        
        expected_narrative_txt2 = "Product Category range of Accessories - Video Production."
        utillobj.asin(expected_narrative_txt2, actual_narrative_txt, "Step 05.2: Narrative Text describing the chart appears at the top of the chart in line1")
        
        expected_narrative_txt3 = "the Gross Profit overall"
        utillobj.asin(expected_narrative_txt3, actual_narrative_txt, "Step 05.3: Narrative Text describing the chart appears at the top of the chart in line2")
        
        expected_narrative_txt4 = "from 39,854,441 to 17,947,620."
        utillobj.asin(expected_narrative_txt4, actual_narrative_txt, "Step 05.4: Narrative Text describing the chart appears at the top of the chart in line2")
        
        expected_narrative_txt5 = "in Stereo Systems at 86,181,071."
        utillobj.asin(expected_narrative_txt5, actual_narrative_txt, "Step 05.5: Narrative Text describing the chart appears at the top of the chart in line3")
        
        expected_narrative_txt6 = "Gross Profit fell to 17,947,620, a 55%"
        utillobj.asin(expected_narrative_txt6, actual_narrative_txt, "Step 05.6: Narrative Text describing the chart appears at the top of the chart in line3")
        
        time.sleep(3)
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 05:a(ii) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 05.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Gross Profit:$39,854,440.53']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar, "Step 05.d: Verify bar value")
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,'C2355874_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1) 
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 06: Restore chart for edit with IA using API call:
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%C2355874.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10117_chart_visual_1', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        parent_css= "#TableChart_1 svg rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 20)
        
        """Chart opens without error."""
        time.sleep(3)
        parent_css="[class='narrativeText']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        actual_narrative_txt = driver.find_element_by_css_selector("[class='narrativeText-label']").text.strip()
        print(actual_narrative_txt)
        
        expected_narrative_txt1 = "Gross Profit"
        utillobj.asin(expected_narrative_txt1, actual_narrative_txt, "Step 06.1: Narrative Text describing the chart appears at the top of the chart in line1")
        
        expected_narrative_txt2 = "Product Category range of Accessories - Video Production."
        utillobj.asin(expected_narrative_txt2, actual_narrative_txt, "Step 06.2: Narrative Text describing the chart appears at the top of the chart in line1")
        
        expected_narrative_txt3 = "the Gross Profit overall"
        utillobj.asin(expected_narrative_txt3, actual_narrative_txt, "Step 06.3: Narrative Text describing the chart appears at the top of the chart in line2")
        
        expected_narrative_txt4 = "from 39,854,441 to 17,947,620."
        utillobj.asin(expected_narrative_txt4, actual_narrative_txt, "Step 06.4: Narrative Text describing the chart appears at the top of the chart in line2")
        
        expected_narrative_txt5 = "in Stereo Systems at 86,181,071."
        utillobj.asin(expected_narrative_txt5, actual_narrative_txt, "Step 06.5: Narrative Text describing the chart appears at the top of the chart in line3")
        
        expected_narrative_txt6 = "Gross Profit fell to 17,947,620, a 55%"
        utillobj.asin(expected_narrative_txt6, actual_narrative_txt, "Step 06.6: Narrative Text describing the chart appears at the top of the chart in line3")
        
        time.sleep(3)
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 06:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 06:a(ii) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 06.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 06.c: Verify first bar color")
        time.sleep(5)
        
        """
        Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()