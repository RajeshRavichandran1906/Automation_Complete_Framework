from selenium.webdriver.common.by import By
class VisualizationPropertiesLocators(object):
    
    ''' Filter Prompt'''
    filter_prompt_checked = "//span[contains(text(),'{0}')]/../../../../tr/td/div/form/div/table/tbody/tr/td/div/input[@checked='checked']"
    prompt_dropdown = (By.CSS_SELECTOR, "[id^='FilterBox'] [src^='data:image/png;base64']")
    prompt_dropdown_8201 = (By.XPATH, "//*[contains(@src,'ar_images/irbpoparw.png')]")
    prompt_option_dropdown = '//td[contains(text(),"{0}")]'
    
    ''' Slider '''
    prompts =  '//*[contains(@id,"Prompt_{0}")]//form[contains(@id, "slider")]'  
    slider_min = '//span[contains(@id,"s_min")]'
    slider_max = '//span[contains(@id,"s_max")]'
    prompt_val = '//input[@checked="checked"][@value="{0}"]'