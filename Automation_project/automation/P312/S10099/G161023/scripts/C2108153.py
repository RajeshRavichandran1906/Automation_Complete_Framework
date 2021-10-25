'''
Created on 8June, 2016
@author: Kiruthika
Completed on 10Jun 2016

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108153&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case Description : IA-4538:BUE: FOC error on Exclude when field contains quote
'''
import unittest, time, re
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon

class C2108153_TestClass(BaseTestCase):

    def test_C2108153(self):
        
        """
        TESTCASE OBJECTS
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
                   
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108153'
                     
        def verify_chart_color(parent_id, riser_class, color, msg):
            """
            parent_id='MAINTABLE_0'
            riser_class='riser!s1!g8!mbar!'
            color='green OR #gf443' OR 'text-green'(text-green means it will verify only green not the rgb of green)
            color='green'
            Syntax:verify_chart_color('MAINTABLE_0', 'riser!s1!g8!mbar!', 'green OR #gf443', 'Step 10: Verify Color')
            Syntax:verify_chart_color('MAINTABLE_0', 'riser!s1!g8!mbar!', 'green', 'Step 10: Verify Color')
            @author : Niranjan
            """
            raiser_css="#"+ parent_id + " [class*='" + riser_class + "']"
             
            actual_color = driver.find_element_by_css_selector(raiser_css).value_of_css_property("stroke")
            expected_color_list=[]
            for color_item in color.split(' OR '):
                if bool(re.match(r'^\#', color_item)):
                    expected_color_list.append(color_item)
                elif bool(re.match(r'^text-(.*)', color_item)):
                    reobj=re.match(r'^text-(.*)', color_item)
                    expected_color_list.append(reobj.group(1))
                else:
                    expected_color_list.append(utillobj.color_picker(color_item))
            utillobj.asin(actual_color, expected_color_list, msg)
        
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/customer_data&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/customer_data','P312/S10099', 'mrid', 'mrpass')
        element_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 60)
        
        """
        Step 02: Change to scatter chart.
        """
        ribbonobj.change_chart_type("scatter")
        """
        Step 03: Add Net Sales to vertical axis.
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Net Sales', 1, 'Vertical Axis', 0)
#         metaobj.datatree_field_click('Net Sales', 1, 1, 'Add To Query', 'Vertical Axis')
        time.sleep(5)
