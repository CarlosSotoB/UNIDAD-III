# Author: Jose Carlos Soto Barco
#description: a chain is declared


class Handler: # Abstract handler
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor # Define who is the next handler

    def handle(self, request):
        handler = self._handler(request)# If handled, stop here

        #Otherwise, keep going
        if not handler:
            self._successor.handle(request)

    def _handler(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): # Inherits from the abstract handler
    """ Concrete handler 1 """
    def _handler(self, request):
        if 0 < request <= 10: # Provite a condition for handling
            print(" Request {} handled in handler 1 ".format(request))
            return True # Indicates that the request has been handled

class DefaultHandler(Handler): # Inherits from the abstract handler
    """ Default handler """
    def _handler(self, request):
        """ If there is no handler available """
        #No condition checking since this a default handler
        print("End of chain, no handler for {}".format(request))
        return True # indicates that the request has been handled

class Client: #Using handlers
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))#create handlers and use them in a sequence you want
                                                            #Note that the default handler has no succesor

    def delegate(self, requests): # Send your request one at a time for handlers to handler
        for request in requests:
            self.handler.handle(request)

# Create a client
c = Client()

# Create request
requests =[2, 5, 30]

# Send the requests
c.delegate(requests)