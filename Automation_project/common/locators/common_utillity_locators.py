from selenium.webdriver.common.by import By
class CommonUtillityLocators(object):
    
    '''Field Tab - Grouping'''
    group = (By.XPATH, "//div[contains(@id,'groupSelValuesBtn')]/div")
    rename = (By.XPATH, "//div[contains(@id,'renameGrpBtn')]/div")
    ungroup = (By.XPATH, "//div[contains(@id,'ungroupBtn')]/div")
    ungroup_all = (By.XPATH, "//div[contains(@id,'ungroupAllBtn')]/div")
    show_other = (By.XPATH, "//div[contains(@id,'toggleOtherBtn')]/div")
    ok_button = (By.XPATH,"//div[contains(@id,'dynaGrpsOkBtn')]/div")
    grp_tree =  "//div[contains(@id,'dynaGrpsValuesTree')]//td[contains(text(),'{0}')]/img[1]"
