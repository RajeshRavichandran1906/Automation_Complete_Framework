from selenium.webdriver.common.by import By
class IaRibbonLocators(object):
    
    '''Join-ToolBar'''
    join_add_new = (By.CSS_SELECTOR, "#dlgJoin #dlgJoin_btnAddMaster img")
    join_edit = (By.CSS_SELECTOR, "#dlgJoin #dlgJoin_btnEditJoin img")
    join_remove = (By.CSS_SELECTOR, "#dlgJoin #dlgJoin_btnDeleteJoin img")
    join_filter = (By.CSS_SELECTOR, "#dlgJoin #dlgJoin_btnEditWhere img")
    join_view = (By.CSS_SELECTOR, "#dlgJoin #dlgJoin_btnToggleView img")
    join_index_only = (By.CSS_SELECTOR, "#dlgJoin #dlgJoin_btnFilterIndex img")
    join_blend = (By.CSS_SELECTOR, "#dlgJoin #dlgJoin_btnJoinBlend img")
    
    join_ok = (By.ID, "dlgJoin_btnOK")
    join_cancel = (By.ID, "dlgJoin_btnCancel")
    
    ''' define & compute '''
    data_define = (By.CSS_SELECTOR, "#DataCalcDefine img")
    data_compute = (By.CSS_SELECTOR, "#DataCalcCompute img")
    
    '''other chart types'''
    left_pane="div[id^='QbDialog'][style*='visibility: inherit'] #selectChartLeftPane"
    right_pane="div[id^='QbDialog'][style*='visibility: inherit'] #selectChartHorizSplitPane"
    '''Bar'''
    select_bar_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Bar img")
    bar_buttons=(By.CSS_SELECTOR, "#RightPane_Bar div[id^='BiToolBarRadioButton']")
    bar_stacked=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_stacked.png']")
    vertical_clustered_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_clustered.png']")
    vertical_stacked_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_stacked.png']")
    vertical_percent_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_percent.png']")
    vertical_waterfall_chart=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_waterfall.png']")
    error_bar=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_clustered_with_errorbars.png']")
    vertical_histogram=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_histogram.png']")
    multi_y=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_multi_y.png']")
    multi_y4=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_multi_y4.png']")
    multi_y5=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_multi_y5.png']")
    vertical_dual_axis_clustered_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_clustered_dual_axis.png']")
    vertical_dual_axis_stacked_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_stacked_dual_axis.png']")
    vertical_bi_ploar_clustered_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_clustered_bipolar.png']")
    vertical_bi_ploar_stacked_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_stacked_bipolar.png']")
    horizontal_clustered_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_clustered_horizontal.png']")
    horizontal_stacked_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_stacked_horizontal.png']")
    horizontal_dual_axis_clustered_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_clustered_dual_axis_horizontal.png']")
    horizontal_dual_axis_stacked_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_stacked_dual_axis_horizontal.png']")
    horizontal_bi_polar_clustered_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_clustered_bipolar_horizontal.png']")
    horizontal_bi_polar_stacked_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_stacked_bipolar_horizontal.png']")
    horizontal_percent_bars=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_percent_horizontal.png']")
    horizontal_histogram=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_histogram_horizontal.png']")
    horizontal_waterfall_charts=(By.CSS_SELECTOR, "#RightPane_Bar img[src$='bar_waterfall_horizontal.png']")
    '''Line'''
    select_line_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Linetype img")
    line_buttons=(By.CSS_SELECTOR, "#RightPane_Linetype div[id^='BiToolBarRadioButton']")
    vertical_absolute_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_absolute.png']")
    vertical_stacked_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_stacked.png']")
    vertical_percent_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_percent.png']")
    vertical_dual_axis_absolute_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_absolute_dual.png']")
    vertical_dual_axis_stacked_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_stacked_dual.png']")
    vertical_bi_polar_absolute_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_absolute_bipolar.png']")
    vertical_bi_polar_stacked_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_stacked_bipolar.png']")
    horizontal_absolute_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_absolute_horizontal.png']")
    horizontal_stacked_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_stacked_horizontal.png']")
    horizontal_dual_axis_absolute_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_absolute_dual_horizontal.png']")
    horizontal_dual_axis_stacked_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_stacked_dual_horizontal.png']")
    horizontal_bi_polar_absolute_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_absolute_bipolar_horizontal.png']")
    horizontal_bi_polar_stacked_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_stacked_bipolar_horizontal.png']")
    horizontal_percent_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_percent_horizontal.png']")
    radar_line=(By.CSS_SELECTOR, "#RightPane_Linetype img[src$='line_radar_lines.png']")
    '''Area'''
    vertical_absolute_area=(By.CSS_SELECTOR, "#RightPane_Area img[src$='area_absolute.png']")
    horizontal_absolute_area=(By.CSS_SELECTOR, "#RightPane_Area img[src$='area_absolute_horizontal.png']")
    select_area_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Area img")
    area_buttons=(By.CSS_SELECTOR, "#RightPane_Area div[id^='BiToolBarRadioButton']")
    area=(By.ID, "ChartTypeButton_Icon_Area_Absolute")
    area_stacked=(By.ID, "ChartTypeButton_Icon_Area_Stacked")
    area_absolute_bipolar=(By.ID, "ChartTypeButton_Icon_Area_Absolute_BiPolar")
    area_stacked_bipolar=(By.ID, "ChartTypeButton_Icon_Area_Stacked_BiPolar")
    area_percent=(By.ID, "ChartTypeButton_Icon_Area_Percent")
    area_absolute_horizontal=(By.ID, "ChartTypeButton_Icon_Area_Absolute_Horizontal")
    area_stacked_horizontal=(By.ID, "ChartTypeButton_Icon_Area_Stacked_Horizontal")
    area_absolute_bipolar_horizontal=(By.ID, "ChartTypeButton_Icon_Area_Absolute_BiPolar_Horizontal")
    area_stacked_bipolar_horizontal=(By.ID, "ChartTypeButton_Icon_Area_Stacked_BiPolar_Horizontal")
    area_percent_horizontal=(By.ID, "ChartTypeButton_Icon_Area_Percent_Horizontal")
    area_radar=(By.ID, "ChartTypeButton_Icon_Area_Radar_Area")
    
    '''Pie'''
    select_pie_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Pie img")
    pie_buttons=(By.CSS_SELECTOR, "#RightPane_Pie div[id^='BiToolBarRadioButton']")
    pie=(By.ID, "ChartTypeButton_Icon_Pie_Pie")
    pie_bar=(By.ID, "ChartTypeButton_Icon_Pie_Pie_Bar")
    pie_bar_ring=(By.ID, "ChartTypeButton_Icon_Pie_Pie_Bar_Ring")
    ring_pie=(By.ID, "ChartTypeButton_Icon_Pie_Ring")
    pie_multi=(By.ID, "ChartTypeButton_Icon_Pie_Multi")
    pie_multi_ring=(By.ID, "ChartTypeButton_Icon_Pie_Multi_Ring")
    pie_multi_proportional=(By.ID, "ChartTypeButton_Icon_Pie_Multi_Proportional")
    pie_multi_ring_proportional=(By.ID, "ChartTypeButton_Icon_Pie_Multi_Ring_Proportional")
    
    ''''X Y Plots'''
    select_x_y_plots_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_X_Y_Plots img")
    x_y_plots_buttons=(By.CSS_SELECTOR, "#RightPane_X_Y_Plots div[id^='BiToolBarRadioButton']")
    x_y_plots_polar=(By.ID, "ChartTypeButton_Icon_X_Y_Plots_Polar")
    x_y_plots_bubble=(By.ID, "ChartTypeButton_Icon_X_Y_Plots_Bubble")
    x_y_plots_scatter=(By.ID, "ChartTypeButton_Icon_X_Y_Plots_Scatter")
    
    '''3D'''
    select_threed_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_ThreeD img")
    threed_buttons=(By.CSS_SELECTOR, "#RightPane_ThreeD div[id^='BiToolBarRadioButton']")
    threed_bars=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_riser.png']")
    threed_connected_series_ribbon=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_connected_series.png']")
    threed_connected_group_ribbon=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_connected_groups.png']")
    threed_pyramid=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_pyramid.png']")
    threed_octagon=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_octagon.png']")
    threed_cylinder=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_cylinder.png']")
    threed_floating_cubes=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_floating_cubes.png']")
    threed_floating_pyramids=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_floating_pyramids.png']")
    threed_connected_series_area=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_connected_series_area.png']")
    threed_cone=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_cone.png']")
    threed_connected_group_area=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_connected_groups_area.png']")
    threed_sphere=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_sphere.png']")
    threed_surface=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_surface.png']")
    threed_surface_with_sides=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_surface_sides.png']")
    threed_honeycomb_surface=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_honeycomb.png']")
    threed_smooth_surface=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_smooth_surface.png']")
    threed_smooth_surface_with_sides=(By.CSS_SELECTOR, "#RightPane_ThreeD img[src$='threed_smooth_surface_sides.png']")
    '''Stock'''
    select_stock_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Stock img")
    stock_buttons=(By.CSS_SELECTOR, "#RightPane_Stock div[id^='BiToolBarRadioButton']")
    stock_high_low=(By.ID, "ChartTypeButton_Icon_Stock_Hi_Lo")
    stock_high_low_volume=(By.ID, "ChartTypeButton_Icon_Stock_Hi_Lo_Volume")
    stock_high_low_open_close=(By.ID, "ChartTypeButton_Icon_Stock_Hi_Lo_Open_Close")
    stock_high_low_open_close_volume=(By.ID, "ChartTypeButton_Icon_Stock_Hi_Lo_Open_Close_Volume")
    stock_candlestick_high_low_open_close=(By.ID, "ChartTypeButton_Icon_Stock_Candlestick_Hi_Lo_Open_Close")
    stock_candlestick_high_low_open_close_volume=(By.ID, "ChartTypeButton_Icon_Stock_Candlestick_Hi_Lo_Open_Close_Volume")
    
    
    '''Special'''
    select_special_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Special img")
    special_buttons=(By.CSS_SELECTOR, "#RightPane_Special div[id^='BiToolBarRadioButton']")
    gauge=(By.ID, "ChartTypeButton_Icon_Special_Gauges")
    thermometer_gauge=(By.ID, "ChartTypeButton_Icon_Special_Gauges_Thermometer")
    pareto=(By.ID, "ChartTypeButton_Icon_Special_Pareto")
    vertical_boxplot=(By.ID, "ChartTypeButton_Icon_Special_Boxplot_Vertical")
    horizontal_boxplot=(By.ID, "ChartTypeButton_Icon_Special_Boxplot_Horizontal")
    funnel=(By.ID, "ChartTypeButton_Icon_Special_Funnel")
    pyramid=(By.ID, "ChartTypeButton_Icon_Special_Pyramid")
    spectral=(By.ID, "ChartTypeButton_Icon_Special_Spectral_Mapped")
    
    
    '''HTML5'''
    select_html5_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Html5 img")
    html5_buttons=(By.CSS_SELECTOR, "#RightPane_Html5 div[id^='BiToolBarRadioButton']")
    tree_map=(By.CSS_SELECTOR, "#ChartTypeButton_Icon_Treemap")
    stream_graph=(By.ID,"ChartTypeButton_Icon_Streamgraph")
    html5_parabox=(By.ID,"ChartTypeButton_Icon_Parabox")
    html5_Mekko=(By.ID,"ChartTypeButton_Icon_Mekko")
    html5_DataGrid=(By.ID,"ChartTypeButton_Icon_DataGrid")
    html5_tagCloud=(By.ID,"ChartTypeButton_Icon_tagCloud")
    
    '''Map'''
    select_map_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_Map img")
    map_buttons=(By.CSS_SELECTOR, "#RightPane_Map div[id^='BiToolBarRadioButton']")
    leaflet_choropleth=(By.CSS_SELECTOR, "#RightPane_Map img[src$='leaflet_choropleth.png']")
    leaflet_bubblemap=(By.CSS_SELECTOR, "#RightPane_Map img[src$='leaflet_bubblemap.png']")
    
    '''Html5 Extension'''
    select_html5_extension_chart=(By.CSS_SELECTOR, "#ChartTypeGroup_html5_extensions img")
    html5_extension_buttons=(By.CSS_SELECTOR, "#RightPane_html5_extensions div[id^='BiToolBarRadioButton']")
    sparkline=(By.CSS_SELECTOR, "img[id='ChartTypeButton_Icon_com.ibi.kpi.sparkline']")
    kpi_with_sparkline=(By.CSS_SELECTOR, "img[id='ChartTypeButton_Icon_com.ibi.kpi.sparkline2']")
     
    '''Right cornor Ribbon Buttons'''
    helpmenu=(By.ID, "#showHelpButton")
    show_hide_ribbon=(By.ID, "#minMaxRibbonButton")
    
    output_format="#HomeFormatType"
    '''Active Report options'''
    active_report_option_tabs="#activeReportOptionsLeftContainer"
    general_window_default_value="#genWindowCombo [class*='combo-box-label']"
    general_freeze_columns_default_value = "#freezeColsCombo [class*='combo-box-label']"
    general_freeze_columns_dropdown =  "#freezeColsCombo [id^='BiButton']"
    general_window_dropdown = "#genWindowCombo [id^='BiButton']"
    general_records_per_page_default_value="#recordsPerPageCombo input"
    alignment_left= "#generalPane #Left"
    alignment_center="#generalPane #Center"
    alignment_right="#generalPane #Right"
    advanced_rows_retrieved ="#advancedPane #rowsRetrievedCombo input"
    general_window_label = "#genWindowLabel"
    general_freeze_columns_label = "#freezeColsLabel"
    general_records_per_page_label = "#recordsPerPageLabel"
    general_records_per_page_dropdown =  "#recordsPerPageCombo [id^='BiButton']"
    general_display_page_information_label =  "#displayPageInfoCheckbox"
    general_display_page_info_checkbox =  "#displayPageInfoCheckbox [type*='checkbox']"
    general_alignment_label = "#pageAlignmentLabel"
    general_location_label = "#pageLocationLabel"
    general_location_default_value =  "#pageLocationCombo [class*='combo-box-label']"
    general_location_dropdown =  "#pageLocationCombo [id^='BiButton']"
