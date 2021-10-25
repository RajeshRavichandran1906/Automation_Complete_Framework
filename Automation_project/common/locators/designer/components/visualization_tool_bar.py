from selenium.webdriver.common.by import By

class VisualizationToolBar:
    
    base_css = "div.df-level2-toolbar-wrapper "
    add_data = (By.CSS_SELECTOR, base_css + "div[title='Add data']")
    add_visualization = (By.CSS_SELECTOR, base_css + "div[title='Add visualization']")
    convert_to_page = (By.CSS_SELECTOR, base_css +"div[title='Convert to page']")
    filter_options = (By.CSS_SELECTOR, base_css + "div[title='Filter options']")
    live_data = (By.CSS_SELECTOR, base_css + "div[title='Live data']:not([style*='none'])")
    hide_show_panes = (By.CSS_SELECTOR, base_css + "div[title='Hide/show panes']") 
    run_in_new_window = (By.CSS_SELECTOR, base_css + "div[title='Run in new window']")
    add_container = (By.CSS_SELECTOR, base_css + "div[title='Add container']")
    add_all_filters_to_page = (By.CSS_SELECTOR, base_css + "div[title='Add all filters to page']")
    filter_dropdown = (By.CSS_SELECTOR, "div.split-menu")
    show_menu = (By.CSS_SELECTOR, base_css + "div[title='Show Menu']")
    info = (By.CSS_SELECTOR, base_css + "div[title='Info']")
    add_data_icon = (By.CSS_SELECTOR, "div.fa.database")
    add_visualization_icon = (By.CSS_SELECTOR, "div.fa-chart-bar")
    convert_to_page_icon = (By.CSS_SELECTOR, "div.fa-file")
    filter_options_icon = (By.CSS_SELECTOR, "div.fa-filter")
    live_data_icon = (By.CSS_SELECTOR, ".ds-icon-toggle-auxiliary-sidebar")
    hide_show_panes_icon = (By.CSS_SELECTOR, ".ds-icon-toggle-auxiliary-sidebar")
    run_in_new_window_icon = (By.CSS_SELECTOR, "div.ds-icon-preview")
    info_icon = (By.CSS_SELECTOR, "div.fa-search")
    output_format = (By.CSS_SELECTOR, "div[title='Output Format']")
    output_format_parent = (By.CSS_SELECTOR, "div.df-output-format-menu")
    different_output_format = (By.CSS_SELECTOR, output_format_parent[1] + " [data-ibx-type='ibxRadioMenuItem']")
    
    
    