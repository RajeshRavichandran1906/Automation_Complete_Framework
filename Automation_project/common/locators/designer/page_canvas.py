from selenium.webdriver.common.by import By

RUN_MODE = (By.CSS_SELECTOR, "div.df-visualization-run")
EDIT_MODE = (By.CSS_SELECTOR, "div.df-theme-background")
PAGE = (By.CSS_SELECTOR, "div.pd-page-tab-content-wrapper")
BACKGROUND = (By.CSS_SELECTOR, PAGE[1] + " [data-ibx-type='pdPage']")

class Section:

    section = (By.CSS_SELECTOR, "div.pd-page-acc-section")
    grid = (By.CSS_SELECTOR, "div.pd-page-section-grid")
    
    
class Container:
    
    containers = (By.CSS_SELECTOR, "div.pd-container")
    title_bar = (By.CSS_SELECTOR, "div.pd-container-title-bar")
    title = (By.CSS_SELECTOR, title_bar[1] + " div.pd-container-title")
    options = (By.CSS_SELECTOR, title_bar[1] + " div[title='Options']")
    options_icon = (By.CSS_SELECTOR, "div.ds-icon-setting")
    maximize = (By.CSS_SELECTOR, title_bar[1] + " div[title='Maximize']")
    maximize_icon = (By.CSS_SELECTOR, "div.ds-icon-expand")
    restore = (By.CSS_SELECTOR, title_bar[1] + " div[title='Restore']")
    restore_icon = (By.CSS_SELECTOR, "ds-icon-collapse")
    frame = (By.CSS_SELECTOR, "div.pd-cont-iframe iframe")
    loading = (By.CSS_SELECTOR, "div.ibx-busy-container")
    resize_se = (By.CSS_SELECTOR, "div.ui-resizable-se:not([style*='display: none;'])")
    resize_sw = (By.CSS_SELECTOR, "div.ui-resizable-sw:not([style*='display: none;'])")
    resize_s = (By.CSS_SELECTOR, "div.ui-resizable-s:not([style*='display: none;'])")
    resize_e = (By.CSS_SELECTOR, "div.ui-resizable-e:not([style*='display: none;'])")
    resize_w = (By.CSS_SELECTOR, "div.ui-resizable-e:not([style*='display: none;'])")
    
    class Tab:
        
        container_content = (By.CSS_SELECTOR, "div.pd-container-content")
        tab_content = (By.CSS_SELECTOR, container_content[1] + " div.pd-cont-tab-page")
        tab = (By.CSS_SELECTOR, container_content[1] + " div.ibx-tab-button[role='tab']")
        title = (By.CSS_SELECTOR, tab[1] + " .ibx-label-text")
        new_button = (By.CSS_SELECTOR, container_content[1] + " div.tab-new-button")
        overflow_icon = (By.CSS_SELECTOR, container_content[1] + " div.tab-overflow-button .ds-icon-ellipse")
        new_tab_icon_in_overflow_menu = (By.CSS_SELECTOR, "div.tab-overflow-menu-item div.ds-icon-plus")
        
    class Carousel:
        
        content = (By.CSS_SELECTOR, "div.pd-container-content ")
        slides = (By.CSS_SELECTOR, content[1] + "div.ibx-csl-items-box [data-ibx-type='pdContent']")
        previous_slide =  (By.CSS_SELECTOR, content[1] + "div[title='Previous slide']")
        next_slide = (By.CSS_SELECTOR, content[1] + "div[title='Next slide']")
        go_to_slide_pin = (By.CSS_SELECTOR, content[1] + "div.ibx-csl-page-marker[title*='Go to slide']")
        selected_slider_pin =  (By.CSS_SELECTOR, content[1] + "div.ibx-csl-items-box div.ibx-csl-page-selected")
        
    class Accordion:
    
        content = (By.CSS_SELECTOR, "div.pd-container-content")
        area = (By.CSS_SELECTOR, content[1] + " div.pd-cont-acc-page")
        title = (By.CSS_SELECTOR, area[1] + " div.ibx-accordion-button-text")
        Add = (By.CSS_SELECTOR, content[1] + " div.pd-cont-accordion-add-button div.ds-icon-plus")
        area_content = (By.CSS_SELECTOR, area[1] + " div.pd-cont-iframe")
    
    class Workspace:
        
        content_resource = (By.CSS_SELECTOR, "div[data-ibxp-type='workbench']")
        content_items = (By.CSS_SELECTOR, content_resource[1] + " div.ibx-tree-browser-node>div.tnode-label")
        
