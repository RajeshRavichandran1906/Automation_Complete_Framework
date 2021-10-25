from selenium.webdriver.common.by import By
class InfoassistLocators(object):
    
    '''Ribbon Menu Option'''
    text_area = (By.CSS_SELECTOR, '#ftext')
    HomeTab= (By.ID, "HomeTab_tabButton")
    FormatTab= (By.ID, "FormatTab_tabButton")
    ChangeChartType = (By.ID, "HomeAVChart")
    calculation = (By.ID, 'HomeCalcMenuBtn')
    define_input = (By.ID, 'fname')
    format_button = (By.ID, 'btnFormat')
    format_ok = (By.ID, 'fmtDlgOk')
    filter_creator_ok = (By.ID, 'fldCreatorOkBtn')
    mvv = (By.XPATH, '//div[.="MYY"]')
    
    '''COMMON'''
    common_xpath = '//td[contains(text(),"{0}")]' #call this string and pass required string 
    
    '''FIELDS'''
    SearchField = (By.CSS_SELECTOR, 'input#metaDataSearchTxtFld')
    Selected_Field = (By.XPATH, '//*[contains(@class,"selected")]/td')
    order_date = (By.XPATH, '//img[@src="/ibi_apps/dhtml/images/qb/column_g_16.png"]')
    
    '''Add Fields'''
    Selected_Field_text = (By.XPATH, '//*[contains(@class,"selected")]/td')
    Selected_Field_image = (By.XPATH, '//*[contains(@class,"selected")]/td/img[2]')
    Initial_RC_Menu = (By.XPATH, "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'Sum')]")
    Selected_RC_Menu = (By.XPATH, '//div[contains(@style,"inherit")]/div/table/tbody/tr[contains(@bi-moz-focused,"true")]/td[2]')
    Initial_RC_Submenu_img = (By.XPATH, "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'Color')]/../td/img")
    Initial_RC_Submenu_Grid_img = (By.XPATH, "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'Rows')]/../td/img")
    Selected_RC_Submenu = (By.XPATH, '//div[contains(@style,"inherit")]/div/table/tbody/tr[contains(@bi-moz-focused,"true")]/td[2]')
    
    ''' Module Save IA > Locators  saved here'''
    error_message = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_text1 > table:nth-child(1) > tbody > tr > td:nth-child(2) > div > pre > h5')
    error_message_close = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_menu1 > div > div > img')
    ia = (By.ID, 'applicationButton')
    new = (By.ID, 'optionsNewBtn')
    open = (By.ID, 'optionsOpenBtn')
    save = (By.ID, 'optionsSaveBtn')
    save_as = (By.ID, 'optionsSaveAsBtn')
    run = (By.ID, 'optionsRunBtn')
    close = (By.ID, 'optionsCloseBtn')
    app_option = (By.ID, 'appOptionsButton')
    app_menu = (By.ID, 'applicationMenu')
    open_window = (By.ID, 'dlgIbfsOpenFile7')
    save_fex = (By.ID, 'IbfsOpenFileDialog7_btnOK')  
    cancel = (By.ID, 'IbfsOpenFileDialog7_btnCancel')
    result_area = (By.ID, 'resultArea')
    input_filename = (By.XPATH, '//*[@id="IbfsOpenFileDialog7_cbFileName"]/input')


    '''Filter pane & prompt > Locators  saved here'''
    prompt_title = (By.CSS_SELECTOR, '#LOBJC200 > table > tbody > tr:nth-child(1) > td > div')
    aggregation_option = (By.CSS_SELECTOR, '#FieldAggregation')
    cancel_filter = (By.ID, 'avFilterCancelBtn')
    filter_menu = (By.CSS_SELECTOR, '#FieldFilter')
    clickOK = (By.CSS_SELECTOR, '#avFilterOkBtn')
    searchValues = (By.ID, 'avSearchValueText')  
    filterPane = (By.ID, 'qbFilterWindow')
    searchBox = (By.ID, 'avSearchValueText')
    operatorDropdown = (By.XPATH, "//div[contains(@id,'avAlphaOperatorComboBox')]/div/div[2]")
    changeOperator_notequal = (By.XPATH, "//*[contains(text(),'Not equal to')]")
    changeOperator_equal = (By.XPATH, "//*[contains(text(),'Equal to')]")
    sortDropdown = (By.XPATH, "//div[contains(@id,'avfSortValuesComboBox')]/div/div[2]")
    sortOption = (By.XPATH, "//div[contains(text(),'Descending')]")
    uncheckShowPrompt = (By.XPATH, "//div[contains(@id,'avFilterShowPrompt')]/input")
    filterpane_scroll = (By.XPATH, '//*[@class="bi-scroll-bar scroll-bar-vertical"]//div[starts-with(@id, "BiMoveHandle")]')
    United_States_Checked = (By.XPATH, '//input[@checked="checked" and @value="United States"]')
    prompt_dropdown = (By.XPATH, "//*[contains(@src,'ar_images/irbpoparw.png')]")
    prompt_option_dropdown = '//td[contains(text(),"{0}")]'
    filter_pane_right_click_menus = '//td[contains(text(),"{0}")]'
    prompts =  '//*[contains(@id,"Prompt_{0}")]//form[contains(@id, "slider")]'  
    slider_min = '//span[contains(@id,"s_min")]'
    slider_max = '//span[contains(@id,"s_max")]'

    ''' Run menu icon & option > Locators  saved here'''
    run_menu_icon = (By.XPATH,"//div[contains(@onclick,'toggleBottomMenu(1)')]")
    grid_icon = (By.XPATH, "//span[contains(@onclick,'mshowReport(1)')]/div")
    reset_icon = (By.XPATH, "//span[contains(@onclick,'mresetDashboard(1)')]/div")
    removeFilter_icon = (By.XPATH,"//span[contains(@onclick,'ibiChart.removeFilter(-1,1)')]/div")

    '''Filter pane Range > Locators  saved here'''
    range_operatorDropdown = (By.XPATH, "//div[contains(@id,'avOperatorComboBox')]/div/div[2]")
    changeOperator_GT_orequalto = (By.XPATH, "//*[contains(text(),'Greater than or equal to')]")
    changeOperator_LT_orequalto = (By.XPATH, "//*[contains(text(),'Less than or equal to')]")
    changeOperator_Range = (By.XPATH, "//*[contains(text(),'Range')]")
    sort_Asc = (By.XPATH, "//div[contains(text(),'Ascending')]")
    From = (By.XPATH, "//div[contains(@id,'avfFromValue')]/input")
    Starting_Date = (By.XPATH,"//div[contains(text(),'Starting Date')]/../div/input")
    Ending_Date = (By.XPATH,"//div[contains(text(),'Ending Date')]/../div/input")

    '''Query Pane > Locators saved here'''
    query_pane = (By.ID, 'queryBoxColumn')
    field_querypane = '//*[contains(text(),"{0}")]/img[2]'
 
    '''Verify chart values'''
    tooltip1_name = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[1]/td[1]")
    tooltip1_value = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[1]/td[2]")
    tooltip2_name = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[2]/td[1]")
    tooltip2_value = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[2]/td[2]")
    tooltip3_name =  (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[3]/td[1]")
    tooltip3_value = (By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody/tr[3]/td[2]")


    '''Map Related Locators'''
    pan = (By.CSS_SELECTOR, "[id*='SelectionButton']")
    lasso_options = ".//*[@id='ibi$tt$1']/span[contains(text(), '{0}')]"
    lasso ='#layerId_0_layer > circle.riser\\21 s0\\21 g{0}\\21 mmarker'
    lasso_chart = "svg > g.chartPanel > g:nth-child(2) > g > g > g > rect.riser\\21 s{0}\\21 g{1}\\21 mbar"
    lasso_chart_xpath= "//*[contains(@class,'{0}!{1}!{2}')]"
    lasso_chart_xpath_rowcolumn="//*[contains(@class,'{0}!{1}')]"
    marker_options = "// *[contains(text(), '{0}')]"
    bubble_legend = (By.CSS_SELECTOR,'#MAINTABLE_wbody2_f > div > svg > g.legend > g > g')
    
    '''Result area locators '''  
    
    x_label = (By.CSS_SELECTOR, '#MAINTABLE_wbody1_f > svg > g.chartPanel > g:nth-child(4) > g:nth-child(2)')
    legend_clip = (By.CSS_SELECTOR, '#MAINTABLE_wbody1_f > svg > g.legend-clip > g > g:nth-child(2) > g')
    querycolumn = (By.XPATH, "//*[@id='queryTreeColumn']/*[@class='bi-tree-view-body-content']/table/tbody") 
    
    '''Verify Filter Prompt checkbox values'''
    filter_prompt_checked = "//span[contains(text(),'{0}')]/../../../../tr/td/div/form/div/table/tbody/tr/td/div/input[@checked='checked']"

    '''Verify number of risers displayed in a chart'''
    no_of_risers = (By.XPATH, "//*[@class='risers']/*/*[contains(@tdgtitle,'p')]")
 
    ''' Drag and Drop Visualization to required position'''  
   
    chart_type= "//div[contains(@id,'BoxLayoutMiniWindow')]/div/div[contains(text(),'{0}')]"
    
    Left_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div")
    Left = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div[2]")
    
    Top_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div")
    Top = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[2]")
    Centre = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[3]")
    Bottom = (By.XPATH , "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[4]")
    Bottom_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div/div[5]")
    
    Right = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div[4]")
    Right_most = (By.XPATH, "//div[starts-with(@id,'BoxLayoutIconsMarker')]/div[5]")
    
    '''Verify Color legend values (legend values)'''
    
    color_legend = (By.XPATH,"//*[@class='legend']")
    #Grid Verification Row
    rows = (By.CSS_SELECTOR, '#MAINTABLE_wbody1_f > svg > g.chartPanel > g > g.rowHeader > g > g.rowLabels')
    measure_grid = (By.CSS_SELECTOR, '#MAINTABLE_wbody1_f > svg > g.chartPanel > g > g.innerTable > g > g.labels')
    #Grid Slider
    slider_grid = (By.CSS_SELECTOR, 'svg > g.chartPanel > g > g.scrollBars > g > g > rect')
    
    '''Preview Area'''
    move_to_title = "//div[contains(@id,'BoxLayoutMiniWindow')]/div/div[contains(text(),'{0}')]" #Function 53
    preview_menu="//div[contains(@class,'mini-window-check')]/div/div[contains(@class,'{0}-button')]"  #Function 53
    multi_drill = "//li[contains(text(),'{0}')]/div[contains(@class,'tdgchart-submenu')]/div/ul/li[*]/span[contains(text(),'{1}')]" #Function 15
    filter = "//*[@id='tdgchart-tooltip']/div/ul/li[*]/span[contains(text(),'{0}')]" #Function 15
    drill = "//*[@id='tdgchart-tooltip']/div/ul/li[contains(text(),'{0}')]" #Function 15
    
    '''Run Document Chart Title'''
    run_chart_title=(By.CSS_SELECTOR, "#MAINTABLE_0 .title")
    run_chart_title1=(By.CSS_SELECTOR, "#MAINTABLE_3 .title")
    
    '''Preview Chart Title'''
    preview_chart_title=(By.CSS_SELECTOR, "#TableChart_1 .title")
    
