'''
Created on DEC 04, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235380
TestCase Name = Test Splash Screen and Switch Reports shortcut
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_resultarea,visualization_properties
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C2235380_TestClass(BaseTestCase):

    def test_C2235380(self):
        
        Test_Case_ID = "C2235380"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)  
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)  
        propertyobj =visualization_properties.Visualization_Properties(self.driver)
        
        """
            Step 01:Launch IA Report mode:
                http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login_with_masterfile_promt('report', 'mrid', 'mrpass')       
        parent_css="[id*='dlgIbfsOpenFile7'] div[class='bi-window-caption window-caption']"
        resobj.wait_for_property(parent_css, 1)
         
        """
            Step 02:Select baseapp/wf_retail_lite > click Open
        """
        utillobj.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        time.sleep(5)
        parent_css="div[align='justify']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(2)
        """
            Step 03:Double click fields "Product,Category" and "Cost of Goods"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(3) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=50)
        time.sleep(1)
        ia_resultobj.create_across_report_data_set('TableChart_1', 2, 2, 7, 1, Test_Case_ID+'_DataSet_01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,1,Test_Case_ID+'_DataSet_01.xlsx','Step 03 : Verify report')
   
        """
            Step 04:Click "New" button in the toolbar > Select "Build a Chart"
        """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        resobj.wait_for_property("#splash_options", 1, expire_time=8)   
        ribbonobj.select_item_in_splash_options("Build a Chart")
 
        """
            Step 05:Select wf_retail_lite > click Open
        """
        utillobj.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        time.sleep(5)
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        """
            Step 06:Double click fields "Product,Category" and "Cost of Goods"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=20)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=20)
        time.sleep(1)
        resobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 06.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'Cost of Goods', "Step 06.2: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 06.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 06.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 06.5: Verify the total number of risers displayed on preview')
         
        """
            Step 07:Click "New" button in the toolbar > Select "Build a Document"
        """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        resobj.wait_for_property("#splash_options", 1, expire_time=8)   
        ribbonobj.select_item_in_splash_options("Build a Document")
         
        """
            Step 08:Select wf_retail_lite > click Open
        """
        utillobj.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        time.sleep(5)
        resobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=10, string_value='Document') 
         
        """
            Step 09:Double click fields "Product,Category" and "Cost of Goods"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=20)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=20)
        time.sleep(1)
        resobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 09.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'Cost of Goods', "Step 09.2: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 09.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 09.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 09.5: Verify the total number of risers displayed on preview')
         
        """
            Step 10:Click "New" button in the toolbar > Select "Build a Visualization"
        """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        resobj.wait_for_property("#splash_options", 1, expire_time=8)   
        ribbonobj.select_item_in_splash_options("Build a Visualization")
         
        """
            Step 11:Select car from ibisamp > click Open
        """
        utillobj.select_masterfile_in_open_dialog("ibisamp", "car")
        time.sleep(5)
        resobj.wait_for_property("#pfjTableChart_1 g text[class='title']", 1, expire_time=25, string_value='DropMeasuresorSortsintotheQueryPane',with_regular_exprestion=True ) 
        
        """
            Step 12:Double click fields "Car" and "Sales"
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='CAR', with_regular_exprestion=True,expire_time=20)
        metaobj.datatree_field_click("SALES", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='SALES', with_regular_exprestion=True,expire_time=20)
        resobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 12.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'SALES', "Step 12.2: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 12.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 12.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 12.5: Verify the total number of risers displayed on preview')
               
        """
            Step 13:Drag field "Car" to the Filter pane > Click OK to create filter
        """
        metaobj.datatree_field_click('CAR',1,1,'Filter')
        time.sleep(5)
        item_list=['[All]', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True)
        metaobj.verify_filter_pane_field('CAR',1,"Step 13.1: Verify Car appears in filter pane")
        resobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 13.2: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'SALES', "Step 13.3: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 13.4: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 13.5: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 13.6: Verify the total number of risers displayed on preview')
        if Global_variables.browser_name == 'ie':
            verify_type='true'
        else:
            verify_type=True
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=verify_type, msg="Step 13.7: Verify [All] is checked in filter prompt")
        
        """
            Step 14:Click on the "Reports" shortcut in the lower right corner in Visualization mode
        """
        
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReportPanel")
        utillobj.default_left_click(object_locator=elem)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu( verify='true',expected_popup_list=['Report1', 'Chart1', 'Document1', 'Visual1'],msg='Step 1: Verify popup menu')
        time.sleep(5)
        """
            Step 15:Select the "Document1" fex
        """
        utillobj.select_or_verify_bipop_menu('Document1')
        time.sleep(5)
        
        """
        Step 16:Verify Document Canvas
        """
        resobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        resobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 16.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'Cost of Goods', "Step 16.2: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 16.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 16.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 16.5: Verify the total number of risers displayed on preview')
        
        """
            Step 17:Click on the "Reports" shortcut in the lower right corner in Document mode
        """
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReportPanel")
        utillobj.default_left_click(object_locator=elem)
        time.sleep(1)
        
        """
            Step 18:Select the "Chart1" fex
        """
        utillobj.select_or_verify_bipop_menu('Chart1')
        time.sleep(5)
        
        """
            Step 19:Verify Preview
        """
        parent_css="#TableChart_1 text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product Category',expire_time=20)
        resobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 17.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'Cost of Goods', "Step 17.2: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 17.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 17.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 17.5: Verify the total number of risers displayed on preview')       
        
        """
            Step 20:Click on the "Reports" shortcut in the lower right corner in Chart mode
        """
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReportPanel")
        utillobj.default_left_click(object_locator=elem)
        time.sleep(1)
        
        """
            Step 21:Select the "Report1" fex
        """
        utillobj.select_or_verify_bipop_menu('Report1')
        time.sleep(5)
        
        """
            Step 22:Verify Preview
        """
        parent_css="#TableChart_1 div[class^='x']"
        resobj.wait_for_property(parent_css, 18)
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,2,7,1,Test_Case_ID+'_DataSet_01.xlsx','Step 22: Verify report')
        
        """
            Step 23:Click on the "Reports" shortcut in the lower right corner in Report mode
        """ 
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReportPanel")
        utillobj.default_left_click(object_locator=elem)
        time.sleep(1)        
        
        """
            Step 24:Select the "Visual1" fex
        """ 
        
        utillobj.select_or_verify_bipop_menu('Visual1')
        time.sleep(5)
        parent_css="#TableChart_1 text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='CAR', with_regular_exprestion=True,expire_time=20) 
        
        """
            Step 25:Verify Visualization Preview with chart a Filter Prompt
        """
        resobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 25.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("TableChart_1", 'SALES', "Step 25.2: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 25.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 25.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 25.5: Verify the total number of risers displayed on preview')
        if Global_variables.browser_name == 'ie':
            verify_type='true'
        else:
            verify_type=True
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=verify_type, msg="Step 25.6: Verify [All] is checked in filter prompt")
        
        """
            Step 26:Click "IA" menu > "Close"
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(3)
        
        """
            Step 27:Select "No" in Visual1 save prompt
        """
        btn_No=driver.find_element_by_id('btnNo')
        btn_No.click()
#         utillobj.default_left_click(object_locator=btn_No)

        """
            Step 28:Click "IA" menu > "Close"
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(3)
        
        """
            Step 29:Select "No" in Report1 save prompt
        """
        btn_No=driver.find_element_by_id('btnNo')
        btn_No.click()
#         utillobj.default_left_click(object_locator=btn_No)
        time.sleep(1)
        
        """
            Step 30:Click "IA" menu > "Close"
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(3)
        
        """
            Step 31:Select "No" in Chart1 save prompt
        """
        btn_No=driver.find_element_by_id('btnNo')
        btn_No.click()
        time.sleep(1)
#         utillobj.default_left_click(object_locator=btn_No)

        """
            Step 32:Click "IA" menu > "Close"
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(3)
        
        """
            Step 33:Select "No" in Document1 save prompt
        """
        btn_No=driver.find_element_by_id('btnNo')
        btn_No.click()
        time.sleep(1)
#         utillobj.default_left_click(object_locator=btn_No)
        
        """
            Step 34:Verify there are no reports opened in IA
        """
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReportPanel")
        elem.click()
#         utillobj.default_left_click(object_locator=elem)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu( verify='true',expected_popup_list=['<Empty>'],msg='Step 34: Verify there are no reports opened in IA')
        time.sleep(5)
        css=["#HomeTab_tabButton", "#InsertTab_tabButton", "#FormatTab_tabButton", "#DataTab_tabButton"]
        for i in range(len(css)):
            status = bool(self.driver.find_element_by_css_selector(css[i]).get_attribute("disabled"))
            utillobj.asequal(True, status, "Step 03"+str(i)+": Verify all option is disabled there are no reports opened")
        
        """
            Step 35:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        time.sleep(2)        
          
if __name__ == '__main__':
    unittest.main() 