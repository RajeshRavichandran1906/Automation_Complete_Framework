'''
Created on AUG 02, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204939
TestCase Name = Creating a customizable Heading Area With Controls within a multi-component Dashboard
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_run,ia_resultarea
from common.lib import utillity
from common.lib.utillity import UtillityMethods


class C2204939_TestClass(BaseTestCase):

    def test_C2204939(self):
        
        Test_Case_ID="C2204939"
        """
            TESTCASE VARIABLES
        """   
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj = ia_run.IA_Run(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        br1 = UtillityMethods.parseinitfile(self,'browser')
        """ 
             Step 01:Execute the revised repro C46039a.fex.
                    This version uses ARICONSET = WHITE.
        """
        utillobj.active_run_fex_api_login("C46039a.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 02: verification for layout 1
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 02.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 02.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 03:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 03.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 03.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 02.5: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 03.3: C46039a.fex data verification")
        """
            Step 04:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 04.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 04.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 04.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 04.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 04.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 04.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 04.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 05: Funtions for verify archartmenubar color and  background color
        """
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.1:Verify More Options color',custom_css=".arChartMenuBar div[title='More Options'] img", attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.2:Verify Column color',custom_css=".arChartMenuBar div[title='Column'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.3:Verify Pie color',custom_css=".arChartMenuBar div[title='Pie'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.4:Verify Line color',custom_css=".arChartMenuBar div[title='Line'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.5:Verify Scatter color',custom_css=".arChartMenuBar div[title='Scatter'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.6:Verify Advanced Chart color',custom_css=".arChartMenuBar div[title='Advanced Chart'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.7:Verify Original Chart color',custom_css=".arChartMenuBar div[title='Original Chart'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 05.8:Verify sammation color',custom_css=".arChartMenuBarContainer .tabPagingText1 td[title] img",attribute_type='color')
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 05.9:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 05.10:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 05.11:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        time.sleep(2)
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        driver.find_element_by_css_selector(select_css).click()
        time.sleep(5)
        """
            Step 06: verification for layout 2
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 06.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 06.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 07:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 07.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 07.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(3,'9of39records,Page1of1', 'Step 07.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData3']", Test_Case_ID+"_Ds03.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData3']", Test_Case_ID+'_Ds03.xlsx',"Step 07.3: C46039a.fex data verification")
        """
            Step 08:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 08.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 08.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 08.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 08.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 08.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 08.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 08.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 09: Funtions for verify archartmenubar color and  background color
        """
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.1:Verify More Options color',custom_css=".arChartMenuBar div[title='More Options'] img", attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.2:Verify Column color',custom_css=".arChartMenuBar div[title='Column'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.3:Verify Pie color',custom_css=".arChartMenuBar div[title='Pie'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.4:Verify Line color',custom_css=".arChartMenuBar div[title='Line'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.5:Verify Scatter color',custom_css=".arChartMenuBar div[title='Scatter'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.6:Verify Advanced Chart color',custom_css=".arChartMenuBar div[title='Advanced Chart'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.7:Verify Original Chart color',custom_css=".arChartMenuBar div[title='Original Chart'] img",attribute_type='color')
        utillobj.verify_chart_color('MAINTABLE_wmenu1',None, 'white', 'Step 09.8:Verify sammation color',custom_css=".arChartMenuBarContainer .tabPagingText1 td[title] img",attribute_type='color')
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 09.9:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 09.10:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'cyan', 'Step 09.11:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        time.sleep(2)
        """
            Step 10:Hover to the right of Dollar Sales in the upper left 4 line report until the 'hand' symbol occurs.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        fieldmenu.click()
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        expected_menus_ie=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus)    
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 10: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 10: verify menulist")
            
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        """ 
             Step 11:Execute the revised repro C46039b.fex.
                     This version uses ARICONSET = BLUE.
        """
        utillobj.active_run_fex_api_login("C46039b.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 12: verification for layout 1
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 12.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 12.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 13:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 13.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 13.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 13.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 13.4: C46039a.fex data verification")
        """
            Step 14:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 14.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 14.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 14.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 14.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 14.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 14.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 14.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 15: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 15.1:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 15.2:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 15.3:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        """
            Step 16:Select the drop down control for Dollar Sales in the upper left report.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        fieldmenu.click()
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus)  
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 16: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 16: verify menulist")  
        
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """ 
             Step 17:Execute the revised repro C46039c.fex.
                    This version uses ARICONSET = ORIGINAL.
        """
        utillobj.active_run_fex_api_login("C46039c.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 18: verification for layout 
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 18.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 12.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 19:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 19.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 19.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 19.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 19.4: C46039a.fex data verification")
        """
            Step 20:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 20.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 20.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 20.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 20.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 20.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 20.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 20.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 21: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step21', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 21.1:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 21.2:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 21.3:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        """
            Step 22:Select the drop down control for Dollar Sales in the upper left report.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        fieldmenu.click()
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus)
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 22: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 22: verify menulist")  

        
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        """ 
             Step 23:Execute the revised repro C46039d.fex.
                    This version uses ARICONSET = XXXXX, an invalid value.
        """
        utillobj.active_run_fex_api_login("C46039d.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 24: verification for layout 
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 24.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 24.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 25:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 24.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 25.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 25.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 25.4: C46039a.fex data verification")
        """
            Step 26:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 26.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 26.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 26.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 26.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 26.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 26.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 26.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 27: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step27', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 27.1:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 27.2:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 27.3:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        """
            Step 28:Select the drop down control for Dollar Sales in the upper left report.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        utillity.UtillityMethods.click_on_screen(self, fieldmenu, 'middle', click_type=0)
        
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus) 
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 28: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 28: verify menulist")     
        
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        """ 
             Step 29:Execute the revised repro C46039e.fex.
                    This version uses ARICONSET = DEFAULT.
        """
        utillobj.active_run_fex_api_login("C46039e.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 30: verification for layout 
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 30.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 30.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 31:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 31.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 32.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 32.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 32.4: C46039a.fex data verification")
        """
            Step 32:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 32.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 32.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 32.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 32.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 32.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 32.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 32.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 33: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step33', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 33.1:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 33.2:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 33.3:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        """
            Step 34:Hover to the right of Dollar Sales in the upper left 4 line report until the 'hand' symbol occurs.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        fieldmenu.click()
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus)  
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 34: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 34: verify menulist")   
        
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        """ 
             Step 35:Execute the revised repro C46039f.fex.
                    This version uses ARICONSET = REVERSE.
        """
        utillobj.active_run_fex_api_login("C46039f.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 36: verification for layout 
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 36.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 36.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 37:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 37.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 37.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 37.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 37.4: C46039a.fex data verification")
        """
            Step 38:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 38.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 38.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 38.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 38.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 38.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 38.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 38.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 39: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step39', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 39.1:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 39.2:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 39.3:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        """
            Step 40:Select the drop down control for Dollar Sales in the upper left report.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        fieldmenu.click()
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus)    
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 40: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 40: verify menulist")  
        
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        """ 
             Step 41:Execute the revised repro C46039g.fex.
                    This version uses no declared ARICONSET value.
        """
        utillobj.active_run_fex_api_login("C46039g.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 42: verification for layout 
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 42.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 42.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 43:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 43.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 37.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 43.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 43.4: C46039a.fex data verification")
        """
            Step 44:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 44.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 44.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 44.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 44.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 44.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 44.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 44.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 45: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step45', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 45.1:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'Ship_Cove', 'Step 45.2:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 45.3:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        """
            Step 46:Select the drop down control for Dollar Sales in the upper left report.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        fieldmenu.click()
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus)
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 46: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 46: verify menulist")  
            
        
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        """ 
             Step 47.Execute the revised repro C46039noicons.fex.
                    This version removes all use of 
                    ARICONSET & ARSTYLESET.
        """
        utillobj.active_run_fex_api_login("C46039noicons.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody1 .chartPanel g text[class*='pieLabel!g0!mpieLabel']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 48: verification for layout 1
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 48.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 48.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 49:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 49.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 49.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(2,'27of107records,Page1of3', 'Step 49.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData2']", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData2']", Test_Case_ID+'_Ds02.xlsx',"Step 49.4: C46039a.fex data verification")
        """
            Step 50:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 50.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 50.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "cerulean_blue_1", "Step 50.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 50.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 50.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 50.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 50.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 51: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step51', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 51.9:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'cerulean_blue_1', 'Step 51.10:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'Dark_Cerulean', 'Step 52.11:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        time.sleep(2)
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        driver.find_element_by_css_selector(select_css).click()
        time.sleep(5)
        """
            Step 52: verification for layout 2
        """
        dropdown=driver.find_element_by_css_selector("#comboboxOBJECT6")
        utillobj.asequal(True,dropdown.is_displayed(),"Step 52.1:verify Midwest combobox")
        parent_css="[id^='IBILAYOUTDIV0OBJS'] [id^='LOBJText'] span"
        resobj.wait_for_property(parent_css, 1, string_value='RegionalSales', with_regular_exprestion=True)
        expected_datalabel=["Regional Sales"]
        resobj.verify_data_labels("IBILAYOUTDIV0OBJS", expected_datalabel, "Step 52.2:verify layout title", custom_css="[id^='LOBJText'] span")
        """
            Step 53:Upper left 4 line report and Lower left 107 line report
        """
        miscelaneous_obj.verify_page_summary('0','4of4records,Page1of1', 'Step 53.1: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 53.2: C46039a.fex data verification")
        time.sleep(1)
        miscelaneous_obj.verify_page_summary(3,'9of39records,Page1of1', 'Step 07.3: Verify Page summary')     
#         ia_runobj.create_table_data_set("table[id='ITableData3']", Test_Case_ID+"_Ds03.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData3']", Test_Case_ID+'_Ds03.xlsx',"Step 53.3: C46039a.fex data verification")
        """
            Step 54:Funtions for Pie char
        """
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1', ['Dollar Sales'], "Step 54.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['Coffee','Food','Gifts']
        resobj.verify_riser_legends('MAINTABLE_wbody1', expected_label_list, 'Step 54.2: Verify pie lablesList ')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "cerulean_blue_1", "Step 54.3: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 54.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 54.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 54.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody1', 3, "Step 54.7: Verify number of pie", custom_css="path[class*='riser!']") 
        """
            Step 55: Funtions for verify archartmenubar color and  background color
        """
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step55', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        layout=['Layouts', 'layout 1', 'layout 2', '']
        resobj.verify_data_labels("IBILAYOUTDIV0TABS", layout, "Step 09.9:verify layout title", custom_css=" table[id^='iLayTB']>tbody>tr>td>div")
        utillobj.verify_chart_color('orgdiv0',None, 'cerulean_blue_1', 'Step 09.10:Verify Layout 1 color',custom_css=".arDashboardBar[id='IBILAYOUTDIV0']", attribute_type='background-color')
        utillobj.verify_chart_color('orgdiv0',None, 'cyan', 'Step 09.11:Verify Layout 2 color',custom_css="[id='orgdivouter0']", attribute_type='background-color')
        time.sleep(2)
        """
            Step 56:Select the drop down control for Dollar Sales in the upper left report.
                    Left-click for the Active menu.
        """
        fieldmenu=driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading td:nth-child(2)  div[id^='popid'] img")
        fieldmenu.click()
        expected_menus=['Sort Ascending', 'Sort Descending', '', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', '', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', '', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        menu_css="[id='dt0_1_0']>table>tbody>tr[id^='t0']>td>span[id^='set']"
        actual_menus=[]
        total_menus=self.driver.find_elements_by_css_selector(menu_css)
        for i in range(len(total_menus)):
            actual_menus.append(total_menus[i].text.strip())
        print(actual_menus)    
        if br1=="IE":
            utillobj.as_List_equal(actual_menus,expected_menus_ie,"Step 56: verify menulist")
        else:
            utillobj.as_List_equal(actual_menus,expected_menus,"Step 56: verify menulist")
        
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        
if __name__ == "__main__":
    unittest.main()  