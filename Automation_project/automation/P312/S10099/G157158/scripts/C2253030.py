'''
Created on Feb 15, 2018

@author: BM13368
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2253030
TestCase Name :IA-4521:Vis: Show data at run time after Drilldown on 2By fields with sorted measure, show empty values for some measure entries
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253030_TestClass(BaseTestCase):

    def test_C2253030(self):
        
        Test_Case_ID = "C2253030"
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"  
        wait_time_in_sec=120
        visual = visualization.Visualization(self.driver)
        
        """
            Step 1:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
            The signon screen will be displayed.
            Login as userid devuser(autodevuser01/02/03/04/05) and blank password
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """    
            Step 2:Double click "Revenue" and "Customer Business Region".
        """ 
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "Revenue", 45)
        visual.double_click_on_datetree_item('Customer,Business,Region', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "CustomerBusinessRegion", 45)
             
        """ 
            Step 3:Verify labels
        """ 
        no_of_riser=4
        x_axis_title=['Customer Business Region']
        y_axis_title=['Revenue']
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        expected_x_axis_label_list=['EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_x_axis_label(expected_x_axis_label_list, msg="Step 3:1:Verify x-axis label")
        expected_y_axis_label_list=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        visual.verify_y_axis_label(expected_y_axis_label_list, msg="Step 3.2:Verify y-axis label") 
        visual.verify_number_of_risers(total_no_of_riser_css, 1, 4, msg="Step 3.3:Verify number of riser")
        visual.verify_x_axis_title(x_axis_title, msg="Step 3.4: Verify x-axis title")
        visual.verify_y_axis_title(y_axis_title, msg="Step 3.5: Verify y-axis title")
                 
        """ 
            Step 4:Verify each bar riser values (CustomerBusinessRegion: Revenue)
            EMEA:$562,316,133.90
            North America:$444,147,282.83
            Oceania:$2,562,553.72
            South America:$52,166,954.75
        """
        EMEA_riser_css='riser!s0!g0!mbar!'
        EMEA_expected_tooltip=['Customer Business Region:EMEA', 'Revenue:$562,316,133.90', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Sub Region']
        North_America_css='riser!s0!g1!mbar!'
        North_America_tooltip=['Customer Business Region:North America', 'Revenue:$444,147,282.83', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Sub Region']
        Oceania_riser_css='riser!s0!g2!mbar!'
        Oceania_tooltip=['Customer Business Region:Oceania', 'Revenue:$2,562,553.72', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Sub Region']
        South_America_css='riser!s0!g3!mbar!'
        South_America_tooltip=['Customer Business Region:South America', 'Revenue:$52,166,954.75', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Sub Region']
        
        visual.verify_tooltip(EMEA_riser_css, EMEA_expected_tooltip, "Step 4:01:Verify EMEA barriser value")
        visual.verify_tooltip(North_America_css, North_America_tooltip, "Step 4:02:Verify North America value")
        visual.verify_tooltip(Oceania_riser_css, Oceania_tooltip, "Step 4:03:Verify Oceania value")
        visual.verify_tooltip(South_America_css, South_America_tooltip, "Step 4:04:Verify South America value")
        
        """    
            Step 5:Right Click on Revenue in Query Panel and Sort to Descending.
        """
        field_name='Revenue'
        visual.right_click_on_field_under_query_tree(field_name, 1, 'Sort->Sort->Descending')
        no_of_riser=4
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        visual.verify_field_listed_under_querytree('Horizontal Axis', field_name, 1, msg="Step 05:verify Revenue is added underneath Horizontal Axis", color_to_verify='Trolley_Grey', font_to_verify='italic')
        
        """    
            Step 6:Verify revenue values of each bar riser (CustomerBusinessRegion:Revenue )
            EMEA:$562,316,133.90
            North America:$444,147,282.83
            South America:$52,166,954.75
            Oceania:$2,562,553.72
        """
        
        Oceania_tooltip=['Customer Business Region:South America', 'Revenue:$52,166,954.75', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Sub Region']
        South_America_tooltip=['Customer Business Region:Oceania', 'Revenue:$2,562,553.72', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Sub Region']
        visual.verify_tooltip(EMEA_riser_css, EMEA_expected_tooltip, "Step 6:01:Verify EMEA barriser value")
        visual.verify_tooltip(North_America_css, North_America_tooltip, "Step 6:02:Verify EMEA barriser value")
        visual.verify_tooltip(Oceania_riser_css, Oceania_tooltip, "Step 6:03:Verify EMEA barriser value")
        visual.verify_tooltip(South_America_css, South_America_tooltip, "Step 6:04:Verify EMEA barriser value")
        
        """    
            Step 7:Add "Sale Quarter" to Horizontal axis.
        """ 
        field_name='Sale,Quarter'
        no_of_riser=16
        visual.right_click_on_datetree_item(field_name, 1, 'Add To Query->Horizontal Axis')
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        visual.verify_number_of_risers(total_no_of_riser_css, 1, 16, msg="Step 7.01:Verify number of riser")
             
        """ 
            Step 8:Verify query pane
        """ 
        visual.verify_field_listed_under_querytree('Horizontal Axis', field_name, 3, msg="Step 08:")
            
        """   
            Step 9:Verify label values
        """
        no_of_riser=16
        riser='riser!s0!g0!mbar!'
        x_axis_title=['Customer Business Region : Sale Quarter']
        y_axis_title=['Revenue']
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        expected_x_axis_label_list=['EMEA : 4', 'EMEA : 1', 'EMEA : 3', 'North America : 4', 'EMEA : 2', 'North America : 1', 'North America : 3', 'North America : 2', 'South America : 4', 'South America : 1', 'South America : 3', 'South America : 2', 'Oceania : 4', 'Oceania : 1', 'Oceania : 3', 'Oceania : 2']
        visual.verify_x_axis_label(expected_x_axis_label_list, msg="Step 9:1:Verify x-axis label")
        expected_y_axis_label_list=['0', '40M', '80M', '120M', '160M', '200M']
        visual.verify_y_axis_label(expected_y_axis_label_list, msg="Step 9:2:Verify y-axis label") 
        visual.verify_number_of_risers(total_no_of_riser_css, 1, no_of_riser, msg="Step 9.3:Verify number of riser")
        visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step 9.4 : Verify riser color')
        visual.verify_x_axis_title(x_axis_title, msg="Step 9.5: Verify x-axis title")
        visual.verify_y_axis_title(y_axis_title, msg="Step 9.6: Verify y-axis title")  
            
        """ 
            Step 10:Verify first and last 2 bar riser values
            CustomerBusinessRegion:Sale Quarter:Revenue
            First 2 bar values-
            EMEA:4:$165,452,839.61
            EMEA:1:$134,541,453.92
            Last 2 bar values-
            Oceania:3:$637,687.87
            Oceania:2:$594,510.90
        """
        EMEA_riser_css1='riser!s0!g0!mbar!'
        EMEA_expected_tooltip1=['Customer Business Region:EMEA', 'Sale Quarter:4', 'Revenue:$165,452,839.61', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        EMEA_riser_css2='riser!s0!g1!mbar!'
        EMEA_expected_tooltip2=['Customer Business Region:EMEA', 'Sale Quarter:1', 'Revenue:$134,541,453.92', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        Oceania_riser_css1='riser!s0!g14!mbar!'
        Oceania_expected_tooltip1=['Customer Business Region:Oceania', 'Sale Quarter:3', 'Revenue:$637,687.87', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        Oceania_riser_css2='riser!s0!g15!mbar!'
        Oceania_expected_tooltip2=['Customer Business Region:Oceania', 'Sale Quarter:2', 'Revenue:$594,510.90', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        
        visual.verify_tooltip(EMEA_riser_css1, EMEA_expected_tooltip1, "Step 10:01:Verify EMEA barriser value")
        visual.verify_tooltip(EMEA_riser_css2, EMEA_expected_tooltip2, "Step 10:02:Verify EMEA barriser value")
        visual.verify_tooltip(Oceania_riser_css1, Oceania_expected_tooltip1, "Step 10:03:Verify EMEA barriser value")
        visual.verify_tooltip(Oceania_riser_css2, Oceania_expected_tooltip2, "Step 10:04:Verify EMEA barriser value")
        
        """ 
            Step 11:Click Run in the toolbar
        """ 
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        no_of_riser=16
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        riser='riser!s0!g0!mbar!'
        expected_x_axis_label_list=['EMEA : 4', 'EMEA : 1', 'EMEA : 3', 'North America : 4', 'EMEA : 2', 'North America : 1', 'North America : 3', 'North America : 2', 'South America : 4', 'South America : 1', 'South America : 3', 'South America : 2', 'Oceania : 4', 'Oceania : 1', 'Oceania : 3', 'Oceania : 2']
        visual.verify_x_axis_label(expected_x_axis_label_list, msg="Step 11:1:Verify x-axis label")
        expected_y_axis_label_list=['0', '40M', '80M', '120M', '160M', '200M']
        visual.verify_y_axis_label(expected_y_axis_label_list, msg="Step 11:2:Verify y-axis label") 
        visual.verify_number_of_risers(total_no_of_riser_css, 1, no_of_riser, msg="Step 11.3:Verify number of riser")
        visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step' + str('11.4') + ': Verify riser color')
            
        """   
            Step 12:Hover over on any bar(EMEA:2) and choose > Drill up > Sale, Year
        """ 
        riser_tooltip=['Customer Business Region:EMEA', 'Sale Quarter:4', 'Revenue:$165,452,839.61', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        riser_css1='riser!s0!g0!mbar!'
        visual.verify_tooltip(riser_css1, riser_tooltip, "Step 12:01:Verify EMEA value") 
        visual.select_tooltip(riser_css1, 'Drill up to Sale Year')
        no_of_riser=23
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        x_axis_title=['Customer Business Region : Sale Year']
        y_axis_title=['Revenue']
        expected_x_axis_label_list=['EMEA : 2016', 'North America : 2016', 'EMEA : 2015', 'North America : 2015', 'EMEA : 2014', 'EMEA : 2013', 'North America : 2014', 'EMEA : 2012', 'EMEA : 2011', 'North America : 2013', 'South America : 2016', 'North America : 2012', 'North America : 2011', 'South America : 2015', 'South America : 2014', 'South America : 2013', 'South America : 2011', 'South America : 2012', 'Oceania : 2016', 'Oceania : 2015', 'Oceania : 2014', 'Oceania : 2013', 'Oceania : 2012']
        visual.verify_x_axis_label(expected_x_axis_label_list, msg="Step 12:1:Verify x-axis label")
        expected_y_axis_label_list=['0', '40M', '80M', '120M', '160M', '200M']
        visual.verify_y_axis_label(expected_y_axis_label_list, msg="Step 12:2:Verify y-axis label") 
        visual.verify_number_of_risers(total_no_of_riser_css, 1, no_of_riser, msg="Step 12.3:Verify number of riser")
        visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step' + str('12.4') + ': Verify riser color')
        visual.verify_x_axis_title(x_axis_title, msg="Step 12.5: Verify x-axis title")
        visual.verify_y_axis_title(y_axis_title, msg="Step 12.6: Verify y-axis title")
        
        """ 
            Step 13:Hover on a bar riser(NorthAmerica:2014) and verify Sale, Quarter is changed to Sale, Year
        """ 
        riser='riser!s0!g6!mbar!'
        riser_tooltip=['Customer Business Region:North America', 'Sale Year:2014', 'Revenue:$43,907,888.55', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip(riser, riser_tooltip, "Step 13:01:Verify tooltip value")
           
        """ 
            Step 14:Choose show Data from Run menu option (grid icon).
        """ 
        visual.select_bottom_right_run_menu_options('show_report_css')
        wait_time=120
        table_css="#MAINTABLE_wbody0"
        visual.wait_for_number_of_element(table_css, 1, wait_time)
             
        """    
            Step 15:Verify Revenue value of NorthAmerica:2015
            Revenue: $128,662,736.78
        """
#         visual.create_visualization_tabular_report(Test_Case_ID+'_DS_01.xlsx')
        visual.verify_visualization_tabular_report(Test_Case_ID+'_DS_01.xlsx', msg='Step 15.1:')
        
        """
            Step 16:Close the output
        """
        visual.switch_to_previous_window() 
             
        """ 
            Step 17:Click "Save" in the toolbar > Type C2141608 > Click "Save" in the Save As dialog
            Save the fex with the same name as this test case.
        """
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
        """
            Step 18:Logout of the IA API using the following URL. 
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()