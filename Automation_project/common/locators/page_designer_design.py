
class ToolBar :
    
    PARENT_CSS                  = "div[data-ibx-type='pdTool']>div[class*='pd-toolbar'] "
    APPLICATION_BUTTON_CSS      = PARENT_CSS + "div[class*='pd-logo']"
    SAVE_BUTTON_CSS             = PARENT_CSS + "div[title*='Save']"
    PREVIEW_BUTTON_CSS          = PARENT_CSS + "div[title='Preview']"
    QUICK_FILTER_BUTTON_CSS     = PARENT_CSS + "div[title='Quick filter']"
    PAGE_FILTER_BUTTON_CSS      = PARENT_CSS + "div[title='Page filter configuration']"
    INFO_MODE_BUTTON_CSS        = PARENT_CSS + "div[title*='Info mode']"
    HELP_BUTTON_CSS             = PARENT_CSS + "div[title*='Help']"
    PROPERTY_BUTTON_CSS         = PARENT_CSS + "div[title='Properties']"
    RESOURCES_BUTTON_CSS        = PARENT_CSS + "div[title='Resources']"
    PROPERTY_TAB_CONTENT_CSS    = "div[class^='pd-{0}-tab-page'] div[data-ibx-type='ibxAccordionPage'] div[class*='ibx-accordion-button-text']"
    PROPERTY_TAB_CSS    = "div[data-ibx-type='ibxTabPane'][class*='ibxtool-right-tab-pane'] div[class^='ibx-tab-button'][title='{0}']"

class ContentTab :
    
    PARENT_CSS                  = "div[class*='pd-content-tab-page'] "
    EXPANDED_CONTENT_CSS        = PARENT_CSS + "div[data-ibx-type='pdTreeBrowserNode'].tnode-expanded"
    EXPANDED_CONTENT_LABEL_CSS  = EXPANDED_CONTENT_CSS + " >.tnode-label"
    EXPANDED_CONTENT_ITEMS_CSS  = EXPANDED_CONTENT_CSS + ">div[class*='tnode-children']>.ibx-tree-node"
    CONTENT_EXPAND_ICON_CSS     = ".tnode-btn-collapsed"
    BASIC_CONTAINER_CSS = "[data-ibxp-btn-options*='Basic'][data-ibxp-btn-options*='Containers']"
    BASIC_CONTAINER_ITEM_CSS = BASIC_CONTAINER_CSS + " [data-ibxp-conttype='{0}']"
    REPOSITORY_WIDGETS_CSS = "[data-ibxp-btn-options*='Repository'][data-ibxp-btn-options*='Widgets']"
    REPOSITORY_WIDGETS_ITEM_CSS = REPOSITORY_WIDGETS_CSS + " .ibx-glyph-{0}"
    CONTENT_SEARCH_TEXTBOX_CSS = ".ibfs-tree-search-edit input[type='search']"
    CONTENT_SEARCH_BUTTON_CSS = ".ibfs-tree-search-btn .fa-search"
    PUBLISHED_CONTENT_CSS = "div[data-ibx-type='pdTreeBrowserNode']:not(.ibfs-tree-node-private)"
    UNPUBLISHED_CONTENT_CSS = "div[data-ibx-type='pdTreeBrowserNode'].ibfs-tree-node-private"

class NewPagePopModal :
    
    PARENT_CSS                  = "div[data-ibx-type='pdNewPage'] "
    TEMPLATES_CSS               =  PARENT_CSS + "div[class*='pd-np-item']"

class ApplicationMenu :
    
    PARENT_CSS                  = "div[class*='pd-tool-menu'][class*='pop-top'] "
    MENU_ITEMS_CSS              = PARENT_CSS + "div[data-ibx-type='ibxMenuItem']"

class Designer:
    
    TAB_SELECTION_CSS = ".ibx-csl-items-box.ibx-selection-manager[role='tablist'] .wb-tab-button"
    
class Designer_chart_workbook_data_tab :
    
    PARENT_CSS                  = ".designer-tab-page.tpg-selected"
    DATA_PAGE_FRAME_CSS         = "{0} .ibx-iframe-frame".format(PARENT_CSS)
    NODE_BROWSER_CSS            = '[data-ibx-type="ibxTreeBrowserNode"]'
    JOIN_CANVAS_CSS             = '.wcx-graph-top'

class FilterModalWindow:
    
    PARENT_CSS = ".pd-filter-window.pop-top"
    BUTTONS_CSS = PARENT_CSS + " .fbx-justify-content-end [role='button']"
    