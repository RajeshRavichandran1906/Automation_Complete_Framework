from runners import DefaultRunner
from runners import WiniumRunner
import testrailreadcofiguration 
class RunnerFactory:
    @classmethod
    def getInstance(cls, product, confid, release): 
        
        #try
        tr = testrailreadcofiguration.TestRailReadConfiguration()
        key="prodid"
        result_dictionary = tr.get_result_dictionary(key)
        if (result_dictionary == None):
            raise KeyError('Unable to get the requested dictionary as the ' + key + ' is not currently a valid request to TestRail.')
        product_key = result_dictionary.get(product)
        if (product_key == None):
            raise KeyError('The requested product ' + key + ' is not currently a valid release choice in TestRail.')
        
        key="configurations"
        result_dictionary = tr.get_result_dictionary(key)
        if (result_dictionary == None):
            raise KeyError('Unable to get the requested dictionary as the ' + key + ' is not currently a valid request to TestRail.')
        configuration_key = result_dictionary.get(confid)
        if (configuration_key == None):
            raise KeyError('The requested configuration ' + key + ' is not currently a valid release choice in TestRail.')
        
        print('RunnerFactory for product: [' + product + '] and release: [' + release + ']')
        
        if product in ('as') and release in ('8201m'):
            obj = WiniumRunner.Focshell(confid, release)
        elif product in ('as'):
            obj = WiniumRunner.WiniumRunner(confid, release)
        else:    
            obj = DefaultRunner.DefaultRunner()
        return(obj)

        