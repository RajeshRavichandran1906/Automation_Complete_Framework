from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.lib.base import BasePage
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from common.pages import visualization_resultarea
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
from selenium.common.exceptions import NoSuchElementException
from common.lib.global_variables import Global_variables
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class Visualization_Ribbon(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Visualization_Ribbon, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def select_visualization_application_menu_item(self, application_menu_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        param: item_name: 'save_as' OR 'run'.
        '''
        ia_btn=self.driver.find_element(*VisualizationRibbonLocators.Appbtn)
        coreutillityobject.left_click(self, ia_btn)
        elem1=VisualizationRibbonLocators.__dict__['menu_'+application_menu_item_name]
        self._validate_page(elem1)
        application_menu_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__['menu_'+application_menu_item_name])
        coreutillityobject.left_click(self, application_menu_item)
        time.sleep(8)

    def select_visualization_top_toolbar_item(self, top_toolbar_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        param: item_name: 'new' OR 'run'.
        '''
        toolbar_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__['toolbar_'+top_toolbar_item_name])
        coreutillityobject.python_left_click(self, toolbar_item)
        time.sleep(8)
    
    def switch_ribbon_tab(self, tab_name): 
        '''
        Desc: This is used to switch to any visualization tab.
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        '''
        utillityobject.wait_for_page_loads(self, 100)
        tab_css=VisualizationRibbonLocators.tab_css.format(tab_name)
        utillityobject.synchronize_with_number_of_element(self, tab_css, 1, 30)
        tab_elem=self.driver.find_element_by_css_selector(tab_css)
#         utillityobject.default_left_click(self, object_locator=tab_elem)
        coreutillityobject.python_left_click(self, tab_elem)
        enabled_tab_css="div[id*='{0}Tab'][class*='checked']" .format(tab_name)
        utillityobject.synchronize_with_number_of_element(self, enabled_tab_css, 1, 30)
        time.sleep(8)
    
    def unhide_ribbon_item(self, tab_name, ribbon_button_name):
        '''
        Desc: This is used to unhide the ribbon item if it hidden. In future we will add the key value to the dictionary.
        '''
        ribbon_dictionary ={'auto_drill':'run_with', 
                            'enable_auto_linking':'auto_linking', 
                            'auto_link_target':'auto_linking'}
        if ribbon_button_name.lower() in ribbon_dictionary.keys():
            ribbon_image_button_name = tab_name.lower() + "_" + ribbon_dictionary[ribbon_button_name.lower()]
            try:
                ribbon_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__[ribbon_image_button_name])
                try:
                    if ribbon_item.is_displayed():
                        coreutillityobject.left_click(self, ribbon_item)
                        time.sleep(2)
                except:
                    pass
            except NoSuchElementException:
                pass
            
    def select_visualization_ribbon_item(self, tab_name, ribbon_button_name_path):
        '''
        Desc: This is used to select any ribbon item within any tab. In order to select the ribbon item, user can provide multilevel
        Eg: select_visualization_ribbon_item('Home', 'insert->Grid')
        '''
        ribbon_item_path_list=ribbon_button_name_path.split('->')
        Visualization_Ribbon.switch_ribbon_tab(self, tab_name)
        button_name = tab_name.lower() + "_" + ribbon_item_path_list[0].lower()
        Visualization_Ribbon.unhide_ribbon_item(self, tab_name, ribbon_item_path_list[0])
        ribbon_item_css=VisualizationRibbonLocators.__dict__[button_name] 
        utillityobject.synchronize_with_number_of_element(self, ribbon_item_css[1], 1, 10)
        ribbon_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__[button_name])
        coreutillityobject.left_click(self, ribbon_item)
        for opt in ribbon_item_path_list[1:]:
            utillityobject.select_bipopup_list_item(self, opt)
            time.sleep(10)
        
        
    def create_header_footer_styling(self, heading_type, input_text, default_heading_type_highlighted='Page Header', step_num='X', style_dict=None, close_dialog='ok'): 
        """
        :Params: heading_type= Page Header or Page Footer
        :Params: Input_text = provide the text to be added
        :Params: style_dict={'font_name':'Arial','font_size':12,'bold':True,'italic':True,'underline'=True,'left_justify':True,'center_justify':True,'right_justify':True'
        'text_color':'red','background_color':'yellow'}
        :Usage:  create_header_footer('Page Header','<PRICE_DOLLARS_BIN_1',default_heading_type_highlighted='Page Header', step_num='1', 
        style_dict={'font_name':'COMIC SANS MS', 'text_color':'blue'}, close_dialog='ok')  
        """
        header_footer_css={"page_header":"#pgHding","page_footer":"#pgFting"}
        header_footer_ok_button_css="#subheaderDlg [class*='active'] #okBtn"
        utillityobject.synchronize_with_number_of_element(self, header_footer_ok_button_css, 1, 50)
        Page_heading_elem=self.driver.find_element_by_css_selector(header_footer_css[default_heading_type_highlighted.replace(" ","_").lower()])
        utillityobject.verify_object_highlighted(self, Page_heading_elem, checked_class='checked', highlight_color=None, step_num=step_num)
        ids={'Report Header':'rptHding','Page Header':'pgHding','Page Footer':'pgFting','Report Footer':'rptFting'}#Conversion change
        btn_css="#" + ids[heading_type] + " img"
        btn_css_obj=self.driver.find_element_by_css_selector(btn_css)
        coreutillityobject.left_click(self, btn_css_obj)
        time.sleep(2)        
        elem=self.driver.find_element_by_id("Editor")
        utillityobject.set_text_to_textbox_using_keybord(self, input_text, text_box_elem=elem)
        Visualization_Ribbon.set_header_footer_style(self,style_dict)
        button_id={'apply':"applyBtn",'ok':"okBtn",'cancle':"cancelBtn",'reset':"resetBtn"}
        btn_element=self.driver.find_element_by_id(button_id[close_dialog])
        coreutillityobject.left_click(self, btn_element)
        time.sleep(1)
    
    def set_header_footer_style(self, style_dict):
        '''
        params: style_dict={'font_name':'Arial','font_size':12,'bold':True,'italic':True,'underline'=True,'left_justify':True,'center_justify':True,'right_justify':True'
        'text_color':'red','background_color':'yellow'}
        '''
        style_dict_css={'font_name':"#subheaderDlg  div[id*=FontName] div[id^='BiButton']",'font_size':"#subheaderDlg  div[id*=FontSize] div[id^='BiButton']",
               'bold':"#subheaderDlg #Bold img",'italic':"#subheaderDlg #Italic img",'underline':"#subheaderDlg #Underline img",'left_justify':"#subheaderDlg #Left img",
               'center_justify':"#subheaderDlg #Center img",'right_justify':"#subheaderDlg #Right img",'text_color':"#subheaderDlg #Color img",'background_color':"#subheaderDlg #BackColor img"}
        for item in style_dict:
            style_elem=self.driver.find_element_by_css_selector(style_dict_css[item])
            if item in ['font_name','font_size']:
                utillityobject.select_combo_box_item(self, style_dict_css[item], combobox_dropdown_elem=style_elem)
            if item in ['bold','italic','underline','left_justify','center_justify','right_justify']:
                coreutillityobject.left_click(self, style_elem)
            if item in ['text_color','background_color']:
                coreutillityobject.left_click(self, style_elem)
                parent_css="div[id^='IAColorPicker']"
                utillityobject.set_color_in_color_picker_dialog(self, parent_css, style_dict['background_color'],close_dialog_button='ok')
    
    def select_visualization_chart_type(self, chart_type_name):
        '''
        Desc: This is used to select chart type.
        '''
        chart_ids={'grid':'tablegrid_32.png',
                    'bar':'chart_bar_32.png',
                    'stacked_bar':'stacked_bar_32.png',
                    'line':'chart_line_32.png',
                    'area':'chart_area_32.png',
                    'stacked_area':'stacked_area_32.png',
                    'pie':'chart_pie_32.png',
                    'ring_pie':'chart_pie_ring_32.png',
                    'scatter':'chart_scatter_32.png',
                    'bubble_chart':'x_y_plots_bubble_32.png',
                    'matrix_marker':'matrix_marker_32.png',
                    'treemap':'treemap_32.png',
                    'gauge':'gauge_32.png',
                    'choropleth_map':'choropleth_32.png',
                    'bubble_map':'bubblemap_32.png',
                    'heatmap':'special_marker_mapped_32.png',
                    'map':'select_map_32.png'}
        chart_type_css="div[id^='InsertVizPopupDlg'] img[src$='" + chart_ids[chart_type_name] + "']"
        utillityobject.synchronize_with_number_of_element(self, chart_type_css, 1, 10)
        chart_elem = self.driver.find_element_by_css_selector(chart_type_css)
        coreutillityobject.left_click(self, chart_elem)
        time.sleep(3)
    
    def verify_fexcode_syntax(self,expected_syntax_list,msg):
        '''
        :Description - verify fex syntax code in fex procedure code
        :param : expected_syntax_list=["DEFAULTH &WF_NODATA='None';","SET NODATA=&WF_NODATA"]
        :usage : verify_fexcode_syntax(expected_syntax_list,'Step 09.1 : Verify Syntax for Missing Value')
        '''
        Visualization_Ribbon.select_visualization_top_toolbar_item(self,'showfex')
        time.sleep(2)
        frame_css="iframe[id^='BiRichEdit']"
        utillityobject.synchronize_with_number_of_element(self, frame_css, 1, 15)
        coreutillityobject.switch_to_frame(self, frame_css)
        actual_fex_code = self.driver.find_element_by_css_selector("body>div").text
        for syntax in expected_syntax_list :
            if syntax in actual_fex_code :
                status=True
            else :
                status=False
                break
        utillityobject.asequal(self,True,status,msg)
        coreutillityobject.switch_to_default_content(self)
        ok_btton=self.driver.find_element_by_css_selector("#showFexOKBtn")
        coreutillityobject.left_click(self, ok_btton)
        
    def verify_syntax_not_in_fexcode(self,expected_syntax_list,msg):
        '''
        :Description - verify fex syntax code in fex procedure code
        :param : expected_syntax_list=["DEFAULTH &WF_NODATA='None';","SET NODATA=&WF_NODATA"]
        :usage : verify_fexcode_syntax(expected_syntax_list,'Step 09.1 : Verify Syntax for Missing Value')
        '''
        Visualization_Ribbon.select_visualization_top_toolbar_item(self,'showfex')
        time.sleep(2)
        frame_css="iframe[id^='BiRichEdit']"
        utillityobject.synchronize_with_number_of_element(self, frame_css, 1, 15)
        coreutillityobject.switch_to_frame(self, frame_css)
        actual_fex_code = self.driver.find_element_by_css_selector("body>div").text
        for syntax in expected_syntax_list :
            if syntax in actual_fex_code :
                status=False
                break
            else :
                status=True
        utillityobject.asequal(self,True,status,msg)
        coreutillityobject.switch_to_default_content(self)
        ok_btton=self.driver.find_element_by_css_selector("#showFexOKBtn")
        coreutillityobject.left_click(self, ok_btton)
        
    
    def select_map_dialog(self, map_type=None, teritory_name=None, close_dialog='ok'):
        """
        Usage: select_map('choropleth',teritory='World',btn_click='ok')
        """
        maps={'choropleth':'choroplethMapBtn', 'bubble':'bubbleMapBtn'}
        btns={'ok':'mapTypesOkBtn', 'cancel':'mapTypesCancelBtn', 'apply':'mapTypesApplyBtn'}
        if map_type != None:
            required_map_css="div[id^='QbDialog'] #" +  maps[map_type]
            utillityobject.synchronize_with_number_of_element(self, required_map_css, 1, 30)
            elem = self.driver.find_element_by_css_selector(required_map_css)
            coreutillityobject.python_left_click(self, elem)
            time.sleep(2)
        if teritory_name != None:
            combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #mapTerrCombo div[id^='BiButton']")
            utillityobject.select_combo_box_item(self, teritory_name, combobox_dropdown_elem=combo_btn)
        if close_dialog != None:
            self.driver.find_element_by_css_selector("div[id^='QbDialog'] #" +  btns[close_dialog]).click()
        time.sleep(2)
                            
    """========================================Old functions==============================================="""  
    def switch_ia_tab(self, tab_name, **kwargs): #To be deleted
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: switch_ia_tab('Layout')
        @author = Niranjan
        """
        time.sleep(2)
        tab_css=VisualizationRibbonLocators.tab_css.format(tab_name)
        obj_tab=self.driver.find_element_by_css_selector(tab_css)
        coreutillityobject.left_click(self, obj_tab)
        time.sleep(4)
        flag=False
        count=0
        while flag!=True:
            try:
                flag=self.driver.find_element_by_css_selector("div[id='" + tab_name + "Tab'][style*='z-index: 1']").is_enabled()
#                 print("Is Specified -", tab_name ,"Tab - is active:", flag)
            except:
#                 print("except")
                coreutillityobject.left_click(self, obj_tab)
                time.sleep(1)
            count=count+1
            if count==3:
#                 print("Is Specified -", tab_name ,"Tab - is active:", flag)
                break
                   
    
    def change_output_format_type(self, output_format_type, location='Home'):#To be deleted
        """
        param: output_format_type: 'active_report' OR 'pdf'
        location='Home' or 'status_bar'
        @author = Niranjan
        """
        format_btn_ids={'html':'menu_html_btn',
                        'reporthtml':'menu_html_btn',
                    'active_report':'menu_ahtml_btn',
                    'pdf':'pdf_btn',
                    'active_pdf':'menu_apdf_btn',
                    'excel':'menu_excel2k07_btn',
                    'powerpoint':'menu_ppt_2007_btn',
                    'charthtml':'menu_pngShowhtml_btn'}
        if location=='Home':
            Visualization_Ribbon.select_ribbon_item(self, 'Home', 'format_type')
        else:
            #self.driver.find_element_by_css_selector("#sbpOutputFormatPanel div[class$='drop-down-arrow']").click()
            status_btn=self.driver.find_element_by_css_selector("#sbpOutputFormatPanel #sbpOutputFormat img")
            coreutillityobject.left_click(self, status_btn)
        time.sleep(2)
        format_btn_css="#HomeFormatTypeMenu " + "[id*='" +format_btn_ids[output_format_type] + "'] img[src*='dhtml']"
        obj_output=self.driver.find_element_by_css_selector(format_btn_css)
        coreutillityobject.left_click(self, obj_output)
        time.sleep(5)
    
    def select_ribbon_item(self, tab_name, ribbon_button_name, **kwargs):#To be deleted
        """
        param: tab_name: 'Layout' or 'Home' 
        param: ribbon_button_name: 'Document' or 'Data_from_Source' (The button name as displayed in ribbon bar. If space is there, then replace it by underscore.)
        param: opt: The dropdown menu list from a ribbon button.
        Syntax: select_ribbon_item('Layout', 'LayoutMargins', opt='Custom')
        @author : Nasir
        """
        ribbon_dictionary ={'auto_drill':'run_with', 'enable_auto_linking':'auto_linking', 'auto_link_target':'auto_linking','grid':'features','frame_and_background':'features'}
        time.sleep(3)
        Visualization_Ribbon.switch_ia_tab(self, tab_name, **kwargs)
        time.sleep(3)
        button_name = tab_name.lower() + "_" + ribbon_button_name.lower()
        if ribbon_button_name.lower() in ribbon_dictionary.keys():
            ribbon_image_button_name = tab_name.lower() + "_" + ribbon_dictionary[ribbon_button_name.lower()]
            try:
                ribbon_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__[ribbon_image_button_name])
                try:
                    if ribbon_item.is_displayed():
                        coreutillityobject.python_left_click(self, ribbon_item)
                except:
                    pass
            except NoSuchElementException:
                pass
        Visualization_Ribbon._validate_page(self, VisualizationRibbonLocators.__dict__[button_name])
        ribbon_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__[button_name])
        coreutillityobject.python_left_click(self, ribbon_item)
        time.sleep(15)
        if 'opt' in kwargs:
            utillityobject.select_or_verify_bipop_menu(self, kwargs['opt'],**kwargs)
            time.sleep(10)
    
    def change_chart_type(self, chart_type, **kwargs):#To be deleted
        """
        param: chart_type: 'grid' OR 'bar' OR 'line'
        @author = Niranjan
        """
        chart_ids={'grid':'tablegrid_32.png',
                    'bar':'chart_bar_32.png',
                    'stacked_bar':'stacked_bar_32.png',
                    'line':'chart_line_32.png',
                    'area':'chart_area_32.png',
                    'stacked_area':'stacked_area_32.png',
                    'pie':'chart_pie_32.png',
                    'ring_pie':'chart_pie_ring_32.png',
                    'scatter':'chart_scatter_32.png',
                    'bubble_chart':'x_y_plots_bubble_32.png',
                    'matrix_marker':'matrix_marker_32.png',
                    'treemap':'treemap_32.png',
                    'gauge':'gauge_32.png',
                    'choropleth_map':'choropleth_32.png',
                    'bubble_map':'bubblemap_32.png',
                    'heatmap':'special_marker_mapped_32.png',
                    'map':'select_map_32.png',
                    'simple_bar':'simple_bar/icons/icon.svg'}
        self.select_ribbon_item('Home', 'change')
        chart_type_css="div[id^='InsertVizPopupDlg'] img[src$='" + chart_ids[chart_type] + "']"
        chart_elem = self.driver.find_element_by_css_selector(chart_type_css)
        utillityobject.synchronize_with_number_of_element(self, chart_type_css, 1, 240)
        coreutillityobject.left_click(self, chart_elem)
        time.sleep(3)

    def select_tool_menu_item(self, item_name, **kwargs):#To be deleted
        """
        param: item_name: 'menu_save_as' OR 'menu_run' - these need to be get it from Visualization_ribbon_locators.
        @author = Niranjan
        """
        ia_btn=self.driver.find_element(*VisualizationRibbonLocators.Appbtn)
        coreutillityobject.left_click(self, ia_btn)
        elem1=VisualizationRibbonLocators.__dict__[item_name]
        Visualization_Ribbon._validate_page(self, elem1)
        obj_tool_menu=self.driver.find_element(*VisualizationRibbonLocators.__dict__[item_name])
        coreutillityobject.left_click(self, obj_tool_menu)
        time.sleep(8)

    def select_top_toolbar_item(self, item_name, **kwargs):#To be deleted
        """
        param: item_name: 'toolbar_new' OR 'toolbar_run' - these need to be get it from Visualization_ribbon_locators.
        This function is specific to click on toolbar buttons - new, run, undo, redo, run
        @author = Niranjan
        """
        if item_name == 'toolbar_showfex':
            fexcode=self.driver.find_element_by_css_selector("#showFexButton img")
            coreutillityobject.left_click(self, fexcode, action_chain_click=True)
        elif item_name == 'infomini_edit':
            fexcode=self.driver.find_element_by_css_selector("#editModeButton img")
            coreutillityobject.left_click(self, fexcode, action_chain_click=True)
        elif item_name == 'infomini_save':
            fexcode=self.driver.find_element_by_css_selector("#saveButton img")
            try:
                coreutillityobject.left_click(self, fexcode, action_chain_click=True)
            except:
                pass
#                 print("Chrome exception in infomini save:")    
        elif item_name == 'toolbar_run':
            if coreutillityobject.parseinitfile(self, 'suite_type') == 'visualization' and Global_variables.browser_name =='edge':
#                 keyboard.send('ctrl+r') 
                for _ in range(300):
                    status = self.driver.execute_script("return document.readyState == 'interactive' || document.readyState == 'complete'")
                    if status:
                        time.sleep(1)
                        break
#                 run_btn=self.driver.find_element_by_css_selector("#runButton")
                if sys.platform == 'linux':
                    pykeyboard.press_key(pykeyboard.control_key)
                    pykeyboard.tap_key(character=u'\u0072')
                    pykeyboard.release_key(pykeyboard.control_key)
                else:
                    keyboard.send('ctrl+r')
#                 coreutillityobject.left_click(self, run_btn, action_chain_click=True)
            else:
                run_btn=self.driver.find_element_by_css_selector("#runButton img")
                coreutillityobject.left_click(self, run_btn, action_chain_click=True)
        else:
            ribbion_obj=self.driver.find_element(*VisualizationRibbonLocators.__dict__[item_name])
            coreutillityobject.left_click(self, ribbion_obj)
        time.sleep(8)
        
    def select_theme(self, theme_library, theme_file, **kwargs):
        """
        :param: theme_library: 'Legacy Templates' or 'Templates'
        :param: theme_file: 'ENIADefault_combine.sty'
        :usage: select_theme('Legacy Templates', 'ENIADefault_combine.sty')
        @author : Niranjan
        """
        elem = self.driver.find_element_by_css_selector("#HomeThemes img")
        coreutillityobject.left_click(self, elem)
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#IbfsOpenFileDialog7_btnOK", 1, 30, string_value='Open')
        time.sleep(1)
        theme_library_xpath="//div[@id='paneIbfsExplorer_scTree']//td[contains(text(), '" + theme_library + "')]/img"
        lib_ele = self.driver.find_element_by_xpath(theme_library_xpath)
        coreutillityobject.left_click(self, lib_ele)
        utillityobject.select_item_from_ibfs_explorer_list(self, theme_file)
        
    def repositioning_document_component(self, horizontal_pos, vertical_pos, **kwargs):
        """
        :usage: repositioning_document_component('2.5', '2.5')
        @author : Nasir
        """
        Visualization_Ribbon.switch_ia_tab(self, 'Layout')
        elem = self.driver.find_element_by_css_selector("#ClusterLayoutSizeArrange img[src$='images/qb/group_16.png']")
        coreutillityobject.left_click(self, elem)
        time.sleep(3)
        elem1 = self.driver.find_element_by_id("positionOptions")
        coreutillityobject.left_click(self, elem1)
        time.sleep(3)
        input_left = self.driver.find_element_by_id("positionHorzSpinner")
        input_left.clear()
        input_left.send_keys(horizontal_pos)
        time.sleep(1)
        input_left.send_keys(keys.Keys.ENTER)
        time.sleep(1)
        input_top = self.driver.find_element_by_id("positionVertSpinner")
        input_top.clear()
        input_top.send_keys(vertical_pos)
        time.sleep(1)
        input_top.send_keys(keys.Keys.ENTER)
        time.sleep(3)
        apply_btn = self.driver.find_element_by_css_selector("#sapApplyBtn img")
        coreutillityobject.left_click(self, apply_btn)
#         utillityobject.default_left_click(self, object_locator=apply_btn, **kwargs)
        time.sleep(1)
        ok_btn = self.driver.find_element_by_css_selector("#sapOkBtn img")
        coreutillityobject.left_click(self, ok_btn)
#         utillityobject.default_left_click(self, object_locator=ok_btn, **kwargs)
        time.sleep(3)
    
    def resizing_document_component(self, size_height, size_width, **kwargs):
        """
        :usage: resizing_document_component('2.5', '2.5')
        @author : Nasir
        """
        Visualization_Ribbon.switch_ia_tab(self, 'Layout')
        cluster_obj=self.driver.find_element_by_css_selector("#ClusterLayoutSizeArrange img[src$='images/qb/group_16.png']")
        coreutillityobject.left_click(self, cluster_obj)
        time.sleep(3)
        self.driver.find_element_by_id("sizeOptions").click()
        time.sleep(3)
        h1 = self.driver.find_element_by_id("sizeHeightSpinner")
        h1.clear()
        h1.send_keys(size_height)
        time.sleep(1)
        h1.send_keys(keys.Keys.ENTER)
        time.sleep(1)
        w1 = self.driver.find_element_by_id("sizeWidthSpinner")
        w1.clear()
        w1.send_keys(size_width)
        time.sleep(1)
        w1.send_keys(keys.Keys.ENTER)
        time.sleep(3)
        apply_btn = self.driver.find_element_by_css_selector("#sapApplyBtn img")
        coreutillityobject.left_click(self, apply_btn)
        time.sleep(3)
        sapokbtn_obj=self.driver.find_element_by_css_selector("#sapOkBtn")
        coreutillityobject.python_left_click(self, sapokbtn_obj)
#         coreutillityobject.left_click(self, sapokbtn_obj)
        time.sleep(3)
        
    def select_map(self, map_type, **kwargs):
        """
        Usage: select_map('choropleth',teritory='World',btn_click='ok')
        """
        maps={'choropleth':'choroplethMapBtn', 'bubble':'bubbleMapBtn'}
        btns={'ok':'mapTypesOkBtn', 'cancel':'mapTypesCancelBtn', 'apply':'mapTypesApplyBtn'}
        elem = self.driver.find_element_by_css_selector("div[id^='QbDialog'] #" +  maps[map_type])
        coreutillityobject.left_click(self, elem)
        time.sleep(2)
        if 'teritory' in kwargs:
            combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #mapTerrCombo div[id^='BiButton']")
            utillityobject.select_any_combobox_item(self,combo_btn, kwargs['teritory'])
        if 'btn_click' in kwargs:
            self.driver.find_element_by_css_selector("div[id^='QbDialog'] #" +  btns[kwargs['btn_click']]).click()
        time.sleep(2)
        
    def select_item_in_splash_options(self, item_name, **kwargs):
        """
        param: item_name='Build a Report' OR 'Build a Chart'  or 'Build a Visualization'  
        usage: select_item_in_splash_options('Build a Report')
        """
        elem=(By.CSS_SELECTOR,'#splash_options #splash_bar_content')
        Visualization_Ribbon._validate_page(self, elem)
        splash_options=self.driver.find_elements_by_css_selector("#splash_options div[class*='tool-bar-button']")
        click_elem=splash_options[[el.text.strip() for el in splash_options].index(item_name)]
        coreutillityobject.left_click(self, click_elem)
        time.sleep(15)
        
    def select_report_output_window(self, output_window_name, **kwargs):
        """
        @Param: output_window_name: 'Single Window'
        @Usage: select_report_output_window('Single Window')
        """
        elem=self.driver.find_element_by_css_selector("#sbpTargetOutputPanel")
        coreutillityobject.left_click(self, elem)
        time.sleep(1)
        utillityobject.select_or_verify_bipop_menu(self, output_window_name,**kwargs)
        time.sleep(5)
        
    def switch_to_report_panel(self,panel_name,**kwargs):
        """
        @Param: panel_name: 'Report1' or 'Chart1'
        @Usage: switch_to_report_panel('Report1')
        """
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReportPanel")
        coreutillityobject.left_click(self, elem)
        time.sleep(1)
        utillityobject.select_or_verify_bipop_menu(self, panel_name,**kwargs)
        time.sleep(3)       