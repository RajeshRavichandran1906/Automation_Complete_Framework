'''
Created on Jul 11, 2017
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.lib.utillity import UtillityMethods

class C2205006_TestClass(BaseTestCase):

    def test_C2205006(self):
        """
        TESTCASE VARIABLES
        """
        Fex_ID = 'Chart-AHTML'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        def verify_checkpoints(ostep):
            result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['11%', '5%', '5%', '5%', '17%', '8%', '24%', '10%', '9%', '5%', 'Unit Sales'], ostep,custom_css=" text[class*='Label']",same_group=True)
            expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
            result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, ostep+' Verify pie lablesList')
            utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g0!mwedge!", "oslo_gray", ostep+" Verify Pie segment color")
            result_obj.verify_number_of_pie_segments('MAINTABLE_wbody0', 2, 10, ostep+" Verify number of pie segments")
            miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Product', ostep+' Verify Chart Title')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],ostep+" Verify Chart toolbar")
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],ostep+" Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],ostep+" Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """    1. Right click on folder created in IA and select New > Chart. Select Reporting server as GGSALES. On the Format tab, in the Output Types group, click Active report/Active PDF.    """
        utillobj.infoassist_api_edit(Fex_ID, "chart", "P116/S7074", mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 g.chartPanel g text", 3, 65)
        
        """    Expect to see the following Active PIE chart preview pane. The default Legend position is Bottom Center.    """
        result_obj.verify_riser_pie_labels_and_legends('TableChart_1', ['Unit Sales'], "Step 01.00:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 01.01: Verify pie labels List')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mwedge!", "gold_tips", "Step 01.02: Verify first bar color")
        result_obj.verify_number_of_pie_segments('TableChart_1', 2, 2, "Step 01.03: Verify number of pie segments")
        x=driver.find_element_by_css_selector("#TableChart_1 g.legend").get_attribute('transform')
        x1=x.strip("abcdefghijklmnopqrstuvwxyz()=,")
        br = UtillityMethods.parseinitfile(self,'browser')
        if br=='IE':
            x1=x1.split(' ')
        else:
            x1=x1.split(',')
           
        print(x1)
        left=int(x1[0])
        top=int(x1[1])
        if left in range(510,610) and top in range(610,710):
            utillobj.asequal(True, True, "Step 01.04. Verify the default Legend position is Bottom Center")
        else:
            utillobj.asequal(True, False, "Step 01.04. Verify the default Legend position is Bottom Center")
         
        """    2. Click the Run button.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 15)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 g.chartPanel g text", 11, 15)
        utillobj.wait_for_page_loads(result_obj.chart_long_timesleep)
        verify_checkpoints("Step 02.00:")
        x=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.legend").get_attribute('transform')
        x1=x.strip("abcdefghijklmnopqrstuvwxyz()=,")
        print(x1)
        left=int(x1[:3])
        top=int(x1[4:])
        if left in range(100,200) and top in range(575,710):
            utillobj.asequal(True, True, "Step 02.01. Verify the default Legend position is Bottom Center")
        else:
            utillobj.asequal(True, False, "Step 02.01. Verify the default Legend position is Bottom Center")
        utillobj.switch_to_default_content(pause=5)
        time.sleep(2)
        
        """    3. Click the Format tab, then Labels, then Legend.Select Legend Position of Right.    """
        ribbonobj.switch_ia_tab('Format')
        if driver.find_element_by_css_selector("#FormatChartLegend img").is_displayed()==False:
            elem=utillobj.validate_and_get_webdriver_object("#chartLabels_altButton img", "Legend Button")
            utillobj.default_click(elem)
        ribbonobj.select_ribbon_item('Format', 'Legend', opt='Legend Position')
        utillobj.select_or_verify_bipop_menu('Right')
        utillobj.synchronize_with_visble_text("#TableChart_1 svg > g text[class*='pieLabel']", "UnitSales", 25)
        result_obj.verify_riser_pie_labels_and_legends('TableChart_1', ['Unit Sales'], "Step 03.00:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03.01: Verify pie labels List')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mwedge!", "gold_tips", "Step 03.02: Verify first bar color")
        result_obj.verify_number_of_pie_segments('TableChart_1', 2, 2, "Step 03.03: Verify number of pie segments")
        x=driver.find_element_by_css_selector("#TableChart_1 g.legend").get_attribute('transform')
        x1=x.strip("abcdefghijklmnopqrstuvwxyz()=,")
         
        br = UtillityMethods.parseinitfile(self,'browser')
        if br=='IE':
            x1=x1.split(' ')
        else:
            x1=x1.split(',')
           
        print(x1)
        left=int(x1[0])
        top=int(x1[1])
        if left in range(1150,1250) and top in range(300,400):
            utillobj.asequal(True, True, "Step 03.04. Verify the Legend position set as Right")
        else:
            utillobj.asequal(True, False, "Step 03.04. Verify the Legend position set as Right")
             
        """    4. Click the Run button.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 25)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 g.chartPanel g text", 11, 25)
        utillobj.wait_for_page_loads(result_obj.chart_long_timesleep)
        verify_checkpoints("Step 04.00:")
        x=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.legend").get_attribute('transform')
        x1=x.strip("abcdefghijklmnopqrstuvwxyz()=,")
        if br=='IE':
            x1=x1.split(' ')
        else:
            x1=x1.split(',')
         
        left=int(x1[0])
        top=int(x1[1])
        if left in range(1120,1220) and top in range(200,300):
            utillobj.asequal(True, True, "Step 04.01: Verify the default Legend position is Bottom Center")
        else:
            utillobj.asequal(True, False, "Step 04.01: Verify the default Legend position is Bottom Center")
        utillobj.switch_to_default_content(pause=5)
        time.sleep(2)
        
        br = UtillityMethods.parseinitfile(self,'browser')
        legends_positions=['Left', 'Top', 'Right bottom', 'Right top', 'Left bottom', 'Bottom right' ,'Top right', 'Bottom left', 'Top left']
        legends_XY_positions=[[5,231], [127,6], [1150,450], [1150, 6], [5,450], [240, 623], [240,6], [5,620], [5,6]]
        
        """    5. Click the Format tab, then Labels, then Legend. Select Legend Position of Left. Click the Run button.    """
        """    6. Click the Format tab, then Labels, then Legend. Select Legend Position of Top. Click the Run button.    """
        """    7. Click the Format tab, then Labels, then Legend. Select Legend Position of Right Bottom. Click the Run button.    """
        """    8. Click the Format tab, then Labels, then Legend. Select Legend Position of Top Right. Click the Run button.    """
        """    9. Click the Format tab, then Labels, then Legend. Select Legend Position of Left Bottom. Click the Run button.    """
        """    10. Click the Format tab, then Labels, then Legend. Select Legend Position of Bottom Right. Click the Run button.    """
        """    11. Click the Format tab, then Labels, then Legend. Select Legend Position of Top Right. Click the Run button.    """
        """    12. Click the Format tab, then Labels, then Legend. Select Legend Position of Bottom Left. Click the Run button.    """
        """    13. Click the Format tab, then Labels, then Legend. Select Legend Position of Top Left. Click the Run button.    """
        for i in range(9):
            ribbonobj.select_ribbon_item('Format', 'Legend', opt='Legend Position')
            utillobj.select_or_verify_bipop_menu(legends_positions[i])
            time.sleep(15)
            ribbonobj.select_top_toolbar_item('toolbar_run')
            utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 25)
            utillobj.switch_to_frame(pause=2)
            utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 g.chartPanel g text", 11, 25)
            verify_checkpoints("Step "+str(i+5)+":")
            x=driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.legend").get_attribute('transform')
            x1=x.strip("abcdefghijklmnopqrstuvwxyz()=,")
            if br=='IE':
                x1=x1.split(' ')
            else:      
                x1=x1.split(',')
                
            left=int(x1[0])
            top=int(x1[1])
            left_range=legends_XY_positions[i][0]
            top_range=legends_XY_positions[i][1]
            if left in range(left_range-50,left_range+50) and top in range(top_range-50,top_range+50):
                utillobj.asequal(True, True, "Step "+str(i+5)+"a: Verify the default Legend position is "+legends_positions[i])
            else:
                utillobj.asequal(True, False, "Step "+str(i+5)+"a: Verify the default Legend position is "+legends_positions[i])
            utillobj.switch_to_default_content(pause=5)
            time.sleep(2)
                    
if __name__ == '__main__':
    unittest.main()