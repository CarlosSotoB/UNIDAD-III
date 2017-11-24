# Author: Jose Carlos Soto Barco
# Description: observation of data

class Subject(object):  # Represents whats is being 'observed'

    def __init__(self):
        self._observers = []  # This where references to all the observers are being kept
                                # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple observers

    def attach(self, observer):
        if observer not in self._observers:  # If the observer is not alrealy in the observers list
            self._observers.append(observer)  # apped the observer to the list

    def detach(self, observer):  # simple remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # For all the observers in the list
            if modifier != observer:  # Don't notify the observer who is actually updating the temperature
                observer.update(self)  # Alert the observers!


class Core(Subject):  # Inherits form the Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # Set the name of the core
        self._temp = 0  # Initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()

class TempViewer:

    def update(self, subject):  # Alert method is invoked when tke notify() method in a concrete subject is invoked
        print(" Temperature Viewer: {} has Temperature{}".format(subject._name, subject._temp))


# Let's create our subject
c1 = Core("Core 1")
c2 = Core("Core 2")


# Let's create our observer
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)
# Let's changes the temperature of our first core
c1.temp = 80
c1.temp = 90
