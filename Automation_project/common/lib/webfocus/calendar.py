from selenium.webdriver.support.ui import Select
from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utillobject
from common.lib.core_utility import CoreUtillityMethods as coreutilobj

class Calendar(BasePage):
    
    calendar_css=None
    
    def __init__(self, driver):
        super(Calendar, self).__init__(driver)
        
    def get_calander_object(self):
        calendar_css_css=Calendar.calendar_css
        calendar_description='Calendar'
        calendar_elements=utillobject.validate_and_get_webdriver_objects(self, calendar_css_css, calendar_description)
        return calendar_elements[-1]
    
    def get_arrow(self, arrow_type):
        if arrow_type == 'left':
            arrow_css=Calendar.calendar_css+'.ui-datepicker-header ui-datepicker-prev'
            arrow_description='Calendar left arrow'
        else:
            arrow_css=Calendar.calendar_css+'.ui-datepicker-header ui-datepicker-next'
            arrow_description='Calendar next arrow' 
        arrow_element=utillobject.validate_and_get_webdriver_object(self, arrow_css, arrow_description)
        return arrow_element
    
    def select_arrow(self, arrow_type='left'):
        required_arrow_element=Calendar.get_arrow(self, arrow_type)
        coreutilobj.python_left_click(self, required_arrow_element)
        
    def select_month(self, month_name):
        month_css=Calendar.calendar_css+'.ui-datepicker-header .ui-datepicker-month'
        month_description='month dropdown'
        month_element=utillobject.validate_and_get_webdriver_object(self, month_css, month_description)
        select = Select(month_element)
        select.select_by_value(month_name)
        
    def select_year(self, year_name):
        year_css=Calendar.calendar_css+'.ui-datepicker-header .ui-datepicker-year'
        year_description='year dropdown'
        year_element=utillobject.validate_and_get_webdriver_object(self, year_css, year_description)
        select = Select(year_element)
        select.select_by_value(year_name)
        
    def get_date_element(self, date_value):
        token=False
        date_css=Calendar.calendar_css+'table.ui-datepicker-calendar td' 
        date_description='date buttons'
        date_elements=utillobject.validate_and_get_webdriver_objects(self, date_css, date_description)
        for date_element in date_elements:
            if date_element.text.strip() == date_value:
                token=True
                return date_element
        if token==False:
            error_msg='The requested date value [' + date_value + '] is not available in the calendar.'
            raise LookupError(error_msg)
    
    def select_date(self, date_value):
        date_element=Calendar.get_date_element(self, date_value)
        coreutilobj.python_left_click(self, date_element)   
         
class Single_Calendar(Calendar):
    calendar_css = 'div.ui-datepicker'

class Range_Calendar(Calendar):
    calendar_css = 'div.ui-datepicker > .ui-datepicker-group-first'
    