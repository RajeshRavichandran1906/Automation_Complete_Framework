from selenium.webdriver.common.by import By


class Map:
    
    legend_title = (By.CSS_SELECTOR, "text.colorScaleLegend-title")
    legend_lables = (By.CSS_SELECTOR, "text[class^='colorScale-labels']")
    map_title = (By.CSS_SELECTOR, "foreignObject[class='title']")
    scale_title = (By.CSS_SELECTOR, "text[class='sizeLegend-title']")
    scale_values = (By.CSS_SELECTOR, "text[class^=sizeLegend-labels]")
    