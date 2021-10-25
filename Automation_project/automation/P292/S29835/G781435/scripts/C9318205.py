"""-------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 11-September-2019
-------------------------------------------------------------"""
from common.wftools.designer_chart import Designer_Chart
from common.lib.basetestcase import BaseTestCase

class C9318205_TestClass(BaseTestCase):
    
    def test_C9318205(self):
        
        """
            CLASS OBJECTS
        """
        designer_chart = Designer_Chart(self.driver)
        
        """
            VARIABLES
        """
        preview_chart_css = "[id*='chartpreview']"
        
        """
            STEP 01 : Create new chart with employee using API
            http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2F&master=ibisamp%2Femployee&tool=chart
        """
        designer_chart.invoke_designer_chart_using_api("ibisamp/employee")
        designer_chart.wait_for_visible_text(preview_chart_css, "Group", designer_chart.chart_long_timesleep)
        
        """
            STEP 02 : Drag EMP_ID to color bucket
        """
        designer_chart.drag_dimension_field_to_query_bucket("EMP_ID", "Color")
        designer_chart.wait_for_visible_text(preview_chart_css, "EMP_ID", designer_chart.chart_short_timesleep)
        
        """
            STEP 02 - Expected : Verify preview
        """
        legends = ['EMP_ID', '071382660', '112847612', '117593129', '119265415', '119329144', '123764317', '126724188', '219984371', '326179357', '451123478', '543729165', '818692173']
        designer_chart.verify_number_of_risers(preview_chart_css + " rect", 1, 12, "Step 02.01")
        designer_chart.verify_legends_in_preview(legends, msg="Step 02.02")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "bar_blue", msg="Step 02.03 ")
        
        """
            STEP 03 : Change chart type to Scatter
        """
        designer_chart.select_chart_from_chart_picker("scatter_bubble")
        
        """
            STEP 03 - Expected : Verify preview
        """
        legends = ['EMP_ID', '071382660', '112847612', '117593129', '119265415', '119329144', '123764317', '126724188', '219984371', '326179357', '451123478', '543729165', '818692173']
        designer_chart.verify_number_of_risers(preview_chart_css + " circle", 1, 12, "Step 03.01")
        designer_chart.verify_legends_in_preview(legends, msg="Step 03.02")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("circle[class='riser!s11!g0!mmarker!']", "tequila", msg="Step 03.03 ")
        
        """
            STEP 04 : Drag EMP_ID from color to Detail bucket
        """
        designer_chart.drag_query_bucket_field_to_another_query_bucket('Color', 'EMP_ID', 'Detail')
        
        """
            STEP 04 - Expected : Verify preview
        """
        designer_chart.verify_number_of_risers(preview_chart_css + " circle", 1, 12, "Step 04.01")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("circle[class='riser!s0!g11!mmarker!']", "bar_blue", msg="Step 04.02 ")
        
        """
            STEP 05 : Logout using API
        """