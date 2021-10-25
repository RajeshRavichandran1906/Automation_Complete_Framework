from selenium.webdriver.common.by import By
class VisualizationResultareaLocators(object):
    
    '''Preview Area'''
    move_to_title = "//div[contains(@id,'BoxLayoutMiniWindow')]/div/div[contains(text(),'{0}')]" #Function 53
    preview_menu="//div[contains(@class,'mini-window-check')]/div/div[contains(@class,'{0}-button')]"  #Function 53
    show_data = "//div[contains(@id,'Popup')]//*[contains(@class,'menu-table')]//*[.='{0}']"
	
    ''' Chart '''
    resultarea = (By.CSS_SELECTOR, '[id*=Chart_1]')
    default_riser=(By.CSS_SELECTOR, "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']")
    no_of_risers = (By.XPATH, "//*[@class='risers']/*/*[contains(@tdgtitle,'p')]")
    riser = "[id^='{0}'] [class*='{1}']"
    tooltip_last = ".//*[@id='tdgchart-tooltip']/div/ul//li[last()]"
    drill_menu1 = "//*[@id='tdgchart-tooltip']/div/ul/li[*]//*[contains(text(),'Drill {0}')]"
    drill_menu1_with_menu2 = "//*[@id='tdgchart-tooltip']/div/ul/li[*][contains(text(),'Drill {0}')]/div/div/ul/li/span[contains(text(),'{1}')]"
    drill_menu2="//*[@id='tdgchart-tooltip']/div/ul//li[contains(text(),'{0}')]"
    drill_menu2_with_menu1=".//*[@id='tdgchart-tooltip']/div/ul/li[*][contains(text(),'{0}')]/div/div/ul/li/span[contains(text(),'{1}')]"
    riser_xpath ="//*[contains(@id,'{0}')]//*[contains(@class,'{1}')]"
    bar_xlabel= "//*[contains(@class,'xaxis')and contains(@class,'title')]"
    '''    Legend '''
    legend_clip = (By.CSS_SELECTOR, '#MAINTABLE_wbody1_f > svg > g.legend-clip > g > g:nth-child(2) > g')
    color_legend = (By.XPATH,"//*[@class='legend']")
    row_header = "div[id^={0}] text.rowHeader-label"
    size_legend = "div[id^={0}] text.sizeLegend-title"
    
    '''     Drag Drop Visualization    '''
    chart_type= "//div[contains(@id,'BoxLayoutMiniWindow')]/div/div[contains(text(),'{0}')]"
    Prompts = "//div[contains(@id,'BoxLayoutFilterBox')]/div/div[contains(text(),'{0}')]"
    Left_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div")
    Left = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div[2]")
    Top_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div")
    Top = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[2]")
    Centre = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[3]")
    Bottom = (By.XPATH , "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[4]")
    Bottom_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[5]")
    Right = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div[4]")
    Right_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div[5]")
    
    '''        Tooltip - Verify chart values'''
    tooltip1_name = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[1]/td[1]")
    tooltip1_value = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[1]/td[2]")
    tooltip2_name = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[2]/td[1]")
    tooltip2_value = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[2]/td[2]")
    tooltip3_name =  (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[3]/td[1]")
    tooltip3_value = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[3]/td[2]")
    multi_drill = "//li[contains(text(),'{0}')]/div[contains(@class,'tdgchart-submenu')]/div/ul/li[*]/span[contains(text(),'{1}')]" #Function 15
    filter = "//*[@id='tdgchart-tooltip']/div/ul/li[*]/span[contains(text(),'{0}')]" #Function 15
    drill = "//*[@id='tdgchart-tooltip']/div/ul/li[contains(text(),'{0}')]" #Function 15
    
    '''     Lasso '''
    lasso_options = ".//*[@id='ibi$tt$1']/span[contains(text(), '{0}')]"
    lasso ='#layerId_0_layer > circle.riser\\21 s0\\21 g{0}\\21 mmarker'
    lasso_chart = "svg > g.chartPanel > g:nth-child(2) > g > g > g > rect.riser\\21 s{0}\\21 g{1}\\21 mbar"
    lasso_chart_xpath= "//*[contains(@class,'{0}!{1}!{2}')]"
    lasso_chart_xpath_rowcolumn="//*[contains(@class,'{0}!{1}')]"
    
    
    ''' Map '''
    pan = (By.CSS_SELECTOR, "[id*='SelectionButton']")
    bubble_map_riser = "//*[contains(@id,'{0}_f_com-esri-map') and contains(@overflow,'hidden')]/*[contains(@id,'layerId')]/*[contains(@class,'{1}!{2}!{3}')]"
    
    ''' Grid '''
    slider_grid = (By.CSS_SELECTOR, 'svg > g.chartPanel > g > g.scrollBars > g > g > rect')
    rows = (By.CSS_SELECTOR, '#MAINTABLE_wbody1_f g .rowLabels')
    measure_grid = (By.CSS_SELECTOR, '#MAINTABLE_wbody1_f g .labels')
    
    '''Error  Message '''
    error_message = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_text1 > table:nth-child(1) > tbody > tr > td:nth-child(2) > div > pre > h5')
    error_message_close = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_menu1 > div > div > img')
    