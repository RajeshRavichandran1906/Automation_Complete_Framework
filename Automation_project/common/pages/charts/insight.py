from common.pages import charts 
from common.locators.charts import insight
from common.pages.basepage import BasePage
from common.pages.insight_header import Insight_Header
from common.lib.webfocus.ibx_custom_controls import ibxSelectItemList


class Insight(BasePage): 
    
    def __init__(self):
        
        super().__init__()
        self._locators = insight.Insight
        
    @property
    def Bar(self): return charts.bar.Bar(parent_locator=self._locators.insight_chart)
    
    @property
    def Pie(self): return charts.pie.Pie(parent_locator=self._locators.insight_chart)
    
    @property
    def InteractiveHeader(self): return Insight_Header(self._driver)
    
    @property
    def SelectItemList(self): return ibxSelectItemList()

    
    