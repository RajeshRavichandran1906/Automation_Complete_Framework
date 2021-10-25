from selenium.webdriver.common.by import By

class Registration:
    
    form        =   (By.CSS_SELECTOR, "#trial-form #gform_1 ")
    country     =   (By.CSS_SELECTOR, form[1] + "select[name='input_6']")
    state       =   (By.CSS_SELECTOR, form[1] + "select[name='input_30']")
    first_name  =   (By.CSS_SELECTOR, form[1] + "input[name='input_1']")
    last_name   =   (By.CSS_SELECTOR, form[1] + "input[name='input_8']")
    email       =   (By.CSS_SELECTOR, form[1] + "input[name='input_10']")
    phone       =   (By.CSS_SELECTOR, form[1] + "input[name='input_11']")
    job_title   =   (By.CSS_SELECTOR, form[1] + "input[name='input_12']")
    company     =   (By.CSS_SELECTOR, form[1] + "input[name='input_13']")
    terms       =   (By.CSS_SELECTOR, form[1] + "input[name='input_14.1'][type='checkbox']")
    aws         =   (By.CSS_SELECTOR, form[1] + "input[type='radio'][id='choice_1_31_0']")
    azure       =   (By.CSS_SELECTOR, form[1] + "input[type='radio'][id='choice_1_31_1']")
    terms       =   (By.CSS_SELECTOR, form[1] + "input[name='input_14.1'][type='checkbox']")
    sumbmit     =   (By.CSS_SELECTOR,  form[1] + "input[id='gform_submit_button_1']")
    state_error =   (By.ID, "edit-field-state-error")
    fname_error =   (By.ID, "edit-field-first-name-0-value-error")
    lname_error =   (By.ID, "edit-field-last-name-0-value-error")
    email_error =   (By.ID, "edit-field-email-0-value-error")
    job_error   =   (By.ID, "edit-field-job-title-0-value-error")
    company_error=  (By.ID, "edit-field-company-0-value-error")
    terms_error =   (By.ID, "field_terms_and_conditions[value]-error")
    
    
