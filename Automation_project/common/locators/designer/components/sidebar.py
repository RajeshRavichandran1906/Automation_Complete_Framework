from selenium.webdriver.common.by import By


class SideBar:
    
    base_css = "div.ds-left-bar "
    outline = (By.CSS_SELECTOR, base_css + "div[title='View outline']")
    fields = (By.CSS_SELECTOR, base_css + "div[title='View fields']")
    container = (By.CSS_SELECTOR, base_css + "div[title='Add containers']")
    content = (By.CSS_SELECTOR, base_css + "div[title= 'Add content']")
    controls = (By.CSS_SELECTOR, base_css + "div[title= 'Add controls']")
    insights = (By.CSS_SELECTOR, base_css + "div[title='Get Insights']")
    filters  = (By.CSS_SELECTOR, base_css + "div[title='Filters']")
    outline_icon = (By.CSS_SELECTOR, "div.fa-sitemap")
    fields_icon = (By.CSS_SELECTOR, "div.fa-list")
    container_icon = (By.CSS_SELECTOR, "div.fa-window-maximize")
    content_icon = (By.CSS_SELECTOR, "div.fa-globe")
    controls_icon = (By.CSS_SELECTOR, "div.fa-toggle-on")
    