from common.pages.basepage import BasePage
from common.locators.charts import common as Locators

class Common(BasePage):
    
    def __init__(self, chart_name, riser_locator, parent_locator=Locators.html5_run_chart):
        
        BasePage.__init__(self)
        self._parent_locator = parent_locator
        self._name = chart_name + " Chart"
        self._locators = Locators.Common
        self._riser_locator = riser_locator
        
    def verify_xaxis_title(self, expected_title, step_num):
        """
        Description : verify chart x axis title 
        Parameters :
            expected_title = ['CAR','COUNTRY']
            step_num = example "04.01"
        Usage:
            verify_xaxis_title(['COUNTRY'], "04.01")
        """
        self._webelement.verify_elements_text(self._locators.xaxis_title, expected_title, step_num, self._name + " X-Axis title", parent_instance=self._parent_object)
    
    def verify_yaxis_title(self, expected_title, step_num):
        """
        Description : verify chart y axis title 
        Parameters :
            expected_title = ['CAR','COUNTRY']
            step_num= example "04.01"
        Usage:
            verify_yaxis_title(['CAR','COUNTRY'], "04.01")
        """
        self._webelement.verify_elements_text(self._locators.yaxis_title, expected_title, step_num, self._name + " Y-Axis title", parent_instance=self._parent_object)
        
    def verify_xaxis_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description : verify chart x axis labels 
        Parameters :
            expected_labels = ['CAR','COUNTRY']
            step_num = example "04.01"
        Usage:
            verify_xaxis_labels(['CAR','COUNTRY'], "04.01")
        """
        name = self._name + " X-Axis Labels"
        self._webelement.verify_elements_text(self._locators.xaxis_label, expected_labels, step_num, name, assert_type, label_len, slicing, self._parent_object)
        
    def verify_yaxis_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description : verify chart y axis labels 
        Parameters :
            expected_labels = ['0','10','12']
            step_num = example "04.01"
        Usage:
            verify_yaxis_labels(['CAR','COUNTRY'], "04.01")
        """
        name = self._name + " Y-Axis Labels"
        self._webelement.verify_elements_text(self._locators.yaxis_label, expected_labels, step_num, name, assert_type, label_len, slicing, self._parent_object)
    
    def verify_column_title(self, expected_title, step_num):
        """
        Description : verify chart column title
        Parameters :
            expected_title = ['CAR:SEDAN']
            step_num = example "04.01"
        Usage:
            verify_column_title(['CAR:SEDAN','COUNTRY:ENGLAND'], "04.01")
        """
        self._webelement.verify_elements_text(self._locators.column_title, expected_title, step_num, self._name + " Y-Axis title", parent_instance=self._parent_object)
    
    def verify_row_title(self, expected_title, step_num):
        """
        Description : verify chart row title
        Parameters :
            expected_title:list = ['CAR:SEDAN']
            step_num:str = example "04.01"
        Usage:
            verify_row_title(['CAR:SEDAN','COUNTRY:ENGLAND'], "04.01")
        """
        self._webelement.verify_elements_text(self._locators.row_title, expected_title, step_num, self._name + " Y-Axis title", parent_instance=self._parent_object)
    
    def verify_column_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description : verify column labels
        Parameters :
            expected_labels = ['CAR:SEDAN']
            step_num = example "04.01"
        Usage:
            verify_column_labels(['CAR:SEDAN','COUNTRY:ENGLAND'], "04.01")
        """
        name = self._name + " Column Labels"
        self._webelement.verify_elements_text(self._locators.column_label, expected_labels, step_num, name, assert_type, label_len, slicing, self._parent_object)
    
    def verify_row_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description : verify row labels
        Parameters :
            expected_labels = ['CAR:SEDAN']
            step_num = example "04.01"
        Usage:
            verify_row_labels(['CAR:SEDAN','COUNTRY:ENGLAND'], "04.01")
        """
        name = self._name + " Row Labels"
        self._webelement.verify_elements_text(self._locators.row_label, expected_labels, step_num, name, assert_type, label_len, slicing, self._parent_object)
    
    def verify_number_of_risers(self, expected_count, step_num):
        """
        Description : verify number of visible risers in chart
        Parameters :
            expected_count:int = Number of visible risers count
            step_num:str = example "04.01"
        Usage:
            verify_number_of_risers(10, "04.01")
        """
        msg = "Step {0} : Verify {1} risers displayed in {2}".format(step_num, expected_count, self._name)
        self._webelement.verify_number_of_visible_elements(self._riser_locator, expected_count, msg, self._parent_object)
    
    def verify_riser_color(self, riser_index_and_color, step_num, attribute='fill'):
        """
        Description : verify riser color by passing index of the riser
        Parameters :
            expected = (1, "blue")
            step_num = example "04.01"
        Usage:
            verify_riser_color([(1, "blue"), (2, "green")], "04.01")
        """
        risers = self._parent_object.find_elements(*self._riser_locator)
        msg = "Step {0} : Verify number {1} riser color in {2}"
        for index, color in riser_index_and_color:
            if index <= len(risers):
                self._webelement.verify_element_color_by_css_property(risers[index-1], attribute, color, msg.format(step_num, index, self._name), self._name + " Riser")
            else:
                raise IndexError("Number {} riser not found in {}".format(index, self._name))
                
    def wait_for_text(self, text, time_out=60, pause_time=1, case_sensitive=False):
        """
        Description: WebDiver will wait until given text visible on chart, Otherwise raise TimeOutError
        """
        self._webelement.wait_for_element_text(self._parent_locator, text, time_out, pause_time, case_sensitive)
        
    @property
    def _parent_object(self):
        
        return self._utils.validate_and_get_webdriver_object_using_locator(self._parent_locator, self._name + " Chart") 
    
    
