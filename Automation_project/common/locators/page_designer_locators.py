from selenium.webdriver.common.by import By

class PageDesigner(object):
    
    '==================================== Page Designer Tool Bar ===================================='
    
    QUICK_FILTER = (By.CSS_SELECTOR, "#filter>div[class*='quick-filter']")
    PREVIEW = (By.CSS_SELECTOR, "#preview>div[class*='preview']")
    PROPERTY = (By.CSS_SELECTOR, "#toggleright>div[class*='pane_properties']")
    RESOURCES = (By.CSS_SELECTOR, "#toggleleft>div[class*='pane_resources']")
    PAGE_FILTER = (By.CSS_SELECTOR, "#settings>div[class*='sliders']")
    HELP = (By.CSS_SELECTOR, "#help>div[class*='question']")
    SAVE = (By.CSS_SELECTOR, "#save>div[class*='floppy']")
    GO_BACK_DESIGN = (By.CSS_SELECTOR, "div[class*='pd-preview-button'][style*='visible']")
    
    '====================================== Page Header ======================================'
    
    PAGE_HEADER = (By.CSS_SELECTOR, "div[data-ibx-name='_header'][class*='pd-page-header']")
    PAHE_HEADER_TITLE = (By.CSS_SELECTOR, "div[class*='pd-page-title'][data-ibx-name='_title']")
    
    
    '====================================Page Canvas CSS===================================='
    
    'PANEL'
    PANEL_TITLE_CSS ="div[class*='pd-container-title-button'][title={0}]"
    FILTER_GRID_PARENT_CSS = "div[data-ibx-type='pdFilterGrid']"
    FILTER_BAR_GRID_CSS = "div.pd-regular-filter-wrapper " + FILTER_GRID_PARENT_CSS
    FILTER_MODEL_WINDOW_GRID_CSS = "div[data-ibx-type='pdFilterWindow']:not(.pop-closed) " + FILTER_GRID_PARENT_CSS
    PAGE_SECTION_PARENT_CSS = "div.pd-page-canvas div.pd-page-acc-section"
    PD_CONTAINER_CSS = "div[data-ibx-type='pdContainer']"
    PD_PANEL_CSS = PD_CONTAINER_CSS + " div[class*='pd-cont-relative']"
    
    'Filter Drop down control'
    FILTER_DROPDOWN_PARENT_CSS = "div[class*='pd-amper-select'][data-ibx-type*='Page']"
    
    'Filter Button set control'
    FILTER_BUTTONSET_PARENT_CSS = "div[data-ibx-type='ibxAmperButtonGroup'] .pd-amper-control-wrapper"
    FILTER_BUTTONSET_OPTIONS_CSS = FILTER_BUTTONSET_PARENT_CSS + " div[class*='ibx-check-box']"
    
    'Filter Radio button control'
    FILTER_RADIOGROUP_PARENT_CSS = "div[data-ibx-type='ibxAmperRadioGroup'] .pd-amper-control-wrapper"
    FILTER_RADIOGROUP_OPTIONS_CSS = FILTER_RADIOGROUP_PARENT_CSS + " div[data-ibx-type='ibxRadioButtonSimple']"
    FILTER_RADIOGROUP_BUTTON_ICON_CSS = "div[class^='ibx-radio-button-simple-marker'][class*='ibx-radio-button-simple-marker']"
    SELECTED_FILTER_RADIOGROUP_BUTTON_ICON_CSS = "div[class^='ibx-radio-button-simple-marker'][class*='ibx-radio-button-simple-marker-check']"
    
    'Filter date picker control'
    FILTER_DATE_PICKER_PARENT_CSS = "div[data-ibx-type^='ibxDate']"
    FILTER_DATE_PICKER_ICON_CSS = FILTER_DATE_PICKER_PARENT_CSS + " div[class*='fa fa-calendar']"
    FILTER_DATE_CLEAR_ICON_CSS = "div[class*='ibx-datepicker-clear']"
    
    'Filter date picker popup control'
    FILTER_DATE_PICKER_POPUP_PARENT_CSS = "div[class^='ibx-datepicker-popup'][class*='pop-top']"
    FILTER_DATE_PICKER_MONTH_SELECT_CSS = FILTER_DATE_PICKER_POPUP_PARENT_CSS + " select[class='ui-datepicker-month']"
    FILTER_DATE_PICKER_YEAR_SELECT_CSS = FILTER_DATE_PICKER_POPUP_PARENT_CSS + " select[class='ui-datepicker-year']"
    FILTER_DATE_PICKER_DATE_SELECT_CSS = FILTER_DATE_PICKER_POPUP_PARENT_CSS + " table[class='ui-datepicker-calendar']>tbody>tr>td[data-handler][data-month]"
    
    FILTER_CONTROL_CONVERTOR_POP_CSS = "div[data-ibx-type='ibxDialog'][class^='pd-filter-convert'][class*='pop-top']"
    FILTER_CONTROL_CONVERTOR_OPTIONS_CSS = FILTER_CONTROL_CONVERTOR_POP_CSS + " div[class^='pd-filter-btn'][data-ibx-type='ibxButton']:not([style*='none']"
    FILTER_CONTROL_CONVERTOR_POP_CLOSE_BTN_CSS = FILTER_CONTROL_CONVERTOR_POP_CSS + " div[class^='ibx-title-bar-close-button']"
    
    'Filter Check box'
    FILTER_CHECKBOX_PARENT_CSS = "div[data-ibx-type='ibxAmperRadioGroup'] .pd-amper-control-wrapper"
    FILTER_CHECKBOX_OPTIONS_CSS = FILTER_CHECKBOX_PARENT_CSS + " div[data-ibx-type='ibxCheckBoxSimple']"
    FILTER_CHECKBOX_OPTION_CHECK_ICON_CSS = "div[class*='ibx-check-box-simple-marker']"
    SELECTED_FILTER_CHECKBOX_OPTION_ICON_CSS = FILTER_CHECKBOX_OPTION_CHECK_ICON_CSS + "[class*='ibx-check-box-simple-marker-check']"
    
    'Filter Slider control'
    FILTER_SLIDER_PARENT_CSS = "div[class*='pd-amper-control'][class*='ibx-slider']"
    FILTER_SLIDER_MIN_VAL_CSS = FILTER_SLIDER_PARENT_CSS + " div[class*='ibx-slider-label-min']"
    FILTER_SLIDER_MAX_VAL_CSS = FILTER_SLIDER_PARENT_CSS + " div[class*='ibx-slider-label-max']"
    FILTER_SLIDER_SELECTED_VAL_CSS = FILTER_SLIDER_PARENT_CSS + " div[class*='ibx-slider-label-value']"
    FILTER_SLIDER_LINE_CSS = FILTER_SLIDER_PARENT_CSS + " div[class*='ibx-slider-body']"
    FILTER_SLIDER_MARKER1_CSS = FILTER_SLIDER_PARENT_CSS + " div[class*='slider-marker-one']"
    FILTER_SLIDER_MARKER2_CSS = FILTER_SLIDER_PARENT_CSS + " div[class*='slider-marker-two']"
    FILTER_SLIDER_RANGE_LINE_CSS = FILTER_SLIDER_PARENT_CSS +" div[class*='ibx-slider-range-body']"
    
    ''' Page Footer'''
    PAGE_TAB_GROUP=(By.CSS_SELECTOR, ".ibx-tab-position-bottom:not([style*='none'])")