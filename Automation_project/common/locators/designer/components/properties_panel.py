from selenium.webdriver.common.by import By

class PropertiesPanel:
    
    property_panel_tab = (By.CSS_SELECTOR, "div[data-ibx-type='ibxTabButton'][role='tab']")

class Settings:
    
    page_settings_css = (By.CSS_SELECTOR, "div.settings-container-box div.df-settings-tab-page ")
    
    id       = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-value-id [role='textbox']")
    classes  = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-value-custom [role='textbox']")
    
    # Page Settings
    
    show_page_heading    = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-show-header")
    show_page_toolbar    = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-show-toolbar")
    show_page_refresh    = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-show-refresh")
    show_export          = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-show-export")
    show_export_PDF      = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-show-export-pdf")
    show_export_image    = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-show-export-image")
    include_page_filters = (By.CSS_SELECTOR, page_settings_css[1] + "div.df-page-filter-include")
    below_header         = (By.CSS_SELECTOR, page_settings_css[1] + "div.df-ps-filter-bottom")
    above_header         = (By.CSS_SELECTOR, page_settings_css[1] + "div.df-ps-filter-top")
    modal                = (By.CSS_SELECTOR, page_settings_css[1] + "div.df-ps-filter-modal")
    
    # Container Settings
    
    container_settings        = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='Container Settings'] ")
    show_title                = (By.CSS_SELECTOR, container_settings[1] + "div.pd-ps-container-title")
    show_toolbar              = (By.CSS_SELECTOR, container_settings[1] + "div.pd-ps-container-toolbar")
    show_on_desktop           = (By.CSS_SELECTOR, container_settings[1] + "div.pd-ps-container-desktop")
    show_on_tablet            = (By.CSS_SELECTOR, container_settings[1] + "div.pd-ps-container-tablet")
    show_on_mobile            = (By.CSS_SELECTOR, container_settings[1] + "div.pd-ps-container-mobile")
    autoplay_interval_textbox = (By.CSS_SELECTOR, container_settings[1] + "div.ibx-spinner-text-input")
    autoplay_interval_up      = (By.CSS_SELECTOR, container_settings[1] + "div.ibx-spinner-btn-up")
    autoplay_interval_down    = (By.CSS_SELECTOR, container_settings[1] + "div.ibx-spinner-btn-down")
    rerun_content             = (By.CSS_SELECTOR, container_settings[1] + "div.pd-ps-carousel-rerun")
     
    # Container Customization
    
    container_customization      = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='Container Customization'] ")
    lock_container               = (By.CSS_SELECTOR, container_customization[1] + "div.pd-ps-es-lock-content")
    select_content_from_textbox  = (By.CSS_SELECTOR, container_customization[1] + "div.pd-ps-es-path")
    select_content_from_elipsis  = (By.CSS_SELECTOR, container_customization[1] + "div.pd-ps-es-path-btn")
    lock_path                    = (By.CSS_SELECTOR, container_customization[1] + "div.pd-ps-es-lock-path")
    flatten_list                 = (By.CSS_SELECTOR, container_customization[1] + "div.pd-ps-es-flatten-list")
    hide_tags                    = (By.CSS_SELECTOR, container_customization[1] + "div.pd-ps-es-hide-tags")
    grid                         = (By.CSS_SELECTOR, container_customization[1] + "div[title='Grid']")
    list                         = (By.CSS_SELECTOR, container_customization[1] + "div[title='List']")
    
    # Link Tile
    
    link_tile              = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='Link Tile'] ")
    background_textbox     = (By.CSS_SELECTOR, link_tile[1] + "div.pd-ps-background-path-edit")
    background_elipsis     = (By.CSS_SELECTOR, link_tile[1] + "div.pd-ps-background-path-btn")
    content_textbox        = (By.CSS_SELECTOR, link_tile[1] + "div.pd-ps-content-path-edit")
    content_elipsis        = (By.CSS_SELECTOR, link_tile[1] + "div.pd-ps-content-path-btn")
    attach_all_parameters  = (By.CSS_SELECTOR, link_tile[1] + "div.pd-ps-content-params")
    target                 = (By.CSS_SELECTOR, link_tile[1] + "div.pd-ps-target")
    target_dropdown        = (By.CSS_SELECTOR, link_tile[1] + "div.pd-ps-target div.ibx-select-open-btn")
    
    # Section Settings
    
    section_settings  = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='Section Settings'] ")
    collapsible       = (By.CSS_SELECTOR, section_settings[1] + "div.pd-ps-section-collapsible")
        
    
    # control settings
    
    general_settings = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='General Settings'] ")
    control_settings = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='Control Settings'] ")
    data_settings = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='Data Settings'] ")
    parameters = (By.CSS_SELECTOR, page_settings_css[1] + "[data-ibxp-btn-options*='Parameters'] ")
    
    type = (By.CSS_SELECTOR, general_settings[1] + "div.pd-ps-type input")
    tooltip = (By.CSS_SELECTOR, general_settings[1] + "div.pd-ps-tooltip input")
    global_name = (By.CSS_SELECTOR, general_settings[1] + "div.pd-ps-global-name input")
    optional = (By.CSS_SELECTOR, control_settings[1] + "div.pd-ps-optional")
    placeholder = (By.CSS_SELECTOR, control_settings[1] + "div.pd-ps-placeholder")
    search = (By.CSS_SELECTOR, control_settings[1] + "div.pd-ps-search")
    selection_controls = (By.CSS_SELECTOR, control_settings[1] + "div.pd-ps-selection-controls")
    allow_reordering = (By.CSS_SELECTOR, control_settings[1] + "div.pd-ps-sortable")
    show_all_option = (By.CSS_SELECTOR, data_settings[1] + "div.pd-ps-show-all input")
    display_text = (By.CSS_SELECTOR, data_settings[1] + "div.pd-ps-all-label")
    default_value = (By.CSS_SELECTOR, data_settings[1] + "div.pd-ps-default-value input")
    default_value2 = (By.CSS_SELECTOR, data_settings[1] + "div.pd-ps-default-value2 input")
    parameter_value = (By.CSS_SELECTOR, parameters[1] + "div.pd-ps-parameters input")
    parameter_value2 = (By.CSS_SELECTOR, parameters[1] + "div.pd-ps-parameters2 input")
    
    # content settings
    
    content_id = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-value-id-content [role='textbox']")
    content_classes = (By.CSS_SELECTOR, page_settings_css[1] + "div.pd-ps-value-custom-content [role='textbox']")
    content_settings  = (By.CSS_SELECTOR, "div[data-ibx-name='contentPage']")
    enable_heading = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='enableHeading'] .ibx-check-box-simple-marker")
    enable_footing = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='enableFooting'] .ibx-check-box-simple-marker")
    enable_auto_refresh = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='enableAutoRefresh'] .ibx-check-box-simple-marker")
    run_with_insight = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='runWithInsights'] .ibx-check-box-simple-marker")
    drill_anywhere_parent = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='drillAnyWhere']")
    drill_anywhere = (By.CSS_SELECTOR, drill_anywhere_parent[1] + " .ibx-check-box-simple-marker")
    autodrill = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='autoDrill'] .ibx-check-box-simple-marker")
    autolink = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='autoLink'] .ibx-check-box-simple-marker")
    autolinktarget = (By.CSS_SELECTOR, content_settings[1] + " div[data-ibx-name='autoLinkTarget'] .ibx-check-box-simple-marker")

    
    class Display:
        
        display = (By.CSS_SELECTOR,  "div.pd-table-builder:not([style*='none']) div[data-ibx-name='displayPane'] ")
        change_chart_orientation = (By.CSS_SELECTOR, display[1] + "div[title='Change chart orientation'] ")
        layout_button = (By.CSS_SELECTOR, display[1] + "div[data-ibx-name='layoutBtn'] ") # Stacked, Side-by-side, Absolute, Percent
        layout_button_dropdown = (By.CSS_SELECTOR, layout_button[1] + "div.ibx-menu-button-arrow ")
        type_button = (By.CSS_SELECTOR, display[1] + "div[data-ibx-name='verbTypeBtn'] ") # Summaries, Counts, Details
        type_button_dropdown = (By.CSS_SELECTOR, type_button[1] + "div.ibx-menu-button-arrow ")
        clear_buckets_content = (By.CSS_SELECTOR, display[1] + "div[title='Clear buckets content'] ")
        bucket = (By.CSS_SELECTOR, display[1] + "div[data-ibx-type='bucket'] ") 
    

