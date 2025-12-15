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
        self.__code = ''
        self.__name = ''
        self.__price = 0

    


# manual test from main() method
def main():
    i1 = Item('ABCD-1234', 'Blue Sweater', 22)
    i2 = Item('WXYZ-9876', 'Red Pants', 36)

if __name__ == "__main__":    main()