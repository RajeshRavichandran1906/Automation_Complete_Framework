from builtins import object

class DesignerChart(object):
    
    MEASURES_TAB_CSS = "div[class*='metadata-container'][class*='measure-tree-box'] [class*='tnode-children'] [class*='tnode-label']"
    DIMENSIONS_TAB_CSS = "div[class*='metadata-container'][class*='dimension-tree-box'] [class*='tnode-children'] [class*='tnode-label']"
    DIMENSIONS_VERIFY_CSS = "div[class*='metadata-container'][class*='dimension-tree-box'] [class*='tnode-label']"
    MEASURES_VERIFY_CSS = "div[class*='metadata-container'][class*='measure-tree-box'] [class*='tnode-label']"
    DIMENSIONS_FIELD_AREA_CSS="div[class*='metadata-container'][class*='dimension-tree-box'] .wfc-mdfp-dimension-tree"
    MEASURES_FIELD_AREA_CSS="div[class*='metadata-container'][class*='measure-tree-box'] [class*='wfc-mdfp-measure-tree']"
    TOOLBAR_CSS = ".wfc-main-toolbar"
    SAVE_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcTBButtonSave']"
    UNDO_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcTBButtonUndo']"
    REDO_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcTBMenuRedo']"
    PREVIEW_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcTBButtonPreview']"
    THUMBNAIL_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcThumbnail']"
    LAYOUT_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcTBButtonLayoutOptions']"
    MORE_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcTBMenuMore']"
    SETTINGS_BUTTON_CSS  = TOOLBAR_CSS + " div[data-ibx-name='wfcTBButtonSettings']"
    HELP_BUTTON_CSS = TOOLBAR_CSS + " div[data-ibx-name='wfcTBButtonHelp']"
    SPACER_CSS = TOOLBAR_CSS + " .ibxtool-toolbar-group-spacer"
    POPUP_CSS = "div[class*='pop-top'][data-ibx-type='ibxMenu']"
    HEADING_CSS = ".wfc-bc-heading-area .wfc-bc-heading-title"
    FOOTING_CSS = ".wfc-bc-footing-area .wfc-bc-heading-title"
    VARIABLES_CSS = ".wfc-mdfp-variables-tree [class*='tnode-label']"
    HEADING_FOOTING_TOOLBAR_CSS = ".re-toolbar-main"
    FILTER_BAR = ".filter-bar"
    FORMAT_QUICK_ACCESS = ".wfc-chart-quick-access-menu"
    QUICK_MARKER_MARKER = '[data-ibx-name="seriesShapeMarker"] [aria-label="Circle"]'
    CHART_THEME_INPUT = ".wfc-chart-theme-select-property"
    QUERY_CSS = ".wfc-bucket-display-box"
    LABELS_CSS = "div[data-ibx-name='axisLabelsPage']"
    TITLE_CSS = "div[data-ibx-name='axisTitlePage']"
    ROTATION_CSS = LABELS_CSS + " div[data-user-data='xAxisLabelsRotation']"
    FONT_CSS = "div[data-ibx-name='axisLabelsFontFormatter']"
    COLOURS_CSS = "div[data-ibx-name='wfcColorPopup'][aria-hidden='false'] .pp-swatch-box .pp-swatch"
    DIMENSIONS_MENU_BUTTON = '.dimension-menu-btn'
    MEASURES_MENU_BUTTON = ".measure-menu-btn"
    NEW_CALCULATIONS_DIMENSIONS = ".wfc-mdfp-whole-tree  [class*='tnode-children'] [class*='tnode-label']"
    CALCULTION_FRAME = ".wfc-calculator-rich-edit iframe"
    CALCULTION_DIALOG_NAME = ".wfc-expression-name input[role='textbox']"
    LEGEND_LABELS_CSS="div[data-ibx-name='legendLabelsPage']"
    CHART_EXPAND_BUTTON = ".wfc-chartpicker-next-button"
    CHART_PICKER_DEFAULT = ".wfc-chartpicker-buttons-box"
    CHART_PICKER_EXPANDED = '.wfc-chartpicker-extended-container'
    LINE_STYLE_CSS='.wfc-line-select-menu.pop-top'
    LINE_DROPDOWN_CSS='.wfc-chart-line-style[data-ibx-name="seriesLine"] .wfc-line-dash'
    QUERY_BUCKET_CSS = ".wfc-bucket-display-box [data-ibx-type='bucket']"
    QUERY_BUCKET_CONTAINER_CSS = ".wfc-bucket-pills"
    QUERY_BUCKET_FIELD_CSS = "{0} .wfc-bucket-pill".format(QUERY_BUCKET_CONTAINER_CSS)
    QUERY_BUCKET_FIELD_REMOVE_BUTTON_CSS = ".wfc-bucket-pill-delete .ibx-glyph-times-small"
    RIBBON_APPLICATION_BUTTON_CSS = "[class*='ibxtool-toolbar'][class*='main-toolbar'] div[class*='pd-logo']"
    POP_TOP_CSS = '.pop-top'
    QUERY_BUCKET_DISPLAY_TOOLBAR_CSS = ".tpg-selected .wfc-bucket-toolbar [title]:not([style*='none'])"
    DATA_GRID = ".chartPanel .tablePanel"
    DATA_GRID_ROW_HEADER1 = DATA_GRID + " .rowTitle text"
    DATA_GRID_ROW_CELL1 = DATA_GRID + " .rowHeader text"
    DATA_GRID_ROW_HEADER2 = DATA_GRID + " .colHeaderScroll text"
    DATA_GRID_ROW_CELL2 = DATA_GRID + " .innerTable [class*='row']"
    
        
    
class DesignerInsight(object):
    
    INSIGHT_PREVIEW_FRAME = ".ides-tool-preview-frame .ibx-iframe-frame"
    OPTIONS_BOX = ".header-box .options-box"
    QUERY_BOX = ".header-box .query-box"
    RESET_BUTTON = OPTIONS_BOX + " .reset-button"
    PIVOT_BUTTON = OPTIONS_BOX + " .pivot-button"
    CHART_PICKER_BUTTON = OPTIONS_BOX + " .chart-picker-button"
    FILTER_BUTTON = OPTIONS_BOX + " .filter-button"
    MORE_OPTIONS_BUTTON = OPTIONS_BOX + " .more-options-button"
