'''
Created on Feb 15, 2018

@author: BM13368
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2253029
TestCase Name :A-4719:Vis:Drill up on filtered values with "Not Equal To" operator resets the filter to All
'''
import unittest,time
from common.wftools import visualization
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData

class C2253029_TestClass(BaseTestCase):

    def test_C2253029(self):
        
        """
            VARIABLES
        """
        Test_Case_ID = "C2253029"
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"  
        wait_time_in_sec=120
        color_riser='riser!s0!g5!mbar!'
        
        """
            CLASS & OBJECTS
        """
        visual = visualization.Visualization(self.driver)
        utils = UtillityMethods(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,total_risers,step_num, xyz_axis_label_length=None):
            visual.verify_x_axis_title(x_title, msg='Step ' + str(step_num) + '.01:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step ' + str(step_num) + '.02:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, xyz_axis_label_length=xyz_axis_label_length, msg='Step ' + str(step_num) + '.03'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + str(step_num) + '.04'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + str(step_num) + '.05: Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+color_riser+"']", 'bar_blue',  msg='Step ' + str(step_num) + '.06: Verify riser color')
#             visual.verify_tooltip(riser,tooltip,msg='Step ' + str(step_num) + '.7: Verify riser tooltip')
        
        """
            Step 1:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
            The signon screen will be displayed.
            Login as userid devuser(autodevuser01/02/03/04/05) and blank password
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """    
            Step 2:Double click "Revenue" and "Customer,Country".
            Verify horizontal and vertical axis labels:
        """ 
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "Revenue", 45)
        visual.double_click_on_datetree_item('Customer,Country', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "CustomerCountry", 45)
            
        no_of_riser=42
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)  
        expected_xaxis_labels=['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Tunisia', 'Turkey', 'United Kingdom', 'United States']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
#         argentina_riser='riser!s0!g0!mbar!'
#         argentina_tooltip=['Customer Country:Argentina', 'Revenue:$5,291,947.92', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
        verify_bar_chart(['Customer Country'],['Revenue'],expected_xaxis_labels,expected_yaxis_labels,no_of_riser, '02') 
            
        """ 
            Step 3:Hover over United States bar.
            Verify the tool tip:
        """
        USA_riser='riser!s0!g41!mbar!'
        USA_tooltip_value=['Customer Country:United States', 'Revenue:$333,514,945.66', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
        visual.verify_tooltip(USA_riser, USA_tooltip_value, "Step 03:01: Verify USA tooltip values")
        
        """
            Step 4:Add Customer Country to Filters
        """
        field_name='Customer,Country'
        field_position=1
        CoreMetaData.collapse_data_field_section(self, 'Filters and Variables', False)
        visual.drag_and_drop_from_data_tree_to_filter(field_name, field_position)
        visual.wait_for_number_of_element("#avFilterOkBtn", 1, time_out=120)
        
        """  
            Step 5:Uncheck "All" check box and Select Operator as "Not equal to" and Select "United States" check box.
            Click OK.
            Verify query added to filter
        """
        visual.select_filter_operator_combobox('alpha','Not equal to')
        item_list=['[All]','United States']
        visual.select_filter_field_values(item_list, Ok_button=True)
        time.sleep(3)
        visual.verify_prompt_title(field_name)
        visual.verify_field_in_filterbox('Customer,Country', 1, msg="Step 05.01:Verify Customer, Country is added underneath Filter box")
        
        """ 
            Step 6:Verify United States value is removed.
        """
        x_axis_label=['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Tunisia', 'Turkey', 'United Kingdom']
        utils.wait_for_page_loads(15)
        visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=4, msg="Step 06.01:Verify United States Value is removed") 
        
        """ 
            Step 7:Hover on "Italy" and select drill down to Customer State Province
            Verify axis labels
        """
        to_move_location_element='riser!s0!g20!mbar!'
        menu_path='Drill down to Customer State Province'
        visual.select_tooltip(to_move_location_element, menu_path)
        no_of_riser=18
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        expected_x_axis_label_list=['Abruzzi', 'Calabria', 'Campania', 'Emilia-Romagna', 'Friuli-Venezia Giulia', 'Lazio', 'Liguria', 'Lombardia', 'Marche', 'Piemonte', 'Puglia', 'Sardegna', 'Sicilia', 'Toscana', 'Trentino-Alto Adige', 'Umbria', "Valle D'Aosta", 'Veneto']
        expected_y_axis_label_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '45M']
        verify_bar_chart(['Customer State Province'],['Revenue'],expected_x_axis_label_list,expected_y_axis_label_list,no_of_riser,'07',  xyz_axis_label_length=4)
        
        """    
            Step 8:Hover on Emilia-Romania and verify tooltip
        """
        Emilia_Romania_tooltip_value=['Customer State Province:Emilia-Romagna', 'Revenue:$41,881,864.93', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Country', 'Drill down to Customer City']
        Emilia_Romania_riser='riser!s0!g3!mbar!'
        visual.verify_tooltip(Emilia_Romania_riser, Emilia_Romania_tooltip_value,"Ste 08.01:Verify tooltip")
        
        """ 
            Step 9:Hover on "Lazio" bar and Select "Drill up to Customer Country".
        """
        menu_path='Drill up to Customer Country'
        riser_css='riser!s0!g5!mbar'
        visual.select_tooltip(riser_css, menu_path)
                        
        """  
        Verify Filter prompt value
        """
        utils.wait_for_page_loads(15)
        no_of_riser=32
#         visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        expected_items_list=['[All]', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Tunisia', 'Turkey', 'United Kingdom', 'United States']
        visual.verify_show_prompt_table_list(expected_items_list, msg="Step 09.00: Verify show prompt values")
        
        """ 
            Verify preview display united state values
            Zavalkov, Nicholas added a comment - 31/Aug/16 6:20 PM
            The current behavior is acceptable.
            After we drill up we remove ALL filters and the user is presented with All option.
            The user can then reapply the filter.
            Please make sure the behavior is the same for both preview and runtime.
            Thank you.
        """
        no_of_riser=42
        utils.wait_for_page_loads(15)
        expected_x_axis_label_list=['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Tunisia', 'Turkey', 'United Kingdom', 'United States']
        expected_y_axis_label_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        verify_bar_chart(['Customer Country'],['Revenue'],expected_x_axis_label_list,expected_y_axis_label_list,no_of_riser, '09')
        
        """    
            Step 10:Click Run in the toolbar
            Verify output
        """
        visual.run_visualization_from_toptoolbar()
        utils.wait_for_page_loads(15)
        visual.switch_to_new_window()
        no_of_riser=42

        expected_xaxis_labels=['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Tunisia', 'Turkey', 'United Kingdom', 'United States']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        verify_bar_chart(['Customer Country'],['Revenue'],expected_xaxis_labels,expected_yaxis_labels,no_of_riser, '10')
        expected_items_list=['[All]', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia', 'Czech Republic', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malaysia', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Tunisia', 'Turkey', 'United Kingdom', 'United States']
        visual.verify_show_prompt_table_list(expected_items_list, parent_prompt_css="#PROMPT_1_cs", msg="Step 10.07:Verify show prompt values")
        
        """  
            Step 11:Close the output window
        """
        visual.switch_to_previous_window()
        
        """  
            Step 12:Click "Save" in the toolbar > Type C2141383 > Click "Save" in the Save As dialog
            Save the fex with the same name as this test case.
        """
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
        """   
            Step 13:Logout of the IA API using the following URL. 
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == "__main__":
    unittest.main()