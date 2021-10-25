'''
Created on Dec 4, 2018

@author: qaauto
'''      
class Exceptions(object):
    
    def exceptions_method(self, exception_type):
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, exception_type, lambda: "Exception not implemented")
        # Call the method as we return it
        return method()
 
    def NoSuchElementException(self):
        return "raise NoSuchElementException('The Provided element might be incorrect')"
 
    def AttributeError(self):
        return "raise AttributeError('The Provided element is currently not available on the page')"
 
    def TypeError(self):
        return "raise TypeError('The Provided element value is null')"       