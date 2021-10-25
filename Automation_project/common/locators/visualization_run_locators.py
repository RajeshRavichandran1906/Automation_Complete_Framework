from selenium.webdriver.common.by import By
class VisualizationRunLocators(object):
    
    ''' Run menu icon & option > Locators  saved here'''
    run_menu_icon = (By.XPATH,"//div[contains(@onclick,'toggleBottomMenu(1)')]")
    grid_icon = (By.XPATH, "//span[contains(@onclick,'mshowReport(1)')]/div")
    reset_icon = (By.XPATH, "//span[contains(@onclick,'mresetDashboard(1)')]/div")
    removeFilter_icon = (By.XPATH,"//span[contains(@onclick,'ibiChart.removeFilter(-1,1)')]/div")