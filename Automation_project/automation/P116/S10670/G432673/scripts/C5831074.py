'''
Created on Jan 9, 2019

@author: Vpriya

Testsuite =  http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=432673&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/5831074
TestCase Name = Verify that a Multi-Page Document can be navigated and Filtered.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_chart
# from common.wftools import active_report
from common.wftools import document
from common.wftools import visualization
from common.lib import utillity
import time

class C5831074_TestClass(BaseTestCase):

    def test_C5831074(self):
        
        """
            TESTCASE VARIABLES
        """
        
        Testcase_ID="C5831074"
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        MEDIUM_WAIT=60
        folder_name="P116_S10670/G432673"
        fex_name='Multipage_Dashboard1'
        legend_css="#MAINTABLE_wbody0 text[class*='legend-labels!s1!']"
        legend_css1="#MAINTABLE_wbody2 text[class*='legend-labels!s1!']"
        table_css="table[id='iLayTB$']"
        chart_title='Unit Sales, Dollar Sales by Category, Product'
        expected_x_label=['Coffee/Ca...', 'Coffee/Es...', 'Coffee/Latte', 'Food/Bisc...', 'Food/Croi...', 'Food/Scone', 'Gifts/Coff...', 'Gifts/Coff...', 'Gifts/Mug', 'Gifts/The...']
        expected_y_label=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        expected_legend_list=['Unit Sales', 'Dollar Sales']
        main_chart_title='Global Filter for Multi-page Charts'
        chart_title2="Budget Units, Budget Dollars by Category, Product"
        expected_y_label_1=['0', '3M', '6M', '9M', '12M']
        expected_legend_list_2=['Budget Units', 'Budget Dollars']
        expected_x_axis_title2=['Category : Product']
        chart_title3="Unit Sales by Category"
        expected_label_list3=['Unit Sales']
        expected_legend_list_3=['Coffee', 'Food', 'Gifts']
        expected_x_label_3=['37%', '38%', '25%']
        expected_tooltip_list_1=['6 points', 'Filter Chart', 'Exclude from Chart']
        filter_expected_x_label=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        Filter_expected_tooltip=['1 point', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        filter_legend_list_3=['Food', 'Gifts']
        filter_x_label_3=['60%', '40%']
        filter_expected_x_label1=['Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        filter_y_label=['0', '1M', '2M', '3M', '4M', '5M']
        parent_css_1="#MAINTABLE_wbody0"
        parent_css_2="#MAINTABLE_wbody2"
        parent_css_3="#MAINTABLE_wbody3"
        
        
        def verify_lasso_tooltip_pie(self, expected_tooltip_list, msg='Step X: Verify default Chart tooltip'):
            utill_obj=utillity.UtillityMethods(self.driver)
            tooltip_css="span[id='ibi$tt$3']" 
            raw_tooltip_list=self.driver.find_element_by_css_selector(tooltip_css).text.replace(u'\xa0\n', '').replace(u'\xa0', ' ').split('\n')
            actual_list=utill_obj.get_actual_tooltip_list(raw_tooltip_list)
            utill_obj.asequal(expected_tooltip_list, actual_list, msg)
            
        def verify_page_summary(self,page_num, expected_title, msg):
            import re
            utill_obj=utillity.UtillityMethods(self.driver)
            table_css_img="#MAINTABLE_wbody"+ str(page_num) +" .arGridBar table>tbody"
            utill_obj.synchronize_with_number_of_element(table_css_img, 2,2)
            get_title=self.driver.find_element_by_css_selector(table_css_img).text.strip()
            print(get_title)
            actual_title=re.sub('\s', '', get_title)
            actual_title=re.sub('[^0-9a-zA-z-/, ]','',actual_title)
            utill_obj.asin(expected_title, actual_title, msg)
            
        
        """
        Step 1:Execute the attached Document - Multipage_Dashboard1.
        Expect to see the following Document, Page 1,Page 2
        """
        report_obj.run_fex_using_api_url(folder_name,fex_name,'mrid','mrpass',run_table_css=legend_css,wait_time=MEDIUM_WAIT)
        doc_obj.verify_active_document_page_layout_menu_run_window(table_css,['Layouts','Page 1','Page 2'], "Step01: Verify Multipage_dashboard")
        active_chart_obj.verify_chart_title(chart_title,msg="Step:1.1", parent_css=parent_css_1)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label, parent_css_1, msg="step 1.2")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_label, parent_css_1, msg="step 1.3")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g4!mbar!']", "gold_tips", parent_css="#MAINTABLE_wbody0",msg="step 1.4")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g2!mbar!']", "cerulean_blue", parent_css="#MAINTABLE_wbody0",msg="step 1.5")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#MAINTABLE_wbody0", legend_length=2, msg="Step:1.6")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 1.6', parent_css='#MAINTABLE_wmenu0')
        active_chart_obj.verify_chart_title(main_chart_title,msg="Step:1.7", parent_css='div[id*="LOBJText_"]')
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title2, parent_css="#MAINTABLE_wbody0",msg="Step:1.8")
        
        "report verification"
        #report_obj.create_table_data_set("#IWindowBody1", Testcase_ID+".xlsx")
        report_obj.verify_table_data_set("#IWindowBody1", Testcase_ID+".xlsx", msg="Step1.9")
        verify_page_summary(self,1,"10of10records,Page1of1",msg="Step 1.10 verify page summary")
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        active_chart_obj.wait_for_number_of_element(legend_css1, 1, MEDIUM_WAIT)
        
        """ verification for page 2"""
        active_chart_obj.verify_chart_title(chart_title2,msg="Step:1.11", parent_css=parent_css_2)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label, parent_css_2, msg="step 1.12")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_label_1, parent_css_2, msg="step 1.13")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g4!mbar!']", "gold_tips", parent_css="#MAINTABLE_wbody2",msg="step 1.14")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g2!mbar!']", "cerulean_blue", parent_css="#MAINTABLE_wbody2",msg="step 1.15")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list_2, parent_css="#MAINTABLE_wbody2", legend_length=2, msg="Step:1.16")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 1.17', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title2, parent_css="#MAINTABLE_wbody2",msg="Step:1.18")
        
        """ report verification"""
        
        #report_obj.create_table_data_set("#IWindowBody4", Testcase_ID+"_1.xlsx")
        report_obj.verify_table_data_set("#IWindowBody4", Testcase_ID+"_1.xlsx", msg="Step1.19")
        verify_page_summary(self,4,"11of11records,Page1of1",msg="Step 1.20 verify page summary")
        
        """ pie chart verification in Page 2"""
        
        active_chart_obj.verify_chart_title(chart_title3,msg="Step:1.20", parent_css=parent_css_3)
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list3, parent_css_3,msg="Step 1.21")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody3', 1, 6, msg="Step 1.22")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list_3, parent_css="#MAINTABLE_wbody3", legend_length=3, msg="Step:1.23")
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label_3, parent_css_3,xyz_axis_label_css="[class*='dataLabels!']",msg="step 1.24")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 1.25', parent_css='#MAINTABLE_wmenu3')
        
        """
        Step:2 From Page 1, select all three sets of Bars representing Category - FOOD.
        Expect to see the Filter selection pane.
        """
        
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        active_chart_obj.wait_for_number_of_element(legend_css, 1, MEDIUM_WAIT)
        source_css="rect[class='riser!s0!g3!mbar!']"
        source_element=utill_obj.validate_and_get_webdriver_object(source_css, "riser_css")
        target_css="rect[class='riser!s1!g5!mbar!']"
        target_element=utill_obj.validate_and_get_webdriver_object(target_css, "riser_css")
        vis_obj.create_lasso(source_element, target_element)
        vis_obj.verify_lasso_tooltip(expected_tooltip_list_1, msg="Step:2.1")
        
        """
        Step:3 Click the Exclude from Chart button.
        Expect to see the following filtered Bar Chart and Report on Page 1.
        Also notice that the Filter icon appears with the Bar Chart.
        """
        
        vis_obj.select_lasso_tooltip("Exclude from Chart")
        
        """page 1 chart verification"""
        
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 22, parent_css="#MAINTABLE_wbody0", msg="Step:3.1")
        active_chart_obj.verify_x_axis_label_in_run_window(filter_expected_x_label, parent_css_1, msg="step 3.2")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_label, parent_css_1, msg="step 3.3")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g4!mbar!']", "gold_tips", parent_css="#MAINTABLE_wbody0",msg="step 3.4")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g2!mbar!']", "cerulean_blue", parent_css="#MAINTABLE_wbody0",msg="step 3.5")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#MAINTABLE_wbody0", legend_length=2, msg="Step:3.6")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 3.7', parent_css='#MAINTABLE_wmenu0')
        active_chart_obj.verify_chart_title(main_chart_title,msg="Step:3.8", parent_css='div[id*="LOBJText_"]')
        filter_css="#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']"
        utill_obj.verify_object_visible(filter_css,True,msg="Step:3.9")
        
        """ Report verification"""
        
        #report_obj.create_table_data_set("#IWindowBody1", Testcase_ID+"_2.xlsx")
        report_obj.verify_table_data_set("#IWindowBody1", Testcase_ID+"_2.xlsx", msg="Step:3.10")
        verify_page_summary(self,1,"10of10records,Page1of1",msg="Step:3.11 verify page summary")
        
        
        """
        Step:4 Select Page 2 from the Layout menu at the top of the Dashboard.
        Expect to see the following filtered Bar Chart, PIE and Report on Page 2.
        There is no effect on the Report component because it does not contain Category, to be Filtered on.
        Also notice that there is no Filter icon present, it is attached to the Bar Chart on Page 1.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        active_chart_obj.wait_for_number_of_element(legend_css1, 1, MEDIUM_WAIT)
        
        "chart verification"
        active_chart_obj.verify_chart_title(chart_title2,msg="Step:4.1", parent_css=parent_css_2)
        active_chart_obj.verify_x_axis_label_in_run_window(filter_expected_x_label, parent_css_2, msg="step 4.2")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_label_1, parent_css_2, msg="step 4.3")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g4!mbar!']", "gold_tips", parent_css="#MAINTABLE_wbody2",msg="step 4.4")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g2!mbar!']", "cerulean_blue", parent_css="#MAINTABLE_wbody2",msg="step 4.5")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list_2, parent_css="#MAINTABLE_wbody2", legend_length=2, msg="Step:4.6")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 4.7', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title2, parent_css="#MAINTABLE_wbody2",msg="Step:4.8")
        filter_css1="#MAINTABLE_2 .arChartMenuBar div[title][onclick*='Filter']"
        utill_obj.verify_object_visible(filter_css1,True,msg="Step:4.9")
        
        """report verification"""
        report_obj.verify_table_data_set("#IWindowBody4", Testcase_ID+"_1.xlsx", msg="Step:4.10")
        verify_page_summary(self,4,"11of11records,Page1of1",msg="Step 4.11:verify page summary")
        
        """pie chart verifcation"""
        
        active_chart_obj.verify_chart_title(chart_title3,msg="Step:4.11", parent_css=parent_css_3)
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list3, parent_css_3,msg="Step 4.12")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody3', 1, 6, msg="Step 4.13")
        
        active_chart_obj.verify_legends_in_run_window(expected_legend_list_3, parent_css="#MAINTABLE_wbody3", legend_length=3, msg="Step:4.14")
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label_3, parent_css_3,xyz_axis_label_css="[class*='dataLabels!']",msg="step 4.15")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 4.16', parent_css='#MAINTABLE_wmenu3')
        filter_css3="#MAINTABLE_2 .arChartMenuBar div[title][onclick*='Filter']"
        utill_obj.verify_object_visible(filter_css3,True,msg="Step:4.17")
        
        
        """
        Step:5 From the PIE chart on Page 2, click the slice for COFFEE.
        Expect to see the following Filter menu.
        """
        source_css="path[class='riser!s0!g0!mwedge!']"
        source_element=utill_obj.validate_and_get_webdriver_object(source_css, "riser_css")
        target_css="path[class='riser!s0!g0!mwedge!']"
        target_element=utill_obj.validate_and_get_webdriver_object(target_css, "riser_css")
        vis_obj.create_lasso(source_element, target_element)
        verify_lasso_tooltip_pie(self,Filter_expected_tooltip, msg="Step:5.1")
        
        """
        Step:6 Click Exclude from Chart.
        Expect to see this additional Filter applied to the Bar Chart and PIE chart, in addition to the Filter applied in step 3. Now only Category FOOD and GIFTS should remain on pie chart in Page 2.
        """
        vis_obj.select_lasso_tooltip("Exclude from Chart")
        
        "Pie chart verification"
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step:6.1', parent_css='#MAINTABLE_wmenu3')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list3, parent_css_3,msg="Step 6.2")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody3', 1, 4, msg="Step 6.3")
        active_chart_obj.verify_legends_in_run_window(filter_legend_list_3, parent_css="#MAINTABLE_wbody3", legend_length=3, msg="Step:6.4")
        active_chart_obj.verify_x_axis_label_in_run_window(filter_x_label_3, parent_css_3,xyz_axis_label_css="[class*='dataLabels!']",msg="step 6.5")
        filter_css3="#MAINTABLE_3 .arChartMenuBar div[title][onclick*='Filter']"
        utill_obj.verify_object_visible(filter_css3,True,msg="Step:6.7")
        
        """Chart Verification"""
        
        active_chart_obj.verify_chart_title(chart_title2,msg="Step:6.8", parent_css=parent_css_2)
        active_chart_obj.verify_x_axis_label_in_run_window(filter_expected_x_label1, parent_css_2, msg="step 6.9")
        active_chart_obj.verify_y_axis_label_in_run_window(filter_y_label, parent_css_2, msg="step 6.10")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list_2, parent_css="#MAINTABLE_wbody2", legend_length=2, msg="Step:6.11")
        filter_css2="#MAINTABLE_2 .arChartMenuBar div[title][onclick*='Filter']"
        utill_obj.verify_object_visible(filter_css2,True,msg="Step:6.12")
        
        """ Report verification"""
        
        report_obj.verify_table_data_set("#IWindowBody4", Testcase_ID+"_1.xlsx", msg="Step:6.12")
        verify_page_summary(self,4,"11of11records,Page1of1",msg="Step 6.13 verify page summary")
        
        
        """
        Step:7 Select Page 1 from the Layout menu.
        Expect to see the additional filtering also applied to Page 1, with only GIFTS remaining.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        active_chart_obj.wait_for_number_of_element(legend_css, 1, MEDIUM_WAIT)
        
        """Chart verification"""
        
        active_chart_obj.verify_x_axis_label_in_run_window(filter_expected_x_label1, parent_css_1, msg="step 7.1")
        active_chart_obj.verify_y_axis_label_in_run_window(filter_y_label, parent_css_1, msg="step 7.2")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#MAINTABLE_wbody0", legend_length=2, msg="Step:7.3")
        filter_css1="#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']"
        utill_obj.verify_object_visible(filter_css1,True,msg="Step:7.4")
        
        """report verification"""
        
        #report_obj.create_table_data_set("#IWindowBody1", Testcase_ID+"_3.xlsx")
        report_obj.verify_table_data_set("#IWindowBody1", Testcase_ID+"_3.xlsx", msg="Step:7.5")
        verify_page_summary(self,1,"7of10records,Page1of1",msg="Step:7.6:verify page summary")
        
        
        """
        Step:8 Now remove the Filter on Page 1, by clicking on the Filter icon in the Bar Chart.
        Expect to see Coffee and FOOD added back into the Bar Chart
        Also expect to see the Filter icon removed from the Bar Chart.
        """
        filter_css1="#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']"
        utill_obj.validate_and_get_webdriver_object(filter_css1,"Filter_icon").click()
        time.sleep(2)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label, parent_css_1, msg="step:8.1")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_label, parent_css_1, msg="step:8.2")
        utill_obj.verify_object_visible(filter_css1,False,"Step:8.3")
        
        """Report verification"""
    
        report_obj.verify_table_data_set("#IWindowBody1", Testcase_ID+".xlsx", msg="Step:8.4")
        verify_page_summary(self,1,"10of10records,Page1of1",msg="Step:8.5verify page summary")
        
        """
        Step 9:Select Page 2 from the Layout menu.
        Expect to see all three slices ]in the PIE chart and all Category bars return.
        This will return the Dashboard to its original appearance for Page 2.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        active_chart_obj.wait_for_number_of_element(legend_css1, 1, MEDIUM_WAIT)
        
        """ verification for page 2"""
        active_chart_obj.verify_chart_title(chart_title2,msg="Step:9.1", parent_css=parent_css_2)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label, parent_css_2, msg="step:9.2 ")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_label_1, parent_css_2, msg="step:9.3")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g4!mbar!']", "gold_tips", parent_css="#MAINTABLE_wbody2",msg="step:9.4")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g2!mbar!']", "cerulean_blue", parent_css="#MAINTABLE_wbody2",msg="step:9.5")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list_2, parent_css="#MAINTABLE_wbody2", legend_length=2, msg="Step:9.6")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step:9.7', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title2, parent_css="#MAINTABLE_wbody2",msg="Step:9.8")
        
        """ report verification"""
        
        report_obj.verify_table_data_set("#IWindowBody4", Testcase_ID+"_1.xlsx", msg="Step9.9")
        verify_page_summary(self,4,"11of11records,Page1of1",msg="Step 9.9.1 verify page summary")
        
        """ pie chart verification in Page 2"""
        
        active_chart_obj.verify_chart_title(chart_title3,msg="Step:9.10", parent_css=parent_css_3)
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list3, parent_css_3,msg="Step 9.11")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody3', 1, 6, msg="Step 1.22")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list_3, parent_css="#MAINTABLE_wbody3", legend_length=3, msg="Step:9.12")
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label_3, parent_css_3,xyz_axis_label_css="[class*='dataLabels!']",msg="step:9.13")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step:9.14', parent_css='#MAINTABLE_wmenu3')
        
        """
        Step 10:Select Page 1 from the Layout menu.
        Expect to see the original content of Page 1.
        """
        
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        active_chart_obj.wait_for_number_of_element(legend_css, 1, MEDIUM_WAIT)
        
        doc_obj.verify_active_document_page_layout_menu_run_window(table_css,['Layouts','Page 1','Page 2'], "Step 10: Verify Multipage_dashboard")
        active_chart_obj.verify_chart_title(chart_title,msg="Step:10.1", parent_css=parent_css_1)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_label, parent_css_1, msg="step 10.2")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_label, parent_css_1, msg="step 10.3")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g4!mbar!']", "gold_tips", parent_css="#MAINTABLE_wbody0",msg="step 10.4")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g2!mbar!']", "cerulean_blue", parent_css="#MAINTABLE_wbody0",msg="step 10.5")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#MAINTABLE_wbody0", legend_length=2, msg="Step:10.6")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 10.7', parent_css='#MAINTABLE_wmenu0')
        active_chart_obj.verify_chart_title(main_chart_title,msg="Step:10.8", parent_css='div[id*="LOBJText_"]')
        active_chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title2, parent_css="#MAINTABLE_wbody0",msg="Step:10.9")
        
        "report verification"
        
        report_obj.verify_table_data_set("#IWindowBody1", Testcase_ID+".xlsx", msg="Step10.10")
        verify_page_summary(self,1,"10of10records,Page1of1",msg="Step:10.10 verify page summary")


if __name__ == '__main__':
    unittest.main()