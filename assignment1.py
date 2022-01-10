'''
Write a function called `geq` which accepts two arguments `a` and `b`, in that order.
If `a` is greater than or equal to `b` it returns true otherwise it returns false.
'''
def geq(a, b):
    if a >= b:
        return True
    else:
        return False

'''
Write a function called `logical_mess` that accepts 3 arguments in the order `a`, `b`, `c`.

Whichever of the following conditions is encountered first should determine the return value of the function.

i.   If any one or more of the arguments are `None` the function should return -1. (None is NULL in Python)
ii.  If any two or more of the arguments are equal it should return 1.
iii. If all three arguments are equal it should return 2.
iv.  If `a` is greater than `b` and `b` is greater than `c` it should return 3.
v.   If `c` is equal to 10 and `a` is not equal to 5 it should return 4.
vi.  If `c` is equal to 10 and `a` is equal to 5 it should return 5.
vii. Otherwise return 6.
'''
def logical_mess(a, b, c):
    if a == None or b == None or c == None:
        return -1
    if a == b or a == c or b == c:
        return 1
    if a == b == c:
        return 2
    if a > b and b > c:
        return 3
    if c == 10 and a != 5:
        return 4
    if c == 10 and a == 5:
        return 5
    else:
        return 6 

'''
Create an Adventurer class. The class name should be Adventurer.
It should have the following properties:

gold - an integer that describes how much gold the adventurer has, it should never go below zero.
inventory - a list of items represented as strings in the adventurers inventory
name - a string representing the adventurer's name.
 
It should have the following methods:

Constructor ( str, int) - this will set the adventurers name and starting gold respectively.
  If starting gold is negative it should be set to 0.
lose_gold( int ) - this will cause the adventurer to lose gold the amount of gold specified but never
  go below zero. If it tries to go below zero it should set the adventurer's gold to zero and return
  False, otherwise it should return True.
win_gold( int ) - this will cause the adventurer to gain the amount of gold specified.
add_inventory( str ) - this will add the string to the adventurers inventory
remove_inventory( str ) - this will remove at most one copy of an item from the adventurer's
  inventory. It should return True if it removed an item or False if the item was not found
'''
class Adventurer:
  def __init__(self, name, gold):
    self.gold = gold
    if self.gold < 0:
        self.gold = 0
    self.inventroy = []
    self.name = name

  def test_gold(self, lose_gold):
    self.lose_gold = lose_gold
    if self.gold - self.lose_gold < 0:
        self.gold = 0
        return False
    else:
        self.gold = self.gold - self.lose_gold
        return True
  
  def test_wingold(self, win_gold):
      self.win_gold = win_gold
      self.gold = self.gold + self.win_gold
      return self.gold

  def test_add_inv(self, add_inventory):
      self.inventroy.append(add_inventory)

  def method_empty_inv(self, remove_inventory):
    if remove_inventory in self.inventroy:
        self.inventroy.remove(remove_inventory)
        return True
    else:
        return False
