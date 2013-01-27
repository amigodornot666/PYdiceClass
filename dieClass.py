'''
	diceClass.py
	__package__ =  'pyDice10k'
	__author__ = 'aMigod666(KyleJRoux)
	
	the Die class represents a single dice object
	a Die has a number of sides
	each side has a value
	a die also has a "face" value
	the "face" value is None if
	the Die is not "rolled"
	if the die is "rolled" the 
	face value is what was rolled
'''
import random

class Die(object):
    _faces = [None, 'One', 'Two', 'Three', 'Four', 'Five', 'Six']
    _nums = [None, '1', '2', '3', '4', '5', '6']
    
    def __init__(self, num=None):
        if not(num == None):
            self.numSides = num
        else:
            self.numSides = 6
        self.rolled = False
        self.face = None
    def __str__(self):
        if not(self.rolled):
            return 'Im a {0} sided die'.format(self.numSides)	
        else:
            return Die._nums[self.value]

    def __add__(self, other):
        return self.face + ' ' + other.face
    
    def __len__(self):
        return 1

    def __mul__(self, other):
        v = self.value
        if v == 1:
            return 100
        else:
            return (10 * v)
            
    def roll(self, num=6):
        self.rolled = True
        self.value = random.choice(range(1,7))
        self.face = Die._faces[self.value]
        
            
def test():
    x = Die()
    #print x
    y = Die()
    #3print y	
    x.roll()
    y.roll()
    #z = y + x	
    #print z
    print x
    print y
    #print x + y
    print x * y
    
if __name__ == "__main__":
    test()
    
