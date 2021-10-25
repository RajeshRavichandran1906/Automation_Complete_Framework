class Wf_Exception_Handler():
    
    
    def __init__(self, msg=None):
        self.msg = msg
    
    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        return exception_msg

class LookupDomainFolder(Wf_Exception_Handler):
    """
    Thrown when an error has occurred on the server side.

    This may happen when communicating with the firefox extension
    or the remote driver server.
    """
    pass

        