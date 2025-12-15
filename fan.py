"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #2 (25 points)
Filename: fan.py

Complete the Fan class and functions below to keep track of the state of the fan.
Ensure that fields are limited to only the defined state and that a constructor
is provided.

State
    Brand (string) - the brand name of the fan
    Is On (boolean) - keeps track whether or not the fan is on
    Spped (integer) - the speed of the current fan

Constructor: 
    Accepts a brand name.  The fan should default to off and a speed of 0
"""
class Fan:
    __slots__ = ['brand', 'speed', 'on']
    def __init__(self, brand, speed = 0, on = False):
        self.brand = brand
        self.speed = speed
        self.on = on

    def turn_on(self):
        if 1 <= self.speed <= 10 and self.on == True:
            return True
        else:
            return False
    
    def turn_off(self):
        if self.on == False:
            self.speed = 0

    def get_state(self):
        return (self.brand, self.on, self.speed)
    
    def __str__(self):
        return "(" + self.brand + ", " + str(self.on) + ", " + str(self.speed) + ")"

"""
Complete the get_state function below.
Parameters:     fan - a fan object
Returns:    Tuple - in the form of (brand, is on, speed)
Example:
    fan = Fan("Holmes")
    get_state(fan) returns ("Holmes", False, 0)
    turn_on(fan,3)
    get_state(fan) returns ("Holmes", True, 3)
More test cases in main() method
"""

def main():
    fan = Fan("Holmes")
    print(fan)
    assert Fan.get_state(fan) == ("Holmes", False, 0)
    assert Fan.turn_on(fan,3) == True
    assert Fan.get_state(fan) == ("Holmes", True, 3)
    Fan.turn_off(fan)
    assert Fan.get_state(fan) == ("Holmes", False, 0)
    assert Fan.turn_on(fan,5) == True
    assert Fan.get_state(fan) == ("Holmes", True, 5)
    assert Fan.turn_on(fan,11) == False
    assert Fan.get_state(fan) == ("Holmes", True, 5)

if __name__ == "__main__":    main()