
from common.pages.basepage import BasePage
from common.pages.designer import components
from common.pages.designer.dialog import Dialog
from common.pages.designer.page_canvas import PageCanvas
from common.pages.designer.components import filter_toolbar
from common.locators.designer import page_canvas as Locator
from common.lib.webfocus.ibx_custom_controls import ContextMenu 
from common.locators.designer.components.filter_toolbar import FilterToolbar as locators

class Designer(BasePage):
    
    def __init__(self):
        
        super().__init__()
    
    @property
    def API(self): return components.API()
    
    @property
    def ToolBar(self): return components.ToolBar()
    
    @property
    def SideBar(self): return components.SideBar()
    
    @property
    def VisualizationToolBar(self): return components.VisualizationToolBar()
    
    @property
    def ResourcesPanel(self): return components.ResourcesPanel()
    
    @property
    def PropertiesPanel(self): return components.PropertiesPanel()
    
    @property
    def Data(self): return components.Data()
    
    @property
    def Dialog(self): return Dialog()
    
    @property
    def PageCanvas(self): return PageCanvas()
    
    @property
    def VisualizationCanvas(self): return components.VisualizationCanvas()
    
    @property
    def RunMode(self): return _RunMode()
    
    @property
    def ContextMenu(self): return ContextMenu()
    
    @property
    def VisualizationFilterToolbar(self): return filter_toolbar.FilterToolbar()
    
    @property
    def PageFilterToolbar(self): return filter_toolbar.FilterToolbar(parent=locators.page_filter_toolbar, name="Page Filter Toolbar")
    
    @property
    def ContentPicker(self): return components.ContentPicker()
    
    
class _RunMode:
    
    @property
    def PageCanvas(self): return PageCanvas(Locator.RUN_MODE)    