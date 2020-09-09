# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def n_to(self):
    if self.name == 'Outside Cave Entrance':
      return 'foyer'
    if self.name == 'Narrow Passage':
      return 'treasure'
    if self.name == 'Foyer':
      return 'overlook'
  def s_to(self):
    if self.name == 'Foyer':
      return 'outside'
    if self.name == 'Grand Overlook':
      return 'foyer'
    if self.name == 'Treasure Chamber':
      return 'narrow'
  def e_to(self):
    if self.name == 'Foyer':
      return 'narrow'
  def w_to(self):
    if self.name == 'Narrow Passage':
      return 'foyer'