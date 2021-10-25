from selenium.webdriver.common.by import By
class ActiveMiscelaneousLocators(object):

    ''''Title Area'''
    move_toBottom = (By.CSS_SELECTOR, '[title$="Bottom"] img')
    move_toTop = (By.CSS_SELECTOR, '[title$="Top"] img')           
    summation = (By.CSS_SELECTOR, '[title="Toggle Calculation Type"] img')
    itable_row = "#ITableData0 > tbody > tr:nth-child({0})"
    Aggregation="#ITableData0 > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > span:nth-child(1)"
    active_chart_container = (By.CSS_SELECTOR, 'div#Pie1.chartContainer')
    
    '''Chart Tool '''
    
    
    chart_tool_title_inner = "#wall{0} td[align='center'] div"
    charts_series_title = "#wall{0} [id^='ttpanel_']"
    
    yaxis_title = (By.CSS_SELECTOR,'text.yaxis-title')
    xaxis_title = (By.CSS_SELECTOR, 'text.xaxisNumeric-title')  