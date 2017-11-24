# Author: Jose Carlos Soto Barco
#description: an iterator is declared

def count_to(count):
    """ Our iterator implementation """

    # Our list
    number_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    #Creates a tuple such as (1, "eins")
    iterator = zip(range(count), number_in_german)

    # Iterate throungh our iterable list
    # Extract the German number
    # Put them in a generator called number
    for position, number in iterator:

        # Returns a 'generator' containing number in German
        yield number

# Let's test generator returned by our iterator
for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))