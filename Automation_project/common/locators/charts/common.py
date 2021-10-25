from selenium.webdriver.common.by import By


html5_run_chart = (By.CSS_SELECTOR, "div[id*='jschart']")
insight_chart = (By.ID, "runbox_id")
content_chart = (By.CSS_SELECTOR, "div[id*='arpreview_fdmId_11']")

class Common:
    
    xaxis_title = (By.CSS_SELECTOR, "[class^='xaxis'][class$='title']")
    yaxis_title = (By.CSS_SELECTOR, "[class='yaxis-title']")
    xaxis_label = (By.CSS_SELECTOR, "[class^='xaxisOrdinal-labels']")
    yaxis_label = (By.CSS_SELECTOR, "[class^='yaxis-labels']")
    column_title = (By.CSS_SELECTOR, "[class^='colHeader']")
    row_title = (By.CSS_SELECTOR, "[class^='rowHeader']")
    column_label = (By.CSS_SELECTOR, "[class^='colLabel']")
    row_label = (By.CSS_SELECTOR, "[class^='rowLabel']")
    

class Legend:
    
    base_css = "g.legend "
    title = (By.CSS_SELECTOR, base_css +  "text.legend-title")
    background = (By.CSS_SELECTOR, base_css +  "path.legend-background")
    labels = (By.CSS_SELECTOR, base_css +  "[class^='legend-labels']")
    markers = (By.CSS_SELECTOR, base_css +  "[class^='legend-markers']")
    color_scale_title = (By.CSS_SELECTOR, base_css +  "text.colorScaleLegend-title")
    color_scale_labels = (By.CSS_SELECTOR, base_css +  "[class^='colorScale-labels']")
    size_legend_title = (By.CSS_SELECTOR, base_css +  "text.sizeLegend-title")
    size_legend_markers = (By.CSS_SELECTOR, base_css +  "[class^='sizeLegend-markers']")
    size_legend_labels = (By.CSS_SELECTOR, base_css +  "[class^='sizeLegend-labels']")
    