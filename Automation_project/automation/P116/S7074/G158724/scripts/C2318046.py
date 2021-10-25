'''
Created on Nov 23, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/tests/view/14084503&group_by=cases:custom_automation_status&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2318046
TestCase Name = Verify Mekko Chart in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon
from common.lib import utillity

class C2318046_TestClass(BaseTestCase):

    def test_C2318046(self):
        
        Test_Case_ID="C2318046"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        """
        Step 01:Right click on folder created in IA and create a new Chart using the GGSALES file.
                From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S10670', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1) 
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.1: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 01.2: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 01.3: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 01.4: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar", "med_green", "Step 01.5: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar", "pale_yellow_2", "Step 01.6: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar", "brick_red", "Step 01.7: Verify  bar color")
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.8: Verify Y-Axis legend")      
        """
            Step 02:Add fields Product, Unit Sales, Sequence# & Dollar Sales.
        """
        metadataobj.datatree_field_click('Product', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True, expire_time=25)
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True, expire_time=25)
        metadataobj.datatree_field_click('Sequence#', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Sequence#', with_regular_exprestion=True,expire_time=25)
        metadataobj.datatree_field_click('Dollar Sales', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True, expire_time=25)
        time.sleep(3)
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 02.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval1_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 6, 'Step 02.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 02.4: Verify  bar color")
        legend=["Unit Sales","Sequence#","Dollar Sales"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.5: Verify Y-Axis legend")    

        """
            Step 03:Click the Run button.
                    Expect to see the following Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s2!g0!mbar!", expected_tooltip_list, "Step 03.1: Verify bar value")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 03.2: Verify -xAxis Title")       
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 30, 'Step 03.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 03.5: Verify  bar color")
        legend=["Unit Sales","Sequence#","Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.6: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Sequence#, Dollar Sales by Product', 'Step 03.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)


        """
            Step 04:Select Format > Other.
                    Select the HTML5 series of charts.From Select a chart pop up choose Mekko Chart.
                    Click OK.
                    Expect to see the Clustered bar chart converted into the Preview pane for Mekko Chart.
        """
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        resobj.wait_for_property(parent_css, 1, expire_time=50, string_value='Selectachart', with_regular_exprestion=True)
        ia_ribbobj.select_other_chart_type('html5', 'html5_Mekko', 2, ok_btn_click=True)
        time.sleep(3)
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 04.1: Verify -xAxis Title")
        expected_xval_list=['Espresso', 'Capuccino']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04.2: Verify XY Label')
        expected_label_list=["Unit Sales","Sequence#","Dollar Sales"]
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 04.3: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 04.4: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 6, 'Step 04.5: Verify the total number of risers displayed on preview')
        expected_datalabel=['4.1M', '2.6M']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 04.6: Verify datalabels ', custom_css=".chartPanel text[class^='stackTotalLabel']") 

        """
            Step 05:Click the Run button.
                    Expect to see the following Mekko Chart.
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5) 
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 05.1: Verify X-Axis Title")
        expected_xval_list=['Latte', 'Croissant', 'Mug', 'Biscotti', 'Scone', 'Espresso', 'Thermos', 'Coffee Pot', 'Coffee Grin...', 'Capucc...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list,'Step 05.2: Verify XY Label', x_axis_label_length=2)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 30, 'Step 05.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g6!mbar!', 'bar_blue', 'Step 05.4: Verify Color')       
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Sequence#, Dollar Sales by Product', 'Step 05.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=["Unit Sales","Sequence#","Dollar Sales"]
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 05.9 Verify Legends ')
        expected_datalabel=['12.7M', '9.9M', '7.0M', '6.4M', '5.5M', '4.3M', '3.8M', '3.6M', '3.4M', '2.6M']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 05.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s2!g0!mbar!', expected_tooltip_list, 'Step 05.11: verify the default tooltip values')
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)   
            

if __name__ == '__main__':
    unittest.main()
        


