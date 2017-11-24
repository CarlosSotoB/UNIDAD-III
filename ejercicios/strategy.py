# Author: Jose Carlos Soto Barco
#description: a strategy is declared

import types # Import the types module


class Strategy:
    """ The Strategy Pattern class """

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a references to a function is provided, replace the execute() method the given function

    def execute(self): # This gets replaced by anoyher version if another strategy is provided
        """ The default method tht prints the name of the strategy being used """
        print("{} is used! ".format(self.name))

# replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

# Replace method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))

# Let's create our default strategy
s0 = Strategy()
#Let's execute our default strategy
s0.execute()

# Let's create the first of default strategy by providing new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()