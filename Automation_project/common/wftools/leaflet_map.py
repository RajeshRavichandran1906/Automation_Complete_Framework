from common.lib import utillity
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import time
from pynput.mouse import Button, Controller
from selenium.webdriver.support.color import Color
import pyautogui

class AS_Esri_Map_Run(BasePage):
    
        
    def __init__(self, driver):
        super(AS_Esri_Map_Run, self).__init__(driver)
        self.browser = utillity.UtillityMethods.parseinitfile(self,'browser')
        

    

    def _validate_page(self, locator, **kwargs):
        """        
        Usage1: Here selenium will wait for a default time of default long wait of 250 seconds.
        
        ok_btn_css="div[id^='IAColorPicker'] div[class$='window-active'] #BiColorPickerOkBtn"
        ok_elems=self.driver.find_element_by_css_selector(ok_btn_css)
        elem1=(By.CSS_SELECTOR, ok_btn_css)
        self._validate_page(elem1)
        
        Usage2: Here selenium will wait for your passed value of 500 seconds. So you can pass as much time you want        
        ok_btn_css="div[id^='IAColorPicker'] div[class$='window-active'] #BiColorPickerOkBtn"
        ok_elems=self.driver.find_element_by_css_selector(ok_btn_css)
        elem1=(By.CSS_SELECTOR, ok_btn_css)
        self._validate_page(elem1, wait_time=500)
        """
        if 'wait_time' in kwargs:
            custom_wait = WebDriverWait(self.driver, kwargs['wait_time'])
            custom_wait.until(EC.visibility_of_element_located(locator))
        else:
            self.longwait.until(EC.visibility_of_element_located(locator))           
        
        

        
    def esri_select_main_menu_map_widget(self, widget_name):
        """
        params: widget_name = 'home' OR 'toc', OR 'select_tool', OR 'change_map', OR 'find_location'
        Syntax: select_map_main_menu('home')
        """
        main_menu="#mainMenu"
        btn_title={'home':"div[title='Default extent']",
                  'toc':"li[title='Table of Contents']",
                  'selection':"li[title='Selection Tools']",
                  'basemap':"li[title='Change Base Map']",
                  'my_location':"div[title='Find my location']"}
        btn_css= main_menu + " " + btn_title[widget_name]
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(1)
    
    def esri_select_map_toc_tools(self, layer_name, opt):
        """
        params: btn_name = 'zoom_to_layer' OR 'toggle_options', OR 'toggle_layer_legend'
        Syntax: select_map_tools_in_toc('Customers' ,'toggle_layer')
        """
        
        layers=self.driver.find_elements_by_css_selector("#lwFloatingPane .lyrName")
        layer_index=[el.get_attribute('title') for el in layers].index(layer_name)
        options={'show_tool':'li.optionsBoxBtn',
                 'zoom_to_layer':'li.goToLyr',
                  'toggle_options':"li[id='"+layer_name+"Djt'] li[class^='optsIcon']",
                  'toggle_layer_legend':'li.legIcon'}
        
        if not self.driver.find_elements_by_css_selector(options[opt])[layer_index].is_displayed():
            self.driver.find_elements_by_css_selector(options['show_tool'])[layer_index].click()
            time.sleep(2)
            
        self.driver.find_elements_by_css_selector(options[opt])[layer_index].click()
        time.sleep(1)

        
    def esri_selection_widget_click_tools(self, opt):
        """
        :param : NONE
        :Usage: esri_selection_widget_click_tools("zoom_to_layer")
        :author: Jesmin
        :date: 12/12/2016
        """   
        options={'zoom_to_layer':'#selectionTools > ul > li:nth-child(1) > ul > li.goToLyr',
                 'zoom_to_selection':'#selectionTools > ul > ul:nth-child(6) > li',
                  'pan':'#selectionTools > ul > li:nth-child(3) > ul > li.panMap',
                  'clear_selection':'#selectionTools > ul > li:nth-child(3) > ul > li.clearAll',
                  'extent_select':'#selectionTools > ul > li:nth-child(3) > ul > li.selectByExtent',
                  'polygon_select':'#selectionTools > ul > li:nth-child(3) > ul > li.selectByPolygon',
                  'line_select':'#selectionTools > ul > li:nth-child(3) > ul > li.selectByPolyline',
                  'distance_select':'#selectionTools > ul > li:nth-child(3) > ul > li.selectByDistance',
                  'unselect':'#selectionTools > ul > li:nth-child(3) > ul > li.clearSelection2'                  
                  }
            
        self.driver.find_element_by_css_selector(options[opt]).click()
        time.sleep(1)  
          
 
    def verify_esri_map_fill_color(self, obj_css, fill_color, msg, **kwargs):
        """
        params: outline_thickness= outline_thickness="5" 
        params: fill_color = 'red', OR 'green', OR 'electric_violet'...
        Syntax: verify_esri_map_fill_color(point_poly_css, 'electric_violet', "Step X:Verify Color","outline_thickness=5" )
        :author: Niranjan
        """               
        expected_color=utillity.UtillityMethods.color_picker(self, fill_color, 'rgba')
        actual_color=Color.from_string(self.driver.find_element_by_css_selector(obj_css).get_attribute("fill")).rgba
        utillity.UtillityMethods.asequal(self, expected_color, actual_color , msg + "verify fill color")
        
        if 'outline_color' in kwargs and kwargs['outline_style']!=None:
            expected_stroke_color=utillity.UtillityMethods.color_picker(self, kwargs['outline_color'], 'rgba')
            actual_stroke_color=Color.from_string(self.driver.find_element_by_css_selector(obj_css).get_attribute("stroke")).rgba 
            #print(actual_stroke_color)
            utillity.UtillityMethods.asequal(self, expected_stroke_color, actual_stroke_color , msg + "verify stroke color")
                        
        if 'outline_thickness' in kwargs and kwargs['outline_style']!=None:
            actual_stroke_thickness=self.driver.find_element_by_css_selector(obj_css).get_attribute("stroke-width")
            #print(actual_stroke_thickness)
            utillity.UtillityMethods.asequal(self, kwargs['outline_thickness'], actual_stroke_thickness , msg + "verify stroke width")

        if 'outline_style' in kwargs:
            actual_stroke_style=self.get_html_attribute(obj_css, "dojoGfxStrokeStyle", kwargs['outline_style'])
            #print(actual_stroke_style)
            utillity.UtillityMethods.asequal(self, kwargs['outline_style'], actual_stroke_style , msg + "verify stroke style")  
    
    def verify_esri_map_selected_layer(self, selected_layer):
        actual_stroke_style=self.get_html_attribute(selected_layer, "dojoGfxStrokeStyle", "shortdashdotdot")
        #print(actual_stroke_style)
        utillity.UtillityMethods.asequal(self, "shortdashdotdot", actual_stroke_style , "Verify stroke style for selected extent")
        #assert self.driver.find_element_by_css_selector(selected_layer).get_attribute("Name"), "Layer not selected"
        #print(self.driver.find_element_by_css_selector(selected_layer).get_attribute("Name") + " layer is selected")
    
    def get_html_attribute(self, obj_css, attribute_name, outline_style):
        attributes = self.driver.find_element_by_css_selector(obj_css).get_attribute("outerHTML").split()
        snip = len(attribute_name)
        for x in attributes:
            if x[:snip] == attribute_name:
                if outline_style in x:
                    return outline_style
                else:
                    print("Outline style not found")
                    return ""
                #return (x[(snip+1):].strip('"'))
     

    def esri_select_basemap(self, basemap_title,msg):
        """
        params: select_base_map = 'Imaginary', OR 'Streets' ...
        Syntax: select_base_map('demo_color')
        modified: Jesmin 12/15/2016
        """ 
        img_css="#imDijit img[title='" + basemap_title + "']"   
        self.driver.find_element_by_css_selector(img_css).click()
        time.sleep(2)
        
        get_basemaps_title=self.driver.find_elements_by_css_selector(".esriBasemapGalleryNode")
       
        for elem in get_basemaps_title:        
            if elem.text == self.driver.find_element_by_css_selector("#imDijit span[title='"+basemap_title+"']").text:        
                break
        utillity.UtillityMethods.asin(self.driver,"esriBasemapGallerySelectedNode", elem.get_attribute("class") ,msg+ "verify"+basemap_title+" basemap is selected")
               

        
        
    
    def esri_check_uncheck_layer(self, layer_name):
        """
        params: layer_name = 'Layer 1', OR 'Layer 2' ...
        Syntax: esri_check_uncheck_layer('Layer 1')
        """ 
        layers=self.driver.find_elements_by_css_selector("#lwFloatingPane .layerList")        
        layers[[el.text.strip() for el in layers].index(layer_name)].find_element_by_css_selector("li[class^='LyrCb']").click()
        time.sleep(1)

    
    def esri_zoom_in_out(self, zoom_type, zoom_times):
        """
        params: zoom_type = 'in', OR 'out'
        params: zoom_times = 1, 2, 3...(Any integer value, Means the number of times you want to zoom in or zoom out)
        Syntax: esri_zoom_in_out('out', 2)
        """
        if zoom_type=='in':
            zoom_css="#emfobject1_zoom_slider .esriSimpleSliderIncrementButton > span"
        else:
            zoom_css="#emfobject1_zoom_slider .esriSimpleSliderDecrementButton > span" 
        loc=self.driver.find_element_by_css_selector(zoom_css)
        for i in range(zoom_times):
            loc.click()
            #utillity.UtillityMethods.click_type_using_pyautogui(loc, leftClick=True)
            time.sleep(3)
           
    def esri_close_widget(self,widget):
        close_css={'toc':"#lwFloatingPane > div.dojoxFloatingPaneTitle > span.dojoxFloatingCloseIcon",
                  'selection':"#stFloatingPane > div.dojoxFloatingPaneTitle > span.dojoxFloatingCloseIcon",
                  'basemap':"#imFloatingPane > div.dojoxFloatingPaneTitle > span.dojoxFloatingCloseIcon"}
        #close_css="span.dojoxFloatingCloseIcon"      
        self.driver.find_element_by_css_selector(close_css[widget]).click()
        time.sleep(1)
       

 
    def esri_move_map_widget(self,widget_name, x, y, x_off_set=0, y_off_set=0):
        """
        :Usage: esri_move_map_widget("toc",600,10)
        :param: widget_name = toc ; x =600; y =10
        :author = Jesmin
        """     
        widget_icon_title={'toc':'div.dojoxFloatingPaneTitle',
                  'selection':'#stFloatingPane > div.dojoxFloatingPaneTitle',
                  'basemap':'#imFloatingPane > div.dojoxFloatingPaneTitle'}
        
        elem=self.driver.find_element_by_css_selector(widget_icon_title[widget_name])
        
        pyautogui.FAILSAFE=False    
        browser=utillity.UtillityMethods.parseinitfile(self,'browser')
        if browser=='Firefox':
            x1=elem.location['x']+x_off_set
            y1=elem.location['y']+70+y_off_set
            pyautogui.moveTo(x1, y1, 3)
            time.sleep(2)
            pyautogui.dragRel(x, y, 3)
        else:
            time.sleep(1)    
            action=ActionChains(self.driver)
            action.move_to_element_with_offset(elem, 100, 5).click_and_hold(on_element=None).move_by_offset(x, y).release().perform()         
            del action 
        time.sleep(1) 

    def toggle_cluster_heatmap_transparency_button(self,layer_name, opt,**kwargs):
        """
        :Usage: esri_toggle_cluster_heatmap_transparency_on_off("Customers","heatmap", 0.2, "step 1")
        :param: layer_name = "Customers" ; opt =transparency  
        :param: value="value=20"  #gets divided by 100 = 0.2
        :paraam: btn_css = btn_css="#CustomersDjt .lyrInfo label[for='Customers_hm']" 
        :param: btn_color= btn_color="sea_green"
        :author = Jesmin
        :date:  11/30/2016     
        """        
        toggle_buttons={'cluster':"#"+ layer_name +"_optsTemp > ul.tg-list > li:nth-child(1) > label",
                        'heatmap':"#"+ layer_name +"_optsTemp > ul.tg-list > li:nth-child(2) > label",
                        'transparency':"#"+ layer_name +"_optsTemp .minput"}
        
        if opt in ("cluster", "heatmap"):
            self.driver.find_element_by_css_selector(toggle_buttons[opt]).click()
            time.sleep(3)   
            
            if self.browser not in ("IE","Firefox"):
                '''verify button color after toggle''' 
                if 'btn_color' in kwargs:
                    expected_color=utillity.UtillityMethods.color_picker(self, kwargs['btn_color'], 'rgb')
                    btn_color =self.driver.find_element_by_css_selector(kwargs['btn_css']).value_of_css_property("border") 
                    actual_color=re.match('.*(rgb.*)', btn_color).group(1)                 
                    utillity.UtillityMethods.asequal(self, expected_color, actual_color, "Step X: verify button color has changed after toggle")   
                        
        elif 'value' in kwargs:  
            el=self.driver.find_element_by_css_selector(toggle_buttons["transparency"])     
            action = ActionChains(self.driver)
            minval = float(el.get_attribute("min") or 0)
            maxval = float(el.get_attribute("max") or 100)
            v = max(0, min(1, (float(kwargs['value']) - minval) / (maxval - minval)))
            width = el.size["width"]
            target = float(width) * v
            action.move_to_element_with_offset(el, target, 1).click().perform()
            time.sleep(2)
            del action          
     
    def esri_minimize_maximize_widget(self, widget_name):
        """
        :Usage: esri_minimize_maximize_widget("toc")
        :param: widget_name = toc or sselection or basemap
        :author = Jesmin
        :date:  11/30/2016
        """           
        widget_icon_title={'toc':"div[class='tocToggle']",
                          'selection_tool':"div[class='stToggle']",
                          'basemap':"div[class='imToggle']"}
        btn_css=widget_icon_title[widget_name]
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(1)    
    
    def esri_select_map_layer_dropdown(self,layer_name): 
        """
        :Usage: esri_select_map_layer_dropdown("Zip3")
        :param: layer_name = "Zip3"
        :author = Jesmin
        :date: 12/06/2016
        """        
        layer_dropdown=Select(self.driver.find_element_by_css_selector("select[id='select:opLayer']"))
        layer_dropdown.select_by_visible_text(layer_name)        
        #print(self.driver.find_element_by_css_selector("select[id='select:opLayer']").is_displayed()) 
        # Verify value is selected   

        
    def verify_map_legend_in_toc_widget(self,layer_name,opt,fex_field_name, using_field_name ):  
        layer_name_css=".lyrContainer .lyrName"
        get_layer_name=[el.get_attribute("title") for el in self.driver.find_elements_by_css_selector(layer_name_css)]
        for i in get_layer_name:
            if layer_name==i:  
                show_tool_button_css="#"+layer_name+"Djt> div > ul.optionsBox > li.optionsBoxBtn" 
                self.driver.find_element_by_css_selector(show_tool_button_css).click()                      
                time.sleep(1)   
                                
                btnZoomToLyr="#"+layer_name+"Djt> div > ul.optionsBox > li.BoxLi > ul > li.goToLyr"  
                btnToggleOpt="#"+layer_name+"Djt > div > ul.optionsBox > li.BoxLi > ul > li.optsIcon"
                btnToggleLyrLegend= "#"+layer_name+"Djt > div > ul.optionsBox > li.BoxLi > ul > li.legIcon"  
                
                options={'zoom_to_layer':btnZoomToLyr,
                          'toggle_options':btnToggleOpt,
                          'toggle_layer_legend':btnToggleLyrLegend}
                
                btn_css=options[opt]                
                self.driver.find_element_by_css_selector(btn_css).click()
                time.sleep(1) 
                
                'verify field name' 
                using_field_name_css="#"+using_field_name+"_Legend"+using_field_name+" > table > tbody > tr > td > span"
                
                """  
                get_using_field_name_css=self.driver.find_element_by_css_selector(using_field_name_css).text                              
                if using_field_name==get_using_field_name_css:                    
                    print("Legend Title matches with the Using Field Name: "+get_using_field_name_css)
                else :                    
                    print("Legend Title DOES NOT match with the Using Field Name: "+get_using_field_name_css)                                     
            else :
                print("Layer name doesn't match")                 
                """ 
                     
                 
    def verify_esri_main_menu_tooltips(self,msg):
        """
        :param : NONE
        :Usage: verify_main_menu_tooltip("Steps xx: )
        :author: Jesmin
        :date:  11/21/2016        """
        expected_tooltips=['Default extent', 'Table of Contents', 'Selection Tools', 'Change Base Map', 'Find my location']
        btn_title=["div[title='Default extent']", "li[title='Table of Contents']", "li[title='Selection Tools']", "li[title='Change Base Map']", "div[title='Find my location']"]
        actual_tooltips=[y.get_attribute("title") for y in [self.driver.find_element_by_css_selector("#mainMenu " + x) for x in btn_title]]
        utillity.UtillityMethods.asequal(self,expected_tooltips, actual_tooltips, msg+"verify Home Button tooltips")
        
                          
    def verify_esri_map_widget_minimize_maximize(self,widget_state,msg):
        """
        :Usage: esri_move_map_widget("toc",600,10)
        :param: minimize or maximized
        :author = Jesmin
        :date = 11/22/2016
        """    
        floating_widget_css = "#lwFloatingPane > div.dojoxFloatingPaneCanvas"
        floating_widget_size_css="#lwFloatingPane"        
        
        get_floating_widget= self.driver.find_element_by_css_selector(floating_widget_css).get_attribute("style")   
        time.sleep(1)  
            
        if widget_state=="minimize":  
            search_string="display: none"    
            matchobj= re.search(search_string, get_floating_widget,re.MULTILINE|re.IGNORECASE)   
            time.sleep(1)    
            search_size="width: 65px"
            get_widget_size= self.driver.find_element_by_css_selector(floating_widget_size_css).get_attribute("style")  
            matchobj_size= re.search(search_size, get_widget_size,re.MULTILINE|re.IGNORECASE)    
            time.sleep(1) 
            utillity.UtillityMethods.asequal(self,search_string, matchobj.group(),msg+"verify widget is minimized") 
           
        else:  #maximized
            #this section isn't working 
            search_string="display: block"  
            matchobj= re.search(search_string, get_floating_widget,re.MULTILINE|re.IGNORECASE)    
            print(matchobj.group()) 
            time.sleep(1)    
            search_size="width: 217px"  
            get_widget_size=self.driver.find_element_by_css_selector(floating_widget_size_css).get_attribute("style")  
            matchobj_size= re.search(search_size, get_widget_size,re.MULTILINE|re.IGNORECASE)    
            print(matchobj_size.group()) 
            time.sleep(1)
            utillity.UtillityMethods.asequal(self,search_string, matchobj.group(),msg+"verify widget is maximized")
                                                 
                 
    def verify_esri_toc_widget_tooltips(self,layer_name,layer_type,msg):
        """
        :param : NONE
        :Usage: verify_main_menu_tooltips("Customers", "point")
        :author: Jesmin
        :date:  11/23/2016 
        """        
        layerName_css= "#lwFloatingPane #"+layer_name +"Djt .lyrName "
        clusterSymbol_css="#"+layer_name +"Djt  .lyrContainer #"+layer_name +"clIcon"
        heatSymbol_css ="#"+layer_name +"Djt .lyrContainer .GeomIconHeat"
        showTooslBtn_css  = "#lwContent #"+layer_name +"Djt .optionsBoxBtn"   
        btnToggleLyrLegend_css = "#lwContent #"+layer_name +"Djt .legIcon"
        btnToggleOpt_css = "#lwContent #"+layer_name +"Djt .optsIcon.optsActive"
        btnZoomToLyr_css="#lwContent #"+layer_name +"Djt .goToLyr" 
        CompletelyTrans_css = "#lwContent #"+layer_name +"Djt #"+layer_name +"_optsTemp  .opacityMin"
        opacity_range_css = "#lwContent #"+layer_name +"Djt #"+layer_name +"_optsTemp  [type='range']"
        CompletelyOpaque_css = "#lwContent #"+layer_name +"Djt #"+layer_name +"_optsTemp  .opacityMax"
        
        polySymbol_css="#"+layer_name +"Djt  .lyrContainer .GeomIconPolygon" 
                
        btn_title = [heatSymbol_css,clusterSymbol_css,layerName_css,showTooslBtn_css,btnToggleLyrLegend_css,
                    btnToggleOpt_css,btnZoomToLyr_css,CompletelyTrans_css,opacity_range_css,CompletelyOpaque_css]
        
        expected_point_tooltips= ["Geometry: Point","Cluster ON",layer_name,"Show tools","Toggle layer legend"
                                ,"Toggle options","Zoom to layer extent","Completely transparent","Opacity: 0.5","Completely opaque"]
        
        expected_poly_tooltips= ["Geometry: Polygon",layer_name,"Show tools","Toggle layer legend"
                                ,"Toggle options","Zoom to layer extent","Completely transparent","Opacity: 0.5","Completely opaque"]     
        actual_tooltips=[] 
        
        if layer_type=="point":
            for i in btn_title:
                get_tooltip= self.driver.find_element_by_css_selector(i)                
                hover = ActionChains(self.driver)
                hover.move_to_element(get_tooltip).perform()
                self.driver.implicitly_wait(2)
                list1 = get_tooltip.get_attribute("title")
                actual_tooltips.append(list1)
                del hover
                self.driver.implicitly_wait(2)               
            utillity.UtillityMethods.as_List_equal(self,expected_point_tooltips,actual_tooltips,msg+"verify tooltips of point layer for all TOC tools.") 
        elif layer_type=="polygon":
            btn_title.remove(heatSymbol_css)
            btn_title.remove(clusterSymbol_css)    
            btn_title.insert(0,polySymbol_css)
            for i in btn_title:
                get_tooltip= self.driver.find_element_by_css_selector(i)                
                hover = ActionChains(self.driver)
                hover.move_to_element(get_tooltip).perform()
                time.sleep(2)
                list1 = get_tooltip.get_attribute("title")
                actual_tooltips.append(list1)
                del hover
                time.sleep(1)                
            utillity.UtillityMethods.as_List_equal(self,expected_poly_tooltips,actual_tooltips,msg+"verify tooltips of polygon layer for all TOC tools.")                  
        else:
            print("this section is for line when feature is available")
    


    def verify_esri_selection_widget_tooltips(self,layer_type,msg):
        """
        :param : NONE
        :Usage: verify_main_menu_tooltips("point")
        :author: Jesmin
        :date: 12/12/2016
        """        
        active_layer_css= "#selectionTools > ul > li:nth-child(1) > ul > li.layerST" 
        zoom_to_layer_extent_css="#selectionTools > ul > li:nth-child(1) > ul > li.goToLyr"
        select_by_extent_css="#selectionTools > ul > li:nth-child(3) > ul > li.selectByExtent"
        select_by_polygon_css="#selectionTools > ul > li:nth-child(3) > ul > li.selectByPolygon"
        select_by_distance_css="#selectionTools > ul > li:nth-child(3) > ul > li.selectByDistance"
        pan_css="#selectionTools > ul > li:nth-child(3) > ul > li.panMap"
        unselect_css="#selectionTools > ul > li:nth-child(3) > ul > li.clearSelection2"
        clear_selection_css="#selectionTools > ul > li:nth-child(3) > ul > li.clearAll"
        zoom_to_selection_css="#selectionTools > ul > ul:nth-child(6) > li"
        
        poly_select_by_line_css="#selectionTools > ul > li:nth-child(3) > ul > li.selectByPolyline"   
          
        btn_title = [active_layer_css,zoom_to_layer_extent_css,select_by_extent_css,select_by_polygon_css,
                     select_by_distance_css,pan_css,unselect_css,clear_selection_css,zoom_to_selection_css]
        
        expected_tooltips= ["Active layer","Zoom to layer extent","Select features within an extent","Select features within a polygon",
                          "Select features within a distance","Pan","Unselect","Clear Selection","Zoom to Selection"]
                
        actual_tooltips=[] 
        
        if layer_type=="point":
            for i in btn_title:
                get_tooltip= self.driver.find_element_by_css_selector(i)                
                hover = ActionChains(self.driver)
                hover.move_to_element(get_tooltip).perform()
                time.sleep(2)
                list1 = get_tooltip.get_attribute("title")
                actual_tooltips.append(list1)    
                del hover
                self.driver.implicitly_wait(2)           
            utillity.UtillityMethods.as_List_equal(self,expected_tooltips,actual_tooltips,msg+"verify tooltips of all Selection tools  for point layer.") 
                
        elif layer_type=="polygon":
            btn_title.remove(select_by_distance_css)       
            btn_title.insert(4,poly_select_by_line_css)
            expected_tooltips.remove("Select features within a distance")
            expected_tooltips.insert(4,"Select features intersecting a line")
            for i in btn_title:
                get_tooltip= self.driver.find_element_by_css_selector(i)                
                hover = ActionChains(self.driver)
                hover.move_to_element(get_tooltip).perform()
                time.sleep(2)
                list1 = get_tooltip.get_attribute("title")
                actual_tooltips.append(list1)
                del hover
                time.sleep(1)                 
            utillity.UtillityMethods.as_List_equal(self,expected_tooltips,actual_tooltips,msg+"verify tooltips of all Selection tools for polygon layer.")                  
        else:
            print("this section is for line when feature is available")


              
    def verify_esri_map_layer_on_off(self,layer_name,default_check,msg):
        """
        :Usage: verify_esri_map_layer_on_off('Layer 1', True,"Step X: ....")
        :param: layer_name = "Customers" ; layer_visible = True or False
        :author = Niranjan
        :date:  12/01/2016
        """ 
        layers=self.driver.find_elements_by_css_selector("#lwFloatingPane .layerList")
        checked=layers[[el.text.strip() for el in layers].index(layer_name)].find_element_by_css_selector("li[class^='LyrCb']").get_attribute("class")
        time.sleep(1)

        checked_status = True if bool(re.match(r'.*icon-check.*', checked)) else False       
        if default_check==True:
            utillity.UtillityMethods.asequal(self,True, checked_status, msg+"layer is OFF (locator=  "+checked+" )")
        else:
            utillity.UtillityMethods.asequal(self,False, checked_status, msg+"layer is OFF (locator= "+checked+" )")
      
              
    def verify_esri_map_cluster_image_text(self, layer_name, expected_no_of_clusters, index, str_expected_cluster_text, msg):
        """
        :Usage: verify_esri_map_clusters_text("Customers", 4,0, 96, "Step 10: ")
        :param: parent_css=g[id^='Customers-(cl)_layer'] ; expected_no_of_clusters=4;  index=0, 1,2...
        :author = Niranjan
        :date:  12/07/2016 
        """
        cluster_images=self.driver.find_elements_by_css_selector("g[id^='"+layer_name+"-(cl)_layer'] image")
        print(len(cluster_images))
        cluster_texts=self.driver.find_elements_by_css_selector("g[id^='"+layer_name+"-(cl)_layer'] text")
        print(cluster_texts[index].text.strip())          
        #To verify number of clusters. 
        utillity.UtillityMethods.asequal(self.driver,expected_no_of_clusters, len(cluster_images), msg + "verify total number of clusters at current zoom level.") 
        #To verify the particular cluster image
        utillity.UtillityMethods.asequal(self.driver,True, bool(re.search('GreenPin1LargeB.png', cluster_images[index].get_attribute("xlink:href"))), msg + "verify green pin cluster image.")
        #To verify the cluster text
        utillity.UtillityMethods.asequal(self.driver,str_expected_cluster_text, cluster_texts[index].text.strip(), msg + "verify the text of cluster")
        
        
    def verify_esri_map_layer_cluster_on_off(self,layer_name,int_clusters,msg):
        """
        :Usage: verify_esri_map_layer_cluster_on_off("Customers", 4,0, 96, "Step 10: ")
        :param: layer_name=Customers ; default_check= True or False;  msg= "Step xx: "
        :author = Jesmin
        :date:  12/08/2016 
        """        
        cluster_images=self.driver.find_elements_by_css_selector("g[id^='"+layer_name+"-(cl)_layer'] image") 
        if len(cluster_images) != 0:    
            utillity.UtillityMethods.asequal(self.driver,int_clusters, len(cluster_images), msg + "verify clusters is ON") 
        else :
            len(cluster_images)==0
            utillity.UtillityMethods.asequal(self.driver,0, len(cluster_images), msg+"verify cluster is OFF")
        

    def verify_esri_basemap_list(self,exptd_basemap_list,msg): 
        """
        :Usage: verify_esri_basemap_list("Step 10: ")
        :param: msg= "Step xx: "
        :author Jesmin
        :date:  12/15/2016 
        """ 
          
        get_basemaps_title=self.driver.find_elements_by_css_selector(".esriBasemapGalleryNode")
        
        actual_basemap_list=[]
        
        for elem in get_basemaps_title: 
            list1=elem.text.strip()
            actual_basemap_list.append(list1)  
        
        print(actual_basemap_list)   
        utillity.UtillityMethods.asequal(self.driver,exptd_basemap_list, actual_basemap_list, msg+"verify list of basemap in basemap widget match ") 
        
        
    def verify_esri_map_widget_size_location(self,widget,x,y,width,height,msg):
            """
            :Usage: verify_esri_map_widget_size_location("toc",121,122,98,219)
            :param: widget="toc" ; x= 121 ; y= 122; height= 98;  width= 219;  msg="Step 03: "
            :author Jesmin
            :date:  12/6/2016 
            """ 
            options={'toc':"#lwFloatingPane",
                     'selection':"div[class='stToggle']",
                     'basemap':"div[class='imToggle']"} 
        
            get_widget= self.driver.find_element_by_css_selector(options[widget])                                                      
            actual_loc=get_widget.location
            print(actual_loc)
            actual_size=get_widget.size  
            print(actual_size)
            #print(actual_loc)
            #print(actual_size)
            
            bol1= True if (actual_loc["x"]==x and actual_loc["y"]==y) else False  
            time.sleep(1)
            utillity.UtillityMethods.asequal(self.driver,True,bol1,msg+"location")
            time.sleep(1)
            
            bol2= True if (actual_size["width"]==width and actual_size["height"]==height) else False
            time.sleep(1)
            utillity.UtillityMethods.asequal(self.driver,True,bol2,msg+"size")    
                      
        
    def esri_selection_widget_extent_unselect_tools(self,opt,src_loc, tar_loc): 
        """
        :Usage: esri_select_map_layer_dropdown(source_elem,target_elem)
        :param: src_loc = driver.find_element_by_css_selector("#"Customers_layer > circle:nth-child(61)")
                tar_loc = driver.find_element_by_css_selector("#"Customers_layer > circle:nth-child(329)")
        :author = Niranjan
        :date: 12/20/2016
         
        option={"extent":"#selectionTools > ul > li:nth-child(3) > ul > li.selectByExtent", 
                "unselect":"#selectionTools > ul > li:nth-child(3) > ul > li.clearSelection2"} 
        """
        self.esri_selection_widget_click_tools(opt)
        time.sleep(1)
                  

        action1=""   
        source = self.driver.find_element_by_css_selector(src_loc)
        target = self.driver.find_element_by_css_selector(tar_loc)
        self.driver.implicitly_wait(6)    
        try:
            action1=ActionChains(self.driver)
            action1.click_and_hold(source).perform()  
            action1.move_to_element(target).perform()
            action1.release().perform()   
        except:
            print("except1")
            del action1
            action1=ActionChains(self.driver)
            action1.move_to_element(target).perform()
            try:
                action1.release().perform()
            except:
                pass                
            del action1              
            time.sleep(2)   
        
    def esri_selection_widget_polygon_tool(self,src_loc,tar_loc):
        """
        :Usage: esri_selection_widget_polygon_tool(source,target1,target2)
        :param: source=driver.find_element_by_css_selector("#Customers_layer > circle:nth-child(3)")       
                target1=driver.find_element_by_css_selector("#Customers_layer > circle:nth-child(299)") 
                target2=driver.find_element_by_css_selector("#Customers_layer > circle:nth-child(33)")
        :author = Jesmin
        :date:  12/27/2016 
        """         
 
        source = self.driver.find_element_by_css_selector(src_loc)
        target = self.driver.find_element_by_css_selector(tar_loc)
        self.driver.implicitly_wait(6)    
        try:
            action1=ActionChains(self.driver)
            action1.click_and_hold(source).perform()  
            action1.move_to_element(target).perform()
            action1.release().perform()   
        except:
            print("except1")
            del action1
            action1=ActionChains(self.driver)
            action1.move_to_element(target).perform()
            try:
                action1.release().perform()
            except:
                print("except2")                
            del action1              
            time.sleep(2)       

      
               
        
    def esri_selection_widget_distance_tool(self,opt,value, unit,point_css):
        """
        :Usage: esri_selection_widget_distance_tool("10", "km","#Customers_layer > circle:nth-child(93)")
        :param: value =
        :author = Jesmin
        :date:  12/22/2016 
        """ 
        self.esri_selection_widget_click_tools(opt)
        time.sleep(1)
        #self.driver.find_element_by_css_selector("#selectionTools > ul > li:nth-child(3) > ul > li.selectByDistance").click()        
        
        self.driver.find_element_by_css_selector("#_distanceTxt").send_keys(value)
        time.sleep(2)
        
        self.driver.find_element_by_css_selector("#dist_units").click()
        time.sleep(2)
        Select(self.driver.find_element_by_css_selector("#dist_units")).select_by_visible_text(unit)  
           
        self.driver.find_element_by_css_selector(point_css).click()
        time.sleep(2)
                
      
                 
    def verify_esri_map_selected_point_image_text(self,msg):
        """
        :Usage: verify_esri_map_clusters_text("Customers", 4,0, 96, "Step 10: ")
        :param: 
        :author = Jesmin
        :date:  12/21/2016 
        """        
        points=int(self.driver.find_element_by_css_selector("#selectionTools > ul > ul:nth-child(6) > li").text.strip())
        act_selected_points=points
        #To verify number of point selected.        
        utillity.UtillityMethods.as_GE(self.driver,act_selected_points, 5, msg + "verify more than 5 number of points selected") 
        print(act_selected_points)
        
        #To verify the selected image file
        selected_image=self.driver.find_element_by_css_selector("#SelectedGraphics_layer > image:nth-child(2)")
        utillity.UtillityMethods.asequal(self,True, bool(re.search('esriCartographyMarker_73_Yellow.png', selected_image.get_attribute("xlink:href"))), msg + "verify circular yellow selected image.")
        return(act_selected_points)
            
    def verify_esri_map_selected_unselected_points(self,msg): 
        """
        :Usage: verify_esri_map_selected_unselected_points(True, "Step 10: ")
        :param: value = True or False
        :author = Jesmin
        :date:  12/21/2016 
        """       
        try:
            self.driver.find_element_by_css_selector("#SelectedGraphics_layer").is_displayed()  
            actual_value=self.driver.find_element_by_css_selector("#selectionTools > ul > ul:nth-child(6) > li").get_attribute('innerHTML')            
            utillity.UtillityMethods.as_GE(self,int(actual_value),0,msg)
        except NoSuchElementException: 
            utillity.UtillityMethods.asequal(self,True,True,msg)
            
         
  
    def pynput_double_click(self,src_loc):
        """
        :Usage: pynput_double_click(""#SelectedGraphics_layer"")
        :param: 
        :author = Niranjan
        :date:  12/28/2016 
        """     
        mouse = Controller()        
        source=self.driver.find_element_by_css_selector(src_loc)
        x=source.location['x']
        y=source.location['y']
        mouse.position= (x, y)
        time.sleep(5)
        mouse.click(Button.left, 2)
        time.sleep(2)
        mouse.click(Button.left, 2)
        
        
    def click(self,src_loc):   
        """
        :Usage: click("#SelectedGraphics_layer"")
        :param: 
        :author = Niranjan
        :date:  12/28/2016 
        """ 
        source = self.driver.find_element_by_css_selector(src_loc)
        try:
            action1=ActionChains(self.driver)        
            action1.click(source).perform()
        except:
            print("except1")
            del action1
            action1=ActionChains(self.driver)
            action1.click(source).perform()
        del action1
        time.sleep(2)       
        
        
    def verify_esri_map_toc_widget_legend_text(self,legend_css,expected_legend,msg): 
        """
        :Usage: 
        :param:         
        legend_css="#Customers_Legend_Customers"
        expected_legend=['CUST_TYPE', 'Repeat Customer', 'Valued Customer', 'Hi-Value Customer', 'others']
        msg="Step 08:"        
        :author = Niranjan
        :date:  01/09/17
        """  
        actual_legend=self.driver.find_element_by_css_selector(legend_css).text.split('\n')
        print(actual_legend)
        utillity.UtillityMethods.asequal(self,expected_legend,actual_legend,msg + "verify layer legend text")
                

    def verify_esri_map_toc_widget_legend_color(self,obj_css,expected_fill_color,expected_stroke_color,msg): 
        """
        :Usage:= verify_esri_map_toc_widget_legend_color(obj_css,expected_fill_color, expected_stroke_color,msg) 
        :param: obj_css="div[id='US County_Legend_US County'] svg path"      
                svg_position= 0 
                expected_fill_color="lime_green"
                expected_stroke_color="blue"   
                msg="Step 13: "              
        :author = Jesmin
        :date:  01/09/17
        """ 
        #To verify legend shape Color & outline :
        get_legend=self.driver.find_elements_by_css_selector(obj_css)  
        fill_color=utillity.UtillityMethods.color_picker(self, expected_fill_color, 'rgba')
        stroke_color=utillity.UtillityMethods.color_picker(self, expected_stroke_color, 'rgba') 

        actual_fill_color = [Color.from_string(i.get_attribute("fill")).rgba for i in get_legend if i.get_attribute("fill") != 'none']
        actual_stroke_color= [Color.from_string(i.get_attribute("stroke")).rgba for i in get_legend if i.get_attribute("stroke") !='none']  

        utillity.UtillityMethods.asin(self, fill_color, actual_fill_color , msg + "verify layer legend symbol fill color")
        utillity.UtillityMethods.asin(self, stroke_color, actual_stroke_color , msg + "verify layer legend symbol outline color")
        
        
    def verify_esri_basemap_image(self,image_path,msg): 
        """
        :Usage: verify_esri_basemap_list("Step 10: ")
        :param: msg= "Step xx: "
        :author Jesmin
        :date:  02/07/17
        """ 
        actual_image_path_css= "#emfobject1_container img[src*='https://services.arcgisonline.com/ArcGIS/rest/services/']"  
        get_actual_image_path=self.driver.find_element_by_css_selector(actual_image_path_css).get_attribute("src")    
        #print(get_actual_image_path)       
        utillity.UtillityMethods.asin(self.driver,image_path, get_actual_image_path, msg+"verify actual basemap image match") 
       

    def verify_esri_map_feature_tooltip(self,point_poly_css,tooltip_data,msg):
        """
        :Usage: verify_esri_map_feature_tooltip("g[id^='Zip5'] > path:nth-child(2)", "COLOR_NAMES: GREEN", "Step 08: ")
        :param: msg= "Step xx: "
        :author Jesmin
        :date:  02/13/17
        """         
        get_record=self.driver.find_element_by_css_selector('.contentPane').text.split('\n')        
        print(get_record)
        utillity.UtillityMethods.asin(self.driver,tooltip_data,get_record,msg+"Verify infowindow shows correct record for selected field")
           
    #under construction     
    def verify_esri_map_geometry_icon(self, point_poly_css,exptd_icon_name,msg):
        """
        :Usage: verify_esri_map_feature_tooltip("li[id^='Zip5 Sale'] > div > ul.lyrItems > li.GeomIconPolygon"", "polygon", "Step 08: ")
        :param: msg= "Step xx: "
        :author Jesmin
        :date:  02/13/17
        """                 
        get_icon=self.driver.find_element_by_css_selector(point_poly_css).get_attribute("title")
        #print(geo_icon.lower())
        utillity.UtillityMethods.asin(self.driver,exptd_icon_name,get_icon.lower(),msg+"Verify geometry icons for layer")      
        
        
        
    def select_autolink_tooltip_menu(self, parent_table_css, row, col, menu_path, msg):
        """
        :Usage: as_esri_map_runobj.select_autolink_tooltip_menu(self, "table", 12, 4,"Show Locations","Step 14a: verify 'AUTOLINK_TARGET01' fex is listed") 
        :author Niranjan
        :date:  03/01/17
        """  
        driver = self.driver
        move_cursor=parent_table_css
        menus=menu_path.split('->')
        cell_css=move_cursor + " > tbody > tr:nth-child(" + str(row) + ") > td:nth-child(" + str(col) + ") > a"
        tooltip_css="span[class*='tdgchart-tooltip']>div>ul>li"  
        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_css_selector(cell_css)).click().perform()
        del action        
        time.sleep(2)        
        
        tooltips=driver.find_elements_by_css_selector(tooltip_css) 
        for i in range(len(tooltips)):
            line1=tooltips[i].text.strip()
            if menus[0] in (re.sub('>', '', line1) if bool(re.match(r'^>', line1)) else tooltips[i].text.strip()).split('\n'):
                tooltips[i].click()
                break
            
        tooltip_css="div[class='tdgchart-submenu']>div>ul>li"
        tooltips1=self.driver.find_elements_by_css_selector(tooltip_css)
        
        if len(menus) > 1:
            for i in range(len(tooltips1)):
                if(tooltips1[i].text == menus[1]):
                    utillity.UtillityMethods.asequal(self, True, True, msg)
                if menus[1] in (tooltips1[i].text.strip()).split('\n'):
                    tooltips1[i].click()
                    break
                
    def click_on_bar_chart_tooltip(self,raiser_css,tooltip_css,menus):  
        ''' 
        :param: tooltip_css= "#jschart_HOLD_0 span[id='tdgchart-tooltip']  li[class='tdgchart-tooltip-pad tdgchart-tooltip-hover tdgchart-tooltip-pointer']"  
                raiser_css=  "#jschart_HOLD_0 [class*='riser!s1!g1!mbar!']"
                menus= "Show Zip Location"
        :Author: Jesmin
        '''
        obj_locator=self.driver.find_element_by_css_selector(raiser_css)    
        action1=ActionChains(self.driver)    
        action1.move_to_element(obj_locator).perform()
        del action1
        time.sleep(2)
        tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
        print([el.text.strip() for el in tooltips])
        tooltips[[el.text.strip() for el in tooltips].index(menus)].click()
                        
    #def verify_zoom_level(self,initial_zoom,after_zoom,msg):  