class Format:

    format = (By.CSS_SELECTOR, "div.settings-container-box div.df-style-tab-page" )
    container_format = (By.CSS_SELECTOR, "[data-ibxp-btn-options*='Container Format'] ")
    section_format = (By.CSS_SELECTOR, "[data-ibxp-btn-options*='Section Format'] ")

    
    #Page Format
    theme_dropdown = (By.CSS_SELECTOR, format[1] + " div[data-ibx-type='dfPropertiesSelect'] input")
    margin_textbox = (By.CSS_SELECTOR, format[1] + " div.pd-ps-margin input[role='textbox']")
    maximum_width_textbox = (By.CSS_SELECTOR, format[1] + " div.pd-ps-max-width input[role='textbox']")

    #Grid Style
    grid_style = (By.CSS_SELECTOR, "div[data-ibxp-btn-options*='Grid Style']")
    
    #Section Format
    options = (By.CSS_SELECTOR,  section_format[1] + "div[data-ibx-type='ibxVBox']")
    lables = (By.CSS_SELECTOR, options[1] + " div[data-ibx-type='ibxLabel']")
    
    #Map Settings
    base_map = (By.CSS_SELECTOR, "div[data-ibx-name='baseMapList']")
    base_map_default = (By.CSS_SELECTOR, base_map[1] + ' input')
    demographic_layer = (By.CSS_SELECTOR, "div[data-ibx-name='demoLayerList']")
    reference_layer = (By.CSS_SELECTOR, "div[data-ibx-name='refLayerList']")
    
    class General:
        
        general_dropdown = (By.CSS_SELECTOR, "div[data-ibx-name='quickAccessMenu']")
        
        #Frame and Background
        frame_and_background = (By.CSS_SELECTOR, "div[data-ibx-name='chartFrameBackgdPage']")
        frame = (By.CSS_SELECTOR, frame_and_background[1] + " div[data-ibx-name='chartFrameColor']")
            
        class ColorPalette:
            
            color_palette = (By.CSS_SELECTOR, "div[data-ibx-type='colorSwatchPopup']")
            color = "div[data-ibx-type='colorSwatchPopup'] div[title='{}']"
        
        
    
    