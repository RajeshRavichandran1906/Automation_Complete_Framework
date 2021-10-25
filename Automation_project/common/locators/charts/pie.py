from selenium.webdriver.common.by import By


class Pie:
    
    total_label = (By.CSS_SELECTOR, "text[class^='totalLabel']")
    pie_lables = (By.CSS_SELECTOR, "text[class^='pieLabel']")
    data_lables = (By.CSS_SELECTOR, "text[class^='dataLabels']")