class Legend(BasePage):
        
        def __init__(self, chart_name, marker_riser=Locators.Legend.markers, parent_locator=Locators.html5_run_chart):
        
            BasePage.__init__(self)
            self._parent_locator = parent_locator
            self._name = chart_name + " Chart"
            self._legend_locators = Locators.Legend
            self.marker_riser = marker_riser
        
        def verify_legend_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
            """
            Description : verify values in legend
            Parameters :
            expected_labels:list = ["ALFA ROMEO", "AUDI", "BMW"]
            step_num:str = "07.01"
            assert_type:str = 'equal'
            Usage:
            verify_legend_values(["ALFA ROMEO", "AUDI", "BMW"], "07.01")
            """
            name = self._name + "  Legend Labels"
            self._webelement.verify_elements_text(self._legend_locators.labels, expected_labels, step_num, name, assert_type, label_len, slicing, self._parent_object)
        
        def verify_legend_title(self, expected_title, step_num,):
            """
            Description : verify title of the legend
            Parameters :
            expected_title:str = "COUNTRY"
            step_num:str = "07.01"
            Usage:
            verify_legend_title("COUNTRY", "07.01")
            """
            self._webelement.verify_elements_text(self._legend_locators.title, expected_title, step_num, self._name + " Legend title", parent_instance=self._parent_object)
            
        def verify_legend_colors(self, legend_colors, step_num, assert_type='asequal'):
            """
            Description : verify colors of the legend
            Parameters :
            legend_colors:list[tuple(int, str)] = [(1, 'blue'), (2, 'green')]
            step_num:str = "07.01"
            assert_type:str = 'asequal'
            Usage:
            verify_legend_colors([(1, 'blue'), (2, 'green')], "07.01")
            """
            pass
        
        def verify_legend_is_expanded(self, step_num):
            """
            Description : verify legend is expanded
            Parameters :
            step_num:str = "04.01"
            Usage:
            verify_legend_is_expanded("04.01")
            """
            pass
    
        def verify_legend_is_collapsed(self, step_num):
            """
            Description : verify legend is collapsed
            Parameters :
            step_num:str = "04.01"
            Usage:
            verify_legend_is_collapsed("04.01")
            """
            pass
    
        def expand_legend(self):
            """
            Description : expand the legend section
            Usage:
            expand_legend_area()
            """
            pass
    
        def collapse_legend(self):
            """
            Description : collapse the legend section
            Usage:
            collapse_legend_area()
            """
            pass      