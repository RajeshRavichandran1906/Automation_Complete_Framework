from selenium.webdriver.common.by import By


class VisualizationCanvas:
    
    chart_preview = (By.CSS_SELECTOR, "div[id*='chartpreview']")
    
    
    class FormattingToolbar:
        
        font_name = (By.CSS_SELECTOR, "div[title='Font Name']")
        font_size = (By.CSS_SELECTOR, "div[title='Font Size']")
        bold = (By.CSS_SELECTOR, "div[title*='bold']")
        italic = (By.CSS_SELECTOR, "div[title*='italic']")
        underline = (By.CSS_SELECTOR, "div[title*='underline']")
        left_align = (By.CSS_SELECTOR, "div[title*='Left']")
        centered = (By.CSS_SELECTOR, "div[title*='Centered']")
        right_align = (By.CSS_SELECTOR, "div[title*='Right']")
        text_color = (By.CSS_SELECTOR, "div.tb-colorSwatch-fore")
        background_color = (By.CSS_SELECTOR, "div.tb-colorSwatch-back")
        close = (By.CSS_SELECTOR, "div[title='Close']")
        color_palette = (By.CSS_SELECTOR, "div[data-ibx-type='colorSwatchPopup']")
        color = "div[data-ibx-type='colorSwatchPopup'] div[title='{}']"
        
    
    class Heading:
        
        heading = (By.CSS_SELECTOR, "div[data-ibx-type='wfcHeading'] div[role='region']")
        iframe = (By.CSS_SELECTOR, heading[1] + " iframe.ibx-iframe-frame")
        text = (By.CSS_SELECTOR, "body font textnode")
        parent = (By.CSS_SELECTOR, "body")
        title = (By.CSS_SELECTOR, parent[1] + " span[style*='font-size']")
    
    
        class RunMode:
            
            parent = (By.CSS_SELECTOR, "foreignObject[class='title']")
        
        
    class Footing:
        
        footing = (By.CSS_SELECTOR, "div[data-ibx-type='wfcFooting'] div[role='region']")
        iframe = (By.CSS_SELECTOR, footing[1] + " iframe.ibx-iframe-frame")
        
        
        class RunMode:
            
            parent = (By.CSS_SELECTOR, "foreignObject[class='footnote']")
            
            
    class RunMode:
        
        class AutoDrill:
            
            auto_drill_parent = (By.CSS_SELECTOR, "[id*='tdgchart-tooltip'][style*='visible']")
            menu_options = (By.CSS_SELECTOR, auto_drill_parent[1] + " ul li[class*='tdgchart-tooltip-pointer']")
            parent_menu_options = (By.CSS_SELECTOR, auto_drill_parent[1] + ">div>ul>li:nth-child(3)")
            sub_menu_parent = (By.CSS_SELECTOR, parent_menu_options[1] + " div[class*='tdgchart-submenu'][style*='visible']")
            sub_menu_options = (By.CSS_SELECTOR, sub_menu_parent[1] + " ul li[class*='tdgchart-tooltip-pointer']")
            tooltip_values = (By.CSS_SELECTOR, auto_drill_parent[1] + " li.tdgchart-tooltip-pad table tr td")
            
            
        class BreadCrumbTrail:
            
            bread_crumb_trail = (By.CSS_SELECTOR, "foreignObject[class='title'] span")
             
            
            
            