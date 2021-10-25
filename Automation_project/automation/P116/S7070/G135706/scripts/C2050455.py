'''
Created on Aug 18, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050455
'''
import unittest, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools.chart import Chart
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous

class C2050455_TestClass(BaseTestCase):

    def test_C2050455(self):
        
        """Test case variable"""

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        active = active_miscelaneous.Active_Miscelaneous(self.driver)
        chart_obj = Chart(self.driver)
        
        """
        1. Using infoassist, Create chart with CAR master file.
        From the Format tab, change the output to Active Report.
        Add CAR as X-axis and DEALER_COST as Measure(SUM)
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P116/S7070', 'mrid', 'mrpass')
        WebDriverWait(self.driver, 70).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id*=metaDataSearchTxtFld]')))  # time given to make infoassist to load    
        ribbonobj.change_output_format_type('active_report', 'Home')
        time.sleep(4)
        metaobj.datatree_field_click("CAR",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST",2,1)
        parent_css="#TableChart_1 svg g text.yaxis-title"
        utillobj.synchronize_with_visble_text(parent_css,"DEALER_COST", 10)
        
        '''
        Expect to see the following Preview pane.
        '''
        #VP: Verifying the X-Axis/Y-Axis Labels on Preview chart
        resultobj.verify_xaxis_title('TableChart_1', 'CAR', 'Step 01.01: verify the x_axis labels')
        resultobj.verify_yaxis_title('TableChart_1', 'DEALER_COST', 'Step 01.02: verify the y_axis labels')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.03: Verify the xy-Axis labels and bar fills')

        """
        2. From the Home tab, click themes icon and choose ENgradient_combine.sty theme.
        3. Click the Open button.
        
        Expect to see the following Preview pane, displaying gradient shading
        """
        ribbonobj.select_theme('Legacy Templates', 'ENgradient_combine.sty')
        
        # Verify Color on bars
        fill = 'url(#pfjTableChart_1__lineargradient_0_0_100p_0_0_4894213_1_035_83131255_1_1_1750136_1)'
        fill_r1 = driver.find_element_by_css_selector("#pfjTableChart_1>svg>g.chartPanel rect[class^='riser!s0!g7!mbar!']").get_attribute("fill")
        fill_r2 = driver.find_element_by_css_selector("#pfjTableChart_1>svg>g.chartPanel rect[class^='riser!s0!g2!mbar!']").get_attribute("fill")
        bar_r1 = (fill == fill_r1 == fill_r2)
        utillity.UtillityMethods.asequal(self,True, bar_r1, 'Step 03.01: Verifying theme color on preview chart')
        
        """
        4. Click the Run button.
         
        Expect to see the following Bar Chart with gradient styling applied.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^=ReportIframe-]", 1, 30)
        utillobj.switch_to_frame()
        
        # verify total number of slicers
        resultobj.verify_number_of_riser('MAINTABLE_wbody0_f',1,10,'Step 04.01: Verify the total number of risers displayed on Run Chart')
        #VP: Verifying the X-Axis/Y-Axis Labels on Preview chart
        parent_css="MAINTABLE_wbody0_f"
        resultobj.verify_xaxis_title(parent_css, 'CAR', "Step 04.02: Verify x_axis title")
        resultobj.verify_yaxis_title(parent_css, 'DEALER_COST', "Step 04.03: Verify y_axis title")
        expected_xaxis_label=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yaxis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels(parent_css, expected_xaxis_label, expected_yaxis_label, 'Step 04.04:')
        active.verify_chart_title(parent_css+"t", 'DEALER_COST by CAR', 'Step 04.05: Verify chart title')
        active.verify_arChartToolbar('MAINTABLE_wmenu0 ', ['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation'], 'Step 04.06: Verify chart tool menus', custom_css='[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu0 ', ['Sum'], 'Step 04.07: Verify Aggregation menu text', text=True, custom_css="[id^='SUM'] td[class^='tabPagingTex']")
        fill = 'url(#MAINTABLE_wbody0_f__lineargradient_0_0_100p_0_0_4894213_1_035_83131255_1_1_1750136_1)'
        fill_r1 = driver.find_element_by_css_selector("#MAINTABLE_wbody0_f>svg>g.chartPanel rect[class^='riser!s0!g7!mbar!']").get_attribute("fill")
        fill_r2 = driver.find_element_by_css_selector("#MAINTABLE_wbody0_f>svg>g.chartPanel rect[class^='riser!s0!g2!mbar!']").get_attribute("fill")
        bar_r1 = (fill == fill_r1 == fill_r2)
        utillity.UtillityMethods.asequal(self,True, bar_r1, 'Step 04.08: Verifying theme color on Run chart')
        time.sleep(2)            
          
        """
        5. In Format tab, Select line chart in chart types
        Expect to see the following Line Chart Preview pane. 
        """
        chart_obj.switch_to_default_content()
        chart_obj.select_ia_ribbon_item('Format', 'line')
        parent_css="TableChart_1"
        parent_css1="#"+parent_css+" svg g circle[class*='marker']"
        utillobj.synchronize_with_number_of_element(parent_css1, 10, 25)
        
        resultobj.verify_xaxis_title(parent_css, 'CAR', "Step 05.01: Verify x_axis title")
        resultobj.verify_yaxis_title(parent_css, 'DEALER_COST', "Step 05.02: Verify y_axis title")
        expected_xaxis_label=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yaxis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels(parent_css, expected_xaxis_label, expected_yaxis_label, 'Step 05.03:')
        
        fill = 'url(#pfjTableChart_1__lineargradient_0_0_100p_0_0_4894213_1_035_83131255_1_1_1750136_1)'
        fill_r1 = driver.find_element_by_css_selector("#pfjTableChart_1>svg>g.chartPanel circle[class^='marker!s0!g1!mmarker!']").get_attribute("fill")
        fill_r2 = driver.find_element_by_css_selector("#pfjTableChart_1>svg>g.chartPanel circle[class^='marker!s0!g6!mmarker!']").get_attribute("fill")
        line_r1 = (fill == fill_r1 == fill_r2)
        utillity.UtillityMethods.asequal(self,True, line_r1, 'Step 05.04: Verifying Line color on preview chart')
           
        """
        6. Run the report
        Expect to see the following Run time Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')  
        elem_css='[id^=ReportIframe-]'
        utillobj.synchronize_with_number_of_element(elem_css, 1, 25)
        utillobj.switch_to_frame()
        parent_css="MAINTABLE_wbody0_f"
        resultobj.verify_xaxis_title(parent_css, 'CAR', "Step 06.01:Verify x_axis title")
        resultobj.verify_yaxis_title(parent_css, 'DEALER_COST', "Step 06.02:Verify y_axis title")
        expected_xaxis_label=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yaxis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels(parent_css, expected_xaxis_label, expected_yaxis_label, 'Step 06.03:')
        active.verify_chart_title(parent_css+"t", 'DEALER_COST by CAR', 'Step 06.04: Verify chart title')
        active.verify_arChartToolbar('MAINTABLE_wmenu0 ', ['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation'], 'Step 06.05: Verify chart tool menus', custom_css='[title]')
        active.verify_arChartToolbar('MAINTABLE_wmenu0 ', ['Sum'], 'Step 06.06 : Verify Aggregation menu text', text=True, custom_css="[id^='SUM'] td[class^='tabPagingTex']")
        fill = 'url(#MAINTABLE_wbody0_f__lineargradient_0_0_100p_0_0_4894213_1_035_83131255_1_1_1750136_1)'
        fill_r1 = driver.find_element_by_css_selector("#MAINTABLE_wbody0_f>svg>g.chartPanel circle[class^='marker!s0!g1!mmarker!']").get_attribute("fill")
        fill_r2 = driver.find_element_by_css_selector("#MAINTABLE_wbody0_f>svg>g.chartPanel circle[class^='marker!s0!g6!mmarker!']").get_attribute("fill")
        bar_r1 = (fill == fill_r1 == fill_r2)
        utillity.UtillityMethods.asequal(self,True, bar_r1, 'Step 06.07: Verifying theme color on Run chart')
        time.sleep(2)       
   
        utillobj.switch_to_default_content(pause=2) 
        
if __name__ == '__main__':
    unittest.main()