#         ia.add_field_right_click_menu_submenu('Net Sales', 'Add To Query',second_menu='Vertical Axis')
        """
        Step 04: Add Number of Days Since Contact to Horizontal axis.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Number of Days Since Contact', 1, 'Horizontal Axis', 0)
#         metaobj.datatree_field_click('Number of Days Since Contact', 1, 1, 'Add To Query', 'Horizontal Axis')
#         ia.add_field_right_click_menu_submenu('Number of Days Since Contact', 'Add To Query',second_menu='Horizontal Axis')
        """
        Step 05: Verify x and y axis labels.
        """
        time.sleep(5)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class='xaxisNumeric-title']"
        resultobj.wait_for_property(parent_css, 1)
        expected_xval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K'] 
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 05a: X annd Y axis Scales Values has changed or NOT')
        xaxis_value="Number of Days Since Contact"
        yaxis_value="Net Sales"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 05:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 05:c(ii) Verify Y-Axis Title")
        
        
        '''WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.XPATH,"//*[contains(@class,'xaxis')and contains(@class,'title')]")))
        time.sleep(5)
        resultobj.verification_x_y_label('Number of Days Since Contact', 'Net Sales', "Step 05: Verify x and y axis labels.")'''
        """
        Step 06: Add Net Sales to Size.
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Net Sales', 1, 'Size', 0)
#         metaobj.datatree_field_click('Net Sales',1,1,'Add To Query','Size')
        """
        Step 07: Add Company Name to Detail.
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Company->Company Name', 1, 'Detail', 0)
        time.sleep(5)
#         metaobj.datatree_field_click('Company Name', 1, 1,'Add To Query','Detail')
        """
        Step 08: Add Sales Region to Color.
        """
        chart_type_css="circle[class*='riser!s0!g44!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Sales->Sales Region', 1, 'Color', 0)
#         metaobj.datatree_field_click('Sales Region',1, 1,'Add To Query','Color')
        """
        Step 09: Add Sales Region to Columns.
        """
        chart_type_css="circle[class*='riser!s0!g44!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        metaobj.datatree_field_click('Dimensions->Sheet1->Sales->Sales Region',1,1,'Add To Query','Columns')
        chart_type_css="circle[class*='riser!s3!g130!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """
        Step10: Verify legend title and values
        """
        time.sleep(5)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='xaxisNumeric-title']"
        resultobj.wait_for_property(parent_css1, 5)
        expected_xval_list=['0','10','20','30','40','50','60','70'] 
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10a: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step 10.b(i) Verify first column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g290!mmarker", "pale_green", "Step 10.b(ii) Verify second column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g502!mmarker", "dark_green", "Step 10.b(iii) Verify third column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g130!mmarker", "pale_yellow", "Step 10.b(iiii) Verify fourth column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g235!mmarker!", "brick_red", "Step 10.b(iiiii) Verify fifth column circle color")
        xaxis_value="Number of Days Since Contact"
        yaxis_value="Net Sales"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 10:c(ii) Verify Y-Axis Title")
        labels=['Canada', 'Central', 'Eastern', 'Southern', 'Western']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1_f", "Columns", "Sales Region", labels, "Step 10:d")
         
         
        """
        Step 11: Verify query pane
        """
        metaobj.verify_query_pane_field("Columns", "Sales Region", 1, "Step 11a")
        metaobj.verify_query_pane_field("Vertical Axis", "Net Sales", 1, "Step 11b")
        metaobj.verify_query_pane_field("Horizontal Axis", "Number of Days Since Contact", 1, "Step 11c")
        metaobj.verify_query_pane_field("Size", "Net Sales", 1, "Step 11d")
        metaobj.verify_query_pane_field("Detail", "Company Name", 1, "Step 11e")
        metaobj.verify_query_pane_field("Color BY", "Sales Region", 1, "Step 11f")
         
        """
        Step 12: Lasso > Exclude from chart
        """
        time.sleep(5)
        resultobj.create_lasso("MAINTABLE_wbody1_f", "circle", "riser!s0!g73!mmarker!r0!c0!", target_tag='circle', target_riser='riser!s0!g41!mmarker!r0!c0!')
        resultobj.select_or_verify_lasso_filter(select="Exclude from Chart")
        chart_type_css="circle[class*='riser!s3!g130!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        #resultobj.lasso_by_offset('s0!g103!mmarker!r0!c0',80,60, 'rowcolumn',type="scatter")
        #resultobj.lasso_tooltip_menu('Exclude from Chart')
        """
        Step 13: Verify query added to filter pane
        """
        WebDriverWait(self.driver, 70).until(EC.presence_of_element_located((By.CSS_SELECTOR, "circle[class*='s0!g0!mmarker!r0!c0']")))
        time.sleep(8)
        metaobj.verify_filter_pane_field("SALES_REGION and SALES_REGION and COMPANY_NAME", 1, "Step 13")
         
        """
        Step 14: Verify values below 40k of blue column is excluded.
        """
        try:
            driver.find_element_by_css_selector("circle[class='riser!s0!g73!mmarker!r0!c0!']").exists()
            status=True
        except NoSuchElementException:
            status=False
        utillobj.asequal(False, status, "Step 14: Verify whether the selected circles has been excluded from the chart")
        #resultobj.verify_riser_not_displayed('s0!g103!mmarker!r0!c0',"Step 14: verify ",'rowcolumn', type='scatter')
         
        """
        Step 15: Click Run in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(8)
        chart_type_css="circle[class*='riser!s3!g130!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
         
        """
        Step 16: Verify output at runtime.
        """
        time.sleep(5)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody1"),'C2108153_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        expected_xval_list=['0', '10', '20', '30', '40', '50', '60', '70'] 
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16a: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker", "bar_blue", "Step 16.b(i) Verify first column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g290!mmarker", "pale_green", "Step 16.b(ii) Verify second column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g502!mmarker", "dark_green", "Step 16.b(iii) Verify third column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s3!g130!mmarker", "pale_yellow", "Step 16.b(iiii) Verify fourth column circle color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s4!g235!mmarker!", "brick_red", "Step 16.b(iiiii) Verify fifth column circle color")
        xaxis_value="Number of Days Since Contact"
        yaxis_value="Net Sales"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 16:c(ii) Verify Y-Axis Title")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2108153_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        #labels=['Canada', 'Central', 'Eastern', 'Southern', 'Western']
        #resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1_f", "Columns", "Sales Region", labels, "Step 10:d")
         
        try:
            driver.find_element_by_css_selector("circle[class='riser!s0!g73!mmarker!r0!c0!']").exists()
            status=True
        except NoSuchElementException:
            status=False
        utillobj.asequal(False, status, "Step 16x: Verify whether the selected circles has been excluded from the chart")
         
        """
        Step 17: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 18: Click "Save" in the toolbar > Type C2108153 > Click "Save" in the Save As dialog
        """
        time.sleep(2)  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()