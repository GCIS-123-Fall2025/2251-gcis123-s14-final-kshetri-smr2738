"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
    __slots__ = ['__code', '__name', '__price']
    def __init__(self, code, name, price):
        self.__code = code
        self.__name = name
        self.__price = price

    def get_code(self, __code):
        return self.__code
    def get_name(self, __name):
        return self.__name
    def get_price(self, __price):
        return self.__price
    
    def set_code(self, code):
        self.__code = code
    def set_name(self, name):
        self.__name = name
    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return self.__name + " [" + self.__code + "] - $" + str(self.__price) 
    
    def __repr__(self):
        return '(' + self.__code + ', ' \
            + self.__name + ', ' \
            + str(self.__price) + ')'
        


# manual test from main() method
def main():
    i1 = Item('ABCD-1234', 'Blue Sweater', 22)
    i2 = Item('WXYZ-9876', 'Red Pants', 36)

    print(repr(i1))
    print(repr(i2))

    if i1 == i2:
        print('These are the same item')
    else:
        print('These items are different')

if __name__ == "__main__":    main()