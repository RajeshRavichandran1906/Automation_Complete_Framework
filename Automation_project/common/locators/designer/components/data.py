from selenium.webdriver.common.by import By


class Data:
    
    DATA = (By.CSS_SELECTOR, "div.tool-container-data ")
    FRAME = (By.CSS_SELECTOR, "iframe.ibx-shell-tool-host")
    
    
    class Source:
        
        source_css = (By.CSS_SELECTOR, "div[qa='MFDataContent']")
        row_css = (By.CSS_SELECTOR, "div.wcx-grid-body-tree-row")
        
        
    class Canvas:
        
        canvas_css = (By.CSS_SELECTOR, "div[qa='MFGraphContent'] ")
        original_data_css = "div[class*='ds-flow-node'][qa='{}']"
        join_label_css = (By.CSS_SELECTOR, canvas_css[1] + "div[class*='ds-flow-node'] div.ds-node-label")
    
    
    class SampleData:
        
        sample_data_css = (By.CSS_SELECTOR, "div[qa='MFOutputContent']")
    
    
    class Toolbar:
        pass 
        