class Heading:
    
    page_header = (By.CSS_SELECTOR, "div.pd-page-header ")
    heading = (By.CSS_SELECTOR, page_header[1] + "div.pd-page-title ")    
    refresh = (By.CSS_SELECTOR, page_header[1] + "div.pd-header-button-refresh")
    refresh_icon = (By.CSS_SELECTOR, refresh[1] + "div.ds-icon-refresh")
    show_filter = (By.CSS_SELECTOR, page_header[1] + "div[title='Show filters']")
    show_filter_icon = (By.CSS_SELECTOR, show_filter[1] + "div[style*='filter-off.svg']")
    hide_filter = (By.CSS_SELECTOR, page_header[1] + "div[title='Hide filters']")
    hide_filter_icon = (By.CSS_SELECTOR, hide_filter[1] + "div[style*='filter-on.svg']")
    export_to_file = (By.CSS_SELECTOR, page_header[1] + "div[title='Export to file']")
    export_to_file_icon = (By.CSS_SELECTOR, export_to_file[1] + "div.fa-file-export")
    
    
class FilterGrid:
    
    filter_grid_parent = (By.CSS_SELECTOR, "div[data-ibx-name='_regularFilterWrapper'] ")
    filter_grid = (By.CSS_SELECTOR, "div[data-ibx-type='pdFilterGrid'].pd-filter-grid ")
    grid_cells = (By.CSS_SELECTOR, filter_grid[1] + "div.pd-filter-cell")
    controls = (By.CSS_SELECTOR, grid_cells[1] + " div.pd-filter-panel")
    control_labels = (By.CSS_SELECTOR, controls[1] + " div.pd-amper-label")
    control_box = (By.CSS_SELECTOR, controls[1] + " div.pd-amper-control")
    
    class Slider:
        
        slider = (By.CSS_SELECTOR, "div.pd-amper-control.ibx-slider ")
        min_value = (By.CSS_SELECTOR, slider[1] + "div.ibx-slider-label-min")
        max_value = (By.CSS_SELECTOR, slider[1] + "div.ibx-slider-label-max")
        value = (By.CSS_SELECTOR, slider[1] + "div.ibx-slider-label-value")
        marker1 = (By.CSS_SELECTOR, slider[1] + "div.ibx-slider-marker-one")
        marker2 = (By.CSS_SELECTOR, slider[1] + "div.ibx-slider-marker-two")
        line = (By.CSS_SELECTOR, slider[1] + "div.ibx-slider-body-start")
        
    class Toggle:
        
        toggle = (By.CSS_SELECTOR, "div[data-ibx-type='ibxAmperToggleSwitch']")
        toggle_labels = (By.CSS_SELECTOR, "div[class^='pd-amper-toggle-switch'][data-ibx-type='ibxLabel']")
        toggle_checked = (By.CSS_SELECTOR, "div[data-ibx-type='ibxAmperToggleSwitch'] div[class*='pd-amper-toggle-switch-ctrl'][class*='checked']")
        toggle_unchecked = (By.CSS_SELECTOR, "div[data-ibx-type='ibxAmperToggleSwitch'] div[class*='pd-amper-toggle-switch-ctrl']")
        
    class DoubleList:
        
        double_list = (By.CSS_SELECTOR, "div[data-ibx-type='ibxAmperDoubleList']")
        double_list_pop_up = (By.CSS_SELECTOR, "div.pd-dual-list-box-popup ")
        
        
        
        
        
        
        