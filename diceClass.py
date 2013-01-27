'''
	diceClass.py
	__package__ =  'pyDice10k.py'
	__author__ = 'aMigod666(KyleJRoux)'
	
	the Dice class is really just a fancy list filled
	with Die objects. I made it a class because i wanted
	to give it some custom operator handling. 
	
'''
import random
from dieClass import Die

class Dice(object):
	_dieList = [] 	# global die list
	_handList = []	# global list of created Dice objects
	
	def __init__(self, num=6, sides=6):
	    '''
	    in here we initalize the dice in the current roll
	    a Dice object is really a Roll or a collection of
	    Die objects.
	    
	    we add all dies to the Global die list and all
	    Dice to the global hand list.
	    '''
	    self.numberToRoll = num
	    self.dieSides = sides
	    self.currentRoll = []
	    self.rolled = False
	    Dice._handList.append(self.currentRoll)
	    
	    
        def __str__(self):
            if not(self.rolled):
                return '{0} unrolled dice.'.format(self.numberToRoll)
            else:
                roll  = ' '
                for die in self.currentRoll:
                    roll = str(die) + ' '  +roll
                return roll
                
        def roll(self, num=6):
            self.rolled = True
            for i in range(self.numberToRoll):
                self.currentRoll.append(Die())
            for i in self.currentRoll:
                i.roll()
        
        def _make_face(self):
            if not(self.rolled):
                raise ValueError('No Roll To print. Must call roll first.')
            else:
                face = ' ' 
                message = 'You rolled:\n\n\n \t{0}'
                for i in self.currentRoll:
                    face = str(i.face) + ' ' + face
                
            return message.format(face)
        
        def print_roll(self):
            print self._make_face()
            
        def return_face(self):
            return self.make_face()
            
                    

        
def test():
    aRoll = Dice()
    aRoll.roll()
    print aRoll                   	
    aRoll.print_roll()
	
if __name__ == "__main__":
    test()	
