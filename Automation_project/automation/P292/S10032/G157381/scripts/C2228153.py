'''
Created on Dec 18, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228153
TestCase Name : Verify Document with Report and Chart components
'''
import unittest, time
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous

class C2228153_TestClass(BaseTestCase):

    def test_C2228153(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = "C2228513"
        
        """   
            TESTCASE OBJECTS 
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=Document&master=ibisamp/Car
        """
        utillobj.infoassist_api_login('document','ibisamp/car','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 75)
        
        """
            Step 02:Double click "CAR", "DEALER_COST", "SALES".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6,25)
        
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 17, 25)
        
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 28, 25)
        
        """ 
            Step 03:Verify the following document is displayed.
        """
        coln_list = ["COUNTRY", "CAR", "SALES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 03:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1 ', 10, 3, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1 ', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 03:02: Verify Preview report dataset')
        
        """ 
            Step 04:Select "Insert" > "Chart".
        """
        ribbonobj.select_ribbon_item("Insert", "Chart")   
        """ 
            Step 05:Double click "CAR", "DEALER_COST" For the chart.
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 text[class^='xaxis'][class$='title']", 'COUNTRY', 15)
        
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 text[class^='xaxis'][class$='title']", 'COUNTRY : CAR', 15)
        
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 text[class^='yaxis'][class$='title']", 'SALES', 15)
        """ 
            Step 06:Verify the following chart is displayed in "Live Preview".
        """
        expected_yval_list=['0','20K','40K','60K','80K','100K']
        expected_xval_list=['ENGLAND : J...', 'ENGLAND : J...', 'ENGLAND : T...', 'FRANCE : PE...', 'ITALY : ALFA...', 'ITALY : MASER...', 'JAPAN : DATS...', 'JAPAN : TOYOTA', 'W GERMANY :...', 'W GERMANY :...']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, 'Step 06:01: X and Y axis labels',x_axis_label_length=1)
        resultobj.verify_number_of_riser('TableChart_2',1,10, 'Step 06:02: Verify Number riser in the created chart')
        resultobj.verify_yaxis_title("TableChart_2", 'SALES', "Step 06:03: Verify y-Axis Title")
        resultobj.verify_xaxis_title("TableChart_2", 'COUNTRY : CAR', "Step 06:04: Verify X-Axis Title")
         
        """ 
            Step 07:Re-position the newly added chart to show the report below it.
        """
        ribbonobj.repositioning_document_component('0.90','3.88')
        elem=self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(1)
        ribbonobj.repositioning_document_component('0.96','0.45')
        time.sleep(2)
          
        """ 
            Step 08:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        parent_css="#IWindowBody0 span[title='Move to Top'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 08:01: Verify the Report Heading')
         
        """ 
            Step 09:Verify the following document (Report and Chart) is displayed.
        """
        column_list=['COUNTRY','CAR','SALES']
        miscobj.verify_column_heading('ITableData0', column_list, "Step 09:00: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 09:02: Verify data.')
        expected_yval_list=['0','20K','40K','60K','80K','100K']
        expected_xval_list=['ENGLAND : J...', 'ENGLAND : J...', 'ENGLAND : T...', 'FRANCE : PE...', 'ITALY : ALFA...', 'ITALY : MASER...', 'JAPAN : DATS...', 'JAPAN : TOYOTA', 'W GERMANY :...', 'W GERMANY :...']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_1", expected_xval_list, expected_yval_list, 'Step 09:03: X and Y axis labels',x_axis_label_length=1)
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","SALES by COUNTRY, CAR", "Step 09:04 : Verify chart title ")
        resultobj.verify_number_of_riser('MAINTABLE_1',1,10, 'Step 09:05: Verify Number riser in the created chart')
        resultobj.verify_yaxis_title("MAINTABLE_1", 'SALES', "Step 09:06: Verify y-Axis Title")
        resultobj.verify_xaxis_title("MAINTABLE_1", 'COUNTRY : CAR', "Step 09:07: Verify X-Axis Title")
        expected_tooltip_list=['COUNTRY:W GERMANY', 'CAR:BMW', 'SALES:80390', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_1", "riser!s0!g9!mbar!", expected_tooltip_list, "Step 09:08:Verify bar chart riser tooltip value")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g9!mbar!", "bar_blue", "Step 09:09 Verify  riser color")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1',['More Options','Advanced Chart','Original Chart'], "Step 09:10: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 09:11 Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        utillobj.switch_to_default_content(pause=2)
         
        """
            Step 10:Click Save in the toolbar > Save as "C2228153" > Click Save
            Step 11:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """ 
            Step 12:Run from bip
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228153.fex
        """
        utillobj.infoassist_api_logout()
        time.sleep(8)
        """ 
            Step 13:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="#IWindowBody0 span[title='Move to Top'] img"
        resultobj.wait_for_property(parent_css, 1, expire_time=65)
        column_list=['COUNTRY','CAR','SALES']
        miscobj.verify_column_heading('ITableData0', column_list, "Step 14:01: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 14:02: Verify data.')
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft", "SALES by COUNTRY, CAR","Step 14:03: Verify chart title")
        expected_yval_list=['0','20K','40K','60K','80K','100K']
        expected_xval_list=['ENGLAND : J...', 'ENGLAND : J...', 'ENGLAND : T...', 'FRANCE : PE...', 'ITALY : ALFA...', 'ITALY : MASER...', 'JAPAN : DATS...', 'JAPAN : TOYOTA', 'W GERMANY :...', 'W GERMANY :...']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_1", expected_xval_list, expected_yval_list, 'Step 14:04: X and Y axis labels',x_axis_label_length=1)
        resultobj.verify_number_of_riser('MAINTABLE_1',1,10, 'Step 14:05: Verify Number riser in the created chart')
        resultobj.verify_yaxis_title("MAINTABLE_1", 'SALES', "Step 14:06: Verify y-Axis Title")
        resultobj.verify_xaxis_title("MAINTABLE_1", 'COUNTRY : CAR', "Step 14:07: Verify X-Axis Title")
        expected_tooltip_list=['COUNTRY:W GERMANY', 'CAR:BMW', 'SALES:80390', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_1", "riser!s0!g9!mbar!", expected_tooltip_list, "Step14:08:Verify bar chart riser tooltip value")
        time.sleep(2)
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1',['More Options','Advanced Chart','Original Chart'], "Step 14:09: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 14:10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g9!mbar!", "bar_blue", "Step 14:11: Verify  riser color")
        
if __name__ == "__main__":
    unittest.main()