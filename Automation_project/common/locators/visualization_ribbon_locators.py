from selenium.webdriver.common.by import By
class VisualizationRibbonLocators(object):
    
    Appbtn = (By.CSS_SELECTOR, "#applicationButton img")
    
    tab_css="#IaToolbar #{0}Tab_tabButton" 
    
    
    ''' Series '''
    marker_options = "// *[contains(text(), '{0}')]"
    series_marker = (By.CSS_SELECTOR, "#SeriesChartMarker img")
    series_trendline = (By.CSS_SELECTOR, "#SeriesChartTrendline img")
    
    '''Quick Access Toolbar'''
    error_message = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_text1 > table:nth-child(1) > tbody > tr > td:nth-child(2) > div > pre > h5')
    error_message_close = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_menu1 > div > div > img')
   
    '''IA-Menu'''
    menu_new = (By.CSS_SELECTOR, "#applicationMenu #optionsNewBtn img")
    menu_open = (By.CSS_SELECTOR, "#applicationMenu #optionsOpenBtn img")
    menu_save = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveBtn img")
    menu_save_as = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveAsBtn img")
    menu_run = (By.CSS_SELECTOR, "#applicationMenu #optionsRunBtn img")
    menu_close = (By.CSS_SELECTOR, "#applicationMenu #optionsCloseBtn img")
    menu_options = (By.CSS_SELECTOR, "#applicationMenu #appOptionsButton img")
    menu_exit = (By.CSS_SELECTOR, "#applicationMenu #appExitButton img")
    
    '''IA-ToolBar'''
    toolbar_new = (By.CSS_SELECTOR, "#topToolBar #newButton img")
    toolbar_open = (By.CSS_SELECTOR, "#topToolBar #openReportButton img")
    toolbar_save = (By.CSS_SELECTOR, "#topToolBar #saveButton img")
    toolbar_undo = (By.CSS_SELECTOR, "#topToolBar #undoButton img")
    toolbar_redo = (By.CSS_SELECTOR, "#topToolBar #redoButton img")
    toolbar_showfex = (By.CSS_SELECTOR, "#topToolBar #showFexButton img")
    toolbar_run = (By.CSS_SELECTOR, "#topToolBar #runButton img")
    toolbar_showfex_setting = (By.CSS_SELECTOR,"#showFexSettingsButton img")
    toolbar_thumbnail = (By.CSS_SELECTOR, "#createThumbnailButton img")

    ''''1. Home_Tab'''
    home_change = (By.CSS_SELECTOR, "#HomeAVChart img")
    home_clear = (By.CSS_SELECTOR, "#ClearVisualization img")
    home_clear_dropdown = (By.CSS_SELECTOR, "#HomeVisualizationCluster #ClearVisualization div[class$='drop-down-arrow']")
    
    '''format'''
    home_format_type = (By.CSS_SELECTOR, "#HomeFormatType img")
    home_chart = (By.CSS_SELECTOR, "#HomeDestVBox #HomeOutputChart img")
    home_report= (By.CSS_SELECTOR, "#HomeFormatVBox #HomeOutputReport img")
    home_file_dropdown = (By.CSS_SELECTOR, "#HomeDestVBox #HomeDestFileMenuBtn div[class$='drop-down-arrow']") #default disabled and it is dropdown
    home_file = (By.CSS_SELECTOR, "#HomeDestFile img") 
    '''Design'''
    home_query = (By.CSS_SELECTOR, "#HomeDesignHBox #HomeQuery img") #default disabled
    home_live_preview = (By.CSS_SELECTOR, "#HomeDesignHBox #HomeInteractive img") #default disabled
    home_document = (By.CSS_SELECTOR, "#HomeDesignHBox #HomeCompose img")
    home_data_from_source = (By.CSS_SELECTOR, "#HomeDesignCluster #HomeLiveData img")
    home_use_sample_data = (By.CSS_SELECTOR, "#HomeDesignCluster #HomeSampleData img")
    home_records = (By.CSS_SELECTOR, "#HomeRecordLimit div[class$='combo-box-arrow']")
    '''Data'''
    home_calculation= (By.CSS_SELECTOR, "#HomeCalcMenuBtn img")
    '''Filter'''
    home_filter = (By.CSS_SELECTOR, "#HomeFilter img")
    home_exclude = (By.CSS_SELECTOR, "#HomeFilterRemove img")
    home_include = (By.CSS_SELECTOR, "#HomeFilterReapply img")
    '''Clipboard'''
    home_paste = (By.CSS_SELECTOR, "#HomeClipboardHBox #HomeClipboardPaste img")
    home_cut = (By.CSS_SELECTOR, "#HomeClipboardHBox #HomeClipboardCut img")
    home_copy = (By.CSS_SELECTOR, "#HomeClipboardHBox #HomeClipboardCopy img")
    home_duplicate = (By.CSS_SELECTOR, "#HomeClipboardHBox #HomeClipboardDuplicate img")
    '''Report'''
    home_theme = (By.CSS_SELECTOR, "#HomeReport #HomeThemes img")
    home_style = (By.CSS_SELECTOR, "#HomeReport #HomeStyles img")
    home_banded = (By.CSS_SELECTOR, "#HomeReport #HomeColourBands img")
    home_header_footer = (By.CSS_SELECTOR, "#HomeHeadFoot div[class$='drop-down-arrow']")
    home_header_footer_img = (By.CSS_SELECTOR, "#HomeHeadFoot img")
    home_column_totals = (By.CSS_SELECTOR, "#HomeColumnTotals img")
    home_column_totals_dropdown = (By.CSS_SELECTOR, "#HomeColumnTotals div[class$='drop-down-arrow']")
    home_row_totals = (By.CSS_SELECTOR, "#HomeRowTotals img")
    '''2. Insert'''
    home_insert = (By.CSS_SELECTOR, "#HomeInsertVis [id*='BiToolBarMenuButton']")
    
    '''Pages'''
    insert_page = (By.CSS_SELECTOR, "#InsertPageBtn img")
    '''Reports'''
    insert_report = (By.CSS_SELECTOR, "#InsertReportBtn img")
    insert_chart = (By.CSS_SELECTOR, "#InsertChartBtn img")
    insert_existing_report = (By.CSS_SELECTOR, "#InsertFocexecObjBtn img")
    '''Objects'''
    insert_text_box = (By.CSS_SELECTOR, "#InsertTextObjBtn img")
    insert_image = (By.CSS_SELECTOR, "#InsertImageObjBtn img")
    '''Active Dashboard Prompts'''
    insert_drop_down = (By.CSS_SELECTOR, "#InsertComboBoxBtn img")
    insert_list = (By.CSS_SELECTOR, "#InsertListBoxBtn img")
    insert_checkbox = (By.CSS_SELECTOR, "#InsertCheckGroupBtn img")
    insert_radio_button = (By.CSS_SELECTOR, "#InsertRadioGroupBtn img")
    insert_text = (By.CSS_SELECTOR, "#InsertTextFieldBtn img")
    '''3. Format'''
    '''Destination'''
    format_infomini_arrow = (By.CSS_SELECTOR, "#FormatApplicationRibbonEnableMenuBtn div[class$='drop-down-arrow']")
    format_infomini = (By.CSS_SELECTOR, "#FormatApplicationRibbonEnable img")
    format_chart = (By.CSS_SELECTOR, "#FormatOutputChart img")
    format_report = (By.CSS_SELECTOR, "#FormatOutputReport img")
    format_file = (By.CSS_SELECTOR, "#FormatDestFileMenuBtn div[class$='drop-down-arrow']")
    format_other=(By.CSS_SELECTOR, "#FormatOtherChart img")
    format_narrative = (By.CSS_SELECTOR, "#FormatChartNarrative img")
    '''Chart_Types'''
    format_bar = (By.CSS_SELECTOR, "#FormatBarChart img")
    format_pie = (By.CSS_SELECTOR, "#FormatPieChart img")
    format_line = (By.CSS_SELECTOR, "#FormatLineChart img")
    format_area = (By.CSS_SELECTOR, "#FormatAreaChart img")
    format_scatter = (By.CSS_SELECTOR, "#FormatScatterChart img")
    format_choropleth = (By.CSS_SELECTOR, "#FormatChoroplethChart img")
    format_proportional_symbol = (By.CSS_SELECTOR, "#FormatBubbleMapChart img")
    format_proportional_symbol = (By.CSS_SELECTOR, "#FormatBubbleMapChart img")
    format_other = (By.CSS_SELECTOR, "#FormatOtherChart img")
    '''Navigation'''
    format_table=(By.CSS_SELECTOR,'#FormatReportTable img')
    format_table_of_contents=(By.CSS_SELECTOR,'#FormatReportToc img')
    format_freeze=(By.CSS_SELECTOR,'#FormatReportFreeze img')
    format_pages_on_demand=(By.CSS_SELECTOR,'#FormatReportPod img')
    '''Features'''
    format_title_popup=(By.CSS_SELECTOR, "#FormatTitlePopup img")
    format_accordion=(By.CSS_SELECTOR, "#FormatAccordion img")
    format_repeat_sort_value=(By.CSS_SELECTOR, "#FormatRepeatSort img")
    format_stack_measures=(By.CSS_SELECTOR, "#FormatStackMeasures img")
    format_active_report_options=(By.CSS_SELECTOR, "#FormatActiveReportStyling img")
    format_active_report_options_chart=(By.CSS_SELECTOR, "#FormatActiveReportStylingChart img")
    format_accessibility=(By.CSS_SELECTOR, "#FormatAccessibility img")
    format_rotate=(By.CSS_SELECTOR, "#FormatChartRotate img")
    format_gauges=(By.CSS_SELECTOR, "#FormatGauge img")
    format_frame_background=(By.CSS_SELECTOR, "#FormatFrameBackground img")
    '''Labels'''
    format_labels=(By.CSS_SELECTOR, "#chartLabels_altButton img")
    format_legend=(By.CSS_SELECTOR, "#FormatChartLegend img")
    format_legend_dropdown=(By.CSS_SELECTOR, "#FormatChartLegend div[class$='drop-down-arrow']")
    format_axes=(By.CSS_SELECTOR, "#FormatChartAxes img")
    '''grid'''
    format_grid=(By.CSS_SELECTOR, "#FormatChartGrid img")
    '''frame and background'''
    format_frame_and_background=(By.CSS_SELECTOR, "#FormatFrameBackground img")
    
    '''Auto Drill '''
    format_run_with=(By.CSS_SELECTOR, "#FormatAutoDrillCluster_altButton img")
    format_auto_drill=(By.CSS_SELECTOR, "#FormatAutoDrill img")
    format_features=(By.CSS_SELECTOR,'#chartFeatures_altButton img')
    
    '''AutoLinking'''
    format_auto_linking=(By.CSS_SELECTOR, "#FormatAutoLinkCluster_altButton img")
    format_enable_auto_linking=(By.CSS_SELECTOR, "#FormatEnableAutoLink img")
    format_auto_link_target=(By.CSS_SELECTOR, "#FormatTargetAutoLink img")
    format_insight=(By.CSS_SELECTOR, "#FormatEnhancedRun img")
    
    '''4. Data'''
    '''Calculation'''
    data_detail_define = (By.CSS_SELECTOR, "#DataCalcDefine img")
    data_summary_compute = (By.CSS_SELECTOR, "#DataCalcCompute img")
    '''Join'''
    data_join = (By.CSS_SELECTOR, "#DataJoin img")
    '''Filters'''
    data_filter = (By.CSS_SELECTOR, "#WhereEditor img")
    '''Display'''
    data_missing_data = (By.CSS_SELECTOR, "#MissingData img")
    '''DataSource'''
    data_add = (By.CSS_SELECTOR, "#AddDataSourceBtn img")
    data_switch = (By.CSS_SELECTOR, "#SwitchDataSourceBtn img")
    '''5. Slicers'''
    '''Options'''
    slicers_new_group = (By.CSS_SELECTOR, "#createSlicerGroupBtn img")
    slicers_clear_slicers = (By.CSS_SELECTOR, "#clearSlicersBtn img")
    slicers_update_preview = (By.CSS_SELECTOR, "#slicersUpdatePreviewBtn img")
    '''Record Limit'''
    slicers_preview = (By.CSS_SELECTOR, "#SlicersPreviewComboBox div[class$='combo-box-arrow']")
    slicers_run_time = (By.CSS_SELECTOR, "#SlicersRunTimeComboBox div[class$='combo-box-arrow']")
    '''6. Layout'''
    '''Page_Setup'''
    layout_margins = (By.CSS_SELECTOR, "#LayoutMargins img")
    layout_orientation = (By.CSS_SELECTOR, "#LayoutOrientation img")
    layout_size = (By.CSS_SELECTOR, "#LayoutSize img")
    layout_units = (By.CSS_SELECTOR, "#LayoutUnits img")
    layout_page_numbers = (By.CSS_SELECTOR, "#LayoutPageNumbering img")
    layout_active_dashboard = (By.CSS_SELECTOR, "#LayoutAdaptiveDashboard img")
    '''Size & Arrange'''
    layout_height = (By.CSS_SELECTOR, "#ClusterLayoutSizeArrange input[id='LayoutHeightSpinner']")
    layout_widht = (By.CSS_SELECTOR, "#ClusterLayoutSizeArrange input[id='LayoutWidthSpinner']")
    layout_auto_overflow = (By.CSS_SELECTOR, "#LayoutAutoOverflow img")
    layout_aspect_ratio = (By.CSS_SELECTOR, "#LayoutLockAspectRatio img")
    layout_autofit = (By.CSS_SELECTOR, "#LayoutAutoFit img")
    layout_align = (By.CSS_SELECTOR, "#LayoutAlign img")
    layout_relative_position = (By.CSS_SELECTOR, "#LayoutRelPos img")
    '''7. View'''
    '''Design'''
    view = (By.CSS_SELECTOR, "#ViewTab_tabButton")
    view_query = (By.CSS_SELECTOR, "#ViewQuery img")
    view_live_preview = (By.CSS_SELECTOR, "#ViewInteractive img")
    view_document = (By.CSS_SELECTOR, "#ViewCompose img")
    '''Show/Hide'''
    view_resources = (By.CSS_SELECTOR, "#ViewResources img")
    view_ruler = (By.CSS_SELECTOR, "#ViewRulerBtn img")
    view_grid = (By.CSS_SELECTOR, "#ViewGridBtn img")
    view_relationships = (By.CSS_SELECTOR, "#ViewRelationshipsBtn img")
    '''Data_Panel'''
    view_logical = (By.CSS_SELECTOR, "#DataViewBusiness div[class$='drop-down-arrow']")
    view_list = (By.CSS_SELECTOR, "#DataViewList div[class$='drop-down-arrow']")
    view_structured = (By.CSS_SELECTOR, "#DataViewTechnical div[class$='drop-down-arrow']")
    view_list_tab = (By.CSS_SELECTOR, "#DataViewList")
    view_structured_tab = (By.CSS_SELECTOR, "#DataViewTechnical")
    
    '''Query_Panel'''
    view_area22 = (By.CSS_SELECTOR, "#QueryArea22")
    view_area14 = (By.CSS_SELECTOR, "#QueryArea14")
    view_tree = (By.CSS_SELECTOR, "#QueryAreaTree")
    '''Output Window'''
    view_arrange = (By.CSS_SELECTOR, "#ArrangeOutputWin img")
    view_output_location = (By.CSS_SELECTOR, "#Output img")
    view_switch_output = (By.CSS_SELECTOR, "#OutputWindowSwitch img")
    '''Report'''
    view_switch_report = (By.CSS_SELECTOR, "#switchQuery img")
    '''8. Field'''
    '''Filter'''
    field_filter = (By.CSS_SELECTOR, "#FieldFilter img")
    field_exclude = (By.CSS_SELECTOR, "#FieldFilterRemove img")
    field_include = (By.CSS_SELECTOR, "#FieldFilterReapply img")
    field_prompt = (By.CSS_SELECTOR, "#FieldColumnPrompt img")
    '''Sort'''
    field_up = (By.CSS_SELECTOR, "#FieldSortUp img")
    field_down = (By.CSS_SELECTOR, "#FieldSortDown img")
    field_rank = (By.CSS_SELECTOR, "#FieldRank img")
    field_group = (By.CSS_SELECTOR, "#SortGroup img")
    field_limit = (By.CSS_SELECTOR, "#FieldSortLimit div[class$='combo-box-arrow']")
    '''Break'''
    field_page_break_icon = (By.CSS_SELECTOR, "#FieldPageBreak img")
    field_page_break = (By.CSS_SELECTOR, "#FieldPageBreak div[class$='drop-down-arrow']")
    field_line_break = (By.CSS_SELECTOR, "#FieldLineBreak img")
    field_subtotal = (By.CSS_SELECTOR, "#FieldRecompute div[class$='drop-down-arrow']")
    field_subtotal_icon = (By.CSS_SELECTOR, "#FieldRecompute img")
    field_sub_header = (By.CSS_SELECTOR, "#FieldSubhead img")
    field_sub_footer = (By.CSS_SELECTOR, "#FieldSubFoot")
    #field_sub_footer = (By.CSS_SELECTOR, "#FieldSubFoot img")
    ''''Style'''
    field_fieldfont = (By.CSS_SELECTOR, "#FieldFont div[class$='combo-box-arrow']")
    field_fontsize = (By.CSS_SELECTOR, "#FieldFontSize div[class$='combo-box-arrow']")
    field_fontcolour = (By.CSS_SELECTOR, "#FieldFontColour img")
    field_resetsyle = (By.CSS_SELECTOR, "#FieldResetSyle img")
    field_fontbold = (By.CSS_SELECTOR, "#FieldFontBold img")
    field_fontitalic = (By.CSS_SELECTOR, "#FieldFontItalic img")
    field_fontunderline = (By.CSS_SELECTOR, "#FieldFontUnderline img")
    field_fontleft = (By.CSS_SELECTOR, "#FieldFontLeft img")
    field_fontcentre = (By.CSS_SELECTOR, "#FieldFontCentre img")
    field_fontright = (By.CSS_SELECTOR, "#FieldFontRight img")
    field_fontbackcolour = (By.CSS_SELECTOR, "#FieldFontBackColour img")
    field_data_style = (By.CSS_SELECTOR, "#FieldDataStyle img")
    field_titlestyle = (By.CSS_SELECTOR, "#FieldTitleStyle img")
    field_dataplusstyle = (By.CSS_SELECTOR, "#FieldDataPlusStyle img")
    '''Format'''
    field_formattype = (By.CSS_SELECTOR, "#FieldFormatType div[class$='combo-box-arrow']")
    field_formatcurrency = (By.CSS_SELECTOR, "#FieldFormatCurrency div[class$='drop-down-arrow']")
    field_formatpercent = (By.CSS_SELECTOR, "#FieldFormatPercent img")
    field_formatcomma = (By.CSS_SELECTOR, "#FieldFormatComma img")
    field_formatdecimallenup = (By.CSS_SELECTOR, "#FieldFormatDecimalLenUp img")
    field_formatdecimallendown = (By.CSS_SELECTOR, "#FieldFormatDecimalLenDown img")
    '''Display'''
    field_hide_field = (By.CSS_SELECTOR, "#FieldColumnHidden img")
    field_columnmissing = (By.CSS_SELECTOR, "#FieldColumnMissing img")
    field_aggregation = (By.CSS_SELECTOR, "#FieldAggregation img")
    field_trafficlights = (By.CSS_SELECTOR, "#FieldTrafficLights img")
    field_databars = (By.CSS_SELECTOR, "#FieldDataBars img")
    field_within = (By.CSS_SELECTOR, "#FieldWithin img")
    '''Links'''
    field_drilldown = (By.CSS_SELECTOR, "#FieldDrillDown img")
    
    '''9. Series '''
    '''Properties'''
    series_type = (By.CSS_SELECTOR, "#SeriesChartType img")
    series_data_labels_menubtn=(By.CSS_SELECTOR,"#SeriesChartDataLabels #SeriesChartDataLabelsMenuBtn")
    series_data_labels=(By.CSS_SELECTOR, "#SeriesChartDataLabels")
    series_select_menubtn=(By.CSS_SELECTOR,"#SeriesChartSelect div[id*='BiButton']")
    series_style=(By.CSS_SELECTOR,"#SeriesStyleCluster #SeriesColorSelection img")
    series_smoothline=(By.CSS_SELECTOR,"#SeriesLineCluster #SeriesSmoothLine img")
    
    '''Line'''
    marker_options = "// *[contains(text(), '{0}')]"
    
    '''Swap'''
    home_swap = (By.CSS_SELECTOR, '#SwapVisualization img')
    ''' Home '''
    
    HOME = (By.ID, 'HomeTab_tabButton')
    HOME_FORMAT_TYPE = (By.ID,'HomeFormatType')
    ACTIVE_REPORT =(By.ID, 'menu_ahtml_btn')
    
    ChangeChartType = (By.ID, "HomeAVChart")
    calculation = (By.ID, 'HomeCalcMenuBtn')
    home_add_storyboard = (By.ID,'HomeAddtoStoryboardBtn')
    home_show_storyboard = (By.ID,'HomeOpenStoryboard')
    home_join = (By.CSS_SELECTOR, "#HomeDataJoin img")
    format_theme = (By.CSS_SELECTOR, "#FormatChartThemes img")
    format_header_footer = (By.CSS_SELECTOR, "#FormatChartHeadFoot div[class$='drop-down-arrow']")
    format_header_footer_img = (By.CSS_SELECTOR, "#FormatChartHeadFoot img")
    format_background = (By.CSS_SELECTOR, "#FormatBaseMap img")
    format_demographiclayers = (By.CSS_SELECTOR, "#FormatDemographicLayers img")
    format_referencelayers = (By.CSS_SELECTOR, "#FormatReferenceLayers img")
    
    '''Quick Access Toolbar'''
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
    filter_menu = (By.CSS_SELECTOR, '#FieldFilter')
    ia_view_code = (By.CSS_SELECTOR,'#showFexButton img')
    
    '''Right cornor Ribbon Buttons'''
    helpmenu=(By.CSS_SELECTOR, "#showHelpButton")
    show_hide_ribbon=(By.CSS_SELECTOR, "#minMaxRibbonButton")
    
    
    